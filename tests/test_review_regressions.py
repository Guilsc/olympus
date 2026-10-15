"""Independent runner review regressions; no provider/network calls."""
import pathlib
import tempfile
import time
import unittest
from unittest.mock import patch
import yaml
from olympus.providers import RecordingProvider
from olympus.runner import deadline, run


class RunnerReviewRegressions(unittest.TestCase):
    def test_inner_deadline_never_relaxes_shorter_outer_budget(self):
        started = time.monotonic()
        with self.assertRaises(TimeoutError):
            with deadline(0.04):
                with deadline(1):
                    time.sleep(0.08)
        self.assertLess(time.monotonic() - started, 0.065, 'Inner deadline must respect the already-active outer budget')

    def test_storage_interruption_never_claims_complete_record(self):
        original = pathlib.Path.open
        def interrupted(path, *args, **kwargs):
            if path.name == 'host.input.yaml':
                raise TimeoutError()
            return original(path, *args, **kwargs)
        with tempfile.TemporaryDirectory() as directory:
            provider = RecordingProvider([])
            with patch.object(pathlib.Path, 'open', interrupted):
                record = run(yaml.safe_dump({'initiative': {'objective': 'Fictional text'}}), pathlib.Path(directory) / 'attempt', provider)
            self.assertEqual(record['outcome'], 'technical_failure')
            self.assertEqual(record['error']['code'], 'timeout')
            self.assertFalse(record['storage_complete'], 'Timeout during evidence persistence is an incomplete record')
            self.assertEqual(provider.calls, [])


class GovernanceInputRegressions(unittest.TestCase):
    def test_optional_input_route_does_not_relax_governor_output(self):
        from olympus import boundaries as b
        value = {'initiative': {'objective': 'test'}, 'governance': {'decision': 'proceed', 'reason': 'bounded'}, 'available_realm_owners': []}
        b.orchestrator_input(value)
        for governance in [{'decision': 'proceed', 'reason': 'bounded'}, {'decision': 'proceed', 'reason': 'bounded', 'next_owner': None}, {'decision': 'proceed', 'reason': 'bounded', 'next_owner': 'orchestrator', 'extra': True}]:
            with self.subTest(governance=governance):
                with self.assertRaises(b.BoundaryError): b.governor(governance)
                with tempfile.TemporaryDirectory() as directory:
                    provider = RecordingProvider([yaml.safe_dump(governance)])
                    record = run('initiative: {objective: test}', pathlib.Path(directory) / 'attempt', provider)
                    self.assertEqual(record['outcome'], 'technical_failure')
                    self.assertEqual(len(provider.calls), 1)
        value['governance']['next_owner'] = 'wrong'
        with self.assertRaises(b.BoundaryError): b.orchestrator_input(value)


class FinalizationRegressions(unittest.TestCase):
    def test_cli_finalization_failure_is_safe_and_visible(self):
        import contextlib
        import io
        from olympus import __main__ as cli
        from olympus.runner import EvidenceFinalizationError
        stderr = io.StringIO()
        error = EvidenceFinalizationError({'error': {'code': 'timeout'}, 'storage_complete': False})
        with patch.object(cli, 'read_text', return_value='initiative: {objective: test}'), patch.object(cli, 'run', side_effect=error), contextlib.redirect_stderr(stderr):
            self.assertEqual(cli.main(['--input', 'unused', '--record-dir', 'unused']), 2)
        self.assertIn('finalization timeout', stderr.getvalue())
        self.assertIn('storage incomplete', stderr.getvalue())
        self.assertNotIn('Traceback', stderr.getvalue())

    def test_cancellation_during_intermediate_write_is_incomplete(self):
        original = pathlib.Path.open
        def interrupted(path, *args, **kwargs):
            if path.name == 'host.input.yaml': raise KeyboardInterrupt('unsafe')
            return original(path, *args, **kwargs)
        with tempfile.TemporaryDirectory() as directory, patch.object(pathlib.Path, 'open', interrupted):
            record = run('initiative: {objective: test}', pathlib.Path(directory) / 'attempt', RecordingProvider([]))
        self.assertEqual(record['error']['code'], 'cancelled')
        self.assertFalse(record['storage_complete'])

    def test_final_record_write_obeys_remaining_invocation_budget(self):
        import olympus.runner as runner
        original = runner.json.dump
        def slow(*args, **kwargs):
            time.sleep(0.25)
            return original(*args, **kwargs)
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / 'attempt'
            started = time.monotonic()
            with patch.dict(runner.SETTINGS, total_seconds=0.12), patch.object(runner.json, 'dump', slow):
                with self.assertRaisesRegex(OSError, 'Evidence finalization failed') as caught:
                    run('initiative: {objective: test}', path, RecordingProvider(['decision: clarify\nreason: Missing detail\nnext_owner: null\n']))
            self.assertLess(time.monotonic() - started, 0.22)
            self.assertEqual(caught.exception.record['error']['code'], 'timeout')
            self.assertFalse(caught.exception.record['storage_complete'])
            self.assertEqual(caught.exception.record['outcome'], 'technical_failure')
            self.assertTrue((path / 'host.input.yaml').exists())
            self.assertFalse((path / 'record.json').exists())

    def test_finalization_interruptions_are_safe_visible_failures(self):
        import olympus.runner as runner
        for failure, code in [(TimeoutError('unsafe'), 'timeout'), (KeyboardInterrupt('unsafe'), 'cancelled'), (OSError('unsafe'), 'storage_error')]:
            with self.subTest(code=code), tempfile.TemporaryDirectory() as directory:
                path = pathlib.Path(directory) / 'attempt'
                with patch.object(runner.json, 'dump', side_effect=failure):
                    with self.assertRaisesRegex(OSError, '^Evidence finalization failed; partial attempt retained$') as caught:
                        run('initiative: {objective: test}', path, RecordingProvider(['decision: clarify\nreason: Missing detail\nnext_owner: null\n']))
                self.assertFalse(caught.exception.record['storage_complete'])
                self.assertEqual(caught.exception.record['error']['code'], code)


if __name__ == '__main__':
    unittest.main()
