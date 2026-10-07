---
type: governance-index
abstraction_layer: 运营机制（治理文件地图）
date: 2026-07-09
updated: 2026-07-12
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, Governance, 审计, 维护]
---

# Governance Index — 治理文件地图

> 本页解释顶层治理文件各自的用途，防止未来维护者把历史审计、强模型 review、计划草案误当成新的活任务队列。

## 1. 当前应该先读什么

如果你是维护者，顺序是：

1. [总入口](README.md)：确认知识库整体结构。
2. [维护手册](MAINTENANCE.md)：确认可改什么、必跑什么验证。
3. [编辑审计](01_编辑审计.md)：唯一活任务队列。
4. [Agent 工作规则](AGENTS.md)：确认 repo / Agent 操作边界。
5. [Contributing](CONTRIBUTING.md)：确认 GitHub 协作与 PR 要求。
6. [Repo 状态](REPO_STATUS.md)：确认 GitHub repo、baseline、tag 与上传边界。
7. [Governance Reorg Plan](_governance/GOVERNANCE_REORG_PLAN.md)：查看本轮治理文件收纳的移动边界与验证要求。
8. [术语翻译审计](_governance/terminology/TERMINOLOGY_TRANSLATION_AUDIT.md)：查看“权威定义、自动生成文件、程序可解析结构”等词分别表示什么，以及哪些历史原文被保留。

> [!note] 历史措辞说明
> 已归档审计与 `_governance/fable5/` 下的署名审阅快照保留成文时的原话，其中可能出现当前正文已经不用的术语。它们记录的是当时的判断，不是当前写作范例；现行文档统一使用更直接的中文说法。

## 2. 不是活任务队列的文件

这些文件可以作为依据，但不要从里面重新开任务队列：

| 文件 | 性质 | 怎么用 |
|---|---|---|
| [Architecture Review](_governance/architecture/ARCHITECTURE_REVIEW.md) | 全局架构审查 | 用来理解全库书目分层的历史快照（成文于十四本时代），不直接照单改写 |
| [Laws Taxonomy Review](_governance/laws/LAWS_TAXONOMY_REVIEW.md) | Laws 分类审查 | 用来理解 Law System 的 family / core-law 边界 |
| [Laws Rewrite Grand Plan](_governance/laws/LAWS_REWRITE_GRAND_PLAN.md) | Laws 改写计划定稿 | 已执行/部分收束的历史计划，不是新队列 |
| [Law Reference Audit](_governance/laws/LAW_REFERENCE_AUDIT.md) | Law 引用审计 | 查历史判断与候选来源 |
| [Law Reference System Closure](_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md) | Law 引用收束说明 | 判断哪些 Law 引用已经不应重复审 |
| [Remaining Candidates](_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md) | 脚本生成候选表 | 不是待办清单；保留项是终态裁决 |
| [Law External Reference Audit](_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT.md) | 外部 citation pilot | 说明试点证据，不代表全量 citation 已完成 |
| [Core Laws External Reference Audit](_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT.md) | Core Laws 18 条外部核验 | 查每条 Core Law 的证据强度、过度声称边界和后续建议措辞；不替代 Law 的正式定义 |
| [Core Laws P0 Rewrite Impact Audit](_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT.md) | Law 12/86 正式定义改写影响审计 | 查 P0 正式定义、主动正文、Constitution 与 ADS 运行时压缩如何完成一致性收束 |
| [Core Laws P1 Rewrite Impact Audit](_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT.md) | Core Laws P1 分批改写影响审计 | 查 Law 7、Law 84/95、Law 100 如何按语义耦合分批收窄并同步下游定义 |
| [ADS Law Source Map Audit](_governance/ads-case/ADS_LAW_SOURCE_MAP_AUDIT.md) | ADS ↔ Laws 来源审计 | 查 invariant 源头关系 |
| [ADS Case Routing Closure Audit](_governance/ads-case/ADS_CASE_ROUTING_CLOSURE_AUDIT.md) | ADS ↔ Case Library 收束审计 | 查案例直达关系完成情况 |
| [Case Library Double Layer Audit](_governance/ads-case/CASE_LIBRARY_DOUBLE_LAYER_MAINTENANCE_AUDIT.md) | 案例库双层结构审计 | 查 20 个深度样板的选择逻辑 |
| [Usage Router Dogfood Audit](_governance/usage-router/USAGE_ROUTER_DOGFOOD_AUDIT.md) | 使用路径验收 | 查任务路由是否真的可用 |
| `_governance/fable5/FABLE5_*.md` | 外部强模型审阅快照 | 可参考，但执行口径必须回到编辑审计与维护手册 |
| [M3 Multimodal Scope Review](_governance/content/M3_MULTIMODAL_SCOPE_REVIEW.md) | 内容立项审计 | 判断 M3 是否立项、写什么、不写什么 |
| [M6–M8 Scope & v1.0 Readiness Review](_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md) | 内容立项与版本收束审计 | 查 M6/M7 合并边界、M8 快照纪律与 v1.0 就绪标准 |
| [Book Expansion Priority Audit](_governance/content/BOOK_EXPANSION_PRIORITY_AUDIT.md) | 十五本书扩写优先级审计 | 判断哪些书值得扩写、先补什么；它是只读建议，不是活任务队列 |
| [编辑修复记录（归档）](_governance/EDITORIAL_CHANGELOG.md) | 2026-07-07 以来的修复记录与已完成待办 | 追溯历史决定；新任务仍只登记在编辑审计 |
| [2026-Q4 方法层季度重估](_governance/reevaluation/REEVALUATION_2026_Q4.md) | 季度重估报告（首轮） | 查 LDP 与 Multi-Agent 手册各模式的 KEEP / BOUNDARY / HISTORY_CANDIDATE / ESCALATE 建议；裁决结果回写编辑审计 |
| [Agent Bible P1-C Scope Audit](_governance/content/AGENT_BIBLE_P1C_SCOPE_AUDIT.md) | Agent Bible 生产运行规则立项审计 | 裁决五项能力运行规则的边界、字段、批次、跨库影响和停手条件；不代表正文已实施 |

