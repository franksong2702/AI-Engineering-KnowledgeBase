#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
AI Engineering Knowledge Base · Laws 剩余文件级引用审计

用途：
  重新生成 `_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md`，列出仍然指向
  Laws 系统、但没有跳到具体 `## Law N — ...` heading 的 wikilink。

默认只打印统计，不写文件：
  python3 _tools/audit_remaining_law_references.py

写入审计文档：
  python3 _tools/audit_remaining_law_references.py --write

原则：
  - 这不是批量替换脚本；只做审计与分组。
  - 高确信度 = `upgrade_law_wikilinks.py` 已能机械识别、理论上应被升级。
  - 中确信度 = 像是在引用某条 Law，但 alias 仍需上下文判断。
  - 低确信度 = 整本书、family、治理页、导航页等，保留文件级链接更合适。
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import datetime as _dt
import os
import re
import sys
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from upgrade_law_wikilinks import (  # noqa: E402
    LINK_RE,
    build_law_index,
    build_title_alias_index,
    iter_markdown_files,
    law_number_from,
    split_wikilink_ref,
    strip_md_ext,
)


GENERATED_AUDIT_REL = "_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md"
EXCLUDE_EXACT_RELS = {
    GENERATED_AUDIT_REL,
    "LAW_REFERENCE_REMAINING_CANDIDATES.md",
    "_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md",
    "LAW_REFERENCE_SYSTEM_CLOSURE.md",
}
EXCLUDE_NAME_PARTS = ("FABLE5",)

LOW_NAV_ALIASES = {
    "Law System",
    "Law System / 约束库",
    "Laws",
    "Laws INDEX",
    "The Laws of AI Engineering",
    "Core Laws",
    "Law Relation Graph",
    "Reference Policy",
    "Metadata Schema",
    "定律元信息字段说明",
    "核心定律清单",
    "引用策略",
    "Laws 总索引",
    "无 alias",
}

