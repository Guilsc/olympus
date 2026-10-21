---
name: olympus-declarative-validation
description: "Use when validating Olympus declarative role prompts."
version: 0.1.0
author: Guilsc, Hermes-Main
license: LicenseRef-Private
platforms: [windows, linux, macos]
metadata:
  hermes:
    tags: [olympus, validation, declarative-roles, native-agent]
    related_skills: [development-delivery-policy, hermes-agent, code-review]
---

# Governed Olympus declarative validation

Load development-delivery-policy and hermes-agent first. Hermes-Main remains the external host; isolated role evaluations do not change its identity. Repository-specific instructions and the user's block boundaries override this recipe.

## When to Use

Use for explicitly authorized Olympus Domain/role prompt bootstrap and isolated model-backed validation. Do not use to instantiate persistent Olympus agents or bypass an unapproved block, governance outcome, or merge gate.

## Admission and discovery

- Retrieve the actual repository path; never assume an old workspace still exists. Read its existing Governor documentation and unchanged prompt before admission.
- Run the exact supplied initiative with the repository's documented native AIAgent settings before repository changes. Preserve input tokens and authority boundaries. Extract the YAML block using a line-anchored `initiative:` boundary: prose such as 'Provide Zeus with this initiative:' must not become part of the mapping. Parse and reject duplicate keys before invoking.
- If Governor returns stop or clarify, report its raw response, make no repository changes, and stop. A proceed result is conceptual admission, not a real orchestration handoff or merge authorization.
- Fetch, confirm clean tree and matching local/remote main, read relevant architecture, and create a development branch before implementation. Preserve sequential Domain/Owner commits when requested.

## Native isolation

Use the installed host read-only configuration and native provider/credential resolver. Construct a fresh AIAgent per case with ephemeral_system_prompt and no conversation history:

```
enabled_toolsets=[]
skip_context_files=True
load_soul_identity=False
skip_memory=True
skip_background_review=True
max_iterations=1
quiet_mode=True
save_trajectories=False
```

Assert agent.tools is empty, conversation completed without failure, and returned messages contain no tool_calls/function_call/tool-role messages. Always close the agent. Do not substitute generic CLI chat, delegate_task, persistent bot/profile, or identity mutation.

## Pitfalls

On Windows, check the actual interpreter's imports and sys.path before concluding dependencies are missing. A managed python.exe may be a launcher shim; invoking its path does not necessarily expose that environment's site-packages. Discover the existing installed environment and source path, then use them only in a scratch validation process if needed. Do not install dependencies into Olympus or mutate the active host profile to repair a scratch probe.

## Evidence and semantic checks

- Keep invocation/assertion code, raw responses, and fixture evidence under the host scratch directory, outside the repository. Append completed cases to JSONL so later failures do not erase progress. Aggregate/dedupe/count from files in code.
- Use the host safe YAML parser with duplicate keys rejected; check exact fields, types, enums, canonical identities, assignment/ownership, blockers, dependency evidence, primary/supporting routing, and artifact-stage consistency. Inspect raw outputs for fabricated execution/consultation/Workers/subsystems, not only parseability.
- Make fixture intent, scope, decisions, first action, and criteria internally consistent. A wrong-Domain assignment should test routing rather than accidentally fail for an unrelated malformed handoff. Distinguish missing admission/intent information (clarify) from missing essential execution evidence on valid assigned work (blocked).
- Validate Domain-only and Owner-only separately. Pairwise contract consistency may explicitly concatenate just the two contracts with a supplied handoff fixture; it is not an executed Governor→Orchestrator→Owner chain. Do not cross a prohibited end-to-end block boundary.
- Hash exactly the normalized-newline UTF-8 prompt text loaded by Path.read_text. Record observed cases, results, hashes, limitations, and native isolation in repository documentation. Never describe prompt behavior as deterministic enforcement or authenticated authority.
- When an end-to-end block is explicitly authorized, execute fresh native conversations sequentially and nest the complete raw upstream YAML using indentation only; assert both textual transfer and independently parsed envelope equality. Assign actual returned work IDs without rewriting the plan. For satisfied dependencies, execute the actual assigned prerequisite and pass its entire raw result unchanged as evidence; supplied planned status is not completion evidence.
- Label downstream evaluations of stop/clarify/non-ready outputs as negative gate probes, never admitted execution. Disclose baseline supplemental facts and fallback invalid assignments so refusal coverage is not mistaken for an isolated missing-evidence test; exercise execution blockers separately on valid ready assignments.
- Preserve existing uncommitted execution evidence when resuming. Write complete reruns separately, use bounded batches that survive wrapper timeouts, and aggregate unique scenario/conversation/assertion counts programmatically. Retain failed exploratory assertions and source versions; never silently replace them with passing reruns. Distinguish last-batch metadata from per-conversation timestamps.
## Verification

- Confirm exact requested cases are present once each in persisted host evidence, every response matches structural/semantic assertions, raw outputs show no fabricated execution, and repository documentation hashes match loaded prompts. Report observations, not guarantees.
- Run static YAML/example/link/hash/diff checks. Review Standards and Intent separately as Hermes-Main self-review, fix findings, rerun affected native cases, and re-review the pinned final revision. Push/create one PR when authorized; read back the exact PR/head/base and main state. Stop before merge for explicit human approval.
