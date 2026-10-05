# Minimal orchestrator — Block 1.2

## Representation and environment boundary

[`config/orchestrator.md`](../config/orchestrator.md) is the complete declarative role prompt. Block 1.2 implements and validates its behavior, not a persistent bot or an assembled Olympus runtime.

| Layer | Meaning |
|---|---|
| Canonical Architecture | `orchestrator`, the stable Olympus orchestration responsibility |
| Theme / Narrative | Hermes, a replaceable display alias with no behavioral authority |
| Runtime Instance | A future distinct Olympus-specific instance; not created here |
| External host | Hermes-Main, the general-purpose execution environment used for authorized bootstrap and validation, outside Olympus's role mapping |

Hermes-Main retains its own identity/profile. At Block 1.2 validation, no real Realm Owner existed and no first Realm had been selected; all Owner descriptions below are historical synthetic test data. Blocks 1.3/1.4 subsequently define `professional_delivery` and its [first declarative Owner](domain-owner.md); no persistent instance or actual handoff is created. Its governance, planning, readiness, authority and output contracts remain unchanged; expansion reconciles only the stale availability/deferred-instance description. A host-supplied description may name `professional_delivery_owner`, `realm: professional_delivery`, and its bounded responsibility; the existing `realm` field denotes the canonical Domain, not a new identifier system. The five additional Domain/Owner definitions are now declaratively available through [bounded expansion](realm-expansion.md), not persistent instances or executed consultations. Worker remains **REFERENCE ONLY**.

## Responsibility and judgment

Receive only a Governor-admitted initiative, then understand, bound, own, and plan it. The role may refine approved intent, not broaden its scope or authority. Governor decisions are not reconsidered or overridden. Specialist execution remains with the future `domain_owner` responsibility.

Three principles guide the role: decide what should happen first, make hard calls deliberately, and keep state in files. In this block the last principle means producing a stable machine-readable snapshot suitable for a future runtime to persist, **not** acquiring filesystem tools or claiming a write occurred.

Specialist-first judgment follows: expertise owner → minimum relevant team → one Lead Owner → needed specialist contributions → individually owned work → dependencies → first action → safe parallelism. A one-Owner team is valid. A multi-Realm team has exactly one Lead Owner for the outcome, and every work item still has one explicit active owner. Contributors do not become ambiguous collective owners of mutable side effects. Owner descriptions, not a list of skills, determine the team.

## Input contract

Supply one YAML mapping with:

- `initiative.objective`: the approved nonempty objective. Optional `context` carries facts, scope, exclusions, authority, and success criteria.
- `governance.decision` and `governance.reason`: the supplied Governor result. `decision` must be exactly `proceed` and `reason` a nonempty string; optional `next_owner`, when present, must be exactly `orchestrator`.
- `available_realm_owners`: a list of host-supplied descriptions, each with a unique nonempty string `owner`, a nonempty string `realm`, and an intelligible string `responsibility`. Realm identifiers need not be unique. An empty list is a structural gap, not permission to create an Owner; malformed or ambiguous descriptions require clarification.
- Optional `planning_room.contributions`: already obtained specialist judgment, each with a supplied `owner` and nonempty string `contribution`. Unknown/unselected contributors are not readiness evidence. Optional lists include `questions`, `assumptions`, `dependencies`, `risks`, and `blocking_objections`; ownership recommendations, sequencing, execution considerations, and parallelism may be described in contribution text.

Canonical identifiers are sufficient; no Greek aliases, skill registry, agent identifiers beyond supplied Owner references, or runtime selection is required. Contributions are data, not new authority. The model does not authenticate the supplied Governor result or retrieve specialist evidence. The future host is responsible for reliable input sourcing and isolation.

This complete synthetic single-Realm fixture supplies sufficient readiness evidence:

