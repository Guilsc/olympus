# Domain contract: personal_life

This is an outcome-oriented Domain / Realm design contract, not an agent role, capability registry or persistent runtime. Canonical identifiers are independent of theme aliases.

```yaml
canonical_domain: personal_life
display_name: Personal
theme_owner: Hestia
primary_outcome: Achieve a bounded personal, household, or life outcome.
owns:
  - Bounded personal, household, home-organization, and life plans aligned to supplied constraints.
  - Practical personal options and tradeoffs, without claiming purchases, bookings, messages, or external
    actions.
does_not_own:
  research_learning: Produce evidence, synthesis, learning, or knowledge.
  systems_automation: Establish a persistent workflow, integration, automation, or operational outcome.
  experimentation: Reduce uncertainty through bounded experimental investigation.
  creative_media: Produce audience-facing visual or media expression.
  professional_delivery: Deliver a concrete professional outcome.
lead_when:
  - The primary intended outcome is achieve a bounded personal, household, or life outcome.
  - This Domain retains outcome accountability if supporting contributions disappear; format and capabilities
    do not define ownership.
collaborates_when:
  - Another Domain owns a bounded supporting contribution; identify the need through orchestration without
    claiming invocation.
  - Another Domain leads and this Domain has an explicitly assigned bounded supporting contribution; preserve
    original outcome accountability.
returns:
  - Bounded assigned personal plan with supplied evidence and honestly performed textual checks.
  - Assumptions, risks, uncertainty, blockers, missing evidence and conceptual routing needs.
  - DRAFT or REVIEW readiness only; producing is not approving and approving is not releasing.
```

Own personal/home/life outcomes, not commercially accountable professional delivery merely because a personal plan resembles project management. Honor household constraints; avoid inventing personal facts or external actions.

Declarative availability of a corresponding Owner does not establish a persistent instance, consultation, execution or external action. Other Domain contracts remain distinct. Hermes-Main remains the external host.
