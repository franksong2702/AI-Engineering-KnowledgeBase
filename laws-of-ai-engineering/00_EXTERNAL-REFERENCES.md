---
type: external-references
aliases: [LawsExternalReferences, Laws外部依据说明]
date: 2026-07-10
course: laws-of-ai-engineering
abstraction_layer: 运营机制（外部依据入口）
stability: 中（Core Laws 18 条已完成；全量 102 条待核验）
tags: [AI工程, Laws, 外部依据, citation, 研究入口]
---

# Laws 外部依据说明

> 这页是《The Laws of AI Engineering》的研究型 citation 入口。正文仍然优先服务日常阅读与工程调用；外部来源、支撑强度和转译边界集中放在这里。

相关入口：[[laws-of-ai-engineering/00_INDEX|Laws 总索引]] · [[00_CORE-LAWS|Core Laws]] · [[00_EXTERNAL-REFERENCE-POLICY|外部引用口径]] · [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core 18 核验记录]] · [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT|Pilot 10 条审计]]

## 使用原则

1. **正文保持干净**：不在每条 Law 正文里堆 citation。
2. **章节轻量指路**：每个 Law family 文件只放一个默认折叠的 citation 入口。
3. **本页承担严谨性**：来源类型、支撑强度、使用边界、不可过度声称的部分，都写在这里。
4. **未经核验不补来源**：没有完成外部核验的 Law，只标“待核验”，不假装已有 citation。

## Core Laws 核验状态

截至 2026-07-10，[[00_CORE-LAWS|18 条 Core Laws]] 已完成外部核验；“完成”表示每条都有来源、支撑强度与使用边界，不表示每条都被外部来源直接证明。

| 核验层级 | 数量 | Law |
|---|---:|---|
| 直接强支持 | 2 | 24, 26 |
| 底层强支持 + 工程转译 | 8 | 4, 6, 7, 14, 64, 87, 94, 102 |
| 综合命题 / 条件性原则 | 8 | 1, 12, 62, 74, 84, 86, 95, 100 |

