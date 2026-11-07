# Telegram group routing and Hermes Core bridge: staged implementation draft

> Planning only. Created 2026-11-07. Do **not** change a live Telegram bot, remove webhooks, add group admins, rotate tokens, or forward privileged commands without a verified gateway, backup, scoped permission checks and separate approval.

## Verified versus unverified

**Verified via connected Composio Telegram Bot API `getMe` on 2026-11-07:**
- Bot display name `Hermes-VPS-Cli`, username `@guilherme_hermes_agent_bot`.
- Bot reports `can_join_groups=true`, `can_read_all_group_messages=true`, `has_topics_enabled=true`, `allows_users_to_create_topics=true`.
- This shows the connected Telegram bot identity and its declared capabilities. It **does not prove** the remote bot's runtime location, the live Hermes Core `default` link, model availability, gateway routing, active chats or ability to invoke Olympus profiles.
- Telegram `getUpdates` may conflict with an active webhook; **do not use polling as a discovery probe**. No message has been sent.

## Design goal

Use one authorized Telegram **group** as the human-facing entry point, with topical threads as views:
- `#core-operations` — Hermes Core `default` run status, backup and maintenance, restricted to operator.
- `#olympus-intake` — future initiative intake link or topic, routed through Zeus governance only after canonical intake is implemented.
- `#planning-room` — Olympus Hermes-led status and handoffs; avoid an independent group-chat decision authority.
- `#alerts-and-daily` — redacted checkpoints, blockers, daily reports and safety alarms.
- `#review-requests` — asks requiring explicit human approval, not bot-implied consent.

These are optional **topic names**, not guaranteed currently existing Telegram topics. Create only if forum topics and group permissions are actually verified. The bot must not require admin privileges beyond the commands/features selected.

## Routing and ownership

1. The user chats with **one trusted bot identity** in the group or DM. A bot may represent multiple authorized profiles *only if native routing actually supports it*; do not invent API commands.
2. An ingress adapter reads the verified chat ID, message ID, user ID and thread/topic ID; authenticates owner/allowlist. For state-changing commands, require a command-specific approval token or server-side policy rather than trusting a message mentioning `@Zeus`.
3. Hermes Core `default` handles privileged maintenance **only in a dedicated authorized operations context**, never silently as a general group default.
4. Olympus initiative requests use canonical `initiative_id` (later `mission_id`) and enter Zeus → Olympus Hermes → domain owner. Topic routing is display metadata, not authority.
5. Specialist profile selection follows the one-domain-one-owner rules. Profile memory and secrets stay isolated from group content; only sanitized result summaries may be posted.
6. Prevent duplicate jobs on Telegram retries with idempotency keys `chat_id:message_id:command` and canonical mission identifiers. Persist durable state in the actual authorized host, not in chat history.

## Security and Telegram privacy

- Use existing bot identity if appropriate; avoid creating eight Telegram bots. A single bot is a presentation/transport choice, not a shared agent identity.
- Group members may see messages, tasks, screenshots or logs. Redact passwords, credentials, sensitive SOUL/USER/MEMORY, private prompts and full raw worker reasoning. Never forward execution transcripts to a group by default.
- Confirm Telegram privacy settings, topics support, bot user privileges and who can invite participants. Group `can_read_all_group_messages` metadata requires especially careful group membership/authorization controls.
- Confirm current webhook consumer. Avoid `getUpdates`/webhook deletion in a system already consuming updates.
- Rate-limit commands, cap concurrency and validate source; fail closed for unknown chats and sender IDs.
- Every mutating Telegram operation needs durable audit evidence, and user-facing status must reflect actual execution state, not optimistic queued state.

## Staged rollout and validation

| Stage | Action | Pass evidence |
| --- | --- | --- |
| TG-00 | Read-only inventory of existing bot `@guilherme_hermes_agent_bot`, its Hermes transport, webhook, chat allowlist, secrets handling, and runtime version. | Sanitized map of actual bot → gateway → profile and current message handling. |
| TG-01 | Define topic names, role permissions and policy; confirm **one-bot group** vs existing direct messages; preserve current DM behavior. | Reviewed routing matrix, no unsupported command claims. |
| TG-02 | Prepare an isolated **test group** only with explicit consent and authorized operator; avoid adding live secrets and unrelated people. | Bot can read/respond to a harmless test command with confirmed identity and no privileged action. |
| TG-03 | Route a nonmutating status inquiry to Core `default`; verify one response, no duplicate dispatch, no cross-profile memory. | Correlated chat message ID and actual VPS profile trace. |
| TG-04 | Use native group-chat Lead Bot routing **only** for notification/response selection; enforce Zeus and Domain Owner authorization outside LLM prompt. | Forbidden test request denied; approved request traced to correct owner. |
| TG-05 | Summarize BOOT progress to group after VPS backups + review gates; never dump raw logs/secrets. | Safe daily report, history and rollback of bot settings documented. |

Stop when the VPS or model cannot be attested. Future profile delegation needs a separate gate. No stage should add a new Olympus role, global capability owner or independent project.

## Ready-to-use safe probe message (do not send until chat destination verified)

```text
Hermes Core (default) — read-only diagnostic request. Please return:
1. Your actual profile ID, Hermes version, runtime/gateway identity and active provider/model (if reported).
2. Whether this message reached the VPS Hermes gateway over the existing Telegram bot and if it has permissions to READ only the current state.
3. Whether you can enumerate current Kanban cards without modifying them.
Do not execute commands, change files, install plugins, modify webhooks, switch providers or start workers.
If unable to verify, explicitly reply UNVERIFIED.
```

This text is not a proof of the claimed identity by itself; corroborate with real VPS-side session ID and host evidence.

## Follow-up: verified Composio outbound transport (2026-11-07)

**New evidence:** using the connected Telegram Bot API, `getChat` succeeded for the user's previously authorized **private chat**, and `sendMessage` succeeded from `@guilherme_hermes_agent_bot` (Telegram message ID **808**). The diagnostic contained no executable instruction and changed no VPS service.

**Important limit:** a message **sent by the bot itself** is an outbound notification, not an inbound user message to its own Telegram webhook. Thus this does **not** establish ChatGPT → Hermes Core command execution, a working VPS gateway, or permission to create/modify a group. The Bot API connection is bot-identity-only; do not assume it can impersonate the human account or send a Telegram user message into its own bot.

Read-only Telegram `getMe` and `getChat` succeeded without modifying the webhook or active session. No webhook-info tool was discoverable through the connected Telegram toolkit; avoid calling `getUpdates` as an unreviewed substitute. Determine the actual webhook/polling consumer later from the authenticated VPS Core runtime.

**Security:** a BotFather credential was shared in conversation. Do **not** embed its value or the user's private chat ID in a public repository, issue, log or prompt. Treat this credential as exposed; plan a controlled rotation with verified current token destination, secure secret store and rollback after the VPS gateway is accessible. Never rotate blindly or break the working bot.

**Recommended next safe test:** user-originated innocuous `/status` or equivalent known supported command from the verified chat, then correlate its reply and session ID with actual Hermes Core VPS logs if available. Do not invent command names or infer profile identity from a Telegram reply alone. User should not need to repeat identities already established by the connected Bot API.
