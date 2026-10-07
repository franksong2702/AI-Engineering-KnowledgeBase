#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查当前有效 Markdown 是否重新出现本库已停用的晦涩术语。

历史审计、署名审阅快照和本轮术语账本按精确路径豁免；代码块与行内代码
不参与检查。退出码：0=当前有效文档无违规，1=发现违规或豁免文件缺失。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


TARGET_TERMS = (
    "机器契约",
    "机器版本",
    "机器文件",
    "机器可读",
    "机器消费",
    "机器投影",
    "机器格式",
    "机器版",
    "正典",
)

# 这些文件保留成文时的原话。新增豁免必须先写入术语审计，不能用目录级通配。
ALLOWED_HISTORICAL_FILES = {
    "01_编辑审计.md",  # 前半部是原始审计历史原文；现行说明已改写。
    "_governance/EDITORIAL_CHANGELOG.md",  # 2026-10-07 从编辑审计原文迁出的修复记录与已完成待办。
    "_governance/ads-case/ADS_LAW_SOURCE_MAP_AUDIT.md",
    "_governance/architecture/ARCHITECTURE_REVIEW.md",
    "_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md",
    "_governance/fable5/FABLE5_REVIEW_PROMPT.md",
    "_governance/fable5/FABLE5_总审报告.md",
    "_governance/fable5/FABLE5_架构收束REVIEW.md",
    "_governance/fable5/FABLE5_深读笔记.md",
    "_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT.md",
    "_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT.md",
    "_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT.md",
    "_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT.md",
    "_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT.md",
    "_governance/laws/LAWS_REWRITE_GRAND_PLAN.md",
    "_governance/laws/LAWS_TAXONOMY_REVIEW.md",
    "_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT.md",
    "_governance/laws/LAW_REFERENCE_AUDIT.md",
    "_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md",
    "_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md",
    "_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT.md",
    "_governance/terminology/TERMINOLOGY_TRANSLATION_AUDIT.md",
}

# 固定每个豁免文件当前保留的数量，避免“整文件豁免”掩盖以后新增的用词回退。
EXPECTED_ALLOWED_COUNTS = {
    "01_编辑审计.md": 19,  # 2026-10-07：12 处随修复记录迁至 EDITORIAL_CHANGELOG
    "_governance/EDITORIAL_CHANGELOG.md": 12,
    "_governance/ads-case/ADS_LAW_SOURCE_MAP_AUDIT.md": 6,
    "_governance/architecture/ARCHITECTURE_REVIEW.md": 27,
    "_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md": 5,
    "_governance/fable5/FABLE5_REVIEW_PROMPT.md": 0,
    "_governance/fable5/FABLE5_总审报告.md": 23,
    "_governance/fable5/FABLE5_架构收束REVIEW.md": 49,
    "_governance/fable5/FABLE5_深读笔记.md": 5,
    "_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT.md": 4,
    "_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT.md": 13,
    "_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT.md": 8,
    "_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT.md": 7,
    "_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT.md": 1,
    "_governance/laws/LAWS_REWRITE_GRAND_PLAN.md": 6,
    "_governance/laws/LAWS_TAXONOMY_REVIEW.md": 12,
    "_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT.md": 1,
    "_governance/laws/LAW_REFERENCE_AUDIT.md": 19,
    "_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md": 1,
    "_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md": 1,
    "_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT.md": 1,
    "_governance/terminology/TERMINOLOGY_TRANSLATION_AUDIT.md": 11,
}

TERM_RE = re.compile("|".join(map(re.escape, sorted(TARGET_TERMS, key=len, reverse=True))))
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def markdown_lines_without_code(text: str):
    """逐行返回去掉 fenced code 与行内代码后的文本，并保留原行号。"""
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        yield line_no, INLINE_CODE_RE.sub("", line)


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    allowlist_config_ok = ALLOWED_HISTORICAL_FILES == set(EXPECTED_ALLOWED_COUNTS)
    missing_allowlist = sorted(path for path in ALLOWED_HISTORICAL_FILES if not (root / path).is_file())
    violations: list[str] = []
    allowed_hits = 0
    allowed_hits_by_file = {path: 0 for path in ALLOWED_HISTORICAL_FILES}
    scanned_files = 0

    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        if "_machine" in path.parts or "_tools" in path.parts:
            continue
        scanned_files += 1
        is_allowed = rel in ALLOWED_HISTORICAL_FILES
        for line_no, line in markdown_lines_without_code(path.read_text(encoding="utf-8")):
            for match in TERM_RE.finditer(line):
                if is_allowed:
                    allowed_hits += 1
                    allowed_hits_by_file[rel] += 1
                else:
                    excerpt = line.strip()
                    violations.append(f"{rel}:{line_no}: {match.group(0)} — {excerpt[:120]}")

    print(f"scanned_markdown_files={scanned_files}")
    print(f"allowlisted_files={len(ALLOWED_HISTORICAL_FILES)}")
    print(f"allowlisted_term_occurrences={allowed_hits}")
    print(f"current_document_violations={len(violations)}")

    if not allowlist_config_ok:
        print("❌ 豁免文件清单与预期数量清单不一致。")

    count_mismatches = {
        path: (EXPECTED_ALLOWED_COUNTS.get(path), observed)
        for path, observed in allowed_hits_by_file.items()
        if EXPECTED_ALLOWED_COUNTS.get(path) != observed
    }

    if missing_allowlist:
        print("❌ 豁免清单中的文件不存在：")
        for path in missing_allowlist:
            print(f"- {path}")
    if violations:
        print("❌ 当前有效文档仍有已停用术语：")
        for item in violations:
            print(f"- {item}")

    if count_mismatches:
        print("❌ 历史豁免文件的保留数量发生变化；请先复核，再更新审计与计数：")
        for path, (expected, observed) in sorted(count_mismatches.items()):
            print(f"- {path}: expected={expected}, observed={observed}")

    if not allowlist_config_ok or missing_allowlist or violations or count_mismatches:
        return 1
    print("✅ 当前有效文档术语检查通过；残留只在精确豁免清单内。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
