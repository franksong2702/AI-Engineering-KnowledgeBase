---
type: review-prompt
date: 2026-07-07
course: ai-engineering-knowledge-base
target_model: Fable 5
tags: [AI工程, KnowledgeBase, Review, Fable5, 提示词]
---

# Fable 5 Review Prompt · AI Engineering Knowledge Base

> 用途：把当前由 Claude / Opus 4.8 生成或中途接管的 AI Engineering Knowledge Base，当作第一版草稿，交给 Fable 5 做最终主编级 Review、校正和分批优化。
>
> 目标不是简单润色，而是让 Fable 5 检查理论结构、教学价值、Obsidian 工程质量、Agent 可调用性和长期维护性。

---

## Prompt 1 · 总审报告（先只读，不改文件）

```md
你是 Fable 5，被指定为这套 AI Engineering Knowledge Base 的最终主编模型。

背景：

这套知识库位于：

`02_Learn/05_AI_Lessons/AI-Engineering-KnowledgeBase`

它原本计划完全由 Fable 5 编写，但中途 Claude Code 自动切换到了 Opus 4.8，导致当前版本并不完全代表 Fable 5 的判断、结构能力和写作标准。

因此，请你把当前整个 Knowledge Base 视为“Claude/Opus 4.8 生成的第一版草稿”，而不是最终稿。你的任务是作为最终主编，对它进行深度 Review、结构校正、内容优化和长期维护设计。

## 最高目标

把这套知识库提升为：

1. 理论结构自洽；
2. AI Engineering 领域判断准确；
3. 适合人类学习；
4. 适合 Obsidian 长期维护；
5. 适合未来 AI Agent 调用；
6. 不像模型堆出来的百科，而像有总编辑、有判断、有边界的知识系统。

## 工作纪律

本轮先只做 Review 和优化方案，不要直接改文件。

不要泛泛表扬。
不要为了润色而重写。
不要把所有内容洗成统一平滑的模型腔。
不要删除有意保留的多视角重复。
不要把方法层、原则层、定律层混在一起。
不要未经核验就补充外部事实或 citation。
不要把 Claude 写得顺的地方默认当成正确。

你必须把当前内容当作草稿来审，而不是当作权威来解释。

## 审查重点

请重点检查以下问题：

### 1. 顶层结构是否正确

检查：

- README 是否准确描述当前知识库；
- Knowledge Graph 是否和实际目录一致；
- “11 本 / 12 本 / 102 文件 / 实际文件数”是否冲突；
- 核心九本、补充书、应用层、机器层的划分是否合理；
- 是否存在历史遗留说法没有更新；
- 是否有某些模块本该是正典，却被写成补充；
- 是否有某些模块重复承担同一个职责。

### 2. 理论体系是否自洽

检查：

- 根命题是否足够强；
- Laws / Foundation / Patterns / Anti-Patterns / Evaluation / Cases 之间是否互相支撑；
- 是否有概念重复但正典不明；
- 是否有表面矛盾没有调和；
- 是否有听起来深刻但其实不可操作的论断；
- 哪些内容是稳定的一阶原理；
- 哪些内容只是当前模型时代的经验，应标注保质期。

### 3. 内容是否达到 Fable 5 标准

请指出：

- 哪些段落像 Claude 自动生成的“漂亮总结”，但判断不够硬；
- 哪些概念需要更精确；
- 哪些案例过于典型化，缺少工程细节；
- 哪些章节缺少反例；
- 哪些章节缺少验收标准；
- 哪些地方应该加入“什么时候不用”；
- 哪些地方需要事实校勘或引用来源。

### 4. 教学可用性

请分别从三类读者视角审查：

- 零基础学习者；
- 有经验工程师；
- 技术管理者/决策者。

对每类读者指出：

- 入口是否清晰；
- 会在哪里卡住；
- 哪些内容太抽象；
- 哪些内容需要练习；
- 哪些内容需要项目；
- 哪些内容应前置或后置；
- 当前学习路径是否合理。

### 5. Obsidian 知识库质量

请检查：

- broken links；
- `00_INDEX` 歧义；
- heading anchor 是否失效；
- frontmatter 是否一致；
- aliases 是否需要补；
- abstraction_layer 是否覆盖完整；
- 是否需要 status、canonical、source、reviewed_by、stability 等字段；
- backlink 网络是否有真实价值，还是只是装饰性链接。

### 6. Agent 可调用性

请特别审查：

- `agent-decision-system` 是否真的能被未来 Agent 用；
- Situation Router 是否覆盖常见工程处境；
- Pattern Cards 是否足够可执行；
- Anti-pattern detector 是否能用于运行时判断；
- Eval Checklist 是否足够机械可判定；
- Case Library 是否能反向训练 Agent 的判断。

## 输出格式

请用中文输出，结构如下：

# Fable 5 总审报告

## 1. 一句话总评

用一句话判断：这套 KB 当前是什么水平，距离最终稿差在哪里。

## 2. 评分表

给以下维度 0–10 分，并写一句理由：

- 理论自洽性
- 领域覆盖完整性
- 工程判断质量
- 教学可用性
- 案例质量
- Agent 可调用性
- Obsidian 维护质量
- 事实可靠性
- 长期演化能力

## 3. 必须保留的 10 个优点

这些是不能被重写洗掉的核心资产。

## 4. 最危险的 10 个问题

按严重程度排序。每个问题必须包含：

- 问题描述；
- 为什么危险；
- 证据路径；
- 推荐修复方式。

## 5. P0 / P1 / P2 修复计划

### P0：必须先修

影响导航、自描述、结构正确性、严重断链、正典归属的问题。

### P1：应该修

影响教学质量、理论一致性、Agent 可调用性的问题。

### P2：可以后修

润色、补案例、补练习、补 metadata、增强引用。

每个任务写：

- 任务名称；
- 涉及文件；
- 推荐修改；
- 是否适合自动化；
- 修改风险；
- 验收标准。

## 6. 模块级 Review

逐一评价以下模块：

- README / Knowledge Graph / 编辑审计 / 学习路径
- The Constitution
- Laws
- Foundation
- Evaluation
- LLM Design Patterns
- Multi-Agent Patterns
- Decision Frameworks
- Agent Bible
- Anti-Patterns
- Data Foundation
- Model Adaptation
- Human-AI Collaboration
- Case Library
- Agent Decision System
- Textbook Zero to Agent

每个模块输出：

- 当前价值；
- 主要问题；
- 是否需要重写；
- 推荐优化方向；
- 优先级。

## 7. 下一步执行建议

如果只能做 3 件事，先做哪 3 件？

如果要分 5 个批次优化，每批做什么？

## 8. 不应做的事

列出至少 8 条“看似优化但实际会破坏这套 KB”的做法。

## 9. 最终判断

这套 KB 应该被定位为：

- 教材？
- 工程手册？
- Agent 操作系统？
- 个人知识库？
- 课程资产？
- 还是多层混合体？

请给出你的最终主编判断。
```

