# Proposed Session 2 / Block 2.1 — minimal local operational text flow

## Status and provenance

**Planning only; implementation is NOT authorized.** This document formalizes the external `olympus-post-pr3-scope.md` proposal against baseline `437a337419bdbb2c3fe383cfdf6bddec7e8af842` (PR #3 merge). No runner, provider adapter, dependency manifest or runtime tests are implemented by this planning PR. No model calls are made.

The repository documents Session 1 Blocks 1.1–1.5, followed by the unnumbered declarative Domain expansion. It defers Context & Memory to Session 3 and Skills & Capabilities to Session 4, but defines no Session 2 block sequence. **Session 2 / Block 2.1 is a proposed number for human approval**, not a recovered or previously approved construction block. Renumbering does not authorize implementation.

Human approval of the scoped architecture exception and explicit implementation authorization are required before coding. Merging documentation alone is not authorization to implement. Merge also requires separate explicit approval.

## Objective and canonical chain

Demonstrate real Olympus-owned, deterministic gated dispatch for one supplied-fact professional text outcome, rather than another external harness conversation. A local command executes synchronously in one process, with one initiative per invocation and fresh isolated role contexts:

```text
User input → governor (Zeus) → orchestrator (Hermes)
           → professional_delivery_owner (Apollo) → bounded result
```

Canonical identifiers control behavior; aliases never select routes or confer authority. Hermes-Main remains the external development environment, not Olympus's orchestrator. `domain_owner` is the canonical handoff target; `professional_delivery_owner` is the specific assigned recipient. Domain and Owner contracts remain separate.

The product is a bounded DRAFT/REVIEW text artifact or an explicit terminal refusal, question, planning requirement, blocker or technical error. It is not initiative acceptance, external delivery, approval, release or evidence of software execution.

## Required bounded scope (conditional on approval)

- One explicitly invoked local entrypoint with explicit input and run-record destination; no daemon, server, UI or background loop.
- A small direct provider adapter using existing native read-only credential resolution. No global installation, profile changes or infrastructure changes.
- Unchanged canonical Governor, Orchestrator, professional Domain and Apollo Owner contracts, loaded from this repository.
- A deterministic validation/dispatch boundary outside the model roles. Model judgment does not authenticate permissions or enforce host policy.
- Exactly one `planned` work item owned by `professional_delivery_owner`, with `depends_on: []`, one participant and Lead Owner `professional_delivery_owner`, and host Owner input `dependencies: []`.
- All six declarative Owner descriptions are supplied as candidates. Only Apollo has executable dispatch support in this block. A valid plan selecting another Owner, multiple items/participants, or dependencies terminates as an unsupported plan. Do not hide available contracts to force Apollo selection.
- A local evidence record owned solely by the runner, not durable canonical Initiative State, Agent Memory or a Delivery Workspace. In-process state exists only during the invocation.
- A documented, explicit host execution-context seam to test a supplied fact becoming unavailable after planning. It must not rewrite the approved objective, raw governance or ready handoff, or silently change authority. Conflicting late facts must be surfaced rather than resolved by invention.

## Strict validation and dispatch rules

Accept a single raw YAML mapping at each role boundary. Reject Markdown fences, surrounding commentary, multiple documents, duplicate mapping keys, unsafe/custom tags, invalid field types, missing/extra schema fields and unsupported structures; do not coerce, strip fences, repair or normalize a response to make it pass. Specify a safe restricted YAML subset and resource limits during implementation; unsupported YAML features fail closed.

Validate the exact output shapes in [`governor`](../config/governor.md), [`orchestrator`](../config/orchestrator.md) and [`professional_delivery_owner`](../config/domain_owners/professional_delivery.md), including nested shapes, allowed enums, nullability, typed lists, canonical identifiers and status-specific invariants. Validate host input against the corresponding contracts before a call; an intentionally empty objective is a documented Governor clarification scenario, not permission to skip input validation elsewhere.

Only valid Governor `proceed` with `next_owner: orchestrator` permits the second call. Only valid Orchestrator `ready` with `next_action: {type: handoff, target: domain_owner}` permits consideration of specialist dispatch. Check bounded scope, original objective, traceable criteria, unique supplied participants, participating Lead Owner, unique work IDs, participating ownership, planned status, valid referenced acyclic dependencies, first action/reason, empty blockers and requested contributions. Then apply the narrower single-independent-professional-item gate.

Build `assignment` with exactly `canonical_domain: professional_delivery`, `owner: professional_delivery_owner`, and the actual unique returned work ID. Do not substitute a fixture ID, silently reassign, execute all Lead Owner work, or narrow a multi-item plan after the fact. Check the assignment against the unchanged handoff before Apollo is invoked. Approval authority is an explicitly supplied string or null under the Owner contract; a label is not authenticated approval evidence.

Carry actual Governor raw YAML into `governance` and actual Orchestrator raw YAML into `handoff`; only reversible envelope indentation/newline changes are permitted. Record and test decoded textual equality and parsed equality. Re-serializing parsed objects is not a substitute for raw preservation. Apollo's result must match the assignment and lifecycle contract; REVIEW requires actual nonempty criterion checks, and refusal/blocker results require null stage/content, empty checks and concrete blockers.

Any rejected gate prevents all downstream calls. No fallback, automatic retry, repair loop, runtime Planning Room, specialist consultation or recursive return to governance is included. `next_owner: orchestrator` in Apollo's output is a canonical return label; the host terminates this invocation without another model call.

## Terminal outcomes (host classifications, not new role fields)

| Observed condition | Host terminal interpretation | Further dispatch |
|---|---|---|
| Governor `stop` | Governance refusal; retain reason | None |
| Governor `clarify` | Minimum missing intent/context/authority question | None |
| Orchestrator `clarify` | Governance/intent/structure clarification needed | None |
| Orchestrator `planning` | Specialist contribution or planning requirement; no Planning Room execution | None |
| Valid ready plan outside bounded subset | Unsupported plan, not a forged role status | None |
| Apollo `clarify` | Assignment/admission/routing correction required | None |
| Apollo `blocked` | Essential execution evidence/resource unavailable | None |
| Apollo `draft` / `review` | Return bounded DRAFT / REVIEW artifact and limitations | None |
| Invalid input/output, transport/auth/provider error, timeout, cancellation or record-write failure | Technical failure with stage and safe diagnostic; never success | None |

DRAFT is mutable; REVIEW is inspection readiness, not APPROVED or RELEASED. A returned artifact is not human acceptance, external publishing, deployment or completion of a broader initiative. Host technical outcomes must not be added to canonical role schemas. A blocked run is not a failed YAML parse; a provider error is not a semantic refusal.

At most three sequential role calls, each at most once. Proposed limits for approval: 120 seconds per call, 360 seconds total invocation deadline, explicit cancellation support, and 1 MiB per raw input/response. No hidden retries. On technical failure retain all prior available evidence; if storage itself fails, emit a safe visible error and never claim a complete persisted record. A new invocation is a new attempt with a new identifier, never an overwrite of the original attempt.

## Evidence and proposed physical configuration

Initial model-backed validation is proposed as **`openai-codex` / `gpt-6.1-sol`, direct**, without a combo, alias route or fallback. Do not probe availability or invoke a model in this planning stage. If later unavailable (including HTTP 429), retain the availability failure and stop; another configuration requires explicit authorization and separately labeled evidence.

Each later run records:

- Unique attempt ID, timestamps, start/end stage, terminal outcome, call order and validation assertions.
- Supplied initiative, available Owner descriptions, authority/context, execution-context updates and exact assembled role inputs.
- Exact raw outputs, parsed snapshots, parse/validation errors, and hashes of input/output bytes and each loaded prompt/Domain contract; use SHA-256 with explicit UTF-8 byte semantics.
- Repository revision, runner revision, direct requested/resolved provider/model, response-reported model/IDs, settings (including sampling and output limits), and isolation switches.
- Whether physical execution is provider-attested or merely requested/resolved/reported. A route name, active chat metadata or configured model alone is not upstream execution attestation; mark unavailable attribution explicitly.
- No credentials, tokens, unrelated host context or hidden personal data. Proposed destination: an explicit caller-selected path outside tracked repository content. Reserve a fresh run directory, refuse overwrites, preserve partial attempts, and finalize the record without pretending local files are immutable against arbitrary user edits. Record redactions explicitly rather than silently modifying evidence.

Role calls must have no tools, host context files, soul identity, memory, background review or trajectory saving. Evidence belongs to the runner only. Native credential handling must remain external; do not copy secrets into Olympus.

Historical validation files stay unchanged. New [fixture specifications](fixtures/block-2.1.md) reflect six defined Owners while distinguishing declarative availability from executable dispatch support. Prior mixed-route failures and direct Sol passes suggest configuration sensitivity; **they do not establish an exclusive model cause or rule out transport/harness differences**. The historical passing corpus is not an implemented dispatcher, a single-shot reliability study or a guarantee for this runner.

## Architecture changes requested for approval

The existing [architecture](architecture.md) anticipates durable persistence alongside future dispatch; the [foundation](foundation.md) explicitly says no runner/application stack exists. This block requests an exception: an Olympus-owned ephemeral dispatcher may execute this three-call subset with local historical records **without** a canonical persistence engine or persistent agents. The existing role prohibition on tools/real invocation still applies to model roles; host-owned dispatch is outside their authority. No role schema or prompt amendment is proposed.

| Item | Scope-gate classification | Boundary |
|---|---|---|
| Planning document and new fixture specifications | REQUIRED NOW | Documentation only in this PR |
| Local synchronous command, direct adapter, strict gates, recording fake-provider test seam, run records | REQUIRED NOW **only after implementation approval** | Minimum executable slice; no framework or service |
| Persistent agents, durable initiative store, multi-item/dependency scheduling, cross-Owner dispatch, Planning Room execution | LIKELY LATER | Not needed for one independent item |
| Context & Memory / Shared Second Brain | LIKELY LATER | Session 3 remains deferred |
| Skills & Capabilities, acquisition or registry | LIKELY LATER | Session 4 remains deferred |
| Mission Control, observability platform, Delivery Workspace, approval/release engine | LIKELY LATER | Local run evidence is not these subsystems |
| Worker role | REFERENCE ONLY | No demonstrated delegation need |
| Event bus, distributed runtime, API/service, automatic retries/fallback, global Hermes/OmniRoute changes | NOT NEEDED | Excluded from this block |

Approval must explicitly accept this exception and the single-item limits. Conditional planning sections do not amend current implemented-state claims or authorize additional subsystems.

## Acceptance criteria and minimum future tests

The fixture file specifies fresh inputs and perturbations, not executed results. All tests below are pending implementation authorization.

| ID | Acceptance criterion / minimum scenario | Evidence required |
|---|---|---|
| AC1 | Supplied fictional search-typo fact produces one Apollo DRAFT/REVIEW text result | Three valid real role outputs, strict gates, actual work-ID assignment; no approval/delivery claims |
| AC2 | Empty objective yields Governor clarification | Exactly one call, no Orchestrator/Apollo call |
| AC3 | Missing planning fact produces Orchestrator planning or clarification as justified | No Apollo call; retained explanation, no invented fact |
| AC4 | Explicit essential fact withdrawal after valid ready admission yields Apollo blocked | Unchanged upstream outputs, explicit late-context input, null artifact/check invariants |
| AC5 | Governor stop, Orchestrator clarify/planning, Apollo clarify all terminate | Recording fake-provider traces, respective schemas and no forbidden next call |
| AC6 | Fences, commentary, duplicate keys, multi-document YAML, unsafe tags, wrong types, missing/extra fields or invalid status/stage fail closed at each boundary | Targeted deterministic boundary tests, including invalid final Owner output not exposed as success |
| AC7 | Wrong route/alias, noncanonical target, malformed assignment, missing work ID, wrong Owner, duplicates, unknown/self/cyclic dependencies fail closed | Mutation tests on valid captured or synthetic contract outputs |
| AC8 | Otherwise valid multi-item, multi-participant, prerequisite or non-Apollo plan is unsupported | No trimming/reassignment and zero Owner dispatch |
| AC9 | Raw transfer integrity and initiative isolation hold | Text/parsed equality and separate invocations with no leaked context |
| AC10 | HTTP 429, unavailable pinned model, timeout, cancellation, oversize response and storage failure terminate technically | Retained partial evidence; no fallback/retry, overwrite or fabricated role status |
| AC11 | Evidence attributes direct requested/resolved/reported physical configuration honestly | No combo, no secrets; unavailable attestation explicit; attempt IDs/hashes/settings present |
| AC12 | Role isolation and no external actions | Recording provider checks and real-call configuration evidence; no tools, memory, retrieval or publication |

Implement deterministic tests with a recording fake provider first; synthetic replies must never be reported as model-backed evidence. Then run the minimum fresh pinned real trials AC1–AC4, separately labeling all attempts and distinguishing model variability from enforcement. Fake-provider tests prove gates, not model behavior. Do not repeat all historical expansion validation: rerun only boundaries affected by new code, failed/unavailable results and relevant Apollo contract cases. Failures remain failures even if later attempts pass; preserve both. Review valid captured result text semantically for assigned outcome, factual scope and authority boundaries, not just schema shape.

## Pending human decisions and implementation prerequisites

1. Approve proposed Session 2 / Block 2.1 numbering and this operational exception, or supply the authoritative next-block sequence.
2. Explicitly authorize a separate implementation task/branch; approve the one-item, three-call, no-resume/no-fallback boundary.
3. Confirm proposed deadlines/size limits and explicit caller-selected outside-repository run-record destination; retention/redaction policy remains to be agreed before real inputs containing sensitive data.
4. Choose the smallest repository-local language/dependency/entrypoint strategy during the authorized task, based on native direct-adapter compatibility. No dependency manifests, adapter prototype or global installation in this PR.
5. Verify native direct provider availability and attribution capabilities only during authorized implementation/validation. Absence of upstream attestation is a reported limitation, not invented certainty.

## Review and delivery gate

Standards and Intent/Spec reviews are separate Hermes-Main self-reviews, not independent reviews. Their exact fixed base/reviewed commit, findings, verification and limitations are recorded in the documentation PR. No runtime acceptance criterion is claimed passed by documentation checks. Stop for explicit approval before any runner implementation; no merge or infrastructure mutation is authorized by this plan.
