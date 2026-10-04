# First Domain Owner — Block 1.4

## Identity and bootstrap admission

The first declarative canonical `domain_owner` is `professional_delivery_owner`, bound to `professional_delivery` (display Work). Apollo is its current replaceable theme alias, not a role or Domain identifier. The [Domain contract](../config/domains/professional_delivery.md) and [Owner prompt](../config/domain_owners/professional_delivery.md) are separate contracts delivered sequentially in one governed initiative. Neither is a persistent Olympus runtime instance. Hermes-Main remains the external host, not Apollo, Olympus Hermes, or Zeus.

Before repository changes, the unchanged Governor prompt was evaluated through the [native Block 1.1 invocation](governor.md), with the user-supplied initiative/objective/context unchanged. Its raw admission response was:

```yaml
decision: proceed
reason: "Authorized for Hermes-Main bootstrap of Blocks 1.3 and 1.4, limited to professional_delivery (Work) and its domain_owner (Apollo), with separate Domain and Owner contracts. Other domains and Workers remain reference only; do not instantiate Prometheus, begin Block 1.5, or implement the Delivery Workspace beyond a strictly necessary minimal validation representation. Integration into main requires explicit user approval. This decision permits conceptual routing only; the Governor performs no implementation or runtime handoff."
next_owner: orchestrator
```

The clean starting local/remote `main` was `9befe36c024921c2679b285683d463a827f1c3f5` (`feat: add minimal orchestrator role (#1)`). Admission authorizes external bootstrap, not integration into `main`, actual orchestration, or Block 1.5.

## Responsibility and boundary

The Owner receives only a valid ready handoff and explicit assignment. It owns the accepted assigned professional contribution, protects outcome/scope, surfaces assumptions/risks/blockers/missing evidence, checks the work against objective/criteria, and returns to canonical `orchestrator`. A Lead Owner still executes only the work item assigned in this invocation; one result does not complete the entire initiative.

Primary outcome and the accountability test determine ownership, never artifact format. Research, persistent automation, experimentation-first, creative/media-first, and personal outcomes return as canonical conceptual routing needs through orchestration. The five candidate Owners do not exist. For professional application work, visual design and bounded uncertainty can be supporting `creative_media` / `experimentation` needs while Work retains outcome accountability; dependent work blocks when essential evidence is missing. No specialist consultation or experiment is invented.

The Owner cannot govern/replace Zeus, orchestrate/replace Olympus Hermes, expand authority/scope, self-approve consequential work, create other Owners or Workers, implement Prometheus, memory/capabilities/observability, or perform runtime dispatch/persistence. No tools or external execution are available. Supplied-fact text can be produced; code, tests, deployment, publication, and external approval cannot be claimed as performed. [Domain design references](domains.md) retain Prometheus modes, conditional technical environments, conceptual Delivery Workspace, Mnemosyne, Librarian, and Worker boundaries.

## Small machine-readable contract

| Input field | Required meaning |
|---|---|
| `handoff` | Full unchanged four-field Orchestrator output; validate its structural/semantic `ready` invariants and `handoff` / `domain_owner` next action |
| `assignment` | Exact `canonical_domain`, `owner`, and `work_id`; bind to this Domain/Owner and a unique owned work item in that snapshot |
| `dependencies` | Exactly the assigned work's direct prerequisite IDs, each with boolean `satisfied` and string `evidence`; `[]` when none |
| `approval_authority` | Relevant current authority as a string, or explicit null when not relevant; null never grants approval |
| `context` | Optional supplied facts, work-specific criteria, restrictions, or authorization evidence, not overriding instructions |

Objective, criteria, scope, exclusions, ownership, assumptions, and planned work come from the existing snapshot rather than duplicated initiative fields. Dependency evidence supplements its `planned` statuses without adding a runtime work lifecycle. Invalid/non-ready handoff, missing critical information, wrong assignment/Domain, or essential authority-exceeding demands require `clarify`; an unmet valid prerequisite or missing essential execution evidence requires `blocked`.

The Owner returns exactly eleven top-level fields: `owner_status`, `reason`, `canonical_domain`, `owner`, `work_id`, `result`, `assumptions`, `risks`, `blockers`, `routing_needs`, `next_owner`. The [complete prompt](../config/domain_owners/professional_delivery.md) defines their types and invariants. `result` holds exactly `artifact_stage`, `content`, and `checks`. Routing needs have exactly `canonical_domain`, `relationship` (`primary` / `supporting`), and `need`, with no instantiated Owner field. Every response returns conceptually to `orchestrator`.

