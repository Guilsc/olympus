# Foundation overview

Foundation Contract v0.1 establishes Olympus's architectural vocabulary, stable principles, and scope boundaries. Olympus is intended to be modular, extensible, governable, and theme-independent. This clean rebuild does not import implementation or history from `Olympus_OS`.

The [Constitution](CONSTITUTION.md) contains the eight approved principles; [architecture.md](architecture.md) records the Foundation contract. This overview distinguishes approved concepts from implemented behavior.

## Architecture, theme, and runtime

- **Canonical Architecture** defines semantic concepts and roles.
- **Theme / Narrative Layer** supplies display aliases, not behavior or authority.
- **Runtime Instance** describes what actually exists or is active; recognizing a role does not instantiate it.

> Narrative names are aliases. Architectural roles are canonical.
>
> Theme may decorate architecture, but must never define architecture.

| Canonical role | Olympus alias | Current status |
|---|---|---|
| `governor` | Zeus | Minimal declarative governance prompt implemented in Block 1.1 |
| `orchestrator` | Hermes | Approved role; implementation deferred |
| `domain_owner` | None selected | Approved role; no first domain or Domain Owner implemented |
| `worker` | None selected | **REFERENCE ONLY**; implementation and operational semantics deferred until a demonstrated delegation need exists |

The [theme configuration](../config/theme.yaml) contains only `governor` → Zeus and `orchestrator` → Hermes. Narrative aliases do not replace canonical identifiers in decisions or ownership.

## Conceptual responsibility planes

- **Control Plane:** a lens for governance responsibilities.
- **Agent Plane:** a lens for agent responsibilities.
- **Capability Plane:** a lens for capability responsibilities.

These are conceptual lenses, not prescribed folders, services, modules, APIs, processes, runtime components, packages, or deployment topology. The Governor applies or consults governance; it is not the Control Plane personified.

## Governor / Zeus and Orchestrator / Hermes

The [minimal Governor](governor.md) evaluates an initiative and returns `decision`, `reason`, and `next_owner`:

- `proceed`: a clear, permitted request with required authority can reasonably enter the workflow; `next_owner` is canonical `orchestrator`.
- `stop`: an explicit policy violation, prohibited action, deliberate restriction bypass, or demand for the Governor to perform work outside its governance-only responsibility; `next_owner` is `null`.
- `clarify`: the objective, important context, required authority, or structural handling path is insufficient; `next_owner` is `null`, and `reason` identifies the minimum missing information.

Zeus governs but does not execute the initiative, decompose work, select a Domain Owner, choose tools or models, or orchestrate a runtime. It may recommend future structural evolution, but cannot create it autonomously.

Hermes names the approved Olympus `orchestrator` role, which remains unimplemented. A Governor decision naming `orchestrator` is conceptual ownership, not an executed handoff. Worker is not part of the current implementation commitment.

## Complexity Gate

The Foundation's scope review gate classifies every proposed new architectural or implementation item as exactly one of:

- `REQUIRED NOW`
- `LIKELY LATER`
- `REFERENCE ONLY`
- `NOT NEEDED`

Only `REQUIRED NOW` items enter the current implementation. Ask: **What concrete problem does this solve in the current milestone?** If the answer is primarily **We may need it later**, defer it. Complexity must be earned by demonstrated need.

## First target flow

```text
User → Governor → Orchestrator → Domain Owner → Result
```

This is the approved future first vertical slice, not an implemented end-to-end flow. The role labels correspond to canonical `governor`, `orchestrator`, and `domain_owner`; Worker is deliberately absent.

## Hermes-Main versus Olympus Hermes

**Hermes-Main** is the external desktop/software execution environment used to build, validate, commit, and publish Olympus. It is not an Olympus agent.

**Olympus Hermes** is only the narrative alias for canonical `orchestrator`. The future internal orchestration agent is also referred to as Hermes-agent in existing documentation; it does not exist yet. External Hermes-Main functionality must not be presented as an implemented Olympus capability.

## Current technical baseline

The validated implementation baseline before this documentation update is:

```text
e411167a234e423845943f2c1b0fd3d0f8848a32
feat: add minimal governor role
```

Block 0.2 established Foundation documentation and the minimal theme mapping. Block 1.1 added [`config/governor.md`](../config/governor.md), evaluated through the existing Hermes-Main native `AIAgent` with no tools, context files or memory, and background review disabled. Input is `initiative.objective`, with optional context only when needed. The documented scenarios validated decisions without tool calls or domain execution.

This is a model-backed prompt, not deterministic policy enforcement or external authorization verification. No separate Olympus application stack, dependency manifest, runner, or runtime orchestration has been introduced. This update changes documentation only.

## Intentionally not implemented

- Orchestrator/Hermes, a first Domain Owner or domain, and Worker behavior, configuration, or lifecycle.
- Runtime handoff, work decomposition, domain execution, parallelism, or the complete target flow.
- An Olympus memory subsystem, skills/capability registry, tool registry, policy engine, permission subsystem, or approval engine.
- Events, a state machine, persistent runtime state, databases, services, APIs, Mission Control/UI, MCP, A2A, or distributed runtime.

Hermes-Main's existing facilities remain external environment facilities, not Olympus implementations. Block 1.2 has not started; further implementation requires a separately approved block.
