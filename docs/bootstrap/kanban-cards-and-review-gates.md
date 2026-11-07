# Hermes Core bootstrap: Kanban cards, verification gates and safe fallback work

> Draft preparation only — 2026-11-07. Must be reconciled with the actual VPS state and the approved v1.2.2 specification before execution.
>
> **Executor**: Hermes Core, native profile `default`, on the VPS via **Hermes VPS (HTTPS)**. SSH to the same VPS is a permitted secondary transport. Never execute this procedure on Windows, Workspace Local, an unrelated cloud sandbox or a disconnected agent.
>
> **Boundary**: recovery and preparation up to, **not including**, Block 3. No merge, proxy/domain cutover, production deployment, permission escalation, Telegram token mutation or automatic installation of new high-privilege plugins.

## Intake policy

This bootstrap is an **administrative recovery workflow**, not an Olympus mission, so these cards can be handled directly by Hermes Core instead of invoking Zeus, Olympus Hermes or the Planning Room.

Each card has an immutable goal statement, observable acceptance evidence, assignee `Hermes Core/default`, dependencies, execution state, reviewer verdict and handoff location. Kanban is a view/trigger, not the canonical source of approval or memory.

The operator must never create duplicate active cards for the same recovery objective. If the current native Kanban board has existing matching cards, reuse them and preserve IDs and history. If write access to Kanban is missing, produce read-only card proposals and do not claim they were added.

## Card definitions

### BOOT-00 | Recover state and establish trust

- **Goal:** identify what actually runs on the VPS today and what is only a local or historical record.
- **Requires:** connected Hermes VPS HTTPS session, verifiable identity of host, no model fallback to unapproved providers.
- **Read-only evidence:** effective Hermes version, profile `default`, remote endpoint, container images/digests, volume mounts, real persistent data paths, current profile IDs, live process and listener inventory, Git revision/branch/dirty state, installed plugin states and reverse proxy destinations. Record secrets as **presence/absence only**, never contents.
- **Acceptance:** dated AS-IS report, evidence/provenance per claim, reconciliation of previous local branch `feat/olympus-universe-v1.2` with current checkout, explicit unknowns and recovery dependencies. A missing profile must be recorded as MISSING, not silently recreated.
- **Fail closed:** no actual remote connection, ambiguous host identity, unavailable read permissions.
- **No changes:** containers, plugins, DNS/proxy, profiles, sessions, Git worktrees.

### BOOT-U0 | Consistent, recoverable VPS backup

- **Goal:** protect the currently working VPS state before subsequent changes.
- **Requires:** BOOT-00 completed, verified free space and snapshot method for any active database.
- **Include:** runtime/persistent mounts and metadata; the `default` and eight `olympus-*` profiles; SOUL/USER/MEMORY and any separate memory DB; session metadata/history; plugin configs and inventory; custom MCP manifests/config and key location metadata (never expose secrets); Git repository including uncommitted changes and branch refs; user-managed reverse-proxy/Coolify service definitions; relevant Telegram *configuration metadata* without credential disclosure.
- **Consistency:** use engine-supported snapshot/export for active databases; avoid trusting non-atomic live file copies. Preserve UID/GID/modes; exclude cache and other reproducible material; do not stop services for convenience. Store archives with restrictive permissions in a verified VPS path outside backed-up trees; use timestamped non-overwriting names.
- **Acceptance:** archive list, snapshot metadata, checksum manifest, checksum verification, sample extraction/restore validation in a safe nonproduction location **on the VPS** when feasible, and an ordered recovery procedure. If restoration was not tested, state exactly what is unverified.
- **Fail closed:** insufficient disk space, failed snapshots/checksums, risk of credential exposure, inability to identify state volumes or backup of a live database consistently. Never mark PASS merely because a compression command exited zero.
- **No changes:** deploy/restart, upgrade, external upload, DNS, credential rotation.

### BOOT-01 | Architecture and repository reconciliation

- **Goal:** preserve and reconcile all existing Olympus development evidence with approved v1.2.2 decisions and the current GitHub baseline.
- **Requires:** BOOT-U0 PASS before altering any VPS repository state; read-only reconciliation may proceed independently.
- **Inputs:** latest authoritative spec, session checkpoint, actual VPS Git HEAD and dirty working tree, remote Git branches/PRs, existing Constitution and shared development guidance. Treat older historical documents as history, not missing implementation.
- **Acceptance:** requirements-to-implementation traceability table, per-file diff plan (no sweeping rewrites), classification of local-only changes, test baseline and review strategy. Never discard or reset pre-existing dirty files.
- **No changes:** direct push/merge to main, force push, silent overwrite of VPS-only commits.

