---
type: law-relation-graph
date: 2026-07-08
course: laws-of-ai-engineering
abstraction_layer: 规律（关系图谱）
stability: 高（关系层，需随 taxonomy 维护）
tags: [AI工程, Laws, 关系图, 父子关系, corollary]
---

# Law Relation Graph｜Law 关系图

> 本页回答一个问题：102 条 Law 之间哪些是父子、派生、成组、边界重叠，哪些不应该被合并？

相关入口：[[laws-of-ai-engineering/00_INDEX|Laws INDEX]] · [[00_CORE-LAWS|Core Laws]] · [[00_REFERENCE-POLICY|Reference Policy]] · [[_governance/laws/LAWS_TAXONOMY_REVIEW|Laws Taxonomy Review]]

## 关系图的作用

如果只看 102 条目录，本书会显得“平铺”：每条 Law 好像同等独立、同等硬度、同等适合作为全库引用。

这个页面把它改成关系视图：

- **父子 / 派生**：后者是前者在工程场景中的操作化表达；
- **成组 / 互补**：几条 Law 共同解释一个问题，但不能互相替代；
- **边界重叠**：两条 Law 看起来相似，需要明确分工；
- **不可合并**：名称接近，但解释层次不同，强行合并会损失信息。

## 父子 / 派生关系

