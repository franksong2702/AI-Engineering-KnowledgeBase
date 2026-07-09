---
type: book-index
aliases: [ModelAdaptation-INDEX]
date: 2026-07-06
abstraction_layer: 方法 + 原则
course: model-adaptation
tags: [AI工程, 微调, 训练, 对齐, 知识库补充]
---

# 《Model Adaptation》总索引

> [!note] 版本状态：v1.0 扩写版（2026-07-07）
> 初版为纲要级；本版已逐 Part 增补"工程手册、反例与边界、验收清单"三类内容，原纲要文本全部保留。数字均为经验量级示意。

> 补齐知识库审计发现的第二大缺失（[[01_编辑审计|M2]]）。整套体系讲了怎么用现成模型（prompt/RAG/工具/编排），却几乎没讲**当这些都不够时，如何定制模型本身**——微调、对齐、蒸馏、自部署。
> 收束于统一体系：[[README|知识库总入口]] · 前置 [[data-foundation-of-ai-systems/00_INDEX|Data Foundation]]（数据质量是训练的前提）。

> [!important] Laws 引用边界
> Model Adaptation 是优化阶梯的高成本层，优先引用与训练/对齐/风险直接相关的 Laws：[[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）|Law 24：古德哈特定律]]（偏好代理被优化后会失真）、[[laws-of-ai-engineering/03_统计与泛化定律#Law 30 — 过拟合定律（Overfitting Law）|Law 30：过拟合定律]]（固定评测和训练目标会被过拟合）、[[laws-of-ai-engineering/06_经济与资源定律#Law 54 — 质量有成本定律（Quality-Costs Law）|Law 54：质量有成本定律]]（质量提升消耗 token、延迟或复杂度）、[[laws-of-ai-engineering/04_系统与控制定律#Law 38 — 冗余-效率权衡定律（Redundancy-Efficiency Tradeoff Law）|Law 38：冗余-效率权衡定律]]（自部署/自训练的韧性与效率权衡）。数据质量仍以前置 [[data-foundation-of-ai-systems/00_INDEX|Data Foundation]] 为准。

## 为什么需要这本书

前九本书默认"用现成模型"。但真实工程中，当 prompt、RAG、工具都用尽仍不够时，你需要改动模型本身。这本书讲优化阶梯的上层——但它的第一课恰恰是：**大多数时候你不该走到这一层。**

## 中心命题

**模型定制（微调/训练）是最后手段，不是高级感的来源；先穷尽提示、检索、工具，走投无路再定制，且定制的成败首先取决于数据质量而非算法。**

这句话对抗两个流行误区：把微调当银弹（多数问题 prompt/RAG 更合适）、把微调当能力提升的万能钥匙（它擅长风格/格式/窄任务，不擅长注入新知识或提升通用推理）。

## 五个 Part

| Part | 主题 | 核心问题 |
|------|------|---------|
| [[01_优化阶梯]] | 优化阶梯 | 什么时候该定制模型？定制之前先穷尽什么？ |
| [[02_微调技术]] | 微调技术 | 全参/LoRA/QLoRA/蒸馏——各自何时用 |
| [[03_对齐与偏好]] | 对齐与偏好优化 | RLHF/DPO——如何让模型符合偏好，以及古德哈特陷阱 |
| [[04_蒸馏与部署]] | 蒸馏与自部署 | 大模型教小模型、开源自部署的取舍 |
| [[05_定制的评价与风险]] | 定制的评价与风险 | 如何评价定制是否成功？灾难性遗忘等风险 |

## 五条贯穿本书的定制定律

1. **优化阶梯，先穷尽上一级**（[[llm-design-patterns/00_INDEX|先穷尽便宜的模式]]）——prompt → few-shot → RAG → 微调 → 继续预训练，成本递增，被证据推着上。
2. **数据质量 > 数据数量 > 算法选择**——几百条高质量样本常胜过几万条脏数据（[[data-foundation-of-ai-systems/00_INDEX|Data Foundation]] 的核心在训练领域的形态）。
3. **微调改风格不改知识**——微调擅长固定格式/风格/窄任务，注入新知识用 [[llm-design-patterns/00_INDEX|RAG]] 更合适。
4. **对齐逃不过古德哈特**（[[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）|古德哈特定律]]）——偏好优化是在优化一个偏好的代理，更强的优化更擅长钻空子。
5. **定制增加了你的负担**——自部署/自训练意味着你接管了 serving、质量保障、维护的全部复杂度（[[laws-of-ai-engineering/04_系统与控制定律#Law 38 — 冗余-效率权衡定律（Redundancy-Efficiency Tradeoff Law）|冗余-效率权衡]]）。

## 与其他书的关系

- **前置 [[data-foundation-of-ai-systems/00_INDEX|Data Foundation]]**：训练的成败首先是数据质量问题，那本是这本的地基。
- **上承 [[llm-design-patterns/00_INDEX|LLM Design Patterns]]**：这本是优化阶梯上 prompt/RAG 之上的一级——只在下层用尽后才上来。
- **受 [[evaluation-of-ai-systems/00_INDEX|Evaluation]] 约束**：定制是否成功由评价判定；对齐的核心难题（古德哈特）就是评价的核心敌人。
- **呼应 [[laws-of-ai-engineering/00_INDEX|Laws]]**：优化阶梯、古德哈特、质量>数量都是定律在训练领域的投影。
