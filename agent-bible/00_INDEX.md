---
type: handbook-index
aliases: [AgentBible-INDEX]
date: 2026-07-06
abstraction_layer: 方法（角色落地）
course: agent-bible
tags: [Agent, SystemPrompt, AI角色, 手册索引]
---

# 《Agent 圣经》总索引

> 每个 Agent 回答同样十二问：名称、职责、适合的问题、输入、输出、System Prompt、Memory 设计、工具需求、质量评估标准、失败模式、最佳实践、未来扩展方向。
> 姊妹篇：[教材](../textbook-zero-to-agent/00_INDEX.md) · [Multi-Agent 架构手册](../multi-agent-patterns-handbook/00_INDEX.md) · [AI 决策框架大全](../decision-frameworks-guide/00_INDEX.md) · [LLM Design Patterns](../llm-design-patterns/00_INDEX.md)

## 这本书怎么用

前四本讲"模式与框架"（怎么思考、怎么协调），这本讲"角色落地"（一个具体职能如何变成可用的 Agent）。每个 Agent 定义都是一份**可直接复制的规格**——拿走 System Prompt 就能用，配上 Memory 和工具设计就能进生产。

三个使用原则：

1. **Agent 是能力的封装，不是人的复刻**。"CEO Agent"不是模拟一个 CEO 的人格，而是封装"做 CEO 类决策所需的视角、约束和输出结构"。别指望换个头衔就变强（[[multi-agent-patterns-handbook/00_INDEX#五条跨模式定律|Multi-Agent 定律 1：上下文隔离]]）——真正的差异来自不同的工具、知识、输出契约和评估标准。
2. **System Prompt 是 Agent 的宪法，但不是全部**。一个 Agent 的质量 = System Prompt（行为定义）× Memory（它记得什么）× 工具（它能做什么）× 评估（它怎么被检验）。四者缺一，Agent 就是个花架子。本书每个条目都四者俱全。
3. **先单体，后编排**。这些 Agent 既可独立使用，也可作为 [Multi-Agent 系统](../multi-agent-patterns-handbook/00_INDEX.md)的成员。但先让单个 Agent 在你的场景里跑通、评测达标，再考虑编排——组合五个没调好的 Agent 只会得到五倍的麻烦。

## Agent 名录（按职能分家族）

| 家族 | Agent | 一句话定位 |
|------|-------|-----------|
| [01_研究与知识](01_研究与知识.md) | 研究员 Researcher | 深入调查一个问题并综合成结论 |
| | 研究规划师 Research Planner | 把研究问题拆成可执行的调研计划 |
| | 事实核查员 Fact Checker | 逐条验证论断的真伪与来源 |
| | 知识整理专家 Knowledge Curator | 把零散信息编译成结构化知识库 |
| | 访谈员 Interviewer | 通过提问挖掘信息与需求 |
| [02_战略与决策](02_战略与决策.md) | CEO | 全局权衡与最终取舍 |
| | CTO | 技术战略与可行性判断 |
| | 产品经理 PM | 把问题转化为要做什么 |
| | 决策者 Decision Maker | 在不确定中给出可复盘的决策 |
| | 规划师 Planner | 把目标拆解为有序可执行的计划 |
| [03_工程与构建](03_工程与构建.md) | 架构师 Architect | 设计系统的结构与取舍 |
| | Workflow 设计师 | 设计可靠的自动化流程 |
| | Prompt 工程师 | 设计与优化可复用的提示 |
| | 文档工程师 Doc Engineer | 产出准确、可维护的文档 |
| [04_质量与审查](04_质量与审查.md) | 代码评审 Code Reviewer | 审查代码的正确性与质量 |
| | 安全审计 Security Auditor | 发现系统的安全漏洞 |
| | 调试专家 Debugger | 定位并解释缺陷的根因 |
| | 通用评审 Reviewer | 按标准评估任意产出 |
| | 批评家 Critic | 找出方案的弱点与盲区 |
| [05_教育与成长](05_教育与成长.md) | 教师 Teacher | 把知识讲到学习者真正理解 |
| | 导师 Mentor | 长期陪伴式的成长指导 |

## Agent 设计的通用骨架

无论哪个角色，一个生产级 Agent 定义都应包含这五层（本书每个条目遵循此结构）：

```
① 身份与职责    —— 它是谁、负责什么、边界在哪（System Prompt 的核心）
② 输入契约      —— 它接受什么、需要什么前置信息
③ 推理与行为    —— 它如何思考（配合[[llm-design-patterns/00_INDEX|推理模式]]）、遵守什么规则
④ 输出契约      —— 它产出什么结构、什么质量标准
⑤ 记忆与工具    —— 它记住什么、能调用什么能力
```

## 六条跨 Agent 心法

1. **明确边界比强调能力更重要**。好的 System Prompt 花在"不做什么""何时该说不知道""何时该上报人类"上的笔墨，往往比"你很擅长X"更有价值。
2. **让 Agent 交代证据状态**。要求区分“有来源确认”“基于证据推断”和“证据不足”，并暴露关键 gaps；未经校准的自报置信度不能当作防御幻觉的闸门。
3. **Memory 分三层**：短期（当前上下文）、中期（任务状态，可存文件）、长期（跨任务经验/用户模型，需检索）。不是每个 Agent 都需要全部三层——按需设计（[见记忆模式](../llm-design-patterns/03_知识与记忆模式.md)）。
4. **质量评估标准必须可操作**。"输出要好"不是标准；"每个论断有来源、无编造引用、覆盖问题的各个方面"才是。没有评估标准的 Agent 无法迭代。
5. **失败模式要预先写下**。每个 Agent 都有典型翻车方式（研究员编引用、评审员放水、决策者过度自信）。预先识别 = 针对性防御。
6. **人在回路的位置决定安全**。可逆输出放手让 Agent 做，不可逆行动（发送、删除、决策拍板）保留人类审批。角色越权威（CEO、Decision Maker），越要强调"我给建议，你做决定"。

## 组合示例（这些 Agent 如何协作）

- **深度研究流水线**：研究规划师（拆解）→ 研究员×N（并行调研）→ 事实核查员（验证）→ 知识整理专家（编译入库）
- **产品决策链**：PM（定义问题）→ 架构师 + CTO（可行性）→ 批评家（挑漏洞）→ CEO/决策者（拍板）
- **代码交付关卡**：Workflow 设计师（设计流程）→ 代码评审 → 安全审计 → 调试专家（修问题）→ 文档工程师（补文档）
- **学习闭环**：教师（讲授）→ Interviewer（检验理解）→ 导师（长期跟踪调整）

组合时套用 [Multi-Agent 架构手册](../multi-agent-patterns-handbook/00_INDEX.md)的拓扑（Planner-Executor、Pipeline、Committee 等）。
