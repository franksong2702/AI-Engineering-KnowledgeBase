---
type: handbook-index
aliases: [DesignPatterns-INDEX]
date: 2026-07-06
abstraction_layer: 方法（会随能力重洗）
course: llm-design-patterns
tags: [LLM, DesignPatterns, Prompt, Agent, 手册索引]
---

# 《LLM Design Patterns》总索引

> 每个模式回答同样十一问：为什么存在、何时用、何时不用、架构图、Prompt、Workflow、Agent、优点、缺点、案例、未来方向。
> 姊妹篇：[《从零到 Agent 专家》](../textbook-zero-to-agent/00_INDEX.md) · [《Multi-Agent 架构手册》](../multi-agent-patterns-handbook/00_INDEX.md) · [《AI 决策框架大全》](../decision-frameworks-guide/00_INDEX.md)

## 本书与《Multi-Agent 架构手册》的分工

两本书有交集（Planner-Executor、MapReduce、Debate、Judge），但视角不同，互补而非重复：

- **本书（LLM Design Patterns）**：焦点是"**如何组织 LLM 的推理与推断**"——从单次调用的思维结构（CoT、ReAct），到提示的写法（few-shot、schema），到知识注入（RAG、记忆），到质量控制（反思、裁判）。粒度更细，下沉到 prompt 和单模型层。
- **[Multi-Agent 架构手册](../multi-agent-patterns-handbook/00_INDEX.md)**：焦点是"**多个智能体如何协调**"——粒度更粗，讲拓扑、通信、状态一致性。

重叠的模式，本书从"推理/推断技术"角度讲，那本从"多体协调"角度讲。遇到编排类模式（家族五）本书会主动引你去那本看协调细节。

## 模式地图（按抽象层分家族）

| 家族 | 抽象层 | 模式 |
|------|--------|------|
| [01_推理模式](01_推理模式.md) | 单次/单体的思维结构 | Chain-of-Thought · Self-Consistency · ReAct · Self-Critique/Reflexion |
| [02_提示结构模式](02_提示结构模式.md) | 提示的组织方式 | Few-shot · Role/Persona · Structured Output · Prompt Chaining · 意图澄清（Rephrase） |
| [03_知识与记忆模式](03_知识与记忆模式.md) | 上下文的来源 | RAG · Memory Retrieval · Tool Use/Function Calling · Context Compression |
| [04_质量控制模式](04_质量控制模式.md) | 输出的把关 | Critic-Refine/Reflection · LLM-as-Judge · Debate · Ensembling/Voting · Guardrails |
| [05_编排模式](05_编排模式.md) | 多次调用的组织 | Planner-Executor · Map-Reduce · Routing · Orchestrator-Workers |
| [06_历史模式](06_历史模式.md) | 已退役（2026-Q4 重估） | Tree Search/ToT · Least-to-Most · Step-back——原文保留，附退役说明与思想去向 |

## 选型速查：我的问题是什么

```
输出质量不稳/推理出错   → 家族一（先换推理模型或加 CoT，难题上 Self-Consistency；有客观验证器时用"多候选 + 验证"）
模型不会做/格式不对     → 家族二（few-shot 教它、schema 约束它）
模型不知道/信息过时     → 家族三（RAG 喂知识、Tool Use 接能力、Memory 记住）
输出不能直接信         → 家族四（Reflection 自改、Judge 把关、Guardrails 兜底）
任务太大/太杂一次做不完 → 家族五（拆解、并行、路由）
```

## 六条跨模式原则

> 2026-10-07 前称"跨模式定律"。"定律"一词留给 [Laws of AI Engineering](../laws-of-ai-engineering/00_INDEX.md)，这里是方法层的经验原则，引用时写"LLM Design Patterns 原则 N"。

1. **先穷尽便宜的模式，再上贵的**。能靠一句 CoT 解决的别上多次采样或搜索，能靠 few-shot 解决的别微调。模式的采用顺序应是成本递增、被证据推着走。
2. **每个模式都是拿 token/延迟换质量**。没有免费的质量提升。采用任何模式前先问"提升几何 ÷ 成本几倍"。
3. **推理类模式的收益取决于任务难度是否超出模型现有能力**。CoT 和多次采样在需要多步推理、模型单次常做错的任务上收益大，在模型本就会的简单任务上是纯浪费甚至有害（过度思考）。
4. **有客观反馈信号时，质量控制模式才真正有效**。Reflection/Judge 接上测试、检索、规则时是利器；纯靠模型自评时容易自我表扬。
5. **模式可组合，但每叠一层都要有可观测性**。生产系统都是组合体（如 Planner + 每步 Reflection + 出口 Judge），但组合的调试成本随层数超线性增长。
6. **模式会因模型能力进化而重新洗牌**。推理模型内化了 CoT，长上下文吃掉了部分 RAG 场景——模式的价值是动态的，定期重估。

## 成本/成熟度速查

> 倍数均为相对单次调用的经验量级，非测量值；按你的任务实测。

| 模式 | 相对成本 | 主要买到的东西 | 成熟度 |
|------|---------|--------------|--------|
| Chain-of-Thought | 1-1.5×（推理模型的思考 token 另计） | 推理准确率 | 生产级 |
| Few-shot / Role / Schema | ~1× | 格式与行为可控 | 生产级 |
| RAG / Tool Use | 1.5-3× | 知识与能力扩展 | 生产级 |
| Self-Consistency / Voting | 3-10× | 可靠性 | 生产级 |
| Reflection / Judge | 2-4× | 输出质量与把关 | 生产级 |
| ReAct / Planner-Executor | 3-8× | 完成复杂任务 | 生产级 |
| ~~Tree Search / ToT~~ | 5-30× | 难题求解上限 | 已移入历史区（2026-Q4） |
| Debate | 5-15× | 高风险判断 | 成熟 |
