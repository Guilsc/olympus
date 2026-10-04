# Olympus

Olympus is a system intended to be modular, extensible, governable, and theme-independent. This repository is a clean rebuild; the previous `Olympus_OS` repository is historical reference only, not an implementation or history source for this bootstrap.

Foundation Contract v0.1 is the current architectural baseline. Canonical architecture is separate from the narrative/theme layer and from runtime instances. Block 0.2 established the clean foundation. Block 1.1 implements and validates the declarative `governor`; Block 1.2 implements and validates the declarative `orchestrator`. Both use fresh no-tools evaluations in the external Hermes-Main environment. Block 1.3 promotes and validates the `professional_delivery` Domain (Work); Block 1.4 implements and validates its first declarative `domain_owner`, functional identifier `professional_delivery_owner`, current theme alias Apollo. Domain and Owner contracts remain separate. No persistent Olympus runtime instance, real runtime handoff, or end-to-end flow exists. Worker remains **REFERENCE ONLY**; Block 1.5 is not started.

- [Foundation overview](docs/foundation.md): architecture, canonical roles, scope gate, and current technical baseline.
- [Constitution](docs/CONSTITUTION.md): the eight approved stable architectural principles.
- [Architecture](docs/architecture.md): Foundation v0.1 concepts and scope boundaries.
- [Theme](config/theme.yaml): the approved Olympus narrative aliases.
- [Minimal Governor](docs/governor.md): role prompt, native invocation, decision contract, and validation.
- [Specialist Domains](docs/domains.md): first Domain, candidate mappings, artifact lifecycle, and reference-only Lab/workspace concepts.
- [First Domain Owner](docs/domain-owner.md): professional-delivery responsibility, ready-handoff input, bounded result/lifecycle contract, and isolated validation.
- [Minimal Orchestrator](docs/orchestrator.md): specialist-first planning, logical Planning Room, initiative-state contract, conceptual handoff, and synthetic validation.

Construction proceeds through approved blocks. By default, one approved implementation block maps to one atomic Git commit. GitHub serves as the canonical chronological construction history of Olympus, beginning with this foundation commit. Block 0.2 does not implement the first vertical slice.
