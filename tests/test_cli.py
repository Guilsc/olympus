import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from seeds import *

PYTHON = '/opt/hermes/.venv/bin/python'
ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def test_cli_recording_and_collision(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'input.yaml').write_text(raw({'initiative': INITIATIVE}))
            (root / 'replies.json').write_text(json.dumps([raw(GOV), raw(PLAN), raw(RESULT)]))
            cmd = [PYTHON, '-m', 'olympus', '--input', str(root / 'input.yaml'), '--record-dir', str(root / 'run'), '--recording-replies', str(root / 'replies.json'), '--approval-authority', 'Project editor']
            p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual(json.loads(p.stdout)['outcome'], 'review')
            self.assertEqual(json.loads((root / 'run/record.json').read_text())['evidence_kind'], 'synthetic-recording-provider')
            p2 = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(p2.returncode, 2)
            self.assertIn('already exists', p2.stderr)

    def test_cli_help_offline(self):
        p = subprocess.run([PYTHON, '-m', 'olympus', '--help'], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(p.returncode, 0)
        self.assertIn('--execution-context-update', p.stdout)
