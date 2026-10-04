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
- **Hermes-agent** refers to the future internal Olympus orchestration agent. It does not exist yet and is not created in this block.

This document uses Hermes-Main explicitly for the external environment and Hermes only for the narrative alias, avoiding ambiguity.

## Minimum working vocabulary

- `agent`: an agent concept, distinct from its role and narrative alias.
- `role`: a canonical architectural responsibility.
- `domain`: an area of responsibility; no first domain is selected.
- `initiative`: an undertaking described within the architecture.
- `task`: a unit of work.
- `policy`: an explicit governance constraint.
- `theme`: the narrative/display layer, separate from canonical architecture.

These terms do not establish schemas, lifecycles, interaction semantics, or runtime entities in this block.

## Canonical roles

Current implementation-facing roles recognized by the foundation:

- `governor`
- `orchestrator`
- `domain_owner`

Recognition is not implementation: none is implemented in Block 0.2. The approved narrative aliases are `governor` → Zeus and `orchestrator` → Hermes. No Domain Owner alias is selected.

### worker — REFERENCE ONLY

`worker` is an approved future architectural role, not part of the current implementation commitment. Its implementation and operational semantics are deferred until a demonstrated delegation need exists. No Worker behavior is defined here.

## Conceptual responsibility lenses

- **Control Plane**: a conceptual lens for governance responsibilities.
- **Agent Plane**: a conceptual lens for agent responsibilities.
- **Capability Plane**: a conceptual lens for capability responsibilities.

These are conceptual responsibility lenses only. They do not currently prescribe folders, services, modules, APIs, processes, runtime components, packages, deployment topology, or infrastructure.

The Governor applies or consults governance. The Governor is not the Control Plane personified.

## First vertical slice boundary

The approved future target is:

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