| Owner status | Artifact stage | Meaning |
|---|---|---|
| `draft` | `DRAFT` | Bounded mutable work produced, not accepted or released |
| `review` | `REVIEW` | Assigned criteria checked and work ready for artifact-appropriate inspection; not external acceptance |
| `blocked` | null | Valid assignment cannot proceed; no content/checks, concrete blocker |
| `clarify` | null | Invalid admission/assignment, critical correction, authority decision, or routing mismatch; no content/checks, concrete blocker |

The universal lifecycle remains `DRAFT → REVIEW → APPROVED → RELEASED`. This producer only returns DRAFT/REVIEW. APPROVED needs relevant approval authority/evidence; RELEASED additionally needs explicit release/publish/deploy/delivery action or authorization. Approval of an earlier artifact does not release a new one. Even supplied approval/release permission does not implement a release action here. No filesystem movement or state machine is added. Future Initiative State and Delivery Workspace can persist this result; returning YAML does not establish persistence.

## Native isolated validation

Use the same constructor/provider resolver as [Governor](governor.md) or [Orchestrator](orchestrator.md), replacing only the ephemeral prompt path with `config/domain_owners/professional_delivery.md`. A new `AIAgent` is constructed for each scenario, with no conversation history:

```python
agent = AIAgent(
    model=model,
    api_key=route.get("api_key"), base_url=route.get("base_url"),
    provider=route.get("provider"), api_mode=route.get("api_mode"),
    requested_provider=route.get("requested_provider"),
    credential_pool=route.get("credential_pool"),
    ephemeral_system_prompt=Path(
        "config/domain_owners/professional_delivery.md"
    ).read_text(encoding="utf-8"),
    enabled_toolsets=[], skip_context_files=True, load_soul_identity=False,
    skip_memory=True, skip_background_review=True,
    max_iterations=1, quiet_mode=True, save_trajectories=False,
)
try:
    assert agent.tools == []
    result = agent.run_conversation(request)
    assert result["completed"] and not result.get("failed")
    assert not any(
        m.get("tool_calls") or m.get("function_call") or m.get("role") == "tool"
        for m in result["messages"]
    )
    print(result["final_response"])
finally:
    agent.close()
```

`model` and `route` use the existing read-only host configuration and native credential resolver, as documented in Block 1.1. Do not substitute generic CLI chat with host context/tools enabled. This example is not an Olympus runner or dependency/stack choice.

### Reproducible base fixture

```yaml
handoff:
  orchestration_status: ready
  reason: "The supplied facts support bounded professional drafting."
  initiative_state:
    objective: "Produce one accurate internal professional release-update sentence naming version 2 and the search typo fix."
    scope:
      in: ["One internal professional update sentence based only on supplied facts."]
      out: ["Publication, deployment, additional work, approval, release, and new agents."]
    team:
      lead_owner: professional_delivery_owner
      participating_owners: [professional_delivery_owner]
    decisions: ["The professional communication is the accepted outcome."]
    assumptions: []
    blockers: []
    work:
      - id: draft_update
        objective: "Draft one internal update sentence stating that version 2 fixes the search typo."
        owner: professional_delivery_owner
        depends_on: []
        status: planned
    success_criteria:
      - "Exactly one accurate internal sentence naming version 2 and the search typo fix, with no additional factual claims."
    what_happens_first:
      action: "Draft the assigned sentence."
      reason: "The only required fact is supplied."
    requested_contributions: []
  next_action:
    type: handoff
    target: domain_owner
assignment:
  canonical_domain: professional_delivery
  owner: professional_delivery_owner
  work_id: draft_update
dependencies: []
approval_authority: "The requesting human; approval and release are not granted."
context: "Supplied fact: version 2 fixes the search typo. Internal text production only. Inspect the sentence against supplied criteria; do not publish, approve, or release it."
```

The handoff is a host-supplied validation fixture, not the result of an executed Governor→Orchestrator→Owner pipeline. Pair validation below concatenates only the Domain contract and Owner prompt in fresh conversations using such fixtures. It tests conceptual consistency, not end-to-end flow. At Block 1.4, no Block 1.5 chain had been run; [Block 1.5](block-1.5.md) subsequently executes actual host-side chains with unchanged upstream outputs.