REVIEW_HINTS = {
    "无法止损": "可能是 Law 74 不可逆性 / Law 77 恢复优于预防 / Law 72 爆炸半径；需要读具体风险语境。",
    "提示层的约束可被绕过": "可能是 Law 87 一切输入皆指令 / Law 90 无可靠转义 / Law 94 权限胜过自觉。",
    "安全形同虚设": "可能是 Law 75 纵深防御 / Law 94 权限胜过自觉；alias 太宽，保留审阅。",
    "选择困难": "可能是 Law 41 复杂度累积，也可能只是工具设计经验。",
    "3-5 个工具": "更像工具数量经验，不是稳定 Law 标题。",
    "3-5 个起步": "更像工具/指标数量经验，不是稳定 Law 标题。",
    "泄漏": "可能是 Law 45 抽象泄漏，也可能是安全/数据泄漏；alias 太短。",
    "规模不经济": "可能是 Law 57 规模效应 / Law 52 边际定律，需要看是否讨论规模还是边际。",
    "超线性增长": "可能是 Law 57 规模效应 / Law 41 复杂度累积，需要看成本还是复杂度。",
    "上下文腐烂": "可能是 Law 2 上下文即状态 / Law 76 静默降级危险，需看上下文。",
    "记忆污染": "可能是 Law 92 数据即攻击面 / Law 87 一切输入皆指令。",
    "被污染": "可能是 Law 92 数据即攻击面 / Law 87 一切输入皆指令；alias 太宽。",
    "过度设计": "可能是 Law 99 简单性存活 / Law 41 复杂度累积。",
    "不适应变化": "可能是 Law 25 分布漂移 / Law 16 不可预验证；需看上下文。",
    "解释的不忠实": "可能是 Law 68 后合理化 / Law 62 流畅度非正确。",
    "解释不忠实": "可能是 Law 68 后合理化 / Law 62 流畅度非正确。",
    "不忠实的解释": "可能是 Law 68 后合理化 / Law 62 流畅度非正确。",
    "过度工程": "可能是 Law 99 简单性存活 / Law 41 复杂度累积。",
    "确认偏误": "是认识论风险，但当前 Laws 未必有一条直接等价 Law。",
    "浪费": "可能是 Law 52 边际定律 / Law 51 机会成本；alias 太宽。",
    "纯风险": "可能是 Law 74 不可逆性 / Law 72 爆炸半径。",
    "注入指令": "可能是 Law 87 一切输入皆指令 / Law 90 无可靠转义。",
    "prompt injection": "可能是 Law 87 一切输入皆指令 / Law 90 无可靠转义。",
    "诱导无限循环烧钱": "可能是 Law 21 停机与预算 / Law 89 攻防不对称。",
    "资源耗尽攻击": "可能是 Law 21 停机与预算 / Law 89 攻防不对称。",
    "无人把关": "可能是 Law 79 人在回路 / Law 86 责任不可委托。",
    "无韧性": "可能是 Law 77 恢复优于预防 / Law 70 墨菲。",
    "检查点": "可能是 Law 77 恢复优于预防 / Law 79 人在回路。",
    "成本失控": "可能是 Law 56 成本结构决定架构 / Law 21 停机与预算。",
    "回归": "可能是 Law 29 回归均值，也可能只是回归测试语境；需看上下文。",
    "分布不匹配": "可能是 Law 25 分布漂移 / Law 7 分布内可靠。",
    "系统性偏差": "可能是 Law 32 抽样偏差 / Law 23 偏差-方差。",
    "方差小": "可能是 Law 23 偏差-方差定律；也可能只是评价稳定性表述。",
    "方差": "可能是 Law 23 偏差-方差定律；alias 太短。",
    "计算与验证定律（第 12–21 条）": "family 总览链接，通常保留文件级。",
    "信息与压缩定律（第 1–11 条）": "family 总览链接，通常保留文件级。",
    "统计与泛化定律（第 22–32 条）": "family 总览链接，通常保留文件级。",
    "系统与控制定律（第 33–42 条）": "family 总览链接，通常保留文件级。",
    "接口与边界定律（第 43–50 条）": "family 总览链接，通常保留文件级。",
    "经济与资源定律（第 51–59 条）": "family 总览链接，通常保留文件级。",
    "认识论与真理定律（第 60–69 条）": "family 总览链接，通常保留文件级。",
    "可靠性与失败定律（第 70–78 条）": "family 总览链接，通常保留文件级。",
    "人机与信任定律（第 79–86 条）": "family 总览链接，通常保留文件级。",
    "对抗与安全定律（第 87–94 条）": "family 总览链接，通常保留文件级。",
    "演化与元定律（第 95–102 条）": "family 总览链接，通常保留文件级。",
    "分布外": "可能是 Law 25 分布漂移 / Law 7 分布内可靠；需看上下文。",
    "注入": "可能属于对抗 family，但 alias 太短。",
    "系统性盲区": "可能是抽样/评价偏差，也可能只是设计表述。",
    "边际递减": "可能是 Law 52 边际定律；需看具体成本/收益语境。",
    "长尾/边界/对抗": "复合概念，可能跨 Law 31/25/89，不应压成一条。",
    "复杂系统": "family 级概念，不宜自动锚定到单条 Law。",
    "护栏": "可能是控制/安全边界，不宜自动猜。",
    "流畅度": "可能是 Law 62 流畅度非正确，但 alias 太短。",
    "无审批": "可能是 Law 79 人在回路 / Law 86 责任不可委托。",
    "同源裁判": "可能是 Law 28 集成去相关 / Law 24 古德哈特。",
    "prompt injection、越狱、数据泄露": "复合安全主题，可能跨 Law 87/90/92/94。",
    "持续红队": "可能是 Law 75 纵深防御 / Law 89 攻防不对称。",
    "评测": "太泛，不应改成具体 Law。",
    "递归自指": "可能是 Law 34 反馈回路，但需要看是否讨论评价污染。",
    "验证": "可能是 Law 12，但 alias 太泛。",
    "数据处理不等式": "它是外部信息论概念，可支撑 Law 1/4，但不是当前 Laws 的某条标题。",
    "正反馈": "可能是 Law 34 反馈回路；若不是明确反馈控制语境，先保留审阅。",
    "反馈决定行为": "可能是 Law 34 反馈回路；若已在上下文确认，可加入升级白名单。",
    "不可信内容": "可能是 Law 87 一切输入皆指令；也可能只是安全输入治理表述。",
    "把错误进行到底": "可能是 Law 14 误差累积 / Law 76 静默降级。",
}