逐条裁决、不能过度声称的部分和后续建议措辞见 [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core Laws 外部引用核验]]。

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
- `主要来源`: [DeepMind, Language Modeling Is Compression](https://deepmind.google/research/publications/39768/)；[TruthfulQA](https://openai.com/index/truthfulqa/)；[Cover and Thomas, Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X)
- `可支撑的说法`: 语言建模可从预测—压缩等价视角理解；参数生成不提供事实正确性保证，模型可以流畅地产生错误内容。
- `使用边界`: 不能写成“信息论已经证明 LLM 的所有幻觉都由有损压缩导致”。压缩视角、事实无保证和具体幻觉机制必须分开。
- `正文处理`: P2-B 已完成收窄；正文保留轻量依据与本节入口，不堆叠行内 citation。

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
- `主要来源`: [Shannon 1959, Coding Theorems for a Discrete Source With a Fidelity Criterion](https://gwern.net/doc/cs/algorithm/information/1959-shannon.pdf)；[Cover and Thomas, Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X)
- `可支撑的说法`: 有损编码用失真换取码率；压缩质量取决于失真度量和必须保留的信息。
- `使用边界`: “摘要、记忆、状态压缩会丢后续所需细节”是工程推论；可逆编码、充分统计量或没有丢失任务相关信息的结构化转换属于边界。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 7 — 分布证据边界定律

关联正文：[[01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）|Law 7：分布证据边界定律]]

- `依据类型`: 统计学习依据 + 工程转译
- `支撑强度`: 中-强
- `主要来源`: [Ben-David et al. 2010, A Theory of Learning from Different Domains](https://escholarship.org/uc/item/2nv1j9sc)
- `可支撑的说法`: 训练与测试分布差异会破坏原有泛化保证；跨域性能需要额外假设和证据。
- `使用边界`: “分布内”不等于“近乎可靠”；插值也可能失败，分布边界通常不可直接观察。更稳妥的工程表述是“分布内证据不能自动外推到分布外”。
- `正文处理`: ✅ 已于 2026-07-10 完成正典、Constitution、ADS 与主动正文的 P1-A 收窄；编号保留，heading 已迁移。

---

## 02 计算与验证定律

关联章节：[[02_计算与验证定律]]

### Law 12 — 验证-生成不对称定律

关联正文：[[02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）|Law 12：验证-生成不对称定律]]

- `依据类型`: 条件性计算原则 + 工程转译
- `支撑强度`: 中
- `主要来源`: [Clay Mathematics Institute, P vs NP](https://www.claymath.org/millennium/p-vs-np/)；[Cook 1971](https://doi.org/10.1145/800157.805047)；[Prover-Verifier Games](https://openai.com/index/prover-verifier-games-improve-legibility/)
- `可支撑的说法`: 某些问题存在可快速检查的证书；输出的可检查性可以被工程化改善。
- `使用边界`: NP 的定义不证明“一般任务中验证通常远比生成容易”，P vs NP 仍未解决。只有任务存在客观、廉价、独立验证器时，这个不对称才可直接用于委托设计。
- `正文处理`: ✅ 已于 2026-07-10 完成正典收窄与全库主动正文同步；见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|P0 改写影响审计]]。

### Law 14 — 误差累积定律

关联正文：[[02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）|Law 14：误差累积定律]]

- `依据类型`: 概率模型 + 工程转译
- `支撑强度`: 中-强
- `主要来源`: [AgentBench, ICLR 2024](https://arxiv.org/abs/2308.03688)；[METR, Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499)
- `可支撑的说法`: 长链路增加失败机会；长时任务可靠性需要单独测量。
- `使用边界`: `pⁿ` 只适用于独立、每步都必须成功且没有纠错的简化模型；真实步骤可能相关、可恢复或受反馈修正。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

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

### Law 62 — 流畅度非正确性定律

关联正文：[[07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）|Law 62：流畅度非正确性定律]]

- `依据类型`: 实证研究 + 综合判断
- `支撑强度`: 中
- `主要来源`: [Style Over Substance, COLING 2025](https://aclanthology.org/2025.coling-main.21/)；[TruthfulQA](https://openai.com/index/truthfulqa/)
- `可支撑的说法`: 评价者会受到风格影响，甚至偏好含事实错误但风格更好的答案；模型可以流畅地产生错误内容。
- `使用边界`: 不能声称流畅度与正确性在所有任务中统计独立或必然负相关。准确说法是：流畅、专业和自信不是正确性的充分证据，并可能掩盖错误。
- `正文处理`: P2-B 已完成收窄；正文改为“不是正确性的充分证据，并可能诱发评价偏差”。

### Law 64 — 可证伪性定律

关联正文：[[07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）|Law 64：可证伪性定律]]

- `依据类型`: 直接哲学依据 + 工程规范
- `支撑强度`: 中-强
- `主要来源`: [Popper, The Logic of Scientific Discovery](https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447)
- `可支撑的说法`: 可证伪性是 Popper 提出的科学划界标准；明确失败条件能提高经验性主张的可检验性。
- `使用边界`: 它不是所有知识唯一公认的定义；伦理规范、定义、数学命题和解释性框架需要不同评价方式。
- `正文处理`: ✅ 已于 2026-07-10 完成 P2-A 正典与主动正文收窄；保留 Law 64 编号与 heading，改为经验性工程主张的审计纪律。见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 改写影响审计]]。

---

## 08 可靠性与失败定律

关联章节：[[08_可靠性与失败定律]]

### Law 74 — 不可逆性定律

关联正文：[[08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）|Law 74：不可逆性定律]]

- `依据类型`: 决策理论 + 管理启发式
- `支撑强度`: 中
- `主要来源`: [Arrow and Fisher 1974](https://academic.oup.com/qje/article-abstract/88/2/312/1861520)；[Amazon 2015 shareholder letter](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/whitepapers/approved/executive-insights/2015-letter-to-shareholders.pdf)
- `可支撑的说法`: 不确定性与不可逆后果会提高保留选择权和谨慎决策的价值；可逆决策可采用更轻流程。
- `使用边界`: 决策速度不只由可逆性决定；影响大小、时间压力、信息价值和恢复成本同样重要。单向门/双向门首先是管理启发式，不是覆盖所有决策的数学定理。
- `正文处理`: 本轮不改正文；已列入后续措辞收窄清单。

---

## 09 人机与信任定律

关联章节：[[09_人机与信任定律]]

### Law 84 — 信任-可靠性剪刀差定律

关联正文：[[09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）|Law 84：信任-可靠性剪刀差定律]]

- `依据类型`: 综合判断
- `支撑强度`: 中
- `主要来源`: [Parasuraman and Riley 1997](https://web.mit.edu/16.459/www/parasuraman.pdf)；[Lee and See 2004](https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392)
- `可支撑的说法`: 自动化系统存在 misuse / overreliance 等人因风险；适当信任应与系统能力相匹配。
- `使用边界`: “信任-可靠性剪刀差”是本库综合命名；来源没有证明信任必然比可靠性增长更快。
- `正文处理`: ✅ 已于 2026-07-10 完成 P1-B 正典收窄与全库主动正文同步；保留“剪刀差”名称，但明确它是可测失配风险，不是必然增长曲线。见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 改写影响审计]]。

### Law 86 — 责任不可委托定律

关联正文：[[09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）|Law 86：责任不可委托定律]]

- `依据类型`: 治理规范 + 法律角色分配
- `支撑强度`: 中
- `主要来源`: [UNESCO AI Ethics Recommendation](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)；[OECD AI Principles](https://www.oecd.org/en/topics/ai-principles.html)；[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en)
- `可支撑的说法`: 最终责任与问责应可追溯到自然人或法人；责任应基于生命周期角色、语境和行动能力分配。
- `使用边界`: 不能把责任一律归给“部署者”。提供者、部署者、经营者、组织与专业人员可能承担不同义务；具体法律责任取决于司法辖区与场景。
- `正文处理`: ✅ 已于 2026-07-10 完成正典收窄与全库主动正文同步；见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|P0 改写影响审计]]。

---

## 10 对抗与安全定律

关联章节：[[10_对抗与安全定律]]

### Law 87 — 一切输入皆指令定律

关联正文：[[10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）|Law 87：一切输入皆指令定律]]

- `依据类型`: 新兴安全威胁模型
- `支撑强度`: 中-强
- `主要来源`: [Greshake et al. 2023](https://arxiv.org/abs/2302.12173)；[UK NCSC, Prompt injection is not SQL injection](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)
- `可支撑的说法`: 检索内容和外部数据中的文本可改变模型行为；当前 LLM 没有传统软件那样的代码/数据硬边界。
- `使用边界`: 准确含义是“所有进入上下文的内容都可能影响行为”，不是“所有输入都会被模型执行”。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 88 — 致命三重奏定律

关联正文：[[10_对抗与安全定律#Law 88 — 致命三重奏定律（Lethal-Trifecta Law）|Law 88：致命三重奏定律]]

- `依据类型`: 新兴 AI 安全威胁模型
- `支撑强度`: 中-强
- `主要来源`: [Simon Willison 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)；[OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)；[Design Patterns for Securing LLM Agents](https://arxiv.org/html/2506.08837v2)
- `可支撑的说法`: 私有数据访问、暴露机制、外部通信能力叠加后，会显著放大 prompt injection 与数据外泄风险。
- `使用边界`: “Lethal Trifecta”术语来源清晰，但这是新兴 AI 安全威胁模型，不是像 Goodhart 那样已有长期经典地位的定律。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 94 — 权限胜过自觉定律

关联正文：[[10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）|Law 94：权限胜过自觉定律]]

- `依据类型`: 直接安全工程依据 + AI 投影
- `支撑强度`: 中-强
- `主要来源`: [Saltzer and Schroeder 1975](https://web.mit.edu/Saltzer/www/publications/memos.html)；[NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
- `可支撑的说法`: 最小权限、故障安全默认值和完全仲裁能限制受损组件造成的后果；硬权限比行为提示更适合作为安全边界。
- `使用边界`: 权限不能解决错误授权、越权漏洞或输出层伤害；提示约束仍可作为纵深防御的一层，但不能替代权限控制。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

---

## 11 演化与元定律

关联章节：[[11_演化与元定律]]

### Law 95 — 能力-可靠性剪刀定律

关联正文：[[11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）|Law 95：能力-可靠性剪刀定律]]

- `依据类型`: 多维评价 + 本库综合判断
- `支撑强度`: 中
- `主要来源`: [HELM](https://crfm.stanford.edu/2022/11/17/helm.html)；[METR Task-Completion Time Horizons](https://metr.org/time-horizons/)
- `可支撑的说法`: 能力、校准、鲁棒性和可靠性是不同评价维度；新增、复杂和长时任务需要单独测成功概率。
- `使用边界`: 没有稳定证据证明“每一代能力增长都快于可靠性增长”；部分研究同时观察到可靠性和可完成任务长度改善。
- `正文处理`: ✅ 已于 2026-07-10 完成 P1-B 正典收窄与全库主动正文同步；保留编号与 heading，改为能力和可靠性分维度评价，不预设可靠性必然滞后。见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 改写影响审计]]。

### Law 96 — 任务重组定律

关联正文：[[11_演化与元定律#Law 96 — 任务重组定律（Task-Recomposition Law）|Law 96：任务重组定律]]

- `依据类型`: 任务型劳动经济学 + 工作场景实证 + 本库综合转译
- `支撑强度`: 中
- `主要来源`: [Autor 2015](https://doi.org/10.1257/jep.29.3.3)；[Acemoglu & Restrepo 2019](https://doi.org/10.1257/jep.33.2.3)；[Brynjolfsson, Li & Raymond 2023/2025](https://www.nber.org/papers/w31161)；[ILO 2025](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)
- `可支撑的说法`: 自动化会替代部分任务，也会与劳动互补、创造新任务，并对不同经验水平和职业产生不同影响；分析单位应落到任务而不是把岗位看成整体。
- `使用边界`: 这些来源不能证明“人的工作必然持续上移”或“执行层最终几乎完全由 AI 接管”。任务还可能消失、下沉、标准化、保持不变或重新组合。
- `正文处理`: ✅ 已于 2026-07-10 将“抽象上移定律”改为“任务重组定律”，保留 Law 96 编号并降为演化综合命题；见 [[_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT|Law 96 任务重组审计]]。

### Law 100 — 判断力稀缺定律

关联正文：[[11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）|Law 100：判断力稀缺定律]]

- `依据类型`: 生产率研究 + 认识论综合
- `支撑强度`: 中
- `主要来源`: [Noy and Zhang 2023](https://doi.org/10.1126/science.adh2586)；[Dell’Acqua et al., Jagged Technological Frontier](https://pubsonline.informs.org/doi/pdf/10.1287/orsc.2025.21838)
- `可支撑的说法`: 生成式 AI 能降低部分知识工作的生产成本；能力边界参差，使用者仍需识别任务边界并检查结果。
- `使用边界`: 这些研究不能证明判断力是“唯一”持续稀缺资源，也不能证明所有判断都无法自动化。本条是需持续验证的本库综合命题。
- `正文处理`: ✅ 已于 2026-07-10 完成 P1-C 正典收窄与全库主动正文同步；保留 Law 100 编号与 heading，改为需要按任务验证的条件性判断瓶颈，不再声称判断力是唯一持续稀缺资源。见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 改写影响审计]]。

### Law 102 — 定律有边界定律

关联正文：[[11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）|Law 102：定律有边界定律]]

- `依据类型`: 科学哲学 + 建模规范
- `支撑强度`: 中-强
- `主要来源`: [Box 1976, Science and Statistics](https://gwern.net/doc/statistics/decision/1976-box.pdf)；[Popper, The Logic of Scientific Discovery](https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447)
- `可支撑的说法`: 模型是现实的简化；经验性理论需要测试条件、适用域和被反驳的可能。
- `使用边界`: 这是一条建模与审查元原则，不是无条件数学定理；它要求包括自身在内的工程 Law 都声明边界。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。