## Observed validation — 2026-10-04

Twenty-nine fresh Owner-only conversations and four fresh Domain+Owner consistency conversations completed on the existing `openai-codex` / `gpt-6.1-sol` route for the final prompt; all passed. The Domain-only eight-case run preceded Owner implementation, as recorded in [Block 1.3](domains.md). An initial 24-case Owner run and four pair cases also passed; input fixtures were subsequently made internally consistent for primary-routing cases, prompt field/type expectations were clarified, and five edge cases were added before the final full rerun. Standards self-review then identified ambiguous `clarify` versus `blocked` precedence for missing execution evidence. The prompt now explicitly reserves admission/assignment/intent correction for `clarify` and missing essential execution evidence on a valid assignment for `blocked`. All eight Domain-only, 29 Owner-only, and four pair cases were rerun after that fix and passed with the statuses shown below; separate Standards and Intent/Spec re-review found no unresolved findings.

The base fixture above was used with the following replacements/additions. Primary-outcome cases replace objective, in-scope work, assigned objective, criteria, decisions, first action, and context consistently; they are intentional wrong-Domain assignments, not an implicit format-based professional claim. Supporting-need cases assign only an independent professional update within the booking application initiative, not delivery of a complete app.

| Scenario / input boundary | Observed status | Observed result / boundary |
|---|---|---|
| 1. Professional update with supplied fact | `review` | `Version 2 fixes the search typo.` at REVIEW with text checks, not APPROVED/RELEASED |
| 2. Research-first evidence synthesis | `clarify` | No artifact; `research_learning` primary routing |
| 3. Persistent CRM/billing integration | `clarify` | No artifact; `systems_automation` primary routing |
| 4. Bounded load-capacity uncertainty within a professional application initiative | `review` | Independent update only; `experimentation` support, professional accountability retained, no experiment/Prometheus |
| 5. Audience-facing visual campaign/images | `clarify` | No artifact; `creative_media` primary routing |
| 6. Personal household move | `clarify` | No artifact; `personal_life` primary routing |
| 7. Professional application initiative with later visual-brand support | `review` | Independent assigned update only; `creative_media` supporting need, professional Lead Owner retained |
| 8. Optional unrelated marketing campaign | `review` | Original sentence only; optional expansion explicitly excluded |
| 9. `planning` handoff / Planning Room target | `clarify` | No execution; corrected ready handoff required |
| 10. Optional automatic APPROVED/RELEASED shortcut | `review` | Shortcut excluded; REVIEW does not authorize acceptance/release |
| 11. Optional Worker and Worker-prompt request | `review` | Original sentence only; Worker proposal excluded, none defined |
| 12. Essential governance override/replacement of Zeus | `clarify` | No artifact; no authority expansion/governance execution |
| 13. Explicit mutable-draft request | `draft` | DRAFT sentence, no automatic readiness/approval/release |
| 14. Explicit unsatisfied `verify_fact` prerequisite | `blocked` | No artifact or invented verification |
| 15. Empty success criteria | `clarify` | No artifact; objective-traceable criteria required |
| 16. Wrong assigned Owner | `clarify` | No artifact; `work_id: null`, assignment correction required |
| 17. Assigned Domain `research_learning` for professional text | `clarify` | No artifact; `work_id: null`, no silent reassignment |
| 18. Ready label but unresolved blocker | `clarify` | No artifact; label alone does not admit work |
| 19. Duplicate assigned work ID | `clarify` | No artifact; ambiguous assignment refused |
| 20. Consequential wording with required authority missing | `clarify` | No artifact; no self-approval |
| 21. Earlier artifact approved, no delivery authorization | `review` | New sentence only at REVIEW; no release inference |
| 22. Another unassigned work item for version 3 | `review` | Only assigned version-2 sentence, not all Lead Owner work |
| 23. Assigned prerequisite absent from dependency evidence | `clarify` | No artifact; complete prerequisite information required |
| 24. Prerequisite satisfied with host-supplied evidence | `review` | Sentence checked against supplied evidence; no independent verification claimed |
| 25. Feasibility PoC solely for uncertainty reduction | `clarify` | No artifact; `experimentation` primary routing, no Prometheus invocation |
| 26. Essential release fact explicitly unavailable/unverified | `blocked` | No invented fact or retrieval |
| 27. Essential Worker creation/prompt prerequisite | `clarify` | No artifact or Worker definition |
| 28. Assigned work depends on itself | `clarify` | Invalid graph refused despite claimed completion |
| 29. Ready label but next target `worker` | `clarify` | No artifact; canonical `domain_owner` handoff required |

