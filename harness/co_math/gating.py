from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schemas import GateResult
from .workspace import find_goal, load_goals, read_yaml


def check_goal_approval(workspace: str | Path, goal_id: str | None = None) -> GateResult:
    goals_data = load_goals(workspace)
    goals = goals_data.get("goals", [])
    issues: list[str] = []

    if goal_id is not None:
        goal = find_goal(goals_data, goal_id)
        if goal is None:
            issues.append(f"Goal {goal_id} was not found.")
        elif str(goal.get("status", "")).lower() != "approved":
            issues.append(
                f"Goal {goal_id} is not approved (status: {goal.get('status', 'missing')})."
            )
    elif not any(str(goal.get("status", "")).lower() == "approved" for goal in goals):
        issues.append("No approved goals are recorded.")

    return GateResult("goal_approval", not issues, issues, {"goal_id": goal_id})


def check_workstream_completion(
    workspace: str | Path, workstream_id: str | None = None
) -> GateResult:
    root = Path(workspace)
    workstreams = _selected_workstreams(root, workstream_id)
    issues: list[str] = []
    details: dict[str, Any] = {"workstreams": [path.name for path in workstreams]}

    if not workstreams:
        issues.append("No workstream directories were found.")

    for workstream in workstreams:
        issues.extend(_workstream_issues(workstream))

    return GateResult("workstream_completion", not issues, issues, details)


def check_final_render(workspace: str | Path) -> GateResult:
    root = Path(workspace)
    approved = []
    rejected = {}
    for workstream in sorted((root / "workstreams").glob("*")):
        if not workstream.is_dir():
            continue
        gate = check_workstream_completion(root, workstream.name)
        if gate.passed:
            approved.append(workstream.name)
        else:
            rejected[workstream.name] = gate.issues

    issues = [] if approved else ["No reviewed workstream reports are ready to render."]
    return GateResult(
        "final_render",
        not issues,
        issues,
        {"approved_workstreams": approved, "rejected_workstreams": rejected},
    )


def check_gate(
    workspace: str | Path,
    gate: str,
    *,
    goal_id: str | None = None,
    workstream_id: str | None = None,
) -> GateResult:
    if gate == "goal_approval":
        return check_goal_approval(workspace, goal_id)
    if gate == "workstream_completion":
        return check_workstream_completion(workspace, workstream_id)
    if gate == "final_render":
        return check_final_render(workspace)
    raise ValueError(f"Unsupported gate: {gate}")


def _selected_workstreams(root: Path, workstream_id: str | None) -> list[Path]:
    workstreams_dir = root / "workstreams"
    if workstream_id:
        path = workstreams_dir / workstream_id
        return [path] if path.exists() else []
    if not workstreams_dir.exists():
        return []
    return sorted(path for path in workstreams_dir.iterdir() if path.is_dir())


def _workstream_issues(workstream: Path) -> list[str]:
    label = workstream.name
    issues: list[str] = []
    status = _load_status(workstream)
    report = workstream / "report.md"
    reviews = _load_reviews(workstream)

    if not report.exists():
        issues.append(f"{label}: report.md is missing.")

    approved_reviewers = [
        review.get("reviewer", path.stem)
        for path, review in reviews
        if review.get("approved") is True
    ]
    coordinator = status.get("coordinator", "workstream_coordinator")
    independent_approvals = [
        reviewer for reviewer in approved_reviewers if reviewer != coordinator
    ]
    if not independent_approvals:
        issues.append(f"{label}: missing independent reviewer approval.")

    for path, review in reviews:
        if review.get("severity") == "blocking":
            issues.append(f"{label}: blocking review in {path.name}.")

    if report.exists():
        text = report.read_text(encoding="utf-8")
        if not _has_section(text, "Provenance"):
            issues.append(f"{label}: report.md is missing a Provenance section.")
        if not _has_section(text, "Uncertainty"):
            issues.append(f"{label}: report.md is missing an Uncertainty section.")
        if not _has_section(text, "Failed Explorations"):
            issues.append(f"{label}: report.md is missing a Failed Explorations section.")

    return issues


def _load_status(workstream: Path) -> dict[str, Any]:
    path = workstream / "status.yaml"
    if path.exists():
        data = read_yaml(path)
        return data if isinstance(data, dict) else {}
    return {}


def _load_reviews(workstream: Path) -> list[tuple[Path, dict[str, Any]]]:
    reviews_dir = workstream / "reviews"
    if not reviews_dir.exists():
        return []
    reviews = []
    for path in sorted(reviews_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {"severity": "blocking", "comment": "Review JSON is invalid."}
        reviews.append((path, data))
    return reviews


def _has_section(text: str, section: str) -> bool:
    expected = f"## {section}".lower()
    return any(line.strip().lower() == expected for line in text.splitlines())
