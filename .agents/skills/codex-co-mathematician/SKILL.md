---
name: codex-co-mathematician
description: Use when conducting a Codex-driven mathematical research project that needs durable workspace state, approved goals, parallel workstreams, reviewer gates, provenance, uncertainty tracking, failed exploration records, and a final working paper.
---

# Codex Co-Mathematician

Use this skill to run mathematical research as a stateful Codex workspace. Codex remains the driver; do not implement a new platform. The harness is only for state, schema, gates, report skeletons, and validation.

## Non-Negotiable Flow

```text
onboarding -> research question formalization -> goal approval -> workstreams -> reviewer loop -> final working paper
```

- Do not solve the math problem during onboarding.
- Do not start a workstream until the user explicitly approves a goal.
- Do not mark a workstream complete until an independent reviewer approves its report.
- Do not hide uncertainty, failed attempts, or missing provenance.

## Onboarding

Collect enough context to write `workspace/project/PROJECT.md`:

- problem statement and mathematical setting
- definitions, notation, constraints, and allowed assumptions
- known references and user-provided artifacts
- desired output type and unacceptable shortcuts
- user expertise, steering preferences, and review expectations

Record durable status in `workspace/project/messages.jsonl`. Keep user-facing chat high level; put detailed logs in files.

## Research Question And Goals

Write a formal research question and proposed goals in `workspace/project/GOALS.yaml`. Goals begin as drafts. Ask the user to approve or revise them. Only goals with `status: approved` may receive workstreams.

Use:

```bash
PYTHONPATH=. python3 -m harness.co_math.cli check-gate --workspace workspace --gate goal_approval --goal-id G1
```

## Workstreams

Create workstreams only after goal approval:

```bash
PYTHONPATH=. python3 -m harness.co_math.cli new-workstream --workspace workspace --goal-id G1 --title "..." --kind proof
```

Valid kinds are `proof`, `computation`, `literature`, and `review`.

Workstreams must write durable artifacts:

- `WORKSTREAM.md` for scope
- `plan.md` for route
- `notes.md` for running observations
- `messages.jsonl` for internal messages
- `artifacts/` for code, tables, figures, proof sketches, or citations
- `failures/` for dead ends and rejected attempts
- `reviews/` for independent reviewer output
- `report.md` for the reviewed workstream report

## Internal Messages As JSONL

Each message must include:

```json
{
  "timestamp": "...",
  "sender": "...",
  "recipient": "...",
  "type": "status",
  "content": "...",
  "provenance": [],
  "uncertainty": []
}
```

Use message types: `status`, `instruction`, `question`, `decision`, `artifact`, `review`, `failure`.

## Provenance And Uncertainty

Every important claim must be traceable to one or more of:

- user input
- literature reference
- internal artifact
- computation output
- proof sketch
- reviewer comment
- failed exploration

Reports must contain explicit `Provenance`, `Uncertainty`, and `Failed Explorations` sections.

## Reviewer Loop

Send each workstream report to an independent reviewer subagent. Reviewers should output JSON matching `assets/reviewer_output_schema.json`.

If review fails:

- preserve the review in `reviews/`
- revise or escalate
- keep unresolved uncertainty visible
- do not mark the workstream complete

Use:

```bash
PYTHONPATH=. python3 -m harness.co_math.cli check-gate --workspace workspace --gate workstream_completion --workstream-id <id>
```

## Final Working Paper

Render final output only from reviewed workstream reports:

```bash
PYTHONPATH=. python3 -m harness.co_math.cli render-final --workspace workspace
```

The final output is `workspace/final/working_paper.md`. It is a working paper, not a chat summary.

## Assets

Use templates in `assets/` when creating project files, goals, workstreams, reports, or reviewer output.
