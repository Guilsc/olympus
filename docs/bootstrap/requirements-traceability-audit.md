# Olympus Universe v1.2.2 — requirements traceability and open-loop audit

> Draft audit, 2026-11-07. This is an **evidence-separated checklist**, NOT an implementation authorization, a live VPS inspection, a validated second-brain design or a claim that full conversation history has been exhaustively indexed.
>
> Evidence classes: **APPROVED** = user decision/constraint; **PROPOSED** = not approved for runtime; **GITHUB VERIFIED** = actual remote file/PR/test run; **HOST REPORTED** = older VPS/assistant report, not live reverified; **UNVERIFIED** = still needs evidence. Status defaults to *OPEN* until a success artifact and review can be linked.
>
> The **only current operational objective** is recovery and preparation through BOOT-00/BOOT-U0/BOOT-01/BOOT-02, with a stop **before Block 3**. Future Mission Control and Cronos phases may be designed in draft form but not implemented or deployed. Never silently turn a UI concept into another authority, datastore or service.

## 0. Pre-flight: status and chronology hazards

- [ ] **Reconcile the authoritative source revision.** Remote GitHub `main` currently describes Foundation Contract v0.1 and the older Session 1 / Session 2 numbering; separate previous VPS reports describe a v1.2.2 branch with OLY-01...07 changes. **Do not equate labels or assume reported commits exist on remote.**
- [ ] **Reconcile conflicting block labels from prior checkpoint files**: some older notes label BOOT-00 as backups and BOOT-U0 as inventory, while the current PR #12 card plan labels BOOT-00 as inventory and BOOT-U0 as backup. Resolve against the effective approved spec *before writing native cards*, retaining historical aliases and never silently rewriting card IDs.
- [ ] **Resolve the actual Hermes version and runtime topology.** User previously initiated an upgrade; do not schedule another update or restart until current server and Desktop versions and the v0.23 WebApp are read from real runtime.
- [ ] **Distinguish five-hour session budget from weekly Sol quota.** User reported five-hour window at 100%, weekly allowance exhausted; never claim model available from UI/session timing.
- [ ] **Keep secrets out of all public GitHub artifacts.** A Telegram BotFather token appeared in chat and must eventually be rotated with managed downtime/rollback; do not propagate it into scripts, commands, URLs, job metadata, logs or reports.
- [ ] **Understand automation boundaries.** A scheduled ChatGPT turn is not automatically a VPS/Work/Desktop executor. Each run must establish actual tool provenance and append meaningful evidence or a precise BLOCKED state.

## 1. Canonical architecture and governance checklist

- [ ] [APPROVED] Maintain the three independent layers **Canonical Architecture → Theme/Narrative → Runtime Instance**. Theme names/colors never confer role, routing, tools or permissions.
- [ ] [APPROVED] Preserve the eight constitutional principles in `docs/CONSTITUTION.md`: canonical roles, theme separation, earned complexity, unique mutable side-effect owner, bounded authority, chat as interface, distinct capability/skill/memory/policy/artifact, and observable interruptible background work.
- [ ] [APPROVED] Preserve **Zeus = governor**, **Olympus Hermes = orchestrator**, six specialized Domain Owners; **Hermes Core `default`** is an *external* generalist bootstrap/operator, not Olympus Hermes.
- [ ] [APPROVED] Domain ownership is **exclusive** even for small contributions; non-owners delegate through Olympus Hermes, not borrow another god's privileged tool. Side-effect grants are enforceable by runtime policy rather than natural-language prompts.
- [ ] [APPROVED] Distinguish conceptual **Control Plane / Agent Plane / Capability Plane** lenses from deployed servers. No extra permanent planes/services without demonstrated need and ADR.
- [ ] [APPROVED] Preserve operating sequence **Cronos/Apex universal intake → Zeus governance → Olympus Hermes planning/ownership → Domain Owners → bounded results**, once future phases are implemented.
- [ ] [APPROVED] Preserve independent projects/galaxies: Olympus first; Mission Control interface second; Cronos/Apex intake third. Curatia remains its own galaxy; generic outputs need a bounded workspace rather than forcing a new galaxy per request.
- [ ] [APPROVED] Support fast/bounded vs governed vs galaxy-specific routes only within authority limits; do not bypass Zeus for initiatives because a shortcut is convenient.
- [ ] [APPROVED] Shared discovery/capability registry may span projects, but actual capability execution grants are scoped to owning profile/realm/project. Reuse existing custom MCP/capability platform and resource list; avoid parallel competing registries.
- [ ] [APPROVED] Humans retain final approvals for privileged mutations, releases, external changes and architectural exceptions. Separate planner, worker, reviewer and approver authority.
- [ ] [APPROVED] Architecture freeze: only propose a material change with evidence, alternatives, ADR, independent second Senior Architect (real separate context) and explicit human approval before implementation.

