---
type: laws-taxonomy-review
date: 2026-07-08
course: ai-engineering-knowledge-base
abstraction_layer: 图谱层（正典分类审查）
tags: [AI工程, Laws, taxonomy, 正典边界, 架构审查]
---

# Laws Taxonomy Review · 全局正典分类审查

> 本报告承接 [[_governance/architecture/ARCHITECTURE_REVIEW|Architecture Review]]：先从全库架构视角判断 `Laws` 层的职责，再审查 102 条 `Law` 的正典强度与引用策略。
> 本轮只做 taxonomy / 引用权重 / 后续动作建议，不改 [[laws-of-ai-engineering/00_INDEX|Laws]] 正文定义。

> [!note] 执行状态
> Taxonomy 本身已经被落地为 Law System：[[laws-of-ai-engineering/00_INDEX|Laws INDEX]] 已加入引用层级说明，[[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]] 定义全局核心，[[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] 定义引用规则，102 条 Law 已补齐中文 `定律元信息`。本页保留为分类审查依据，不再是“待执行计划”。
>
> 2026-07-10 后续状态：本页表格中的 Law 12“硬规律”、Law 7“分布内可靠”等分类是当时的 taxonomy 快照，不再代表当前证据裁决。Law 12/86 见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|P0 改写影响审计]]；Law 7 现行正典为“分布证据边界定律”，见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 改写影响审计]]。

## 0. Executive Summary

用户的直觉是对的：**《The Laws of AI Engineering》不是说 102 条都要被全库同等引用。**
更合理的架构是：`Laws` 作为全库的约束库，其中只有少数是全局核心 laws；其余是某个领域、某个场景、某个 family 的局部约束、工程原则、通用定律投影或未来判断。

本轮分类后的结论：

1. **S 级全库核心**：少数条目可作为总图、README、Foundation、Evaluation、Decision System 的稳定引用核心。
2. **A 级家族锚点**：只应在相关书/相关 family 的首次定义处引用。
3. **B 级场景引用**：只在具体场景、案例、章节中引用，不应提升为全局正典。
4. `Laws` 里确实混合了 hard law / imported law / engineering principle / heuristic / forecast / meta-law；这不是失败，但必须显式标注。
5. 当前已完成 Laws INDEX / Core Laws / Reference Policy / Metadata Schema 的落地；下一步应按 S/A/B 层级做 Batch 7 引用修复，而不是全库机械补 `见 Law N`。

## 1. 本报告的全局视角

本报告不是从单条 law 的文字质量出发，而是从整个 KB 的架构链条出发：

```text
Root Thesis → Data/Foundation/Laws/Evaluation/Human-AI → Methods → Anti-Patterns → Case Library → Agent Decision System
```

因此，一条 law 的价值不只看它“听起来对不对”，还看它在全库里承担什么职责：

- 它是否支撑根命题？
- 它是否被多个模块反复调用？
- 它是否应该作为全库引用正典？
- 它是否其实只是某个场景的工程原则？
- 它是否会随模型能力变化而重洗？
- 它是否应该由 [[foundation-of-ai-engineering/00_INDEX|Foundation]]、[[evaluation-of-ai-systems/00_INDEX|Evaluation]]、[[human-ai-collaboration-foundation/00_INDEX|Human-AI Collaboration]] 或 [[ai-systems-in-production/00_INDEX|Production]] 承担，而不是由 `Laws` 强行承担？

## 2. Taxonomy 分类定义

| 类型 | 含义 | 处理原则 |
|---|---|---|
| 硬规律 | 信息论、计算理论、概率论、统计学习等较硬约束 | 可作为强正典，但仍需适用边界 |
| 通用定律投影 | 已有通用 law 在 AI 工程中的应用，如 Goodhart、Conway、Murphy | 可引用，但应标明 imported / projected，不当原创 law |
| 工程原则 | 可靠性、安全、软件工程中的强原则 | 有价值，但不要和数学 law 同级 |
| 启发式/经验规律 | 当前工程实践中有用但依赖上下文或模型代际 | 只做场景引用，需定期重估 |
| 预测/演化判断 | 对未来技术演化、工作抽象上移、模式重洗的判断 | 需要证据与边界，不宜过硬正典化 |
| 认识论/元原则 | 关于证据、可证伪、地图非疆域、判断力等的高层原则 | 常是全库最稳定的思维骨架，但需避免口号化 |
| 安全硬约束 | Prompt injection、权限、攻击面等安全底线 | 对 Agent/Production/Tool Use 具有强约束力 |

## 3. 引用层级定义

| 层级 | 含义 | 建议引用方式 |
|---|---|---|
| S | 全库核心 law / meta-law | README、总图、学习路径、Constitution、Decision System 可稳定引用 |
| A | 家族锚点 | 相关书/相关 family 首次定义处引用，不要全库泛化 |
| B | 场景引用 | 只在具体章节、案例、反模式、生产问题中按需引用 |