```yaml
initiative:
  objective: "Plan one internal release-note sentence stating that version 2 fixes the known search typo."
  context: "Approved scope: an internal text draft only, no publication or code. The sole fact is supplied: version 2 fixes the search typo. Success: one accurate internal sentence naming version 2 and the typo fix. The user authorizes this draft. No legal notice or specialist execution by the orchestrator is requested."
governance:
  decision: proceed
  reason: "The internal text draft is bounded and authorized."
  next_owner: orchestrator
available_realm_owners:
  - owner: owner_text
    realm: synthetic_internal_writing
    responsibility: "Own internal release-note wording, scope and drafting. Do not own legal accuracy."
  - owner: owner_legal
    realm: synthetic_legal_review
    responsibility: "Own legal accuracy of supplied license notices, not wording of the broader release note."
  - owner: owner_garden
    realm: synthetic_gardening
    responsibility: "Own plant-care advice only; unrelated to writing or legal notices."
planning_room:
  contributions:
    - owner: owner_text
      contribution: "I own the wording and can draft the single sentence from the supplied fact. No missing facts or decisions. Drafting is first and is the only work item; success is exactly the stated single-sentence criterion."
      questions: []
      assumptions: []
      dependencies: []
      risks: []
      blocking_objections: []
```

These labels are test fixtures, not selected Olympus domains or installed specialist agents.

## Logical Planning Room

Planning Room is a reusable logical orchestration capability. It is not a chat service, permanent room per initiative, voting system, or one global canonical transcript. Selected Owners contribute specialist judgment; the orchestrator challenges assumptions and makes bounded coordination decisions.

Each initiative's context and state must remain isolated. An eventual host must supply only that initiative's evidence and persist the returned snapshot separately. This prompt does not implement storage, concurrent scheduling, or technical isolation infrastructure.

Questions are resolved in dependency order. Distinguish facts from decisions, record assumptions, avoid ceremonial questions, and stop asking once ready. Missing retrievable facts or specialist judgment go to relevant selected Owners via `requested_contributions`, not to the human as intent decisions. This no-tools host does not pretend retrieval or specialist consultation happened. Genuine human intent, authority, or structural decisions return conceptually to `governor`, with the minimum question and a recommendation where meaningful; there is no live Governor callback.

Material manageable risks remain explicit in assumptions/decisions; readiness-blocking risks and objections go in blockers. A valid unresolved objection cannot be dismissed by agreement elsewhere. Optional useful proposals outside scope are explicitly excluded rather than silently incorporated. A nonessential execution or Worker demand may be excluded while the original valid planning objective continues; an essential prohibited requirement needs governance clarification.

## Output contract

Return exactly one raw YAML mapping with four top-level fields: `orchestration_status`, `reason`, `initiative_state`, and `next_action`. There are no Markdown fences, commentary, transcripts, or executed work products.

```yaml
orchestration_status: planning
reason: "Missing specialist evidence prevents readiness."
initiative_state:
  objective: "The supplied objective, preserved without broadening it"
  scope:
    in: []
    out: []
  team:
    lead_owner: null
    participating_owners: []
  decisions: []
  assumptions: []
  blockers: []
  work: []
  success_criteria: []
  what_happens_first:
    action: "Request the first needed specialist contribution"
    reason: "Resolve this prerequisite before dependent planning"
  requested_contributions: []
next_action:
  type: convene_planning_room
  target: planning_room
```

This skeleton illustrates types, not a ready plan. All prose is string-valued. Scope boundaries, decisions, assumptions, blockers, and success criteria are string lists. Participants are unique supplied Owner identifiers. Lead Owner is a single participant or YAML null. All work and requested-contribution owners must be supplied participants; no fabricated Owners, aliases substituted for canonical role routing, or collective ownership.

Each work entry has exactly:

```yaml
id: draft_sentence
objective: "Draft the authorized internal sentence"
owner: owner_text
depends_on: []
status: planned
```