## 2. Profiles, themes, skills and knowledge

- [ ] [HOST REPORTED] Verify eight *actual native Olympus profiles*: `olympus-zeus`, `olympus-hermes`, `olympus-apollo`, `olympus-athena`, `olympus-hestia`, `olympus-hephaestus`, `olympus-prometheus`, `olympus-aphrodite`; separate `default` Core identity.
- [ ] [APPROVED] Preserve each profile's **SOUL / USER / MEMORY** and any auxiliary storage, provider route, session IDs and no cross-profile writable memory aliasing. A declarative contract alone is not a live profile.
- [ ] [APPROVED] Map canonical Domain/Owner from `config/theme.yaml`: Apollo Professional Delivery, Athena Research & Learning, Hestia Personal Life, Hephaestus Systems & Automation, Prometheus Experimentation, Aphrodite Creative & Media. Use replaceable Greek visuals/themes for display only.
- [ ] [APPROVED] For each profile record approved skills/tool allowlist, dependencies, runtime grant, and scope `global discovery / project / realm owner / ephemeral task`. Do not clone Hermes Core secrets or privilege grants to gods.
- [ ] [APPROVED] Skills lookup order: locally installed/owned skills → Hermes knowledge/shared registry → approved dynamic GitHub resource list; new resources require trust/license/compatibility review before execution.
- [ ] [APPROVED] Preserve existing SharedWorkspace guidance and custom Composio MCP. Historical skill catalog entries do not prove full skill content is retrievable or executing.
- [ ] [PROPOSED] Mnemosyne/second brain: investigate whether the nightly-memory plugin already covers required reflective consolidation; compare Hindsight vs Obsidian only after checking real stores, privacy and retrieval needs. Avoid auto-promoting unreviewed reflections into authority.
- [ ] [PROPOSED] Memory scopes: universal / galaxy / realm / agent; private by default, shared knowledge by explicit review and promotion. Define provenance, retention, correction and access-control policies before implementation.

## 3. Execution / Kanban / evidence / safety

- [ ] [APPROVED] Hermes Core `default` handles initial administrative recovery via existing native Kanban, **without** unnecessarily bringing Zeus, Olympus Hermes or Planning Room into the bootstrap itself.
- [ ] [APPROVED] One idempotent card/attempt ID per goal, traceable to immutable objective, owner, inputs, dependencies, tools, model and evidence.
- [ ] [APPROVED] Each card: goal → bounded action → deterministic tests → independent reviewer where available → PASS/REWORK/BLOCKED; a blocked prerequisite must not block independent documentation or non-mutating analysis.
- [ ] [APPROVED] Reviewer cannot grant execution permissions. REWORK requires evidence of actual progress and finite budget/time/iteration limits; no arbitrary two-retry policy or invisible endless loop.
- [ ] [APPROVED] Installed OMH / OMH Restricted Bridge mechanisms are to be **inspected**; don't assume autonomous retry or disable unused plugins before actual usage review.
- [ ] [APPROVED] Bootstrap strategy **Install First, Enable on Demand, Cleanup Later**, but installation, enablement and new privileges still require verification of actual compatible versions, backup and explicit authorization where relevant. Keep already installed plugins available.
- [ ] [APPROVED] Verify plugin candidates: Advanced Delegation (Olympus Hermes scoped), Bot Forge (controlled manager/provisioner), Agent Importers (dry-run staging), Kanban Empowered optional additive layer, native group-chat Lead Bot, capability registry connectors, memory tools, themes and core native tools.
- [ ] [APPROVED] Do not disable or swap provider routes to compensate for unavailable Sol; a comparable model must be verified, with provenance, spend limit and operator authorization.
- [ ] [APPROVED] Human-visible run state, interruption/cancellation, auditable decisions, restore documentation and UAT per block are required.
- [ ] [GITHUB VERIFIED] Pre-Block-3 test plans, negative cases and per-card gates are documented in PR #12; **no live VPS tests are claimed**.

