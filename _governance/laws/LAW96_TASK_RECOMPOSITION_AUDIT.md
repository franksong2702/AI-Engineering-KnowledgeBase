---
type: law-rewrite-impact-audit
aliases: [Law96TaskRecompositionAudit, Law 96 任务重组审计]
abstraction_layer: 运营机制（正典改写影响审计）
date: 2026-07-10
course: laws-of-ai-engineering
status: completed-rewritten
scope: Law 96 抽象上移命题的外部依据、边界与下游影响
tags: [AI工程, Laws, Law96, 工作重组, 自动化, 审计]
---

# Law 96 “抽象上移”命题审计

> 本文承接 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|Core Laws P1 影响审计]]。问题不是“AI 会不会改变工作”，而是原命题能否支持“人的工作必然持续上移、执行层最终几乎全部被 AI 接管”。

## 1. 原命题的问题

原 Law 96（当时名为“抽象上移定律”，现见 [[laws-of-ai-engineering/11_演化与元定律#Law 96 — 任务重组定律（Task-Recomposition Law）|Law 96：任务重组定律]]）把三件不同的事压成了一条单向规律：

1. 技术替代一部分既有任务；
2. 技术与人互补，使部分工作重新分配；
3. 新任务、新职业和新的责任边界出现。

由此直接推出“人的工作持续上移”并不成立。真实结果还可能包括岗位消失、任务下沉、技能要求下降、原岗位基本不变、低经验者被增强，或新的协调与监督工作出现。

## 2. 外部依据

| 来源 | 能支持什么 | 不能支持什么 |
|---|---|---|
| [Autor 2015, Why Are There Still So Many Jobs?](https://doi.org/10.1257/jep.29.3.3) | 自动化既会替代劳动，也会与劳动互补，并改变岗位类型和工资结构 | 不能推出所有剩余工作都会向更高抽象层移动 |
| [Acemoglu & Restrepo 2019, Automation and New Tasks](https://doi.org/10.1257/jep.33.2.3) | 自动化存在 displacement effect，新任务存在 reinstatement effect；核心分析单位是任务如何在人与资本之间重新分配 | 不能把技术变化写成单向的“机器接管执行、人类上移判断” |
| [Brynjolfsson, Li & Raymond 2023/2025, Generative AI at Work](https://www.nber.org/papers/w31161) | AI 辅助对不同经验水平员工影响不一，并可能把高技能者的实践扩散给低经验者 | 不能证明高技能者必然上移，也不能把单一客服场景外推到所有职业 |
| [ILO 2025, Generative AI and Jobs: A Refined Global Index](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure) | 应按任务暴露与职业内部差异分析，技术暴露不等于整个岗位立即自动化 | 不能从“任务可由 AI 完成”直接推出岗位消失或统一的抽象上移 |

## 3. 裁决

### 不删除编号，不与 Law 100 合并

- Law 96 讨论**工作和任务如何重新分配**；
- [[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）|Law 100]] 讨论**生成降本后什么可能成为瓶颈**。

两条相关但不重复，保留独立编号更清楚。

### 改名并降硬度

- heading 从“抽象上移定律”改为“任务重组定律”；
- `定律性质` 从“演化规律”改为“演化综合命题”；
- 保留家族级引用，但禁止把它当成人类必然上移的职业预言。

### 新核心命题

> AI 能力与成本变化会重新分配人、模型和传统工具承担的任务；结果可能是替代、增强、重组或新任务产生，方向必须按任务和制度环境实测。

## 4. 下游影响

- [[foundation-of-ai-engineering/03_必须掌握的能力|Foundation 第三章]]：从“人的工作持续上移”改为“任务持续重组，需识别新的瓶颈与能力要求”。
- [[foundation-of-ai-engineering/05_最值得写进教材的知识|Foundation 第五章]]：决策素养的重要性改为条件性判断，不再由必然上移直接推出。
- [[human-ai-collaboration-foundation/09_长期协作关系|Human-AI 长期协作]]：共同演化保留，但不预设人的单向上移。
- [[_governance/laws/LAWS_TAXONOMY_REVIEW|Taxonomy Review]]：历史 B 级裁决保留，只迁移 heading 并增加后续状态说明。

## 5. 停手条件

- [x] 新旧 Law 96 heading 各自满足 1 / 0；
- [x] 主动正文中的“人的工作必然持续上移”“执行层几乎完全被 AI 接管”为 0；
- [x] 外部 citation 进入集中入口，不堆进 Law 正文；
- [x] 全库体检与 `git diff --check` 通过。