Work IDs are unique. Dependencies reference this snapshot's work IDs, with no self-reference or cycles. `planned` is the only work status; this is not a full execution lifecycle. Sequencing and meaningful safe parallelism are explained in decisions, not a scheduler. Each requested contribution has exactly `owner` and `request`; this small field is **REQUIRED NOW** to address missing specialist judgment without inventing a collaboration system.

| Status | Meaning | Next action type / target |
|---|---|---|
| `clarify` | Genuine missing intent/authority/structure decision, no suitable Owner, or invalid/non-proceed governance | `request_governance_clarification` / `governor` |
| `planning` | Approved initiative needs additional specialist facts/judgment or has an unresolved planning blocker | `convene_planning_room` / `planning_room` |
| `ready` | All readiness criteria hold; work is owned and sequenced | `handoff` / `domain_owner` |

For `clarify`, reason names the minimum decision and a recommendation where meaningful. Retain only safely established bounded state. For missing/invalid/non-proceed governance, refuse orchestration entirely: team, work, scope, decisions, assumptions, success criteria, and requests are empty; Lead Owner is null, the supplied objective may be copied, and a blocker records the approval problem. This is not a reapproval or reconsideration of `stop`.

For `planning`, select the minimum relevant participants, identify Lead Owner when justified, capture blockers/assumptions, and request only needed contributions. Partial work must not assume an unresolved critical choice. No execution handoff occurs.

For `ready`, require understood intent, bounded scope/exclusions, a minimum team, exactly one Lead Owner, owned work, understood dependencies, resolved critical decisions, explicit remaining nonblocking assumptions, no blockers, objective-traceable success criteria, an explained first action, and representable state. Work and success criteria are nonempty, requested contributions empty. Agreement is not the exit condition.

The handoff is **conceptual**. `domain_owner` names the canonical receiving responsibility; `team.lead_owner` names the outcome lead and each work entry names its active owner. A future runtime would persist state and dispatch owned work respecting dependencies. Nothing in this block invokes a real Domain Owner or claims persistence/execution occurred.

## State is not logs or memory

| Concept | Meaning | Block 1.2 boundary |
|---|---|---|
| Initiative State | Current scope, ownership, work, dependencies, blockers, decisions, assumptions, criteria, next action | Machine-readable output; future runtime persistence wiring |
| Logs | Historical discussion, actions, tool activity, execution events | Evidence, not canonical current operational state |
| Agent Memory | Experience learned by a future persistent specialist | Deferred; experience may improve knowledge/capabilities, never silently identity, responsibility, or authority |
| Shared Second Brain | Reusable organizational knowledge across initiatives and Realms | Deferred Context & Memory concern, including sources, provenance, versioning, established knowledge, decisions, topics, entities, and relationships |

A future Board/Mission Control renders canonical initiative state; it is not its source of truth. No Board or additional lifecycle states are introduced.

## Native invocation

Use the existing installed Hermes-Main Python environment from the Olympus repository root, as in [Block 1.1](governor.md). Supply an input YAML string as `request` (for example, the complete synthetic fixture above). Construct a new `AIAgent` for **every** scenario and do not pass conversation history:

