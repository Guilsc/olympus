import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx

from olympus.providers import HermesCustomProvider, ProviderError, native_custom_connection


class CustomProviderTests(unittest.TestCase):
    def request(self):
        from olympus.runner import ISOLATION
        return dict(role='governor', system='Contract only', input='initiative: fictional',
                    isolation=dict(ISOLATION), provider='custom:unified-routing', model='routing-model')

    def provider(self, handler):
        return HermesCustomProvider('custom:unified-routing', 'routing-model',
            connection_reader=lambda name: ('https://example.test/v1', 'TEST_SECRET_NEVER_SAVE'),
            transport=httpx.MockTransport(handler))

    def test_single_isolated_chat_call_and_honest_routed_model(self):
        seen = []
        def handler(request):
            seen.append(request)
            self.assertEqual(str(request.url), 'https://example.test/v1/chat/completions')
            self.assertEqual(json.loads(request.content), {
                'model': 'routing-model', 'messages': [
                    {'role': 'system', 'content': 'Contract only'},
                    {'role': 'user', 'content': 'initiative: fictional'}], 'stream': False})
            return httpx.Response(200, json={'id': 'reply', 'model': 'reported-downstream-model',
                'choices': [{'index': 0, 'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'decision: clarify'}}]})
        p = self.provider(handler)
        reply = p.call(self.request(), 1)
        self.assertEqual(len(seen), 1)
        self.assertEqual(reply.metadata['reported_model'], 'reported-downstream-model')
        self.assertEqual(p.resolution['resolved_provider'], 'custom:unified-routing')
        self.assertEqual(p.resolution['resolved_model'], 'routing-model')
        self.assertNotIn('TEST_SECRET_NEVER_SAVE', repr(reply))

    def test_failures_no_retry_or_unsanitized_wire(self):
        cases = [
            (401, {'error': 'TEST_SECRET_NEVER_SAVE'}, 'http_error'),
            (429, {}, 'http_429'),
            (404, {}, 'model_unavailable'),
            (200, {'choices': [{'finish_reason': 'length', 'message': {'role': 'assistant', 'content': 'partial'}}]}, 'invalid_response'),
            (200, {'choices': [{'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'ok', 'tool_calls': [{}]}}]}, 'invalid_response'),
            (200, {'choices': [{'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'TEST_SECRET_NEVER_SAVE'}}]}, 'credential_echo'),
            (200, {}, 'invalid_response'),
        ]
        for status, body, code in cases:
            with self.subTest(code=code):
                seen = []
                def handler(request):
                    seen.append(1)
                    return httpx.Response(status, json=body)
                with self.assertRaises(ProviderError) as caught:
                    self.provider(handler).call(self.request(), 1)
                self.assertEqual(caught.exception.code, code)
                self.assertEqual(len(seen), 1)
                self.assertNotIn('TEST_SECRET_NEVER_SAVE', repr(caught.exception.wire))

    def test_size_timeout_and_malformed_fail_closed(self):
        for kind, expected in [('size', 'response_limit'), ('timeout', 'timeout'), ('malformed', 'invalid_response')]:
            seen = []
            def handler(request):
                seen.append(1)
                if kind == 'timeout': raise httpx.ReadTimeout('TEST_SECRET_NEVER_SAVE')
                return httpx.Response(200, content=b'x' * (1048577 if kind == 'size' else 10))
            with self.assertRaises(ProviderError) as caught:
                self.provider(handler).call(self.request(), 1)
            self.assertEqual(caught.exception.code, expected)
            self.assertEqual(caught.exception.wire, None)
            self.assertEqual(len(seen), 1)

    def test_request_mismatch_and_isolation_fail_before_connection(self):
        for field, value in [('provider', 'openai-codex'), ('model', 'other'), ('isolation', {'tools': True})]:
            request = self.request()
            request[field] = value
            with self.assertRaises(ProviderError):
                self.provider(lambda r: self.fail('unexpected HTTP')).call(request, 1)

    def test_native_resolution_uses_hermes_resolver_and_limits_http_to_loopback(self):
        from hermes_cli import runtime_provider
        template = dict(provider='custom:unified-routing', base_url='http://127.0.0.1:8123/v1',
                        api_key='TEST_SECRET_NEVER_SAVE', api_mode='chat_completions')
        with patch.object(runtime_provider, 'resolve_runtime_provider', return_value=template):
            self.assertEqual(native_custom_connection('custom:unified-routing'),
                             ('http://127.0.0.1:8123/v1', 'TEST_SECRET_NEVER_SAVE'))
        for url in ('http://example.test/v1', 'http://192.0.2.1/v1'):
            with self.subTest(url=url), patch.object(runtime_provider, 'resolve_runtime_provider',
                                                    return_value=dict(template, base_url=url)):
                with self.assertRaises(ProviderError) as caught:
                    native_custom_connection('custom:unified-routing')
                self.assertEqual(caught.exception.code, 'insecure_remote_endpoint')
        with patch.object(runtime_provider, 'resolve_runtime_provider',
                          return_value=dict(template, base_url='https://example.test/v1')):
            self.assertEqual(native_custom_connection('custom:unified-routing')[0], 'https://example.test/v1')

    def test_exact_authorized_router_endpoint_only(self):
        from hermes_cli import runtime_provider
        template = dict(provider='custom', requested_provider='custom:unified-routing',
                        base_url='http://unified-router-v1:20139/v1',
                        api_key='TEST_SECRET_NEVER_SAVE', api_mode='chat_completions')
        with patch.object(runtime_provider, 'resolve_runtime_provider', return_value=template):
            self.assertEqual(native_custom_connection('custom:unified-routing'),
                             (template['base_url'], template['api_key']))
        for endpoint in ('http://unified-router-v1:20140', 'http://unified-router-v1',
                         'http://unified-router-v1.evil:20139/v1', 'http://192.0.2.1:20139'):
            with self.subTest(endpoint=endpoint), patch.object(runtime_provider, 'resolve_runtime_provider',
                    return_value=dict(template, base_url=endpoint)):
                with self.assertRaises(ProviderError) as caught:
                    native_custom_connection('custom:unified-routing')
                self.assertEqual(caught.exception.code, 'insecure_remote_endpoint')

    def test_runner_metadata_and_request_use_actual_custom_target(self):
        from olympus.runner import run
        from seeds import INITIATIVE, raw
        def handler(request):
            self.assertEqual(json.loads(request.content)['model'], 'routing-model')
            return httpx.Response(200, json={'model': 'reported', 'choices': [{'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'decision: clarify\nreason: Specify scope\nnext_owner: null\n'}}]})
        with tempfile.TemporaryDirectory() as temp:
            record = run(raw({'initiative': INITIATIVE}), Path(temp) / 'fresh', self.provider(handler))
        self.assertEqual(record['outcome'], 'clarify')
        self.assertEqual(record['configuration']['provider'], 'custom:unified-routing')
        self.assertEqual(record['configuration']['model'], 'routing-model')
        self.assertEqual(record['configuration']['reasoning_effort'], 'provider-default (not sent)')
        self.assertTrue(record['storage_complete'])
