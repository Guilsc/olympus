# Olympus Universe implementation runway: phased draft to handoff

> Long-range DRAFT, November 2026. This file is a sequencing and validation artifact, not authorization to execute future blocks. **The current autonomous bootstrap must STOP before Block 3.** Architectural baseline v1.2.2 remains frozen unless an ADR, independent senior architect review and explicit human approval authorize a change.

## Source-of-truth reconciliation prerequisite

Remote `Guilsc/olympus` main is a documented foundation and older block sequence. Historical VPS updates reported a separate local `feat/olympus-universe-v1.2` branch and newer OLY-01...07 activities. Those parallel labels are **not interchangeable**. Before running scripts, confirm effective VPS checkpoint and map old Block 1.x/2.1 vs newer BOOT/OLY tasks in a status matrix. No inferred rename or restart.

## Phase 0: Recovery and source-of-truth (now, before Block 3)

| Order | Track | Goal | Evidence / acceptance | Execution status |
| --- | --- | --- | --- | --- |
| 0.1 | BOOT-00 | Verify Hermes Core/default, real VPS gateway, models/quotas, git state, profiles, plugins and mounts | Host fingerprint, config inventory, source revision and classified uncertainty | Awaiting VPS connection |
| 0.2 | BOOT-U0 | Consistent VPS backup and recovery test | Hash manifest, engine snapshots, staged extraction and rollback | Awaiting VPS connection |
| 0.3 | BOOT-01 | Reconcile authoritative v1.2.2 vs actual VPS branch and remote foundation | Requirements trace, non-destructive Git diff and test baseline | Docs prepared; live reconciliation pending |
| 0.4 | BOOT-02 | Review installed plugin scopes, OMH loops, model routes, native Kanban/Telegram, capability grants | Compatibility/owner matrix, risks and staged integration plan | Docs prepared; live inventory pending |
| 0.5 | Gate | Independent verification of all goal evidence; preserve before-Block-3 stopping point | PASS/REWORK/BLOCKED, limitations, user handoff | Not executed |

Do not reorder live backup behind an irreversible service mutation. Read-only parallel work is allowed.

## Phase 1: Olympus runtime foundation (future, only as specifically authorized)

- Recover/review existing canonical v1.2.2 role/realm contracts and eight separate profile identities.
- Verify Zeus as governor, Olympus Hermes as orchestrator, Domain Owners as exclusive side-effect owners.
- Verify native profile isolation, SOUL/USER/MEMORY, model provenance and template creation grants.
- Confirm approved capability ownership, registry and dispatcher, without creating duplicative MCP infrastructure.
- Establish initiative/mission idempotency, persisted ledger, Kanban mapping, Planning Room context and clear human approval gates.
- Use native group chat only where it cannot bypass authority. Temporary workers are task-bound and interrupted/observable.
- Test at minimum: one authorized initiative, one denied request, one cross-realm delegation, one unavailable owner, one failed task/retry and one model quota failure.

## Phase 2: Operator integrations (future, sequencing can be planned now)

### 2A. Hermes WebApp and secure gateway
- Preserve Hermes VPS HTTPS as the verified Core engineering endpoint (Hermes Dash Gateway).
- Evaluate native v0.23 WebApp on an authenticated private route; prove session consistency with Desktop.
- Only then plan `hermes.guilhermecosta.tech` migration, retiring redundant public UI/hostname after dependency and rollback review.
- Keep gateway listener and sessions; do not equate extra UI with duplicate backend.

### 2B. Telegram one-bot group
- Verify existing connected `@guilherme_hermes_agent_bot` actually reaches VPS Hermes profile.
- Prepare group/topic routing with separate maintenance vs initiative policy; do not create eight bots unnecessarily.
- Respect private data and approval boundaries, no changes to webhook/Telegram token until tested backup and access proof.
- Post redacted status and daily notifications only with authorized recipient/chat IDs.

