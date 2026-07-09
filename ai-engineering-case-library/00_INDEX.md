---
type: case-library-index
aliases: [CaseLibrary-INDEX]
date: 2026-07-06
abstraction_layer: 应用（把知识体系用在真实问题上）
course: ai-engineering-case-library
tags: [AI工程, 案例库, 实战]
---

# 《AI Engineering Case Library》总索引

> 不讲理论。108 个典型 AI 系统设计问题（原 100 个通用案例 + 8 个多模态补充案例），每个演示如何调用整个知识体系解决它。
> 这是知识库的**应用层**——[[The-Constitution-of-AI-Engineering|宪法]]给骨架、[[agent-decision-system/00_PROTOCOL|决策系统]]给协议，本库给"用在真问题上长什么样"。

## 怎么用这个案例库

每个案例按 11 字段展开：**Problem · Context · Constraints · Analysis · Relevant Laws · Relevant Patterns · Architecture Decision · Anti-Patterns Avoided · Evaluation Method · Final Solution · Lessons Learned**。

案例里的具体 ID 已升级为一键直达：例如 [[agent-decision-system/04_LAW-INVARIANTS#LAW-02 · 压缩必然有损→会幻觉（Lossy Compression）|LAW-02]] 会直接跳到对应定律条目，[[agent-decision-system/02_PATTERN-CARDS#PAT-03 · RAG（检索增强生成）|PAT-03]] 会直接跳到对应模式卡。模块速查：**LAW-xx**→[[agent-decision-system/04_LAW-INVARIANTS|定律约束]]，**PAT-xx**→[[agent-decision-system/02_PATTERN-CARDS|模式卡]]，**ANTI-xx**→[[agent-decision-system/03_ANTIPATTERN-DETECTORS|反模式检测器]]，**Q-xx**→[[agent-decision-system/05_EVAL-CHECKLIST|评价清单]]。

**学习方式**：先只读 Problem/Context/Constraints，先用 [[agent-decision-system/01_SITUATION-ROUTER|Situation Router]] 做处境分诊，再自己走一遍决策循环（诊断→定律→模式→避坑→评价），最后对照案例的 Analysis 及后续。差异就是你的成长点。案例的价值不在答案，在**推理路径**。

**深度版案例**：Case 1/5/11/14/21/27/31/40/41/43/51/54/61/64/73/75/81/88/91/100 已扩为深度版（含失败反转、trace 片段、具体参数、多条教训），原十类各有两个深度样板；多模态分册先保持精简案例层，后续只有出现明确教学缺口才挑 1–2 个深度化。

## 十一类，108 个案例

| 类 | 领域 | 案例 |
|----|------|------|
| [[01_RAG与知识系统]] | RAG 与知识系统 | Case 1–10 |
| [[02_Agent架构]] | 单 Agent 架构 | Case 11–20 |
| [[03_多Agent系统]] | 多 Agent 系统 | Case 21–30 |
| [[04_可靠性与生产]] | 可靠性与生产部署 | Case 31–40 |
| [[05_评价与质量]] | 评价与质量 | Case 41–50 |
| [[06_安全与对抗]] | 安全与对抗 | Case 51–60 |
| [[07_成本与性能]] | 成本与性能 | Case 61–70 |
| [[08_记忆与上下文]] | 记忆与上下文 | Case 71–80 |
| [[09_数据与模型定制]] | 数据与模型定制 | Case 81–90 |
| [[10_人机与产品决策]] | 人机协作与产品决策 | Case 91–100 |
| [[11_多模态系统]] | 多模态系统 | Case 101–108 |

## 三条贯穿全库案例的实战教益

读完 108 个案例，你会反复看到同样几个教训——它们比任何单个案例都重要：

1. **多数"更聪明"的方案是错的**。真实案例里，正确解往往是更简单的那个（单次调用胜过 Agent、RAG 胜过微调、规则胜过模型）。复杂度必须被证明。
2. **最贵的错误都发生在评价缺失处**。刷分、无评测上线、只测峰值、忽略长尾——案例里的翻车几乎都能追溯到"没有正确地评价"。
3. **不可逆 + 过度信任 = 灾难配方**。案例里的安全/信任事故，几乎都是"给了不该给的自主权 + 信了不该信的输出"。

## 案例的诚实声明

这些案例是**典型化、综合化**的真实问题（不指向特定公司/产品），用于教学。它们的技术判断基于本知识库的定律和模式，但每个真实项目都有本库未覆盖的具体情境（[[agent-decision-system/00_PROTOCOL|定律有边界]]）——案例教的是**推理方法**，不是可照抄的配方。案例中的具体数字（命中率、成本倍数、成功率等）同为教学编排值——用于展示推理的量级感，非实测数据。
