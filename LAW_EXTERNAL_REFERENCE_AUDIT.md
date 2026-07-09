---
type: external-reference-audit
abstraction_layer: 运营机制（外部引用核验）
date: 2026-07-09
course: laws-of-ai-engineering
status: pilot-10-completed
scope: Laws 理论依据字段 Pilot
pilot_laws: [1, 4, 6, 16, 24, 26, 39, 52, 84, 88]
tags: [AI工程, Laws, 外部引用, citation, 审计]
---

# Laws 外部引用核验 Pilot（10 条）

> 本文是外部 citation 项目的 Pilot。它只核验 10 条 Law 的“理论依据”字段，不直接改 102 条 Law 正文。
>
> 核心纪律：**未经核验不补 citation；外部来源支持到哪里，就只写到哪里。** 不把 AI Engineering 的工程转译伪装成论文直接结论。

相关口径：[[laws-of-ai-engineering/00_EXTERNAL-REFERENCE-POLICY|Laws 外部引用口径]] · [[01_编辑审计|编辑审计]] · [[laws-of-ai-engineering/00_REFERENCE-POLICY|Laws 引用策略]]

## 1. Pilot 选择原则

本轮 10 条不是“最好查的 10 条”，而是为了校准五种来源类型：

- 信息论硬理论：Law 1 / 4 / 6
- 可计算性理论类比：Law 16
- 经典社会科学 / 管理 / 经济定律：Law 24 / 39 / 52
- 概率预测与校准：Law 26
- 人因工程与自动化信任：Law 84
- 新兴 AI 安全威胁模型：Law 88

## 2. 支撑强度定义

| 支撑强度 | 含义 | 是否可直接补 citation |
|---|---|---:|
| 强 | 外部来源直接支持当前“理论依据”的核心命题 | 可以 |
| 中 | 外部来源支持底层理论，但 Law 的 AI 工程表达是转译 / 投影 / 综合 | 可以，但必须标明转译边界 |
| 弱 | 外部来源只提供背景或相邻概念 | 不建议直接补到正文 |
| 不支持 | 当前理论依据写法与来源不符或过度声称 | 需先改写理论依据 |

## 3. Pilot 审计表