@dataclasses.dataclass(frozen=True)
class Candidate:
    rel: str
    line: int
    target: str
    heading: str | None
    alias: str | None
    raw: str
    line_text: str


def build_laws_target_index(kb: Path) -> dict[str, str]:
    """Map any common laws target spelling to its KB-relative md path."""
    vault = kb.parents[2]
    out: dict[str, str] = {}
    laws_dir = kb / "laws-of-ai-engineering"
    for path in sorted(laws_dir.glob("*.md")):
        rel = os.path.relpath(path, kb).replace(os.sep, "/")
        kb_rel = strip_md_ext(rel)
        vault_rel = strip_md_ext(os.path.relpath(path, vault))
        base = path.stem
        for target in {rel, kb_rel, vault_rel, base}:
            out[target] = rel
    return out


def is_laws_target(target: str, laws_target_index: dict[str, str]) -> bool:
    if target in laws_target_index:
        return True
    # Only basename-match genuinely short Obsidian links such as
    # [[01_信息与压缩定律]]. Do not treat other books' `.../00_INDEX` as
    # Laws just because Laws also has a `00_INDEX`.
    if "/" not in target and os.path.basename(target) in laws_target_index:
        return True
    return "laws-of-ai-engineering/" in target


def canonical_laws_rel(target: str, laws_target_index: dict[str, str]) -> str | None:
    if target in laws_target_index:
        return laws_target_index[target]
    base = os.path.basename(target)
    if "/" not in target and base in laws_target_index:
        return laws_target_index[base]
    if "laws-of-ai-engineering/" in target:
        # Normalize full vault paths back into KB-relative paths when possible.
        marker = "laws-of-ai-engineering/"
        return marker + target.split(marker, 1)[1].removesuffix(".md") + ".md"
    return None


def iter_audit_markdown_files(kb: Path):
    for rel in iter_markdown_files(kb):
        if rel in EXCLUDE_EXACT_RELS:
            continue
        if any(part in rel for part in EXCLUDE_NAME_PARTS):
            continue
        yield rel


def find_candidates(kb: Path, laws_target_index: dict[str, str]) -> list[Candidate]:
    candidates: list[Candidate] = []
    for rel in iter_audit_markdown_files(kb):
        path = kb / rel
        lines = path.read_text(encoding="utf-8").splitlines()
        in_fence = False
        for line_no, line in enumerate(lines, 1):
            stripped = line.lstrip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in LINK_RE.finditer(line):
                inner = match.group(1)
                target, heading, alias, _sep = split_wikilink_ref(inner)
                if heading:
                    continue
                if not is_laws_target(target, laws_target_index):
                    continue
                candidates.append(
                    Candidate(
                        rel=rel,
                        line=line_no,
                        target=target,
                        heading=heading,
                        alias=alias,
                        raw=match.group(0),
                        line_text=line.strip(),
                    )
                )
    return candidates


def is_file_level_keep(candidate: Candidate, laws_rel: str | None) -> bool:
    alias = candidate.alias or "无 alias"
    target = candidate.target
    basename = Path(laws_rel or target).stem

    if basename.startswith("00_"):
        return True
    if alias in LOW_NAV_ALIASES:
        return True
    if "INDEX" in alias or "Core Laws" in alias or "Policy" in alias:
        return True
    if "（第 " in alias or re.search(r"定律（第\s*\d+–\d+\s*条）", alias):
        return True
    if re.search(r"定律（第\s*\d+[-–]\d+\s*条）", alias):
        return True
    if candidate.rel.startswith("laws-of-ai-engineering/00_METADATA-SCHEMA") and "定律" in alias:
        return True
    return False


