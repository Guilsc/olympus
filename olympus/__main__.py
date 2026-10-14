"""Explicit local invocation; no service, agent loop, retries or fallback."""
import argparse
import json
from pathlib import Path
import sys

from .boundaries import BoundaryError, LIMIT, parse, shape, text
from .providers import NativeCodexProvider, RecordingProvider
from .runner import EvidenceFinalizationError, run


def read_text(path):
    with Path(path).open('rb') as stream:
        data = stream.read(LIMIT + 1)
    if len(data) > LIMIT:
        raise BoundaryError('Input file exceeds 1 MiB')
    return data.decode('utf-8')


def main(argv=None):
    parser = argparse.ArgumentParser(description='Olympus Block 2.1 single-item local runner. Native direct openai-codex/gpt-6.1-sol; no retries.')
    parser.add_argument('--input', required=True, help='UTF-8 YAML initiative mapping')
    parser.add_argument('--record-dir', required=True, help='Fresh directory outside repository; parent must exist')
    parser.add_argument('--approval-authority', help='Supplied label only, NOT authenticated approval (default: null)')
    parser.add_argument('--execution-context-update', help='UTF-8 YAML mapping with exactly context: string, appended only after ready admission')
    parser.add_argument('--recording-replies', help='Offline synthetic seam: JSON list of raw YAML reply strings; never model evidence')
    args = parser.parse_args(argv)
    try:
        input_raw = read_text(args.input)
        update = None
        if args.execution_context_update:
            supplied = parse(read_text(args.execution_context_update))
            shape(supplied, ('context',))
            text(supplied['context'])
            update = supplied['context']
        provider = NativeCodexProvider()
        if args.recording_replies:
            replies = json.loads(read_text(args.recording_replies))
            if type(replies) is not list or not all(type(item) is str for item in replies):
                raise BoundaryError('Recording replies must be a JSON list of raw YAML strings')
            provider = RecordingProvider(replies)
        record = run(input_raw, args.record_dir, provider, approval_authority=args.approval_authority, execution_context_update=update)
        summary = {key: record[key] for key in ('attempt_id', 'outcome', 'evidence_kind', 'end_stage', 'storage_complete')}
        if 'error' in record: summary['error'] = record['error']
        if 'result' in record: summary['result'] = record['result']
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 2 if record['outcome'] == 'technical_failure' else 0
    except EvidenceFinalizationError as exc:
        print('Technical failure: evidence finalization ' + exc.code + '; partial attempt retained; storage incomplete.', file=sys.stderr)
    except FileExistsError:
        print('Technical failure: record directory already exists; no overwrite or provider call.', file=sys.stderr)
    except KeyboardInterrupt:
        print('Technical failure: cancelled.', file=sys.stderr)
    except (OSError, ValueError, UnicodeError):
        print('Technical failure: input/options or evidence storage unavailable; no complete record claimed.', file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