本轮统计：

| 层级 | 数量 | Law 编号 |
|---|---:|---|
| S | 18 | Law 1, Law 4, Law 6, Law 7, Law 12, Law 14, Law 24, Law 26, Law 62, Law 64, Law 74, Law 84, Law 86, Law 87, Law 94, Law 95, Law 100, Law 102 |
| A | 42 | Law 2, Law 3, Law 5, Law 10, Law 11, Law 13, Law 15, Law 18, Law 21, Law 25, Law 30, Law 33, Law 34, Law 36, Law 37, Law 41, Law 42, Law 46, Law 47, Law 56, Law 60, Law 61, Law 63, Law 65, Law 67, Law 69, Law 70, Law 71, Law 72, Law 75, Law 77, Law 78, Law 79, Law 82, Law 83, Law 88, Law 90, Law 92, Law 93, Law 97, Law 98, Law 99 |
| B | 42 | Law 8, Law 9, Law 16, Law 17, Law 19, Law 20, Law 22, Law 23, Law 27, Law 28, Law 29, Law 31, Law 32, Law 35, Law 38, Law 39, Law 40, Law 43, Law 44, Law 45, Law 48, Law 49, Law 50, Law 51, Law 52, Law 53, Law 54, Law 55, Law 57, Law 58, Law 59, Law 66, Law 68, Law 73, Law 76, Law 80, Law 81, Law 85, Law 89, Law 91, Law 96, Law 101 |

按类型粗分：

| 类型 | 数量 |
|---|---:|
| 通用定律投影 | 23 |
| 工程原则 | 22 |
| 硬规律 | 18 |
| 安全/工程原则 | 5 |
| 经验规律/启发式 | 3 |
| 硬规律投影 | 3 |
| 认识论原则 | 3 |
| 元原则 | 2 |
| 人机协作原则 | 2 |
| 安全硬约束 | 2 |
| 架构原则/启发式 | 1 |
| 硬规律/工程约束 | 1 |
| 硬规律/认识论 | 1 |
| 认识论/工程原则 | 1 |
| 认识论/经验规律 | 1 |
| 认识论/预测 | 1 |
| 工程/决策原则 | 1 |
| 认识论/人机原则 | 1 |
| 人机协作核心规律 | 1 |
| 人机协作启发式 | 1 |
| 伦理/治理原则 | 1 |
| 安全模式规则 | 1 |
| 安全/统计投影 | 1 |
| 预测/统计观察 | 1 |
| 预测/演化判断 | 1 |
| 预测/元规律 | 1 |
| 元认识论 | 1 |
| 工程原则/元判断 | 1 |
| 经济/认识论预测 | 1 |

## 4. S 级：全库核心 laws

这些条目可以被视为全库核心引用层。它们支撑根命题、跨多个模块反复出现，并且直接影响 Agent Decision System 的默认判断。

| Law | 当前名称 | 类型 | 全局角色 | 主要注意事项 |
|---|---|---|---|---|
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] | 有损压缩定律（Lossy Compression Law） | 硬规律 | 事实性幻觉与知识外置的底层根 | 核心引用；与 Law 6 做边界/合并说明 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）\|Law 4]] | 信息守恒定律（No-Information-From-Nothing Law） | 硬规律 | 事实、数据、检索、RAG 的根 | 核心引用 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]] | 压缩必然丢失定律（Compression-Loses Law） | 硬规律 | 摘要、压缩、记忆边界 | 核心引用；与 Law 1 去重/分工 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）\|Law 7]] | 分布内可靠定律（In-Distribution Reliability Law） | 硬规律 | 可委托性与分布外风险的根 | 核心引用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]] | 验证-生成不对称定律（Verification-Generation Asymmetry Law） | 硬规律 | 生成、验证、人机分工的根 | 核心引用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）\|Law 14]] | 误差累积定律（Error Compounding Law） | 硬规律 | Agent/Workflow 分解与纠错的根 | 核心引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24]] | 古德哈特定律（Goodhart's Law） | 通用定律投影 | 评价、对齐、KPI 的核心风险 | 核心引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]] | 校准定律（Calibration Law） | 硬规律 | 置信、信任、评价者校准的根 | 核心引用 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）\|Law 62]] | 流畅度非正确性定律（Fluency-Is-Not-Truth Law） | 认识论原则 | 流畅不等于真 | 核心引用 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）\|Law 64]] | 可证伪性定律（Falsifiability Law） | 元原则 | 可证伪性和审计要求 | 核心引用 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）\|Law 74]] | 不可逆性定律（Irreversibility Law） | 工程/决策原则 | 可逆性决定审慎度 | 核心引用 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84]] | 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law） | 人机协作核心规律 | 信任随能力过涨风险 | 核心引用 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] | 责任不可委托定律（Accountability-Cannot-Be-Delegated Law） | 伦理/治理原则 | 责任主体不能外包 | 核心引用 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）\|Law 87]] | 一切输入皆指令定律（All-Input-Is-Instruction Law） | 安全硬约束 | prompt injection 的根 | 核心引用 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）\|Law 94]] | 权限胜过自觉定律（Permission-Over-Restraint Law） | 安全/工程原则 | 权限硬边界胜过模型自觉 | 核心引用 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）\|Law 95]] | 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law） | 预测/统计观察 | 能力增长不等于可靠增长 | 核心引用但需证据边界 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）\|Law 100]] | 判断力稀缺定律（Judgment-Is-Scarce Law） | 经济/认识论预测 | 判断力成为稀缺资源 | 核心引用 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）\|Law 102]] | 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries） | 元原则 | 所有定律按边界使用 | 核心引用 |

