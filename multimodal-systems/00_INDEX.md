---
type: book-index
aliases: [MultimodalSystems-INDEX]
date: 2026-07-09
abstraction_layer: 方法 + 原则（多模态工程层）
course: multimodal-systems
tags: [多模态, 感知管线, 视觉, 音频, 视频, 手册索引]
---

# 《Multimodal Systems》总索引

> 中心命题：**多模态不是"模型多会一项技能"，而是"系统多了一条不可靠的输入通道"。** 文本 LLM 的一切可靠性问题——压缩、幻觉、注入、漂移——在图像、音频、视频、屏幕、传感器上全部重演，且多了一层：在模型推理之前，感知管线已经对世界做了一轮有损压缩。本书把知识库已经成熟的可靠性、评价、生产、权限框架，扩展到非文本输入世界。
>
> 立项审计见 [M3 立项审计](../_governance/content/M3_MULTIMODAL_SCOPE_REVIEW.md)；本书按其边界执行——是文本 KB 的**模态扩展层**，不是 CV/ASR/机器人学教材。

> [!important] 编号空间纪律
> 本书**不新增定律、不新开反模式编号**。定律一律引用 [Law System](../laws-of-ai-engineering/00_INDEX.md) 的正式定义（heading 级链接）；反模式一律引用 [Anti-Patterns](../ai-engineering-anti-patterns/00_INDEX.md) 与 [ADS ANTI 检测器](../agent-decision-system/03_ANTIPATTERN-DETECTORS.md)的既有条目，多模态特有的失败以**具名描述**呈现，不设 ID。这是 [Reference Policy](../laws-of-ai-engineering/00_REFERENCE-POLICY.md) 防串号条款在本书的落实。

## 与姊妹书的边界（立项时划清）

| 姊妹书 | 它管什么 | 本书管什么 |
|---|---|---|
| [Human-AI Interaction Design](../human-ai-interaction-design/00_INDEX.md) | 界面如何向人呈现 AI（输出侧的最后一米） | 感知如何进入系统（输入侧的最初一米） |
| [Data Foundation](../data-foundation-of-ai-systems/00_INDEX.md) | 数据工程的通用规律（质量/管线/漂移/治理） | 非文本模态带来的额外信息损失与验证难题 |
| [Evaluation](../evaluation-of-ai-systems/00_INDEX.md) | 怎么评价 AI 系统（评价理论与设计） | 多模态系统哪些地方必须被**额外**评价（感知/定位/对齐） |
| [AI Systems in Production](../ai-systems-in-production/00_INDEX.md) | 生产系统的通用机制（serving/观测/发布/成本/降级） | 媒体与传感器输入让这些机制**变难**的地方 |
| [Laws](../laws-of-ai-engineering/00_INDEX.md) | 102 条定律的正式定义 | 只引用不新增——本书是若干条 Law 在感知通道上的投影 |
| [Anti-Patterns](../ai-engineering-anti-patterns/00_INDEX.md) | 102 个反模式的正式定义 | 多模态特有失败以具名描述呈现，根因回指既有 ANTI/Law |

凡本书与姊妹书冲突，以对方书中对应概念的正式定义为准——本书只在"非文本模态的特殊性"上有定义权。

## 六章地图

| 章 | 回答的问题 |
|---|---|
| [01 多模态系统的第一性](01_多模态系统的第一性.md) | 多模态到底给系统加了什么？（答案：一条经过采样与压缩的不可靠输入通道） |
| [02 感知管线与表征损失](02_感知管线与表征损失.md) | 输入如何进入系统？每一步预处理丢了什么？ |
| [03 跨模态上下文与状态](03_跨模态上下文与状态.md) | 截图、语音、DOM、工具返回如何合成一个可用的任务状态？ |
| [04 多模态评价与证据](04_多模态评价与证据.md) | "答案对了但看错了"如何被发现？感知/定位/对齐/推理四层错误怎么切分？ |
| [05 多模态生产系统](05_多模态生产系统.md) | 大对象、实时流、隐私、不可重放的输入如何生产化与降级？ |
| [06 多模态安全与反模式](06_多模态安全与反模式.md) | 像素和声波如何成为注入通道？多模态特有的坑长什么样？ |

## 全书的定律地基

本书反复调用七条 Law，先立在此处：[[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）|Law 6：压缩必然丢失定律]]（抽帧、转录、缩放都要定义并测量任务相关损失）、[[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）|Law 4：信息守恒定律]]（没被采集到的信息不能靠推理补成事实）、[[laws-of-ai-engineering/01_信息与压缩定律#Law 9 — 表征决定能力定律（Representation-Determines-Capability Law）|Law 9：表征决定能力定律]]（模型能处理什么取决于输入被怎样表征——这是全书的第一性锚点）、[[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）|Law 12：验证-生成不对称定律]]（多模态核验未必便宜，必须主动设计证据和验证器）、[[laws-of-ai-engineering/07_认识论与真理定律#Law 63 — 不确定性外显定律（Surface-Uncertainty Law）|Law 63：不确定性外显定律]]（看不清听不清必须显式说出）、[[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）|Law 87：一切输入皆指令定律]]（图像里的文字、语音里的话也是输入）、[[laws-of-ai-engineering/10_对抗与安全定律#Law 92 — 数据即攻击面定律（Data-Is-Attack-Surface Law）|Law 92：数据即攻击面定律]]（每多一种模态，攻击面多一个维度）。

## 这本书怎么用

做截图/语音/视频驱动的 Agent 前读 01、02、06；调不好"模型看不懂我的输入"读 02、03；评价多模态系统读 04；上生产读 05。全书遵循 100× 测试：**只写模型强 100 倍后仍然成立的结构性内容**——具体模型能看多清、听多准，本书一个字不写。
