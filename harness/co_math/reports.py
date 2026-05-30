from __future__ import annotations

from pathlib import Path

from .gating import check_workstream_completion
from .schemas import utc_timestamp


def render_final(workspace: str | Path) -> Path:
    root = Path(workspace)
    final_dir = root / "final"
    final_dir.mkdir(parents=True, exist_ok=True)

    sections: list[str] = []
    for workstream in sorted((root / "workstreams").glob("*")):
        if not workstream.is_dir():
            continue
        gate = check_workstream_completion(root, workstream.name)
        if not gate.passed:
            continue
        report = workstream / "report.md"
        sections.append(
            f"## Workstream: {workstream.name}\n\n"
            + report.read_text(encoding="utf-8").strip()
        )

    if not sections:
        raise ValueError("No reviewed workstream reports are ready to render.")

    output = final_dir / "working_paper.md"
    output.write_text(
        "# Working Paper\n\n"
        f"- rendered_at: {utc_timestamp()}\n"
        "- status: draft_from_reviewed_workstreams\n"
        "- note: This is a working paper, not a chat summary.\n\n"
        + "\n\n---\n\n".join(sections)
        + "\n",
        encoding="utf-8",
    )
    return output
