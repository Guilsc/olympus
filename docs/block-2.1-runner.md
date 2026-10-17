# Block 2.1 — bounded local runner

## Implemented scope and validation status

The `olympus` Python entrypoint implements an ephemeral, synchronous, at-most-three-call chain: Governor → Orchestrator → one supported Domain Owner. All six declarative Owners are supplied to planning. One independent item with no dependencies can execute when Apollo (`professional_delivery_owner`) or Athena (`research_learning_owner`) is the sole participant and Lead Owner. A valid plan selecting another Owner, multiple items or participants, or dependencies terminates as `unsupported_plan`; it is never trimmed. Contracts under `config/` and historical validation remain unchanged. The [planning document](block-2.1-plan.md) is historical proposed scope, not execution evidence.

Offline unittest/recording-provider tests exercise structural gates, assignment, raw transfer, isolation, terminal outcomes and selected failure/resource boundaries. They do **not** prove model behavior, factual fidelity, authority, one-sentence semantics, availability or reliability. Fresh real F1–F4 trials and manual semantic inspection remain outstanding; this fix pass made no live calls. DRAFT/REVIEW is not approval, acceptance, delivery or release.

## Setup and native compatibility

Run from the repository root with an existing Python environment containing `PyYAML` and `httpx`, plus importable native `hermes_cli.auth` for real execution. The reviewed host environment is `/opt/hermes/.venv/bin/python`; no global installs, provider/profile changes or dependency installation are performed by this runner. It requires Linux/POSIX signals and main-thread execution for absolute deadlines. Git must be available for evidence revision lookup.

The direct adapter is pinned to `openai-codex` / `gpt-6.1-sol` and `https://chatgpt.com/backend-api/codex/responses`; it ignores environment proxies and does not follow redirects. It reads strict JSON from native `_auth_file_path()` at `providers.openai-codex.tokens.access_token`, then uses the pure native expiry helper with 120-second skew. Missing, malformed or expiring credentials fail without locks, corrupt backups, CLI credential import, pool rotation or refresh. Expiry interpretation follows that native helper (not independent JWT authenticity validation). Authenticate/renew credentials separately outside this runner; do not put them in fixtures or records.

Protocol headers mirror native `agent/auxiliary_client.py:_codex_cloudflare_headers`: `originator: codex_cli_rs`, `User-Agent: codex_cli_rs/0.0.0 (Hermes Agent)`, and optional JWT-derived `ChatGPT-Account-ID`. This is an inspected compatibility assumption, not a stable public API guarantee. Credential/account headers are not recorded. SSE content is reconstructed from completed output items, or explicitly final-phase deltas; legacy completed output also works. Terminal output may be null/missing. Explicit successful `response.completed` is required; tools, failed/incomplete/error events and EOF without completion fail. Multiple final assistant messages are rejected; only content parts of one final message may be concatenated. Commentary/analysis is not appended to final YAML. There is no YAML repair.

No tools, prior conversation, host context files, soul, memory, background review or trajectory are sent. `store: false` is requested from the provider; that is not an independent guarantee about upstream retention. There are no retries, fallback, resumption, durable Initiative State, persistence engine, external actions or downstream recursion. Local attempt evidence is the only runner-owned storage.

## Input subset and limits

Use a single UTF-8 YAML mapping, with `initiative: {objective: string, context: string}` (context optional). Empty objective is allowed only for Governor clarification admission. Model outputs must match the unchanged role schemas exactly. Restricted YAML accepts string mapping keys, mappings/lists, string/null/bool/int scalars. Duplicate keys, aliases/anchors, explicit tags, complex keys, document markers/directives, multiple documents, floats/timestamps, fences and surrounding prose fail closed. There is no coercion or normalization to rescue an invalid response.

Limits: 1 MiB raw input/output and SSE capture, depth 32 and 20,000 YAML parser events; 120 seconds per call, 360 seconds per invocation. CLI files are bounded before decoding. The SSE buffer is bounded even on transport failure. Limits can reject otherwise legitimate large outputs. No token ceiling is sent; the byte ceiling is enforced locally. Sampling defaults to the provider; reasoning effort is medium.

## Fresh attempts and evidence

Choose an explicit new directory **outside the repository**, with an existing parent. Never reuse an attempt directory: collisions are refused before any call. Preserve failed/partial attempts and select a fresh name for any separately authorized invocation. Records contain raw role inputs/outputs, parsed snapshots, exact assembled `.system.txt` UTF-8 prompt bytes, component contracts, SHA-256 file hashes, runner source hashes, Git revision, call order, assertions and safe stage/error codes. An uncommitted implementation is identified by its source hashes; Git HEAD alone does not identify it.