### S 级的含义

S 级不是“永远不能改”，而是：如果全库要补 `见 Law N`，优先只补这些。它们适合出现在：

- [[README|README]]；
- [[00_Knowledge-Graph-总图|知识图谱总图]]；
- [[The-Constitution-of-AI-Engineering|Constitution]]；
- [[foundation-of-ai-engineering/00_INDEX|Foundation]]；
- [[evaluation-of-ai-systems/00_INDEX|Evaluation]]；
- [[agent-decision-system/00_PROTOCOL|Agent Decision System]]。

但即使是 S 级，也仍要遵守 [[laws-of-ai-engineering/11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）|Law 102：定律有边界定律]]。

## 5. 102 条 Law 全量 Taxonomy 表

| Law | 当前名称 | 类型 | 引用层级 | 全局角色 | 建议动作 |
|---|---|---|---|---|---|
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] | 有损压缩定律（Lossy Compression Law） | 硬规律 | S | 事实性幻觉与知识外置的底层根 | 核心引用；与 Law 6 做边界/合并说明 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 2 — 上下文即状态定律（Context-is-State Law）\|Law 2]] | 上下文即状态定律（Context-is-State Law） | 硬规律 | A | Memory、Tool、Agent 状态管理的根 | 相关领域首次引用 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 3 — 信噪比定律（Signal-to-Noise Law）\|Law 3]] | 信噪比定律（Signal-to-Noise Law） | 硬规律 | A | 长上下文与知识库压缩纪律 | 保留为信息家族锚点 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）\|Law 4]] | 信息守恒定律（No-Information-From-Nothing Law） | 硬规律 | S | 事实、数据、检索、RAG 的根 | 核心引用 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 5 — 检索优于记忆定律（Retrieval-Over-Memorization Law）\|Law 5]] | 检索优于记忆定律（Retrieval-Over-Memorization Law） | 架构原则/启发式 | A | RAG 与知识外置的架构选择 | 保留为应用原则，不当硬 law 全局化 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]] | 压缩必然丢失定律（Compression-Loses Law） | 硬规律 | S | 摘要、压缩、记忆边界 | 核心引用；与 Law 1 去重/分工 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）\|Law 7]] | 分布内可靠定律（In-Distribution Reliability Law） | 硬规律 | S | 可委托性与分布外风险的根 | 核心引用 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 8 — 熵反映不确定性定律（Entropy-Reflects-Uncertainty Law）\|Law 8]] | 熵反映不确定性定律（Entropy-Reflects-Uncertainty Law） | 硬规律 | B | 置信与不确定性信号 | 只在概率/熵场景引用 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 9 — 表征决定能力定律（Representation-Determines-Capability Law）\|Law 9]] | 表征决定能力定律（Representation-Determines-Capability Law） | 硬规律 | B | token/表征导致能力边界 | 补边界，不全局化 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 10 — 有效注意力有限定律（Finite-Effective-Attention Law）\|Law 10]] | 有效注意力有限定律（Finite-Effective-Attention Law） | 经验规律/启发式 | A | 长上下文容量治理 | 需随架构变迁重估 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 11 — 语义邻近非相关定律（Semantic-Proximity-Is-Not-Relevance Law）\|Law 11]] | 语义邻近非相关定律（Semantic-Proximity-Is-Not-Relevance Law） | 经验规律/启发式 | A | RAG 检索质量治理 | 保留为 RAG 家族锚点 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]] | 验证-生成不对称定律（Verification-Generation Asymmetry Law） | 硬规律 | S | 生成、验证、人机分工的根 | 核心引用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 13 — 可委托性定律（Delegability Law）\|Law 13]] | 可委托性定律（Delegability Law） | 工程原则 | A | 可委托性判断公式 | 由 Law 12 派生，不当硬定理 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）\|Law 14]] | 误差累积定律（Error Compounding Law） | 硬规律 | S | Agent/Workflow 分解与纠错的根 | 核心引用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 15 — 分解降难定律（Decomposition Law）\|Law 15]] | 分解降难定律（Decomposition Law） | 工程原则 | A | 复杂任务分解到可验证粒度 | 作为方法层桥梁保留 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 16 — 不可预验证定律（Undecidability Law）\|Law 16]] | 不可预验证定律（Undecidability Law） | 硬规律投影 | B | 探索任务无法完全预验证 | 避免滥用停机问题背书 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 17 — 幂等性定律（Idempotency Law）\|Law 17]] | 幂等性定律（Idempotency Law） | 工程原则 | B | 副作用操作的可重试设计 | 生产/工具场景引用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 18 — 确定性优先定律（Determinism-First Law）\|Law 18]] | 确定性优先定律（Determinism-First Law） | 工程原则 | A | 确定性方法优先于模型调用 | 应作为原则引用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 19 — 计算可换质量定律（Compute-Quality Tradeoff Law）\|Law 19]] | 计算可换质量定律（Compute-Quality Tradeoff Law） | 经验规律/启发式 | B | test-time compute 与质量 tradeoff | 需要实测与定期重估 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 20 — 归约定律（Reduction Law）\|Law 20]] | 归约定律（Reduction Law） | 硬规律投影 | B | 把新问题转成熟问题 | 决策/方法场景引用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 21 — 停机与预算定律（Termination-Budget Law）\|Law 21]] | 停机与预算定律（Termination-Budget Law） | 硬规律/工程约束 | A | Agent 循环预算和终止边界 | Agent/Production 家族锚点 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 22 — 没有免费午餐定律（No Free Lunch Law）\|Law 22]] | 没有免费午餐定律（No Free Lunch Law） | 通用定律投影 | B | 选型无万能方法 | 防止过度泛化 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 23 — 偏差-方差定律（Bias-Variance Law）\|Law 23]] | 偏差-方差定律（Bias-Variance Law） | 硬规律 | B | 模型复杂度与稳定性权衡 | ML/评价场景引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24]] | 古德哈特定律（Goodhart's Law） | 通用定律投影 | S | 评价、对齐、KPI 的核心风险 | 核心引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 25 — 分布漂移定律（Distribution Shift Law）\|Law 25]] | 分布漂移定律（Distribution Shift Law） | 硬规律 | A | 生产、数据、评测漂移 | 相关模块首次引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]] | 校准定律（Calibration Law） | 硬规律 | S | 置信、信任、评价者校准的根 | 核心引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 27 — 基率定律（Base Rate Law）\|Law 27]] | 基率定律（Base Rate Law） | 硬规律 | B | 异常、诊断、贝叶斯决策 | 场景引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 28 — 集成去相关定律（Ensemble-Decorrelation Law）\|Law 28]] | 集成去相关定律（Ensemble-Decorrelation Law） | 硬规律 | B | 集成/投票有效性的条件 | Multi-Agent/评价场景引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 29 — 回归均值定律（Regression-to-Mean Law）\|Law 29]] | 回归均值定律（Regression-to-Mean Law） | 通用定律投影 | B | 评测波动与极端样本解释 | 场景引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 30 — 过拟合定律（Overfitting Law）\|Law 30]] | 过拟合定律（Overfitting Law） | 硬规律 | A | benchmark 过拟合与冻结集纪律 | Evaluation/Model Adaptation 锚点 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 31 — 长尾定律（Long-Tail Law）\|Law 31]] | 长尾定律（Long-Tail Law） | 通用定律投影 | B | 长尾输入和风险测试 | Production/Evaluation 场景引用 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 32 — 抽样偏差定律（Sampling-Bias Law）\|Law 32]] | 抽样偏差定律（Sampling-Bias Law） | 硬规律 | B | 数据代表性和选择偏差 | Data/Evaluation 场景引用 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 33 — 瓶颈定律（Bottleneck Law）\|Law 33]] | 瓶颈定律（Bottleneck Law） | 通用定律投影 | A | 系统吞吐与成本瓶颈 | Production 锚点 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 34 — 反馈回路定律（Feedback-Loop Law）\|Law 34]] | 反馈回路定律（Feedback-Loop Law） | 通用定律投影 | A | 反馈系统稳定性 | Production/Data/Evaluation 锚点 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 35 — 延迟致振荡定律（Latency-Oscillation Law）\|Law 35]] | 延迟致振荡定律（Latency-Oscillation Law） | 通用定律投影 | B | 延迟反馈导致振荡 | 控制/生产场景引用 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 36 — 可观测性定律（Observability Law）\|Law 36]] | 可观测性定律（Observability Law） | 工程原则 | A | 可观测性是控制前提 | Production/Evaluation 锚点 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 37 — 单点故障定律（Single-Point-of-Failure Law）\|Law 37]] | 单点故障定律（Single-Point-of-Failure Law） | 工程原则 | A | 关键依赖的可靠性设计 | Production 场景引用 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 38 — 冗余-效率权衡定律（Redundancy-Efficiency Tradeoff Law）\|Law 38]] | 冗余-效率权衡定律（Redundancy-Efficiency Tradeoff Law） | 工程原则 | B | 可靠性与效率权衡 | Production/Cost 场景引用 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 39 — 康威定律（Conway's Law）\|Law 39]] | 康威定律（Conway's Law） | 通用定律投影 | B | 组织/多 Agent 结构映射 | 组织与多体场景引用 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 40 — 二阶效应定律（Second-Order Effects Law）\|Law 40]] | 二阶效应定律（Second-Order Effects Law） | 通用定律投影 | B | 干预的间接后果 | Decision 场景引用 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 41 — 复杂度累积定律（Complexity-Accumulation Law）\|Law 41]] | 复杂度累积定律（Complexity-Accumulation Law） | 工程原则 | A | 复杂度/技术债治理 | Anti-Patterns/Design 锚点 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 42 — 优雅降级定律（Graceful-Degradation Law）\|Law 42]] | 优雅降级定律（Graceful-Degradation Law） | 工程原则 | A | 高可用降级设计 | Production 锚点 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 43 — 接口永存定律（Interface-Permanence Law）\|Law 43]] | 接口永存定律（Interface-Permanence Law） | 工程原则 | B | 接口比实现更持久 | HCI/Production 场景引用 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 44 — 契约显式化定律（Explicit-Contract Law）\|Law 44]] | 契约显式化定律（Explicit-Contract Law） | 工程原则 | B | 组件边界契约 | Workflow/Tool 场景引用 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 45 — 抽象泄漏定律（Leaky-Abstraction Law）\|Law 45]] | 抽象泄漏定律（Leaky-Abstraction Law） | 通用定律投影 | B | 抽象层泄漏风险 | 框架/API 场景引用 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 46 — 边界即安全定律（Boundary-is-Security Law）\|Law 46]] | 边界即安全定律（Boundary-is-Security Law） | 安全/工程原则 | A | 信任边界定义安全 | Security 锚点 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 47 — 最小权限定律（Least-Privilege Law）\|Law 47]] | 最小权限定律（Least-Privilege Law） | 安全/工程原则 | A | 权限设计底线 | Security/Agent 锚点 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 48 — 关注点分离定律（Separation-of-Concerns Law）\|Law 48]] | 关注点分离定律（Separation-of-Concerns Law） | 工程原则 | B | 职责拆分 | Architecture 场景引用 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 49 — 组合性定律（Composability Law）\|Law 49]] | 组合性定律（Composability Law） | 工程原则 | B | 组合性与模块化 | Architecture 场景引用 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 50 — 松耦合定律（Loose-Coupling Law）\|Law 50]] | 松耦合定律（Loose-Coupling Law） | 工程原则 | B | 低耦合 | Architecture 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 51 — 机会成本定律（Opportunity-Cost Law）\|Law 51]] | 机会成本定律（Opportunity-Cost Law） | 通用定律投影 | B | 资源分配和取舍 | Decision 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 52 — 边际定律（Marginal Law）\|Law 52]] | 边际定律（Marginal Law） | 通用定律投影 | B | 边际收益递减 | Cost/Optimization 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 53 — 比较优势定律（Comparative-Advantage Law）\|Law 53]] | 比较优势定律（Comparative-Advantage Law） | 通用定律投影 | B | 人机/模型分工 | Human-AI/Delegation 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 54 — 质量有成本定律（Quality-Costs Law）\|Law 54]] | 质量有成本定律（Quality-Costs Law） | 工程原则 | B | 质量不是免费 | Cost/Production 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 55 — 帕累托定律（Pareto Law）\|Law 55]] | 帕累托定律（Pareto Law） | 通用定律投影 | B | 80/20 聚焦 | Decision 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 56 — 成本结构决定架构定律（Cost-Structure-Shapes-Architecture Law）\|Law 56]] | 成本结构决定架构定律（Cost-Structure-Shapes-Architecture Law） | 工程原则 | A | 成本结构塑造架构 | Production/Model Adaptation 锚点 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 57 — 规模效应定律（Scale-Effects Law）\|Law 57]] | 规模效应定律（Scale-Effects Law） | 通用定律投影 | B | 规模经济与规模不经济 | Production 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 58 — 缓存定律（Caching Law）\|Law 58]] | 缓存定律（Caching Law） | 工程原则 | B | 重复计算缓存 | Cost/Performance 场景引用 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 59 — 沉没成本无关定律（Sunk-Cost-Irrelevance Law）\|Law 59]] | 沉没成本无关定律（Sunk-Cost-Irrelevance Law） | 通用定律投影 | B | 是否继续投入的判断 | Decision 场景引用 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 60 — 证据分级定律（Evidence-Hierarchy Law）\|Law 60]] | 证据分级定律（Evidence-Hierarchy Law） | 认识论原则 | A | 证据层级 | Evaluation/Foundation 锚点 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 61 — 贝叶斯更新定律（Bayesian-Updating Law）\|Law 61]] | 贝叶斯更新定律（Bayesian-Updating Law） | 硬规律/认识论 | A | 信念更新 | Decision/Evaluation 锚点 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）\|Law 62]] | 流畅度非正确性定律（Fluency-Is-Not-Truth Law） | 认识论原则 | S | 流畅不等于真 | 核心引用 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 63 — 不确定性外显定律（Surface-Uncertainty Law）\|Law 63]] | 不确定性外显定律（Surface-Uncertainty Law） | 认识论/工程原则 | A | 不确定性外显 | Evaluation/Human-AI 锚点 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）\|Law 64]] | 可证伪性定律（Falsifiability Law） | 元原则 | S | 可证伪性和审计要求 | 核心引用 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 65 — 地图非疆域定律（Map-Is-Not-Territory Law）\|Law 65]] | 地图非疆域定律（Map-Is-Not-Territory Law） | 通用定律投影 | A | 模型/地图边界 | Foundation 锚点 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 66 — 似然比定律（Likelihood-Ratio Law）\|Law 66]] | 似然比定律（Likelihood-Ratio Law） | 硬规律 | B | 证据诊断价值 | Decision 场景引用 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 67 — 诚实无知定律（Honest-Ignorance Law）\|Law 67]] | 诚实无知定律（Honest-Ignorance Law） | 认识论原则 | A | 诚实无知 | Foundation/Evaluation 锚点 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 68 — 后合理化定律（Post-Hoc-Rationalization Law）\|Law 68]] | 后合理化定律（Post-Hoc-Rationalization Law） | 认识论/经验规律 | B | 解释未必等于真实推理 | CoT/Evaluation 场景引用 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 69 — 知识半衰期定律（Knowledge-Half-Life Law）\|Law 69]] | 知识半衰期定律（Knowledge-Half-Life Law） | 认识论/预测 | A | 知识保值期 | Learning Path/维护策略锚点 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 70 — 墨菲定律（Murphy's Law）\|Law 70]] | 墨菲定律（Murphy's Law） | 通用定律投影 | A | 长期运行必有失败 | Reliability 锚点 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 71 — 显式失败定律（Fail-Loudly Law）\|Law 71]] | 显式失败定律（Fail-Loudly Law） | 工程原则 | A | 失败显式化 | Production/Workflow 锚点 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 72 — 爆炸半径定律（Blast-Radius Law）\|Law 72]] | 爆炸半径定律（Blast-Radius Law） | 工程原则 | A | 限制故障影响面 | Safety/Production 锚点 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 73 — 遍历性定律（Ergodicity Law）\|Law 73]] | 遍历性定律（Ergodicity Law） | 硬规律投影 | B | 避免出局/不可恢复风险 | Decision/Risk 场景引用 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）\|Law 74]] | 不可逆性定律（Irreversibility Law） | 工程/决策原则 | S | 可逆性决定审慎度 | 核心引用 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 75 — 纵深防御定律（Defense-in-Depth Law）\|Law 75]] | 纵深防御定律（Defense-in-Depth Law） | 安全/工程原则 | A | 多层防御 | Security 锚点 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 76 — 静默降级危险定律（Silent-Degradation-Danger Law）\|Law 76]] | 静默降级危险定律（Silent-Degradation-Danger Law） | 工程原则 | B | 静默退化监控 | Production 场景引用 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 77 — 恢复优于预防定律（Recovery-Over-Prevention Law）\|Law 77]] | 恢复优于预防定律（Recovery-Over-Prevention Law） | 工程原则 | A | 恢复能力优先 | Production 锚点 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 78 — 测试即真理定律（Untested-Is-Broken Law）\|Law 78]] | 测试即真理定律（Untested-Is-Broken Law） | 工程原则 | A | 测试/评测作为证据 | Evaluation/Production 锚点 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 79 — 人在回路定律（Human-in-the-Loop Law）\|Law 79]] | 人在回路定律（Human-in-the-Loop Law） | 人机协作原则 | A | HITL 位置设计 | Human-AI 锚点 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 80 — 信任梯度定律（Trust-Gradient Law）\|Law 80]] | 信任梯度定律（Trust-Gradient Law） | 人机协作原则 | B | 风险分层信任 | Human-AI 场景引用 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 81 — 信任即带宽定律（Trust-Is-Bandwidth Law）\|Law 81]] | 信任即带宽定律（Trust-Is-Bandwidth Law） | 通用定律投影 | B | 信任降低协作成本 | Human-AI/Agent Team 场景引用 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 82 — 自动化悖论定律（Automation-Paradox Law）\|Law 82]] | 自动化悖论定律（Automation-Paradox Law） | 通用定律投影 | A | 自动化导致技能/兜底风险 | Human-AI 锚点 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 83 — 意图-指令鸿沟定律（Intent-Instruction-Gap Law）\|Law 83]] | 意图-指令鸿沟定律（Intent-Instruction-Gap Law） | 认识论/人机原则 | A | 意图与指令不等同 | Agent/Human-AI 锚点 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84]] | 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law） | 人机协作核心规律 | S | 信任随能力过涨风险 | 核心引用 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 85 — 可解释性驱动采纳定律（Explainability-Drives-Adoption Law）\|Law 85]] | 可解释性驱动采纳定律（Explainability-Drives-Adoption Law） | 人机协作启发式 | B | 采纳需要可解释 | HCI/高风险系统场景引用 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] | 责任不可委托定律（Accountability-Cannot-Be-Delegated Law） | 伦理/治理原则 | S | 责任主体不能外包 | 核心引用 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）\|Law 87]] | 一切输入皆指令定律（All-Input-Is-Instruction Law） | 安全硬约束 | S | prompt injection 的根 | 核心引用 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 88 — 致命三重奏定律（Lethal-Trifecta Law）\|Law 88]] | 致命三重奏定律（Lethal-Trifecta Law） | 安全模式规则 | A | 数据访问 + 外部动作高危组合 | Security/Agent 锚点 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 89 — 攻防不对称定律（Attack-Defense-Asymmetry Law）\|Law 89]] | 攻防不对称定律（Attack-Defense-Asymmetry Law） | 通用定律投影 | B | 攻防不对称 | Security 场景引用 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 90 — 无可靠转义定律（No-Reliable-Escaping Law）\|Law 90]] | 无可靠转义定律（No-Reliable-Escaping Law） | 安全硬约束 | A | prompt escaping 不可靠 | Security 家族锚点 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 91 — 军备竞赛定律（Arms-Race Law）\|Law 91]] | 军备竞赛定律（Arms-Race Law） | 通用定律投影 | B | 安全对抗持续演化 | Security 场景引用 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 92 — 数据即攻击面定律（Data-Is-Attack-Surface Law）\|Law 92]] | 数据即攻击面定律（Data-Is-Attack-Surface Law） | 安全/工程原则 | A | 数据源也是攻击面 | Data/Security 锚点 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 93 — 对抗性古德哈特定律（Adversarial-Goodhart Law）\|Law 93]] | 对抗性古德哈特定律（Adversarial-Goodhart Law） | 安全/统计投影 | A | 对抗性优化指标 | Security/Evaluation 锚点 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）\|Law 94]] | 权限胜过自觉定律（Permission-Over-Restraint Law） | 安全/工程原则 | S | 权限硬边界胜过模型自觉 | 核心引用 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）\|Law 95]] | 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law） | 预测/统计观察 | S | 能力增长不等于可靠增长 | 核心引用但需证据边界 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 96 — 抽象上移定律（Abstraction-Rises Law）\|Law 96]] | 抽象上移定律（Abstraction-Rises Law） | 预测/演化判断 | B | 人的抽象层上移 | Future/Learning 场景引用 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 97 — 模式重洗定律（Pattern-Reshuffling Law）\|Law 97]] | 模式重洗定律（Pattern-Reshuffling Law） | 预测/元规律 | A | 方法层会重洗 | 维护策略锚点 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 98 — 认识论永恒定律（Epistemology-Endures Law）\|Law 98]] | 认识论永恒定律（Epistemology-Endures Law） | 元认识论 | A | 认识论比技巧持久 | Architecture/Learning 锚点 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 99 — 简单性存活定律（Simplicity-Survives Law）\|Law 99]] | 简单性存活定律（Simplicity-Survives Law） | 工程原则/元判断 | A | 简单性长期存活 | Architecture/Anti-Patterns 锚点 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）\|Law 100]] | 判断力稀缺定律（Judgment-Is-Scarce Law） | 经济/认识论预测 | S | 判断力成为稀缺资源 | 核心引用 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 101 — 涌现不可预测定律（Emergence-Is-Unpredictable Law）\|Law 101]] | 涌现不可预测定律（Emergence-Is-Unpredictable Law） | 通用定律投影 | B | 复杂系统涌现需监控 | Multi-Agent/Swarm 场景引用 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）\|Law 102]] | 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries） | 元原则 | S | 所有定律按边界使用 | 核心引用 |