## 3. 当前活任务入口

唯一活任务入口仍是：[01_编辑审计 · 待办清单](01_编辑审计.md)。

截至 repo baseline，已完成的主线包括：

- Law Reference System 收束；
- ADS ↔ Case Library heading 级直达；
- Case Library 双层维护；
- Usage Router dogfood 小修；
- Laws external reference pilot 与集中 citation 入口；
- GitHub repo baseline 与 public 发布状态同步。

当前没有 Phase 1 / v1.0 内容阻塞项。已明确保留的后续边界是：

- M6/M7 只有满足 [机械触发条件](_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md)才合并立项；
- M8 只做任务型 dated snapshot，不进入长期维护的核心内容；
- Laws 剩余 61 条外部核验按季度风险排序，不机械清零；
- `v1.0` Git tag / GitHub Release 仍需独立发布决定。

## 4. 为什么只搬治理文件，不搬正文

顶层治理文件已经按 [Governance Reorg Plan](_governance/GOVERNANCE_REORG_PLAN.md) 收纳到 `_governance/`。本轮只搬审计、计划、强模型 review 快照，不搬正文书籍、ADS、Case Library 和 Laws 正文结构，原因是：

1. 正文目录已经被 Obsidian wikilink、ADS ↔ Case Library 路由、GitHub Actions 共同验证；
2. 正文目录重组会带来大量链接迁移风险，收益不高；
3. 治理文件是“依据/快照”，收纳后顶层更清楚，且不改变知识体系结构。

如果未来还要继续整理，建议只做下面两类小批次：

1. 给 `_governance/` 内文件继续加更细的索引；
2. 做 GitHub 阅读镜像，但不要反向改写 Obsidian 原生链接。

## 5. Repo 协作文件

- `.github/workflows/kb-health-check.yml`：push / PR 自动运行体检。
- `.github/pull_request_template.md`：PR 自检模板。
- [Contributing](CONTRIBUTING.md)：人和 Agent 的协作流程。
- [Agent 工作规则](AGENTS.md)：Agent 操作边界。
- [Repo 状态](REPO_STATUS.md)：public repo、baseline 与发布候选状态。