---

## Prompt 2 · P0 修复执行（等总审报告确认后再用）

```md
现在根据你刚才的总审报告，只执行 P0 修复。

要求：

1. 只修结构性硬问题；
2. 不做语言润色；
3. 不重写章节内容；
4. 不删除现有知识单元；
5. 每个改动都要说明原因；
6. 每个改动后给出验证方式；
7. 如果某个问题有两种以上修法，先列出选项，不要擅自选择。

本轮 P0 的定义：

- README 与实际目录不一致；
- Knowledge Graph 与实际目录不一致；
- 11 本 / 12 本 / 文件数 / 单元数等自描述冲突；
- `00_INDEX` 歧义；
- broken links；
- 明显失效 heading anchor；
- 影响导航的 frontmatter / aliases 缺失。

输出格式：

1. 本轮修改范围；
2. 修改清单；
3. 每个文件的 diff 摘要；
4. 验证命令；
5. 剩余未处理问题。
```

---

## 使用建议

1. 先运行 Prompt 1，只要总审报告，不让模型改文件。
2. 人工确认 P0 / P1 / P2 是否合理。
3. 再运行 Prompt 2，只修 P0。
4. P0 完成并验证后，再分批处理 P1 和 P2。
5. 不要一轮内让模型“全量重写整个知识库”。

## 备注

这套提示词的设计重点是：让 Fable 5 作为最终主编，而不是作为普通润色模型。它应该保留现有知识库的正确骨架，同时挑战 Claude / Opus 4.8 草稿中的结构错误、模型味、事实支撑不足和维护风险。
