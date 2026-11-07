# Telegram to Hermes: operator prompt playbook

Status: DRAFT. These are prompts to submit through an actual authenticated inbound Hermes Core default session. Bot API outbound message from Hermes cannot trigger its own listener. No live Hermes VPS execution verified.

## Transport rules

1. Preferred: existing Hermes VPS HTTPS API/WebSocket gateway with verified profile default, authenticated session and evidence ID.
2. Alternative: user-originated message to the existing Hermes Telegram bot in an allowlisted topic. The connected Composio integration sends AS the Hermes bot, not as the user.
3. A second bot can deliver messages in a compatible group only after actual bot-to-bot communication mode, group ID, mention/reply and both membership/permission checks are verified.
4. Never compete with current webhook by polling getUpdates, create a duplicate runner, or disclose/reenroll the BotFather token.
5. Topic names already reported: Infrastructure & Operations; Research & Learning; Projects & Integrations; Olympus; Hermes & AI Agents; Planning & Inbox. Topic ID and valid ingress still unverified.
6. The existing Universal Agent Bot Hub commands /help, /new, /status belong to that Codex gateway. Do not assume they work on the Hermes bot without actual runtime verification.

## Prompt 0: provenance handshake (read only)

> Act as Hermes Core operator on the actual Hostinger VPS, effective native profile default. This is a provenance challenge only, with NO side effects.
>
> Report your actual hostname and current authenticated ingress transport, effective Hermes version/profile, active model/provider or UNKNOWN, and whether you can READ ONLY current Kanban cards, profiles and plugin state. For each claim provide a sanitized host/session evidence reference. Do not infer facts from my question. If you are not on the verified VPS or cannot prove profile default, answer BLOCKED with the specific missing permission. Do not use terminal writes, new bot polling, provider fallback or service changes.

Acceptance: host/source independently corroborated; bot reply alone is not enough.

## Prompt 1: BOOT-00 read-only inventory

> You are Senior SRE operating through the VERIFIED Hermes VPS HTTPS or SSH into the same VPS as profile default. Inspect only: Hermes runtime/version, provider/model status, profile names and isolated roots, Docker/Coolify service names/ports/volumes, proxy and TLS routing, Telegram webhook or polling mode (without altering it), native Kanban boards, installed plugins including OMH, Git checkout branch/HEAD/dirty files. Never reveal credentials, SOUL, USER or MEMORY contents. Produce a redacted evidence table with verified/unverified columns. No upgrades, installs, backups, restarts or changes. Complete only if host and profile provenance can be proven.

## Prompt 2: BOOT-U0 backup after inventory and verified permission

> Act as Senior SRE. Verify BOOT-00 PASS and available VPS disk/snapshot mechanism. Produce a timestamped NON-overwriting consistent backup of actual Hermes/Olympus state, sessions, eight profile memory roots, plugins and MCP metadata, live databases using appropriate snapshots, Git branch and dirty state and Coolify/reverse proxy config. Preserve restrictive permissions; no secrets in output. Verify SHA-256 manifest and safe isolated restore/extraction on SAME VPS. Never stop working services for convenience. PASS only with checksums plus restoration evidence. Otherwise BLOCKED with precise blocker. No DNS, Docker, model or token changes.

## Prompt 3: BOOT-01 reconciliation

> As Senior BA and Platform Engineer, compare v1.2.2 approved decisions with live VPS checkout and the remote Guilsc/olympus main and draft PR #12. Preserve all uncommitted work. Reconcile historical Blocks 1.1..1.5, proposed Block 2.1, OLY-01..07 and conflicting BOOT-00/U0 labels. Produce per-file diffs, test baseline and authoritative checkpoint recommendation. Do not git reset, merge, overwrite, implement future blocks or invent missing commits.

## Prompt 4: BOOT-02 plugins and owner scopes

