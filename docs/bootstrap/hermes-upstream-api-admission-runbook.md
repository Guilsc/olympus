# Verified Hermes HTTP/WS integration surface and next safe admission plan

**Evidence source read on 2026-11-07:** upstream NousResearch Hermes Agent official files, not a third-party blog:
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/api-server.md
- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/programmatic-integration.md

**Applicability:** verify exact running Hermes VPS revision first. The upstream main branch is not proof of what is installed or enabled on the Hostinger VPS. This is an implementation-ready design draft, **not** a working connection, a token export, a new public endpoint or a permission to alter services.

## Confirmed upstream API features

### OpenAI-compatible HTTP API
- Default local listener described in docs: 127.0.0.1:8642, only if API server is enabled. **Do not assume the user's existing public gateway on HTTPS port 9120 exposes this API.**
- Auth uses `API_SERVER_KEY` in the upstream configuration; no key value is known or required by this document.
- `POST /v1/chat/completions` accepts a user-message array with `model: hermes-agent`.
- `GET /v1/capabilities` advertises feature availability.
- `POST /api/sessions`, `GET /api/sessions`, `GET /api/sessions/{id}`, `GET /api/sessions/{id}/messages`, and `POST /api/sessions/{id}/chat` provide session and turn handling (if installed version supports them).
- `POST /api/sessions/{id}/chat/stream` emits SSE tool progress and terminal `run.completed/run.failed/run.cancelled` events.
- API requests may use `Idempotency-Key`; semantics vary between canonical durable session authority and legacy mode. An HTTP acceptance is NOT completion, and `finish_reason: length` indicates iteration budget exhaustion, NOT full goal achievement.
- Under ambiguous admission (`unknown_execution` or `admission_conflict`) **do not retry using a new key to force execution**, because the original operation may have run.

### TUI gateway control plane

- Upstream describes `hermes-gateway-v1` JSON-RPC over authenticated WebSocket / local stdio, with single-use tickets. Desktop/TUI uses this for `runtime.describe`, `session.create`, `prompt.submit`, `session.status`, `session.history`, interrupts and approvals.
- Do not open a guessed WebSocket or manufacture tickets from an unrelated API secret.
- The session source and `profile_id` are validated against the owner. Client name is attribution only, never authority.
- A frontend receiving a server-issued approval/secret/sudo request must not auto-approve. If no authorized interactive human answer is available, respond unsupported/refuse, not implicit consent.

### Telegram bot-to-bot official constraints

- Source: https://core.telegram.org/api/bots/bot-to-bot and https://core.telegram.org/bots/features
- In a shared group, a targeted command mentioning the recipient or a direct reply can be delivered if at least one bot has Bot-to-Bot Communication Mode enabled.
- Without explicit target/reply, broader group bot-message reception requires the receiving bot's bot-to-bot mode plus admin rights or disabled Group Privacy Mode; **do not grant admin just for convenience**.
- Direct private bot-to-bot requires both bots' mode enabled.
- Loop prevention requires deduplication, rate limits, maximum depth and timeouts.

## Safe next interaction once an authorized VPS executor is connected

**Step 1: prove host and process.** READ ONLY show real hostname, Hermes installed version, host identity, running listener status, whether API server is already enabled, actual bound interface and effective ingress/proxy route. Redact secrets.

**Step 2: prove least privilege.** Compare existing API access against session-profile `default` and requested read-only capabilities. Never change `API_SERVER_ENABLED`, `API_SERVER_KEY` or firewall as a discovery step. If disabled, record as an approval-gated change proposal, not an action.

**Step 3: capability discovery.** Only if there is an already authorized private API session, call `GET /v1/capabilities`, confirm feature flags and `GET /api/sessions` without dumping private message contents. No public probing, no auth brute force, no key exposure.

**Step 4: bounded harmless challenge.** Create or reuse an explicitly authorized private `default` session (not Olympus Hermes) with a unique request ID and the provenance-handshake prompt from `telegram-hermes-prompt-playbook.md`. Use the actual supported schema from `/v1/capabilities` and installed docs, never guess API structure based on upstream.

**Step 5: correlate lifecycle.** Verify API admission, session ID, model/provider provenance, terminal run status, actual host, no side effects and independent reviewer. If tool calls occurred unexpectedly, treat as REWORK, preserve evidence and stop.

**Step 6: only after pass:** plan scoped BOOT-00 read-only inventory; no backup or other mutation until authorization and actual host backup preconditions are established.

## Request skeleton (illustration, NOT executed)

```bash
# This is an illustrative template for a verified, EXISTING authorized HTTPS API endpoint.
# DO NOT run on Windows or expose a new port. Derive URL, key and profile from VPS.
curl --fail-with-body --silent --show-error \
  --header "Authorization: Bearer ${APPROVED_API_KEY}" \
  "${VERIFIED_PRIVATE_HERMES_BASE_URL}/v1/capabilities"
```

Do **not** embed the real BotFather token in any API header. Telegram bot credentials and Hermes API credentials are different classes of secret.

## Current capability verdict

| Required condition | State as of this documentation |
| --- | --- |
| Official endpoint contract exists upstream | Verified from upstream source |
| Effective VPS Hermes version/config and API enabled | UNVERIFIED |
| API key available through an approved connector/session | UNVERIFIED |
| Authenticated chat turn to VPS Core default | NOT EXECUTED |
| Actual BOOT-00 inventory and backup | NOT EXECUTED |
| Telegram self-message runs a task | NO; outbound notification alone cannot supply ingress |
| Synthetic Bot Hub group unit tests | PASS in separate GitHub draft PR #4; not VPS/Telegram live evidence |

## Design boundary

The default VPS Hermes Core is an engineering operator. Any future Galaxy intake still follows Olympus Zeus → Olympus Hermes → owning Domain Owner. The HTTP transport must not bypass scope and owner enforcement; an LLM prompt is not an access-control layer. Native WebApp and Telegram are clients to authenticated underlying runtime, not alternate mission policy engines.