## 4. VPS, desktop, HTTPS, bot and WebApp

- [ ] [APPROVED] Operate live infrastructure **only on actual VPS through Hermes VPS HTTPS**, with SSH **to same VPS** secondary. No Windows/Workspace Local scripts, backups or deployment; do not assume a generic cloud browser is the VPS.
- [ ] [APPROVED] Preserve existing container volumes, history, profiles, memories, active Telegram sessions, proxy, Coolify and OmniRoute; no speculative restart/upgrade.
- [ ] [APPROVED] Verify `hermes-gateway.guilhermecosta.tech` as existing **Hermes Dash Gateway**, and the internal gateway listener before any URL changes.
- [ ] [APPROVED] Target `hermes.guilhermecosta.tech` for native Hermes v0.23 WebApp; community WebUI retirement later, only after TLS, authentication, WebSocket, same-session queue and restore/rollback tests.
- [ ] [APPROVED] Retire `gateway.guilhermecosta.tech` only when proven redundant; never delete the actual backend listener with a cosmetic public dashboard route.
- [ ] [APPROVED] Preserve Desktop connections; a prior direct `connections.json` edit broke remote entries. Windows JSON backup is not a VPS backup.
- [ ] [APPROVED] Verify **Telegram CLI and Desktop same actual Hermes runtime** where expected, no parallel duplicate pollers. Auth and capability policy must be consistent across interfaces, without broad default tools.
- [ ] [GITHUB VERIFIED] Connected Composio Telegram bot identity and outbound message 808 to owner confirmed; this is **not** an incoming command or proof of VPS action.
- [ ] [APPROVED] Telegram one-bot/many-profile **group/topics** design should reuse Infrastructure & Operations, Research & Learning, Projects & Integrations, Olympus, Hermes & AI Agents, Planning & Inbox; actual topic IDs and who receives messages require verification.
- [ ] [HOST REPORTED] An older second Telegram/Codex bot exists in conversation; do not assume identical to newly created bot or alive. Direct `getChat`/send by username from connected Hermes bot returned `chat not found`, not successful ingress.
- [ ] [APPROVED] Prefer authenticated HTTPS/API/WS ingress to Hermes Core `default` over bot self-messages; if testing bot-to-bot, confirm actual group, BotFather mode and allowlists without creating duplicate pollers or increasing admin privileges.
- [ ] [GITHUB VERIFIED] Isolated draft PR `Guilsc/universal-agent-bot-hub#4` adds synthetic bot-originated ingress tests; CI passed but **does not** verify Telegram-to-VPS execution.
- [ ] [APPROVED] Control actions should preserve Telegram message/chat/topic/user IDs for idempotency and map to the same canonical mission/attempt; Telegram history is never canonical state.

## 5. Mission-first and future project planning (DRAFT ONLY)