| Law | 当前理论依据 | 来源类型 | 找到的外部来源 | 支撑强度 | Pilot 裁决 |
|---|---|---|---|---|---|
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）]] | 信息论：有损压缩的定义 | 工程转译依据 | [Shannon 1948](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)；[Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X) | 中 | 信息论依据强；“LLM 参数事实输出会幻觉”是 AI 工程转译。可补来源，但 citation 文案必须写成“信息论支持有损压缩边界”，不能写成“Shannon 证明 LLM 会幻觉”。 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）]] | 数据处理不等式：处理不能增加信息量 | 直接理论依据 + 工程转译 | [MIT Information Theory notes](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/5d8f16adc3385c9ff2975b121bd620e4_MIT6_441S16_course_notes.pdf)；[Polyanskiy and Wu notes](https://people.lids.mit.edu/yp/homepage/data/simple-IMA.pdf)；[Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X) | 中-强 | 数据处理不等式可支撑“处理不增加信息”；“prompt 不能凭空补外部事实”是工程转译。当前理论依据可保留，但建议补“工程转译”措辞。 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）]] | 信息论：无损压缩有理论下界，突破下界必有损 | 直接理论依据 + 工程转译 | [Shannon 1948](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)；[Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X) | 中-强 | 信息论能支撑“压缩有界 / 有损压缩会丢信息”；“摘要、状态压缩会丢后续所需细节”是工程转译。可补来源，但不能写成数学定理直接覆盖所有摘要策略。 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 16 — 不可预验证定律（Undecidability Law）]] | 可计算性理论：停机问题不可判定 | 类比依据 | [Turing 1936](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)；[Origins of the Halting Problem](https://www.sciencedirect.com/science/article/pii/S235222082100050X) | 中 | Turing/停机问题支撑“存在不可判定问题”；把它用于复杂 AI 任务的“事前不可完全验证”是类比 / 上界提醒，不是严格归约。正文若补 citation，应标“类比依据”。 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）]] | 控制论 / 经济学：Goodhart | 直接理论依据 | [Goodhart 1984 chapter](https://link.springer.com/chapter/10.1007/978-1-349-17295-5_4)；[CNA Goodhart report 2022](https://www.cna.org/reports/2022/09/Goodharts-Law-Recognizing-Mitigating-Manipulation-Measures-in-Analysis.pdf) | 强 | 这是最适合直接补 citation 的条目之一。Goodhart 原始来源 + 后续度量操纵综述能直接支撑当前理论依据。 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）]] | 概率论 / 预测评分：校准定义 | 直接理论依据 | [Brier 1950](https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml)；[Dawid 1982](https://fitelson.org/seminar/dawid.pdf) | 强 | 概率预测校准、Brier score、well-calibrated forecaster 都直接支持当前理论依据。可补 citation。 |
| [[laws-of-ai-engineering/04_系统与控制定律#Law 39 — 康威定律（Conway's Law）]] | 组织社会学：Conway | 直接理论依据 + AI 系统投影 | [Conway 1968](https://www.melconway.com/Home/pdf/committees.pdf)；[Conway HTML mirror](https://www.melconway.com/research/committees.html) | 中-强 | Conway 对“组织沟通结构影响系统设计”支撑强；用于多 Agent / 上下文边界是本库投影。建议 citation 写“Conway 来源 + AI 工程投影”。 |
| [[laws-of-ai-engineering/06_经济与资源定律#Law 52 — 边际定律（Marginal Law）]] | 经济学：边际分析 | 直接理论依据 + 工程转译 | [OpenStax Microeconomics Ch.2](https://openstax.org/books/principles-microeconomics-3e/pages/2-key-concepts-and-summary)；[OpenStax Economics Ch.7](https://openstax.org/books/principles-economics-3e/pages/7-key-concepts-and-summary) | 中-强 | 边际分析来源可靠；“AI 系统继续堆模型/上下文/采样的边际收益递减”是工程转译。可补来源并标“经济学转译”。 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）]] | 人因工程：自动化偏见 / 过度信任 | 综合判断 | [Parasuraman and Riley 1997](https://web.mit.edu/16.459/www/parasuraman.pdf)；[SAGE article page](https://journals.sagepub.com/doi/10.1518/001872097778543886) | 中 | 自动化 misuse / overreliance 来源强；“信任-可靠性剪刀差”是本库综合命名。可以补人因工程来源，但要标为“综合判断”，不要说该论文提出剪刀差定律。 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 88 — 致命三重奏定律（Lethal-Trifecta Law）]] | 安全工程：攻击链分析 | 新兴 AI 安全威胁模型 | [Simon Willison 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)；[OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)；[Design Patterns for Securing LLM Agents](https://arxiv.org/html/2506.08837v2) | 中-强 | “Lethal Trifecta”术语来源清晰；OWASP 和 agent security 论文支撑 prompt injection / tool access / sensitive data 风险链。适合补 citation，但要标为新兴威胁模型，不是长期经典定律。 |

## 4. Pilot 总结

### 可以直接进入 citation 的条目

- Law 24 — 古德哈特定律
- Law 26 — 校准定律

这两条的外部来源和当前理论依据几乎同构，风险低。

### 可以补 citation，但必须标转译边界

- Law 1 — 有损压缩
- Law 4 — 信息守恒 / 数据处理不等式
- Law 6 — 压缩必然丢失
- Law 39 — 康威定律
- Law 52 — 边际定律
- Law 84 — 信任-可靠性剪刀差
- Law 88 — 致命三重奏

这些条目的底层来源强，但 AI Engineering 里的 Law 表述是工程转译、投影或综合命名。

### 不应直接硬补为“论文证明”的条目

- Law 16 — 不可预验证定律

Turing / 停机问题是强理论来源，但当前 Law 用法是类比，不是严格证明 AI 任务无法预验证。若补 citation，必须写为“类比依据”。

## 5. 对全量项目的建议

1. 不要直接给 102 条 Law 全部加 citation。
2. 先在 10 条 Pilot 基础上确定正文格式。
3. 推荐新增一种正文段落，而不是塞进现有“理论依据”句子里：

```markdown
**外部依据**：直接依据 / 工程转译 / 类比依据 / 综合判断。来源：...
```

4. 全量推进时按 family 批次做，每批完成后跑 `kb_health_check.py`。
5. 如果某条 Law 的理论依据只能找到弱来源，应保留为“本库综合判断”，不要补弱 citation。

## 6. 本轮不改正文声明

本 Pilot 没有修改任何 Law 正文，只完成来源核验和引用口径校准。是否把 citation 写进 102 条 Law，需要另行授权。
