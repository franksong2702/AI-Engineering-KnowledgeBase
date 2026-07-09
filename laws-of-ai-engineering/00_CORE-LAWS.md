---
type: law-system-map
date: 2026-07-08
course: laws-of-ai-engineering
abstraction_layer: 规律（核心正典）
stability: 高（核心约束层）
tags: [AI工程, Laws, CoreLaws, 正典, 引用策略]
---

# Core Laws｜全库核心 Law

> 本页回答一个问题：102 条 Law 里，哪些可以作为整套 AI Engineering Knowledge Base 的稳定核心引用？

相关入口：[[laws-of-ai-engineering/00_INDEX|Laws INDEX]] · [[00_LAW-RELATION-GRAPH|Law Relation Graph]] · [[00_REFERENCE-POLICY|Reference Policy]] · [[_governance/laws/LAWS_TAXONOMY_REVIEW|Laws Taxonomy Review]]

## 使用边界

这里的 “Core Laws” 不是说其他 Law 不重要，也不是要把 102 条压缩成 18 条后删除其余条目。

它的作用只有三个：

1. **全库引用治理**：当 README、总图、宪法、Foundation、Evaluation、Agent Decision System 等入口层需要引用 Laws 时，优先从这里选择。
2. **避免 Law 泛化**：不要把所有看起来像原则的句子都升级成全库公理。
3. **保留适用边界**：即使是 S 级核心，也必须服从 [[11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）|Law 102：定律有边界定律]]。

## S 级核心 Law 清单

| Law | 名称 | 全局角色 | 使用注意 |
|---|---|---|---|
| [[01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] | 有损压缩定律（Lossy Compression Law） | 事实性幻觉与知识外置的底层根 | 与 Law 6 分工：Law 1 偏模型表征与事实性输出 |
| [[01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）\|Law 4]] | 信息守恒定律（No-Information-From-Nothing Law） | 事实、数据、检索、RAG 的底层约束 | 适合用于反驳“无来源生成事实”的设计 |
| [[01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]] | 压缩必然丢失定律（Compression-Loses Law） | 摘要、记忆、状态压缩的边界 | 与 Law 1 分工：Law 6 偏压缩操作与状态摘要 |
| [[01_信息与压缩定律#Law 7 — 分布内可靠定律（In-Distribution Reliability Law）\|Law 7]] | 分布内可靠定律（In-Distribution Reliability Law） | 可委托性与分布外风险判断 | 引用时要说明“分布”是什么，而不只是泛称可靠 |
| [[02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]] | 验证-生成不对称定律（Verification-Generation Asymmetry Law） | 生成、验证、人机分工的根 | Foundation、Evaluation、Agent Workflow 的核心 law |
| [[02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）\|Law 14]] | 误差累积定律（Error Compounding Law） | 多步 Agent / Workflow 分解与纠错的根 | 适合解释为什么需要短链路、检查点与回滚 |
| [[03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24]] | 古德哈特定律（Goodhart's Law） | 评价、对齐、KPI 的核心风险 | 指标成为目标时才引用；不要泛化成“指标都没用” |
| [[03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]] | 校准定律（Calibration Law） | 置信、信任、评价者校准的根 | 适合连接 confidence、eval、human trust |
| [[07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）\|Law 62]] | 流畅度非正确性定律（Fluency-Is-Not-Truth Law） | 流畅不等于真 | 适合事实核查、评估、教学场景 |
| [[07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）\|Law 64]] | 可证伪性定律（Falsifiability Law） | 可证伪性和审计要求 | 适合定义完成标准、验证标准、review 标准 |
| [[08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）\|Law 74]] | 不可逆性定律（Irreversibility Law） | 可逆性决定审慎度 | 与权限、审批、生产变更、长期承诺相关 |
| [[09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84]] | 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law） | 人对系统的信任可能快于真实可靠性增长 | 与 Law 95 成组，但不要互相替代 |
| [[09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] | 责任不可委托定律（Accountability-Cannot-Be-Delegated Law） | 责任主体不能外包给模型 | 适合治理、审批、HITL 和组织责任讨论 |
| [[10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）\|Law 87]] | 一切输入皆指令定律（All-Input-Is-Instruction Law） | Prompt injection 与上下文污染的根 | 安全设计的基础假设，不依赖模型“自觉” |
| [[10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）\|Law 94]] | 权限胜过自觉定律（Permission-Over-Restraint Law） | 权限硬边界胜过模型自我约束 | 与工具权限、文件系统、生产操作直接相关 |
| [[11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）\|Law 95]] | 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law） | 能力扩张不等于可靠性同步扩张 | 是模型侧剪刀；Law 84 是人机关系侧剪刀 |
| [[11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）\|Law 100]] | 判断力稀缺定律（Judgment-Is-Scarce Law） | AI 让知识变便宜，让选择更稀缺 | 适合解释人类架构师、reviewer、owner 的价值 |
| [[11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）\|Law 102]] | 定律有边界定律（Meta-Law: Every Law Has Boundaries） | 所有 Law 都必须按边界使用 | 防止把 Laws 变成新的教条 |

## 与全库模块的关系

| 模块 | 优先引用的 Core Laws | 说明 |
|---|---|---|
| [[README\|README]] / [[00_Knowledge-Graph-总图\|知识图谱总图]] | Law 12, Law 1/6, Law 7, Law 24, Law 74, Law 84, Law 100, Law 102 | 只用于解释全库骨架，不做逐条展开 |
| [[The-Constitution-of-AI-Engineering\|Constitution]] | Law 12, Law 1/6, Law 7, Law 24, Law 74, Law 84, Law 87, Law 102 | 作为“底层来源”说明，不替换宪法内部 10 条 |
| [[foundation-of-ai-engineering/00_INDEX\|Foundation]] | Law 12, Law 1/4/6, Law 7, Law 24, Law 84, Law 100 | 用于解释工程第一性原理 |
| [[evaluation-of-ai-systems/00_INDEX\|Evaluation]] | Law 12, Law 24, Law 26, Law 62, Law 64, Law 84 | 用于解释评测、校准、证据和 trust |
| [[human-ai-collaboration-foundation/00_INDEX\|Human-AI Collaboration]] | Law 74, Law 84, Law 86, Law 95, Law 100 | 用于解释 HITL、责任、信任与判断力 |
| [[agent-decision-system/00_PROTOCOL\|Agent Decision System]] | Law 12, Law 1/6, Law 7/26, Law 24, Law 87/94, Law 14, Law 74, Law 84, Law 100/86, Law 102 | 只作为操作约束来源，不把 102 条全部塞进运行时 |

## 引用原则

- 全库入口层引用 Core Laws，正文模块引用相关 family anchors，具体案例只在必要处引用场景 Law。
- 不要把每个出现“可靠性”“校准”“不可逆”“指标”的句子都改成 Law 链接。
- 如果一个 Law 的适用边界说不清，应先引用 [[00_REFERENCE-POLICY|Reference Policy]]，不要直接升格为全局公理。
