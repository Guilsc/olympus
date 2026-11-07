# Future block-by-block draft pack (NOT approved execution)

**Version:** planning draft 2026-11-07  
**Source boundary:** existing Olympus Foundation/Constitution and `docs/block-2.1-plan.md`, approved user v1.2.2 direction, and bootstrap reconciliation. Historical VPS `OLY-01..07` labels are **not yet mapped** to current GitHub block numbers.

**STOP LINE:** current autonomous authorization ends *before Block 3*. Everything marked **FUTURE** below is proposed acceptance scope and must not be executed on the VPS, created as native work cards, or interpreted as an architecture revision. Existing code/state must be inspected before any implementation plan is accepted.

## Common contract for every future block

```yaml
block_id: "FUTURE-Bxx"
status: "DRAFT_NOT_AUTHORIZED"
source_revision: "UNVERIFIED_VPS"
goal: "observable user outcome"
canonical_owner: "one authorized owner"
supports_roles: []
dependencies: []
entry_gate: "reviewed evidence of prerequisite PASS"
scope_in: []
scope_out: ["unapproved grants", "silent model fallback", "unreviewed architecture change"]
artifacts: []
negative_tests: []
uat: []
rollback: "defined after effective runtime inspection"
reviewer: "separate context or deterministic independent check"
human_approval: "required for privilege, deploy, architecture, destructive/external action"
result: "NOT_RUN"
```

No block may complete from the author's self-report alone. A failed precondition is BLOCKED, not permission to invent an adjacent implementation.

## Reconciliation before future numbered blocks

| Historical stream | What is evidenced | What must be checked |
| --- | --- | --- |
| GitHub Session 1 / 1.1-1.5 | Foundation roles, declared six Owners; Oct 4 Block 1.5 recorded 19/19 host experiments | Whether they reflect still-current contracts and unchanged prompts |
| GitHub proposed Session 2 / 2.1 | Explicitly **planning only** for a narrow local text runner with Zeus → Olympus Hermes → Apollo | It was not implementation authorization; don't auto-promote it into live Hermes v1.2.2 profiles |
| Older VPS OLY-01..07 | User/assistant historical checkpoint descriptions of v1.2.2 and native profiles | Actual host Git HEAD, dirty changes, artifact and test inventory, persisted state |
| Current BOOT-00/U0/01/02 | GitHub-only preparatory cards | Historical BOOT numbering conflict; reconcile authoritative VPS checkpoint before instantiation |

## FUTURE-B03 · Canonical runtime reconciliation and validation (proposed)

**Objective:** turn already-authorized declarative roles into verified live profile bindings without redefining their contracts.

- **Prerequisites:** BOOT-00, U0 backup with restore check, 01 reconciliation, 02 compatibility status, approved role grants.
- **Owner:** Hermes Core as external **operator** for configuration only; ownership of Olympus execution permissions stays with canonical policy.
- **Scope:** verify eight profiles, isolated roots for SOUL/USER/MEMORY, exact model/provider route and account quota; migrate only audited existing config if permitted.
- **Exclude:** cloning Core credentials into Olympus, new god types, changing v1.2.2 roles, activating Telegram dispatch.
- **Acceptance:** profile table matched to actual config plus negative tests for cross-profile memory and cross-owner tools; exact backup/rollback reference.
- **Blockers:** missing native profile API, model quota, unsupported config format or inconsistent local checkout.

## FUTURE-B04 · Governor intake enforcement

**Objective:** enforce Zeus governance as a deterministic gate, not a cosmetic persona.

- **Inputs:** immutable initiative envelope with ID, objective, context, requester, policy scope, idempotency key.
- **Actions:** validate strict canonical Governor schema; `proceed` only to Olympus Hermes, `clarify` requires missing facts, `stop` terminates with reason.
- **Exclude:** Zeus doing domain-owner work, special-case prompt overrides, unauthorized "fast path".
- **Acceptance tests:** allowed, denied, ambiguous, malformed YAML/schema, duplicate initiative, revoked authorization, retry with same key.
- **Evidence:** admitted/denied envelope, source policy version, trace to next owner, no hidden side effects.

## FUTURE-B05 · Olympus Hermes planning and owner-dispatch contract

**Objective:** one orchestrator owns planning and handoff, never other Owners' tools.

- **Inputs:** unchanged Governor output and canonical initiative ID.
- **Actions:** preserve all real work items, unique IDs, dependencies, requested contributions, owner/Lead Owner and approvals; dispatch only validated plan.
- **Exclude:** silently narrowing a multi-owner plan, rewriting blocked work into success, hidden executor fallback.
- **Acceptance tests:** no delegate on non-`ready` handoff, wrong Owner refusal, satisfied/unsatisfied dependencies, cancellation, idempotent resume.

## FUTURE-B06 · Exclusive Domain Owner execution

**Objective:** six separate authorized capabilities and memories, one side-effect owner for each execution.

| Owner | Domain | Example output, never implied blanket privileges |
| --- | --- | --- |
| Apollo | professional_delivery | bounded BA/project deliverable |
| Athena | research_learning | source-backed research |
| Hestia | personal_life | privately scoped personal plan |
| Hephaestus | systems_automation | audited scoped automation |
| Prometheus | experimentation | sandboxed experiment |
| Aphrodite | creative_media | creative artifact |

- **Actions:** grants catalog with executable allowlist, explicit worker scopes and request-to-owner delegation, including minor contributions.
- **Acceptance:** non-owner denies or delegates; correct owner executes; shared discovery does not grant use; cross-memory leakage denied; canceled worker stopped.

