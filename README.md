# Codex Co-Mathematician

> English | [中文](README.zh-CN.md)

A lightweight, Codex-driven workspace pattern for mathematical research.

This project is inspired by the public design principles described in Google
DeepMind's [AI co-mathematician paper](https://arxiv.org/abs/2605.06651), but
it is **not** a reproduction of their system. It adapts those ideas into a
Codex-native, filesystem-based workflow.

This repository does **not** implement a new multi-agent platform. Codex is the
driver, the repository filesystem is the shared artifact store, Codex subagents
act as workstream coordinators, specialists, and reviewers, and the harness only
provides schema, state, gating, report skeletons, and validation scripts.

## What Is Included

- `AGENTS.md`: hard operating rules for the workspace.
- `.agents/skills/codex-co-mathematician/`: the Codex Skill and reusable templates.
- `.codex/`: narrow custom agent definitions for proof, computation, review, citation checking, and synthesis.
- `harness/co_math/`: a small Python harness for workspace state and gates.
- `workspace/`: an empty scaffold for a new project.

## What Is Not Included

- No solved research project.
- No downloaded paper corpus.
- No external repository snapshots.
- No web app or agent runtime.
- No proprietary prompts or private systems.

## Install

Python 3.9+ is supported.

```bash
python3 -m pip install -e .
co-math --help
```

Without installing:

```bash
PYTHONPATH=. python3 -m harness.co_math.cli --help
```

## Use The Skill

Ask Codex to use the `codex-co-mathematician` Skill. The workflow is:

```text
onboarding -> research question formalization -> goal approval -> workstreams -> reviewer loop -> final working paper
```

The core rule is simple: no workstream starts until the user explicitly approves
a goal, and no workstream is complete until an independent reviewer approves its
report.

## Start A New Project

Initialize a workspace:

```bash
co-math init --workspace workspace
```

During onboarding, Codex should update:

```text
workspace/project/PROJECT.md
workspace/project/GOALS.yaml
workspace/project/PROJECT_STATUS.md
workspace/project/messages.jsonl
```

Draft goals are not executable. A goal can receive workstreams only when its
status is exactly:

```yaml
status: approved
```

Check approval:

```bash
co-math check-gate --workspace workspace --gate goal_approval --goal-id G1
```

Create a workstream for an approved goal:

```bash
co-math new-workstream \
  --workspace workspace \
  --goal-id G1 \
  --title "Literature baseline review" \
  --kind literature
```

Allowed workstream kinds are `proof`, `computation`, `literature`, and `review`.

## Harness Commands

```bash
co-math init --workspace workspace
co-math append-message --workspace workspace --sender project_coordinator --recipient user --type status --content "..."
co-math new-workstream --workspace workspace --goal-id G1 --title "..." --kind proof
co-math check-gate --workspace workspace --gate goal_approval --goal-id G1
co-math check-gate --workspace workspace --gate workstream_completion --workstream-id WS-G1-001-example
co-math render-final --workspace workspace
```

## Tests

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest harness/tests -q
```

## License

MIT. See `LICENSE`.
