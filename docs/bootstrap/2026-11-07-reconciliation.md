# Olympus bootstrap reconciliation and safe resume (2026-11-07)

> Status: **planning / evidence reconciliation only**, not a runtime validation or deployment receipt.
> Scope: document the decisions approved in recent user conversations and the discrepancies to verify on the VPS. This file contains no secrets or private infrastructure details.
> This plan does **not** supersede the Olympus Constitution or historical evidence. A developer must reconcile this with the effective VPS repository, shared delivery policy, and latest approved v1.2.2 document before implementation.

## 1. Source and evidence provenance

- **GitHub default branch, observed 2026-11-07:** README identifies an architectural foundation, *not* a running production agent runtime. `docs/architecture.md` distinguishes Hermes-Main (external builder) from Olympus Hermes (canonical orchestrator) and defines Control/Agent/Capability Plane as **conceptual lenses**, not separate deployable services. The default branch has no `docs/v1.2/IMPLEMENTATION_CHECKPOINT.md` at the observed path.
- **Prior VPS session reports, not independently verified here:** `feat/olympus-universe-v1.2` and local commits `7911c1c`, `baed6bc`, `bdc22b9`, `aec377d`, `c1c28b2`. Reported OLY-01 complete, OLY-02 through OLY-07 partially implemented locally, with 21 offline tests passing and no native production deployment. Do not assume this branch exists remotely or that the host checkout still matches.
- **Approved v1.2.2 design (2026-11-06), subject to effective host evidence:** phase order Olympus → generic Mission Control → Cronos/Apex; exclusive domain capability ownership; Hermes Core (`default`) as external engineering/admin agent, Olympus Hermes (`olympus-hermes`) as Olympus orchestration identity.
- **Observed user-operated Windows checkpoint:** the Desktop connection files were copied to a timestamped Windows backup on 2026-11-07, with SHA-256 hashes displayed. This does **not** establish a restorable VPS backup, profile memory health, or application/database consistency.

## 2. Boundaries and entry points

- **Hermes Core `default`**: operates across authorized projects as the bootstrap/maintenance actor; it is not the Olympus `orchestrator` role. For this bootstrap, execute operations **on the VPS via the existing Hermes VPS HTTPS connection**. SSH to that same VPS is an authorized secondary transport. Do not execute commands, tests, file edits or backups on Windows / Workspace Local.
- **Olympus Zeus (`governor`)**: admits and governs Olympus initiatives; **Olympus Hermes (`orchestrator`)**: planning, bounded triage, selecting Lead Owner, coordinating owners, tracking results. Domain Owners retain unique operational authority for their realm. Workers are optional and task-bound, not independent permanent owners.
- **Cronos/Apex** is the eventual universal intake project, forwards to Zeus. **Mission Control** is a separate read/control interface and does not become an execution authority. The universal web entry must later route by policy; a generic Hermes WebApp alone is not Cronos.
- **Bootstrap exception:** Hermes Core `default` may directly execute the already-approved recovery cards via Hermes native Kanban, without instantiating Olympus governance as a prerequisite. This exception does not change future initiative orchestration.
- One canonical mission identifier is intended across Desktop, Telegram, API and future web intake. Idempotency, storage and identity isolation must be tested, not assumed.

## 3. VPS web access and naming (target, NOT deployed)

- Keep **Hermes Dash Gateway** as the user-facing name for the current remote HTTPS engineering connection and its associated administrative dashboard. Preserve its existing, functioning HTTPS endpoint, the underlying runtime listener, profile routing and sessions.
- Retain the existing web hostname as the candidate home for the **native Hermes v0.23 WebApp** instead of the third-party community WebUI, with later integration into the Universe interface.
- The separately published *redundant dashboard hostname* is a candidate for removal **only after** a read-only reverse-proxy/dependency inventory, recoverable proxy backup, HTTPS/WebSocket/auth smoke tests and explicit change approval. Never infer that removing a DNS/proxy route permits deleting the Agent container, listener or persistent state.
- Existing Desktop `local` primary connection must not be renamed through unverified direct JSON edits: prior attempt caused remote connection entries to disappear. Preserve the three working entries and their backed-up JSON before any label change.

## 4. Model and remote execution gate

- The user reports that a session window is available, but the preferred GPT-6.1 Sol weekly quota is exhausted. **Session renewal does not prove model availability**. Check actual model and quota in the connected VPS session before running engineering cards.
- Do not silently fallback to low-quality OmniRoute free models for migrations, privilege changes, backup planning, security or complex implementation. A comparably reliable model requires explicit evaluation and authorization. If none is available, perform read-only discovery and documentation tasks only.
- An automation callback or a cloud browser session does not itself prove direct access to Hermes HTTPS, SSH, or the Desktop app. State actual executor provenance in every report.