## 6. 架构级发现

### 6.1 `Law` 这个名字现在承载了过多东西

102 条里有严格规律、通用定律投影、工程原则、启发式、预测和元原则。这个混合本身可接受，因为工程知识天然混合；但如果全部叫 `Law` 且被全库同等引用，就会制造过度正典化。

建议后续在 [[laws-of-ai-engineering/00_INDEX|Laws INDEX]] 里加入一段“引用层级声明”：

```text
本书 102 条并非同一硬度。S 级为全库核心引用，A 级为相关家族锚点，B 级为场景引用。使用时先看层级和适用边界，不要把 B 级原则当全库公理。
```

### 6.2 `Law 1 / Law 6` 是最明显的边界重叠

当前全库已经把“压缩必然有损”写成 `Law 1/6`。这说明两条本身确实重叠：

- Law 1 更像“模型是有损压缩器 → 幻觉是原理”；
- Law 6 更像“摘要/压缩/记忆状态都会丢信息”。

后续不一定要物理合并，但应该明确：Law 1 面向模型事实性输出，Law 6 面向压缩操作和状态摘要。

### 6.3 `Law 84 / Law 95` 需要作为一组而不是互相替代

- Law 84：人的信任涨得比实际可靠性快；
- Law 95：模型能力边界扩张得比前沿能力可靠性更快。