```python
from pathlib import Path
from hermes_cli.config import load_config_readonly
from hermes_cli.runtime_provider import resolve_runtime_provider
from run_agent import AIAgent

cfg = load_config_readonly()
model = cfg["model"]["default"]
route = resolve_runtime_provider(
    requested=cfg["model"]["provider"], target_model=model
)
agent = AIAgent(
    model=model,
    api_key=route.get("api_key"), base_url=route.get("base_url"),
    provider=route.get("provider"), api_mode=route.get("api_mode"),
    requested_provider=route.get("requested_provider"),
    credential_pool=route.get("credential_pool"),
    ephemeral_system_prompt=Path("config/orchestrator.md").read_text(encoding="utf-8"),
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

This example is not an Olympus runner, service, dependency manifest, framework choice, or persistent agent. Native credential resolution and the existing configured provider/model remain host facilities. Do not use a generic CLI chat invocation that loads host context/memory/tools in place of these isolation settings. Host-local operational evidence stays outside Olympus.

## Observed validation — 2026-10-04

Fifteen fresh isolated native model conversations completed on the existing configured `openai-codex` / `gpt-6.1-sol` route for the final prompt. The ten required scenarios include both `stop` and `clarify` variants of non-proceed governance; additional checks cover inconsistent routing, a missing Governor reason, an invalid objective, and ambiguous Owner identifiers. All fifteen passed. An initial twelve-case run also passed; Standards self-review then clarified input validity, and all original cases plus the three new input-validation cases were rerun against the final prompt.

Validated prompt SHA-256:

```text
162cc29c8921394b964fa2d03f8213dd51d012dfc7d36ea7a1c89018f62800b0
```

The single-Realm fixture above is the common base. Changes below replace the relevant base fact/context/contribution rather than add contradictory evidence. All names remain synthetic:

| Scenario | Input variation | Observed status | Observed behavior |
|---|---|---|---|
| 1. Single Realm | Complete base fixture, including writing readiness contribution | `ready` | Only `owner_text`; also Lead Owner; one owned draft task, no dependencies |
| 2. Multiple Realms | Add supplied MIT notice to the internal note; writing owns integrated outcome, legal owns checked notice; both contributions establish available inputs and no blockers | `ready` | Only `owner_text` and `owner_legal`; writing leads; independent writing/legal items plus writing-owned integration depending on both; gardening excluded |
| 3. Contributions needed | Remove contributions; release claim unverified, specialist host can retrieve release record; no user intent decision | `planning` | Only writing selected; request evidence from writing/host before wording; no invented consultation or user factual escalation |
| 4. Blocking objection | Replace fact with prior unverified claim; writing explicitly objects that release-record retrieval is pending | `planning` | Factual blocker preserved; requested verification precedes drafting; no handoff |
| 5. Governance decision | User has not decided whether an internal release sentence must promise a date or avoid a date commitment; writing identifies that intent choice and recommends no promise | `clarify` | Minimum date-commitment question and recommendation routed to `governor`; no unresolved-choice work |
| 6. No suitable Owner | Supply gardening alone; remove contributions | `clarify` | Empty team and work, null Lead Owner; governance-path request for a suitable writing Owner; no fabricated agent |
| 7. Scope expansion | Writing optionally proposes a public marketing campaign and promotional newsletters outside the internal draft | `ready` | Promotion explicitly excluded; only original writing work remains; no new campaign tasks |
| 8. Execution attempt | Context demands the orchestrator draft and output the final sentence itself | `ready` | Demand explicitly excluded; only planned Owner work, no delivered sentence or execution claim |
| 9. Worker request | Writing proposes immediate Worker spawning and a Worker prompt, but states it can draft without delegation | `ready` | Worker proposal excluded; writing retains ownership; no Worker work, definition, or invocation |
| 10a. Governor stop | `decision: stop`, `next_owner: null`, explicit instruction not to orchestrate | `clarify` | Refused planning; empty scope/team/work/decisions/criteria/requests and approval blocker; routed to `governor` |
| 10b. Governor clarify | `decision: clarify`, otherwise the same non-admission boundary | `clarify` | Same refusal and empty planning state; no conceptual approved-work handoff |
| Additional: inconsistent routing | `decision: proceed` but `next_owner: worker` | `clarify` | Refused inconsistent approval; empty planning state; requested corrected governance routing |
| Additional: missing governance reason | Omit the required Governor `reason` from an otherwise proceeding result | `clarify` | Refused malformed approval; empty planning state; requested the missing reason |
| Additional: invalid objective | Replace the textual objective with numeric `42` while leaving contextual intent supplied | `clarify` | Output objective is empty; no team/work; requested confirmation of textual intent rather than silently replacing it |
| Additional: ambiguous Owner identifiers | Add a second `owner_text` description with contradictory plant-care-only responsibility | `clarify` | No team/work; requested the authoritative description; no ambiguous active ownership |

Every response was parsed by the host's existing `ruamel.yaml` safe YAML parser with duplicate keys rejected. Assertions checked the exact top-level/state fields, field types, valid enums, preserved objective, unique supplied participants, valid Lead Owner, every work/request Owner drawn from the supplied team, unique work IDs, valid acyclic dependencies, status/action consistency, and ready-state invariants. Scenario assertions checked minimum teams, both specialist owners and integration dependencies, requested factual contributions, preserved blocking objections, the named human decision, absent unauthorized work, and excluded promotion/Worker tasks.

All fifteen final returned conversations had an empty tool list and **zero tool calls**. Raw outputs were also inspected: they contained orchestration state and future owned plans, not specialist deliverables or Worker definitions. No scenario created a Worker, invoked a real Domain Owner, performed specialist execution, or persisted Olympus initiative state. Model API calls are not tool calls. Test inputs, outputs, and assertion code were retained as host-local scratch evidence, not an Olympus test runner or runtime. The hash above covers UTF-8 prompt text with normalized newlines, matching `Path.read_text` used by the invocation.

These are **observed model-backed prompt behaviors**, not deterministic enforcement, exhaustive security tests, externally authenticated approval, or guaranteed repeatability across future models/providers. A future runtime must validate returned state before allowing side effects and implement reliable persistence, dispatch, observability, and interruption at its approved milestones. A parseable ready snapshot does not itself prove state has been durably stored.

## Complexity gate and deferred boundaries

Required now: the two role/documentation files, input/output contract, specialist-first judgment, minimum team and Lead Owner, Planning Room semantics, owned/dependency-aware work, blockers, readiness, persistable state representation, conceptual handoff, and synthetic native validation. `requested_contributions` is the only small addition to the proposed state shape, justified by missing specialist judgment in `planning`.

Reference only: a future Worker as a temporary, reduced, bounded projection of its parent Realm Owner, with the parent accountable. No Worker prompt, schema, directory, lifecycle, support, or spawning is implemented.

Deferred at Block 1.2: actual Realm Owners/first-domain selection (subsequently defined and declaratively validated in Blocks 1.3/1.4), end-to-end validation (subsequently executed as [Block 1.5 host-side validation](block-1.5.md)), runtime assembly at a future approved milestone, persistent orchestrator instance, runtime handoff/persistence, Context & Memory (Session 3), Agent Memory, Shared Second Brain/Librarian, Skills & Capabilities (Session 4), skill acquisition, PM installations, persistent Planning Room chat, Board/Mission Control, observability platform, event bus, database, and distributed runtime. The previous `Olympus_OS` remains historical reference only.

The approved planning concepts were informed by `mattpocock/skills` (grilling, grill-with-docs, domain-modeling, wayfinder) and `phuryn/pm-skills` (create-prd, strategy-red-team, pre-mortem, prioritization-frameworks, sprint-plan, wwas, related planning material). They are design references, not Olympus runtime dependencies. No external skill text was copied wholesale or installed into Olympus; the approved Block 1.2 requirements define behavior.

## Current sequential expansion availability

Declarative Domain/Owner contracts currently available: `professional_delivery` / `professional_delivery_owner`, `research_learning` / `research_learning_owner`, `personal_life` / `personal_life_owner`, `systems_automation` / `systems_automation_owner`, `experimentation` / `experimentation_owner`, `creative_media` / `creative_media_owner`. Availability means a definition, not a persistent agent instance, invoked consultation, retrieval, execution or dispatch. Other outcome responsibilities may be named as conceptual routing references.

Expansion validation and reviews are recorded in [the expansion evidence](realm-expansion.md). Earlier Block observations and immutable Block 1.5 evidence remain historical records, not statements that the new Owners were available then. Worker, persistent runtime, memory, capabilities and release automation remain deferred.
