---
type: external-references
aliases: [LawsExternalReferences, Laws外部依据说明]
date: 2026-07-09
course: laws-of-ai-engineering
abstraction_layer: 运营机制（外部依据入口）
stability: 中（Pilot 10 条已完成；全量 102 条待核验）
tags: [AI工程, Laws, 外部依据, citation, 研究入口]
---

# Laws 外部依据说明

> 这页是《The Laws of AI Engineering》的研究型 citation 入口。正文仍然优先服务日常阅读与工程调用；外部来源、支撑强度和转译边界集中放在这里。

相关入口：[[laws-of-ai-engineering/00_INDEX|Laws 总索引]] · [[00_EXTERNAL-REFERENCE-POLICY|外部引用口径]] · [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT|Pilot 审计记录]]

## 使用原则

1. **正文保持干净**：不在每条 Law 正文里堆 citation。
2. **章节轻量指路**：每个 Law family 文件只放一个默认折叠的 citation 入口。
3. **本页承担严谨性**：来源类型、支撑强度、使用边界、不可过度声称的部分，都写在这里。
4. **未经核验不补来源**：没有完成外部核验的 Law，只标“待核验”，不假装已有 citation。

## 支撑强度说明

- **强**：外部来源直接支持当前理论依据的核心命题。
- **中-强**：底层来源强，但 AI Engineering 表达包含工程转译或投影。
- **中**：外部来源支持相邻理论或底层类比，当前 Law 是本库综合表达。
- **弱 / 不支持**：暂不进入正式 citation；先回到审计阶段。

---

## 01 信息与压缩定律

关联章节：[[01_信息与压缩定律]]

### Law 1 — 有损压缩定律

关联正文：[[01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）|Law 1：有损压缩定律]]

- `依据类型`: 工程转译依据
- `支撑强度`: 中
- `主要来源`: [Shannon 1948, A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)；[Cover and Thomas, Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X)
- `可支撑的说法`: 信息论支持“表达/编码/压缩会受到信息保留与失真的约束”。
- `使用边界`: 不能写成“Shannon 证明 LLM 会幻觉”。LLM 事实性输出与幻觉治理是本书把信息论边界转译到 AI 工程后的表达。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 4 — 信息守恒定律

关联正文：[[01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）|Law 4：信息守恒定律]]

