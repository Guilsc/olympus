# Olympus bootstrap: acceptance and recovery test plan

> Planning artifact, 2026-11-07. **No test in this document has been executed** against the current VPS. This plan is not evidence of a successful backup, a deployed gateway, a healthy plugin or an approved production release.

## Authority and baseline

The authoritative Constitution remains [the eight principles](../CONSTITUTION.md). In particular: one active owner per mutable side effect, explicit bounded authority, chat not canonical state, and observable/interruption-capable background execution.

The GitHub repository's [validation workflow](../../.github/workflows/validate.yml) runs `python -m unittest discover -s tests -v` without model calls. Its success cannot establish production readiness. Historical [Block 1.5](../block-1.5.md) records a different *external host-side* validation using `openai-codex/gpt-6.1-sol`, reporting 19/19 scenarios and 58 model conversations; it is **not** a claim that today's VPS has available weekly quota, persistent Olympus agents or a live dispatch service.

This recovery test plan is for the separately authorized v1.2.2 host implementation reported in previous sessions. Reconcile exact effective paths, branches and tool interfaces on the VPS before applying.

## Test inventory

| ID | Requirement / failure mode | Procedure when authorized on VPS | Objective PASS evidence |
| --- | --- | --- | --- |
| R-01 | Correct runtime | Confirm remote connection reaches intended VPS host and Hermes Core `default`; independently inspect container/process, image digest, mount destinations and gateway owner. | Redacted host fingerprint, version/digest and proof of target environment. |
| R-02 | Preserve live session and profiles | Count and inspect actual native profiles, including `default` and eight named Olympus profiles, with their state roots. | Current profile list, isolation mapping, missing/extra profiles explicitly classified. |
| R-03 | Recover memory without cross-profile leakage | For each profile inspect SOUL/USER/MEMORY and auxiliary memory stores, verify backing paths do not alias another profile; **do not open private memory contents in public artifacts**. | Per-profile presence/hash/isolation statuses and no identified cross-profile pointers. |
| R-04 | Reliable backup coverage | Enumerate all persistent mounts/databases, snapshot using database-supported consistency mechanism, include necessary Git/worktree/proxy metadata. | Source-to-archive manifest and snapshot point-in-time metadata, with exclusions explained. |
| R-05 | Reliable backup integrity | Verify archive checksums and a safe nonproduction test extraction; distinguish file recovery from successful full service restore. | Hash verification, extraction outcome, recovery procedure, known gaps. |
| R-06 | Failed backup cannot be marked completed | Simulate, without disrupting production, missing test input or invalid archive in a **dedicated test fixture**. | Gate BLOCKED/REWORK and no next-card release. |
| R-07 | Model quota and approved routing | Identify provider + effective model and quota/429 behavior; inspect whether alias fallback is enabled. Do not invoke risky live tasks merely to probe model. | Actual approved model and capacity, or explicitly BLOCKED; no unapproved OmniRoute fallback. |
| R-08 | Plugins remain available but scoped | Inspect installed/enabled plugin versions and per-profile grants. Compare OMH behavior against actual docs/hooks. | Capability matrix with authorization boundaries and no unexplained disablement. |
| R-09 | Gate after goal completion | Evaluate card evidence using deterministic checks and separate reviewer context where feasible; simulate missing evidence on nonproduction fixture. | PASS only when original acceptance criteria match evidence; otherwise REWORK/BLOCKED. |
| R-10 | Agent ownership is non-overlapping | Try a controlled forbidden capability request against a non-owner in isolated fixtures, never real side effects. | Request refused or delegated to the designated owner; audited routing. |
| R-11 | Olympus vs Core distinction | Verify Core `default` maintenance is outside Olympus mission routing; Olympus `olympus-hermes` remains orchestrator, Zeus remains governor. | Separate profile IDs and contracts; no shared writable memory/implicit authority. |
| R-12 | WebApp and Desktop session parity | With authenticated disposable test session, connect native WebApp and Desktop to same gateway, compare session state; verify WebSocket/TLS/auth. | Session continuity and access-control smoke evidence, no exposure of protected tools without authentication. |
| R-13 | Safe proxy rollback | Record existing routes and dependencies, produce a reversible change proposal; perform an actual cutover only after separate authorization. | Proposed rollback with tested backup; current public endpoints unchanged in this milestone. |
| R-14 | Git reconciliation | Compare working tree/branches with remote `main`, read historical decisions, avoid resetting dirty files. | Diff/provenance table, preserved local-only commits, explicit proposal/PR rather than silent forced sync. |
| R-15 | No Block 3 advancement | Check Kanban and agent execution trace after pre-Block-3 cards. | No Block 3 action, no automatic deployment or scope expansion. |

## Mandatory negative tests and guardrails

1. **Unavailable provider**: a failed or 429 provider probe never selects a free model as a substitute.
2. **Missing state directory**: no automatic creation of replacement profiles or restoring old memory into current profiles.
3. **Wrong destination**: if target is not the verified VPS, abort even when the agent has permissions in a different environment.
4. **Changed plugin grants**: no consent by proxy. Preserve current plugin availability, but request explicit approval for new capabilities.
5. **Stale snapshot**: do not label a stale file-level copy as consistent for a live writable database.
6. **Reviewer disagreement**: stop the dependent card, preserve artifacts and record what evidence would resolve the issue.
7. **Interrupted/retried run**: respect native Kanban ID, idempotency key and history; don't create a duplicate or overwrite an existing attempt.
8. **Sensitive reports**: redact tokens, cookies, private keys, passwords, memory content and connection secrets. Test artifacts should contain only sanitized metadata.

## Review verdict template

```yaml
card_id: ""
goal_id: ""
observed_environment: ""
evidence_checked: []
deterministic_tests: []
reviewer_context: ""
verdict: "PENDING" # PASS | REWORK | BLOCKED
blocking_findings: []
remaining_uncertainty: []
rollback_status: "NOT_REQUIRED"
release_to_next_card: false
```

A PASS verdict must cite real artifact identifiers and test logs. Independent review is a quality gate, not a second authority to modify services.

## Immediate readiness gaps

- GitHub-only review did not inspect effective VPS Docker mounts, volumes, databases, Hermes gateway, native Kanban board, plugins, model quota or profile memories.
- The repository's existing CI checks the static contracts only; it does not cover R-01 through R-15 on a live deployment.
- The existing PR #12 is documentation-only. Do not mark this checklist executed simply because GitHub CI passes.
- Next execution should be read-only R-01/R-02/R-14, then consistent R-04/R-05 backup, then plugin/model gating, all on the authenticated VPS.
