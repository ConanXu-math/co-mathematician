# AGENTS.md

## Repository Contract

This repository is a Codex-driven AI co-mathematician workspace.

Codex is the driver:

- The Codex main thread is the Project Coordinator.
- The repository filesystem is the shared artifact store.
- Codex subagents are workstream coordinators, specialized agents, and reviewers.
- The harness only provides schemas, state files, gates, report skeletons, and validation scripts.
- Do not build a new multi-agent platform here.
- Do not start a mathematical research project during workspace initialization.

## Hard Rules

- Always run onboarding before goal approval.
- Always get explicit user approval of goals before starting any workstream.
- Never start a workstream for an unapproved goal.
- Important claims must include provenance.
- Failed explorations must be saved as durable artifacts.
- Uncertainty must be exposed explicitly in reports and status updates.
- Every workstream report must be reviewed by an independent reviewer subagent.
- A workstream whose review has not passed must not be marked complete.
- Final output must be a working paper, not a chat summary.

## Architecture Principles

These rules are adapted from the public AI co-mathematician paper
`arXiv:2605.06651v2`:

- Mathematics research is broader than proof search: literature, examples, computation, counterexamples, definitions, and exposition are first-class work.
- Research intent is refined interactively; users should not need to front-load a perfect prompt.
- The workspace is stateful and artifact-centric; durable files matter more than transient chat.
- Workstreams can run in parallel, but all must remain tied to approved goals.
- Progressive disclosure matters: high-level project state belongs in project files, while low-level execution logs belong in workstream artifacts.
- Uncertainty is a managed project variable, not an error to hide.
- Failed attempts are permanent research artifacts and should inform later work.
- Review loops are hard gates against premature success claims.

## Fixed Workspace Layout

```text
workspace/
  project/
    PROJECT.md
    GOALS.yaml
    PROJECT_STATUS.md
    messages.jsonl
  workstreams/
  final/
```

Each workstream directory should contain:

```text
WORKSTREAM.md
status.yaml
messages.jsonl
plan.md
notes.md
artifacts/
failures/
reviews/
report.md
```

## Completion Gate

A workstream may be treated as complete only when:

- `report.md` exists.
- At least one independent reviewer has approved it.
- No blocking review remains unresolved.
- The report has explicit `Provenance`, `Uncertainty`, and `Failed Explorations` sections.
- Any code-backed claim has passing tests or is marked unverified.
- Project status has been updated to reflect the workstream state.

If the gate fails, preserve the failure and escalate rather than claiming completion.