它们不是同一条。Law 95 是模型侧，Law 84 是人机关系侧。全库引用时不要混用。

### 6.4 `Foundation` 与 `Laws` 的边界应当进一步固定

很多工程原则类 law，例如 Determinism First、Least Privilege、Fail Loudly、Graceful Degradation，本质更像 Foundation/Production 的原则。它们仍可保留在 Laws 中，但引用策略应该是 A/B，而不是 S。

### 6.5 `Human-AI Collaboration` 应参与 Laws 的引用策略

信任、责任、HITL、自动化偏见、权限边界等条目，不能只从 Laws 内部看。它们的正典边界需要同时参考 [[human-ai-collaboration-foundation/00_INDEX|Human-AI Collaboration]]、[[evaluation-of-ai-systems/05_人类评价|Evaluation Part 5]] 和 [[agent-decision-system/00_PROTOCOL|Agent Decision System]]。

### 6.6 `Agent Decision System` 不应继承全部 102 条

Agent 运行时需要的是少数高约束 invariant，而不是全部 law。当前 `agent-decision-system/04_LAW-INVARIANTS` 已经压缩成 13 条操作约束，这个方向是对的。后续不要把 102 条全部塞进机器运行时。

## 7. 后续建议 / 执行状态

### Step 1：更新 Laws INDEX 的“引用层级声明” —— ✅ 已完成