## 5. Pre-block-3 execution cards (native Kanban)

| Card | Goal and minimum evidence | Exit gate |
| --- | --- | --- |
| BOOT-00 — Recover / inventory | Verify true VPS runtime, Git HEAD, branch, dirty files, Docker persistent mounts, proxy routing, sessions, eight `olympus-*` profiles and `default`; identify missing assets and rollback scope without disclosing secrets. | Evidence-backed current-state report; classify discrepancies as observed, historical, or unverified. |
| BOOT-U0 — Backup / continuity | Produce a **consistent** backup on the VPS of relevant persistent agent state, profiles/SOUL/USER/MEMORY, model/provider config (protected), plugins, session metadata, Olympus repo and proxy definitions; verify SHA-256 and snapshot consistency; preserve running services. | Manifest, checksum verification, minimal restore instructions and explicit gaps; **do not** claim success from a tar exit code alone. |
| BOOT-01 — Reconcile approved contracts | Compare v1.2.2 approved design with live VPS branch and remote `main`; preserve preexisting uncommitted files and historical evidence; prepare a bounded diff or PR, never overwrite local prior work. | Requirements traceability, ownership consistency and offline checks. |
| BOOT-02 — Plugins and model readiness | Inventory installed/enabled/disabled plugins, versions, profile-scoped permissions and actual hooks; review OMH/OMH Restricted Bridge, Advanced Delegation, Bot Forge, Agent Importers, Kanban and model routing. Validate capability discovery from the existing private MCP and approved dynamic GitHub resource registry. | Compatible plugin plan, installation candidates, privileged-grant exceptions and a verifiable execution/validation workflow; **do not preemptively disable installed plugins**. |

**Stop before Block 3.** Do not modify public routes, DNS, privileged grants, Telegram tokens, production deployment or merge to `main` as a side effect of these cards.

### Goal-driven review protocol

For each card: define observable goal → execute bounded work → record files, diffs, versions and tests → have a separate reviewer/context evaluate evidence versus acceptance criteria → PASS / REWORK / BLOCKED. Use OMH's actual installed evaluation/retry machinery **only after inspecting what it truly implements**. Do not assert that OMH automatically prevents endless loops. REWORK should demonstrate progress and respect finite resource budgets and stop conditions. Failed dependencies block dependent cards, not every parallel documentation or source-review activity.

## 6. Plugin availability versus authority

- Keep already installed approved plugins available during bootstrap; log actual usage and only recommend deactivation after the user reviews evidence.
- `advanced-delegation` belongs to Olympus Hermes, not every Domain Owner. `bot-forge` is an optional provisioning accelerator in a controlled manager profile; `agent-importers` should begin with dry-run staging. Native capabilities first.
- `OMH Restricted Bridge`, memory/knowledge tooling, community extensions and the existing custom MCP require live inspection before making claims about enablement, health or security.
- Resource registries distinguish **discoverable**, **installed**, **enabled**, **authorized**, and **executed**. A plugin being loaded globally must not bypass per-owner execution grants.
- A God may be bootstrapped from a reviewed template, but never inherit the Hermes Core's privileged credentials or tools by default. Distribute only the approved minimum capabilities.

## 7. Parallel work when VPS/model access is unavailable

1. Compare repo `main` with recorded VPS-only checkpoint; document drift and avoid publishing claims of unverified implementation.
2. Maintain a user-reviewed checklist for recovery backup, consistency, restore and dependency validation.
3. Draft compatibility matrices for the Hearth v0.23 release, existing prompt/browser tool renames, MCP invocation changes, plugin scopes and WebApp security.
4. Prepare Kanban card descriptions, goal/acceptance evidence forms and UAT minimal smoke procedures.
5. Continue documentation or code review on an isolated branch only; **no speculative production activation, secrets or claims of runtime testing**.

## 8. Safe handoff checklist

- [ ] VPS HTTPS session and model availability verified
- [ ] Effective VPS branch, HEAD, dirty state and protected files inventoried
- [ ] Verified, consistent VPS backup and documented recovery method
- [ ] Eight Olympus profiles and each distinct state/memory verified (do not equate declarative files with live memory)
- [ ] Plugin / OMH capabilities, per-profile grants and actual enablement verified
- [ ] Approved v1.2.2 implementation evidence reconciled with remote `main`
- [ ] Goal-based reviewer PASS for recovery and provisioning cards
- [ ] Explicit human checkpoint **before Block 3**

## 9. Next safe action

Using the existing Hermes Core `default` on **Hermes VPS HTTPS**, verify live host state and produce a consistent, recoverable VPS backup before any deployment or web proxy change. If no qualified model or remote executor is available, continue the independent documentation and Git evidence-reconciliation work; do not silently switch to Windows or OmniRoute free.
