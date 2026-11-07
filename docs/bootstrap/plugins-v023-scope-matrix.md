# Hermes v0.23 bootstrap capability matrix (2026-11-07)

> Prepared from approved Olympus v1.2.2 design, existing audit reports and the Hearth v0.23 release review. **Not** a live inventory, installation receipt, security certification, or authorization to grant capabilities. Validate the installed version and scope on the VPS before acting.

## Five different states

`discoverable` → `installed` → `enabled/loaded` → `authorized for profile and mission` → `actually executed`

These states are **not equivalent**. Do not represent a globally visible plugin as globally authorized. Preserving installed plugins from premature disablement does not imply inheriting all their privileged tool grants into each new god.

## Candidate routing and expected scope

| Capability | Intended scope | Reason / conditions | Live status |
| --- | --- | --- | --- |
| Native Hermes profiles, session gateway and Kanban | Core runtime service; per-profile identity isolation | Native foundation for eight durable gods; avoid redundant scheduling or boards | **Unverified** |
| OMH Restricted Bridge | Existing approved bridge; inspect effective host/profile grants | Preserve availability. Assess its actual hooks, guardrails and goal checking before relying on it | Historical reports only |
| Full OMH | Existing installation if present; **not** automatically re-enabled/replaced | Verify potential overlap with Restricted Bridge, hooks and policies; never assume it prevents unbounded loops | Historical reports say inactive; **reverify** |
| Advanced Delegation | `olympus-hermes` orchestrator profile | Profile/model delegation; enforce exclusive realm ownership at host boundary; requires compatible Hermes | **Unverified** |
| Bot Forge | Provisioning/manager profile, temporary bootstrap use | Build missing god profiles from reviewed template without default tokens, broad grants, cron jobs or extra gateways | **Unverified** |
| Agent Importers | Controlled import/staging profile | Dry-run and selectively import from Codex/Claude/Cursor sources, preserving owner approval | **Unverified** |
| Hermes Agent Builder | Optional authoring profile | Convenience visual editor; not a runtime dependency | **Unverified** |
| Pantheon themes | Presentation only | Theme name and avatar must not alter SOUL, model, realm, grants or memory | Catalog historically reviewed; active behavior **unverified** |
| Memory Wiki / memory providers | Per-profile private state and approved shared knowledge connectors | First verify existing isolated stores and schemas; never silently merge or reset memory | Historical status only |
| Inbox / Perf HUD / operations | Existing operational tools; profile grants according to role | Preserve current installation pending usage evidence and security review | Historical reports only |
| Composio Connections | Connector integration only with account authorization | Search/surface capabilities; require explicit per-tool and per-profile grants; no credential copying | Historical inactive, **reverify** |
| Custom MCP / Capability Registry | Shared read-only discovery, separately authorized private infrastructure reads | Reuse existing `Guilsc/capability-platform`; do not build another authoritative registry | Git/source data vs live endpoint **unverified** |
| Dynamic GitHub resource list | Discovery eligibility, never automatic installation | User-approved list `Guilsc/lists/repo-workspace`; newly starred resource is candidate only, subject to trust review | Last catalog snapshot may be stale |
| Cloud Subscription Direct SDK | Deferred unless valid provider credentials and need | Do not infer subscription entitlements or make it a bootstrap dependency | **Unverified / deferred** |
| Hermes Teammates and duplicate Kanban plugins | Deferred pending a demonstrated gap | Olympus Hermes + native Kanban are already selected | **Not required** |
| Third-party Olympus Dashboard plugin | Inactive until fail-open write paths are addressed | Distinct from `Guilsc/olympus` project and native Hermes WebApp | Historical concern, **reverify** |

## Required source-of-truth validations

Before any plugin package install or update, inspect actual:
1. Package ID, installed hash/version, source URL and trust review.
2. Hermes runtime compatibility and dependencies.
3. Active/inactive state and tool/hook registration.
4. Global versus project versus native-profile configuration surfaces.
5. Actual tool execution grants for `default` and each `olympus-*` profile.
6. Credential location and access controls **without revealing secrets**.
7. Memory/backup impact and rollback method.
8. Whether the same capability is already offered natively or by an installed plugin.

The initial bootstrap should favor making the approved, existing capabilities discoverable/usable within their authorized scope. Record observed use and report after the milestone; do not disable plugins merely because no call was seen during a short test.

## Hermes Hearth v0.23 compatibility checklist

