# End-to-end validation — Session 1 Block 1.5

## Scope and verified starting point

Authorized continuation on `feat/blocks-1.3-1.4-professional-delivery` at `4f4da5d0719d9a9ba507769feada3348f29c13b7`; branch and HEAD were verified exactly. The resumed working tree already contained uncommitted Block 1.5 documentation and evidence. Those changes and the original evidence were preserved, independently checked, and supplemented with a complete fresh native rerun. The existing PR is #2. No merge is authorized or performed.

Block 1.5 executes the first host-side vertical slice:

```text
Synthetic authorized initiative
  → fresh native Governor response
  → fresh native Orchestrator response
  → individually assigned professional_delivery_owner
  → bounded result returned to canonical orchestrator
```

These are real model conversations in external Hermes-Main, not concatenated role prompts, mocked responses, or hand-authored ready snapshots. No persistent Olympus runtime, dispatch service, profile, memory, workspace lifecycle, or approval/release system is created. The final return is an Owner output, not another Orchestrator callback or a persisted initiative update.

**REQUIRED NOW:** this evidence document, the immutable [original execution evidence](validation/block-1.5.json), the [complete fresh rerun evidence](validation/block-1.5-rerun.json), and updates identifying the completed validation boundary in current architecture documentation. The host experiment source is included as text in the evidence for reproducibility, not installed as an Olympus runner. All deferred subsystems retain their existing classification.

## Native execution and unchanged transfers

