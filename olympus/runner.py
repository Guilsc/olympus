"""Ephemeral Olympus-owned single-item dispatcher. Linux/main-thread synchronous CLI."""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import signal
import subprocess
import time
import uuid
import yaml

from . import boundaries as b
from .providers import ProviderError

ROOT = Path(__file__).resolve().parents[1]
class EvidenceFinalizationError(OSError):
    """Fixed safe failure with an explicitly incomplete in-memory attempt."""
    def __init__(self, record):
        self.record = record
        self.code = record['error']['code']
        super().__init__('Evidence finalization failed; partial attempt retained')

ISOLATION = dict.fromkeys(('tools', 'context_files', 'soul', 'memory', 'background_review', 'trajectory'), False)
SETTINGS = {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'resolved_provider': 'openai-codex', 'resolved_model': 'gpt-6.1-sol', 'route': 'direct', 'attestation': 'unavailable', 'sampling': 'provider-default (not sent)', 'output_token_limit': 'not sent; byte limit enforced', 'reasoning_effort': 'medium', 'per_call_seconds': 120, 'total_seconds': 360, 'raw_byte_limit': b.LIMIT, 'retries': 0}


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def dump(value):
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True)


@contextmanager
def deadline(seconds):
    old_timer = signal.getitimer(signal.ITIMER_REAL)
    previous = signal.getsignal(signal.SIGALRM)
    outer_first = bool(old_timer[0] and old_timer[0] <= seconds)
    outer_fired = False
    def expired(signum, frame):
        nonlocal outer_fired
        if outer_first:
            outer_fired = True
            if callable(previous):
                previous(signum, frame)
        raise TimeoutError()
    signal.signal(signal.SIGALRM, expired)
    entered = time.monotonic()
    signal.setitimer(signal.ITIMER_REAL, max(0.000001, min(seconds, old_timer[0]) if old_timer[0] else seconds))
    try:
        yield
    finally:
        elapsed = time.monotonic() - entered
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)
        restored = old_timer[1] if outer_fired else max(0.000001, old_timer[0] - elapsed) if old_timer[0] else 0
        signal.setitimer(signal.ITIMER_REAL, restored, old_timer[1])


def envelope(key, raw):
    # Preserve every original character. Only add indentation and a missing final newline.
    indented = ''.join('  ' + line for line in raw.splitlines(keepends=True))
    recovered = ''.join(line[2:] for line in indented.splitlines(keepends=True))
    b.require(recovered == raw, 'Raw transfer text mismatch')
    return key + ':\n' + indented + ('' if raw.endswith('\n') else '\n')


