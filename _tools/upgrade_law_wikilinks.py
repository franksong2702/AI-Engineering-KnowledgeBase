#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
AI Engineering Knowledge Base · Laws wikilink 批量升级脚本

用途：
  把已经明确指向 laws-of-ai-engineering 的 Law wikilink，从文件级链接升级/修正为标题级链接。

默认 dry-run，不写文件：
  python3 _tools/upgrade_law_wikilinks.py

实际写入：
  python3 _tools/upgrade_law_wikilinks.py --apply

原则：
  - 只处理已经是 wikilink 的 Law 引用，不把普通文本 Law N 自动变成链接。
  - 只处理目标属于 laws-of-ai-engineering 的链接，避免误伤 Constitution / Agent Decision System 的编号空间。
  - 可识别 `Law N` alias，也可识别与 Law 中文标题精确匹配的 alias。
  - Law heading 从真实 `## Law N — ...` 标题生成，不手写锚点。
  - 保留原来的 alias 写法；表格里的 `\|` 也保留为 `\|`。
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import os
import re
import sys
from pathlib import Path


EXCLUDE_NAME_PARTS = ("FABLE5",)
LAW_FAMILY_RE = re.compile(r"laws-of-ai-engineering/(?:0[1-9]|1[01])_")
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
LAW_ALIAS_RE = re.compile(r"\bLaw\s*(\d{1,3})\b")
LAW_HEADING_RE = re.compile(r"^Law\s*(\d{1,3})\s+—\s+.+$")

# Explicit high-confidence aliases approved through Batch 7C audit.
# These are not keyword replacements: they only apply when the text is already
# a wikilink pointing at the Laws system/family files.
LAW_SYNONYM_ALIASES = {
    "lost in the middle": 10,
    "验证易于生成": 12,
    "测试集污染": 30,
    "瓶颈决定吞吐": 33,
    "瓶颈误优化": 33,
    "不可观测": 36,
    "无可观测性": 36,
    "复杂度只增不减": 41,
    "复杂度压垮": 41,
    "复杂度压垮系统": 41,
    "流畅非正确": 62,
    "不可逆的": 74,
    "可逆性决定审慎": 74,
    "静默传播": 76,
    "静默失败": 76,
    "静默失败向上传染": 76,
    "静默退化": 76,
    "静默降级": 76,
    "意图非指令": 83,
    "意图非指令鸿沟": 83,
    "信任-可靠性剪刀": 84,
    "剪刀差": 84,

    # Batch 7E contextual aliases: accepted only after manual context review.
    # Keep this list conservative. Do not add broad one-word aliases unless the
    # wording is effectively the Law's canonical concept in current KB usage.
    "信噪比崩溃": 3,
    "相似非相关": 11,
    "幂等重试": 17,
    "计算换质量": 19,
    "停机问题": 21,
    "停机": 21,
    "忽略方差": 23,
    "优化 benchmark 而非真实能力": 24,
    "校准差": 26,
    "置信度应匹配准确率": 26,
    "忽略基率": 27,
    "罕见事件判断错误": 27,
    "过拟合测试集": 30,
    "长尾主导失败": 31,
    "意外/长尾": 31,
    "反馈决定行为": 34,
    "紧耦合": 50,
    "成本核算是设计阶段的事": 56,
    "贝叶斯": 61,
    "暴露不确定性": 63,
    "地图当疆域": 65,
    "诚实的无知": 67,
    "先结论后解释": 68,
    "辩护而非思考": 68,
    "无法恢复": 77,
    "未测试即坏的": 78,
    "带宽": 81,
    "技能退化": 82,
    "用户能力退化": 82,
    "让人退化": 82,
    "一切进入上下文的文本都可能是指令": 87,
    "持久化攻击面": 92,
    "涌现": 101,
}


@dataclasses.dataclass(frozen=True)
class LawEntry:
    n: int
    file: str
    heading: str
    title: str
    kb_rel: str
    vault_rel: str
    base: str


