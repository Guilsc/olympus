"""Restricted third-cycle boundary regressions (offline)."""
from copy import deepcopy
import unittest
import tempfile
import os
import json
from unittest.mock import Mock

import sys
import traceback

from olympus.boundaries import BoundaryError, LIMIT, orchestrator, orchestrator_input, parse
from seeds import GOV, OBJECTIVE, OWNER, PLAN


def empty_clarification():
    value = deepcopy(PLAN)
    value['orchestration_status'] = 'clarify'
    value['reason'] = 'Supply an objective and valid Governor approval.'
    value['next_action'] = {'type': 'request_governance_clarification', 'target': 'governor'}
    s = value['initiative_state']
    s['objective'] = ''
    s['scope'] = {'in': [], 'out': []}
    s['team'] = {'lead_owner': None, 'participating_owners': []}
    for field in ('decisions', 'assumptions', 'work', 'success_criteria', 'requested_contributions'):
        s[field] = []
    s['blockers'] = ['Missing objective and valid Governor approval']
    s['what_happens_first'] = {'action': 'Request governance clarification', 'reason': 'No work authorized'}
    return value


class IntegerParserTests(unittest.TestCase):
    def test_oversized_integer_is_safe_exact_boundary_error(self):
        literal = '9' * 5000
        before = sys.get_int_max_str_digits()
        try:
            parse('x: ' + literal)
        except ValueError as exc:
            self.assertIs(type(exc), BoundaryError)
            self.assertEqual(str(exc), 'Invalid YAML scalar')
            self.assertIsNone(exc.__cause__)
            self.assertTrue(exc.__suppress_context__)
            rendered = ''.join(traceback.format_exception(exc))
            self.assertNotIn(literal, rendered)
            self.assertNotIn('Exceeds the limit', rendered)
            self.assertNotIn('ValueError:', rendered)
        else:
            self.fail('Oversized integer was accepted')
        finally:
            self.assertEqual(sys.get_int_max_str_digits(), before)

    def test_ordinary_integers_and_quoted_long_string_unchanged(self):
        literal = '9' * 5000
        self.assertEqual(parse('x: 42\ny: -7\nz: 0x10'), {'x': 42, 'y': -7, 'z': 16})
        self.assertEqual(parse('x: "' + literal + '"'), {'x': literal})
        for raw, message in (('x: .nan', 'Unsupported YAML scalar'), ('x: 1\nx: 2', 'Duplicate YAML key'), ('x: [', 'Malformed YAML')):
            with self.subTest(message=message), self.assertRaisesRegex(BoundaryError, '^' + message + '$'):
                parse(raw)


class Utf8ParserTests(unittest.TestCase):
    def test_lone_surrogate_is_safe_exact_boundary_error(self):
        for surrogate in (chr(0xD800), chr(0xDFFF)):
            raw = 'x: ' + surrogate
            with self.subTest(codepoint=ord(surrogate)):
                try:
                    parse(raw)
                except ValueError as exc:
                    self.assertIs(type(exc), BoundaryError)
                    self.assertEqual(str(exc), 'YAML must be valid UTF-8 text')
                    self.assertIsNone(exc.__cause__)
                    self.assertTrue(exc.__suppress_context__)
                    rendered = ''.join(traceback.format_exception(exc))
                    self.assertNotIn(raw, rendered)
                    self.assertNotIn(surrogate, rendered)
                    self.assertNotIn('UnicodeEncodeError', rendered)
                else:
                    self.fail('Invalid UTF-8 was accepted')

    def test_escaped_surrogate_is_safe_boundary_error(self):
        raw = 'x: "\\uD800"'
        with self.assertRaisesRegex(BoundaryError, 'Invalid Unicode surrogate'):
            parse(raw)

    def test_valid_unicode_type_and_byte_limits_unchanged(self):
        self.assertEqual(parse('x: ação 漢字 😀'), {'x': 'ação 漢字 😀'})
        for raw, message in ((b'x: 1', 'YAML must be UTF-8 text'), ('x: ' + 'é' * (LIMIT // 2), 'YAML byte limit')):
            with self.subTest(message=message), self.assertRaisesRegex(BoundaryError, '^' + message + '$'):
                parse(raw)


class EmptyObjectiveTests(unittest.TestCase):
    def test_empty_clarification_snapshot_accepted(self):
        orchestrator(empty_clarification(), '')

    def test_original_objective_cannot_be_rewritten_to_empty(self):
        with self.assertRaisesRegex(BoundaryError, 'Original objective changed'):
            orchestrator(empty_clarification(), OBJECTIVE)

    def test_empty_ready_and_planning_rejected(self):
        for status, route in (('ready', ('handoff', 'domain_owner')), ('planning', ('convene_planning_room', 'planning_room'))):
            value = empty_clarification()
            value['orchestration_status'] = status
            value['next_action'] = dict(zip(('type', 'target'), route))
            with self.subTest(status=status), self.assertRaises(BoundaryError):
                orchestrator(value, '')

    def test_empty_clarification_has_no_authorized_state(self):
        populated = {'team': {'lead_owner': OWNER, 'participating_owners': [OWNER]}, 'work': deepcopy(PLAN['initiative_state']['work']), 'decisions': ['Authorize draft'], 'assumptions': ['Approved'], 'success_criteria': ['Draft'], 'requested_contributions': [{'owner': OWNER, 'request': 'Draft'}]}
        for field, content in populated.items():
            value = empty_clarification()
            value['initiative_state'][field] = content
            with self.subTest(field=field), self.assertRaises(BoundaryError):
                orchestrator(value, '')

    def test_empty_clarification_still_requires_blocker_and_governor_route(self):
        for mutation in ('blockers', 'route'):
            value = empty_clarification()
            if mutation == 'blockers':
                value['initiative_state']['blockers'] = []
            else:
                value['next_action']['target'] = 'planning_room'
            with self.subTest(mutation=mutation), self.assertRaises(BoundaryError):
                orchestrator(value, '')

    def test_runtime_input_and_governance_gates_unchanged(self):
        for objective, decision in (('', 'proceed'), (OBJECTIVE, 'stop'), (OBJECTIVE, 'clarify')):
            value = {'initiative': {'objective': objective}, 'governance': {**GOV, 'decision': decision}, 'available_realm_owners': []}
            with self.subTest(objective=objective, decision=decision), self.assertRaises(BoundaryError):
                orchestrator_input(value)


class RunnerUnicodeTests(unittest.TestCase):
    def test_runner_rejects_config_with_escaped_surrogate(self):
        from olympus.runner import run
        # Use /tmp to ensure evidence is outside the repo
        with tempfile.TemporaryDirectory() as tmpdir:
            f_path = os.path.join(tmpdir, 'config.yaml')
            with open(f_path, 'w') as f:
                f.write('initiative:\n  objective: "\\uD800"\n')
            
            evidence_dir = os.path.join(tmpdir, 'evidence')
            mock_provider = Mock()
            mock_provider.evidence_kind = 'mock'
            mock_provider.resolution = {}
            
            # Executar runner
            run(open(f_path).read(), evidence_dir, mock_provider)
            
            # Conferir registro
            with open(os.path.join(evidence_dir, 'record.json'), 'r') as f:
                record = json.load(f)
            
            self.assertEqual(record['outcome'], 'technical_failure')
            self.assertEqual(record['error']['code'], 'boundary_error')
            self.assertTrue(record['storage_complete'])
            self.assertEqual(len(record['calls']), 0)