def classify_candidates(kb: Path, candidates: list[Candidate]):
    entries, _target_to_file, _family_basenames = build_law_index(kb)
    title_alias_to_law = build_title_alias_index(entries)
    laws_target_index = build_laws_target_index(kb)

    high: list[tuple[Candidate, int]] = []
    medium: list[Candidate] = []
    low: list[Candidate] = []
    for cand in candidates:
        n = law_number_from(cand.alias, cand.heading, title_alias_to_law)
        if n is not None and n in entries:
            high.append((cand, n))
            continue
        laws_rel = canonical_laws_rel(cand.target, laws_target_index)
        if is_file_level_keep(cand, laws_rel):
            low.append(cand)
        else:
            medium.append(cand)
    return high, medium, low


def md_file_link(rel: str) -> str:
    stem = strip_md_ext(rel)
    return f"[[{stem}|{rel}]]"


def display_alias(candidate: Candidate) -> str:
    return candidate.alias or "无 alias"


def group_by_file(items):
    grouped: dict[str, list] = collections.defaultdict(list)
    for item in items:
        cand = item[0] if isinstance(item, tuple) else item
        grouped[cand.rel].append(item)
    return grouped


def render_candidate_line(candidate: Candidate, note: str) -> str:
    alias = display_alias(candidate)
    return (
        f"- {md_file_link(candidate.rel)}:{candidate.line} — "
        f"alias `{alias}`；target `{candidate.target}`；判断：{note}"
    )


