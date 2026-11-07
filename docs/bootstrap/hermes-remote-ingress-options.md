# Hermes remote ingress: evaluated execution paths (2026-11-07)

> Decision record and integration design only. No live VPS agent command, webhook, token rotation, admin grant or new bot was executed. Preserve the existing Hermes VPS HTTPS gateway, native profiles and Telegram messages.

## Problem

We have an active Composio connection authenticated as Telegram bot `@guilherme_hermes_agent_bot` and a previously verified private Telegram chat with topic support. `getMe`, `getChat` and outbound `sendMessage` succeeded. The bot's own outbound message (ID 808) is **not an inbound human command**, so editing/resending it cannot be treated as Hermes execution.

The user wants **unattended programmatic admission** to Hermes Core `default` on the actual VPS, with preservation of existing agent and session ownership.

## Candidate paths, in preference order

| Route | Capability | Prerequisite | Verdict |
| --- | --- | --- | --- |
| A: Hermes API server over existing HTTPS | Authenticated direct submission to existing gateway/profile; can use server response as evidence | Confirm actual endpoint, API key grants, profile route, active listener and HTTPS/auth from VPS | **Preferred**; not connected here |
| B: Authenticated gateway WS / session API | Native shared session, explicit target profile, durable receipts and queue state | Verify runtime v0.23 protocol/auth/ticket; connected remote client and granted `session:submit` | Valid possible route, not yet tested |
| C: Authenticated Telegram user client | Sends actual *user* message to existing bot/topic | Authorized personal session in Work/Telegram Web or MTProto, with its own login/2FA | Valid, but no personal Telegram session exposed by present Bot API connection |
| D: Telegram bot-to-bot *in a group* | Telegram now documents bot-to-bot delivery in supported contexts, with commands targeted at bot or replies and BotFather mode setting | Second **separately connected** bot, same real group, Bot-to-Bot Communication Mode on at least one bot, careful group allowlist and permissions | Possible, but **not** currently connected/verified; do not create a new bot as first choice |
| E: Hermes outbound bot notification to topic | Show human a request, checkpoint or evidence link | Existing Composio bot outbound `sendMessage` | Verified outward direction only; **not execution** |
| F: Hermes cron/kanban reads a GitHub work queue | Poll pre-authorized task source and execute according to policy | Evidence existing scheduled pull process or separately approved secure service/config | Potential future integration; no currently verified polling, so a committed file does not launch it |

