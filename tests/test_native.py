import json
import unittest
import httpx
from olympus.providers import ProviderError


class NativeAdapterTests(unittest.TestCase):
    def request(self):
        from olympus.runner import ISOLATION
        return {'role': 'governor', 'system': 'Only role contract', 'input': 'initiative:\n  objective: test\n', 'isolation': dict(ISOLATION), 'provider': 'openai-codex', 'model': 'gpt-6.1-sol'}

    def test_direct_responses_request_completed_only_no_tools_or_context(self):
        from olympus.providers import NativeCodexProvider
        seen = []
        def handler(request):
            seen.append(request)
            body = json.loads(request.content)
            self.assertEqual(body['model'], 'gpt-6.1-sol')
            self.assertFalse(body['store'])
            self.assertTrue(body['stream'])
            self.assertEqual(body['instructions'], 'Only role contract')
            self.assertEqual(body['input'], [{'role': 'user', 'content': [{'type': 'input_text', 'text': self.request()['input']}]}])
            for key in ('tools', 'previous_response_id', 'conversation', 'prompt_cache_key', 'temperature', 'max_output_tokens'):
                self.assertNotIn(key, body)
            response = {'id': 'resp_mock', 'model': 'gpt-6.1-sol', 'status': 'completed', 'output': [{'type': 'message', 'role': 'assistant', 'content': [{'type': 'output_text', 'text': 'decision: clarify\nreason: Which objective?\nnext_owner: null\n'}]}]}
            return httpx.Response(200, text='data: ' + json.dumps({'type': 'response.completed', 'response': response}) + '\n\n', headers={'x-request-id': 'req_mock'})
        p = NativeCodexProvider(credential_reader=lambda: 'FAKE_SECRET_NEVER_RECORD', transport=httpx.MockTransport(handler))
        reply = p.call(self.request(), 10)
        self.assertEqual(len(seen), 1)
        self.assertEqual(str(seen[0].url), 'https://chatgpt.com/backend-api/codex/responses')
        self.assertEqual(reply.metadata['reported_model'], 'gpt-6.1-sol')
        self.assertNotIn('FAKE_SECRET_NEVER_RECORD', repr(reply))

    def test_http_error_and_incomplete_no_retry(self):
        from olympus.providers import NativeCodexProvider
        for status, text, expected in [(429, 'secret upstream', 'http_429'), (404, 'missing model', 'model_unavailable'), (200, 'data: {"type":"response.incomplete"}\n\n', 'invalid_response'), (200, 'x' * 1048577, 'response_limit')]:
            count = []
            def handler(request):
                count.append(1)
                return httpx.Response(status, text=text)
            p = NativeCodexProvider(credential_reader=lambda: 'fake', transport=httpx.MockTransport(handler))
            with self.assertRaises(ProviderError) as error: p.call(self.request(), 1)
            self.assertEqual(error.exception.code, expected)
            self.assertEqual(len(count), 1)
