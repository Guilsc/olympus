import base64
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import httpx
from olympus.providers import NativeCodexProvider, ProviderError, native_access_token
from olympus.runner import ISOLATION


def request():
    return {'role': 'governor', 'system': 'contract', 'input': 'initiative: {objective: test}', 'isolation': dict(ISOLATION), 'provider': 'openai-codex', 'model': 'gpt-6.1-sol'}


def event(value):
    return 'data: ' + json.dumps(value) + '\n\n'


class FixTests(unittest.TestCase):
    def test_null_terminal_reconstructs_final_items_not_commentary(self):
        text = 'decision: clarify\nreason: Which objective?\nnext_owner: null\n'
        def item(phase, text):
            return {'type': 'message', 'role': 'assistant', 'phase': phase, 'content': [{'type': 'output_text', 'text': text}]}
        for output in [None, []]:
            wire = event({'type': 'response.output_item.done', 'output_index': 0, 'item': item('commentary', 'Not YAML!')}) + event({'type': 'response.output_item.done', 'output_index': 1, 'item': item('final_answer', text)}) + event({'type': 'response.completed', 'response': {'status': 'completed', 'output': output}})
            p = NativeCodexProvider(credential_reader=lambda: 'fake', transport=httpx.MockTransport(lambda r: httpx.Response(200, text=wire)))
            self.assertEqual(p.call(request(), 1).raw, text)

    def test_final_phase_deltas_require_successful_terminal_and_reject_tools(self):
        text = 'decision: clarify\nreason: Which objective?\nnext_owner: null\n'
        prefix = event({'type': 'response.output_item.added', 'output_index': 0, 'item': {'type': 'message', 'role': 'assistant', 'phase': 'commentary'}}) + event({'type': 'response.output_text.delta', 'output_index': 0, 'content_index': 0, 'delta': 'IGNORE'}) + event({'type': 'response.output_item.added', 'output_index': 1, 'item': {'type': 'message', 'role': 'assistant', 'phase': 'final_answer'}}) + event({'type': 'response.output_text.delta', 'output_index': 1, 'content_index': 0, 'delta': text})
        terminal = event({'type': 'response.completed', 'response': {'status': 'completed'}})
        p = lambda wire: NativeCodexProvider(credential_reader=lambda: 'fake', transport=httpx.MockTransport(lambda r: httpx.Response(200, text=wire)))
        self.assertEqual(p(prefix + terminal).call(request(), 1).raw, text)
        for suffix in ['', event({'type': 'response.failed'}), event({'type': 'response.incomplete'}), event({'type': 'response.output_item.done', 'output_index': 2, 'item': {'type': 'function_call'}}) + terminal]:
            with self.subTest(suffix=suffix), self.assertRaises(ProviderError): p(prefix + suffix).call(request(), 1)

    def test_multiple_final_messages_rejected_not_concatenated(self):
        def item(text):
            return {'type': 'message', 'role': 'assistant', 'phase': 'final_answer', 'content': [{'type': 'output_text', 'text': text}]}
        first, second = item('decision: clarify\n'), item('reason: Which?\nnext_owner: null\n')
        done = event({'type': 'response.output_item.done', 'output_index': 0, 'item': first})
        for prefix, output in [('', [first, second]), (done, [first, second]), (done + event({'type': 'response.output_item.done', 'output_index': 1, 'item': second}), None)]:
            with self.subTest(output=output):
                wire = prefix + event({'type': 'response.completed', 'response': {'status': 'completed', 'output': output}})
                p = NativeCodexProvider(credential_reader=lambda: 'fake', transport=httpx.MockTransport(lambda r: httpx.Response(200, text=wire)))
                with self.assertRaises(ProviderError): p.call(request(), 1)
        first['content'] += second['content']
        wire = event({'type': 'response.completed', 'response': {'status': 'completed', 'output': [first]}})
        p = NativeCodexProvider(credential_reader=lambda: 'fake', transport=httpx.MockTransport(lambda r: httpx.Response(200, text=wire)))
        self.assertEqual(p.call(request(), 1).raw, 'decision: clarify\nreason: Which?\nnext_owner: null\n')

    def test_native_protocol_headers(self):
        token = 'x.' + base64.urlsafe_b64encode(json.dumps({'https://api.openai.com/auth': {'chatgpt_account_id': 'FAKE_ACCOUNT'}}).encode()).decode().rstrip('=') + '.x'
        seen = []
        def handler(r):
            seen.append(r)
            return httpx.Response(429, text='not persisted')
        p = NativeCodexProvider(credential_reader=lambda: token, transport=httpx.MockTransport(handler))
        with self.assertRaises(ProviderError): p.call(request(), 1)
        self.assertEqual(seen[0].headers.get('originator'), 'codex_cli_rs')
        self.assertEqual(seen[0].headers.get('User-Agent'), 'codex_cli_rs/0.0.0 (Hermes Agent)')
        self.assertEqual(seen[0].headers.get('ChatGPT-Account-ID'), 'FAKE_ACCOUNT')

    def test_stream_failures_retain_safe_bounded_partial_evidence(self):
        from olympus.runner import run
        from seeds import raw, INITIATIVE
        token = 'FAKE_SECRET_NEVER_RECORD'
        prefix = event({'type': 'response.output_text.delta', 'output_index': 0, 'content_index': 0, 'delta': token})
        class Stream(httpx.SyncByteStream):
            def __init__(self, failure): self.failure = failure
            def __iter__(self):
                yield prefix.encode()
                if self.failure == 'limit': yield b'x' * 1048576
                else: raise self.failure
        for i, (failure, expected) in enumerate([(httpx.ReadError(token), 'transport_error'), (httpx.ReadTimeout(token), 'timeout'), (TimeoutError(token), 'timeout'), (KeyboardInterrupt(token), 'cancelled'), ('limit', 'response_limit')]):
            with self.subTest(code=expected), tempfile.TemporaryDirectory() as temp:
                p = NativeCodexProvider(credential_reader=lambda: token, transport=httpx.MockTransport(lambda r: httpx.Response(200, stream=Stream(failure), headers={'x-request-id': 'req_safe'})))
                path = Path(temp) / 'attempt'
                rec = run(raw({'initiative': INITIATIVE}), path, p)
                self.assertEqual(rec['error']['code'], expected)
                self.assertTrue((path / 'governor.wire').exists())
                self.assertLessEqual((path / 'governor.wire').stat().st_size, 1048576)
                self.assertIn(b'[REDACTED]', (path / 'governor.wire').read_bytes())
                self.assertTrue(rec['redactions'])
                self.assertEqual(rec['calls'][0]['metadata']['request_id'], 'req_safe')
                self.assertEqual(rec['calls'][0]['wire_evidence']['truncated'], expected == 'response_limit')
                self.assertNotIn(token.encode(), b''.join(f.read_bytes() for f in path.iterdir()))

    def test_echoed_credentials_never_persist_even_on_completed_response(self):
        from olympus.runner import run
        from seeds import raw, INITIATIVE
        token = 'FAKE_SECRET_NEVER_RECORD'
        output = 'decision: clarify\nreason: ' + token + '\nnext_owner: null\n'
        wire = event({'type': 'response.completed', 'response': {'status': 'completed', 'id': token, 'output': [{'type': 'message', 'role': 'assistant', 'content': [{'type': 'output_text', 'text': output}]}]}})
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'attempt'
            p = NativeCodexProvider(credential_reader=lambda: token, transport=httpx.MockTransport(lambda r: httpx.Response(200, text=wire, headers={'x-request-id': token})))
            rec = run(raw({'initiative': INITIATIVE}), path, p)
            self.assertEqual(rec['error']['code'], 'credential_echo')
            self.assertNotIn(token.encode(), b''.join(f.read_bytes() for f in path.iterdir()))
            self.assertTrue(rec['redactions'])
            self.assertFalse((path / 'governor.output.yaml').exists())

    def test_exact_system_prompt_and_individual_raw_transfer_evidence(self):
        import hashlib
        from olympus.runner import run
        from olympus.providers import RecordingProvider
        from seeds import raw, INITIATIVE, GOV, PLAN, RESULT
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'attempt'
            p = RecordingProvider([raw(GOV), raw(PLAN), raw(RESULT)])
            rec = run(raw({'initiative': INITIATIVE}), path, p)
            for call in p.calls:
                name = call['role'] + '.system.txt'
                self.assertEqual((path / name).read_bytes(), call['system'].encode('utf-8'))
                self.assertEqual(rec['files'][name]['sha256'], hashlib.sha256(call['system'].encode('utf-8')).hexdigest())
            self.assertTrue(rec['assertions']['governance_raw_text_equal'])
            self.assertTrue(rec['assertions']['handoff_raw_text_equal'])

    def test_synthetic_resolution_does_not_claim_native_model(self):
        from olympus.runner import run
        from olympus.providers import RecordingProvider
        from seeds import raw, INITIATIVE
        with tempfile.TemporaryDirectory() as temp:
            rec = run(raw({'initiative': INITIATIVE}), Path(temp) / 'attempt', RecordingProvider(['decision: clarify\nreason: Which objective?\nnext_owner: null\n']))
            self.assertEqual(rec['configuration']['provider'], 'openai-codex')
            self.assertEqual(rec['configuration']['model'], 'gpt-6.1-sol')
            self.assertEqual(rec['configuration']['resolved_provider'], 'recording-provider')
            self.assertEqual(rec['configuration']['resolved_model'], 'synthetic')
            self.assertEqual(rec['configuration']['route'], 'offline-synthetic')
            self.assertEqual(rec['configuration']['resolution_basis'], 'adapter-selected route, not physical execution attestation')

    def test_json_escaped_credential_echo_is_redacted_and_http_body_omitted(self):
        from olympus.runner import run
        from seeds import raw, INITIATIVE
        token = 'FAKE_SECRET_NEVER_RECORD'
        escaped = ''.join('\\u%04x' % ord(c) for c in token)
        wire = 'data: {"type":"error","message":"' + escaped + '"}\n\n'
        for status in [200, 401, 429]:
            with self.subTest(status=status), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / 'attempt'
                p = NativeCodexProvider(credential_reader=lambda: token, transport=httpx.MockTransport(lambda r: httpx.Response(status, text=wire)))
                rec = run(raw({'initiative': INITIATIVE}), path, p)
                saved = (path / 'governor.wire').read_bytes()
                self.assertNotIn(escaped.encode(), saved)
                self.assertEqual(rec['calls'][0]['metadata']['http_status'], status)
                if status != 200: self.assertEqual(saved, b'')
                else: self.assertIn(b'[REDACTED]', saved)

    def test_terminal_tool_items_rejected_even_when_done_message_exists(self):
        wire = event({'type': 'response.output_item.done', 'output_index': 0, 'item': {'type': 'message', 'role': 'assistant', 'content': [{'type': 'output_text', 'text': 'decision: clarify'}]}}) + event({'type': 'response.completed', 'response': {'status': 'completed', 'output': [{'type': 'function_call', 'name': 'unexpected'}]}})
        p = NativeCodexProvider(credential_reader=lambda: 'fake', transport=httpx.MockTransport(lambda r: httpx.Response(200, text=wire)))
        with self.assertRaises(ProviderError): p.call(request(), 1)

    def test_metadata_redactions_are_labeled(self):
        from olympus.runner import run
        from seeds import raw, INITIATIVE
        token = 'FAKE_SECRET_NEVER_RECORD'
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'attempt'
            p = NativeCodexProvider(credential_reader=lambda: token, transport=httpx.MockTransport(lambda r: httpx.Response(401, text=token, headers={'x-request-id': token})))
            rec = run(raw({'initiative': INITIATIVE}), path, p)
            self.assertTrue(rec['redactions'])
            self.assertEqual(rec['calls'][0]['metadata']['request_id'], '[REDACTED]')
            self.assertNotIn(token, json.dumps(rec))

    def test_unterminated_json_credential_echo_is_redacted(self):
        token = 'FAKE_SECRET_NEVER_RECORD'
        wire = b'data: {"message":"' + ''.join('\\u%04x' % ord(c) for c in token).encode()
        p = NativeCodexProvider(credential_reader=lambda: token, transport=httpx.MockTransport(lambda r: httpx.Response(200, content=wire)))
        with self.assertRaises(ProviderError) as exc: p.call(request(), 1)
        self.assertIn(b'[REDACTED]', exc.exception.wire)
        self.assertTrue(exc.exception.metadata['wire_evidence']['malformed_events_removed'])
        self.assertNotIn(b'\\u0046', exc.exception.wire)

    def test_malformed_escaped_account_event_preserves_only_safe_prior_wire(self):
        from olympus.runner import run
        account = 'FAKE_PRIVATE_ACCOUNT'
        token = 'x.' + base64.urlsafe_b64encode(json.dumps({'https://api.openai.com/auth': {'chatgpt_account_id': account}}).encode()).decode().rstrip('=') + '.x'
        prior = event({'type': 'response.created', 'response': {'id': 'safe'}}).encode()
        escaped = ''.join('\\u%04x' % ord(c) for c in account).encode()
        for tail in [b'data: {"message":"' + escaped, b'data: {"message":"' + escaped + b'\\u00', b'data: {"message":"' + escaped + b'\\q"}\n\n']:
            with self.subTest(tail=tail), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'attempt'
                p = NativeCodexProvider(credential_reader=lambda: token, transport=httpx.MockTransport(lambda r: httpx.Response(200, content=prior + tail)))
                record = run('initiative: {objective: test}', path, p)
                saved = (path / 'governor.wire').read_bytes()
                self.assertTrue(saved.startswith(prior))
                self.assertIn(b'[REDACTED]', saved)
                self.assertNotIn(escaped, saved)
                self.assertNotIn(account.encode(), saved)
                self.assertTrue(record['redactions'])

    def test_invalid_stores_are_read_only(self):
        from hermes_cli import auth
        expired = 'x.' + base64.urlsafe_b64encode(b'{"exp":1}').decode().rstrip('=') + '.x'
        for content in [None, b'{invalid', json.dumps({'providers': {'openai-codex': {'tokens': {'access_token': expired}}}}).encode()]:
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / 'auth.json'
                if content is not None: path.write_bytes(content)
                before = {p.name: p.read_bytes() for p in Path(temp).iterdir()}
                with patch.object(auth, '_auth_file_path', return_value=path):
                    with self.assertRaises(ProviderError): native_access_token()
                self.assertEqual({p.name: p.read_bytes() for p in Path(temp).iterdir()}, before)
