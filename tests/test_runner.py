from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from seeds import *


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'attempt'

    def run_case(self, replies, **kwargs):
        from olympus.runner import run
        from olympus.providers import RecordingProvider
        p = RecordingProvider([raw(r) if isinstance(r, dict) else r for r in replies])
        record = run(raw({'initiative': INITIATIVE}), self.path, p, approval_authority='Project editor', **kwargs)
        return record, p

    def test_ac1_raw_assignment_evidence_and_isolation(self):
        record, p = self.run_case([GOV, PLAN, RESULT])
        self.assertEqual(record['outcome'], 'review')
        self.assertEqual([c['role'] for c in p.calls], ['governor', 'orchestrator', OWNER])
        from olympus.boundaries import parse
        assignment = parse(p.calls[2]['input'])['assignment']
        self.assertEqual(assignment, {
            'canonical_domain': 'professional_delivery',
            'owner': OWNER,
            'work_id': 'actual_returned_id',
        })
        self.assertEqual(record['result']['owner'], OWNER)
        self.assertEqual(record['result']['canonical_domain'], 'professional_delivery')
        self.assertEqual(parse(p.calls[1]['input'])['governance'], GOV)
        self.assertEqual(parse(p.calls[2]['input'])['handoff'], PLAN)
        self.assertIn('  ' + raw(GOV).replace('\n', '\n  ').rstrip(), p.calls[1]['input'])
        self.assertTrue(all(c['isolation'] == {'tools': False, 'context_files': False, 'soul': False, 'memory': False, 'background_review': False, 'trajectory': False} for c in p.calls))
        self.assertEqual(len(parse(p.calls[1]['input'])['available_realm_owners']), 6)
        self.assertTrue(record['assertions']['raw_transfer_text_equal'])
        self.assertEqual(record['configuration']['attestation'], 'unavailable')
        self.assertEqual(record['evidence_kind'], 'synthetic-recording-provider')
        for name, item in record['files'].items():
            self.assertEqual(hashlib.sha256((self.path / name).read_bytes()).hexdigest(), item['sha256'])
        self.assertEqual(json.loads((self.path / 'record.json').read_text())['outcome'], 'review')
        first = record['attempt_id']
        self.path = self.path.parent / 'second'
        rec2, p2 = self.run_case([{'decision': 'clarify', 'reason': 'What objective?', 'next_owner': None}])
        self.assertNotEqual(first, rec2['attempt_id'])
        self.assertEqual(len(p2.calls), 1)
        self.assertNotIn('actual_returned_id', p2.calls[0]['input'])

    def test_athena_single_item_dispatch(self):
        from olympus.boundaries import parse

        owner = 'research_learning_owner'
        objective = 'Summarize the supplied fictional study note.'
        initiative = {
            'objective': objective,
            'context': 'Supplied note: participants preferred the shorter guide. Use only this note.',
        }
        plan_value = deepcopy(PLAN)
        plan_value['initiative_state']['objective'] = objective
        plan_value['initiative_state']['team'] = {
            'lead_owner': owner,
            'participating_owners': [owner],
        }
        plan_value['initiative_state']['work'][0].update(
            objective='Summarize the supplied note',
            owner=owner,
        )
        result_value = deepcopy(RESULT)
        result_value.update(
            canonical_domain='research_learning',
            owner=owner,
        )
        result_value['result']['content'] = 'Participants preferred the shorter guide.'

        from olympus.runner import run
        from olympus.providers import RecordingProvider
        provider = RecordingProvider([raw(GOV), raw(plan_value), raw(result_value)])
        record = run(
            raw({'initiative': initiative}),
            self.path,
            provider,
            approval_authority='Research editor',
        )

        self.assertEqual(record['outcome'], 'review')
        self.assertEqual([call['role'] for call in provider.calls], [
            'governor', 'orchestrator', owner,
        ])
        assignment = parse(provider.calls[2]['input'])['assignment']
        self.assertEqual(assignment, {
            'canonical_domain': 'research_learning',
            'owner': owner,
            'work_id': 'actual_returned_id',
        })
        self.assertEqual(record['result']['owner'], owner)
        self.assertEqual(record['result']['canonical_domain'], 'research_learning')

    def test_ac2_ac3_ac4_and_other_terminal_states(self):
        for role, status, replies, count in [('governor', 'clarify', [{'decision': 'clarify', 'reason': 'Which objective?', 'next_owner': None}], 1), ('governor', 'stop', [{'decision': 'stop', 'reason': 'Explicit restriction', 'next_owner': None}], 1), ('orchestrator', 'planning', [GOV, plan('planning')], 2), ('orchestrator', 'clarify', [GOV, plan('clarify')], 2), (OWNER, 'clarify', [GOV, PLAN, result('clarify')], 3), (OWNER, 'blocked', [GOV, PLAN, result('blocked')], 3), (OWNER, 'draft', [GOV, PLAN, result('draft')], 3)]:
            self.path = self.path.parent / (role + status)
            rec, p = self.run_case(replies, execution_context_update='Earlier version/change fact explicitly withdrawn; no replacement. Do not invent.')
            self.assertEqual(rec['outcome'], status)
            self.assertEqual(len(p.calls), count)
            if count == 3:
                from olympus.boundaries import parse
                inp = parse(p.calls[-1]['input'])
                self.assertEqual(inp['handoff'], PLAN)
                self.assertIn('withdrawn', inp['context'])

    def test_ac6_bad_output_at_every_boundary_stops_dispatch(self):
        for index in range(3):
            for label, bad in [('fenced', '```yaml\na: b\n```'), ('duplicate', 'a: x\na: x'), ('extra', raw({**[GOV, PLAN, RESULT][index], 'extra': 1})), ('wrong-type', 'reason: []')]:
                self.path = self.path.parent / f'bad{index}{label}'
                rec, p = self.run_case([GOV, PLAN, RESULT][:index] + [bad])
                self.assertEqual(rec['outcome'], 'technical_failure')
                self.assertEqual(len(p.calls), index + 1)
                self.assertIn('error', rec)

    def test_ac8_unsupported_no_owner(self):
        p = deepcopy(PLAN)
        p['initiative_state']['work'].append({**p['initiative_state']['work'][0], 'id': 'second'})
        rec, provider = self.run_case([GOV, p])
        self.assertEqual(rec['outcome'], 'unsupported_plan')
        self.assertEqual(len(provider.calls), 2)

    def test_storage_failure_never_claims_complete(self):
        from unittest.mock import patch
        original = Path.open
        def broken(path, *args, **kwargs):
            if path.name == 'orchestrator.output.yaml':
                raise OSError('injected secret diagnostic')
            return original(path, *args, **kwargs)
        with patch.object(Path, 'open', broken):
            rec, p = self.run_case([GOV, PLAN])
        self.assertEqual(rec['outcome'], 'technical_failure')
        self.assertFalse(rec['storage_complete'])
        self.assertEqual(len(p.calls), 2)
        self.assertNotIn('injected secret', json.dumps(rec))

    def test_nested_deadlines_preserve_total_budget(self):
        import time
        from olympus.runner import deadline
        start = time.monotonic()
        with self.assertRaises(TimeoutError):
            with deadline(.15):
                with deadline(.10):
                    time.sleep(.08)
                time.sleep(.3)
        self.assertLess(time.monotonic() - start, .20)

    def test_oversize_host_input_retains_only_bounded_prefix(self):
        from olympus.runner import run
        from olympus.providers import RecordingProvider
        p = RecordingProvider([])
        rec = run('x' * 1048577, self.path, p)
        self.assertEqual(rec['outcome'], 'technical_failure')
        self.assertLessEqual((self.path / 'host.input.yaml').stat().st_size, 1048576)
        self.assertTrue(rec['host_input_truncated'])
        self.assertEqual(p.calls, [])

    def test_empty_objective_and_distinct_initiatives(self):
        from olympus.runner import run
        from olympus.providers import RecordingProvider
        p = RecordingProvider([raw({'decision': 'clarify', 'reason': 'Which objective?', 'next_owner': None})])
        rec = run(raw({'initiative': {'objective': '', 'context': 'UNIQUE_EMPTY_NO_TASK'}}), self.path, p)
        self.assertEqual(rec['outcome'], 'clarify')
        self.path = self.path.parent / 'different'
        rec2, p2 = self.run_case([GOV, PLAN, RESULT])
        self.assertNotIn('UNIQUE_EMPTY_NO_TASK', repr(p2.calls))
        self.assertNotEqual(rec['attempt_id'], rec2['attempt_id'])

    def test_ac10_failures_no_retry_or_overwrite(self):
        from olympus.runner import run
        from olympus.providers import RecordingProvider, ProviderError
        for i, failure in enumerate([ProviderError('http_429'), ProviderError('model_unavailable'), TimeoutError(), KeyboardInterrupt(), 'x' * (1048576 + 1)]):
            self.path = self.path.parent / str(i)
            rec, p = self.run_case([GOV, failure])
            self.assertEqual(rec['outcome'], 'technical_failure')
            self.assertEqual(len(p.calls), 2)
            self.assertTrue((self.path / 'governor.output.yaml').exists())
        before = (self.path / 'record.json').read_bytes()
        p = RecordingProvider([])
        with self.assertRaises(FileExistsError): run(raw({'initiative': INITIATIVE}), self.path, p)
        self.assertEqual(p.calls, [])
        self.assertEqual(before, (self.path / 'record.json').read_bytes())
