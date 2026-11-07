# Hermes Core default: staged Kanban orchestration workpack

STATUS: DRAFT ONLY. The user supplied the existing board at https://hermes-gateway.guilhermecosta.tech/kanban?profile=default . This session's fetch attempt returned DisabledError, so no live Kanban cards were read or modified. The items below are proposed work units to reconcile against the actual board, NOT new native card IDs.

## Rules and responsibilities

- Hermes Core profile default coordinates this administrative VPS bootstrap. The canonical Olympus Hermes orchestrator remains distinct and must not be instantiated or given Core privileges.
- Specialist lanes below are expertise assignments, not persistent Olympus roles, active workers, or new grants. Delegate only to available, authenticated, least-privilege workers on the actual VPS. If unavailable, Core retains the task and records the specialist lens.
- STOP before Block 3. No architecture, provider, bot, webhook, DNS, proxy, or plugin mutation merely for task setup.
- The authoritative BOOT-00 / BOOT-U0 mapping conflicts across historical sources. Inspect live cards and checkpoint before creating, renaming, or moving any card. Match existing tasks by goal, current ID and scope, not title alone.
- Every card needs immutable goal, explicit dependency, one side-effect owner, read-only vs mutating classification, bounded attempt, true execution evidence, deterministic tests, separate reviewer, PASS / REWORK / BLOCKED, and cancellation/rollback.

## Work breakdown for current Olympus bootstrap

| Proposed card | Goal | Expertise lane | Dependencies | Acceptance evidence |
| --- | --- | --- | --- | --- |
| 00-A | Verify actual Hostinger VPS, Core default identity, HTTPS/SSH transport and Hermes version | Senior SRE | none | Host/profile/session provenance, read-only |
| 00-B | Read services, persistent mounts, Git checkout, native Kanban and profiles | Senior SRE | 00-A | Sanitized AS-IS inventory |
| 00-C | Verify active model/provider, weekly quota and fallback policy | Senior LLM Platform | 00-A | Observed model and authorization, or precise blocker |
| 00-D | Read Telegram webhook/polling, group and topic routing | Senior Integration | 00-A | Verified ingress/allowlist map, without polling conflict |
| U0-A | Plan consistent VPS snapshot, disk and database preflight | Senior SRE | 00-B | Volume-by-volume plan |
| U0-B | Produce non-overwriting consistent VPS backup | Senior SRE | U0-A, approved write gate | Backup files, hashes and snapshot evidence |
| U0-C | Independently test restore/checksums in isolated VPS area | Senior QA + SRE reviewer | U0-B | Recovery test and rollback verdict |
| 01-A | Reconcile Foundation main, v1.2.2 and OLY vs BOOT IDs | Senior BA | 00-B | Source-of-truth and traceability artifact |
| 01-B | Validate changes/tests without losing dirty VPS state | Senior Developer + QA | 01-A, U0-C before writes | File diff, tests, negatives |
| 02-A | Inspect Hermes v0.23 plugins, OMH and native Kanban | Senior Platform | 00-B | Loaded vs candidate, version, grants matrix |
| 02-B | Check eight profiles, skills ownership and memory isolation | Senior Security | 00-B | Scoped capability matrix, isolation evidence |
| 02-C | Review native WebApp/Desktop/gateway migration readiness | Senior SRE | 00-B | TLS/auth/WS/rollback plan, no cutover |
| 02-D | Define Telegram relay/group UAT with known bot and topics | Senior Integration | 00-D | Real inbound route test plan, no bot self-message |
| GATE | Independent review of results and STOP before Block 3 | Separate Senior QA/Architect | Relevant accepted predecessors | PASS/REWORK/BLOCKED by original goal |

Parallelism: 00-C and 00-D may run read-only after 00-A. 01-A, 02-A, 02-B, and 02-C can proceed read-only after 00-B while backup planning happens. All mutations require backup restore verification, effective permissions and applicable human approval.

## Native Kanban matching workflow

1. Authenticate existing VPS Hermes default session and READ current board cards, owners, statuses, dependencies and exact IDs.
2. Reconcile existing card goals with proposed tasks above; use existing cards whenever a match exists. Do not replace state or attempts.
3. If a relevant goal is too broad, create child cards only through the installed native Kanban's supported API/tools, and only after the authoritative BOOT naming conflict is resolved.
4. New cards start in Draft or Ready only once prerequisites pass. No documentation commit can put a live task into Running or Done.
5. Record actual card IDs and profile/session provenance in a private VPS artifact, not this public file.