@dataclasses.dataclass
class Change:
    file: str
    line: int
    old: str
    new: str


def split_wikilink_ref(inner: str):
    """Return (target_without_heading, heading, alias, alias_separator)."""
    alias_at = None
    sep = None
    sep_len = 1
    i = 0
    while i < len(inner):
        if inner[i] == "\\" and i + 1 < len(inner) and inner[i + 1] == "|":
            alias_at = i
            sep = "\\|"
            sep_len = 2
            break
        if inner[i] == "|":
            alias_at = i
            sep = "|"
            sep_len = 1
            break
        i += 1

    before_alias = inner if alias_at is None else inner[:alias_at]
    alias = None if alias_at is None else inner[alias_at + sep_len :].strip()
    if "#" in before_alias:
        target_part, heading = before_alias.split("#", 1)
        heading = heading.strip()
    else:
        target_part, heading = before_alias, None
    target = target_part.strip().rstrip("\\")
    return target, heading, alias, sep


def strip_md_ext(path: str) -> str:
    return os.path.splitext(path)[0].replace(os.sep, "/")


def iter_markdown_files(kb: Path):
    for root, dirs, files in os.walk(kb):
        dirs[:] = [d for d in dirs if not d.startswith((".", "_"))]
        for name in files:
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, name), kb).replace(os.sep, "/")
            if any(part in rel for part in EXCLUDE_NAME_PARTS):
                continue
            yield rel


def build_law_index(kb: Path):
    vault = kb.parents[2]
    entries: dict[int, LawEntry] = {}
    target_to_file: dict[str, str] = {}
    family_basenames = set()

    for rel in iter_markdown_files(kb):
        if not LAW_FAMILY_RE.match(rel):
            continue
        path = kb / rel
        text = path.read_text(encoding="utf-8")
        kb_rel = strip_md_ext(rel)
        vault_rel = strip_md_ext(os.path.relpath(path, vault))
        base = Path(rel).stem
        family_basenames.add(base)
        for target in (kb_rel, vault_rel, base):
            target_to_file[target] = rel

        for m in re.finditer(r"^## (Law (\d+) — (.+?)(?:（|\(|$).*)$", text, re.M):
            n = int(m.group(2))
            entries[n] = LawEntry(
                n=n,
                file=rel,
                heading=m.group(1).strip(),
                title=m.group(3).strip(),
                kb_rel=kb_rel,
                vault_rel=vault_rel,
                base=base,
            )

    return entries, target_to_file, family_basenames


def is_laws_target(target: str, target_to_file: dict[str, str], family_basenames: set[str]) -> bool:
    if target in target_to_file:
        return True
    if os.path.basename(target) in family_basenames:
        return True
    return "laws-of-ai-engineering/" in target


def canonical_target(entry: LawEntry, old_target: str, current_file: str) -> str:
    if not old_target and current_file == entry.file:
        return ""
    if old_target.startswith("02_Learn/05_AI_Lessons/AI-Engineering-KnowledgeBase/"):
        return entry.vault_rel
    if old_target and "/" not in old_target:
        return entry.base
    return entry.kb_rel


def build_title_alias_index(entries: dict[int, LawEntry]) -> dict[str, int]:
    candidates: dict[str, set[int]] = collections.defaultdict(set)
    for entry in entries.values():
        aliases = {entry.title}
        if entry.title.endswith("定律"):
            aliases.add(entry.title[:-2])
        for alias in aliases:
            candidates[alias].add(entry.n)
    title_aliases = {alias: next(iter(nums)) for alias, nums in candidates.items() if len(nums) == 1}
    title_aliases.update(LAW_SYNONYM_ALIASES)
    return title_aliases


def law_number_from(alias: str | None, heading: str | None, title_alias_to_law: dict[str, int]) -> int | None:
    if alias:
        m = LAW_ALIAS_RE.search(alias)
        if m:
            return int(m.group(1))
        if alias in title_alias_to_law:
            return title_alias_to_law[alias]
    if heading:
        m = LAW_HEADING_RE.match(heading)
        if m:
            return int(m.group(1))
    return None


