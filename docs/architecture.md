# Architecture — Foundation Contract v0.1

## Architecture separation

- **Canonical Architecture** defines semantic concepts and canonical roles.
- **Theme / Narrative Layer** provides narrative/display aliases for canonical roles, not behavior or authority.
- **Runtime Instance** describes what actually exists or is active once runtime implementation exists. No runtime is implemented in Block 0.2.

Narrative names are aliases. Architectural roles are canonical.

> Theme may decorate architecture, but must never define architecture.

## Naming distinction

- **Hermes-Main** is the external desktop/software execution environment used to build Olympus. It is not an Olympus agent.
- **Hermes** is the Olympus narrative/display alias for the canonical `orchestrator` role, not Hermes-Main.
- **Runtime Instance** of `orchestrator` will be a distinct future Olympus-specific agent instance. Block 1.2 defines and validates the declarative role, not a persistent instance. There is no third canonical role or agent concept named after the theme alias.

This document uses Hermes-Main explicitly for the external environment and Hermes only for the narrative alias, avoiding ambiguity.

## Minimum working vocabulary

- `agent`: an agent concept, distinct from its role and narrative alias.
- `role`: a canonical architectural responsibility.
- `domain`: an outcome-oriented area of responsibility; Block 1.3 promotes `professional_delivery` (display Work, current theme Owner alias Apollo). Other candidate Domains remain reference only; see [Domain contracts](domains.md).
- `initiative`: an undertaking described within the architecture.
- `task`: a unit of work.
- `policy`: an explicit governance constraint.
- `theme`: the narrative/display layer, separate from canonical architecture.

These Foundation terms do not themselves establish runtime entities or full lifecycles. The minimal [Orchestrator contract](orchestrator.md) introduced in Block 1.2 defines only the required initiative planning-state representation and logical interaction semantics, not a runtime platform.

## Canonical roles

Current implementation-facing roles recognized by the foundation:

- `governor`
- `orchestrator`
- `domain_owner`

Recognition is not implementation: none was implemented in Block 0.2. Block 1.1 subsequently implemented and validated the declarative `governor`; Block 1.2 implemented and validated the declarative `orchestrator`. Neither has a persistent Olympus runtime instance. The approved narrative aliases are `governor` → Zeus and `orchestrator` → Hermes. Block 1.3 promotes the `professional_delivery` Domain (Work); Block 1.4 implements and validates its first declarative `domain_owner`, `professional_delivery_owner`, with Apollo only as the replaceable theme alias. Domain and Owner are separate [contracts](domain-owner.md), not persistent runtime instances. Zeus and Hermes remain Olympus-wide roles, not specialist Realms.

### worker — REFERENCE ONLY

`worker` is an approved future architectural role, not part of the current implementation commitment. Its implementation and operational semantics are deferred until a demonstrated delegation need exists. No Worker behavior is defined here.

## Conceptual responsibility lenses

- **Control Plane**: a conceptual lens for governance responsibilities.
- **Agent Plane**: a conceptual lens for agent responsibilities.
- **Capability Plane**: a conceptual lens for capability responsibilities.

These are conceptual responsibility lenses only. They do not currently prescribe folders, services, modules, APIs, processes, runtime components, packages, deployment topology, or infrastructure.

The Governor applies or consults governance. The Governor is not the Control Plane personified.

## First vertical slice boundary

The approved target, exercised as [Block 1.5 host-side validation](block-1.5.md), is:

```text
User
  ↓
Governor
  ↓
Orchestrator
  ↓
Domain Owner
  ↓
Result
```

Governor, Orchestrator, and Domain Owner refer to the canonical `governor`, `orchestrator`, and `domain_owner` roles. Block 0.2 does not implement this flow. Worker is not part of it.

Block 1.2 adds post-governance understanding, minimum-team and Lead Owner selection, individual active work ownership, dependencies, logical Planning Room facilitation, blockers, plan readiness, machine-readable state, and conceptual handoff. Selected Realm Owners advise; the orchestrator makes bounded coordination decisions. It neither overrides governance nor performs specialist work. Block 1.2 planning validation used supplied synthetic specialist descriptions; Blocks 1.3/1.4 subsequently promote and validate the first real Domain and its declarative Owner. The host may describe `professional_delivery_owner` using the existing available-owner input contract (`realm: professional_delivery`); that legacy field denotes the canonical Domain, not a second taxonomy. Other candidate Domains/Owners remain conceptual references. The future runtime must persist state and dispatch work; no actual end-to-end handoff occurred in Blocks 1.2–1.4. Pairwise Domain/Owner consistency validation is not Block 1.5 execution. Block 1.5 now passes actual Governor and Orchestrator outputs unchanged into fresh downstream native role conversations and records the resulting Owner artifacts/refusals. This external host experiment does not implement a persistent Olympus runtime, production dispatcher, persistence or approval/release system.

Planning Room is a reusable logical collaboration capability with separate initiative context/state, not persistent chat infrastructure. Initiative State is the current operational snapshot; Logs are historical evidence; Agent Memory is future specialist experience; Shared Second Brain is future organizational knowledge across initiatives and Realms. The latter two remain deferred, and learning must never silently alter identity, responsibility, or authority. A future Board/Mission Control renders canonical state, never replaces it. Context & Memory, Skills & Capabilities, Workers, observability, and runtime infrastructure are not introduced by Block 1.2.

## Scope review gate

Before introducing a new abstraction, entity, canonical term, file, directory, schema, service, runtime component, agent, interaction type, lifecycle state, infrastructure component, or persistent artifact, classify it as exactly one of:

- `REQUIRED NOW`
- `LIKELY LATER`
- `REFERENCE ONLY`
- `NOT NEEDED`

Only `REQUIRED NOW` items may enter the current implementation.

> What concrete problem does this solve in the current milestone?

If the answer is primarily:

> We may need it later.

defer it.

## Current sequential expansion availability

Declarative Domain/Owner contracts currently available: `professional_delivery` / `professional_delivery_owner`, `research_learning` / `research_learning_owner`, `personal_life` / `personal_life_owner`. Availability means a definition, not a persistent agent instance, invoked consultation, retrieval, execution or dispatch. Other outcome responsibilities may be named as conceptual routing references.

Expansion validation and reviews are recorded in [the expansion evidence](realm-expansion.md). Earlier Block observations and immutable Block 1.5 evidence remain historical records, not statements that the new Owners were available then. Worker, persistent runtime, memory, capabilities and release automation remain deferred.