## FUTURE-B07 · Native Kanban and durable attempt mapping

**Objective:** reflect canonical work items in native board while preserving immutable initiative/attempt IDs and reviewer verdict.

- **Controls:** source-backed status, dependencies, review lane, ticket owner, finite attempt budget, stop/interrupt, retry with evidence.
- **Exclude:** Kanban status becoming independent approval, model inference as security control, new custom queue when native feature suffices.
- **Acceptance:** duplicates collapse safely, blocked prerequisite prevents downstream action, retry history retained, `PASS` requires linked test output, failed ownership routes to REWORK/BLOCKED.

## FUTURE-B08 · Bounded worker delegation and Planning Room

**Objective:** consultation and temporary contribution without granting permanent capabilities.

- **Actions:** group chat/Planning Room only when multiple specialists demonstrably needed; bounded subtask, explicit objective, allowed tools, provider, timeout, cancellation.
- **Exclude:** worker self-promoting to owner, Planning Room as alternate Zeus approval, indefinite reasoning loops.
- **Acceptance:** single-owner task skips unnecessary room; multi-owner task delegates correctly; failed specialist does not invent result.

## FUTURE-B09 · Capability registry, shared skills and plugin boundaries

**Objective:** reuse approved shared registries and resource lists, not create duplicates.

- **Actions:** resolve local skills first, shared knowledge/catalog next, curated external list last; read content before application; record exact plugin version, provider, privileges, approval, license and origin.
- **Specific reviews:** OMH Restricted Bridge/full OMH, Advanced Delegation, Bot Forge, Agent Importers, Kanban Empowered, native Kanban, nightly memory.
- **Acceptance:** global discovery read-only; no non-owner side effects; incompatible plugin produces BLOCKED and fallback documentation, not auto-install.

## FUTURE-B10 · Memory and Mnemosyne knowledge promotion

**Objective:** protect profile-specific memory while making approved reusable knowledge discoverable.

- **Actions:** distinguish ephemeral task state, agent episodic memory and curated second-brain facts; define universal/galaxy/realm/agent scopes.
- **Evaluation:** whether existing nightly-memory plugin already covers needs; compare Hindsight/Obsidian only against proven needs.
- **Acceptance:** privacy negative test, correction/deletion provenance, retention, restore, no nightly auto-authority change.

## FUTURE-B11 · Telegram, Desktop, WebApp unified communication

**Objective:** maintain one actual backend session/gateway across interfaces with secure routing.

- **Actions:** verify `default` Core via authenticated HTTPS API; one-bot group/topic scheme for viewing and scoped commands; native v0.23 WebApp only after restore-ready backup; preserve old HTTPS Desktop route.
- **Exclude:** Telegram bot self-messages as pseudo-inbound, duplicate polling process, unauthenticated public terminal, destroying old UI/proxy before rollback.
- **Acceptance:** identical approved session/profile response through two clients, unauthorized sender denied, topic/mission association correct, no duplicate action on reconnect.

## FUTURE-B12 · End-to-end UAT, recovery and release readiness

**Objective:** independently validate Olympus without silently launching Mission Control or Cronos.

**Positive scenarios:** intake → Zeus → Olympus Hermes → correct Domain Owner → bounded result; supported dependencies; manual review and RESUME.

**Negative scenarios:** denied governance, conflicting evidence, missing memory namespace, wrong owner, stale ticket, replayed Telegram update, disconnected gateway, exhausted model quota, malformed tool output, failed restore verification.

**Evidence:** action-by-action correlation ID, tool/provider records, offline tests, bounded runtime UAT, replay idempotency, cancel safety, rollback report and explicit human release decision.

## Later independent project drafts (no implementation authorization)

### FUTURE-MC01..04 · Mission Control

- **MC01:** compare three UI designs (Command Bridge, Galaxy Atlas, Mission Studio) using realistic but synthetic missions. Pick a visual system; user reviews.
- **MC02:** validate screen contracts: galaxy switcher, mission panel, vertical Kanban picklists, decision trail, owner capabilities, evidence and model budget.
- **MC03:** wire **read-only** canonical data adapters with permission-denial UX and no duplicate ledger.
- **MC04:** gated control actions and UAT after actual Olympus backend is independently verified.

### FUTURE-CR01..04 · Cronos/Apex

- **CR01:** universal intake schema; distinguish bounded output vs project vs automation vs new galaxy.
- **CR02:** stable initiative ID and idempotency across Telegram/WebApp/Desktop/Mission Control.
- **CR03:** dispatch via Zeus → Olympus Hermes; never global domain tool grants.
- **CR04:** full cross-galaxy UAT, review, rollback and approval before production routing.

## Recommended implementation ordering after explicit scope reopening

```text
BOOT reconciliation + verified backup
  → profile and model integrity (B03)
  → Zeus gate (B04)
  → Hermes planning (B05)
  → owner-scoped tools (B06)
  → native Kanban (B07)
  → bounded specialist delegation (B08)
  → shared capability/plugin scope (B09)
  → memory policy (B10)
  → WebApp + Telegram integration (B11)
  → cross-interface UAT (B12)
  → Mission Control separate project (MC01..04)
  → Cronos/Apex separate project (CR01..04)
```

**Important:** this is a *dependency graph proposal*, not a historical canonical block numbering. Once actual VPS state is known, map these logical packages to existing OLY/Block IDs instead of creating duplicate work.