Execution on 2026-10-04 used the existing read-only configuration and native credential resolver: `openai-codex` / `gpt-6.1-sol`. Every stage constructs and closes a fresh `AIAgent` using the [existing invocation](governor.md#native-invocation):

```python
enabled_toolsets=[]
skip_context_files=True
load_soul_identity=False
skip_memory=True
skip_background_review=True
save_trajectories=False
max_iterations=1
quiet_mode=True
```

No conversation history is supplied. Every recorded conversation completed without reported failure, had an empty native tool list, and returned zero tool calls. Explicit evidence written by the external experiment is not native trajectory persistence or Olympus Agent Memory.

The entire raw Governor YAML is nested under `governance`, and the entire raw Orchestrator YAML under `handoff`. Only YAML-envelope indentation and a necessary terminal newline are added; upstream values, work, scope, criteria, status and routing are not rewritten, repaired, filtered or reserialized. Raw strings, complete downstream inputs, textual transfer assertions and independent parsed-envelope equality checks are retained. For ready handoffs, assignment references an actual returned work ID; it does not modify the handoff.

Planning Room contributions are explicitly supplied synthetic fixture data, not claims of prior Owner consultation. The facts describe fictional release records, not actual software releases. The satisfied-dependency case goes further: a fresh Owner conversation performs the actual assigned prerequisite's bounded text inspection, and its **complete raw response** is passed unchanged as the dependent assignment's `dependencies[0].evidence`. The graph still contains `planned` work; evidence does not rewrite a work-status model or establish external software verification.

For Governor `stop`/`clarify` or Orchestrator non-ready results, downstream calls are **negative gate probes**, not permitted execution. They receive the same unchanged rejected/non-ready output and must refuse artifacts. A production host should not dispatch these rejected paths.

## Final scenario results

**19/19 scenarios passed; 58 completed native conversations; 895 recorded passing assertion evaluations.** Independent reparsing, envelope equality, prerequisite raw-evidence equality and final single-assigned-sentence checks also passed. The dependency case includes one extra prerequisite Owner invocation.

| Scenario | Governor → Orchestrator → Owner | Exact result / boundary |
|---|---|---|
| Successful delivery | `proceed → ready → review` | REVIEW: `Version 2 fixes the search typo.` |
| Governance stop | `stop → clarify → clarify` | Worker restriction preserved; no artifact |
| Governance clarification | `clarify → clarify → clarify` | Empty objective; no planning or artifact |
| Missing supplied Owner | `proceed → clarify → clarify` | No invented Owner or assignment |
| Missing facts at admission | `clarify → clarify → clarify` | Authoritative release fact requested; no invented fix |
| Missing specialist evidence | `proceed → planning → clarify` | Selected Owner's blocking objection retained; requested release-record evidence; non-ready Owner probe refused |
| Ready without ceremony | `proceed → ready → review` | Complete supplied facts suffice without a ceremonial contribution; version-2 sentence only |
| Primary ownership mismatch | `clarify → clarify → clarify` | Research-first objective not forced into Work; Owner returns `research_learning` / `primary` routing, no artifact |
| Satisfied dependency | `proceed → ready → review → review` | First Owner inspects `verify_fact`; unchanged raw finding becomes dependency evidence; second Owner produces version-2 sentence at REVIEW |
| Unsatisfied dependency | `proceed → ready → blocked` | Explicit unsatisfied prerequisite; no artifact |
| Missing dependency evidence | `proceed → ready → clarify` | Required prerequisite entry absent; no artifact |
| Wrong assigned Owner | `proceed → ready → clarify` | No silent reassignment; `work_id: null` |
| Wrong assigned Domain | `proceed → ready → clarify` | Assignment correction requested; `work_id: null` |
| Only one assigned item | `proceed → ready → review` | Actual two-item plan; only version-2 sentence returned, no version-3 sentence or initiative-wide completion |
| Scope exclusions | `proceed → ready → review` | Campaign and Worker prompt explicitly excluded; original sentence only |
| Approval/release boundaries | `proceed → ready → review` | Earlier artifact approval confers neither approval nor release of this artifact; REVIEW only |
| Late missing execution fact | `proceed → ready → blocked` | Valid assignment but fact withdrawn as unverified; no artifact; bounded research support returned conceptually |
| Initiative isolation: beta | `proceed → ready → review` | REVIEW: `Version 9 adds offline export.`; no alpha facts |
| Initiative isolation: alpha again | `proceed → ready → review` | REVIEW: `Version 2 fixes the search typo.`; no beta facts |

All final sentence products are exactly the sentence shown for their initiative. The prerequisite result instead explicitly limits its finding to inspection of the supplied text, not actual software behavior. No product is APPROVED or RELEASED; no rejection/blocked result contains a work product or claims checks were performed.

### Prompt hashes

SHA-256 covers UTF-8 normalized-newline prompt text actually loaded through `Path.read_text`, not raw platform newline bytes. All three prompts are unchanged from the verified starting revision.

| Prompt | SHA-256 |
|---|---|
| Governor | `a1aa380d350ef8fc0bebf22ff501830cf7762a29b7545fa6e5754a1d7133e205` |
| Orchestrator | `162cc29c8921394b964fa2d03f8213dd51d012dfc7d36ea7a1c89018f62800b0` |
| professional_delivery_owner | `651a4a80355fd89d7b3ed5cf1cdeea06ad79cda873730bbd39a2f69519a56726` |

## Demonstrated issues and reruns

Four retained failed exploratory assertions were experiment issues, not demonstrated prompt defects:

1. The two-item fixture inherited a contradictory exactly-one-sentence initiative criterion. Governor correctly requested clarification. The criterion was corrected to one sentence **per assigned item**; the actual final two-item plan and single-assignment result passed.
2. A missing-facts fixture still named the intended fix in its criterion while withholding the fact, and expected `proceed`. Governor correctly requested authoritative context. The fixture no longer embeds that fix as acceptance evidence, and validates the clarification chain.
3. A research-first fixture expected admission despite having no established suitable handling path. Governor's clarification is valid under its existing policy; the expected gate result was corrected, not the output or role prompt.
4. Removing a contribution while leaving all necessary facts supplied was incorrectly expected to prevent readiness. Orchestrator correctly avoided ceremonial questioning. A distinct evidence-gap case supplies an explicit unresolved specialist objection, and a separate complete-facts case tests readiness without ceremony.

The evidence retains all four failed records with their raw outputs/assertions and source versions. The final matrix was rerun after fixture corrections. A 420-second tool-wrapper timeout interrupted the large batch after 13 fully recorded scenarios; no validator process remained, and the remaining six were rerun in a bounded second batch. The satisfied-dependency case was then rerun with actual prerequisite output replacing the earlier host-evidence fixture. The final 19-case evidence set therefore has 58 conversations; it is not a claim to count every exploratory or interrupted API invocation. The superseded host-evidence dependency record is retained separately.

No demonstrated Governor, Orchestrator or Owner defect required a prompt change. No speculative fix, new Owner, Worker or deferred subsystem was added.

## Complete fresh rerun on resume

The [fresh rerun evidence](validation/block-1.5-rerun.json) preserves another complete execution of the same 19 scenarios in three bounded batches (7, 6, 6), without replacing the original evidence or its failed exploratory records. It records **19/19 passed, 58 completed native conversations, 895 passing assertion evaluations**, and **488 independent schema rechecks**. Raw response reparsing, exact textual and semantic transfers, unchanged prerequisite-response evidence, canonical routing, invalid-assignment null work IDs, and exact final sentence products passed. Native metadata in this rerun file describes the last batch; it is not a per-conversation timestamp log. The validator and resume-wrapper source snapshots and hashes are retained.

The status chains and exact sentence products match the matrix above. The two complete retained matrices contain 116 completed conversations and 1,790 recorded passing assertion evaluations; these totals exclude failed, interrupted, and superseded exploratory attempts. Negative probes intentionally retain the host's baseline supplemental context and use a fallback `draft_update` assignment when no ready work exists. They demonstrate gate refusal despite that context, not valid admission or isolated missing-fact execution; the separate ready-then-withdrawn-fact scenario exercises the execution blocker on a valid assignment.

Static read-back verifies both evidence files, prompt hashes, source compilation, YAML examples, local links, absence of deferred subsystems, unchanged `main`, and whitespace checks. All raw rerun Owner responses were inspected for invented retrieval, testing, consultation, approval, release, and initiative-wide completion. No demonstrated role defect required a fix.

## Separate self-reviews

### Standards

Hermes-Main reviewed the Block 1.5 delta against the Constitution, Complexity Gate, canonical/theme separation, existing role contracts, privacy/security, artifact/no-tools boundaries and the code-review smell baseline. Host experiment source is immutable evidence text, not production architecture. Raw inputs/responses are deliberately retained once per recorded stage; parser/schema assertions do not replace semantic inspection. Credentials, native host messages and trajectories are excluded.

Experiment fixture contradictions and overstrict expectations were corrected and rerun as described above. The resumed review also corrected an inaccurate clean-working-tree description, qualified actual work-ID assignment claims to ready handoffs, documented negative-probe supplemental-context limitations, and corrected two prose defects. Current-status documentation now separates prior synthetic/pairwise validation from executed host-side chains. The full fresh native matrix and persisted-evidence checks passed after the experiment corrections; subsequent changes are documentation-only. No unresolved material Standards finding remains. This is implementer self-review, not an independent-context review.

### Intent / Spec

The fixed Block 1.5 review base is `4f4da5d0719d9a9ba507769feada3348f29c13b7`; the full PR also retains the earlier Blocks 1.3/1.4 changes relative to `9befe36c024921c2679b285683d463a827f1c3f5`. The reviewed final commit is pinned in PR #2's evidence package.

**Did we build what was actually requested? Yes, within the requested host-side validation boundary:** real Governor → Orchestrator → bound Owner → result calls; unchanged actual outputs; all requested behavioral boundaries; inputs/raw responses/prompt hashes/assertions/exact results; correction only of demonstrated experiment issues; final validation and separate reviews; English evidence on the same branch. No merge or deferred subsystem is included. No unresolved Intent/Spec finding remains.

## Limitations and merge gate

- Observed model behavior is not deterministic enforcement, exhaustive adversarial coverage, externally authenticated authority, or guaranteed repeatability.
- Synthetic supplied-fact text and actual text inspection were exercised, not code execution, real release-record retrieval, experiments, deployment, external review, acceptance or release.
- Planning Room testimony other than the executed prerequisite is host-supplied fixture data, not an invoked specialist consultation workflow.
- Sequential fresh conversations demonstrate initiative isolation in this experiment; concurrent scheduling and production technical isolation are not implemented.
- No persistent runtime, durable initiative state, Delivery Workspace, approval engine, return callback, memory/capabilities/observability platform, Board, other Owner, or Worker is delivered.
- There is no Olympus application/build/CI stack. Safe YAML, links, hashes, transfer/schema/content assertions and clean diffs supplement actual model execution.

The evidence/documentation change is reversible and has no external artifact side effect. Block 1.5 is ready for human review in the existing PR; integration into `main` still requires fresh explicit approval for the reviewed revision. **Stop before merge.**
