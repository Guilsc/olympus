# Domain contract: professional_delivery

This is an outcome-oriented Domain / Realm definition, not an agent role, capability registry, or runtime instance. `domain` is canonical vocabulary; Realm is user-facing domain language. Theme names confer no authority.

```yaml
canonical_domain: professional_delivery
display_name: Work
theme_owner: Apollo
primary_outcome: Deliver a concrete professional outcome.
owns:
  - Professional initiatives whose accepted result is a usable professional deliverable.
  - Business/project deliverables, software/app/site outcomes, business analysis, reports, presentations, and professional content when serving that professional outcome.
  - Technical implementation required for the accepted professional outcome, within assigned scope.
does_not_own:
  research_learning: Research, learning, evidence, synthesis, or knowledge as the primary outcome.
  systems_automation: Persistent automation, integrations, workflows, or operations as the primary outcome.
  experimentation: Uncertainty reduction through experiments, prototypes, or PoCs as the primary outcome.
  creative_media: Audience-facing visual/media expression, design, images, video, or social media assets as the primary outcome.
  personal_life: Personal projects, life/home organization, or personal outcomes.
lead_when:
  - The primary intended outcome is a concrete professional result; artifact type, tool, format, or technique does not determine ownership.
  - This Domain remains accountable for the requested professional outcome if supporting contributions disappear.
collaborates_when:
  - Another Domain owns a bounded supporting contribution needed for the professional outcome; identify that need through orchestration without claiming its Owner has been invoked.
  - A bounded uncertainty needs experimentation evidence; retain professional outcome ownership and identify the question, not a Prometheus runtime or universal QA gate.
  - Another Domain leads the primary outcome and a professional-delivery contribution is explicitly assigned within scope; do not claim the entire initiative.
returns:
  - Bounded professional result and evidence against the assigned objective and success criteria.
  - Assumptions, risks, blockers, missing evidence, and specialist contribution needs through orchestration.
  - Artifact readiness with approval and release boundaries preserved; producing is not approving and approving is not releasing.
```

Declarative Domain/Owner contracts currently available: `professional_delivery` / `professional_delivery_owner`, `research_learning` / `research_learning_owner`, `personal_life` / `personal_life_owner`. Availability means a definition, not a persistent agent instance, invoked consultation, retrieval, execution or dispatch. Other outcome responsibilities may be named as conceptual routing references. Skills, tools, models, plugins, and integrations are capabilities, not Domain identity. A professional report may belong here; a report whose primary purpose is research belongs to `research_learning`. A software artifact may instead belong to `systems_automation`, `experimentation`, `creative_media`, or `personal_life` according to its intended outcome.