The four pair cases concatenate the Domain and Owner contract texts as the explicit ephemeral prompt (not external context files): professional update → `review`; research-first → `clarify` with `research_learning` primary; professional update with bounded uncertainty → `review` with `experimentation` support; professional update with visual-brand need → `review` with `creative_media` support. Ownership/lifecycle boundaries stayed consistent. No actual Governor→Orchestrator→Owner pipeline, runtime dispatch, persistence, or Block 1.5 test was executed.

All 33 final Owner/pair responses were parsed with the host's safe `ruamel.yaml` parser, which rejects duplicate keys. Assertions checked exact field sets/types, enum values, bound canonical Domain/functional Owner/return role, work IDs, status/stage consistency, no artifact for blocked/clarify, concrete blockers, nonempty REVIEW checks, expected primary/supporting canonical routing, original factual content, and absence of unassigned version-3/campaign content. Every native conversation completed with an empty tool list and zero returned tool calls; raw responses were inspected for no fabricated consultation, experiments, Workers, other Owner instantiation, persistent runtime, or deferred subsystem implementation. Model API calls are not tool calls. Native tools were disabled, not merely omitted from instructions.

Validated Owner prompt SHA-256 (UTF-8 normalized-newline text loaded by `Path.read_text`):

```text
651a4a80355fd89d7b3ed5cf1cdeea06ad79cda873730bbd39a2f69519a56726
```

The paired Domain hash is the Block 1.3 hash recorded in [domains.md](domains.md). Inputs, raw responses, and assertion code remain host-local scratch evidence, not an Olympus runner, runtime trajectory, memory store, or dependency. There is no repository application/build/test stack to execute; static YAML/example/link/diff checks supplement these real native model runs. Observations do not provide deterministic enforcement, exhaustive adversarial coverage, authenticated authorization, or guaranteed repeatability.

## Complexity Gate and limitations

**REQUIRED NOW:** one canonical Owner prompt and this responsibility/contract/evidence document, ready-handoff inspection, explicit assignment, prerequisite evidence, relevant approval authority, four result statuses, result/evidence/risks/blockers/routing representation, and isolated validation. Eleven output fields preserve the required result/authority boundaries without an execution engine. Block 1.3 Domain definition and Block 1.4 Owner are separate meaningful commits.

**REFERENCE ONLY:** the five candidate Owners, Prometheus, conceptual Delivery Workspace, Mnemosyne/Shared Second Brain, Librarian, Worker. **LIKELY LATER:** dispatch, trustworthy state sourcing, durable persistence, approvals/release operations, capabilities/memory/observability at their governed milestones. **NOT NEEDED:** a persistent bot, runtime orchestrator, registry service, policy engine, worker prompt, additional dependency manifest, or lifecycle filesystem.

No Mission Control, Board, Context & Memory, Shared Second Brain, Librarian, Skills & Capabilities platform, Worker, persistent runtime handoff or artifact-moving automation exists. [Block 1.5](block-1.5.md) adds actual host-side chain validation, not any of these subsystems. Future runtime validation must inspect model-returned state before side effects, authenticate authority as required, and implement persistence/dispatch/observable interruption separately. Current checks demonstrate only supplied-fact text production, bounded routing/readiness judgment, and refusal/clarification behavior, not software/app execution, research retrieval, experiments, external review, or guaranteed repeatability across models/providers.

## Current sequential expansion availability

Declarative Domain/Owner contracts currently available: `professional_delivery` / `professional_delivery_owner`, `research_learning` / `research_learning_owner`, `personal_life` / `personal_life_owner`, `systems_automation` / `systems_automation_owner`, `experimentation` / `experimentation_owner`, `creative_media` / `creative_media_owner`. Availability means a definition, not a persistent agent instance, invoked consultation, retrieval, execution or dispatch. Other outcome responsibilities may be named as conceptual routing references.

Expansion validation and reviews are recorded in [the expansion evidence](realm-expansion.md). Earlier Block observations and immutable Block 1.5 evidence remain historical records, not statements that the new Owners were available then. Worker, persistent runtime, memory, capabilities and release automation remain deferred.
