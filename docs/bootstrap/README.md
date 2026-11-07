# Olympus bootstrap documentation index

> Current scope: recovery/preparation **through the checkpoint before Block 3**. Architecture v1.2.2 is frozen by default. These documents are **proposals and planning records** in draft PR #12, not evidence of operational execution.
>
> **Start here** to prevent rereading everything or duplicating work.

## Operator reading order

| Read order | Document | Purpose | Current evidence |
| --- | --- | --- | --- |
| 1 | [Requirements traceability audit](requirements-traceability-audit.md) | Full user-decision inventory, mandatory open-loop checklist and historical labeling hazards | Draft documentation, GitHub verified |
| 2 | [Current-state reconciliation](2026-11-07-reconciliation.md) | Separate remote Foundation from unverified VPS implementation | Draft documentation; VPS unverified |
| 3 | [Open-loop register](open-loop-register.md) | Prioritize unresolved outcomes and four-hour daily | Draft documentation; many operational blockers |
| 4 | [Kanban cards and review gates](kanban-cards-and-review-gates.md) | BOOT-00, BOOT-U0, BOOT-01, BOOT-02 descriptions, evidence, review, stop | Written, **not created in native VPS Kanban** |
| 5 | [Acceptance and recovery tests](acceptance-and-recovery-tests.md) | Positive/negative checks, backup consistency, profile isolation | Test design only |
| 6 | [Plugin and v0.23 matrix](plugins-v023-scope-matrix.md) | Candidate plugins, native Kanban vs Empowered, actual grants | Catalog review only; live plugin inventory pending |
| 7 | [Themes and skills scope](profile-themes-and-skills-scope.md) | Canonical roles, replaceable Greek theme, exclusive owner capabilities | Source-mapped draft, live profile audit pending |
| 8 | [Senior-specialist / architecture review](senior-specialist-and-architecture-review.md) | Discipline-specific delivery quality, ADR and independent-architect gate | User-approved process, no architecture change |
| 9 | [Hermes remote ingress options](hermes-remote-ingress-options.md) | VPS HTTPS API/WS vs Telegram user/group/bot-to-bot | Outbound bot tested; inbound not connected |
| 10 | [Telegram group routing](telegram-one-bot-group-routing.md) | Reuse topics and one bot; staged private pilot and safe secret handling | Plan only, no new group/service |
| 11 | [Native WebApp migration](hermes-v023-webapp-migration-runbook.md) | Backup, TLS, sessions, proxy rollback | Plan only, **no cutover** |
| 12 | [Implementation runway](implementation-runway.md) | Order and gates through later phases | Future phases not authorized |
| 13 | [Mission Control design directions](future-mission-control-three-designs.md) | Compare three prototype concepts without frontend deployment | Design only; no ChatGPT Project created |

## Daily checkpoint

1. **Delivered:** source of truth, exact changes, PR/commit, checks and reviewers.
2. **Blocked:** actual unavailable executor/provider/permission and mitigations already attempted.
3. **Decision required:** only user-authorized exceptions, approval or material architecture changes.
4. **Remaining:** next uncompleted card and dependency, relative to current pre-Block-3 scope.
5. **Parallel progress:** independent tests/docs/review and unclaimed proposed future capabilities.

## Critical gate distinctions

- GitHub offline-integrity checks passing do not confirm VPS backups, Sol quota, Telegram inbound routing, running profiles or WebApp availability.
- The original Block 0/1/2 labels and new BOOT numbering have conflicting historical usage. Inspect canonical VPS checkpoint and reconcile **before** creating real cards, without silently replacing identity IDs.
- A ChatGPT scheduled automation does not prove a live Hermes worker or Work browser session.
- A Bot API outbound message does not start an inbound Telegram/Hermes job.
- A draft design for Mission Control/Cronos does not authorize implementation, storage, new agents, global grants or a production deployment.
- One mutable side-effect has one active owner. Themes, skills catalogs, Kanban UI and chat topics are not independent authorities.

## Current verification checkpoint (2026-11-07)

- [GitHub PR #12](https://github.com/Guilsc/olympus/pull/12): draft, no merge; offline-integrity workflow reported **success** on commit `fa8a7919`. Recheck latest head after any subsequent commit.
- [Bot-hub PR #4](https://github.com/Guilsc/universal-agent-bot-hub/pull/4): draft synthetic Telegram group ingress tests reported passing CI; no live Telegram-to-VPS proof.
- **VPS restore-ready backup:** not verified.
- **Hermes Core model quota and HTTPS execution:** not verified.
- **Native Kanban cards / WebApp cutover / new Telegram group:** not executed.

## Last action before stopping a run

Review the [requirements checklist](requirements-traceability-audit.md) and [open-loop register](open-loop-register.md) against the newest user instructions and actual GitHub state. Pick an independent, bounded, authorized next action if possible; otherwise record the precise blocker and resume condition. Never invent success or perform a riskier activity just to keep moving.

## Newly prepared reusable drafts (2026-11-07)

| Document | Purpose | Runtime state |
| --- | --- | --- |
| [Future block-by-block implementation drafts](future-blocks-implementation-drafts.md) | FUTURE-B03..B12 for Olympus and future MC01..04/CR01..04 with prerequisites, negative tests, review and stop gates | Future only; no Block 3 authorization |
| [Telegram/Hermes prompt playbook](telegram-hermes-prompt-playbook.md) | Operator provenance, BOOT task prompts, transport/debug/reviewer/daily scripts and topic guidance | Prepared instructions only; inbound Hermes gateway unverified |
| [Vertical Kanban picklist](vertical-kanban-picklist-ux.md) | Galaxy/initiative tree, board state mapping, permissions, evidence panel, accessibility and synthetic mock data | UI specification only; no new Kanban plugin or app |

Never claim the prompt playbook ran remotely or the UI specification was installed. Read these before asking the user to provide an already documented topic or proposing new project services.

## Static visual prototype

[Mission Control — three selectable layout concepts](mission-control-three-concepts.html) is a **standalone HTML/CSS prototype** with concept tabs (A Command Bridge, B Galaxy Atlas, C Mission Studio), synthetic status data and a vertical initiative picker. It is not connected to the VPS and has no operational backend, model calls, auth or real approvals. The file can be inspected as source on GitHub or rendered safely as a local static HTML artifact; no ChatGPT Project has been created.
