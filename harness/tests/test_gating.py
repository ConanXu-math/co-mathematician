from __future__ import annotations

import json

import pytest
import yaml

from harness.co_math.gating import check_goal_approval, check_workstream_completion
from harness.co_math.workspace import init_workspace, new_workstream


def write_goals(workspace, goals):
    path = workspace / "project" / "GOALS.yaml"
    path.write_text(
        yaml.safe_dump({"research_question": {"status": "draft"}, "goals": goals}),
        encoding="utf-8",
    )


def write_review(workstream, name, payload):
    review_path = workstream / "reviews" / name
    review_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def valid_report() -> str:
    return """# Workstream Report

## Summary
This is a scaffold validation report, not a mathematical result.

## Claims
- Claim C1: The initialization gate has an auditable report.

## Provenance
- Claim C1: harness/tests/test_gating.py

## Uncertainty
- No mathematical claim is being made.

## Failed Explorations
- None for this scaffold-only workstream.
"""


def test_goal_approval_gate_blocks_unapproved_goal(tmp_path):
    workspace = tmp_path / "workspace"
    init_workspace(workspace)
    write_goals(workspace, [{"id": "G1", "title": "Draft goal", "status": "draft"}])

    gate = check_goal_approval(workspace, goal_id="G1")
    assert not gate.passed
    assert "not approved" in gate.issues[0]

    with pytest.raises(ValueError, match="not approved"):
        new_workstream(workspace, goal_id="G1", title="Should not start", kind="proof")


def test_workstream_completion_gate_requires_report_review_and_provenance(tmp_path):
    workspace = tmp_path / "workspace"
    init_workspace(workspace)
    write_goals(workspace, [{"id": "G1", "title": "Approved goal", "status": "approved"}])
    workstream = new_workstream(
        workspace, goal_id="G1", title="Initialization validation", kind="review"
    )

    missing_report = check_workstream_completion(workspace, workstream.name)
    assert not missing_report.passed
    assert any("report.md" in issue for issue in missing_report.issues)

    (workstream / "report.md").write_text("# Report without provenance", encoding="utf-8")
    no_review = check_workstream_completion(workspace, workstream.name)
    assert not no_review.passed
    assert any("reviewer approval" in issue for issue in no_review.issues)

    write_review(
        workstream,
        "logic_reviewer.json",
        {
            "approved": True,
            "severity": "info",
            "issue_type": "logic",
            "reviewer": "logic_reviewer",
            "comment": "Looks consistent.",
            "suggested_fix": "",
        },
    )
    no_provenance = check_workstream_completion(workspace, workstream.name)
    assert not no_provenance.passed
    assert any("Provenance" in issue for issue in no_provenance.issues)

    (workstream / "report.md").write_text(valid_report(), encoding="utf-8")
    write_review(
        workstream,
        "adversarial_reviewer.json",
        {
            "approved": False,
            "severity": "blocking",
            "issue_type": "missing_provenance",
            "reviewer": "adversarial_reviewer",
            "comment": "A blocking issue remains.",
            "suggested_fix": "Add provenance.",
        },
    )
    blocked = check_workstream_completion(workspace, workstream.name)
    assert not blocked.passed
    assert any("blocking review" in issue for issue in blocked.issues)

    (workstream / "reviews" / "adversarial_reviewer.json").unlink()
    passed = check_workstream_completion(workspace, workstream.name)
    assert passed.passed
    assert passed.issues == []
