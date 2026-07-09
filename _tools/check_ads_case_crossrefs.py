#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent Decision System ↔ Case Library cross-reference guard.

用法：
  python3 _tools/check_ads_case_crossrefs.py [KB根目录，默认为脚本上级目录]

检查目标：
  1. Case Library 中具体 LAW/PAT/ANTI/Q/SIT ID 不得裸露。
  2. Case Library 中具体 ADS ID 链接必须指向对应 ADS heading，不得退回文件级链接。
  3. 10 个 Case 类别文件都必须有“决策路由入口”，入口中的 SIT 链接必须指向具体 SIT heading。
  4. Situation Router 的 21 个 SIT 都必须有“可直达案例”，案例链接必须指向真实 Case heading。

退出码：0=全部通过，1=有失败项。
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


KB = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
ADS = KB / "agent-decision-system"
CASE = KB / "ai-engineering-case-library"


@dataclass(frozen=True)
class AdsModule:
    prefix: str
    base: str
    file_name: str
    expected_count: int


ADS_MODULES = {
    "SIT": AdsModule("SIT", "agent-decision-system/01_SITUATION-ROUTER", "01_SITUATION-ROUTER.md", 21),
    "PAT": AdsModule("PAT", "agent-decision-system/02_PATTERN-CARDS", "02_PATTERN-CARDS.md", 20),
    "ANTI": AdsModule("ANTI", "agent-decision-system/03_ANTIPATTERN-DETECTORS", "03_ANTIPATTERN-DETECTORS.md", 12),
    "LAW": AdsModule("LAW", "agent-decision-system/04_LAW-INVARIANTS", "04_LAW-INVARIANTS.md", 13),
    "Q": AdsModule("Q", "agent-decision-system/05_EVAL-CHECKLIST", "05_EVAL-CHECKLIST.md", 10),
}

CONCRETE_ID_RE = re.compile(r"\b(SIT|LAW|PAT|ANTI|Q)-\d{2}\b")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^## ((SIT|PAT|ANTI|LAW|Q)-\d{2}) · .+$")
CASE_HEADING_RE = re.compile(r"^## Case \d+ · .+$")


errors: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(KB).as_posix()


def add_error(message: str) -> None:
    errors.append(message)


def say(ok: bool, label: str, detail: str = "") -> None:
    mark = "✅" if ok else "❌"
    print(f"{mark} {label}" + (f" — {detail}" if detail else ""))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_wikilink(inner: str) -> tuple[str, str | None, str | None]:
    """
    Parse [[target#heading|alias]].

    Also accepts table-safe alias separators written as \\|.
    Return (target_without_heading, heading, alias).
    """
    alias_at: int | None = None
    alias_sep_len = 1
    i = 0
    while i < len(inner):
        if inner[i] == "\\" and i + 1 < len(inner) and inner[i + 1] == "|":
            alias_at = i
            alias_sep_len = 2
            break
        if inner[i] == "|":
            alias_at = i
            alias_sep_len = 1
            break
        i += 1

    before_alias = inner if alias_at is None else inner[:alias_at]
    alias = None if alias_at is None else inner[alias_at + alias_sep_len :].strip()

    if "#" in before_alias:
        target, heading = before_alias.split("#", 1)
        return target.strip().rstrip("\\"), heading.strip(), alias
    return before_alias.strip().rstrip("\\"), None, alias


def build_ads_heading_maps() -> tuple[dict[str, str], dict[str, set[str]], dict[str, str]]:
    id_to_heading: dict[str, str] = {}
    headings_by_base: dict[str, set[str]] = {}
    expected_base_by_prefix = {prefix: module.base for prefix, module in ADS_MODULES.items()}

    for prefix, module in ADS_MODULES.items():
        path = ADS / module.file_name
        if not path.exists():
            add_error(f"{module.file_name} 文件不存在")
            headings_by_base[module.base] = set()
            continue

        headings: set[str] = set()
        for line in read(path).splitlines():
            if not line.startswith("## "):
                continue
            heading = line[3:]
            headings.add(heading)
            m = HEADING_RE.match(line)
            if m and m.group(2) == prefix:
                id_to_heading[m.group(1)] = heading
        headings_by_base[module.base] = headings

        ids = sorted(k for k in id_to_heading if k.startswith(f"{prefix}-"))
        if len(ids) != module.expected_count:
            add_error(f"{module.file_name} expected {module.expected_count} {prefix} headings, got {len(ids)}")

    return id_to_heading, headings_by_base, expected_base_by_prefix


