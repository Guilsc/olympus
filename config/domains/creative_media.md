# Domain contract: creative_media

This is an outcome-oriented Domain / Realm design contract, not an agent role, capability registry or persistent runtime. Canonical identifiers are independent of theme aliases.

```yaml
canonical_domain: creative_media
display_name: Creative & Media
theme_owner: Aphrodite
primary_outcome: Produce audience-facing visual or media expression.
owns:
  - Audience-facing visual/media expression, creative briefs, campaign copy and media-asset concepts within
    supplied brand/audience constraints.
  - Textual creative direction and copy with explicit distinctions between proposed assets and actually
    generated images/video.
does_not_own:
  research_learning: Produce evidence, synthesis, learning, or knowledge.
  personal_life: Achieve a bounded personal, household, or life outcome.
  systems_automation: Establish a persistent workflow, integration, automation, or operational outcome.
  experimentation: Reduce uncertainty through bounded experimental investigation.
  professional_delivery: Deliver a concrete professional outcome.
lead_when:
  - The primary intended outcome is produce audience-facing visual or media expression.
  - This Domain retains outcome accountability if supporting contributions disappear; format and capabilities
    do not define ownership.
collaborates_when:
  - Another Domain owns a bounded supporting contribution; identify the need through orchestration without
    claiming invocation.
  - Another Domain leads and this Domain has an explicitly assigned bounded supporting contribution; preserve
    original outcome accountability.
returns:
  - Bounded assigned creative brief and copy with supplied evidence and honestly performed textual checks.
  - Assumptions, risks, uncertainty, blockers, missing evidence and conceptual routing needs.
  - DRAFT or REVIEW readiness only; producing is not approving and approving is not releasing.
```

Own audience-facing visual/media expression, even when commercially commissioned. Professional application delivery can retain professional ownership with bounded creative support. Textual briefs/copy do not establish generated images/video, audience testing, publication or a media pipeline.

Declarative availability of a corresponding Owner does not establish a persistent instance, consultation, execution or external action. Other Domain contracts remain distinct. Hermes-Main remains the external host.
