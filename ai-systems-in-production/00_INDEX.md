---
type: book-index
aliases: [Production-INDEX]
date: 2026-07-07
abstraction_layer: 方法 + 原则（生产化层）
course: ai-systems-in-production
tags: [AI工程, 生产部署, MLOps, Serving, 可观测性, 知识库补充]
---

# 《AI Systems in Production》总索引

> 补齐知识库审计的 M4 缺失：**把系统真正跑在生产里的工程**。整套体系讲了怎么造（模式/架构）、怎么判断（评价）、怎么定制（训练）——这本讲怎么让它在真实流量、真实故障、真实账单下持续活着。
> 收束于统一体系：[[README|知识库总入口]] · 前置 [[laws-of-ai-engineering/00_INDEX|Laws]] 的系统/可靠性/经济家族 · 与 [[data-foundation-of-ai-systems/00_INDEX|Data Foundation]]（输入侧运维）、[[model-adaptation/04_蒸馏与部署|Model Adaptation Part 4]]（模型侧部署）互为接口。

> [!important] Laws 引用边界
> Production 主要引用 Laws 的系统、可靠性和经济家族：[[laws-of-ai-engineering/04_系统与控制定律#Law 36 — 可观测性定律（Observability Law）|Law 36：可观测性定律]]（看见系统才谈得上控制）、[[laws-of-ai-engineering/08_可靠性与失败定律#Law 70 — 墨菲定律（Murphy's Law）|Law 70：墨菲定律]]（长期运行必有故障）、[[laws-of-ai-engineering/08_可靠性与失败定律#Law 71 — 显式失败定律（Fail-Loudly Law）|Law 71：显式失败定律]] / [[laws-of-ai-engineering/08_可靠性与失败定律#Law 76 — 静默降级危险定律（Silent-Degradation-Danger Law）|Law 76：静默降级危险定律]]（失败必须可见）、[[laws-of-ai-engineering/08_可靠性与失败定律#Law 77 — 恢复优于预防定律（Recovery-Over-Prevention Law）|Law 77：恢复优于预防定律]]（回滚/恢复）、[[laws-of-ai-engineering/06_经济与资源定律#Law 56 — 成本结构决定架构定律（Cost-Structure-Shapes-Architecture Law）|Law 56：成本结构决定架构定律]]（成本是架构属性）。

> [!note] 版本状态：v1.0（2026-07-07）
> 直接按扩写标准写成——每 Part 含底层原则、工程手册、反例与边界、验收清单。数字均为经验量级示意，非测量值。

## 为什么这本书是独立的一层

Demo 和生产之间隔着一个学科。demo 证明"它能做到一次"，生产要求"它在最差的时刻也不失控"——面对对抗性输入、上游故障、流量峰值、供应商悄悄换模型、账单指数增长。整套知识库反复讲"能力是欺骗性的上限、可靠性才决定价值"（[[evaluation-of-ai-systems/00_INDEX|Evaluation]]），这本书就是那句话的基础设施形态。

LLM 系统的生产化还有一个传统软件没有的独特难题，贯穿全书：**它可以在返回 200 OK 的同时静默地错。** 传统监控（延迟/错误率）只覆盖"跑没跑"，不覆盖"对不对"——语义层的可观测性、质量的持续评价、"错误输出"型事故的响应，都是 LLM 生产工程的新增义务。

## 中心命题

**生产化的本质不是把 demo 加固，而是换一个质量定义：从"它能做到"换成"它在最差的时刻也可靠、可查、可回滚、可负担"。生产系统的质量由它的分布和最坏时刻定义，不由演示时刻定义。**

这句话对抗三个流行误区：生产化 = demo 加个 try/except（错，是另一套质量体系）、上线 = 项目结束（错，是运维责任的开始）、稳定 = 不动它（错，不动只会积累大爆炸，见 Part 4）。

## 六个 Part

| Part | 主题 | 核心问题 |
|------|------|---------|
| [[01_从Demo到生产]] | 生产化的第一性 | demo 和生产之间到底差什么？生产就绪怎么分级判定？ |
| [[02_Serving与延迟]] | Serving 与延迟 | 推理服务怎么组织？延迟怎么解剖和优化？容量与背压怎么设计？ |
| [[03_可观测性]] | 可观测性 | 四层监控怎么建？"200 OK 但内容错了"怎么被看见？ |
| [[04_发布与变更管理]] | 发布与变更 | prompt/模型/语料都是变更——怎么版本化、门禁、灰度、回滚？ |
| [[05_成本工程]] | 成本工程 | 成本结构长什么样？优化杠杆按什么顺序拉？护栏怎么设？ |
| [[06_故障与降级]] | 故障与降级 | LLM 系统怎么坏？降级链怎么设计？"错误输出"型事故怎么响应？ |

## 五条贯穿本书的生产定律（Laws 在生产层的投影）

1. **生产质量由分布与最坏时刻定义**（[[laws-of-ai-engineering/03_统计与泛化定律#Law 31 — 长尾定律（Long-Tail Law）|长尾定律]]、[[agent-decision-system/05_EVAL-CHECKLIST|Q-02]]）——报 P95/P99 和最坏情况，不报"平均挺好"。
2. **200 OK ≠ 正确**——LLM 系统必须有语义层监控；只看基础设施指标的系统在等待[[laws-of-ai-engineering/08_可靠性与失败定律#Law 76 — 静默降级危险定律（Silent-Degradation-Danger Law）|静默降级]]。
3. **一切都是变更**——代码、prompt、模型版本、工具、RAG 语料、采样参数，每一类都要版本化、过评测门禁、可回滚（[[laws-of-ai-engineering/00_INDEX|版本管理和回滚]]）。
4. **安全可用时受控降级，否则显式失败**（[[laws-of-ai-engineering/04_系统与控制定律#Law 42 — 优雅降级定律（Graceful-Degradation Law）|优雅降级]]、[[laws-of-ai-engineering/08_可靠性与失败定律#Law 71 — 显式失败定律（Fail-Loudly Law）|显式失败]]）——部分结果只有在安全、语义真实且仍有用时才值得保留；任何情况下都不能“编一个成功”。
5. **成本是架构属性，不是账单属性**（[[laws-of-ai-engineering/06_经济与资源定律#Law 56 — 成本结构决定架构定律（Cost-Structure-Shapes-Architecture Law）|成本结构决定架构]]）——上线后才优化成本，等于重做架构。

## 与其他书的关系

- **上承 [[textbook-zero-to-agent/10_安全与生产部署|教材第 10 章]]**：那里是生产工程的入门清单，本书是它的系统展开。
- **与 [[model-adaptation/04_蒸馏与部署|Model Adaptation Part 4]] 分工**：那里管"模型本体怎么部署划算"（自部署 TCO/量化/蒸馏），本书管"整个系统怎么在生产里运转"（serving 架构、监控、发布、故障）。
- **与 [[data-foundation-of-ai-systems/04_数据评价与漂移|Data Foundation Part 4]] 互补**：那里监控输入侧（数据漂移），本书监控系统与输出侧；告警设计的纪律（双基线、防疲劳、防古德哈特）两侧共用。
- **受 [[evaluation-of-ai-systems/00_INDEX|Evaluation]] 驱动**：发布门禁、在线质量监控、事故复盘，全部是持续评价的运行时形态。
- **反模式镜像**：[[ai-engineering-anti-patterns/06_工作流反模式|工作流反模式]]（无失败恢复、无检查点）与[[ai-engineering-anti-patterns/07_评价反模式|评价反模式]]（无评测上线、一次性评估即部署）是本书要在基础设施层杜绝的东西。
