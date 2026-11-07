# Hermes v0.23 native WebApp cutover: future operational runbook

> Draft only (2026-11-07). This is not a deployed topology, confirmed reverse-proxy inventory, authorization to edit domains, or a substitute for tested backup. **Stop before Block 3.** Execute only later from Hermes Core `default` on the VPS via Hermes VPS HTTPS or SSH of that VPS, after the user approves the cutover.

## Approved user-facing names and expected targets

| URL / name | Intended role | Current status |
| --- | --- | --- |
| `hermes-gateway.guilhermecosta.tech` — **Hermes Dash Gateway** | Existing reliable HTTPS/Desktop remote connection and associated administration | User-reported functional, live proxy mapping **unverified** |
| `hermes.guilhermecosta.tech` | Native Hermes v0.23 WebApp, future Universe-access frontend candidate | Historical third-party community WebUI; cutover **not executed** |
| `gateway.guilhermecosta.tech` | Separate redundant public dashboard route | Candidate retirement after dependency validation, not an executable deletion order |
| Internal Hermes agent listener `:9119` (historical) | Gateway API + session routing; may also serve native WebApp | Must discover actual container port and role; **never remove listener simply because public UI is redundant** |

## Dependency mapping

1. Record the actual active Coolify app/container IDs, images, versions, ports, persistent volumes and current gateway/web UI/relay health.
2. Read current reverse-proxy routes, DNS, upstream hosts, TLS certificates and expiration, WebSocket and HTTP authentication configuration. Do not disclose proxy credentials.
3. Map Desktop (remote HTTPS / SSH), Telegram bot, CLI, MCP clients and other consumers to actual endpoints. Test whether old public dashboard hostname is used by any client or callback.
4. Confirm native WebApp feature in **installed** Hermes v0.23 runtime. Check actual configuration key names against the installed release docs; don't assume names from a third-party guide.
5. Establish which gateway process owns session queues/history. Multiple public names may proxy one process; multiple containers may cause duplicate queues.

## Safety gates before mutation

- **BOOT-U0** verified consistent backup of Hermes state, profile memories/sessions and reverse proxy/Coolify manifests, with restore instructions; no overwrite of prior checkpoints.
- Snapshot effective Git and Docker deployment state, including image digests and current config/mounts.
- Confirm native WebApp has authenticated access, TLS, secure cookies/session policy, bounded authorized operations and no inadvertent exposure of `default` tools.
- Prepare a reversible proxy-only change without destroying the old community WebUI until smoke tests pass; verify Desktop HTTPS route continues working.
- Review with Senior Platform/SRE and Senior Security roles. If rollout requires changing approved architecture (rather than substituting one UI for another) prepare ADR and independent senior architecture review plus explicit human approval.

## Proposed migration sequence (separate future authorized milestone)

```text
READ-ONLY inventory → VPS backup PASS → hidden/private WebApp smoke test
→ session/profile parity tests → proxy backup → gated hostname cutover
→ TLS/auth/WebSocket smoke → Desktop HTTPS/Telegram/API smoke
→ rollback test availability → retire old public WebUI route
→ usage observation → retire only proven redundant resources.
```

The migration should not delete database volumes, Hermes agent containers, gateway listener, or old proxy resources before independent verification. Prefer rollback by restoring the prior proxy target/route rather than rebuilding the entire VPS.

## UAT checklist

| Case | Expected result |
| --- | --- |
| Desktop `Hermes VPS (HTTPS)` reconnect | Existing session data visible; no reauthentication loop |
| Browser signs in through native WebApp | Auth enforced, profile resolved correctly, secure session |
| Anonymous browser access | No access to sessions/tools/avatars/identities |
| Concurrent Desktop + WebApp | One session owner/queue and consistent updates |
| WebSocket reconnect | No duplicate actions or message loss |
| Telegram message | Existing bot still reaches its approved gateway/profile; no webhook reset |
| Historic sessions | Existing IDs and history retained |
| Profiles | `default` and existing Olympus identities do not alias writable memory |
| Bot/side effects | Unauthorized profile cannot execute a capability of another owner |
| Old public dashboard URL retirement | Not removed until external dependents and rollback verified |

## Telegram and WebApp relationship

The Hermes WebApp is a *client UI*. Telegram is a *transport*. Neither independently owns initiative policy, memory or Olympus canonical missions. In later phases the universal front door belongs to Cronos/Apex, with Olympus Zeus → Olympus Hermes → Domain Owners as authorized path, while Mission Control is a view/control experience.

Do not build Cronos or Mission Control in this recovery milestone. Their interface contracts and mockups may be drafted in separate documentation.

## Output requirements for the later operator

Record:
- live topology diagram (with sanitized host and TLS metadata),
- before/after proxy mapping,
- session ID and profile routing evidence,
- screenshot/test evidence without secret content,
- diff, rollback commands generated *from verified live state*,
- final UAT verdict by test case.

No destructive command template is embedded here, because unverified Coolify/Docker names or paths could delete the wrong service.