def wikilink_spans(text: str) -> list[tuple[int, int]]:
    return [m.span() for m in WIKILINK_RE.finditer(text)]


def inside_spans(index: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= index < end for start, end in spans)


def category_case_files() -> list[Path]:
    return sorted(p for p in CASE.glob("[0-9][0-9]_*.md") if p.name != "00_INDEX.md")


def all_case_library_files() -> list[Path]:
    return sorted(CASE.glob("*.md"))


def check_case_to_ads_heading_links(id_to_heading: dict[str, str], headings_by_base: dict[str, set[str]], expected_base_by_prefix: dict[str, str]) -> int:
    heading_link_count = 0
    file_level: list[str] = []
    wrong_target: list[str] = []
    wrong_heading: list[str] = []
    bare_ids: list[str] = []

    for path in all_case_library_files():
        text = read(path)
        spans = wikilink_spans(text)
        for m in CONCRETE_ID_RE.finditer(text):
            if not inside_spans(m.start(), spans):
                line_no = text.count("\n", 0, m.start()) + 1
                bare_ids.append(f"{rel(path)}:{line_no} {m.group(0)}")

        for m in WIKILINK_RE.finditer(text):
            target, heading, alias = split_wikilink(m.group(1))
            if not alias or not CONCRETE_ID_RE.fullmatch(alias):
                continue

            prefix = alias.split("-", 1)[0]
            expected_base = expected_base_by_prefix[prefix]
            line_no = text.count("\n", 0, m.start()) + 1

            if target != expected_base:
                wrong_target.append(f"{rel(path)}:{line_no} {alias} target={target}, expected={expected_base}")
                continue
            if not heading:
                file_level.append(f"{rel(path)}:{line_no} {alias}")
                continue
            expected_heading = id_to_heading.get(alias)
            if heading != expected_heading or heading not in headings_by_base.get(target, set()):
                wrong_heading.append(f"{rel(path)}:{line_no} {alias} heading={heading}, expected={expected_heading}")
                continue
            heading_link_count += 1

    if bare_ids:
        add_error("裸 ADS ID: " + "; ".join(bare_ids[:10]))
    if file_level:
        add_error("文件级 ADS ID 链接残留: " + "; ".join(file_level[:10]))
    if wrong_target:
        add_error("ADS ID 链接目标文件错误: " + "; ".join(wrong_target[:10]))
    if wrong_heading:
        add_error("ADS ID 链接 heading 错误: " + "; ".join(wrong_heading[:10]))

    say(not bare_ids, f"Case Library 裸 ADS ID（{len(bare_ids)} 处）", "; ".join(bare_ids[:3]))
    say(not file_level, f"Case → ADS 文件级具体 ID 链接残留（{len(file_level)} 处）", "; ".join(file_level[:3]))
    say(not wrong_target, f"Case → ADS 目标文件错误（{len(wrong_target)} 处）", "; ".join(wrong_target[:3]))
    say(not wrong_heading, f"Case → ADS heading 错误（{len(wrong_heading)} 处）", "; ".join(wrong_heading[:3]))
    say(True, f"Case → ADS heading 级具体 ID 链接（{heading_link_count} 处）")
    return heading_link_count


def check_category_route_entries(id_to_heading: dict[str, str]) -> int:
    files = category_case_files()
    route_count = 0
    route_errors: list[str] = []
    sit_link_count = 0

    for path in files:
        text = read(path)
        route_lines = [line for line in text.splitlines() if line.startswith("> 决策路由入口：")]
        if len(route_lines) != 1:
            route_errors.append(f"{rel(path)} route_lines={len(route_lines)}")
            continue
        route_count += 1
        links = WIKILINK_RE.findall(route_lines[0])
        sit_aliases = []
        for inner in links:
            target, heading, alias = split_wikilink(inner)
            if alias and re.fullmatch(r"SIT-\d{2}", alias):
                sit_aliases.append(alias)
                if target != ADS_MODULES["SIT"].base:
                    route_errors.append(f"{rel(path)} {alias} target={target}")
                elif heading != id_to_heading.get(alias):
                    route_errors.append(f"{rel(path)} {alias} heading={heading}, expected={id_to_heading.get(alias)}")
        if not sit_aliases:
            route_errors.append(f"{rel(path)} 无 SIT heading 链接")
        sit_link_count += len(sit_aliases)

    if len(files) != 11:
        route_errors.append(f"Case 类别文件数应为 11，实际 {len(files)}")
    if route_errors:
        add_error("决策路由入口异常: " + "; ".join(route_errors[:10]))

    say(len(files) == 11 and not route_errors and route_count == 11, f"Case 类别决策路由入口（{route_count}/11）", "; ".join(route_errors[:3]))
    say(True, f"类别入口中的 SIT heading 链接（{sit_link_count} 处）")
    return route_count


