---
type: handbook-index
aliases: [AntiPatterns-INDEX]
date: 2026-07-06
abstraction_layer: 方法 + 警示（方法的镜像）
course: ai-engineering-anti-patterns
tags: [AI工程, 反模式, AntiPatterns, 警示手册]
---

# 《AI Engineering Anti-Patterns》总索引

> 一本警示手册。总结未来 AI 系统最容易犯的错误——不是简单的 prompt 错误，而是 Agent 架构、多智能体、记忆、工具、工作流、评价、自主性、推理这些层面的**结构性错误**。
> 《[LLM Design Patterns](../llm-design-patterns/00_INDEX.md)》的配套反面教材。整套体系第九本，姊妹篇还有 [Laws](../laws-of-ai-engineering/00_INDEX.md) · [Foundation](../foundation-of-ai-engineering/00_INDEX.md) · [Evaluation](../evaluation-of-ai-systems/00_INDEX.md) · [Multi-Agent 手册](../multi-agent-patterns-handbook/00_INDEX.md) · [Agent 圣经](../agent-bible/00_INDEX.md)。

> [!important] Laws 引用边界
> 本书援引的核心定律以 [Law System](../laws-of-ai-engineering/00_INDEX.md) 为正典，尤其参考 [Core Laws](../laws-of-ai-engineering/00_CORE-LAWS.md) 与 [Reference Policy](../laws-of-ai-engineering/00_REFERENCE-POLICY.md)。反模式是 Laws 被违反时的工程形态，但不要为每个反模式都强行补 Law 链接；只在根因清晰时引用，例如 [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）|Law 24：古德哈特定律]]（刷分/代理指标）、[[laws-of-ai-engineering/02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）|Law 14：误差累积定律]]（长链路失败）、[[laws-of-ai-engineering/08_可靠性与失败定律#Law 71 — 显式失败定律（Fail-Loudly Law）|Law 71：显式失败定律]]（静默失败）、[[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）|Law 87：一切输入皆指令定律]] / [[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）|Law 94：权限胜过自觉定律]]（安全与权限）。

## 为什么反面教材和正面教材一样重要

正面教材（模式、定律）教你"该怎么做"，但真实工程的失败，往往不是因为不知道该怎么做，而是因为**掉进了一个看起来合理、实则有害的陷阱**。反模式的危险恰恰在于它们"表面合理"——每一个反模式在被采用的那一刻都显得像个好主意。这本书的核心价值，是让你在掉进去之前就认出那个坑。

一个隐性洞察（来自 [Foundation 第七章](../foundation-of-ai-engineering/00_INDEX.md)）：**成熟工程师和新手最大的区别，往往在于知道什么不该做。** 正面知识（该做什么）相对容易传授，反面知识（不该做什么、为什么那个诱人的选择是错的）通常只能靠踩坑获得。这本书试图把那些坑提前标出来，让你不必亲自踩。

## 每个反模式的 12 个字段

名称 · 错误模式 · 表面为什么合理 · 为什么实际有问题 · 产生原因 · 典型症状 · 失败案例 · 造成的影响 · 如何检测 · 如何修复 · 更好的设计方式 · 违反了哪些定律/模式原则。

## 七大类，102 个反模式

| 类别 | 反模式数 | 核心陷阱 |
|------|---------|---------|
| [01_Agent架构反模式](01_Agent架构反模式.md) | AP 1–16 | 把简单问题过度 Agent 化、职责不清、无限委托 |
| [02_多Agent反模式](02_多Agent反模式.md) | AP 17–32 | Agent 泛滥、通信爆炸、协调开销吞噬收益 |
| [03_记忆反模式](03_记忆反模式.md) | AP 33–46 | 记忆倾倒、上下文污染、无限历史 |
| [04_推理反模式](04_推理反模式.md) | AP 47–60 | 无目的反思、CoT 成瘾、过度规划、分析瘫痪 |
| [05_工具使用反模式](05_工具使用反模式.md) | AP 61–73 | 工具成瘾、选错工具、过度调用 |
| [06_工作流反模式](06_工作流反模式.md) | AP 74–87 | 过度自动化、僵化流程、无人工检查点、无失败恢复 |
| [07_评价反模式](07_评价反模式.md) | AP 88–102 | 刷分、错误指标、为分数优化、忽略真实用户 |
| [08_最应避免的20个错误](08_最应避免的20个错误.md) | Top 20 | 全书最致命错误的排序总结 |

## 反模式的共同结构：它们为什么诱人

读完全书你会发现，几乎所有反模式都共享同一个诱惑结构——**它们用一个可见的短期好处，换一个不可见的长期代价**：

- 过度 Agent 化：可见的"更智能/更高级"，不可见的方差、成本、不可控。
- 过度自动化：可见的"省人力"，不可见的失控风险和不可逆事故。
- 刷 benchmark：可见的"分数上升"，不可见的过拟合和真实价值脱节。
- 记忆倾倒：可见的"信息更全"，不可见的信噪比崩溃。

**识别反模式的元技巧：当一个选择的好处立即可见、代价延迟且隐蔽时，高度警惕。** 这个不对称正是反模式滋生的温床（呼应 [Foundation](../foundation-of-ai-engineering/00_INDEX.md) 的"负空间"洞察——最高级的工程是关于不做什么）。

## 三条贯穿全书的诊断问题

面对任何设计，问这三个问题，能提前识别大多数反模式：

1. **"这个复杂度被收益证明了吗？"**——对抗过度 Agent 化、过度自动化、多 Agent 泛滥（[简单优先](../foundation-of-ai-engineering/04_最值得记忆的设计原则.md)）。
2. **"它失败时，我能便宜地发现吗？"**——对抗静默失败、无检查点、无监控（[失败廉价可查](../laws-of-ai-engineering/00_INDEX.md)）。
3. **"我优化的这个指标，是真实目标还是它的代理？"**——对抗刷分、错误指标、古德哈特（[[03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）|古德哈特]]）。

如果这三个问题你答不上来，你大概率正站在某个反模式的边缘。
