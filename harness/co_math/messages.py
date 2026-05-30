from __future__ import annotations

import json
from pathlib import Path

from .schemas import VALID_MESSAGE_TYPES, MessageRecord, utc_timestamp


def append_message(
    workspace: str | Path,
    *,
    sender: str,
    recipient: str,
    message_type: str,
    content: str,
    provenance: list[str] | None = None,
    uncertainty: list[str] | None = None,
) -> MessageRecord:
    if message_type not in VALID_MESSAGE_TYPES:
        raise ValueError(f"Unsupported message type: {message_type}")

    record: MessageRecord = {
        "timestamp": utc_timestamp(),
        "sender": sender,
        "recipient": recipient,
        "type": message_type,
        "content": content,
        "provenance": provenance or [],
        "uncertainty": uncertainty or [],
    }
    path = Path(workspace) / "project" / "messages.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record


def read_messages(workspace: str | Path) -> list[MessageRecord]:
    path = Path(workspace) / "project" / "messages.jsonl"
    if not path.exists():
        return []
    records: list[MessageRecord] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records
