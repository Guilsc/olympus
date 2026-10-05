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
| `governor` | Zeus | Minimal declarative governance prompt implemented and validated in Block 1.1 |
| `orchestrator` | Hermes | Minimal declarative orchestration prompt implemented and validated in Block 1.2; no persistent runtime instance |
| `domain_owner` | Apollo, Athena, Hestia, Hephaestus, Prometheus, Aphrodite | Six separately bound declarative Domain/Owner contracts available and validated; see [expansion evidence](realm-expansion.md). No persistent runtime |
| `worker` | None selected | **REFERENCE ONLY**; implementation and operational semantics deferred until a demonstrated delegation need exists |

The [theme configuration](../config/theme.yaml) keeps `governor` → Zeus and `orchestrator` → Hermes and maps all six promoted Domain display names and Owner theme aliases. Narrative aliases do not replace canonical identifiers in decisions or ownership.

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

Hermes names the canonical Olympus `orchestrator` role. The [minimal Orchestrator](orchestrator.md) turns approved intent into bounded, owned, dependency-aware planning state. It selects a minimum useful team and one Lead Owner, facilitates a logical Planning Room, preserves blockers, and judges readiness. Its `planning`, `clarify`, or `ready` result is a machine-readable snapshot suitable for future persistence. Governor routing and Orchestrator handoff are conceptual, not real runtime dispatch. Worker is not part of the current implementation commitment.

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

[Block 1.5](block-1.5.md) executes this vertical slice in isolated native conversations in external Hermes-Main, passing actual raw outputs unchanged. This is host-side validation, not persistent Olympus runtime assembly or production dispatch. The role labels correspond to canonical `governor`, `orchestrator`, and `domain_owner`; Worker is deliberately absent.

## Hermes-Main versus Olympus Hermes

**Hermes-Main** is the external desktop/software execution environment used to build, validate, commit, and publish Olympus. It is not an Olympus agent.

**Olympus Hermes** is only the narrative alias for canonical `orchestrator`. Its declarative role is implemented; its future distinct Olympus-specific runtime instance does not exist yet. There is no third canonical concept derived from the alias. External Hermes-Main functionality must not be presented as an implemented Olympus capability, and Hermes-Main's own identity/profile is not transformed by hosting isolated role evaluations.

## Current technical baseline

The Block 1.2 starting baseline is:

```text
477f0020a95bb28cd16718d50f9d0f0d59025e2b
docs: clarify foundation architecture and technical baseline
```

Block 0.2 established Foundation documentation and the minimal theme mapping. Block 1.1 added [`config/governor.md`](../config/governor.md), evaluated through the existing Hermes-Main native `AIAgent` with no tools, context files or memory, and background review disabled. Input is `initiative.objective`, with optional context only when needed. The documented scenarios validated decisions without tool calls or domain execution.

Block 1.2 adds [`config/orchestrator.md`](../config/orchestrator.md), using the same native no-tools isolation plus no soul identity or trajectory persistence. Input includes the approved initiative, supplied Governor result, synthetic available Owner descriptions, and optional supplied Planning Room contributions. Fifteen fresh final-prompt runs validated the ten required scenarios, including both non-proceed variants and four additional input/routing checks, with no tool calls, specialist execution, Worker creation, or real Domain Owner invocation.

These are model-backed declarative prompts, not deterministic enforcement or external authorization verification. No separate Olympus application stack, dependency manifest, runner, persistent bot, or runtime orchestration has been introduced.

## Planning state and future knowledge

Planning Room is a reusable logical collaboration capability, not an implemented chat service. Each initiative must have isolated context and operational state; host/runtime isolation and persistence wiring remain future work. Initiative State is current scope, ownership, planned work, dependencies, decisions, assumptions, blockers, readiness, and next action. Logs are historical evidence, not canonical current state. Agent Memory is future specialist experience; Shared Second Brain is future reusable organizational knowledge across initiatives/Realms. Neither memory system is implemented. Specialist experience may improve knowledge/capabilities without silently changing identity, responsibility, or authority. A future Board/Mission Control is a view of canonical state, not its source of truth.

## Intentionally not implemented

- Persistent Governor, Orchestrator, or Domain Owner runtime instances, and Worker behavior/configuration/lifecycle. Blocks 1.3/1.4 add the [Domain design contract](domains.md) and [first declarative Owner](domain-owner.md), not runtime assembly.
- Production runtime handoff, external specialist execution, concurrent execution scheduling, or durable initiative persistence. Block 1.5 validates the complete host-side target chain and supplied-fact text inspection/production, not executing apps/software, retrieving research, running experiments, or delivering artifacts externally. Work decomposition, dependency planning, and safe-parallelism judgment remain declarative Block 1.2 semantics.
- An Olympus memory subsystem, skills/capability registry, tool registry, policy engine, permission subsystem, or approval engine.
- Events, a state machine, persistent runtime state, databases, services, APIs, Mission Control/UI, MCP, A2A, or distributed runtime.

Hermes-Main's existing facilities remain external environment facilities, not Olympus implementations. Session 0 is complete. Session 1 Blocks 1.1 and 1.2 are implemented and validated as declarative roles; Block 1.3 promotes and validates the first Domain; Block 1.4 implements and validates its first declarative Owner, separately and together with the Domain contract. [Block 1.5](block-1.5.md) executes end-to-end host-side validation with retained inputs, raw outputs, prompt hashes, assertions and exact results; no persistent Olympus runtime is introduced. Context & Memory is deferred to Session 3, Skills & Capabilities to Session 4, and observability/Mission Control to later sessions. Further implementation requires a separately approved block.

## Current sequential expansion availability

Declarative Domain/Owner contracts currently available: `professional_delivery` / `professional_delivery_owner`, `research_learning` / `research_learning_owner`, `personal_life` / `personal_life_owner`, `systems_automation` / `systems_automation_owner`, `experimentation` / `experimentation_owner`, `creative_media` / `creative_media_owner`. Availability means a definition, not a persistent agent instance, invoked consultation, retrieval, execution or dispatch. Other outcome responsibilities may be named as conceptual routing references.

Expansion validation and reviews are recorded in [the expansion evidence](realm-expansion.md). Earlier Block observations and immutable Block 1.5 evidence remain historical records, not statements that the new Owners were available then. Worker, persistent runtime, memory, capabilities and release automation remain deferred.