### BOOT-02 | Plugins, models and delivery readiness

- **Goal:** assess real installed capability status and prepare the pre-Block-3 integration.
- **Requires:** BOOT-00 state inventory and backup PASS for any install/configuration mutation.
- **Plugin inventory:** for each installed/candidate plugin record package ID, exact version and source, integrity/signature if applicable, plugin scope (host/global, project, profile, task), whether loaded/enabled, actual hooks/tools, required grants, memory/sessions interactions, compatibility with Hermes v0.23 and dependencies.
- **Preserve availability:** no preemptive disable/uninstall merely because a plugin appears unused. In particular inspect OMH Restricted Bridge and any previous full OMH installation without assuming either supplies reliable infinite-loop protection. Reuse native Kanban and dispatch; avoid duplicate orchestration.
- **Candidate allocation:** Advanced Delegation → Olympus Hermes only; Bot Forge → controlled provisioning/manager; Agent Importers → review/dry-run staging; themes → presentation only; MCP resource catalog → discovery, with operational authorization still enforced by Olympus owners. Do not blindly clone privileged Core credentials.
- **Model routing:** report preferred model, verified quota, provider route and actual response provenance. A replenished session allowance does not imply available weekly Sol quota. Do not automatically use OmniRoute free for implementation.
- **Acceptance:** matrix of actual vs proposed availability, gaps requiring approval, compatibility checks and one minimal validation strategy per plugin class. Defer high-risk activation to explicit authorization.

## Evidence format for every card

```yaml
card_id: BOOT-00
goal: "..."
executor: "Hermes Core/default via Hermes VPS (HTTPS)"
started_at: null
host_identity_verified: false
model_requested: null
model_observed: null
inputs:
  approved_contract_version: "v1.2.2"
artifacts: []
tests:
  - name: "..."
    result: "NOT_RUN"
reviewer:
  type: "independent-context-or-deterministic"
  verdict: "PENDING"
  rationale: ""
  evidence_checked: []
  missing_evidence: []
gate: "PENDING"
next_allowed_card: null
approvals_required: []
```

- The actual execution report must replace placeholders; never publish dummy results as evidence.
- Separate `PASS`, `REWORK`, and `BLOCKED`. Review correctness against the original goal, not executor self-report alone.
- Use deterministic tests first; an independent reviewer may run in another bounded context with access only to scoped artifacts.
- Use OMH's evaluation/retry mechanisms if installed **and verified**; enforce finite time, token/cost budget, cancellation and progress-based stop conditions even with OMH.
- A blocked prerequisite blocks dependent cards, but does **not** prevent independent read-only documentation and source-review work.

## Backup integrity and memory test checklist

1. Verify each intended profile identifier from actual config, not Desktop avatar list alone.
2. Verify file and store existence for `SOUL.md`, `USER.md`, `MEMORY.md` and any other profile memory location.
3. Confirm effective profile-to-state isolation (no accidental pointer to `default` data).
4. Verify backups include those exact paths and that checksums match.
5. Classify prior memory state as **present**, **empty**, **missing**, or **unverified**. Declarative SOUL is not durable experience.
6. Never auto-restore potentially stale memory into live agent profiles; restoration is separately gated.

## Read-only parallel tasks if Sol/VPS is blocked

- Maintain architecture contract-to-code mapping from GitHub and previously provided documentation.
- Prepare a Hearth v0.23 compatibility inventory: `browser_exec` replacing legacy `browser_*` references, `hermes mcp-serve` command check, native WebApp authentication and session sharing.
- Review GitHub-only source and open PRs for duplicate functionality, stale docs or missing rollback/UAT cases, without claiming to have inspected VPS-private files.
- Draft acceptance scripts/test manifests, plugin/skill ownership assignments, and safe recovery diagrams.
- Identify which documentation-only improvements can be proposed on an isolated PR without requiring deployment.

## Release and stop rules

- Treat the user's approved architecture and existing approvals as binding, not broad authorization to change unrelated infrastructure.
- Do not push or merge branch content without honoring the repository's review requirements. Documentation-only draft PRs are permitted as proposals; merging requires explicit human approval.
- **Mandatory stop before Block 3.** Hand over verified status, exact remaining tasks, the applicable commits/PRs and approvals to request.
