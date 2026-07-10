---
type: contributor-guide
abstraction_layer: 运营机制（协作与提交流程）
date: 2026-07-09
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, GitHub, 协作, 维护]
---

# Contributing — AI Engineering Knowledge Base

> 这是 public repo 的协作说明。读知识库从 [总入口](README.md) 开始；维护知识库从 [维护手册](MAINTENANCE.md) 和 [编辑审计](01_编辑审计.md) 开始。

## 1. 先判断改动类型

开工前先把改动归到一类：

| 类型 | 例子 | 默认规则 |
|---|---|---|
| 正文增量 | 扩写某章、补案例、加新书 | 先确认边界，小批量做 |
| 结构修复 | 断链、歧义链接、frontmatter、自描述数字 | 可做，但必须跑体检 |
| 治理文档 | 审计、计划、收束记录 | 可以新增，但不能另开活任务队列 |
| 工具脚本 | `_tools/*.py` | 必须本地验证 |
| ADS / Case Library | 情境路由、案例直达、机器 YAML | 改 Markdown 后按规则编译/检查 |
| 正典层 | Constitution、Laws 定义、ADS invariant / detector | 高风险，先提案再改 |

## 2. 活任务只看一个地方

唯一活任务队列是：[编辑审计 · 待办清单](01_编辑审计.md)。

其他文件，例如 [Architecture Review](_governance/architecture/ARCHITECTURE_REVIEW.md)、[Laws Rewrite Grand Plan](_governance/laws/LAWS_REWRITE_GRAND_PLAN.md)、[Law Reference System Closure](_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md)、[Governance Index](GOVERNANCE_INDEX.md)、`FABLE5_*.md`，都是依据或快照，不是新的任务队列。

## 3. Obsidian 格式不要破坏

- 保留 Wiki-link：`[[note]]`、`[[folder/note|alias]]`、`[[file#heading|alias]]`。
- README、总图、学习路径与使用路径是公共导航页，使用标准相对 Markdown 链接，确保 GitHub 与 Obsidian 双兼容；README 是 frontmatter 例外。
- 其他正文继续使用 Wiki-link；不要为了 GitHub 网页显示，把全库链接批量改成普通 Markdown 链接。
- 不要未经授权大规模移动、重命名、翻译中文文件名。
- 新增顶层 Markdown 文件通常需要 YAML frontmatter 和 `abstraction_layer`，否则体检会失败。

## 4. 必跑验证

普通改动后，在 repo 根目录运行：

```bash
python3 _tools/kb_health_check.py
```

如果改动涉及 `agent-decision-system/` 的正典 Markdown，还要运行：

```bash
python3 _tools/compile_decision_system.py
```

如果改动涉及 `agent-decision-system/` ↔ `ai-engineering-case-library/` 的交叉引用，还要运行：

```bash
python3 _tools/check_ads_case_crossrefs.py
```

如果改动涉及 Laws 引用系统，先审计再决定是否升级：

```bash
python3 _tools/audit_remaining_law_references.py --write --low-sample-limit 0
python3 _tools/upgrade_law_wikilinks.py --list-limit 0
```

## 5. PR / 提交说明必须写清楚

完成报告或 PR 描述必须包含：

```text
验证命令: <原样命令>
返回结果: <exit code / 关键输出行>
证据路径: <日志/文件/报告路径/PR 链接>
```

不要写“应该没问题”；没有跑过就说没有跑。

## 6. GitHub Actions

本 repo 有一个最小 CI：`.github/workflows/kb-health-check.yml`。

它会在 `main` 的 push / pull request 上运行：

```bash
python3 _tools/kb_health_check.py
```

CI 只是结构护栏，不替代主编判断。它能发现断链、歧义、元数据、ADS ↔ Case Library 直达关系等问题；它不能判断一章内容是否写得深、外部 citation 是否充分。

## 7. 高风险区

非明确授权，不要改以下内容的定义：

- [The Constitution of AI Engineering](The-Constitution-of-AI-Engineering.md)
- [The Laws of AI Engineering](laws-of-ai-engineering/00_INDEX.md) 的 Law 定义
- [ADS Antipattern Detectors](agent-decision-system/03_ANTIPATTERN-DETECTORS.md)
- [ADS Law Invariants](agent-decision-system/04_LAW-INVARIANTS.md)

可以修链接、元数据、明显格式问题；不要顺手改正典含义。
