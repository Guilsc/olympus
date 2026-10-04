# Olympus

Olympus is a system intended to be modular, extensible, governable, and theme-independent. This repository is a clean rebuild; the previous `Olympus_OS` repository is historical reference only, not an implementation or history source for this bootstrap.

Foundation Contract v0.1 is the current architectural baseline. Canonical architecture is separate from the narrative/theme layer and from runtime instances. Block 0.2 established the clean foundation. Block 1.1 implements and validates the declarative `governor`; Block 1.2 implements and validates the declarative `orchestrator`. Both use fresh no-tools evaluations in the external Hermes-Main environment. Block 1.3 promotes and validates the `professional_delivery` Domain (Work); Block 1.4 implements and validates its first declarative `domain_owner`, functional identifier `professional_delivery_owner`, current theme alias Apollo. Domain and Owner contracts remain separate. Block 1.5 executes and records real host-side Governor → Orchestrator → professional_delivery_owner → result chains, with unchanged raw transfers and fresh native no-tools conversations. No persistent Olympus runtime or production dispatch/persistence system exists. Worker remains **REFERENCE ONLY**.

- [Foundation overview](docs/foundation.md): architecture, canonical roles, scope gate, and current technical baseline.
- [Constitution](docs/CONSTITUTION.md): the eight approved stable architectural principles.
- [Architecture](docs/architecture.md): Foundation v0.1 concepts and scope boundaries.
- [Theme](config/theme.yaml): the approved Olympus narrative aliases.
- [End-to-end validation](docs/block-1.5.md): executed host-side chains, exact scenario results, raw evidence, limitations, and the pre-merge gate.
- [Minimal Governor](docs/governor.md): role prompt, native invocation, decision contract, and validation.
- [Specialist Domains](docs/domains.md): first Domain, candidate mappings, artifact lifecycle, and reference-only Lab/workspace concepts.
- [First Domain Owner](docs/domain-owner.md): professional-delivery responsibility, ready-handoff input, bounded result/lifecycle contract, and isolated validation.
- [Minimal Orchestrator](docs/orchestrator.md): specialist-first planning, logical Planning Room, initiative-state contract, conceptual handoff, and synthetic validation.

Construction proceeds through approved blocks. By default, one approved implementation block maps to one atomic Git commit. GitHub serves as the canonical chronological construction history of Olympus, beginning with this foundation commit. Block 0.2 does not implement the first vertical slice.
