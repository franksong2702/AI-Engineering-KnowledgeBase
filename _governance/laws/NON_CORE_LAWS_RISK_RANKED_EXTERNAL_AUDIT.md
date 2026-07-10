---
type: external-reference-audit
aliases: [NonCoreLawsRiskRankedExternalAudit, 非 Core Laws 风险排序外部核验]
abstraction_layer: 运营机制（风险排序外部核验）
date: 2026-07-10
course: laws-of-ai-engineering
status: completed
scope: 18 条高影响非 Core Law 的外部来源、表述边界与正文裁决
tags: [AI工程, Laws, 外部引用, 风险排序, citation, 非Core]
---

# 非 Core Laws 风险排序外部核验（18 条）

> 本文承接 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCES|Laws 外部依据说明]] 与 [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core Laws 外部核验]]。目标不是机械核验剩余 79 条，而是先处理“被全库频繁调用、且一旦写得过硬会误导架构决策”的非 Core Law。

## 选择方法

1. 统计治理区和 Laws 正典之外的 heading 级入链次数；
2. 提高安全、可靠性、统计、HITL 等高影响主张的风险权重；
3. 优先核验带“数学级、硬规律、必然、唯一、无例外”等强模态的条目；
4. 达到 15–20 条的预定批次后停手，不为了清零剩余 61 条而继续。

## 核验矩阵