Official references: [Hermes programmatic integration](https://github.com/nousresearch/hermes-agent/blob/main/website/docs/developer-guide/programmatic-integration.md), [Hermes gateway internals](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/gateway-internals.md), [Telegram bot-to-bot communication](https://core.telegram.org/api/bots/bot-to-bot), [Telegram Bot API](https://core.telegram.org/bots/api).

## API submission requirements

1. Use **the already active VPS endpoint**; do not expose a new public terminal or another gateway container. Identify actual API availability and whether `/p/<profile>/` is supported on the running revision.
2. Enforce TLS and bearer/session token from approved vault or runtime auth; do not use BotFather token as Hermes API auth and never print a token in logs.
3. Read gateway version, profile ID and session creation contract; use a dedicated, idempotent request ID; target `default` explicitly. Confirm that the returned session and host identity are the actual VPS.
4. Start with **read-only identity + environment probe**. Commands to inspect Kanban, launch workers or create backup require a separate goal gate and effective profile permissions.
5. Correlate request ID, admission ACK, execution completion, model/provider attribution, review verdict and evidence artifact. An ACK is not task completion.
6. Do not switch auth transport or proxy route while active Desktop and Telegram sessions are working. If API unavailable, record not available and continue documentation.

## Telegram topic policy

Existing user-reported topics: **Infrastructure & Operations**, **Research & Learning**, **Projects & Integrations**, **Olympus**, **Hermes & AI Agents**, **Planning & Inbox**. Verify exact topic IDs from current bot configuration only through a nondestructive source. Never guess `message_thread_id`.

- Infrastructure & Operations: protected Hermes Core BOOT status/backup summary, no raw secrets.
- Olympus: approved initiative/role owner summaries, without SOUL/memory dumps.
- Hermes & AI Agents: model/profile/gateway diagnostic notices.
- Planning & Inbox: upcoming goal cards and user-review requests.
- Projects & Integrations: connector and GitHub readiness.
- Research & Learning: documentation reference, no privileged operational dispatch.

The connected Composio `sendMessage` tool exposes `chat_id` and `reply_to_message_id` but **not `message_thread_id`**. Replying to a known message may or may not land in the same private-chat topic; do not use it as a reliable router without a live verification. Its `getChatHistory` is in fact pending-update polling; avoid consuming/competing with active webhook.

## Security and product implications

- A compromised BotFather token allows bot impersonation. It was shared in conversation; perform a controlled rotation **after** tracing all consumers and backing up the running config, update it in vault and VPS, then revoke old token.
- Bot-to-bot group admission adds an attack surface and loop/rate-limit risk; must scope commands to registered bot ID, required mention/reply, allowed group/thread/user and durable idempotency.
- Allowlist the user's Telegram user identity on Hermes ingress only if the current policy says so; Bot API access to chat metadata is not authority to impersonate the user.
- Existing Hermes native Kanban, not Telegram chat history, owns task progress. Olympus Zeus and Hermes roles remain separate from Core maintenance.

## Reusable no-side-effect test objective

```yaml
goal: verify Hermes Core default remote admission
execution_target: verified Hermes VPS HTTPS gateway
operation: read_only
requested_checks:
  - runtime version and gateway identity
  - canonical active profile ID
  - actual model/provider routing or unknown
  - whether Kanban can be read without modifying board state
evidence_needed:
  - request and session correlation IDs
  - remote endpoint/profile provenance
  - returned status and executed/read-only confirmation
acceptance: reject all unverified claims; no side effects
```

## Current status

**Verified**: Telegram bot authenticated; outbound transport reaches the user's Telegram chat; GitHub repo can be updated through connected integration.

**Unverified**: native VPS API authenticated ingress, an effective Telegram user-authenticated session, bot-to-bot-enabled group, active Hermes polling of GitHub queue, and ability to execute commands on VPS.

**Next move**: establish the existing HTTPS gateway's authorized API/session interface; if impossible, use an already authorized user-side Work browser session. Avoid installing a new bot or altering current webhook merely to simulate the user's message.

## 2026-11-07 legacy second bot recovery and actual probe

Relevant conversation history identifies an earlier second Telegram bot, `@guilherme_local_codex_agent_bot`, associated with the Universal Agent Bot Hub / Codex experiment. This does **not** prove it is the *new* bot the user added to a group today. Previous host work also reportedly used Telegram MTProto authentication and separate Telegram bot services under `/opt/olympus-bots`, with in-progress thread/mention routing; confirm effective VPS state before assuming any service is active.

The existing connected Hermes Bot API client attempted a **read-only** `getChat` for that bot username and a **harmless** direct `sendMessage` with no operational instruction. Both failed with Telegram `Bad Request: chat not found`. The failure does not prove the bot doesn't exist; it does prove the current connected bot cannot directly route to it by that username in this setup. Do not retry blindly, disclose BotFather tokens, or bypass Telegram's bot communication mode.

Official Telegram [bot-to-bot documentation](https://core.telegram.org/api/bots/bot-to-bot) allows message exchange in group chats when one bot has the mode enabled and message contains an explicitly targeted command or reply, with additional admission conditions; private bot-to-bot requires mode enabled for both. Group identity and actual member permissions remain unverified. The self-sent Hermes notification (Telegram ID 808) is not an incoming message.

**Test-only code prepared** in a separate isolated draft PR, [universal-agent-bot-hub #4](https://github.com/Guilsc/universal-agent-bot-hub/pull/4): synthetic bot-originated group message validation for both allowlists, command-target matching and topic isolation. GitHub Actions runs are evidence of *offline unit tests only*, not Telegram delivery, Hermes integration, model access or VPS execution. The existing hub uses a Codex worker, not a Hermes runtime. Never deploy it as an implicit replacement for Hermes Core.

Next real integration requires either the group chat ID and BotFather mode/permissions verified from a trusted session, or authenticated HTTP/WS admission into the existing Hermes VPS gateway. The latter remains architecturally preferred and avoids setting up a duplicate Telegram poller.
