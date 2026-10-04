# Specialist Domains — Block 1.3

## Contract and promotion

A Domain is an outcome-oriented responsibility, not an artifact category or bag of capabilities. Realm is user-facing/domain language; `domain` remains the Foundation term. Keep `canonical_domain`, `display_name`, and `theme_owner` separate. The [professional_delivery contract](../config/domains/professional_delivery.md) promotes the first Domain with primary outcome **Deliver a concrete professional outcome**.

| Canonical Domain | Display | Current theme Owner alias | Status / primary purpose |
|---|---|---|---|
| `professional_delivery` | Work | Apollo | **PROMOTED** — concrete professional accepted outcomes |
| `research_learning` | Studies | Athena | **PROMOTED** — research, learning, evidence, synthesis, knowledge |
| `personal_life` | Personal | Hestia | **PROMOTED** — personal projects and life/home outcomes |
| `systems_automation` | Automations | Hephaestus | **PROMOTED** — persistent automation, integrations, workflows, operations |
| `experimentation` | Lab | Prometheus | **PROMOTED** — uncertainty reduction, experiments, prototypes, PoCs |
| `creative_media` | Creative & Media | Aphrodite | **PROMOTED** — visual/media expression and audience-facing assets |

Promotion defines the Domain contract, not a runtime or Owner role. Block 1.4 separately implements and validates the [first declarative Owner](domain-owner.md); the other five Owners are not available, installed, or instantiated. Zeus (`governor`) and Hermes (`orchestrator`) have Olympus-wide governance/orchestration responsibilities, not specialist Realms. There is no `olympus` Domain.

The generic small Domain / Realm Contract has nine fields:

| Field | Semantics |
|---|---|
| `canonical_domain` | Stable theme-independent responsibility identifier |
| `display_name` | Human-facing Domain name |
| `theme_owner` | Replaceable current theme alias of its Owner, not a role |
| `primary_outcome` | Intended accepted result that anchors accountability |
| `owns` | Outcome-aligned responsibility within assigned scope |
| `does_not_own` | Excluded primary outcomes and canonical routing references |
| `lead_when` | When this Domain is accountable for the overall outcome |
| `collaborates_when` | When bounded supporting contributions are appropriate |
| `returns` | Result, evidence, limitations, and readiness returned to orchestration |

**Routing:** the primary intended outcome determines the Domain, not artifact type, tool, file format, or implementation technique. Secondary test: who remains accountable if supporting contributions disappear? Software plus visual design can remain a professional application outcome with `creative_media` support. A research report, persistent integration, feasibility PoC, media campaign, or household plan instead routes to its corresponding candidate Domain even if Work can technically produce the artifact. Routing references do not create unavailable Owners.

## Universal artifact lifecycle

User-consumable outputs follow `DRAFT → REVIEW → APPROVED → RELEASED`:

- **DRAFT:** mutable working version.
- **REVIEW:** ready for the relevant inspection/validation; not itself approval.
- **APPROVED:** accepted by the relevant authority for release, not necessarily delivered.
- **RELEASED:** final consumable version made available for intended use through explicit release/publish/deploy/delivery action or authorization.

REVIEW depends on the artifact: software tests/preview/UAT, creative visual/content review, automation dry run/test execution, documents editorial/evidence review. Technical environments such as dev/test/UAT/production apply conditionally to artifacts that actually execute; they are not the universal lifecycle. Producing never equals approving; approving never equals releasing. These are contract semantics, not a state machine or filesystem automation.

## Prometheus / Lab — REFERENCE ONLY

Prometheus is the theme alias for the candidate `experimentation` Owner: an experimental/R&D sandbox, not the universal reviewer or QA gate. Two future conceptual modes:

1. **Independent Lab:** a bounded experiment may precede an initiative. It may return hypothesis, prototype, evidence, limitations, risks, and recommendation. Disposition: discard, continue experimenting, or propose promotion. Promotion must pass through the Governor / Zeus as a governed initiative.
2. **Initiative-bound experiment:** an active Domain Owner may identify a bounded uncertainty question for later experimentation. The candidate returns evidence, prototype, limitations, and recommendation. The original production Domain retains initiative outcome ownership.

Neither mode is instantiated here. The first Owner can identify such a need via orchestration, not impersonate Prometheus or claim an experiment ran.

## Delivery Workspace — design contract only

