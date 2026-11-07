# Open-loop register: Olympus bootstrap and universe decisions

> Status: **conversation-derived backlog**, prepared 2026-11-07. This is not a live VPS audit, implementation claim or authorization for Cronos/Mission Control production build.
>
> The register is a guard against silently abandoning agreed user requests when an executor or model is blocked. Verify against the canonical v1.2.2 source, latest VPS checkpoint, and any newer user decisions before marking an item resolved.

## How to operate the register

At the start and **before ending** each autonomous execution, perform an open-loop sweep:
1. Check relevant conversation decisions and requests, this register, current GitHub PRs/issues, current approved specification and any actual VPS checkpoint if accessible.
2. Deduplicate by desired outcome, not by wording or conversational turn. Preserve existing canonical initiative/task identifiers.
3. Assign status from **DONE VERIFIED**, **DONE REPORTED / UNVERIFIED**, **READY**, **BLOCKED**, **NEEDS USER DECISION**, **DEFERRED**, or **SUPERSEDED**.
4. Pick the next independent, approved, high-value action if the main task is blocked. Do not stop just because one tool, model or connection is unavailable.
5. For every completion, record actual evidence (commit, artifact, test, verified operation). If none exists, keep the item open.
6. Do not enter Block 3, merge, deploy, expose a new public endpoint or expand grants without the relevant separate approval.

## Current open-loop register

| ID | User-requested outcome | Current evidence and next safe action | State |
| --- | --- | --- | --- |
| OPEN-01 | Recover exact latest Olympus v1.2.2 code and checkpoint, without losing prior work | Prior conversation names a VPS-only development branch and commits, while remote `main` is still foundation-focused. Obtain actual VPS `HEAD`, dirty state and checkpoint after authenticating HTTPS/SSH. | BLOCKED: no verified VPS executor |
| OPEN-02 | Complete consistent VPS backup incl. Hermes Core, 8 Olympus profiles, sessions, memory, configs, MCP, repo and proxy, with rollback | Windows Desktop JSON checkpoint reported completed; **not** a VPS backup. Execute BOOT-U0 only on verified VPS with safe snapshot/restore validation. | BLOCKED |
| OPEN-03 | Verify available GPT-6.1 Sol quota or a genuinely comparable model; no silent OmniRoute free fallback | Five-hour window reportedly available, weekly quota reportedly depleted; no current provider-side attestation. Check from verified VPS session. | BLOCKED |
| OPEN-04 | Verify all eight god profiles and independent SOUL/USER/MEMORY, native session continuity, Desktop and Telegram registrations | Earlier reports describe eight declarative profiles; production/runtime instantiation unverified. Audit identity + isolated state; never recreate absent profiles silently. | BLOCKED |
| OPEN-05 | Inspect installed plugins, including OMH/OMH Restricted Bridge, Advanced Delegation, Bot Forge, Agent Importers, and Pantheon themes | Historical candidate inventory, not current runtime evidence. Keep installed plugins available; evaluate scopes and usage before suggesting later removal. | BLOCKED |
| OPEN-06 | Define exclusive capability ownership and delegation enforcement through Olympus Hermes; preserve governance by Zeus | Approved design; host-side enforcement, idempotency and authorized cross-realm calls need tests. Prepare contract-to-implementation review, then VPS verification. | READY (docs), BLOCKED (runtime) |
| OPEN-07 | Review native Hermes v0.23 WebApp, two dashboards, gateway process and HTTPS routing before removing redundant UI | Desired endpoint roles established; actual proxy routes, auth, WebSockets, login and session sharing unverified. Draft migration and rollback only, no live changes without backup and separate approval. | READY (docs), BLOCKED (runtime) |
| OPEN-08 | First real use of Hermes native Kanban, per-card goal/review/OMH loop and stoppable observable background work | Four BOOT cards, review gates and negative-test plan prepared on draft PR. Create/reconcile native board only after access to same VPS; avoid duplicate cards. | DONE VERIFIED (docs), BLOCKED (runtime) |
| OPEN-09 | Preserve shared custom MCP, capability registry, knowledge registry and dynamic starred-GitHub resource list; avoid duplicate registry/platform | Scope and separate registry responsibilities documented, but present live MCP/API state and ownership not verified. Review and reconcile registry responsibilities against latest spec. | READY (docs), BLOCKED (runtime) |
| OPEN-10 | Design shared skills/tools availability vs profile/project owner grants for Olympus, later Cronos and Mission Control | Matrix on PR #12 is proposed, not activated. Prepare explicit policy and coverage cases; avoid default broad privilege inheritance from Core. | READY |
| OPEN-11 | Carry forward roadmap and prior backlog without implementing postponed subsystems | v1.2.2 phasing: Olympus first → Mission Control → Cronos/Apex. Do not treat older Cronos blueprint as build authorization. Preserve separate projects, idempotent intake and routing through Zeus. | DEFERRED: after Olympus |
| OPEN-12 | Review Mnemosyne / second brain choices and memory night-review plugin, without replacing per-profile identity memory | Previous discussions considered Hindsight vs Obsidian and installed nightly-memory plugin, but no current compatibility/architecture decision is verified. Document decision criteria, defer deployment. | DEFERRED / NEEDS USER DECISION |
| OPEN-13 | Preserve Mission Control as separate generic + galaxy UI; native Hermes WebApp is not its replacement | Earlier proposals included Accordo starter/dashboard visual references; implementation deferred until Olympus. Maintain requirements and screen/permission inventory without creating services. | DEFERRED |
| OPEN-14 | Preserve external source-of-truth documents and historical diagrams / decisions | Older v1.1/v1.2 proposals and drawings exist outside remote GitHub, while newer v1.2.2 was discussed. Reconcile without publishing private source content or treating superseded alternatives as active design. | READY (inventory), BLOCKED (missing sources) |
| OPEN-15 | Resume together before Block 3, with a precise report of accomplished, partial and blocked work | Maintain checkpoint with commits/artifacts/evidence, approval requirements and next verified action. | READY |