| 父 Law | 派生 / 子 Law | 关系说明 |
|---|---|---|
| [[01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1：有损压缩定律]] | [[01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6：压缩必然丢失定律]] | Law 1 偏模型表征与事实性输出；Law 6 偏摘要、记忆、状态压缩 |
| [[02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12：验证-生成不对称定律]] | [[02_计算与验证定律#Law 13 — 可委托性定律（Delegability Law）\|Law 13：可委托性定律]] | 先确认有可靠验证器，再把验证成本、错误成本、委托开销和可逆性转成可委托性判断 |
| [[03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24：古德哈特定律]] | [[10_对抗与安全定律#Law 93 — 对抗性古德哈特定律（Adversarial-Goodhart Law）\|Law 93：对抗性古德哈特定律]] | Law 93 是安全/博弈场景下的古德哈特变体 |
| [[05_接口与边界定律#Law 47 — 最小权限定律（Least-Privilege Law）\|Law 47：最小权限定律]] | [[10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）\|Law 94：权限胜过自觉定律]] | Law 94 是 AI 工具权限场景下对最小权限原则的强化 |
| [[07_认识论与真理定律#Law 69 — 知识半衰期定律（Knowledge-Half-Life Law）\|Law 69：知识半衰期定律]] | [[11_演化与元定律#Law 97 — 模式重洗定律（Pattern-Reshuffling Law）\|Law 97：模式重洗定律]] / [[11_演化与元定律#Law 98 — 认识论永恒定律（Epistemology-Endures Law）\|Law 98：认识论永恒定律]] | Law 97 说明具体模式会随模型能力重洗，Law 98 说明越靠近认识论的规律越持久，二者都是知识半衰期在 AI 工程中的展开 |
| [[04_系统与控制定律#Law 41 — 复杂度累积定律（Complexity-Accumulation Law）\|Law 41：复杂度累积定律]] | [[11_演化与元定律#Law 99 — 简单性存活定律（Simplicity-Survives Law）\|Law 99：简单性存活定律]] | 简单性是抵抗复杂度债务的长期策略；这是一组张力关系，不是删除或重编号关系 |
| [[10_对抗与安全定律#Law 89 — 攻防不对称定律（Attack-Defense-Asymmetry Law）\|Law 89：攻防不对称定律]] | [[10_对抗与安全定律#Law 91 — 军备竞赛定律（Arms-Race Law）\|Law 91：军备竞赛定律]] | 军备竞赛是攻防不对称在时间维度上的长期动态形态 |

## 成组但不合并

| 关系组 | 成员 | 为什么成组 | 为什么不合并 |
|---|---|---|---|
| 分布与可靠性 | [[01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）\|Law 7]] + [[03_统计与泛化定律#Law 25 — 分布漂移定律（Distribution Shift Law）\|Law 25]] | 都在讨论可靠性证据的分布条件 | Law 7 说明证据不能自动跨分布外推，Law 25 说明部署分布会随时间变化 |
| 校准与不确定性 | [[03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26：校准定律]] + [[07_认识论与真理定律#Law 63 — 不确定性外显定律（Surface-Uncertainty Law）\|Law 63：不确定性外显定律]] + [[01_信息与压缩定律#Law 8 — 熵反映不确定性定律（Entropy-Reflects-Uncertainty Law）\|Law 8：熵反映不确定性定律]] | 都涉及置信、不确定性和未知的表达 | 校准、熵、不确定性外显不是同一个概念 |
| 系统稳定性 | [[04_系统与控制定律#Law 36 — 可观测性定律（Observability Law）\|Law 36：可观测性定律]] + [[08_可靠性与失败定律#Law 71 — 显式失败定律（Fail-Loudly Law）\|Law 71：显式失败定律]] + [[08_可靠性与失败定律#Law 76 — 静默降级危险定律（Silent-Degradation-Danger Law）\|Law 76：静默降级危险定律]] + [[08_可靠性与失败定律#Law 78 — 测试即真理定律（Untested-Is-Broken Law）\|Law 78：测试即真理定律]] | 都约束生产系统失败模式 | 可观测性、显式失败、静默退化、测试验证分别对应不同设计动作 |
| 信任剪刀 | [[09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84：信任-可靠性剪刀差定律]] + [[11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）\|Law 95：能力-可靠性剪刀定律]] | 都描述“能力/信任/可靠性”不同步 | Law 84 是人机关系侧，Law 95 是模型能力侧 |
| 安全边界 | [[10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）\|Law 87：一切输入皆指令定律]] + [[10_对抗与安全定律#Law 88 — 致命三重奏定律（Lethal-Trifecta Law）\|Law 88：致命三重奏定律]] + [[10_对抗与安全定律#Law 90 — 无可靠转义定律（No-Reliable-Escaping Law）\|Law 90：无可靠转义定律]] + [[10_对抗与安全定律#Law 92 — 数据即攻击面定律（Data-Is-Attack-Surface Law）\|Law 92：数据即攻击面定律]] | 都是提示词注入和工具安全相关约束 | 上下文指令混合、高危能力组合、无法可靠转义、数据攻击面分别不同 |
| 真理与事实 | [[03_统计与泛化定律#Law 27 — 基率定律（Base Rate Law）\|Law 27：基率定律]] + [[07_认识论与真理定律#Law 61 — 贝叶斯更新定律（Bayesian-Updating Law）\|Law 61：贝叶斯更新定律]] + [[07_认识论与真理定律#Law 66 — 似然比定律（Likelihood-Ratio Law）\|Law 66：似然比定律]] | 都涉及先验、证据和信念更新 | 基率、贝叶斯更新、似然比分别回答不同层次的问题 |
| 失败治理 | [[04_系统与控制定律#Law 37 — 单点故障定律（Single-Point-of-Failure Law）\|Law 37：单点故障定律]] + [[04_系统与控制定律#Law 38 — 冗余-效率权衡定律（Redundancy-Efficiency Tradeoff Law）\|Law 38：冗余-效率权衡定律]] + [[08_可靠性与失败定律#Law 75 — 纵深防御定律（Defense-in-Depth Law）\|Law 75：纵深防御定律]] | 都解释可靠性设计中的脆弱点和防线 | 单点故障、冗余权衡、纵深防御分别对应不同设计动作 |
| 接口边界 | [[05_接口与边界定律#Law 43 — 接口永存定律（Interface-Permanence Law）\|Law 43：接口永存定律]] + [[05_接口与边界定律#Law 44 — 契约显式化定律（Explicit-Contract Law）\|Law 44：契约显式化定律]] + [[05_接口与边界定律#Law 48 — 关注点分离定律（Separation-of-Concerns Law）\|Law 48：关注点分离定律]] + [[05_接口与边界定律#Law 49 — 组合性定律（Composability Law）\|Law 49：组合性定律]] + [[05_接口与边界定律#Law 50 — 松耦合定律（Loose-Coupling Law）\|Law 50：松耦合定律]] | 都在处理边界、契约和组件演化 | 接口持久性、显式契约、职责分离、组合性、松耦合分别不同 |

## 最重要的不可合并边界

### Law 84 vs Law 95

- [[09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）|Law 84]]：人的信任可能随系统能力展示而过快增长。
- [[11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）|Law 95]]：模型能力边界扩张，不代表边界内所有任务同等可靠。

前者是**人机关系与组织风险**，后者是**模型能力与可靠性曲线**。可以成组引用，不能互相替代。

### Law 74 vs Law 86

- [[08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）|Law 74]]：不可逆决定慢做，可逆决定快做。
- [[09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）|Law 86]]：问责不能终止在 AI，必须按角色追溯到自然人或法人。

前者决定**审慎度**，后者决定**责任链**。一个回答“要多慢”，一个回答“哪些自然人或法人角色分别负责什么”。

### Law 12 vs Law 14

- [[02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）|Law 12]]：有客观、廉价、独立验证器时，核验候选输出可比从头生成更便宜。
- [[02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）|Law 14]]：多步链路中错误会累积。

Law 12 解释哪里存在可利用的验证成本杠杆，以及为什么要先设计验证器；Law 14 解释为什么长链路需要分解、检查点和短反馈链。

### Law 4 vs Law 5

- [[01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）|Law 4]]：没有来源就不能凭空产生可靠信息。
- [[01_信息与压缩定律#Law 5 — 检索优于记忆定律（Retrieval-Over-Memorization Law）|Law 5]]：系统输出受输入信息质量限制。

Law 4 是信息来源边界；Law 5 是输入质量边界。它们相邻但不等价。

## 维护规则

1. 本页是**语义关系图**，不是重编号方案。
2. 不因为存在父子关系就删除子 Law；子 Law 的价值通常在于工程操作化。
3. 不因为存在重叠就强行物理合并；先在正文中补“边界/关系”字段。
4. 如果后续要修改关系判断，先更新 [[_governance/laws/LAWS_TAXONOMY_REVIEW|Taxonomy Review]] 或新的审计页，再同步本图。
5. 所有全库引用策略以 [[00_REFERENCE-POLICY|Reference Policy]] 为准。