| Law | 主动 heading 入链 | 核验结论 | 主要来源 | 不能过度声称 | 正文裁决 |
|---|---:|---|---|---|---|
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 2 — 上下文即状态定律（Context-is-State Law）\|Law 2]] | 9 | 架构条件支持 | [Attention Is All You Need](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) | Transformer 单次前向不保留会话状态，不等于所有模型或产品永远只有上下文一种状态 | 收窄 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 3 — 信噪比定律（Signal-to-Noise Law）\|Law 3]] | 14 | 实证支持、数学解释不成立 | [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/) | softmax 权重和为 1 不能证明加入任意内容必然伤害；相关信息也可能改善表现 | 收窄并纠正理论依据 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 21 — 停机与预算定律（Termination-Budget Law）\|Law 21]] | 12 | 工程 guardrail 受支持 | [Turing 1936](https://doi.org/10.1112/plms/s2-42.1.230)；[Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) | 停机不可判定性不直接证明每个业务循环必须使用同一种固定上限 | 收窄 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 25 — 分布漂移定律（Distribution Shift Law）\|Law 25]] | 18 | 强理论边界支持 | [Ben-David et al. 2010](https://proceedings.mlr.press/v9/david10a.html) | 分布变化使旧证据失去自动外推资格，不代表性能一定下降 | 收窄 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 30 — 过拟合定律（Overfitting Law）\|Law 30]] | 18 | 强支持 | [Dwork et al. 2015](https://arxiv.org/abs/1506.02629) | 反复查看固定 holdout 增加自适应过拟合风险，不是“持续优化必然迟早过拟合” | 收窄 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 31 — 长尾定律（Long-Tail Law）\|Law 31]] | 17 | 场景实证支持 | [Dean and Barroso 2013](https://research.google/pubs/the-tail-at-scale/) | 长尾是否主导失败必须按目标分布测量，不能从“真实世界”三个字自动推出 | 收窄 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 36 — 可观测性定律（Observability Law）\|Law 36]] | 14 | 强工程价值，控制论类比需纠正 | [Kalman 1960](https://boletin.math.org.mx/pdf/2/5/BSMM%282%29.5.102-119.pdf)；[OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/) | 控制论中的 observability 与 controllability 是不同性质；前者不是后者的逻辑先决条件 | 收窄并纠正理论依据 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 41 — 复杂度累积定律（Complexity-Accumulation Law）\|Law 41]] | 18 | 有条件经验支持 | [Lehman 1980](https://cs.uwaterloo.ca/~a78khan/cs446/additional-material/scribe/27-refactoring/Lehman-LawsOfSoftwareEvolution.pdf) | “复杂度只会单向累积”“交互必然超线性”“等同熵增”都过强 | 收窄 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 42 — 优雅降级定律（Graceful-Degradation Law）\|Law 42]] | 13 | 强工程实践支持 | [Google SRE: Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) | 安全、完整性和原子操作可能必须 fail closed；降级路径本身也会失效 | 补边界 |
| [[laws-of-ai-engineering/05_接口与边界定律#Law 47 — 最小权限定律（Least-Privilege Law）\|Law 47]] | 10 | 直接强支持 | [Saltzer and Schroeder 1975](https://doi.org/10.1109/PROC.1975.9939) | 最小权限降低暴露与损害，不保证系统没有漏洞或错误授权 | 保留正文 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 63 — 不确定性外显定律（Surface-Uncertainty Law）\|Law 63]] | 11 | 选择性预测支持，表达方式需校准 | [SelectiveNet](https://proceedings.mlr.press/v97/geifman19a.html)；[Guo et al. 2017](https://proceedings.mlr.press/v70/guo17a.html) | 模型自报置信度不自动校准；展示更多不确定性也不一定改善决策 | 收窄 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 71 — 显式失败定律（Fail-Loudly Law）\|Law 71]] | 15 | 可靠性原则支持 | [Fail-stop processors](https://doi.org/10.1145/357369.357374)；[Google SRE: Production Services Best Practices](https://sre.google/sre-book/service-best-practices/) | 不是所有错误都应崩溃或打断用户；关键是不把失败伪装成成功，并按语义选择 fail open/closed/degrade | 收窄 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 72 — 爆炸半径定律（Blast-Radius Law）\|Law 72]] | 10 | 直接工程支持 | [AWS Reliability Pillar: Fault Isolation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.html) | 隔离降低影响范围，不代替预防、检测和恢复 | 保留正文 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 76 — 静默降级危险定律（Silent-Degradation-Danger Law）\|Law 76]] | 31 | 监控实践支持，比较级过强 | [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) | 静默退化不总比崩溃更危险；持续评测也不是唯一发现手段 | 收窄 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 77 — 恢复优于预防定律（Recovery-Over-Prevention Law）\|Law 77]] | 16 | 恢复导向工程支持 | [Recovery-Oriented Computing](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2002/5574.html) | 恢复不应普遍“优于”预防，也不能应对所有故障；不可恢复与安全事故仍需预防优先 | 收窄 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 79 — 人在回路定律（Human-in-the-Loop Law）\|Law 79]] | 13 | 人因研究支持条件性边界 | [Bainbridge 1983](https://doi.org/10.1016/0005-1098(83)90046-8) | 加一个人不自动提高安全；人需要证据、时间、技能与真实干预能力 | 保留 P2-C 后正文 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 92 — 数据即攻击面定律（Data-Is-Attack-Surface Law）\|Law 92]] | 12 | 新兴攻击实证支持 | [Greshake et al. 2023](https://arxiv.org/abs/2302.12173) | 风险来自跨信任边界和可影响行为的数据，不是每个字节都同等危险；内部数据也可能被污染 | 补边界 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 99 — 简单性存活定律（Simplicity-Survives Law）\|Law 99]] | 21 | 间接工程支持 | [Brooks 1987](https://doi.org/10.1109/MC.1987.1663532)；[Saltzer and Schroeder 1975](https://doi.org/10.1109/PROC.1975.9939) | 来源支持控制非必要复杂度，不证明简单方案在所有环境中更能“存活” | 收窄 |

## 批次裁决

- **保留正文、只补集中 citation（3）**：Law 47 / 72 / 79。Law 79 的条件性边界已在 Core P2-C 下游收束时提前完成。
- **正文收窄（15）**：Law 2 / 3 / 21 / 25 / 30 / 31 / 36 / 41 / 42 / 63 / 71 / 76 / 77 / 92 / 99。
- **停手条件**：15 条收窄完成、18 条集中 citation 落地、主动旧强断言清零、全库体检通过后，结束本轮；剩余 61 条不自动进入下一批。

## 完成状态（2026-07-10）

- 18 条集中 citation 已写入 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCES|Laws 外部依据说明]]，全库去重核验覆盖从 23/102 提升到 **41/102**。
- 15 条正文已按本表裁决收窄；Law 编号和 heading 均未改变。
- Constitution、ADS、Foundation、Evaluation、Production、Anti-patterns、Multimodal 与 Human-AI 中的高确信度旧强断言已同步；ADS 机器层由编译器重新生成。
- 剩余 61 条保持候选池状态，不因覆盖率目标自动立项；只有季度重估发现更高传播风险或新外部证据时再进入下一批。

## 初见审查问题

> 反驳：高频引用不等于高风险，为什么不先核验“最像数学定理”的低频 Law？

回应：本轮目标是降低全库传播风险，所以把“错误一旦存在会被多少下游放大”纳入排序；同时用强模态和安全/可靠性权重补偿纯频次的缺陷。低频硬断言仍可在后续季度重估中进入，但不为追求覆盖率立即扩批。

> 初见复查后的第二个质疑：一次改写 15 条会不会让下游语义漂移失控？

回应：本批保留全部编号与 heading，只改不受来源支持的必然性、唯一性和适用边界；集中 citation 与本矩阵保留了逐条裁决坐标。下游只同步高确信度的主动强断言，并用旧短语扫描、ADS 编译、交叉引用检查和全库体检机械验收。