def run(input_raw, evidence_dir, provider, *, approval_authority=None, execution_context_update=None):
    started = time.monotonic()
    destination = Path(evidence_dir).resolve()
    b.require(not destination.is_relative_to(ROOT), 'Evidence must be outside repository')
    destination.mkdir(mode=0o700, parents=False, exist_ok=False)
    record = {'attempt_id': str(uuid.uuid4()), 'started_at': now(), 'start_stage': 'host_input', 'stage': 'host_input', 'outcome': None, 'evidence_kind': provider.evidence_kind, 'configuration': dict(SETTINGS), 'isolation': dict(ISOLATION), 'files': {}, 'calls': [], 'assertions': {}, 'redactions': [], 'storage_complete': False}

    record['configuration'].update(resolved_provider=None, resolved_model=None, route='unknown')
    record['configuration'].update(getattr(provider, 'resolution', {}))
    record['configuration']['request_basis'] = 'desired target sent to adapter; synthetic seam does not execute it'
    record['configuration']['resolution_basis'] = 'adapter-selected route, not physical execution attestation'

    storage_failed = False
    def save(name, data):
        nonlocal storage_failed
        try:
            if isinstance(data, str): data = data.encode('utf-8')
            with (destination / name).open('xb') as f:
                f.write(data)
            record['files'][name] = {'sha256': digest(data), 'bytes': len(data), 'encoding': 'UTF-8' if not name.endswith('.wire') else 'raw bytes'}
        except (Exception, KeyboardInterrupt):
            storage_failed = True
            raise

    def snapshot(name, value):
        save(name, json.dumps(value, ensure_ascii=False, indent=2) + '\n')

    def retain_wire(role, info, wire, metadata):
        info['metadata'] = {k: v for k, v in metadata.items() if k in ('reported_model', 'response_id', 'request_id', 'http_status') and (v is None or type(v) in (str, int))}
        if wire is not None:
            save(role + '.wire', wire[:b.LIMIT])
            info['wire_evidence'] = metadata.get('wire_evidence', {'truncated': len(wire) > b.LIMIT, 'redacted': False, 'sha256_basis': 'saved bounded bytes'})
            if info['wire_evidence'].get('metadata_redacted'):
                record['redactions'].append({'role': role, 'location': 'call metadata', 'kind': 'credential/account value replaced with [REDACTED]'})
            if info['wire_evidence']['redacted']:
                record['redactions'].append({'file': role + '.wire', 'kind': 'credential/account value or boundary prefix replaced with [REDACTED]', 'hash_basis': 'saved sanitized bytes only'})

    def call(role, input_text, validate_input, validate_output):
        record['stage'] = role + '.input'
        parsed_input = b.parse(input_text)
        validate_input(parsed_input)
        save(role + '.system.txt', prompts[role])
        save(role + '.input.yaml', input_text)
        snapshot(role + '.input.json', parsed_input)
        request = {'role': role, 'system': prompts[role], 'input': input_text, 'isolation': dict(ISOLATION), 'provider': SETTINGS['provider'], 'model': SETTINGS['model']}
        remaining = SETTINGS['total_seconds'] - (time.monotonic() - started)
        if remaining <= 0: raise TimeoutError()
        info = {'role': role, 'started_at': now(), 'timeout_seconds': min(SETTINGS['per_call_seconds'], remaining)}
        record['calls'].append(info)
        record['stage'] = role + '.provider'
        try:
            with deadline(info['timeout_seconds']):
                reply = provider.call(request, timeout=info['timeout_seconds'])
        except ProviderError as exc:
            retain_wire(role, info, exc.wire, exc.metadata)
            raise
        finally:
            info['ended_at'] = now()
        record['stage'] = role + '.output'
        b.require(type(reply.raw) is str, 'Provider output must be text')
        output_bytes = reply.raw.encode('utf-8')
        # Retain bounded prefix on oversize output; explicitly record truncation, not repaired output.
        save(role + '.output.yaml', output_bytes[:b.LIMIT])
        info['raw_output_bytes'] = len(output_bytes)
        info['raw_output_sha256'] = digest(output_bytes)
        info['raw_output_truncated'] = len(output_bytes) > b.LIMIT
        retain_wire(role, info, reply.wire, reply.metadata)
        b.require(len(output_bytes) <= b.LIMIT, 'Raw response byte limit')
        value = b.parse(reply.raw)
        snapshot(role + '.output.json', value)
        validate_output(value)
        info['validated'] = True
        return reply.raw, value

    try:
        with deadline(max(0.000001, SETTINGS['total_seconds'] - (time.monotonic() - started))):
            input_bytes = input_raw.encode('utf-8')
            record['host_input_truncated'] = len(input_bytes) > b.LIMIT
            record['host_input_sha256'] = digest(input_bytes)
            record['host_input_bytes'] = len(input_bytes)
            save('host.input.yaml', input_bytes[:b.LIMIT])
            b.require(len(input_raw.encode('utf-8')) <= b.LIMIT, 'Raw input byte limit')
            initial = b.parse(input_raw)
            b.shape(initial, ('initiative',))
            b.initiative(initial['initiative'], allow_empty=True)
            if approval_authority is not None: b.text(approval_authority)
            if execution_context_update is not None:
                b.text(execution_context_update)
                b.require(len(execution_context_update.encode('utf-8')) <= b.LIMIT, 'Context update byte limit')
            snapshot('host.options.json', {'approval_authority': approval_authority, 'execution_context_update': execution_context_update})
            revision = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True, capture_output=True, check=True, timeout=5).stdout.strip()
            record['repository_revision'] = revision
            record['runner_revision'] = {p.name: digest(p.read_bytes()) for p in sorted((ROOT / 'olympus').glob('*.py'))}
            contracts = {}
            for path in sorted((ROOT / 'config').rglob('*.md')):
                data = path.read_bytes()
                name = str(path.relative_to(ROOT))
                contracts[name] = data.decode('utf-8')
                save('contract.' + name.replace('/', '.'), data)
            prompts = {'governor': contracts['config/governor.md'], 'orchestrator': contracts['config/orchestrator.md'], b.OWNER: contracts['config/domains/professional_delivery.md'] + '\n\n' + contracts['config/domain_owners/professional_delivery.md']}
            candidates = []
            for domain, owner in zip(b.DOMAINS, b.OWNERS):
                # Every complete declarative candidate contract is available, never hidden to force Apollo.
                candidates.append({'owner': owner, 'realm': domain, 'responsibility': contracts['config/domains/' + domain + '.md'] + '\n' + contracts['config/domain_owners/' + domain + '.md']})
            gov_raw, gov = call('governor', input_raw, lambda v: (b.shape(v, ('initiative',)), b.initiative(v['initiative'], allow_empty=True)), b.governor)
            if gov['decision'] != 'proceed':
                record['outcome'] = gov['decision']
            else:
                objective = initial['initiative']['objective']
                orch_input = dump(initial) + envelope('governance', gov_raw) + dump({'available_realm_owners': candidates})
                b.require(b.parse(orch_input)['governance'] == gov, 'Governance parsed transfer mismatch')
                record['assertions'].update(governance_raw_text_equal=True, governance_parsed_equal=True)
                plan_raw, plan = call('orchestrator', orch_input, b.orchestrator_input, lambda v: b.orchestrator(v, objective))
                if plan['orchestration_status'] != 'ready':
                    record['outcome'] = plan['orchestration_status']
                elif not b.supported(plan):
                    record['outcome'] = 'unsupported_plan'
                else:
                    assignment = {'canonical_domain': b.DOMAINS[0], 'owner': b.OWNER, 'work_id': plan['initiative_state']['work'][0]['id']}
                    context = initial['initiative'].get('context', '')
                    if execution_context_update is not None:
                        context += '\n\nExplicit host execution-context update (late supplied-data change; original handoff unchanged; conflicts must be surfaced, never invented away):\n' + execution_context_update
                    owner_text = envelope('handoff', plan_raw) + dump({'assignment': assignment, 'dependencies': [], 'approval_authority': approval_authority, 'context': context})
                    b.require(b.parse(owner_text)['handoff'] == plan, 'Handoff parsed transfer mismatch')
                    record['assertions'].update(raw_transfer_text_equal=True, handoff_raw_text_equal=True, handoff_parsed_equal=True)
                    _, result = call(b.OWNER, owner_text, lambda v: b.owner_input(v, objective), lambda v: b.owner_output(v, assignment))
                    record['outcome'] = result['owner_status']
                    record['result'] = result
    except (Exception, KeyboardInterrupt) as exc:
        record['outcome'] = 'technical_failure'
        code = exc.code if isinstance(exc, ProviderError) else 'cancelled' if isinstance(exc, KeyboardInterrupt) else 'timeout' if isinstance(exc, TimeoutError) else 'storage_error' if isinstance(exc, OSError) else 'boundary_error' if isinstance(exc, b.BoundaryError) else 'internal_error'
        record['error'] = {'stage': record['stage'], 'code': code, 'diagnostic': str(exc) if isinstance(exc, (b.BoundaryError, ProviderError)) else code}
    record['ended_at'] = now()
    record['elapsed_seconds'] = time.monotonic() - started
    record['end_stage'] = record['stage']
    record['storage_complete'] = not storage_failed
    try:
        remaining = SETTINGS['total_seconds'] - (time.monotonic() - started)
        if remaining <= 0: raise TimeoutError()
        with deadline(remaining):
            partial = destination / 'record.partial.json'
            with partial.open('x', encoding='utf-8') as f:
                json.dump(record, f, ensure_ascii=False, indent=2)
                f.write('\n')
            partial.rename(destination / 'record.json')
    except (Exception, KeyboardInterrupt) as exc:
        record['storage_complete'] = False
        record['outcome'] = 'technical_failure'
        code = 'timeout' if isinstance(exc, TimeoutError) else 'cancelled' if isinstance(exc, KeyboardInterrupt) else 'storage_error'
        record['error'] = {'stage': 'finalization', 'code': code, 'diagnostic': code}
        record['end_stage'] = 'finalization'
        raise EvidenceFinalizationError(record) from None
    return record
