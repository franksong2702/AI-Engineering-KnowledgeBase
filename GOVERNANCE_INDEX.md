---
type: governance-index
abstraction_layer: 运营机制（治理文件地图）
date: 2026-07-09
updated: 2026-07-10
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
7. [[_governance/GOVERNANCE_REORG_PLAN|Governance Reorg Plan]]：查看本轮治理文件收纳的移动边界与验证要求。

## 2. 不是活任务队列的文件

这些文件可以作为依据，但不要从里面重新开任务队列：

| 文件 | 性质 | 怎么用 |
|---|---|---|
| [[_governance/architecture/ARCHITECTURE_REVIEW\|Architecture Review]] | 全局架构审查 | 用来理解全库书目分层的历史快照（成文于十四本时代），不直接照单改写 |
| [[_governance/laws/LAWS_TAXONOMY_REVIEW\|Laws Taxonomy Review]] | Laws 分类审查 | 用来理解 Law System 的 family / core-law 边界 |
| [[_governance/laws/LAWS_REWRITE_GRAND_PLAN\|Laws Rewrite Grand Plan]] | Laws 改写计划定稿 | 已执行/部分收束的历史计划，不是新队列 |
| [[_governance/laws/LAW_REFERENCE_AUDIT\|Law Reference Audit]] | Law 引用审计 | 查历史判断与候选来源 |
| [[_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE\|Law Reference System Closure]] | Law 引用收束说明 | 判断哪些 Law 引用已经不应重复审 |
| [[_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES\|Remaining Candidates]] | 脚本生成候选表 | 不是待办清单；保留项是终态裁决 |
| [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT\|Law External Reference Audit]] | 外部 citation pilot | 说明试点证据，不代表全量 citation 已完成 |
| [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT\|Core Laws External Reference Audit]] | Core Laws 18 条外部核验 | 查每条 Core Law 的证据强度、过度声称边界和后续建议措辞；不替代 Law 正典 |
| [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT\|Core Laws P0 Rewrite Impact Audit]] | Law 12/86 正典改写影响审计 | 查 P0 正典、主动正文、Constitution 与 ADS 运行时压缩如何完成一致性收束 |
| [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT\|Core Laws P1 Rewrite Impact Audit]] | Core Laws P1 分批改写影响审计 | 查 Law 7、Law 84/95、Law 100 如何按语义耦合分批收窄并同步下游正典 |
| [[_governance/ads-case/ADS_LAW_SOURCE_MAP_AUDIT\|ADS Law Source Map Audit]] | ADS ↔ Laws 来源审计 | 查 invariant 源头关系 |
| [[_governance/ads-case/ADS_CASE_ROUTING_CLOSURE_AUDIT\|ADS Case Routing Closure Audit]] | ADS ↔ Case Library 收束审计 | 查案例直达关系完成情况 |
| [[_governance/ads-case/CASE_LIBRARY_DOUBLE_LAYER_MAINTENANCE_AUDIT\|Case Library Double Layer Audit]] | 案例库双层结构审计 | 查 20 个深度样板的选择逻辑 |
| [[_governance/usage-router/USAGE_ROUTER_DOGFOOD_AUDIT\|Usage Router Dogfood Audit]] | 使用路径验收 | 查任务路由是否真的可用 |
| `_governance/fable5/FABLE5_*.md` | 外部强模型审阅快照 | 可参考，但执行口径必须回到编辑审计与维护手册 |
| [[_governance/content/M3_MULTIMODAL_SCOPE_REVIEW\|M3 Multimodal Scope Review]] | 内容立项审计 | 判断 M3 是否立项、写什么、不写什么 |
| [[_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW\|M6–M8 Scope & v1.0 Readiness Review]] | 内容立项与版本收束审计 | 查 M6/M7 合并边界、M8 快照纪律与 v1.0 就绪标准 |

## 3. 当前活任务入口

唯一活任务入口仍是：[[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|01_编辑审计 · 待办清单]]。

截至 repo baseline，已完成的主线包括：

- Law Reference System 收束；
- ADS ↔ Case Library heading 级直达；
- Case Library 双层维护；
- Usage Router dogfood 小修；
- Laws external reference pilot 与集中 citation 入口；
- private GitHub repo baseline。

当前没有 Phase 1 / v1.0 内容阻塞项。已明确保留的后续边界是：

- M6/M7 只有满足 [[_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW#四、重新立项的机械触发条件|机械触发条件]]才合并立项；
- M8 只做任务型 dated snapshot，不进入正典；
- Laws 剩余 61 条外部核验按季度风险排序，不机械清零；
- `v1.0` Git tag / GitHub Release 仍需独立发布决定。

## 4. 为什么只搬治理文件，不搬正文

顶层治理文件已经按 [[_governance/GOVERNANCE_REORG_PLAN|Governance Reorg Plan]] 收纳到 `_governance/`。本轮只搬审计、计划、强模型 review 快照，不搬正文书籍、ADS、Case Library 和 Laws 正文结构，原因是：

1. 正文目录已经被 Obsidian wikilink、ADS ↔ Case Library 路由、GitHub Actions 共同验证；
2. 正文目录重组会带来大量链接迁移风险，收益不高；
3. 治理文件是“依据/快照”，收纳后顶层更清楚，且不改变知识体系结构。

如果未来还要继续整理，建议只做下面两类小批次：

1. 给 `_governance/` 内文件继续加更细的索引；
2. 做 GitHub 阅读镜像，但不要反向改写 Obsidian 原生链接。

## 5. Repo 协作文件

- `.github/workflows/kb-health-check.yml`：push / PR 自动运行体检。
- `.github/pull_request_template.md`：PR 自检模板。
- [[CONTRIBUTING|Contributing]]：人和 Agent 的协作流程。
- [[AGENTS|Agent 工作规则]]：Agent 操作边界。
- [[REPO_STATUS|Repo 状态]]：private repo 与 baseline 状态。