| Item | Expected change | Verification |
| --- | --- | --- |
| Native WebApp | Gateway-owned shared browser workspace; separate opt-in/security controls | Verify live `webapp.enabled`, auth, TLS, websocket, browser session view and Desktop session parity |
| Single gateway owner | Multiple clients share queue/history on one machine | Prove no duplicate gateway process/competing session owner; do not assume two domains mean two gateways |
| Multi-machine Desktop | Remote connection selector shows gateways, **not a god selector** | Keep three working Desktop entries; no unsafe JSON rename |
| Profile/god selection | Separate requirement from gateway selector | Test native profile routing and real metadata with 2 profiles before UI customization |
| Group Chat Lead Bot | Could route unaddressed chat, not approve or bypass Olympus mission governance | Route through Zeus when needed; Hermes remains Olympus orchestrator |
| `advanced-delegation` | Task-level model/profile selection | Fail closed for cross-realm unauthorized tool calls; no broad grant inheritance |
| Plugins update | `hermes plugins update` supports bulk proposals | Inspect diffs and new capabilities; keep auto-update disabled until separately approved |
| Browser integration | Older `browser_*` references require `browser_exec` updates | Search effective skills/prompts before execution |
| Hermes MCP server | Invocation changed to `hermes mcp-serve` | Inventory actual launch units; no blind command replacement |
| Rewind / fork | Session editor and branch facility | Useful for development but do not confuse with backup, version control, or approval |
| MCP spending limits | Supported for tools declaring prices | Defense-in-depth only; provider bill and undeclared tool costs still require controls |
| Scheduled work | Native cancellation, missed-run policy and provider cache where supported | Require observability, finite budgets and valid owner/permission separation |

## Web URL / dashboard migration guardrails

- **Hermes Dash Gateway:** retain the working HTTPS engineering/administrative connection, not the redundant dashboard public hostname.
- **Native Hermes WebApp:** candidate for the existing browser WebUI hostname; do not expose unauthenticated `default` tools.
- The third-party community WebUI and a separately published redundant dashboard route may be retired **after** a tested backup, dependency inventory, explicit proxy change approval and rollback, not during this inventory.
- Preserve internal listener, API and active Desktop HTTPS connection even if redundant public DNS/proxy route is eventually removed.
- Browser universal entry through Cronos/Mission Control is a future policy-router/frontend milestone. The new Hermes WebApp does not magically satisfy its server-side permission model.

## Model and reviewer rule

The user prefers GPT-6.1 Sol but reports an exhausted weekly allowance while a new session window is available. Verify quota and effective model **on the VPS**; do not assume this chat's model or an OmniRoute alias proves actual model selection. Free OmniRoute models are not approved substitutes for high-risk implementation. Review should be independent where feasible, backed by deterministic tests and evidence, and should not invent a successful result if a model cannot be invoked.

## Follow-up after a verified VPS snapshot

Populate real `installed_version`, `enabled_state`, `profile_owner`, `required_grants`, `used_in_bootstrap` and `decision` columns from sanitized host evidence. Keep candidate package decisions as suggestions until the host has confirmed compatibility, backup integrity, and proper authorization.

## Marketplace Kanban candidates reviewed on 2026-11-07 (public catalog only)

- **Kanban Empowered**: [marketplace](https://hermes-agent.nousresearch.com/marketplace/kanban-empowered). Project lifecycle per board (Active/Suspended/Done), coordinator lock, human asks through Telegram/Desktop, blocker explanations and bounded infrastructure retry are directly relevant to the initial Core Kanban. Marketplace currently advertises **v0.3.0**, while a separate catalog/documentation view was observed advertising **v0.2.0**; verify the exact reviewed/pinned build and installed version before considering activation. It reads all boards and profile state, can write board state, and v0.3.0 may send redacted recent worker reasoning to a configured auxiliary model. Its core veto patch is optional and currently incomplete for review-lane claims. **Recommendation:** high-priority candidate for security and compatibility review; no installation or grants approved by this note.
- **Kanban Gantt**: [marketplace](https://hermes-agent.nousresearch.com/marketplace/kanban-gantt). List, Timeline and Graph views, dependency editing, task movement and attachment previews. Substantial write permissions and board mutation behavior; useful later for project visibility but avoid introducing another orchestration source of truth.
- **Kanban Graph**: [marketplace](https://hermes-agent.nousresearch.com/marketplace/kanban-graph). Read-only graph of boards and worker lineage, no model calls. Still reads worker session tool calls and board data; access should follow existing auth and privacy boundaries.
- **Native Kanban**: [documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban). Already has board lifecycle cards, dispatch and optional auto-decomposition; note that `triage` can trigger model calls if `kanban.auto_decompose` is enabled. During bootstrap do not enable automatic decomposition or broad agent delegation without checking effective settings and quota.

**Decision recommendation:** evaluate Kanban Empowered first as an additive operational/visibility layer, without replacing native Kanban or Olympus canonical initiative state. Inspect package source, configured auxiliary provider, actual hooks and required core patches on the VPS; ensure that summaries do not transmit confidential reasoning to an unapproved model. Preserve existing plugins, make no irreversible toggles, and defer installation until backup and explicit permission review. The user's forthcoming video is additional evidence, not automatic activation authority.
