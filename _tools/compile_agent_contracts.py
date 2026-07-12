#!/usr/bin/env python3
"""Compile canonical Agent Bible contract blocks into one machine JSON file."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_DIR = ROOT / "agent-bible" / "contracts"
MACHINE_FILE = CONTRACT_DIR / "_machine" / "contracts.json"
EXPECTED_CAPABILITIES = {
    "research_evidence",
    "fact_verification",
    "architecture_tradeoff",
    "root_cause_diagnosis",
    "rubric_review",
}
CONTRACT_FIELDS = {
    "capability",
    "contract_version",
    "source_role",
    "when_to_use",
    "when_not_to_use",
    "input_schema",
    "output_schema",
    "tools_and_permissions",
    "state_schema",
    "memory_policy",
    "budget",
    "stop_block_escalate",
    "failure_protocol",
    "trace_schema",
    "ads_refs",
}
ADS_FILES = {
    "SIT": ROOT / "agent-decision-system" / "01_SITUATION-ROUTER.md",
    "PAT": ROOT / "agent-decision-system" / "02_PATTERN-CARDS.md",
    "ANTI": ROOT / "agent-decision-system" / "03_ANTIPATTERN-DETECTORS.md",
    "LAW": ROOT / "agent-decision-system" / "04_LAW-INVARIANTS.md",
    "Q": ROOT / "agent-decision-system" / "05_EVAL-CHECKLIST.md",
}


def extract_json(text: str, tag: str, source: Path) -> Any:
    pattern = rf"<!-- {re.escape(tag)} -->\s*```json\s*(.*?)\s*```"
    matches = re.findall(pattern, text, flags=re.S)
    if len(matches) != 1:
        raise ValueError(f"{source}: expected exactly one {tag} block, found {len(matches)}")
    try:
        return json.loads(matches[0])
    except json.JSONDecodeError as exc:
        raise ValueError(f"{source}: invalid JSON in {tag}: {exc}") from exc


def ads_ids() -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for prefix, path in ADS_FILES.items():
        text = path.read_text(encoding="utf-8")
        result[prefix] = set(re.findall(rf"^## ({prefix}-\d+)", text, flags=re.M))
    return result


def require_list(value: Any, name: str, source: Path) -> list[Any]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{source}: {name} must be a non-empty list")
    return value


def validate_schema(schema: Any, name: str, source: Path) -> None:
    if not isinstance(schema, dict) or schema.get("type") != "object":
        raise ValueError(f"{source}: {name} must be an object JSON schema")
    if not isinstance(schema.get("properties"), dict) or not isinstance(schema.get("required"), list):
        raise ValueError(f"{source}: {name} needs properties and required")
    if not set(schema["required"]) <= set(schema["properties"]):
        raise ValueError(f"{source}: {name}.required references missing properties")


def validate_entry(entry: dict[str, Any], known_ads: dict[str, set[str]], source: Path) -> None:
    contract = entry["contract"]
    if set(contract) != CONTRACT_FIELDS:
        missing = sorted(CONTRACT_FIELDS - set(contract))
        extra = sorted(set(contract) - CONTRACT_FIELDS)
        raise ValueError(f"{source}: contract fields mismatch; missing={missing}, extra={extra}")
    if not re.fullmatch(r"[a-z][a-z0-9_]+", contract["capability"]):
        raise ValueError(f"{source}: invalid capability slug")
    if not re.fullmatch(r"\d+\.\d+\.\d+", contract["contract_version"]):
        raise ValueError(f"{source}: contract_version must be semantic x.y.z")
    for field in ("when_to_use", "when_not_to_use"):
        require_list(contract[field], field, source)
    validate_schema(contract["input_schema"], "input_schema", source)
    validate_schema(contract["output_schema"], "output_schema", source)
    if "status" not in contract["output_schema"]["required"]:
        raise ValueError(f"{source}: output_schema must require status")

    tools = require_list(contract["tools_and_permissions"], "tools_and_permissions", source)
    tool_names: set[str] = set()
    tool_fields = {"name", "permission", "scope", "side_effect", "approval_required", "when_unavailable"}
    for tool in tools:
        if not isinstance(tool, dict) or set(tool) != tool_fields:
            raise ValueError(f"{source}: tool fields mismatch")
        if tool["name"] in tool_names:
            raise ValueError(f"{source}: duplicate tool {tool['name']}")
        tool_names.add(tool["name"])
        if tool["permission"] not in {"read", "write", "execute", "external_send"}:
            raise ValueError(f"{source}: invalid permission for {tool['name']}")
        if not isinstance(tool["side_effect"], bool) or not isinstance(tool["approval_required"], bool):
            raise ValueError(f"{source}: side_effect/approval_required must be booleans")

    validate_schema(contract["state_schema"], "state_schema", source)
    memory_fields = {"persist", "prohibit", "write_condition", "provenance", "conflict", "expiry"}
    if set(contract["memory_policy"]) != memory_fields:
        raise ValueError(f"{source}: memory_policy fields mismatch")
    budget = contract["budget"]
    if set(budget) != {"max_steps", "max_tool_calls", "max_seconds"} or any(
        not isinstance(budget[key], int) or budget[key] <= 0 for key in budget
    ):
        raise ValueError(f"{source}: budget must contain positive integer limits")
    terminal = contract["stop_block_escalate"]
    if set(terminal) != {"stop", "block", "escalate"}:
        raise ValueError(f"{source}: stop_block_escalate fields mismatch")
    for key in terminal:
        require_list(terminal[key], f"stop_block_escalate.{key}", source)
    if not isinstance(contract["failure_protocol"], dict) or not contract["failure_protocol"]:
        raise ValueError(f"{source}: failure_protocol must be non-empty")
    trace_fields = {"required_event_fields", "allowed_events", "terminal_events"}
    if set(contract["trace_schema"]) != trace_fields:
        raise ValueError(f"{source}: trace_schema fields mismatch")

    refs = contract["ads_refs"]
    if set(refs) != set(known_ads):
        raise ValueError(f"{source}: ads_refs must contain {sorted(known_ads)}")
    for prefix, values in refs.items():
        require_list(values, f"ads_refs.{prefix}", source)
        unknown = set(values) - known_ads[prefix]
        if unknown:
            raise ValueError(f"{source}: unknown ADS ids {sorted(unknown)}")

    tests = entry["tests"].get("cases") if isinstance(entry["tests"], dict) else None
    if not isinstance(tests, list) or len(tests) != 10:
        raise ValueError(f"{source}: agent-tests must contain exactly 10 cases")
    test_fields = {"id", "kind", "input", "expected_status", "allowed_tools", "forbidden_tools", "expected_stop_reason"}
    ids: set[str] = set()
    kinds = {"normal": 0, "adversarial": 0}
    for case in tests:
        if not isinstance(case, dict) or set(case) != test_fields:
            raise ValueError(f"{source}: test fields mismatch")
        if case["id"] in ids:
            raise ValueError(f"{source}: duplicate test id {case['id']}")
        ids.add(case["id"])
        if case["kind"] not in kinds:
            raise ValueError(f"{source}: invalid test kind")
        kinds[case["kind"]] += 1
        if case["expected_status"] not in {"completed", "partial", "blocked", "escalated"}:
            raise ValueError(f"{source}: invalid expected_status")
        if set(case["allowed_tools"]) - tool_names or set(case["forbidden_tools"]) - tool_names:
            raise ValueError(f"{source}: test references unknown tool")
    if kinds != {"normal": 5, "adversarial": 5}:
        raise ValueError(f"{source}: tests require 5 normal and 5 adversarial cases")

    events = entry["trace"].get("events") if isinstance(entry["trace"], dict) else None
    if not isinstance(events, list) or len(events) < 4:
        raise ValueError(f"{source}: trace must contain at least four events")
    required_event_fields = set(contract["trace_schema"]["required_event_fields"])
    allowed_events = set(contract["trace_schema"]["allowed_events"])
    terminal_events = set(contract["trace_schema"]["terminal_events"])
    for event in events:
        if not required_event_fields <= set(event):
            raise ValueError(f"{source}: trace event missing required fields")
        if event["event"] not in allowed_events:
            raise ValueError(f"{source}: trace has unknown event {event['event']}")
    if events[0]["event"] != "task_received" or events[-1]["event"] not in terminal_events:
        raise ValueError(f"{source}: trace must start at task_received and end at a terminal event")


def build_payload() -> dict[str, Any]:
    known_ads = ads_ids()
    entries: list[dict[str, Any]] = []
    pages = sorted(CONTRACT_DIR.glob("[0-9][0-9]_*.md"))
    pages = [page for page in pages if not page.name.startswith("00_")]
    for page in pages:
        text = page.read_text(encoding="utf-8")
        entry = {
            "source": page.relative_to(ROOT).as_posix(),
            "contract": extract_json(text, "agent-contract", page),
            "tests": extract_json(text, "agent-tests", page),
            "trace": extract_json(text, "agent-trace", page),
        }
        validate_entry(entry, known_ads, page)
        entries.append(entry)
    capabilities = [entry["contract"]["capability"] for entry in entries]
    if set(capabilities) != EXPECTED_CAPABILITIES or len(capabilities) != len(set(capabilities)):
        raise ValueError(f"expected five capabilities {sorted(EXPECTED_CAPABILITIES)}, got {sorted(capabilities)}")
    entries.sort(key=lambda item: item["contract"]["capability"])
    return {"generated_by": "_tools/compile_agent_contracts.py", "contracts": entries}


def render(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if machine file differs from canonical Markdown")
    args = parser.parse_args()
    try:
        expected = render(build_payload())
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if args.check:
        actual = MACHINE_FILE.read_text(encoding="utf-8") if MACHINE_FILE.exists() else ""
        if actual != expected:
            print(f"ERROR: machine file out of sync: {MACHINE_FILE.relative_to(ROOT)}", file=sys.stderr)
            return 2
        print("Agent contracts machine sync: OK")
        return 0
    MACHINE_FILE.parent.mkdir(parents=True, exist_ok=True)
    MACHINE_FILE.write_text(expected, encoding="utf-8")
    print(f"Compiled 5 contracts -> {MACHINE_FILE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
