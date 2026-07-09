#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent Decision System · md → 机器可读影子文件编译器（严格校验版）

正典是 markdown；本脚本把 5 个模块编译为 YAML（JSON 值编码，任何 YAML/JSON
解析器可读），输出到 agent-decision-system/_machine/。

严格校验项：
  1. 每个模块的条目数量与 ID 序列必须符合 schema。
  2. 每个条目必须包含该模块要求的全部字段。
  3. 字段名必须能映射到 schema；字段值不能为空。
  4. 同一条目不得重复字段，同一模块不得重复 ID。
  5. 所有 LAW/PAT/ANTI/SIT/Q 引用必须指向存在 ID。
  6. ANTI 条目必须带可识别 severity。

用法：
  python3 _tools/compile_decision_system.py [KB根目录，默认为脚本上级目录]

如果任何校验失败，脚本返回 exit 1 且不写出 _machine 文件。
"""
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


KB = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADS = os.path.join(KB, "agent-decision-system")
OUT = os.path.join(ADS, "_machine")


@dataclass(frozen=True)
class ModuleSpec:
    src: str
    dst: str
    heading: str
    id_prefix: str
    expected_count: int
    required_fields: Tuple[str, ...]
    allowed_fields: Tuple[str, ...] = ()
    requires_severity: bool = False


CARD_FIELDS = (
    "when_to_use",
    "when_not_to_use",
    "decision_criteria",
    "related_concepts",
    "common_mistakes",
    "recommended_actions",
    "example_reasoning_path",
)

SPECS: Tuple[ModuleSpec, ...] = (
    ModuleSpec(
        src="01_SITUATION-ROUTER.md",
        dst="situations.yaml",
        heading=r"^## (SIT-\d{2}) · (.+)$",
        id_prefix="SIT",
        expected_count=21,
        required_fields=(
            "situation",
            "diagnosis",
            "relevant_laws",
            "recommended_patterns",
            "avoid",
            "evaluation_checklist",
        ),
    ),
    ModuleSpec(
        src="02_PATTERN-CARDS.md",
        dst="patterns.yaml",
        heading=r"^## (PAT-\d{2}) · (.+)$",
        id_prefix="PAT",
        expected_count=20,
        required_fields=CARD_FIELDS,
    ),
    ModuleSpec(
        src="03_ANTIPATTERN-DETECTORS.md",
        dst="antipatterns.yaml",
        heading=r"^## (ANTI-\d{2}) · (.+?)(?:\s*—\s*(.+))?$",
        id_prefix="ANTI",
        expected_count=12,
        required_fields=CARD_FIELDS,
        requires_severity=True,
    ),
    ModuleSpec(
        src="04_LAW-INVARIANTS.md",
        dst="laws.yaml",
        heading=r"^## (LAW-\d{2}) · (.+)$",
        id_prefix="LAW",
        expected_count=13,
        required_fields=("invariant", "implication", "violation", "check", "source_laws"),
    ),
    ModuleSpec(
        src="05_EVAL-CHECKLIST.md",
        dst="eval_checklist.yaml",
        heading=r"^## (Q-\d{2}) · (.+)$",
        id_prefix="Q",
        expected_count=10,
        required_fields=("question", "pass_criteria", "failure_signal", "relevant"),
    ),
)


FIELD_KEY = {
    # Situation router
    "Situation": "situation",
    "Diagnosis": "diagnosis",
    "Relevant Laws": "relevant_laws",
    "Recommended Patterns": "recommended_patterns",
    "Avoid": "avoid",
    "Evaluation Checklist": "evaluation_checklist",
    # Pattern / Anti-pattern cards
    "When to use": "when_to_use",
    "When not to use": "when_not_to_use",
    "Decision criteria": "decision_criteria",
    "Related concepts": "related_concepts",
    "Common mistakes": "common_mistakes",
    "Recommended actions": "recommended_actions",
    "Example reasoning path": "example_reasoning_path",
    # Law invariants
    "INVARIANT": "invariant",
    "IMPLICATION": "implication",
    "VIOLATION": "violation",
    "CHECK": "check",
    "SOURCE": "source_laws",
    # Eval checklist
    "必答": "question",
    "通过判据": "pass_criteria",
    "失败信号": "failure_signal",
    "Relevant": "relevant",
}


FIELD_RE = re.compile(r"^- \*\*(.+?)\*\*[:：]\s*(.*)$")
REF_RE = re.compile(r"\b((?:LAW|PAT|ANTI|SIT|Q)-\d{2})\b")


def strip_links(text: str) -> str:
    """Keep visible link labels in machine output."""
    text = re.sub(r"\[\[([^\]\|]+)\|([^\]]+)\]\]", r"\2", text)
    return re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)


def normalize_field(raw: str) -> str:
    """Map `When to use (何时警惕)` and `Recommended actions (纠正)` to base keys."""
    return re.sub(r"\s*[(（][^)）]*[)）]\s*$", "", raw.strip())


def severity(raw: str) -> str | None:
    if not raw:
        return None
    if "🔴" in raw:
        return "critical"
    if "🟠" in raw:
        return "major"
    if "🟢" in raw:
        return "minor"
    return None


def expected_ids(prefix: str, count: int) -> List[str]:
    return [f"{prefix}-{i:02d}" for i in range(1, count + 1)]


def add_error(errors: List[str], src: str, line_no: int | None, msg: str) -> None:
    loc = f"{src}:{line_no}" if line_no is not None else src
    errors.append(f"{loc} {msg}")


def parse_module(spec: ModuleSpec) -> Tuple[List[Dict[str, object]], List[str]]:
    path = os.path.join(ADS, spec.src)
    errors: List[str] = []
    if not os.path.exists(path):
        return [], [f"{spec.src} 文件不存在"]

    lines = open(path, encoding="utf-8").read().splitlines()
    heading_re = re.compile(spec.heading)
    entries: List[Dict[str, object]] = []
    cur: Dict[str, object] | None = None
    cur_line: int | None = None
    seen_ids: set[str] = set()
    allowed = set(spec.allowed_fields or spec.required_fields)

    for line_no, line in enumerate(lines, 1):
        hm = heading_re.match(line)
        if hm:
            entry_id = hm.group(1)
            title = strip_links(hm.group(2).strip())
            if entry_id in seen_ids:
                add_error(errors, spec.src, line_no, f"重复 ID: {entry_id}")
            seen_ids.add(entry_id)
            cur = {"id": entry_id, "title": title, "_line": line_no}
            cur_line = line_no
            if spec.requires_severity:
                sev = severity(hm.group(3) if hm.lastindex and hm.lastindex >= 3 else "")
                if not sev:
                    add_error(errors, spec.src, line_no, f"{entry_id} 缺少可识别 severity 标记")
                else:
                    cur["severity"] = sev
            entries.append(cur)
            continue

        if cur is None:
            continue

        fm = FIELD_RE.match(line)
        if not fm:
            continue

        raw_name = fm.group(1).strip()
        normalized = normalize_field(raw_name)
        key = FIELD_KEY.get(normalized)
        if key is None:
            add_error(errors, spec.src, line_no, f"{cur['id']} 未知字段名: {raw_name}")
            continue
        if key not in allowed:
            add_error(errors, spec.src, line_no, f"{cur['id']} 字段 {raw_name} 不属于 {spec.id_prefix} schema")
            continue
        if key in cur:
            add_error(errors, spec.src, line_no, f"{cur['id']} 重复字段: {raw_name}")
            continue

        value = strip_links(fm.group(2).strip())
        if not value:
            add_error(errors, spec.src, line_no, f"{cur['id']} 字段 {raw_name} 为空")
            continue

        cur[key] = value
        refs = sorted(set(REF_RE.findall(value)) - {str(cur["id"])})
        if refs:
            cur["refs"] = sorted(set(cur.get("refs", [])) | set(refs))  # type: ignore[arg-type]

    actual_ids = [str(e["id"]) for e in entries]
    expected = expected_ids(spec.id_prefix, spec.expected_count)
    if actual_ids != expected:
        add_error(
            errors,
            spec.src,
            None,
            f"ID 序列不匹配：expected {expected[:3]}...{expected[-3:]}, actual {actual_ids[:3]}...{actual_ids[-3:]}",
        )

    for entry in entries:
        missing = [f for f in spec.required_fields if f not in entry]
        if missing:
            add_error(errors, spec.src, int(entry.get("_line", 0)) or cur_line, f"{entry['id']} 缺字段: {', '.join(missing)}")

    return entries, errors


def write_yaml(spec: ModuleSpec, entries: Iterable[Dict[str, object]]) -> None:
    out_lines = [
        f"# 由 {spec.src} 编译（正典为 md；勿手改本文件，改 md 后重跑 _tools/compile_decision_system.py）",
        f"source: {json.dumps(spec.src, ensure_ascii=False)}",
        "entries:",
    ]
    for entry in entries:
        out_lines.append(f"  - id: {entry['id']}")
        for key, value in entry.items():
            if key in ("id", "_line"):
                continue
            if key == "refs":
                out_lines.append(f"    refs: {json.dumps(value, ensure_ascii=False)}")
            else:
                out_lines.append(f"    {key}: {json.dumps(value, ensure_ascii=False)}")
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, spec.dst), "w", encoding="utf-8").write("\n".join(out_lines) + "\n")


def main() -> int:
    all_entries: Dict[str, List[Dict[str, object]]] = {}
    all_errors: List[str] = []

    for spec in SPECS:
        entries, errors = parse_module(spec)
        all_entries[spec.src] = entries
        all_errors.extend(errors)

    all_ids = {str(entry["id"]) for entries in all_entries.values() for entry in entries}
    dangling: List[str] = []
    for src, entries in all_entries.items():
        for entry in entries:
            for ref in entry.get("refs", []):  # type: ignore[union-attr]
                if ref not in all_ids:
                    dangling.append(f"{src}:{entry['id']} -> {ref}")
    if dangling:
        all_errors.append("悬空引用: " + "; ".join(sorted(dangling)))

    if all_errors:
        print("决策系统编译失败 ❌")
        for err in all_errors:
            print(f"- {err}")
        return 1

    total = 0
    for spec in SPECS:
        entries = all_entries[spec.src]
        write_yaml(spec, entries)
        print(f"{spec.src} → _machine/{spec.dst}: {len(entries)} entries")
        total += len(entries)

    print(f"总条目 {total}；严格校验：OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