def render_markdown(kb: Path, candidates: list[Candidate], high, medium, low, low_sample_limit: int) -> str:
    today = _dt.date.today().isoformat()
    status = "high-confidence-detected" if high else "remaining-medium-and-file-level"
    lines: list[str] = [
        "---",
        "type: law-reference-audit",
        f"date: {today}",
        "course: AI-Engineering-KnowledgeBase",
        "abstraction_layer: 运营机制（引用审计）",
        f"status: {status}",
        "tags: [AI工程, Laws, 引用审计, Obsidian, KnowledgeBase]",
        "---",
        "",
        "# Law Reference Remaining Candidates｜剩余候选审计",
        "",
        "> 本页由 `_tools/audit_remaining_law_references.py` 生成。它只审计“仍停留在文件级的 Laws wikilink”，不负责替换链接。",
        "> 执行归口：本页不是活任务队列；是否处理这些候选，以 [[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|01_编辑审计 · 待办清单]] 为准。",
        "",
        "## 审计口径",
        "",
        "- 扫描范围：AI Engineering Knowledge Base 内 Markdown 文件。",
        "- 排除：代码块内链接、FABLE5 审阅文档、本审计文档自身。",
        "- 只统计：指向 `laws-of-ai-engineering` 或 Laws family / governance 文件、且尚未带 `#Law N — ...` heading 的 wikilink。",
        "- 不处理：普通正文里的 `Law N` 文本，因为那不是显式链接。",
        "",
        "## 当前总结",
        "",
        f"- 剩余无 heading 的 Laws 相关 wikilink：**{len(candidates)}** 个。",
        f"- 高确信度候选：**{len(high)}** 个。含义：`upgrade_law_wikilinks.py` 已能机械识别，应先跑升级脚本处理。",
        f"- 中确信度候选：**{len(medium)}** 个。含义：语义像 Law，但不是正典标题，需要读上下文。",
        f"- 低确信度 / 不建议改：**{len(low)}** 个。含义：多为 Laws INDEX、Core Laws、Reference Policy、family 总览等导航或治理链接。",
        "",
        "## A. 高确信度候选",
        "",
    ]

    if not high:
        lines.extend(
            [
                "当前没有高确信度候选。`upgrade_law_wikilinks.py --list-limit 0` 应显示 `changed_links=0`。",
                "",
            ]
        )
    else:
        for rel, items in sorted(group_by_file(high).items()):
            lines.append(f"### {md_file_link(rel)}（{len(items)} 处）")
            lines.append("")
            for cand, n in items:
                lines.append(render_candidate_line(cand, f"脚本可识别为 Law {n}，应运行升级脚本。"))
            lines.append("")

    lines.extend(
        [
            "## B. 中确信度候选（需要读上下文后决定）",
            "",
            "这些条目不适合无脑改。它们是概念转述、短语、局部说法或跨多个 Law 的场景。文件名可点击，行号保留为定位参考。",
            "",
        ]
    )
    if not medium:
        lines.extend(["当前没有中确信度候选。", ""])
    else:
        for rel, items in sorted(group_by_file(medium).items()):
            lines.append(f"### {md_file_link(rel)}（{len(items)} 处）")
            lines.append("")
            for cand in items:
                alias = display_alias(cand)
                note = REVIEW_HINTS.get(alias, "需要人工读上下文判断可能对应哪条 Law，或保留 family / governance 级引用。")
                lines.append(render_candidate_line(cand, note))
            lines.append("")

    lines.extend(
        [
            "## C. 低确信度 / 不建议改（保留文件级）",
            "",
            "这类多是导航、治理入口、整本书入口或 family 总览；它们保持文件级链接更好。",
            "",
            "### 按 target 统计",
            "",
        ]
    )
    target_counts = collections.Counter(c.target for c in low)
    for target, count in target_counts.most_common():
        lines.append(f"- `{target}`：{count} 处")
    lines.append("")
    lines.append("### 低确信度清单")
    lines.append("")
    shown_low = low if low_sample_limit == 0 else low[:low_sample_limit]
    if not shown_low:
        lines.append("当前没有低确信度文件级链接。")
    else:
        for cand in shown_low:
            lines.append(render_candidate_line(cand, "保留文件级/导航链接"))
        if low_sample_limit and len(low) > low_sample_limit:
            lines.append("")
            lines.append(f"> 仅显示前 {low_sample_limit} 条；完整清单可运行 `python3 _tools/audit_remaining_law_references.py --write --low-sample-limit 0`。")

    lines.extend(
        [
            "",
            "## D. 下一步规则",
            "",
            "1. 若 A 区不为 0，先运行 `python3 _tools/upgrade_law_wikilinks.py --apply`，再重新生成本页。",
            "2. B 区只在上下文能明确指向某条 Law 时处理；处理方式是把 alias 加入升级脚本白名单后批量跑，不要逐个手改。",
            "3. C 区默认保留文件级；除非它其实是在引用某条具体 Law，否则不要为了清零而改。",
            "4. 每轮结束必须跑 `python3 _tools/upgrade_law_wikilinks.py --list-limit 0` 和 `python3 _tools/kb_health_check.py`。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit remaining file-level Laws wikilinks.")
    parser.add_argument("kb", nargs="?", default=str(Path(__file__).resolve().parents[1]), help="KB root directory")
    parser.add_argument("--write", action="store_true", help="write _governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md")
    parser.add_argument("--output", default=GENERATED_AUDIT_REL, help="output Markdown path relative to KB")
    parser.add_argument("--low-sample-limit", type=int, default=80, help="low-confidence rows to list; 0 means all")
    args = parser.parse_args()

    kb = Path(args.kb).resolve()
    laws_target_index = build_laws_target_index(kb)
    candidates = find_candidates(kb, laws_target_index)
    high, medium, low = classify_candidates(kb, candidates)
    markdown = render_markdown(kb, candidates, high, medium, low, args.low_sample_limit)

    print(f"remaining_no_heading_law_links={len(candidates)}")
    print(f"high_confidence={len(high)}")
    print(f"medium_review={len(medium)}")
    print(f"file_level_keep={len(low)}")

    if args.write:
        out = kb / args.output
        out.write_text(markdown, encoding="utf-8")
        print(f"written={os.path.relpath(out, kb).replace(os.sep, '/')}")
    else:
        print("written=not_applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
