---
type: ads-case-routing-closure-audit
date: 2026-07-08
updated: 2026-07-09
course: ai-engineering-knowledge-base
abstraction_layer: 应用层与操作层之间的闭环审计
status: p1-crossref-guard-implemented
tags: [AI工程, AgentDecisionSystem, CaseLibrary, SituationRouter, 审计]
---

# ADS ↔ Case Library ↔ Situation Router 闭环审计

> 本页记录不触碰 [[human-ai-interaction-design/00_INDEX|Human-AI Interaction Design]] 的并行维护工作：检查并收束 [[ai-engineering-case-library/00_INDEX|Case Library]]、[[agent-decision-system/00_PROTOCOL|Agent Decision System]] 和 [[agent-decision-system/01_SITUATION-ROUTER|Situation Router]] 之间的引用闭环。
>
> 边界：本轮只做类别级路由入口和明确裸 ID 修复；不对 100 个 case 做逐条 `SIT` 语义标注。

> [!note] 执行状态（2026-07-09）
> P0 已完成：10 个 Case 类别文件均已新增“决策路由入口”；[[ai-engineering-case-library/00_INDEX|Case Library Index]] 已提示先用 Situation Router 做处境分诊。
> P1 已完成：[[agent-decision-system/01_SITUATION-ROUTER|Situation Router]] 的 17 个 `SIT` 已补充“可直达案例”；Case Library 中具体 `LAW/PAT/ANTI/Q/SIT` 已升级为对应 ADS heading 级链接。
> 维护护栏已固化为 `_tools/check_ads_case_crossrefs.py`，后续改 ADS ↔ Case Library 链接时必须运行。

## 一句话结论

Case Library 到 ADS 的 `LAW` / `PAT` / `ANTI` / `Q` / `SIT` 已从文件级链接升级为 heading 级一键直达；ADS 到 Case Library 的“可直达案例”也已补齐。现在剩下的不是断链问题，而是是否要把 focused audit 固化成 `_tools` 脚本，以及是否做更重的 per-case `SIT` 标注。
维护护栏也已落为脚本；剩下的只有是否要做更重的 per-case `SIT` 标注或学习路径视图。

## 当前闭环状态

| 闭环方向 | 状态 | 说明 |
|---|---|---|
| Case → ADS LAW/PAT/ANTI/Q/SIT | ✅ heading 级已闭合 | 现有案例引用的具体 ADS ID 都能点击到对应条目 heading；此前唯一裸 `ANTI-09` 已修成链接。 |
| Case → Situation Router | ✅ 类别级已闭合 | 10 个 Case 类别文件均有“决策路由入口”，读者可以从类别直接回到 [[agent-decision-system/01_SITUATION-ROUTER]]。 |
| Situation Router → Case examples | ✅ 已闭合 | [[agent-decision-system/01_SITUATION-ROUTER]] 的 17 个 `SIT` 都已补充“可直达案例”。 |
| ADS ID 有效性 | ✅ 通过 | Case Library 中出现的 ADS ID 都存在于对应 ADS 模块。 |

## 计数快照

| 项目 | 数量 |
|---|---:|
| ADS `SIT` 定义 | 17 |
| ADS `PAT` 定义 | 20 |
| ADS `ANTI` 定义 | 12 |
| ADS `LAW` 定义 | 13 |
| ADS `Q` 定义 | 10 |
| Case 文件数（不含 Index） | 10 |
| Case 数 | 100 |
| 含“决策路由入口”的 Case 类别文件 | 10 |
| Case 中已链接 `SIT` 引用 | 33 |
| Case 中已链接 `LAW` 引用 | 50 |
| Case 中已链接 `PAT` 引用 | 58 |
| Case 中已链接 `ANTI` 引用 | 29 |
| Case 中已链接 `Q` 引用 | 19 |
| Case 中裸 ADS ID | 0 |
| Case 中不存在的 ADS ID | 0 |
| Situation Router 中含“可直达案例”的 `SIT` | 17 |
| Case Library 中 heading 级 ADS ID 链接 | 191 |

## 按文件审计表

