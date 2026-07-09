---
type: governance-index
abstraction_layer: 运营机制（治理文件地图）
date: 2026-07-09
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, Governance, 审计, 维护]
---

# Governance Index — 治理文件地图

> 本页解释顶层治理文件各自的用途，防止未来维护者把历史审计、强模型 review、计划草案误当成新的活任务队列。

## 1. 当前应该先读什么

如果你是维护者，顺序是：

1. [[README|总入口]]：确认知识库整体结构。
2. [[MAINTENANCE|维护手册]]：确认可改什么、必跑什么验证。
3. [[01_编辑审计|编辑审计]]：唯一活任务队列。
4. [[AGENTS|Agent 工作规则]]：确认 repo / Agent 操作边界。
5. [[CONTRIBUTING|Contributing]]：确认 GitHub 协作与 PR 要求。
6. [[REPO_STATUS|Repo 状态]]：确认 GitHub repo、baseline、tag 与上传边界。

## 2. 不是活任务队列的文件

这些文件可以作为依据，但不要从里面重新开任务队列：

| 文件 | 性质 | 怎么用 |
|---|---|---|
| [[ARCHITECTURE_REVIEW\|Architecture Review]] | 全局架构审查 | 用来理解十四本书的分层，不直接照单改写 |
| [[LAWS_TAXONOMY_REVIEW\|Laws Taxonomy Review]] | Laws 分类审查 | 用来理解 Law System 的 family / core-law 边界 |
| [[LAWS_REWRITE_GRAND_PLAN\|Laws Rewrite Grand Plan]] | Laws 改写计划定稿 | 已执行/部分收束的历史计划，不是新队列 |
| [[LAW_REFERENCE_AUDIT\|Law Reference Audit]] | Law 引用审计 | 查历史判断与候选来源 |
| [[LAW_REFERENCE_SYSTEM_CLOSURE\|Law Reference System Closure]] | Law 引用收束说明 | 判断哪些 Law 引用已经不应重复审 |
| [[LAW_REFERENCE_REMAINING_CANDIDATES\|Remaining Candidates]] | 脚本生成候选表 | 不是待办清单；保留项是终态裁决 |
| [[LAW_EXTERNAL_REFERENCE_AUDIT\|Law External Reference Audit]] | 外部 citation pilot | 说明试点证据，不代表全量 citation 已完成 |
| [[ADS_LAW_SOURCE_MAP_AUDIT\|ADS Law Source Map Audit]] | ADS ↔ Laws 来源审计 | 查 invariant 源头关系 |
| [[ADS_CASE_ROUTING_CLOSURE_AUDIT\|ADS Case Routing Closure Audit]] | ADS ↔ Case Library 收束审计 | 查案例直达关系完成情况 |
| [[CASE_LIBRARY_DOUBLE_LAYER_MAINTENANCE_AUDIT\|Case Library Double Layer Audit]] | 案例库双层结构审计 | 查 20 个深度样板的选择逻辑 |
| [[USAGE_ROUTER_DOGFOOD_AUDIT\|Usage Router Dogfood Audit]] | 使用路径验收 | 查任务路由是否真的可用 |
| `FABLE5_*.md` | 外部强模型审阅快照 | 可参考，但执行口径必须回到编辑审计与维护手册 |

## 3. 当前活任务入口

唯一活任务入口仍是：[[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|01_编辑审计 · 待办清单]]。

截至 repo baseline，已完成的主线包括：

- Law Reference System 收束；
- ADS ↔ Case Library heading 级直达；
- Case Library 双层维护；
- Usage Router dogfood 小修；
- Laws external reference pilot 与集中 citation 入口；
- private GitHub repo baseline。

仍可做但不是 Phase 1 阻塞项：

- M3《Multimodal Systems》新书；
- M6–M8 治理深化 / 组织采纳 / 工具快照附录；
- Laws 102 条外部 citation 全量核验。

## 4. 为什么暂时不搬治理文件

顶层治理文件确实多，但首次 repo 化后先不移动它们，原因是：

1. 这些文件被 README、维护手册、审计文件互相引用；
2. 移动会引发一轮链接迁移风险；
3. 当前更需要稳定 baseline，而不是追求顶层“看起来干净”。

如果未来要整理，建议单独做一个小批次：

1. 新建 `_governance/`；
2. 只移动审计快照，不移动 README / MAINTENANCE / 01_编辑审计 / 03_使用路径；
3. 批量更新 wikilink；
4. 运行 `python3 _tools/kb_health_check.py`；
5. 单独 commit。

## 5. Repo 协作文件

- `.github/workflows/kb-health-check.yml`：push / PR 自动运行体检。
- `.github/pull_request_template.md`：PR 自检模板。
- [[CONTRIBUTING|Contributing]]：人和 Agent 的协作流程。
- [[AGENTS|Agent 工作规则]]：Agent 操作边界。
- [[REPO_STATUS|Repo 状态]]：private repo 与 baseline 状态。