- [ ] [APPROVED AS DIRECTION] One universal Mission/Intent/Result contract and stable identity across clients. Categorize user requests into **Output / Project / Automation / Galaxy** with promotion criteria, not everything becomes a project.
- [ ] [APPROVED AS DIRECTION] Galaxy selector and fast/governed/galaxy paths; explicit readiness and owner handoff. Cronos is universal intake, **not** an Olympus governor, executor or a second source of domain permission.
- [ ] [APPROVED AS DIRECTION] Mission ledger with durable event/decision history, idempotent intake and resume, dependency graphs, review statuses and approval boundary. Distinguish implementation source of truth from Kanban view/chat.
- [ ] [APPROVED AS DIRECTION] Deliver bounded outputs to an existing generic workspace or initiate a new project/galaxy only when approved classification demands it.
- [ ] [PROPOSED] Mission Control is a separate generic + galaxy UI with initiative status, agent health, task board, live coordination, attempts/retries, approvals, capabilities, memory, costs, observability and **Decision Trail**. UI is not another control-plane service.
- [ ] [GITHUB VERIFIED] Three future design directions are in PR #12: Command Bridge, Galaxy Atlas, Mission Studio; visual selection and simulation remain pending. No ChatGPT Project created by this automation.
- [ ] [PROPOSED] UX acceptance includes mobile/voice navigation, cross-galaxy switch, signed-in permissions, per-owner action buttons, fallback offline state, accessibility and responsive design.
- [ ] [PROPOSED] Later separate Cronos/Apex service, Mission Control app and Curatia integration must inherit approved universal capabilities without globally granting specialist owner tools.
- [ ] [PROPOSED] Formalize future Project→Galaxy promotion and handoff to independent project repositories; work output should retain source, provenance and acceptance evidence.

## 6. Delivery quality, CI, operations and user communication

- [ ] [APPROVED] Senior specialist lens per task (BA/writer, Architect, SRE, Security, QA, Developer, Delivery Lead), **not** impersonated new persistent Olympus agents.
- [ ] [APPROVED] Before any stop: reread relevant conversation decisions, prior plans, recent git changes, run/checkpoint evidence and this inventory; choose another authorized high-value task unless all are blocked/done/need explicit approval.
- [ ] [APPROVED] Each recurring daily reports **Delivered / Blocked / Decisions Needed / Remaining in Scope / Parallel Progress** by workstream, with exact commit/test/evidence and no fake live VPS claims.
- [ ] [APPROVED] Technical documents, changelogs and commit messages in English; status to user may be Portuguese or English as needed.
- [ ] [APPROVED] Prefer native/shared skills, avoid duplicate skill registries, document provenance, run tests/UAT and security checks, leave drafts under PR until user approves merge.
- [ ] [APPROVED] Later diagnose active GitHub Actions errors in Curatia and personal-site repos as Senior Developer, after higher-value Olympus work; distinguish historic red jobs from current active failures, do not make tests green by weakening CI.
- [ ] [APPROVED] Monitor availability/HTTPS/deploy failures where it advances existing VPS goals, using authorized observability and scheduled checks, without misleading claims of continuous direct VPS access.
- [ ] [APPROVED] Full report must separate historical claims, observed connector result, actual VPS operation, and future hypotheses. Do not ask the user to reprovide IDs/configuration already discovered.

## 7. Evidence index

- [Olympus foundation + Constitution](../CONSTITUTION.md) [GitHub]
- [Implementation runway](implementation-runway.md), [bootstrap Kanban](kanban-cards-and-review-gates.md), [restore tests](acceptance-and-recovery-tests.md)
- [Senior-review policy](senior-specialist-and-architecture-review.md), [open-loop register](open-loop-register.md)
- [Plugins and v0.23 compatibility](plugins-v023-scope-matrix.md), [themes/skills](profile-themes-and-skills-scope.md)
- [Telegram plan](telegram-one-bot-group-routing.md), [remote ingress options](hermes-remote-ingress-options.md)
- [WebApp cutover](hermes-v023-webapp-migration-runbook.md), [Mission Control designs](future-mission-control-three-designs.md)
- [Bot-hub synthetic integration tests (draft PR #4)](https://github.com/Guilsc/universal-agent-bot-hub/pull/4)

## 8. End-of-run gate (mandatory)

```text
[ ] Check previous accepted and deferred user requests
[ ] Check current GitHub repo / open PR state and actual recent tests
[ ] Check whether blocked VPS/model connection has become available
[ ] Record concrete new evidence and the next independent task
[ ] Do NOT imply a draft, scheduled reminder or chat bot message was executed on VPS
[ ] Continue if there is a valuable, bounded, authorized next action
[ ] If all remaining actions need unavailable executor/approval, report exact blockers
[ ] Halt before Block 3 and never conflate future architecture draft with implementation
```
