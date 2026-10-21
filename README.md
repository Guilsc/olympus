# Olympus

Olympus is an evolving operating model for coordinated AI teams. It explores
how persistent agents can work together without concentrating ownership,
memory, governance, and execution in one oversized assistant.

> **Project status:** active development. The repository is public for
> visibility, cloning, and experimentation, but external contributions are
> temporarily paused while the architecture and runtime boundaries are still
> changing. Contributions will open in a later phase.

## What Olympus is designed to provide

- Explicit responsibility and authority boundaries for every role and domain.
- A Governor for scope and governance decisions.
- An Orchestrator for planning, ownership, dependencies, and handoffs.
- Accountable Domain Owners for specialist outcomes.
- Separation between temporary working context, agent memory, and curated
  shared knowledge.
- Reusable skills, lifecycle policies, escalation paths, and human approval
  boundaries.
- Traceability from a request through decisions, reviews, artifacts, and the
  final result.

The current conceptual flow is:

```text
User -> Governor -> Orchestrator -> Domain Owner -> Result
```

The names from Greek mythology are replaceable presentation aliases. The
canonical responsibilities remain theme-independent.

## Current state

Foundation Contract v0.1 is the architectural baseline. The repository
currently defines and documents:

- the canonical Governor and Orchestrator roles;
- six declarative Domain/Owner contracts;
- bounded handoff, readiness, result, and artifact-lifecycle contracts;
- host-side validation of the professional-delivery chain;
- sequential expansion evidence and known limitations.

Available declarative pairs are:

| Domain | Owner |
| --- | --- |
| `professional_delivery` | `professional_delivery_owner` |
| `research_learning` | `research_learning_owner` |
| `personal_life` | `personal_life_owner` |
| `systems_automation` | `systems_automation_owner` |
| `experimentation` | `experimentation_owner` |
| `creative_media` | `creative_media_owner` |

Availability means a reviewed definition, not a continuously running agent.
Persistent runtime, Workers, durable memory, production dispatch, capability
execution, and release automation remain in development or deferred.

## Documentation

- [Foundation overview](docs/foundation.md)
- [Constitution](docs/CONSTITUTION.md)
- [Architecture](docs/architecture.md)
- [Governor](docs/governor.md)
- [Orchestrator](docs/orchestrator.md)
- [Domains](docs/domains.md)
- [Domain Owner](docs/domain-owner.md)
- [End-to-end validation](docs/block-1.5.md)
- [Sequential expansion](docs/realm-expansion.md)
- [Proposed Block 2.1](docs/block-2.1-plan.md)

The public project page provides a visual overview and additional context:
[guilhermecosta.tech/projects/olympus](https://guilhermecosta.tech/projects/olympus).

## Repository policy

The project is being expanded in small, reviewed blocks. The default branch is
protected, direct history rewrites are blocked, and changes are expected to
arrive through pull requests created by the maintainer or authorized agents.

External pull requests, issues, and review requests are not being accepted yet.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the current contribution status and
[SECURITY.md](SECURITY.md) for private security reporting.
