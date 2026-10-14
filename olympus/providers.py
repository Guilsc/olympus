"""Provider seam: requests are fresh, never chat histories or agent instances."""
from copy import deepcopy
from dataclasses import dataclass, field


class ProviderError(RuntimeError):
    """Only a fixed safe code is exposed; transport exception text is never logged."""
    def __init__(self, code, *, wire=None, metadata=None):
        self.code = code if code in ('http_429', 'http_error', 'model_unavailable', 'auth_unavailable', 'transport_error', 'invalid_response', 'response_limit', 'timeout', 'cancelled', 'credential_echo') else 'provider_error'
        self.wire = wire
        self.metadata = metadata or {}
        super().__init__(self.code)


@dataclass
class Reply:
    raw: str
    metadata: dict = field(default_factory=dict)
    wire: bytes | None = None


def native_access_token():
    """Read native singleton credentials only: no refresh/import/pool rotation or writes.

    The general runtime resolver can recover CLI tokens, probe quota and mutate stores.
    Only the native path and pure expiry helper are reused: native store loaders
    can write corrupt backups even when their lock is disabled.
    """
    try:
        import json
        from hermes_cli.auth import _auth_file_path, _codex_access_token_is_expiring
        def strict_pairs(pairs):
            result = {}
            for key, value in pairs:
                if key in result: raise ValueError('duplicate key')
                result[key] = value
            return result
        def invalid_constant(value):
            raise ValueError('non-JSON constant')
        store = json.loads(_auth_file_path().read_text(encoding='utf-8'), object_pairs_hook=strict_pairs, parse_constant=invalid_constant)
        token = store['providers']['openai-codex']['tokens']['access_token']
        if not isinstance(token, str) or not token.strip():
            raise ProviderError('auth_unavailable')
        if _codex_access_token_is_expiring(token, 120):
            raise ProviderError('auth_unavailable')
        return token
    except Exception:
        raise ProviderError('auth_unavailable') from None


def codex_protocol_headers(token):
    """Pure equivalent of native auxiliary_client._codex_cloudflare_headers.

    Pinned to native Hermes implementation inspected for Block 2.1; do not
    import the general auxiliary resolver (refresh/pools are out of scope).
    """
    import base64
    import json
    headers = {'User-Agent': 'codex_cli_rs/0.0.0 (Hermes Agent)', 'originator': 'codex_cli_rs'}
    try:
        payload = token.split('.')[1]
        claims = json.loads(base64.urlsafe_b64decode(payload + '=' * (-len(payload) % 4)))
        account = claims.get('https://api.openai.com/auth', {}).get('chatgpt_account_id')
        if isinstance(account, str) and account: headers['ChatGPT-Account-ID'] = account
    except (ValueError, IndexError, TypeError, AttributeError):
        pass
    return headers