| Case 文件 | Cases | 路由入口 | 已链接 SIT | 已链接 LAW | 已链接 PAT | 已链接 ANTI | 已链接 Q | 裸 ID | 路由入口内容 |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| [[ai-engineering-case-library/01_RAG与知识系统]] | 1–10 | ✅ | 3 | 9 | 12 | 7 | 3 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-02 / SIT-10 / SIT-17 |
| [[ai-engineering-case-library/02_Agent架构]] | 11–20 | ✅ | 6 | 12 | 11 | 5 | 1 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-01 / SIT-03 / SIT-04 / SIT-05 / SIT-13 / SIT-15 |
| [[ai-engineering-case-library/03_多Agent系统]] | 21–30 | ✅ | 3 | 7 | 8 | 3 | 1 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-06 / SIT-09 / SIT-14 |
| [[ai-engineering-case-library/04_可靠性与生产]] | 31–40 | ✅ | 3 | 3 | 0 | 3 | 2 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-07 / SIT-13 / SIT-17 |
| [[ai-engineering-case-library/05_评价与质量]] | 41–50 | ✅ | 3 | 3 | 1 | 3 | 9 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-05 / SIT-10 / SIT-16 |
| [[ai-engineering-case-library/06_安全与对抗]] | 51–60 | ✅ | 3 | 6 | 10 | 2 | 0 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-07 / SIT-08 / SIT-17 |
| [[ai-engineering-case-library/07_成本与性能]] | 61–70 | ✅ | 3 | 1 | 4 | 2 | 1 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-01 / SIT-14 / SIT-16 |
| [[ai-engineering-case-library/08_记忆与上下文]] | 71–80 | ✅ | 2 | 3 | 8 | 1 | 0 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-02 / SIT-09 |
| [[ai-engineering-case-library/09_数据与模型定制]] | 81–90 | ✅ | 2 | 2 | 3 | 0 | 0 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-11 / SIT-12 |
| [[ai-engineering-case-library/10_人机与产品决策]] | 91–100 | ✅ | 5 | 4 | 1 | 3 | 2 | 0 | [[agent-decision-system/01_SITUATION-ROUTER]]：SIT-07 / SIT-10 / SIT-14 / SIT-15 / SIT-16 |

## 本轮已做的 P0 小修

- 已修复 [[ai-engineering-case-library/03_多Agent系统]] 中 1 个裸 `ANTI-09`，改为 `[[agent-decision-system/03_ANTIPATTERN-DETECTORS|ANTI-09]]` 的文件级链接。
- 已在 10 个 Case 类别文件开头补充“决策路由入口”。
- 已更新 [[ai-engineering-case-library/00_INDEX]] 的“学习方式”，明确先用 [[agent-decision-system/01_SITUATION-ROUTER|Situation Router]] 做处境分诊。
- 已在 [[agent-decision-system/01_SITUATION-ROUTER|Situation Router]] 的 17 个 `SIT` 下补充“可直达案例”。
- 已将 Case Library 中 191 个具体 ADS ID 链接升级为对应 heading 级一键直达。

## 剩余问题分级

### P0｜已完成

- [x] 在每个 Case 类别文件开头加一个很短的“决策路由入口”块。
- [x] 更新 [[ai-engineering-case-library/00_INDEX]] 的“怎么用这个案例库”：在“自己走一遍决策循环”前加一句“先用 Situation Router 做处境分诊”。

### P1｜已完成主要导航闭环

- [x] 在 [[agent-decision-system/01_SITUATION-ROUTER]] 每个 `SIT` 下补 1–3 个“可读案例”反向入口。
- [x] 将 Case Library 中具体 `LAW/PAT/ANTI/Q/SIT` 链接升级到 ADS heading 级一键直达。
- [x] 把这轮 focused audit 固化成 `_tools/check_ads_case_crossrefs.py`，防止未来再次出现裸 `LAW/PAT/ANTI/Q/SIT` ID 或退回文件级链接。

### P2｜可选增强

1. 对 100 个 case 做 per-case 级别的 `SIT` 标注。  
   这会更精确，但工作量明显更大，而且容易把案例写得太像索引表；建议只在深度版案例先试点。
2. 建一个“学习路径视图”：`SIT → 推荐案例 → 对应 Pattern/Law → Evaluation Q`。

## 不建议做的事

- 不建议继续把泛用模块速查链接强行改成某个具体 heading；本轮只升级具体 `LAW/PAT/ANTI/Q/SIT` ID。
- 不建议把 `SIT` 路由强塞进每个 case 字段；当前只做类别级轻量入口。
- 不建议在 Fable 5 的 [[human-ai-interaction-design/00_INDEX|M5]] 完成前修改 README/总图/全库文件数。

## 审计结论

Case Library 的模块引用、类别级情境入口、Situation Router 的案例反向入口、Case 到 ADS 的 heading 级一键直达、以及防回退脚本都已经闭合。下一步如果继续推进，才考虑更重的 per-case `SIT` 标注或学习路径视图。
