# Vertical Kanban picklist and initiative hierarchy specification

**Status:** future UX/operational draft, not a running Kanban board or authorized native-plugin modification. Scope covers the user's request for a vertical picklist and initiative→work hierarchy while keeping **Hermes native Kanban** as the execution mechanism. Mission Control is only a later presentation layer; Cronos/Apex intake is even later.

## Product decision

Use a vertically navigable **hierarchical work picker** on the left, with focused board and evidence detail in the center/right. Do **not** spawn new persistent canonical roles or data services simply to display hierarchy.

The effective hierarchy must derive from approved existing initiative/mission and native Kanban identities:

- Galaxy (view scope, e.g. Olympus, Curatia, generic outputs) → Initiative or Project → Mission/Goal → Work item → Attempt/review.
- Project is optional; bounded outputs do not require a new project.
- An item may be seen in multiple filtered views, but only one canonical mutable owner may execute it.
- Worker attempts are append-only evidence, not independent missions.
- The vertical picker MUST be a **view** of canonical state, not a second workflow engine.

## Layout A: Compact hierarchy picker (recommended)

```text
┌─ GALAXY / INITIATIVE ──────┬─ WORK BOARD ─────────────────────┬─ EVIDENCE / REVIEW ─────┐
│ [All galaxies ▼]           │ [Overview] [Board] [Graph]      │ BOOT-01                  │
│ 🔎 Search...               │                                 │ Owner: Core/default      │
│ ▾ Olympus                  │ TODO     RUNNING     REVIEW     │ Goal & acceptance       │
│   ▾ Bootstrap              │ ┌──────┐ ┌──────┐ ┌─────────┐   │ Dependencies             │
│     ▸ BOOT-00              │ │Audit │ │     │ │    ...  │   │ [Evidence] [Tests]      │
│     ▸ BOOT-U0 🔒           │ └──────┘ └──────┘ └─────────┘   │ PASS/REWORK/BLOCKED      │
│     ▸ BOOT-01              │                                 │                         │
│     ▸ BOOT-02              │ [Show blocked only □]           │ Action: Request Review  │
│   ▸ Future blocks (draft)  │                                 │                         │
│ ▸ Curatia                  │                                 │                         │
│ ▸ Generic Outputs          │                                 │                         │
└────────────────────────────┴─────────────────────────────────┴─────────────────────────┘
```

### Vertical picker behavior

1. Default to current galaxy + last selected initiative; persist only a harmless UI preference, never tool permissions.
2. Expand/collapse nodes via keyboard, mouse and accessible controls. Single click selects, no implicit execution.
3. Display clear statuses: `Draft`, `Ready`, `Running`, `Review`, `Blocked`, `Done`, `Suspended`. Canonical backend state may differ; maintain an explicit *view mapping*, not state rewriting.
4. Each node: display title, canonical identifier, status, owner badge, review/blocked count and unmet dependency indicator. Never include model raw reasoning, private memory, API keys or full SOUL in titles.
5. Search across visible authorized nodes only; no side-channel revealing private galaxy names.
6. Filter by galaxy, owner, blocked, awaiting review, timeframe and approved model (if known); all filters are nonmutating.
7. Parent initiative progress aggregates only evidence-backed completed work. A count of subcards moved to Done is not necessarily an approved business result.
8. If selected node is hidden by a new filter, show a non-destructive banner and nearest visible parent. Do not reset user context.
9. Selecting a different galaxy resets scoped navigation only, not a running job or pending approval.
10. On narrow mobile view, picker becomes an overlay/drawer with explicit return to selected card; tool actions remain gated.

## Board semantics and review gates

| Display status | Meaning | Move permitted by |
| --- | --- | --- |
| Draft | Future proposal, no execution grant | Documentation owner; no runtime dispatch |
| Ready | Inputs and owner resolved, dependencies passed | Approved planner or operator, according to current policy |
| Running | Authorized task is executing | Dispatcher with idempotent run receipt |
| Review | Evidence submitted, not yet accepted | Worker may request review; cannot self-approve |
| Blocked | Concrete missing resource, policy denial, model failure or dependency | Deterministic gate/reviewer, with blocker code |
| Done | Accepted task goal with test/review evidence | Authorized review/approval workflow |
| Suspended | Initiative paused without deleting work | Authorized operator/owner with preserved history |

