from __future__ import annotations

import argparse
import json
from pathlib import Path

from .gating import check_gate
from .messages import append_message
from .reports import render_final
from .schemas import VALID_MESSAGE_TYPES, VALID_WORKSTREAM_KINDS
from .workspace import init_workspace, new_workstream


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="co-math")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize workspace scaffold")
    init_parser.add_argument("--workspace", default="workspace")
    init_parser.set_defaults(func=_cmd_init)

    message_parser = subparsers.add_parser("append-message", help="Append JSONL message")
    message_parser.add_argument("--workspace", default="workspace")
    message_parser.add_argument("--sender", required=True)
    message_parser.add_argument("--recipient", required=True)
    message_parser.add_argument("--type", dest="message_type", choices=VALID_MESSAGE_TYPES, required=True)
    message_parser.add_argument("--content", required=True)
    message_parser.add_argument("--provenance", action="append", default=[])
    message_parser.add_argument("--uncertainty", action="append", default=[])
    message_parser.set_defaults(func=_cmd_append_message)

    ws_parser = subparsers.add_parser("new-workstream", help="Create approved-goal workstream")
    ws_parser.add_argument("--workspace", default="workspace")
    ws_parser.add_argument("--goal-id", required=True)
    ws_parser.add_argument("--title", required=True)
    ws_parser.add_argument("--kind", choices=VALID_WORKSTREAM_KINDS, required=True)
    ws_parser.set_defaults(func=_cmd_new_workstream)

    gate_parser = subparsers.add_parser("check-gate", help="Check a harness gate")
    gate_parser.add_argument("--workspace", default="workspace")
    gate_parser.add_argument(
        "--gate",
        choices=("goal_approval", "workstream_completion", "final_render"),
        required=True,
    )
    gate_parser.add_argument("--goal-id")
    gate_parser.add_argument("--workstream-id")
    gate_parser.add_argument("--json", action="store_true")
    gate_parser.set_defaults(func=_cmd_check_gate)

    render_parser = subparsers.add_parser("render-final", help="Render final working paper")
    render_parser.add_argument("--workspace", default="workspace")
    render_parser.set_defaults(func=_cmd_render_final)

    return parser


def _cmd_init(args: argparse.Namespace) -> int:
    root = init_workspace(args.workspace)
    print(f"Initialized workspace: {Path(root)}")
    return 0


def _cmd_append_message(args: argparse.Namespace) -> int:
    record = append_message(
        args.workspace,
        sender=args.sender,
        recipient=args.recipient,
        message_type=args.message_type,
        content=args.content,
        provenance=args.provenance,
        uncertainty=args.uncertainty,
    )
    print(json.dumps(record, ensure_ascii=False))
    return 0


def _cmd_new_workstream(args: argparse.Namespace) -> int:
    path = new_workstream(
        args.workspace,
        goal_id=args.goal_id,
        title=args.title,
        kind=args.kind,
    )
    print(f"Created workstream: {path}")
    return 0


def _cmd_check_gate(args: argparse.Namespace) -> int:
    result = check_gate(
        args.workspace,
        args.gate,
        goal_id=args.goal_id,
        workstream_id=args.workstream_id,
    )
    if args.json:
        print(
            json.dumps(
                {
                    "gate": result.gate,
                    "passed": result.passed,
                    "issues": result.issues,
                    "details": result.details,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"{'PASS' if result.passed else 'FAIL'} {result.gate}")
        for issue in result.issues:
            print(f"- {issue}")
    return 0 if result.passed else 1


def _cmd_render_final(args: argparse.Namespace) -> int:
    path = render_final(args.workspace)
    print(f"Rendered final working paper: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