> As Senior Platform Architect and Security Engineer, READ ONLY installed Hermes version, profiles, native Kanban and Kanban Empowered, OMH Restricted Bridge/full OMH, Advanced Delegation, Bot Forge, Agent Importers, shared MCP/capability registry, skill sources and model routes. Report installed/enabled/loaded vs marketplace-only, exact versions, owner grants, privileged hooks, compatibilities and privacy risks. Keep existing plugins available. Check six Domain Owners' exclusive capabilities and profile-memory isolation. Do not activate a plugin, patch Hermes Core, assign global grants, switch model or install anything.

## Prompt 5: Telegram ingress inspection

> As Senior Integration Engineer, map actual incoming Telegram user/group/topic -> existing bot -> Hermes gateway -> native profile. Read current allowlist, webhook/polling owner, bot-to-bot mode and topic IDs from authorized VPS config WITHOUT displaying secret values. Do not call getUpdates against unknown active webhook. The bot's previous outbound message ID 808 is NOT an inbound task. Return an authenticated session route map, a safe proposed ping and its acceptance evidence; do not claim messages delivered into Hermes unless the incoming receipt and actual runtime trace match.

## Prompt 6: WebApp preparation (no cutover)

> As Senior SRE, map hermes-gateway.guilhermecosta.tech, hermes.guilhermecosta.tech, gateway.guilhermecosta.tech to real TLS, auth, backend and session state. Check v0.23 native WebApp compatibility and Desktop session parity. Preserve actual gateway listener. Write a reversible migration plan and smoke tests. NO proxy edit, DNS edit, service removal, token rotation or cutover.

## Prompt 7: independent review

> You are an independent senior reviewer with a separate context, not the implementing worker. Review the exact original goal, approved constraints, immutable host evidence, source diff, tests and negative scenarios. Return PASS, REWORK or BLOCKED with missing evidence and next permitted step. Do not modify production. A material architecture proposal must first go through ADR, a genuinely independent Senior Architect and explicit human approval.

## Prompt 8: four-hour daily

> Report by workstream: DELIVERED (links to commits/CI/live host receipts), BLOCKED (actual failed tools and attempted alternatives), DECISIONS NEEDED (only those not resolvable without human approval), REMAINING before Block 3, PARALLEL PROGRESS and next authorized task. Re-read requirements-traceability-audit.md and open-loop-register.md. Never conflate GitHub CI with VPS tests, outbound bot notification with inbound Hermes execution, or user-reported VPS snapshots with current runtime proof.

## Follow-up: unable to access VPS

> Do not invent access. Classify the failure as DNS/TLS, gateway authentication, profile routing, missing executor, provider quota or permission. Check only already approved Hermes VPS HTTPS or SSH to same VPS. Report sanitized error, actual verification attempts and next specific action. Move to an independent GitHub/test/documentation task; never silently use a local container.

## Follow-up: model unavailable

> Confirm actual model/provider and observed quota. Do not use a free unapproved provider or burn tokens to repeat failed checks. Continue model-independent source review and document which functional tests require an approved model.

## Follow-up: Telegram unavailable

> Distinguish Telegram bot outbound from true incoming user/bot-in-group update. Verify webhook/poller ownership read-only and check effective group + topic routing with approved allowlists. Do not recreate bots, disable webhook or use BotFather tokens in logs. Prefer authenticated Hermes HTTPS gateway for real execution if this transport remains unavailable.

## Topic suggestions (presentation, not permissions)

- Infrastructure & Operations: server backup, network/proxy, BOOT checklist and daily alarms.
- Hermes & AI Agents: native profiles, plugins, model status, delegation and capability security.
- Olympus: Constitution and realm ownership, governed initiative progress.
- Planning & Inbox: approval requests, intake drafts and daily brief.
- Projects & Integrations: external GitHub CI, connectors, code tests.
- Research & Learning: documentation, videos and experiments with no privileged commands.

Do not invent numeric message_thread_id values. The currently connected Composio Telegram sendMessage tool did not expose topic routing; an outbound message in the private chat does not prove topic delivery.

## Evidence distinction

BOT_OUTBOUND_SUCCESS != HERMES_INPUT_ACCEPTED.
HERMES_INPUT_ACCEPTED != REMOTE_JOB_COMPLETED.
REMOTE_JOB_COMPLETED != UAT_PASS.
GITHUB_CI_PASS != VPS_DEPLOYED.