## Vertical board layout and evidence panel

Left: Olympus > Bootstrap > BOOT-00 / BOOT-U0 / BOOT-01 / BOOT-02 > bounded child tasks.
Center: Draft / Ready / Running / Review / Done; Blocked and Suspended only if native runtime supports them.
Right: original goal, owner, dependencies, observed provider/model, attempt/retry/cancel receipts, tests and review verdict.

UI drag/drop is never permission for privileged execution or acceptance. Parent completion requires independent evidence, not visual count of Done children.

## Ready-to-send coordination prompt for the existing Hermes session

> You are Hermes Core default, working as engineering OPERATOR for Olympus bootstrap v1.2.2. You are NOT the canonical Olympus Hermes orchestrator. Work on the verified Hostinger VPS only, through existing authenticated Hermes VPS HTTPS or SSH into the SAME VPS.
>
> First prove actual host, effective profile default, model/provider quota, and native Kanban read access. Inspect current cards, reconcile historical BOOT IDs, preserve all existing IDs, status and sessions. Use the card proposals in Guilsc/olympus draft PR #12 docs/bootstrap/hermes-default-kanban-orchestration-workpack.md. Break tasks into independently testable subtasks, assign ONE suitable already available authorized specialist per card, and retain Hermes Core as coordinator if no specialist exists. Do not install agents or grant permissions just to fill slots.
>
> Execute approved read-only and backup tasks only through applicable gates, with per-attempt evidence and independent review. Never treat messages sent by the Telegram bot as its own inbound instructions. Never alter bot tokens, webhook, providers, DNS/proxy, memory, roles or native plugins without approval. Stop before Block 3.
>
> When a card blocks, record the real error, attempted safe alternatives and next prerequisite; proceed with an independent authorized card. Before reporting idle, reread requirements-traceability-audit.md and open-loop-register.md. Return actual card IDs, terminal statuses, host/provider receipts, tests and remaining scope. Do not invent successful runs.

## Current evidence

GitHub-only draft workpack: prepared. Actual VPS session: not established. Real native Kanban task IDs: unknown. Specialist workers: unverified. Live VPS backup: unverified. No tasks delegated or executed remotely by this document.

## Ownership transition once Olympus bots are operational (explicit user decision)

**Hermes Core `default` is an infrastructure/bootstrap operator, not the standing orchestrator or owner of Olympus initiatives.** Its interim coordination of BOOT tasks exists solely because the actual Olympus bots and their native capability grants have not been verified ready.

When Zeus, Olympus Hermes and the six Domain Owner bots/profiles are actually configured, authenticated, tested and approved:

1. **Zeus / governor** evaluates and authorizes the initiative or change request. Bootstrap infrastructure maintenance remains a distinct operational responsibility.
2. **Olympus Hermes / orchestrator** becomes responsible for goal breakdown, canonical ownership, task dependency sequencing, specialist delegation, review routing and state coordination. Use the approved native Kanban and agent delegation mechanism; do not create a parallel side-effect authority.
3. **Correct Domain Owner** owns execution within the exclusive realm capabilities. For multi-realm objectives, Hermes delegates each bounded contribution to its owner, even if small. The supporting agent does not take over the lead owner's entire outcome.
4. **Temporary workers and independent reviewers** receive scoped, time-bounded tasks. They cannot acquire permanent capabilities, approve their own privileged changes or bypass Zeus.
5. **Hermes Core `default`** supplies platform/VPS diagnostics, backup, gateway administration and engineering support *when explicitly delegated* or when acting within its separately authorized platform-operator mandate. It must not remain an Olympus mission coordinator, dispatch other gods on its own initiative, or inherit the project mission backlog by default.
6. **Handoff criteria:** prove target bot identities and role contracts, authenticated ingress, effective grants and memory isolation, native Kanban/dispatcher availability, audit/rollback, and end-to-end UAT. Link all BOOT card IDs and historical evidence before transferring or reassigning work; never silently steal existing active attempts.
7. **If bots unavailable or readiness fails:** leave Olympus-owned work BLOCKED/QUEUED pending proper orchestration. Hermes Core may continue separate platform recovery, but must **not impersonate Olympus Hermes or execute domain work as a workaround**.

The 14 proposed Core-owned bootstrap subcards are **temporary administrative recovery cards**, not a reusable policy assigning all future Olympus work to Core. Once bots are ready, the original mission activities must be routed through Zeus → Olympus Hermes → owning Domain Owner and the established delegate/review process. No current live bot activation or work reassignment is claimed.