class NativeCodexProvider:
    evidence_kind = 'model-backed-direct-request'
    resolution = {'resolved_provider': 'openai-codex', 'resolved_model': 'gpt-6.1-sol', 'route': 'direct'}
    endpoint = 'https://chatgpt.com/backend-api/codex/responses'

    def __init__(self, *, credential_reader=None, transport=None):
        self.credential_reader = credential_reader or native_access_token
        self.transport = transport

    def call(self, request, timeout):
        import json
        import httpx
        from .boundaries import LIMIT
        if request['provider'] != 'openai-codex' or request['model'] != 'gpt-6.1-sol' or any(request['isolation'].values()):
            raise ProviderError('invalid_response')
        payload = {'model': 'gpt-6.1-sol', 'instructions': request['system'], 'input': [{'role': 'user', 'content': [{'type': 'input_text', 'text': request['input']}]}], 'store': False, 'stream': True, 'reasoning': {'effort': 'medium'}, 'include': []}
        data = bytearray()
        observed = 0
        secrets = []
        metadata = {}
        def evidence():
            safe = bytes(data)
            redacted = False
            # Retain only parseable SSE data events. Malformed/truncated events
            # may conceal escaped secrets; discard the whole event fail-closed.
            retained = []
            malformed_removed = False
            for event in safe.replace(b'\r\n', b'\n').split(b'\n\n'):
                if not event.strip(): continue
                lines = event.splitlines()
                content = b'\n'.join(line[5:].lstrip(b' ') for line in lines if line.startswith(b'data:'))
                try:
                    if any(line and not line.startswith(b'data:') for line in lines):
                        raise ValueError()
                    if content != b'[DONE]': json.loads(content)
                except (ValueError, UnicodeError):
                    retained.append(b'data: [REDACTED]\n\n')
                    redacted = malformed_removed = True
                else:
                    retained.append(event + b'\n\n')
            safe = b''.join(retained)
            # Decode complete JSON strings so mixed/unicode escapes cannot conceal
            # an echoed credential in SSE evidence. Unchanged strings stay exact.
            import re
            def redact_json_string(match):
                nonlocal redacted
                try:
                    value = json.loads(match.group())
                except (ValueError, UnicodeError):
                    return match.group()
                original = value
                for secret in secrets:
                    value = value.replace(secret.decode('utf-8'), '[REDACTED]')
                if value != original:
                    redacted = True
                    return json.dumps(value, ensure_ascii=True).encode('utf-8')
                return match.group()
            safe = re.sub(rb'"(?:[^"\\]|\\.)*"', redact_json_string, safe)
            for secret in secrets:
                if secret in safe:
                    safe = safe.replace(secret, b'[REDACTED]')
                    redacted = True
                # A bounded prefix can end halfway through an echoed credential.
                for size in range(min(len(secret) - 1, len(safe)), 0, -1):
                    if safe.endswith(secret[:size]):
                        safe = safe[:-size] + b'[REDACTED]'
                        redacted = True
                        break
            clean = {}
            metadata_redacted = False
            for key, value in metadata.items():
                if isinstance(value, str):
                    for secret in secrets:
                        if secret.decode('utf-8') in value: metadata_redacted = True
                        value = value.replace(secret.decode('utf-8'), '[REDACTED]')
                clean[key] = value
            clean['wire_evidence'] = {'observed_bytes': observed, 'truncated': observed > LIMIT or len(safe) > LIMIT, 'redacted': redacted, 'malformed_events_removed': malformed_removed, 'metadata_redacted': metadata_redacted, 'sha256_basis': 'saved sanitized bounded bytes, not original wire'}
            return safe[:LIMIT], clean
        def failure(code):
            wire, info = evidence()
            return ProviderError(code, wire=wire, metadata=info)
        try:
            token = self.credential_reader()
            if not isinstance(token, str) or not token:
                raise ProviderError('auth_unavailable')
            headers = codex_protocol_headers(token)
            secrets = [v.encode('utf-8') for v in (token, headers.get('ChatGPT-Account-ID')) if v]
            # No environment proxy, configurable route, follow-redirect or retry behavior.
            with httpx.Client(transport=self.transport, timeout=timeout, trust_env=False, follow_redirects=False) as client:
                with client.stream('POST', self.endpoint, json=payload, headers={**headers, 'Authorization': 'Bearer ' + token, 'Accept': 'text/event-stream', 'Content-Type': 'application/json'}) as response:
                    metadata = {'http_status': response.status_code, 'request_id': response.headers.get('x-request-id')}
                    if response.status_code != 200:
                        raise ProviderError('http_429' if response.status_code == 429 else 'model_unavailable' if response.status_code == 404 else 'http_error')
                    for chunk in response.iter_bytes():
                        observed += len(chunk)
                        data.extend(chunk[:max(0, LIMIT - len(data))])
                        if observed > LIMIT:
                            raise ProviderError('response_limit')
                    wire = bytes(data)
                    completed = []
                    items = {}
                    added = {}
                    deltas = {}
                    for event in wire.decode('utf-8').replace('\r\n', '\n').split('\n\n'):
                        lines = [line[5:].lstrip(' ') for line in event.splitlines() if line.startswith('data:')]
                        if not lines: continue
                        content = '\n'.join(lines)
                        if content == '[DONE]': continue
                        obj = json.loads(content)
                        if obj.get('type') in ('error', 'response.failed', 'response.incomplete'):
                            raise ProviderError('invalid_response')
                        if obj.get('type') in ('response.output_item.added', 'response.output_item.done'):
                            item = obj['item']
                            if item.get('type') not in ('message', 'reasoning'):
                                raise ProviderError('invalid_response')
                            if obj['type'] == 'response.output_item.added':
                                added[obj['output_index']] = item
                            if obj['type'] == 'response.output_item.done':
                                index = obj['output_index']
                                if type(index) is not int or index in items:
                                    raise ProviderError('invalid_response')
                                items[index] = item
                        if obj.get('type') == 'response.output_text.delta':
                            key = (obj['output_index'], obj['content_index'])
                            if not isinstance(obj['delta'], str): raise ProviderError('invalid_response')
                            deltas.setdefault(key, []).append(obj['delta'])
                        if obj.get('type') == 'response.completed': completed.append(obj['response'])
                    if len(completed) != 1 or completed[0].get('status') != 'completed':
                        raise ProviderError('invalid_response')
                    final = completed[0]
                    if isinstance(final.get('output'), list):
                        if sum(item.get('type') == 'message' and item.get('phase') not in ('commentary', 'analysis') for item in final['output']) > 1:
                            raise ProviderError('invalid_response')
                        for item in final['output']:
                            if item.get('type') not in ('message', 'reasoning'):
                                raise ProviderError('invalid_response')
                    text = []
                    final_messages = 0
                    for index, item in added.items():
                        if index not in items and item.get('phase') == 'final_answer':
                            items[index] = {**item, 'content': [{'type': 'output_text', 'text': ''.join(deltas[key])} for key in sorted(deltas) if key[0] == index]}
                    for item in ([items[i] for i in sorted(items)] if items else final.get('output') or []):
                        if item.get('type') == 'reasoning': continue
                        if item.get('type') != 'message' or item.get('role') != 'assistant':
                            raise ProviderError('invalid_response')
                        if item.get('phase') in ('commentary', 'analysis'): continue
                        if item.get('phase') not in (None, 'final_answer'):
                            raise ProviderError('invalid_response')
                        final_messages += 1
                        if final_messages > 1: raise ProviderError('invalid_response')
                        for part in item.get('content', []):
                            if part.get('type') != 'output_text' or not isinstance(part.get('text'), str):
                                raise ProviderError('invalid_response')
                            text.append(part['text'])
                    if not text: raise ProviderError('invalid_response')
                    reported_model = final.get('model')
                    if reported_model is not None and reported_model != 'gpt-6.1-sol':
                        raise ProviderError('model_unavailable')
                    metadata.update(reported_model=reported_model, response_id=final.get('id'))
                    assembled = ''.join(text)
                    if any(secret.decode('utf-8') in assembled for secret in secrets):
                        raise ProviderError('credential_echo')
                    safe_wire, safe_metadata = evidence()
                    return Reply(''.join(text), safe_metadata, safe_wire)
        except ProviderError as exc:
            raise failure(exc.code) from None
        except (httpx.TimeoutException, TimeoutError):
            raise failure('timeout') from None
        except KeyboardInterrupt:
            raise failure('cancelled') from None
        except httpx.HTTPError:
            raise failure('transport_error') from None
        except (ValueError, KeyError, TypeError, AttributeError):
            raise failure('invalid_response') from None


class RecordingProvider:
    evidence_kind = 'synthetic-recording-provider'
    resolution = {'resolved_provider': 'recording-provider', 'resolved_model': 'synthetic', 'route': 'offline-synthetic'}

    def __init__(self, replies):
        self.replies = iter(replies)
        self.calls = []

    def call(self, request, timeout):
        self.calls.append(deepcopy(request))
        reply = next(self.replies)
        if isinstance(reply, BaseException):
            raise reply
        return reply if isinstance(reply, Reply) else Reply(reply, {'reported_model': 'synthetic', 'response_id': 'synthetic'})