- A draggable card move is a **request** to the authoritative workflow, never a direct privilege elevation.
- Changing a Kanban column must not bypass Zeus governance, missing Domain Owner, required approval or model quota gate.
- Unknown backend status maps to `Unknown` with a warning, never silently to Ready/Done.
- A user-created **future draft** cannot appear Running or Done without an independent live artifact.

## Initiative picker and native Kanban integration

**Keep native Hermes Kanban and the optional Kanban Empowered as separate capabilities.** Native Kanban retains work dispatch/history; Empowered may add Active/Suspended/Done initiative-level controls after source compatibility/security review. A future Mission Control picker only reads authorized board APIs with normalized display fields.

```text
UI Selection
  -> authorized read-only board endpoint
  -> canonical card/mission references
  -> visible hierarchy + evidence

UI action (future and separately approved)
  -> authenticated server-side authorization
  -> idempotent command receipt
  -> underlying owner-controlled runtime dispatch
  -> status update from actual source of truth
```

Do not implement this by scanning private chat history or replicating native Kanban's database. Require server-side authorization on every query, including counts and search.

## Synthetic UX dataset for prototype (never pretend live)

```json
{
  "galaxy": "olympus",
  "initiative": {"id":"demo-bootstrap","title":"Olympus recovery","state":"draft"},
  "items": [
    {"id":"BOOT-00","title":"Read-only VPS inventory","state":"blocked","owner":"core-default","depends_on":[]},
    {"id":"BOOT-U0","title":"VPS recovery backup","state":"blocked","owner":"core-default","depends_on":["BOOT-00"]},
    {"id":"BOOT-01","title":"Reconcile source of truth","state":"draft","owner":"core-default","depends_on":[]},
    {"id":"BOOT-02","title":"Plugin/runtime compatibility","state":"draft","owner":"core-default","depends_on":["BOOT-00"]}
  ]
}
```

The sample mirrors current *planning labels* and an **unverified** live state; before creating actual cards reconcile the conflicting historical BOOT numbering on the real VPS.

## Acceptance checklist

- [ ] Scrollable vertical picker supports 100+ cards without losing keyboard focus or selected item.
- [ ] Screen reader announces hierarchy depth, name, state, owner and action availability.
- [ ] Selecting card changes detail view but cannot start execution.
- [ ] Cross-galaxy unauthorized cards are absent, including counts/search.
- [ ] Blocked cards show precise blocker and next reviewer/permission requirement.
- [ ] Dependency status cannot be bypassed by drag/drop, dropdown or API replay.
- [ ] Every attempted execution shows a distinct attempt ID, model/provider, live host/session evidence and cancellation path.
- [ ] Reviewer UI exposes original goal, evidence, tests, diff, verdict and missing evidence.
- [ ] Session refresh preserves filters/selection without double-submitting a mutation.
- [ ] Mobile vertical picker and three-pane desktop UI behave consistently.
- [ ] Unknown/failed backend requests show explicit error without optimistic Done.
- [ ] Snapshot and rollback are available before any eventual native plugin state migration.

## Which design to pair with the picker?

**Mission Studio** is the preferred structural prototype: vertical hierarchy left, work board center, evidence/approvals right. Use **Command Bridge**'s dense progress strip for operations and **Galaxy Atlas**'s recognizable galaxy switcher without decorative visual noise.

## Implementation separation

**Now, within authorized pre-Block-3 scope:** document the contract, mock data and acceptance tests, audit existing native Kanban plugin capabilities read-only when access returns.

**Later after approval:** build a clickable front-end prototype (separate Mission Control project), use read-only adapters first, then audited execution controls after actual Olympus runtime readiness. Do not deploy a new Kanban engine or enable bot-derived privileged actions.
