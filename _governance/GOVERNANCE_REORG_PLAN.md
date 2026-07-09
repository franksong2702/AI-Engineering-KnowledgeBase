---
type: governance-reorg-plan
abstraction_layer: 运营机制（治理文件搬迁计划）
date: 2026-07-09
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, Governance, Repo, Reorg]
---

# Governance Reorg Plan — 顶层治理文件收纳计划

> 本计划是 Batch A 产物。目标是把顶层审计、计划、强模型 review 快照收纳进 `_governance/`，让 repo 顶层更像“入口层”，同时不移动正文书籍、ADS、Case Library 和 Laws 正文结构。

## 1. 完成标准

完成后必须同时满足：

```text
python3 _tools/kb_health_check.py -> exit 0
GitHub Actions / KB Health Check -> conclusion=success
git status --porcelain=v1 -> 0
```

## 2. 不移动的顶层文件

这些文件保留在 repo 根目录，因为它们是入口、活任务、维护规则或协作规则：

```text
README.md
00_Knowledge-Graph-总图.md
01_编辑审计.md
02_学习路径与未来扩展.md
03_使用路径与任务路由.md
The-Constitution-of-AI-Engineering.md
MAINTENANCE.md
AGENTS.md
CONTRIBUTING.md
GOVERNANCE_INDEX.md
REPO_STATUS.md
```

不移动这些目录：

```text
foundation-of-ai-engineering/
laws-of-ai-engineering/
evaluation-of-ai-systems/
llm-design-patterns/
multi-agent-patterns-handbook/
decision-frameworks-guide/
agent-bible/
ai-engineering-anti-patterns/
textbook-zero-to-agent/
data-foundation-of-ai-systems/
model-adaptation/
human-ai-collaboration-foundation/
ai-systems-in-production/
human-ai-interaction-design/
agent-decision-system/
ai-engineering-case-library/
_tools/
.github/
```

## 3. 要移动的文件

移动到 `_governance/architecture/`：

```text
ARCHITECTURE_REVIEW.md
```

移动到 `_governance/laws/`：

```text
LAWS_TAXONOMY_REVIEW.md
LAWS_REWRITE_GRAND_PLAN.md
LAW_REFERENCE_AUDIT.md
LAW_REFERENCE_REMAINING_CANDIDATES.md
LAW_REFERENCE_SYSTEM_CLOSURE.md
LAW_EXTERNAL_REFERENCE_AUDIT.md
```

移动到 `_governance/ads-case/`：

```text
ADS_CASE_ROUTING_CLOSURE_AUDIT.md
ADS_LAW_SOURCE_MAP_AUDIT.md
CASE_LIBRARY_DOUBLE_LAYER_MAINTENANCE_AUDIT.md
```

移动到 `_governance/usage-router/`：

```text
USAGE_ROUTER_DOGFOOD_AUDIT.md
```

移动到 `_governance/fable5/`：

```text
FABLE5_REVIEW_PROMPT.md
FABLE5_总审报告.md
FABLE5_架构收束REVIEW.md
FABLE5_深读笔记.md
```

本计划执行完成后自身移动到：

```text
_governance/GOVERNANCE_REORG_PLAN.md
```

## 4. 必须同步更新的机制

### 4.1 体检脚本不能跳过 `_governance/`

当前 `_tools/kb_health_check.py` 会跳过所有 `_` 开头目录。如果直接新建 `_governance/`，治理文件会进入体检盲区，而且指向它们的 wikilink 会被判断为断链。

执行时必须改为：

```text
跳过 .git、.github、_tools、__pycache__ 等工具/隐藏目录；
不要跳过 _governance。
```

### 4.2 Law 剩余引用审计脚本输出路径要同步

`_tools/audit_remaining_law_references.py` 当前默认输出：

```text
LAW_REFERENCE_REMAINING_CANDIDATES.md
```

移动后必须同步为：

```text
_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md
```

否则下次运行 `--write` 会在顶层重新生成旧文件。

### 4.3 批量更新 wikilink

所有指向被移动文件的 wikilink 必须更新到新路径，例如：

```text
[[_governance/architecture/ARCHITECTURE_REVIEW|Architecture Review]]
```

改为：

```text
[[_governance/architecture/ARCHITECTURE_REVIEW|Architecture Review]]
```

表格里的 wikilink alias pipe 必须继续写成 `\|`，不能把表格结构打坏。

## 5. 执行顺序

1. 新建 `_governance/` 子目录。
2. `git mv` 上述治理文件到目标目录。
3. 移动本计划到 `_governance/GOVERNANCE_REORG_PLAN.md`。
4. 更新 `_tools/kb_health_check.py`，让 `_governance/` 进入体检范围。
5. 更新 `_tools/audit_remaining_law_references.py` 的默认输出路径与排除路径。
6. 批量更新所有 Markdown wikilink。
7. 更新 [[GOVERNANCE_INDEX|治理文件地图]]、[[README|总入口]]、[[REPO_STATUS|Repo 状态]] 的说明。
8. 更新 README / 总图的文件数自描述。
9. 本地跑体检。
10. 在 `/tmp` 非 Obsidian 路径模拟 GitHub repo 根目录跑体检。
11. commit、push、等待 GitHub Actions。

## 6. 自审结论

本计划可以执行，前提是两个风险点都必须落实：

- `_governance/` 不能成为体检盲区；
- `_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md` 的生成路径不能留在顶层。

如果这两点没有同时解决，应停止在 Batch A，不进入 Batch B。