On provider/timeout/cancel/limit failures, available bounded wire is retained with truncation/redaction metadata. Non-200 HTTP bodies are deliberately not captured; status and safe request-ID metadata suffice. Known sent credential/account values in wire/metadata are redacted, including complete JSON-string escapes and raw capture-boundary prefixes. Unparseable/truncated SSE events (including unterminated escaped JSON strings) are removed fail-closed as `[REDACTED]`, with `malformed_events_removed`; safe prior events remain bounded. A credential in assembled final text causes technical failure instead of exposing repaired YAML. Redactions are labeled; wire hashes cover **saved sanitized bounded bytes**, not an original complete response. This is not general personal-data redaction: use supplied fictional/non-sensitive input only. Files are not immutable against arbitrary host edits, and storage failure cannot promise complete persistence.

Nested deadlines honor the earlier active timer. Final record serialization, close and publication share the remaining 360-second invocation budget, with no extra failure-finalization allowance. Any failed/interrupted evidence write marks storage incomplete regardless of its timeout/cancellation/storage error classification. Finalization failure raises a fixed safe technical error; CLI exits 2 and names timeout/cancellation/storage failure without raw exception text. Earlier files and an uncommitted `record.partial.json`, if created, remain for inspection. Only the published `record.json` is a committed terminal record: partial-file fields are provisional, even if its JSON happens to be parseable. Expired budgets may leave no final record. POSIX alarms cannot guarantee interruption of uninterruptible kernel I/O; there is no crash durability/fsync guarantee.

Configuration distinguishes desired requested target, adapter-selected resolution and response-reported model/IDs. Offline recording resolves to `recording-provider` / `synthetic`, not the desired native model. Physical upstream model attestation is unavailable for both modes.

## Commands

Set `PYTHON` to the compatible interpreter and `RECORDS` to your caller-selected **existing outside-repository parent**. Names below must be fresh. These native commands make real calls; they are documented, **not executed by the offline fix pass**:

```sh
PYTHON=/opt/hermes/.venv/bin/python
RECORDS=/absolute/outside-repo/existing-parent

# F1: supplied fictional version/change fact → bounded text
"$PYTHON" -m olympus --input examples/block-2.1/f1.yaml --record-dir "$RECORDS/f1-new" --approval-authority 'Project editor'

# F2: empty objective → Governor clarification, no downstream calls
"$PYTHON" -m olympus --input examples/block-2.1/f2.yaml --record-dir "$RECORDS/f2-new"

# F3: missing planning fact → clarification/planning, no Apollo dispatch
"$PYTHON" -m olympus --input examples/block-2.1/f3.yaml --record-dir "$RECORDS/f3-new" --approval-authority 'Project editor'

# F4: fresh F1 admission, explicit late authoritative fact withdrawal
"$PYTHON" -m olympus --input examples/block-2.1/f1.yaml --record-dir "$RECORDS/f4-new" --approval-authority 'Project editor' --execution-context-update examples/block-2.1/f4-update.yaml
```

F4 appends the explicit context update only after ready admission, without rewriting governance, objective or handoff. A real blocked Apollo output must have null content/stage and empty checks. If F3 ends at Governor clarification, do not claim the Orchestrator missing-fact boundary was exercised. Inspect F1's actual sentence for version 2/search typo fix and absence of invented facts, tests or approval/release claims. Never substitute synthetic results for unsuccessful real attempts.

Athena dispatch was added as a bounded incremental extension. Its focused offline check verifies the selected Owner identity and exact `research_learning` assignment; the existing Apollo happy-path check covers the same identity and assignment boundary. No live-provider result is claimed for Athena.

Offline checks (no credentials/network calls):

```sh
/opt/hermes/.venv/bin/python -m unittest discover -s tests -v
/opt/hermes/.venv/bin/python -m olympus --help
```

For CLI synthetic execution, supply `--recording-replies /path/to/replies.json` alongside `--input` and a fresh `--record-dir`. The JSON is a list of raw YAML strings, one per call; recording evidence is explicitly synthetic. `tests/test_cli.py` exercises a complete offline chain and collision refusal. Exit code 2 means technical failure; code 0 means a classified terminal result, **not** semantic acceptance.