def build_case_heading_map() -> dict[str, set[str]]:
    case_headings: dict[str, set[str]] = {}
    for path in category_case_files():
        target = rel(path)[:-3]
        case_headings[target] = {line[3:] for line in read(path).splitlines() if CASE_HEADING_RE.match(line)}
    return case_headings


def check_router_to_case_examples() -> int:
    router = ADS / ADS_MODULES["SIT"].file_name
    text = read(router)
    case_headings = build_case_heading_map()

    sections: list[tuple[str, str]] = []
    matches = list(re.finditer(r"^## (SIT-\d{2}) · .+$", text, re.M))
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else text.find("\n---\n\n## 未匹配时的回退", start)
        if end == -1:
            end = len(text)
        sections.append((m.group(1), text[start:end]))

    example_errors: list[str] = []
    example_line_count = 0
    case_link_count = 0

    if len(sections) != ADS_MODULES["SIT"].expected_count:
        example_errors.append(f"SIT section count expected {ADS_MODULES['SIT'].expected_count}, got {len(sections)}")

    for sid, section in sections:
        lines = [line for line in section.splitlines() if line.startswith("> 可直达案例：")]
        if len(lines) != 1:
            example_errors.append(f"{sid} 可直达案例行数={len(lines)}")
            continue
        example_line_count += 1
        links = WIKILINK_RE.findall(lines[0])
        case_links = []
        for inner in links:
            target, heading, alias = split_wikilink(inner)
            if not target.startswith("ai-engineering-case-library/"):
                continue
            case_links.append((target, heading, alias))
            if not heading:
                example_errors.append(f"{sid} {target} 缺 heading")
            elif target not in case_headings:
                example_errors.append(f"{sid} {target} 文件不存在")
            elif heading not in case_headings[target]:
                example_errors.append(f"{sid} {target} heading 不存在: {heading}")
        if not (1 <= len(case_links) <= 3):
            example_errors.append(f"{sid} 案例链接数应为 1–3，实际 {len(case_links)}")
        case_link_count += len(case_links)

    if example_errors:
        add_error("Situation Router 可直达案例异常: " + "; ".join(example_errors[:10]))

    sit_expected = ADS_MODULES["SIT"].expected_count
    say(not example_errors and example_line_count == ADS_MODULES["SIT"].expected_count, f"Situation Router 可直达案例入口（{example_line_count}/{sit_expected}）", "; ".join(example_errors[:3]))
    say(True, f"ADS → Case heading 级案例链接（{case_link_count} 处）")
    return example_line_count


def main() -> int:
    if not ADS.exists() or not CASE.exists():
        print(f"❌ KB 路径不正确: {KB}")
        return 1

    id_to_heading, headings_by_base, expected_base_by_prefix = build_ads_heading_maps()
    say(not errors, "ADS heading 映射构建", "; ".join(errors[:3]))

    heading_link_count = check_case_to_ads_heading_links(id_to_heading, headings_by_base, expected_base_by_prefix)
    route_count = check_category_route_entries(id_to_heading)
    example_count = check_router_to_case_examples()

    print()
    print(f"summary_heading_ads_id_links={heading_link_count}")
    print(f"summary_route_entry_files={route_count}")
    print(f"summary_router_example_entries={example_count}")

    if errors:
        print("\n存在失败项 ❌")
        for err in errors:
            print(f"- {err}")
        return 1

    print("\nADS ↔ Case Library cross-reference 检查通过 ✅")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