- `依据类型`: 直接理论依据 + 工程转译
- `支撑强度`: 中-强
- `主要来源`: [MIT Information Theory notes](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/5d8f16adc3385c9ff2975b121bd620e4_MIT6_441S16_course_notes.pdf)；[Polyanskiy and Wu notes](https://people.lids.mit.edu/yp/homepage/data/simple-IMA.pdf)；[Cover and Thomas, Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X)
- `可支撑的说法`: 数据处理不等式支持“处理过程不能凭空增加源中不存在的信息”。
- `使用边界`: “prompt 不能凭空补外部事实”是工程转译，不是信息论教材中的原句。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 6 — 压缩必然丢失定律

关联正文：[[01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）|Law 6：压缩必然丢失定律]]

- `依据类型`: 直接理论依据 + 工程转译
- `支撑强度`: 中-强
- `主要来源`: [Shannon 1948, A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)；[Cover and Thomas, Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X)
- `可支撑的说法`: 信息论支持“无损压缩有理论下界；有损压缩通过牺牲部分信息换取更高压缩率”。
- `使用边界`: “摘要、记忆、状态压缩会丢后续所需细节”是工程推论；不能把所有摘要策略都说成被同一数学定理直接覆盖。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 02 计算与验证定律

关联章节：[[02_计算与验证定律]]

### Law 16 — 不可预验证定律

关联正文：[[02_计算与验证定律#Law 16 — 不可预验证定律（Undecidability Law）|Law 16：不可预验证定律]]

- `依据类型`: 类比依据
- `支撑强度`: 中
- `主要来源`: [Turing 1936, On Computable Numbers](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)；[Origins of the Halting Problem](https://www.sciencedirect.com/science/article/pii/S235222082100050X)
- `可支撑的说法`: 可计算性理论支持“存在无法用通用程序事前判定的计算问题”。
- `使用边界`: 本 Law 用停机问题提醒复杂 AI 任务存在事前验证边界，但不是把所有 AI 任务严格归约为停机问题。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 03 统计与泛化定律

关联章节：[[03_统计与泛化定律]]

### Law 24 — 古德哈特定律

关联正文：[[03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）|Law 24：古德哈特定律]]

- `依据类型`: 直接理论依据
- `支撑强度`: 强
- `主要来源`: [Goodhart 1984 chapter](https://link.springer.com/chapter/10.1007/978-1-349-17295-5_4)；[CNA Goodhart report 2022](https://www.cna.org/reports/2022/09/Goodharts-Law-Recognizing-Mitigating-Manipulation-Measures-in-Analysis.pdf)
- `可支撑的说法`: 当指标被用作目标时，会被优化压力改变其原本的测量意义。
- `使用边界`: 可以直接作为理论来源；但具体到 AI 评价、reward hacking、benchmark gaming 时，仍要说明场景转译。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 26 — 校准定律

关联正文：[[03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）|Law 26：校准定律]]

- `依据类型`: 直接理论依据
- `支撑强度`: 强
- `主要来源`: [Brier 1950](https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml)；[Dawid 1982](https://fitelson.org/seminar/dawid.pdf)
- `可支撑的说法`: 概率预测质量不仅取决于是否给出答案，也取决于置信度是否与实际频率匹配。
- `使用边界`: Brier score 与 well-calibrated forecaster 可以支撑校准概念；具体到 LLM 置信表达仍需工程评价设计。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 04 系统与控制定律

关联章节：[[04_系统与控制定律]]

### Law 39 — 康威定律

关联正文：[[04_系统与控制定律#Law 39 — 康威定律（Conway's Law）|Law 39：康威定律]]

- `依据类型`: 直接理论依据 + AI 系统投影
- `支撑强度`: 中-强
- `主要来源`: [Conway 1968, How Do Committees Invent?](https://www.melconway.com/Home/pdf/committees.pdf)；[Conway HTML mirror](https://www.melconway.com/research/committees.html)
- `可支撑的说法`: 组织沟通结构会影响系统设计结构。
- `使用边界`: 多 Agent 分工、上下文边界、团队协作结构是本库把 Conway 定律投影到 AI 工程后的表达。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 05 接口与边界定律

关联章节：[[05_接口与边界定律]]

本章尚未完成外部来源核验。引用入口先保留，后续全量核验时再补充具体 Law。

---

## 06 经济与资源定律

关联章节：[[06_经济与资源定律]]

### Law 52 — 边际定律

关联正文：[[06_经济与资源定律#Law 52 — 边际定律（Marginal Law）|Law 52：边际定律]]

- `依据类型`: 直接理论依据 + 工程转译
- `支撑强度`: 中-强
- `主要来源`: [OpenStax Microeconomics Ch.2](https://openstax.org/books/principles-microeconomics-3e/pages/2-key-concepts-and-summary)；[OpenStax Economics Ch.7](https://openstax.org/books/principles-economics-3e/pages/7-key-concepts-and-summary)
- `可支撑的说法`: 理性决策应比较边际收益与边际成本，而不是只看总量或沉没投入。
- `使用边界`: “继续堆模型、上下文、采样、工具的边际收益递减”是经济学边际分析在 AI 系统中的工程转译。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 07 认识论与真理定律

关联章节：[[07_认识论与真理定律]]

本章尚未完成外部来源核验。引用入口先保留，后续全量核验时再补充具体 Law。

---

## 08 可靠性与失败定律

关联章节：[[08_可靠性与失败定律]]

本章尚未完成外部来源核验。引用入口先保留，后续全量核验时再补充具体 Law。

---

## 09 人机与信任定律

关联章节：[[09_人机与信任定律]]

### Law 84 — 信任-可靠性剪刀差定律

关联正文：[[09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）|Law 84：信任-可靠性剪刀差定律]]

- `依据类型`: 综合判断
- `支撑强度`: 中
- `主要来源`: [Parasuraman and Riley 1997](https://web.mit.edu/16.459/www/parasuraman.pdf)；[SAGE article page](https://journals.sagepub.com/doi/10.1518/001872097778543886)
- `可支撑的说法`: 自动化系统存在 misuse / overreliance 等人因风险。
- `使用边界`: “信任-可靠性剪刀差”是本库综合命名；不能说 Parasuraman and Riley 提出了这条 Law。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 10 对抗与安全定律

关联章节：[[10_对抗与安全定律]]

### Law 88 — 致命三重奏定律

关联正文：[[10_对抗与安全定律#Law 88 — 致命三重奏定律（Lethal-Trifecta Law）|Law 88：致命三重奏定律]]

- `依据类型`: 新兴 AI 安全威胁模型
- `支撑强度`: 中-强
- `主要来源`: [Simon Willison 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)；[OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)；[Design Patterns for Securing LLM Agents](https://arxiv.org/html/2506.08837v2)
- `可支撑的说法`: 私有数据访问、暴露机制、外部通信能力叠加后，会显著放大 prompt injection 与数据外泄风险。
- `使用边界`: “Lethal Trifecta”术语来源清晰，但这是新兴 AI 安全威胁模型，不是像 Goodhart 那样已有长期经典地位的定律。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 11 演化与元定律

关联章节：[[11_演化与元定律]]

本章尚未完成外部来源核验。引用入口先保留，后续全量核验时再补充具体 Law。

