# Olympus

Olympus is a system intended to be modular, extensible, governable, and theme-independent. This repository is a clean rebuild; the previous `Olympus_OS` repository is historical reference only, not an implementation or history source for this bootstrap.

Foundation Contract v0.1 is the current architectural baseline. Canonical architecture is separate from the narrative/theme layer and from runtime instances. Block 0.2 established the clean foundation. Block 1.1 adds only a declarative `governor` role, evaluated through the existing Hermes-Main environment; no Olympus runtime orchestration or domain execution is implemented.

- [Constitution](docs/CONSTITUTION.md): the eight approved stable architectural principles.
- [Architecture](docs/architecture.md): Foundation v0.1 concepts and scope boundaries.
- [Theme](config/theme.yaml): the approved Olympus narrative aliases.
- [Minimal Governor](docs/governor.md): role prompt, native invocation, decision contract, and validation.

Construction proceeds through approved blocks. By default, one approved implementation block maps to one atomic Git commit. GitHub serves as the canonical chronological construction history of Olympus, beginning with this foundation commit. Block 0.2 does not implement the first vertical slice.