### 2C. Plugin and worker enhancements
- Keep installed OMH and approved plugins available. Inspect active compatibility with Hermes v0.23, grants, updater and actual usage.
- Use Advanced Delegation only on orchestrator profile where authorized; Bot Forge only controlled provisioning; Agent Importers staged/dry-run.
- Evaluate Kanban Empowered as **supplement**, not replacement for canonical Olympus workflows. Auxiliary summarization requires explicit privacy/model approval.

## Phase 3: Mission Control (separate project, AFTER Olympus readiness)

A read/control frontend for generic operations and galaxy-specific spaces. The future UX can follow one of:
- **Command Bridge:** operational, dense, excellent for daily/incident workflows.
- **Galaxy Atlas:** narrative, exploratory and multi-galaxy.
- **Mission Studio (preferred prototype):** one mission at a time, clear goals, Kanban, evidence, approvals and progress.

The default v1 screen should share canonical mission IDs from Olympus/Cronos contracts, not create its own mission ledger or grant authority. A generic workspace for nonproject outputs must remain distinct from a full galaxy project.

Design prototype and prompt scenarios may be drafted now, but no frontend deployment, persistent new DB or new mission service is authorized by the pre-Block-3 bootstrap.

## Phase 4: Cronos/Apex universal intake (separate project, AFTER Mission Control)

- Global entry point chooses galaxy and request type (initiative, project, bounded output).
- Stable normalized initiative/mission IDs, no duplicate submissions across Telegram, Desktop, WebApp or Mission Control.
- Governance routes through Olympus Zeus, then Olympus Hermes planning and exclusive Domain Owners; projects/results are delivered into the chosen galaxy.
- Universal visibility, second brain references and audit/approval policy are derived from real canonical state.
- Validate permissions, policy rejection, duplicate intake, cross-galaxy isolation, human approvals and resiliency.

## Phase 5: Knowledge / second brain extension (do not make a current dependency)

- Mnemosyne is the desired knowledge/second brain layer, separate from per-agent identity and episodic memory.
- Investigate the actual nightly memory plugin's behavior, privacy, persistence and retention before adding Hindsight or Obsidian.
- Pick a store only after real workload and data-custody requirements are known. Do not silently pool private profile memories.
- Allow versioned, approved knowledge promotion from runtime artifacts; nightly summaries alone must not rewrite Constitution or role grants.

## Global sequencing and quality rules

1. Preserve the v1.2.2 architecture and the user's already decided scope. Do not turn conceptual responsibility planes into unnecessary services.
2. Every mutation has one active owner, least privileges, idempotency, audit and rollback.
3. Backend source of truth remains outside chat, Kanban widget, avatars and Mission Control presentation.
4. Every card has observable goal criteria, deterministic checks, independent review when necessary and a terminal verdict.
5. When work is blocked, continue useful independent documentation/source-review work; do not fabricate production execution or burn unapproved models.
6. Maintain a daily handoff and end-of-run open-loop sweep; pick next approved highest-value item until the requested goal boundary is reached.
7. The current mandate is recovery/preparation **until before Block 3**, not automatic implementation of Phases 1–5. Future phases remain plans awaiting user authorization and the appropriate specialist reviews.

## Current artifacts and handoff pointers

- [Reconciliation and current gaps](2026-11-07-reconciliation.md)
- [Kanban cards and review gates](kanban-cards-and-review-gates.md)
- [Recovery tests](acceptance-and-recovery-tests.md)
- [Plugin and Kanban market review](plugins-v023-scope-matrix.md)
- [Themes and capability-scoped skills](profile-themes-and-skills-scope.md)
- [Telegram group](telegram-one-bot-group-routing.md)
- [WebApp cutover runbook](hermes-v023-webapp-migration-runbook.md)
- [Mission Control design study](future-mission-control-three-designs.md)
- [Specialist/architecture review policy](senior-specialist-and-architecture-review.md)
- [Open loops and daily handoff](open-loop-register.md)
