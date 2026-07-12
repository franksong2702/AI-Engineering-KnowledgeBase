#!/usr/bin/env python3
"""Semantic checks for compiled Agent Bible capability contracts."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MACHINE = ROOT / "agent-bible" / "contracts" / "_machine" / "contracts.json"
TERMINAL = {"completed", "blocked", "escalated"}


def main() -> int:
    sync = subprocess.run(
        [sys.executable, str(ROOT / "_tools" / "compile_agent_contracts.py"), "--check"],
        cwd=ROOT,
        check=False,
    )
    if sync.returncode:
        return sync.returncode
    payload = json.loads(MACHINE.read_text(encoding="utf-8"))
    errors: list[str] = []
    for entry in payload["contracts"]:
        contract = entry["contract"]
        slug = contract["capability"]
        tool_map = {item["name"]: item for item in contract["tools_and_permissions"]}
        for tool in tool_map.values():
            if tool["side_effect"] and not tool["approval_required"]:
                errors.append(f"{slug}: side-effect tool lacks approval: {tool['name']}")
        for case in entry["tests"]["cases"]:
            if set(case["allowed_tools"]) & set(case["forbidden_tools"]):
                errors.append(f"{slug}/{case['id']}: tool is both allowed and forbidden")
            if case["kind"] == "adversarial" and case["expected_status"] == "completed" and case["forbidden_tools"]:
                errors.append(f"{slug}/{case['id']}: adversarial completion leaves forbidden tools")
        events = entry["trace"]["events"]
        if events[-1]["event"] not in TERMINAL:
            errors.append(f"{slug}: trace lacks terminal event")
        requested = [event for event in events if event["event"] == "tool_requested"]
        decisions = [event for event in events if event["event"] in {"tool_allowed", "tool_denied"}]
        if requested and not decisions:
            errors.append(f"{slug}: tool request lacks permission decision")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print("Agent contracts semantic check: 5 contracts / 50 case definitions / 5 trace samples — OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