## Important supersessions and exclusions

- **Latest user direction overrides earlier automatic-disable ideas:** keep existing approved plugins available through bootstrap; measure actual use and decide deactivation later.
- The original suggestion to start at 05:30 was superseded by the user's instruction to **start immediately**, while observing actual weekly quotas. Scheduled recurrence is a backup continuation mechanism, not proof of background Hermes execution.
- **No Windows/Workspace Local operation.** The only authorized engineering execution targets are Hermes Core on VPS HTTPS and SSH of that same VPS. GitHub remote documentation proposals are permitted independently.
- Old alternatives like multiple dashboards, competing Kanban implementations, a new capability registry, or a new Control Plane are **not** new build mandates.
- Users previously explored Multica; later v1.2 discussions discarded that candidate. Do not resurface it without a new demonstrated requirement.
- The Constitution's one-owner-per-side-effect requirement is still binding even when plugins are globally discoverable.
- Historical file/PR/model tests are not evidence of healthy persistent agents or recoverable live backups.

## End-of-run sweep gate

Before each autonomous run finishes, answer:
- What exact request did I complete, and where is the evidence?
- What remains partially done, unverified, or blocked?
- Which previously mentioned user request is not yet represented in this register?
- Is there a parallel, reversible activity independent of the current blocker that fits the user-approved scope?
- Can I produce that work without spending unreliable model quota, touching local Windows, leaking secrets or advancing beyond Block 3?

If the final answer is **yes**, choose and do that work while resources permit. If **no**, record the exact blocker and the first resumption condition; avoid fabricated progress or empty commits.

## GitHub CI housekeeping: final fallback

This request is lower priority than previously approved pre-Block-3 Olympus tasks and independent preparation. When other meaningful work is completed or blocked, inspect checks in the user's other GitHub repositories, especially Curatia and personal website. Apply senior developer root-cause diagnosis; distinguish historic failed runs from current failures. Do not disable checks or claim a historical red run can be turned green. A fix needs an actual reproducible defect, isolated branch/PR, tests and review.

Initial read-only GitHub Actions check on 2026-11-07:
- `Guilsc/curatia-content-engine`: latest listed `Web CI` run on 2026-11-04 **success** ([run 41771315547](https://github.com/Guilsc/curatia-content-engine/actions/runs/41771315547)); historical failures on 2026-10-28, including [run 40649992278](https://github.com/Guilsc/curatia-content-engine/actions/runs/40649992278).
- `Guilsc/my-personal-site`: latest listed `Sync project content` run on 2026-11-06 **success** ([run 42247582332](https://github.com/Guilsc/my-personal-site/actions/runs/42247582332)); `Validate production build` on 2026-11-04 **success** ([run 41785903891](https://github.com/Guilsc/my-personal-site/actions/runs/41785903891)); historical failure on 2026-11-03 ([run 41672365485](https://github.com/Guilsc/my-personal-site/actions/runs/41672365485)).
- These results do not verify all open PR checks, branch restrictions, Copilot jobs, external deployments or remaining GitHub runs. Do not attribute failures to Copilot without supporting job logs.

## Four-hour daily handoff format

For each substantive workstream, provide **Delivered**, **Blocked**, **Decision needed**, and **Remaining in approved scope**. Distinguish tool-verified results from user-reported historical context. Include commits, pull requests, acceptance gates, failed tests and next step. Identify any genuine decision that cannot be resolved by available tools, specialists, skills or plugins. When evidence is missing, do not claim completion; resume from the checkpoint next round.
