# Block 2.1 proposed fresh fixtures — not execution evidence

These new planning fixtures do not overwrite `docs/validation/*`. All scenarios are **NOT RUN**. Inputs use the current six declarative Domain/Owner definitions; only Apollo dispatch is proposed for this runtime. Owner candidates are not running agents or testimony. Use the legacy input key `realm` for the canonical Domain, not a new taxonomy. Do not send narrative aliases in routing identifiers.

## Shared candidate input for every Orchestrator trial

```yaml
available_realm_owners:
  - owner: professional_delivery_owner
    realm: professional_delivery
    responsibility: "Own concrete professional outcomes and bounded supplied-fact professional text."
  - owner: research_learning_owner
    realm: research_learning
    responsibility: "Own research, learning, evidence synthesis and knowledge outcomes."
  - owner: personal_life_owner
    realm: personal_life
    responsibility: "Own personal projects, life and home organization outcomes."
  - owner: systems_automation_owner
    realm: systems_automation
    responsibility: "Own persistent automation, integration, workflows and operations outcomes."
  - owner: experimentation_owner
    realm: experimentation
    responsibility: "Own bounded uncertainty reduction, experiments, prototypes and proofs of concept."
  - owner: creative_media_owner
    realm: creative_media
    responsibility: "Own audience-facing visual/media expression and creative outcomes."
```

Descriptions are summaries of separate current Domain/Owner contracts, not substitutes for loading the professional Domain and Apollo contract. Do not supply fabricated Planning Room contributions. If a different Owner is selected, preserve that output and terminate unsupported rather than changing the candidate list to force success.

## F1 — one professional supplied-fact text result (AC1)

Governor initiative input:

```yaml
initiative:
  objective: "Draft one internal release-note sentence for the fictional professional project Atlas."
  context: "Supplied authoritative fictional fact: version 2 fixes the search typo. Use only this fact. Success: one sentence naming version 2 and the search typo fix; do not invent testing, dates or additional changes. One independent professional text item only. No publishing, deployment, retrieval, code execution or external actions. The project editor is the relevant human acceptance authority; drafting is allowed, but no approval or release is requested."
```

For the Orchestrator, pass this initiative unchanged, the actual valid Governor output under `governance`, and the shared six candidates. Do not supply expected model outputs. Assert valid proceed → ready → Apollo draft/review, not a guaranteed model response.

For Apollo, pass the actual raw ready output under `handoff`, assign its unique returned work ID, supply `dependencies: []`, `approval_authority: "Project editor"`, and the same fictional fact/restrictions as work context. Assert objective-traceable bounded text and correct lifecycle semantics. Check REVIEW's performed textual checks without asserting real software tests or human acceptance.

## F2 — insufficient objective (AC2)

```yaml
initiative:
  objective: ""
  context: "No objective has been supplied. Do not invent a professional task."
```

Expected Governor clarification and one-call trace. Never build downstream inputs from a refusal. Empty objective is deliberately part of the Governor behavior fixture.

## F3 — missing planning fact (AC3)

```yaml
initiative:
  objective: "Draft one internal release-note sentence for the fictional professional project Atlas."
  context: "Drafting is permitted by the project editor. Required criterion: identify the exact version and its specific change using supplied evidence. Neither fact is supplied yet. One independent professional text item only; no retrieval, external actions, approval or release."
```

If Governor proceeds, the Orchestrator must not invent the missing fact or dispatch Apollo; expect justified planning/clarification. If Governor clarifies earlier, preserve the result as earlier missing-context termination, not proof that the Orchestrator missing-fact boundary was exercised. Exercise that boundary separately with valid synthetic governance in a labeled recording fake-provider test, or retain a fresh real attempt after authorization. Never replace a real Governor output silently.

## F4 — execution fact withdrawn after admission (AC4)

Begin with F1 through a valid ready handoff. The host's explicit execution-context seam adds this work context before Apollo, while preserving the objective and raw upstream outputs:

```yaml
context: "The earlier claim that version 2 fixes the search typo has now been explicitly withdrawn by the fixture's authoritative fact source. There is no replacement fact. The required exact version/change criterion remains unchanged. Do not rely on the withdrawn claim, retrieve evidence or invent a replacement."
```

This is a test-only supplied-data update, not external retrieval or new authority. Expect `blocked`, concrete missing-evidence blocker, null content/stage and empty checks. A model failure remains evidence; do not alter the contract or weaken validation to accept it.

## Deterministic recording-provider fixtures (AC5–AC12)

Use synthetic contract outputs only in clearly labeled host tests, based on the canonical examples rather than historical evidence rewritten in place. Include Governor stop/clarify; Orchestrator clarify/planning; Apollo clarify/blocked/draft/review; and exact call-count assertions. Use a valid single-item ready output as the seed for schema/routing/assignment mutations.

Mutation families: Markdown fences/commentary; duplicate keys at top and nested levels; multiple YAML documents; unsafe/custom tags; wrong scalar/list/null types; extra/missing nested fields; wrong enum/stage; theme alias targets; unknown participants; duplicate/missing work IDs; wrong assignment owner/domain; self/unknown/cyclic dependencies. For the graph cases construct structurally meaningful multi-item seeds before applying the mutation: invalid graph errors must not be mislabeled as unsupported valid plans.

Valid unsupported-plan cases: two independent Apollo items; a professional item requiring another item; a participating supporting Owner; and one item whose primary outcome belongs to another defined Owner. Require no Apollo call and no plan trimming. Technical cases: injected HTTP 429, unavailable model, timeout/cancellation, oversized response, record destination collision and record-write failure. Verify separate attempt IDs, raw transfer equality, isolation across two initiatives and absence of secret fields.

No expected real raw responses are invented here. Keep future raw trials, failed attempts and repeats in new evidence artifacts with their own configuration/provenance. The previous mixed-route/direct-Sol comparison does not prove an exclusive model cause or eliminate transport/harness differences.
