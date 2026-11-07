# Senior specialist execution and architecture-change review policy

> **Status:** bootstrap execution rule; supplements the existing Olympus Constitution and v1.2.2 architecture without changing canonical roles, identities or runtime behavior. Added 2026-11-07 for review in draft PR #12.

## Senior specialist standard by task

The executor selects a task-appropriate **working discipline** and quality bar, not a new persistent agent identity, authority or SOUL:

| Work type | Expected working discipline | Minimum quality bar |
| --- | --- | --- |
| Requirements, documentation, traceability | Senior Business Analyst / Senior Technical Writer | Exact source provenance, versioning, explicit assumptions, consistent glossary, Given/When/Then criteria when applicable, practical UAT and audience-fit |
| Architecture and integration | Senior Solution Architect | Compatibility with approved design, constraints, quality attributes, failure modes, tradeoffs, security and migration/rollback implications |
| VPS/containers/HTTPS/operations | Senior Platform Engineer / SRE | State inventory before mutations, backup, idempotency, observability, least privilege, rollback and live health evidence |
| Credentials, plugins, MCP and identity | Senior Security Architect | Trust boundaries, permission minimization, threat model, secret redaction and auditable authorizations |
| Tests, acceptance and reviews | Senior QA/Test Architect | Deterministic tests, negative paths, evidence-to-goal traceability, independent review when necessary and explicit untested gaps |
| Backlog, Kanban and delivery | Senior Product / Delivery Lead | Dependency-aware incremental scope, clear goals, acceptance gates, outcome metrics and no duplicate work |

These are **lenses for producing professional-quality deliverables**. They do not create extra Olympus gods, change the governor/orchestrator/domain-owner contract, or grant cross-domain skills. Olympus's exclusive capability owner remains responsible for its side effects.

## Architecture freeze

The previously approved v1.2.2 topology, role boundaries, exclusive capability ownership, phase order and canonical terminology remain the default. Documentation may clarify these decisions; it must not quietly redefine them. An interesting alternative is not enough to justify architecture modification.

An exception may be considered only for a **material** blocker, demonstrated incompatibility, critical security/correctness flaw or untenable operational constraint that cannot reasonably be handled within the existing design.

Before implementing an exception:

1. **Prepare an ADR proposal** with affected canonical contracts, current-state evidence, problem and severity, no-change option, alternative options, tradeoffs, compatibility, security, cost, migration and rollback.
2. **Spawn or route to a genuinely independent Senior Architect reviewer** (separate worker/context, with access to the relevant approved contract and evidence). Request adversarial scrutiny, not automatic agreement.
3. **Document the review** with reviewer identity/context provenance, evidence inspected, objections, residual risks and a recommendation. Repeating a critique inside the same context is not independent review.
4. **Explicit human approval is mandatory after independent review and before architectural implementation**. A favorable review does not grant authority. If spawn unavailable, mark `REVIEW BLOCKED`, preserve the proposal and continue nonarchitectural independent tasks.

Review is advisory and may not directly execute another Domain Owner's mutable capabilities. No runtime role substitution or privilege expansion is implied.

## Architecture change gate template

```yaml
change_type: ARCHITECTURE_EXCEPTION
status: PROPOSAL_ONLY
approved_baseline: "Olympus / Universe v1.2.2"
problem:
  evidence: []
  material_impact: ""
alternatives:
  - name: "no change"
    tradeoffs: []
  - name: "bounded change"
    tradeoffs: []
security_considerations: []
migration_plan: []
rollback_plan: []
independent_senior_architect_review:
  status: NOT_STARTED
  reviewer_context: null
  objections: []
  recommendation: null
human_architecture_approval:
  status: NOT_REQUESTED
implementation_authorized: false
```

## Execution implications

- No speculative architecture refactor to reconcile stale repository documents.
- No silent creation of a new Control Plane service, global registry, Kanban replacement, all-powerful god or competing Mission Control authority.
- Run normal coding/documentation tasks under the existing v1.2.2 contract with appropriate senior standards and test gates.
- Continue other independent tasks while a proposal awaits architect review or human authorization.
- The executor must report accurately whether it actually invoked an independent reviewer, rather than claiming an imagined review.

## Relationship to prior project sources

- [Constitution](../CONSTITUTION.md): canonical roles, bounded authority, one active side-effect owner, interruption and observability.
- [Bootstrap reconciliation](2026-11-07-reconciliation.md): live-versus-historical evidence distinctions and pre-Block-3 boundary.
- [Acceptance / recovery tests](acceptance-and-recovery-tests.md): test evidence and negative gates.
- [Open-loop register](open-loop-register.md): continuation when a task or model is blocked.