[[laws-of-ai-engineering/00_INDEX|Laws INDEX]] 已经从 102 条目录升级为 Law System 总入口，明确 102 条不是同一硬度，并链接到 Core Laws、Relation Graph、Reference Policy 与 Metadata Schema。

### Step 2：基于 S/A/B 重写 [[_governance/laws/LAW_REFERENCE_AUDIT|Law Reference Audit]] 的执行策略 —— ✅ 已完成第一版

当前执行策略以 [[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] 为准：

- S / Core Laws：入口层和核心模块可补；
- A / family anchors：相关 family 或专题首次定义处可补；
- B / contextual laws：只在具体场景保留，不主动补。

### Step 3：给 Laws 正文补结构化 metadata —— ✅ 已完成中文字段版

原计划中的英文 YAML 字段已改为 Obsidian callout 形式的中文字段：

```markdown
> [!metadata] 定律元信息
> - `定律性质`:
> - `引用层级`:
> - `引用范围`:
> - `关系说明`:
```

字段含义见 [[laws-of-ai-engineering/00_METADATA-SCHEMA|定律元信息字段说明]]。全 102 条 Law 已启用健康检查。

### Step 4：全库引用修复 —— ⏭ 下一批 Batch 7

只有在入口层和 Law System 内部关系稳定后，才回到“见 Law N”的正文引用修复。Batch 7 应按 Reference Policy 分层执行，继续禁止全库机械替换。

## 8. 本轮结论

这套 KB 仍然需要 `Laws` 作为中心层，但 `Laws` 的正确定位不是“102 条同等正典”，而是：

```text
少数 S 级核心 laws + 若干 A 级 family anchors + 大量 B 级 contextual laws/principles/heuristics
```

因此，用户的直觉成立：**原本所谓的 Law，并不是说这本书里所有东西都要被引用；真正应该被全库稳定引用的是核心 law。**

当前 taxonomy 已经变成 Law System 的使用说明。下一步最安全的动作是 Batch 7：按 [[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] 做分层引用修复，而不是机械替换。
