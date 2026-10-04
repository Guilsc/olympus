# Domain contract: research_learning

This is an outcome-oriented Domain / Realm design contract, not an agent role, capability registry or persistent runtime. Canonical identifiers are independent of theme aliases.

```yaml
canonical_domain: research_learning
display_name: Studies
theme_owner: Athena
primary_outcome: Produce evidence, synthesis, learning, or knowledge.
owns:
  - Evidence-led synthesis, learning plans, and knowledge explanations within supplied sources and assigned
    scope.
  - Separate supplied evidence, inference, uncertainty, source limitations, and missing retrieval; citations
    identify only supplied excerpts.
does_not_own:
  personal_life: Achieve a bounded personal, household, or life outcome.
  systems_automation: Establish a persistent workflow, integration, automation, or operational outcome.
  experimentation: Reduce uncertainty through bounded experimental investigation.
  creative_media: Produce audience-facing visual or media expression.
  professional_delivery: Deliver a concrete professional outcome.
lead_when:
  - The primary intended outcome is produce evidence, synthesis, learning, or knowledge.
  - This Domain retains outcome accountability if supporting contributions disappear; format and capabilities
    do not define ownership.
collaborates_when:
  - Another Domain owns a bounded supporting contribution; identify the need through orchestration without
    claiming invocation.
  - Another Domain leads and this Domain has an explicitly assigned bounded supporting contribution; preserve
    original outcome accountability.
returns:
  - Bounded assigned evidence synthesis with supplied evidence and honestly performed textual checks.
  - Assumptions, risks, uncertainty, blockers, missing evidence and conceptual routing needs.
  - DRAFT or REVIEW readiness only; producing is not approving and approving is not releasing.
```

Own evidence, synthesis, learning and knowledge as the accepted outcome. A professional-looking report does not change research ownership. Supplied excerpts can support bounded synthesis, not fabricated retrieval or citations.

Declarative availability of a corresponding Owner does not establish a persistent instance, consultation, execution or external action. Other Domain contracts remain distinct. Hermes-Main remains the external host.
