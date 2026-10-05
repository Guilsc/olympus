# Domain contract: systems_automation

This is an outcome-oriented Domain / Realm design contract, not an agent role, capability registry or persistent runtime. Canonical identifiers are independent of theme aliases.

```yaml
canonical_domain: systems_automation
display_name: Automations
theme_owner: Hephaestus
primary_outcome: Establish a persistent workflow, integration, automation, or operational outcome.
owns:
  - Persistent workflows, integrations, automation and operational outcomes as the primary intended result.
  - Bounded textual workflow designs from supplied mappings, triggers, failure handling and operational
    constraints; explicitly separate design from installation and execution.
does_not_own:
  research_learning: Produce evidence, synthesis, learning, or knowledge.
  personal_life: Achieve a bounded personal, household, or life outcome.
  experimentation: Reduce uncertainty through bounded experimental investigation.
  creative_media: Produce audience-facing visual or media expression.
  professional_delivery: Deliver a concrete professional outcome.
lead_when:
  - The primary intended outcome is establish a persistent workflow, integration, automation, or operational
    outcome.
  - This Domain retains outcome accountability if supporting contributions disappear; format and capabilities
    do not define ownership.
collaborates_when:
  - Another Domain owns a bounded supporting contribution; identify the need through orchestration without
    claiming invocation.
  - Another Domain leads and this Domain has an explicitly assigned bounded supporting contribution; preserve
    original outcome accountability.
returns:
  - Bounded assigned workflow design with supplied evidence and honestly performed textual checks.
  - Assumptions, risks, uncertainty, blockers, missing evidence and conceptual routing needs.
  - DRAFT or REVIEW readiness only; producing is not approving and approving is not releasing.
```

Own persistent/repeatable workflow, integration and operations outcomes, not every technical deliverable. This no-tools producer may describe mappings and a dry-run proposal; a design or proposed dry run is neither installed automation nor a performed dry run.

Declarative availability of a corresponding Owner does not establish a persistent instance, consultation, execution or external action. Other Domain contracts remain distinct. Hermes-Main remains the external host.