def rewrite_link(inner: str, current_file: str, entries: dict[int, LawEntry], target_to_file: dict[str, str], family_basenames: set[str], title_alias_to_law: dict[str, int]):
    target, heading, alias, sep = split_wikilink_ref(inner)
    n = law_number_from(alias, heading, title_alias_to_law)
    if n is None or n not in entries:
        return inner

    entry = entries[n]
    target_is_laws = is_laws_target(target, target_to_file, family_basenames)
    same_file_heading = (not target and current_file == entry.file)
    if not (target_is_laws or same_file_heading):
        return inner

    new_target = canonical_target(entry, target, current_file)
    new_before_alias = f"{new_target}#{entry.heading}" if new_target else f"#{entry.heading}"
    new_sep = sep or "|"
    if alias is None:
        new_inner = new_before_alias
    else:
        new_inner = f"{new_before_alias}{new_sep}{alias}"
    return new_inner


def rewrite_file(rel: str, kb: Path, entries: dict[int, LawEntry], target_to_file: dict[str, str], family_basenames: set[str], title_alias_to_law: dict[str, int]):
    path = kb / rel
    old_text = path.read_text(encoding="utf-8")
    lines = old_text.splitlines(keepends=True)
    new_lines = []
    changes: list[Change] = []
    in_fence = False

    for line_no, line in enumerate(lines, 1):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            new_lines.append(line)
            continue
        if in_fence:
            new_lines.append(line)
            continue

        def repl(match):
            inner = match.group(1)
            new_inner = rewrite_link(inner, rel, entries, target_to_file, family_basenames, title_alias_to_law)
            if new_inner == inner:
                return match.group(0)
            old = match.group(0)
            new = f"[[{new_inner}]]"
            changes.append(Change(rel, line_no, old, new))
            return new

        new_lines.append(LINK_RE.sub(repl, line))

    return old_text, "".join(new_lines), changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Upgrade Laws wikilinks to heading-level links.")
    parser.add_argument("kb", nargs="?", default=str(Path(__file__).resolve().parents[1]), help="KB root directory")
    parser.add_argument("--apply", action="store_true", help="write changes to files; default is dry-run")
    parser.add_argument("--list-limit", type=int, default=80, help="max changes to print")
    args = parser.parse_args()

    kb = Path(args.kb).resolve()
    entries, target_to_file, family_basenames = build_law_index(kb)
    title_alias_to_law = build_title_alias_index(entries)
    missing = [n for n in range(1, 103) if n not in entries]
    if missing or len(entries) != 102:
        print(f"❌ Law heading index invalid: found={len(entries)} missing={missing}", file=sys.stderr)
        return 1

    all_changes: list[Change] = []
    changed_files: dict[str, str] = {}
    for rel in iter_markdown_files(kb):
        old_text, new_text, changes = rewrite_file(rel, kb, entries, target_to_file, family_basenames, title_alias_to_law)
        if changes:
            all_changes.extend(changes)
            changed_files[rel] = new_text

    mode = "apply" if args.apply else "dry-run"
    print(f"mode={mode}")
    print("law_headings=102")
    print(f"changed_files={len(changed_files)}")
    print(f"changed_links={len(all_changes)}")
    if all_changes:
        print("changes_by_file:")
        counts = collections.Counter(change.file for change in all_changes)
        for rel, count in sorted(counts.items()):
            print(f"  {rel}: {count}")

    for change in all_changes[: args.list_limit]:
        print(f"- {change.file}:{change.line}")
        print(f"  old: {change.old}")
        print(f"  new: {change.new}")
    if len(all_changes) > args.list_limit:
        print(f"... omitted {len(all_changes) - args.list_limit} changes; use --list-limit to show more")

    if args.apply:
        for rel, new_text in changed_files.items():
            (kb / rel).write_text(new_text, encoding="utf-8")
        print("write_status=applied")
    else:
        print("write_status=not_applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
