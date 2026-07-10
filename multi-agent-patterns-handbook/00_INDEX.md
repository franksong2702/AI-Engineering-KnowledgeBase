---
type: handbook-index
aliases: [MultiAgent-INDEX]
date: 2026-07-06
abstraction_layer: 方法（会随能力重洗）
course: multi-agent-patterns
tags: [MultiAgent, 架构模式, Agent, 手册索引]
---

# 《Multi-Agent 架构手册》总索引

> 每个模式回答同样十问：为什么存在、适用问题、协作方式、信息传递、终止条件、优点、缺点、Prompt 示例、Workflow 示例、未来改进。
> 姊妹篇：[《从零到 Agent 专家》教材](../textbook-zero-to-agent/00_INDEX.md) 第 8/11 章是本手册的前置。

> [!warning] 读本手册前的强声明（有罪推定原则）
> **本手册教的是"当你确实需要多 Agent 时怎么做对"，不是"鼓励你用多 Agent"。** 多 Agent 应被有罪推定——它必须证明自己的存在合理，否则默认是过度设计（见 [Foundation](../foundation-of-ai-engineering/00_INDEX.md) 的"简单优先"、[Anti-Patterns](../ai-engineering-anti-patterns/00_INDEX.md) 的多 Agent 反模式类）。
> 动手前先过一道检验：**"如果把它压成一个设计良好的单 Agent，会更差吗？"** 答不出多 Agent 具体好在哪（且能用单 Agent 基线对照证明），就别用。真正的正当理由只有三个——上下文隔离、真并行、权限隔离。带着这个怀疑读下面每一个模式。

## 模式地图（按家族分类）

| 家族 | 模式 | 一句话定位 |
|------|------|-----------|
| **结构分解型**（任务怎么拆） | [01_流水线Pipeline](01_流水线Pipeline.md) | 固定阶段串行加工 |
| | [02_MapReduce](02_MapReduce.md) | 同构分片并行 + 聚合 |
| | [03_树状分解Tree](03_树状分解Tree.md) | 异构层层分解，结果向上合并 |
| | [04_递归Recursive](04_递归Recursive.md) | 自相似任务调用自身直到基例 |
| **控制调度型**（谁指挥谁） | [05_Planner-Executor](05_Planner-Executor.md) | 规划与执行分离 |
| | [06_层级Hierarchical](06_层级Hierarchical.md) | 多层管理树 |
| | [07_动态路由DynamicRouting](07_动态路由DynamicRouting.md) | 先分类，再分发给专家 |
| | [08_MixtureOfExperts](08_MixtureOfExperts.md) | 多专家并答，门控融合 |
| **质量对抗型**（怎么保证对） | [09_反思Reflection](09_反思Reflection.md) | 生成-批评-修订循环 |
| | [10_裁判Judge](10_裁判Judge.md) | 独立评审员做质量闸门 |
| | [11_委员会Committee](11_委员会Committee.md) | 多视角审议 + 主席综合（含辩论变体） |
| | [12_投票Voting](12_投票Voting.md) | 独立多答 + 机械聚合 |
| | [13_红蓝对抗RedBlueTeam](13_红蓝对抗RedBlueTeam.md) | 攻击者与防御者的军备循环 |
| **涌现协调型**（无中心协作） | [14_群体Swarm](14_群体Swarm.md) | 简单个体 + 局部规则 → 涌现 |
| | [15_黑板Blackboard](15_黑板Blackboard.md) | 共享工作区，专家机会主义贡献 |

## 选型决策树

```
任务步骤可预知吗？
├── 是 → 数据同构大批量？ → MapReduce
│        阶段固定？ → Pipeline
│        输入类型多样？ → Dynamic Routing
├── 否，但可分解 → 分解方式已知？ → Tree / Recursive
│                   需要动态规划？ → Planner-Executor（超大规模再上 Hierarchical）
└── 核心是"保证质量"而非"完成任务"？
     ├── 有客观判据（测试/规则）→ Reflection（用真实反馈）+ Judge 闸门
     ├── 主观高风险判断 → Committee / Voting（独立性优先）
     └── 安全鲁棒性 → Red/Blue Team
探索型开放问题（罕见）→ Swarm / Blackboard
```

## 五条跨模式定律

1. **上下文隔离是多 Agent 的第一收益**。大多数模式的真实价值不是"分工"而是让每个 Agent 的上下文干净聚焦。同一模型换头衔不会变聪明，换上下文会。
2. **独立性是聚合的前提**。Voting/Committee/MoE 的收益全部来自答案的去相关。同模型同 prompt 跑三次≈同一个错误犯三次。
3. **传结论，不传对话**。Agent 间传结构化工件（schema 化的结论 + 证据 + 置信度），传完整历史 = token 爆炸 + 噪声传染。
4. **终止条件必须显式**。每个循环类模式（Reflection/RedBlue/Swarm）都自带失控风险：最大轮数、收敛判据、预算上限，三选二起步。
5. **成本是一等公民**。多 Agent 的 token 消耗是单 Agent 的 3-15 倍（经验量级，非测量值）。每个模式的采用理由里必须有"质量提升 ÷ 成本倍数"这道除法。

## 组合原则

模式是积木不是选择题，生产系统几乎都是组合体。常见配方：
- Planner-Executor 为骨架 + 每个 Executor 内嵌 Reflection + 出口加 Judge 闸门
- Dynamic Routing 前置分诊 + 各分支是独立 Pipeline
- MapReduce 的 reduce 阶段用 Committee 防止单点综合偏差
- Red/Blue 作为任何系统上线前的外挂检查层

组合的约束：每加一层，可观测性必须跟上（分布式 trace）；两层以上循环嵌套（如 Reflection 套在 Swarm 里）几乎必然失控，慎用。

## 成本与可控性速查

| 模式 | 相对成本 | 可控性 | 成熟度 |
|------|---------|--------|--------|
| Pipeline / Routing | 1-2× | 高 | 生产级 |
| MapReduce / Tree | 2-5× | 高 | 生产级 |
| Planner-Executor / Hierarchical | 3-8× | 中 | 生产级 |
| Reflection / Judge | 2-4× | 中高 | 生产级 |
| Voting / Committee / MoE | 3-10× | 中 | 成熟 |
| Red/Blue | 5-15× | 中 | 成熟（安全域） |
| Swarm / Blackboard | 5-20× | 低 | 实验性 |