Every future initiative producing user-consumable outputs should expose a predictable human-facing surface conceptually equivalent to:

```text
outputs/<initiative>/
  draft/
  review/
  approved/
  released/

lab/<lab-item>/
  prototype/
  evidence/
  limitations/
  recommendation/
```

No folders, movement, persistent runtime, or release automation are implemented. Delivery Workspace is the human-facing artifact surface; Initiative State is the operational snapshot; Logs are historical evidence; Agent Memory is specialist experience; Shared Second Brain is reusable organizational knowledge. They remain distinct. Mnemosyne / Shared Second Brain remains future Olympus-wide Context & Memory infrastructure; Librarian remains a future Session 3 gateway/steward candidate. Worker is **REFERENCE ONLY**, with no implementation or operational semantics added.

## Complexity Gate

**REQUIRED NOW:** one canonical Domain file and this Domain/design document, the nine-field contract, mapping references, lifecycle boundaries, and isolated validation evidence. The existing theme file needs only the promoted display/alias mapping. The Domain and Owner contracts remain separate even within one initiative.

**REFERENCE ONLY:** five candidate Domains/Owners, Prometheus modes, conceptual Delivery Workspace, Mnemosyne, Librarian, and Worker. **LIKELY LATER:** runtime dispatch/persistence, capabilities, memory, observability, Board/Mission Control. **NOT NEEDED:** a Domain registry service, additional role taxonomy, execution engine, filesystem lifecycle, or dependency manifest. [Block 1.5](block-1.5.md) subsequently executes host-side chain validation without introducing any deferred subsystem.

## Observed validation

Eight fresh isolated native `AIAgent` conversations on the existing `openai-codex` / `gpt-6.1-sol` route passed before Owner implementation. Each used the Domain file as the ephemeral prompt plus a validation-only instruction to return `lead_domain`, `supporting_domains`, and `reason`; this reporting shape is a test fixture, not an additional architectural contract. Settings match [Governor native isolation](governor.md): no tools, context files, memory, soul identity, background review, or trajectory persistence. No conversation history was supplied.

| Scenario / intended outcome | Observed lead Domain | Observed supporting references |
|---|---|---|
| Internal professional project update | `professional_delivery` | None |
| Research evidence synthesis, even as a business report | `research_learning` | None |
| Persistent CRM/billing synchronization, even as business software | `systems_automation` | None |
| Feasibility PoC solely for uncertainty reduction | `experimentation` | None |
| Commercial audience-facing campaign/images | `creative_media` | None |
| Household move, even as a project report | `personal_life` | None |
| Accepted professional booking application plus visual branding | `professional_delivery` | `creative_media` |
| Professional booking application with a bounded load-test uncertainty | `professional_delivery` | `experimentation` |

All eight completed, returned parseable duplicate-key-rejecting safe YAML with exact fields and canonical identifiers, matched expected lead/supporting outcomes, and had empty tool lists and zero returned tool calls. Raw responses were inspected: no Owner, Worker, runtime, subsystem, or deliverable was created. Other Domains remained conceptual references. Inputs, raw responses, and assertions are host-local scratch evidence, outside Olympus. Contract SHA-256 (UTF-8 text with normalized newlines, as read for invocation):

```text
221a50c1413e7e99ad6ba1babdb9ff72fb3bd607ede28efbb00d4e195d4b02fa
```

These are observed model-backed behaviors, not deterministic routing, exhaustive enforcement, authenticated authority, or repeatability guarantees. This is Domain-only validation; Owner validation and pairwise contract consistency are separate Block 1.4 evidence, not Block 1.5 end-to-end execution.

## Current sequential expansion availability

Declarative Domain/Owner contracts currently available: `professional_delivery` / `professional_delivery_owner`, `research_learning` / `research_learning_owner`, `personal_life` / `personal_life_owner`, `systems_automation` / `systems_automation_owner`, `experimentation` / `experimentation_owner`. Availability means a definition, not a persistent agent instance, invoked consultation, retrieval, execution or dispatch. Other outcome responsibilities may be named as conceptual routing references.

Expansion validation and reviews are recorded in [the expansion evidence](realm-expansion.md). Earlier Block observations and immutable Block 1.5 evidence remain historical records, not statements that the new Owners were available then. Worker, persistent runtime, memory, capabilities and release automation remain deferred.
