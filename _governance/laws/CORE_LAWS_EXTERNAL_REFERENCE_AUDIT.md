---
type: external-reference-audit
aliases: [CoreLawsExternalReferenceAudit, Core Laws 外部核验]
abstraction_layer: 运营机制（核心定律外部核验）
date: 2026-07-10
updated: 2026-07-10
course: laws-of-ai-engineering
status: core-18-p0-p1ab-rewritten
scope: Core Laws 18 条理论依据与表述边界
audited_laws: [1, 4, 6, 7, 12, 14, 24, 26, 62, 64, 74, 84, 86, 87, 94, 95, 100, 102]
tags: [AI工程, Laws, CoreLaws, 外部引用, citation, 审计]
---

# Core Laws 外部引用核验（18 条）

> 本文核验 [[laws-of-ai-engineering/00_CORE-LAWS|18 条 Core Laws]] 的外部依据与表述边界。它是研究与主编审计记录，不是新的 Law 正典。
>
> 原始核验轮**没有修改 11 个 Law family 正文**。正式 citation 进入 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCES|Laws 外部依据说明]]；后续获授权的正典收窄状态记录如下。

> [!success] 后续执行状态（2026-07-10）
> P0 的 Law 12 / Law 86，以及 P1-A/B 的 Law 7 / Law 84 / Law 95，已完成正典收窄与全库影响修复，详见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|Core Laws P0 改写影响审计]]、[[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|Core Laws P1 改写影响审计]]。下表保留核验时发现的问题；P1-C 的 Law 100 与 P2 仍未执行。

相关口径：[[laws-of-ai-engineering/00_EXTERNAL-REFERENCE-POLICY|外部引用口径]] · [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT|Pilot 10 条审计]] · [[laws-of-ai-engineering/00_REFERENCE-POLICY|Laws 引用策略]]

## 1. 总结论

18 条 Core Laws 的工程价值依然成立，但它们的认识论硬度不同：

| 核验层级 | 数量 | Law | 含义 |
|---|---:|---|---|
| 直接强支持 | 2 | 24, 26 | 外部来源与当前核心命题基本同构 |
| 底层强支持 + 工程转译 | 8 | 4, 6, 7, 14, 64, 87, 94, 102 | 来源支持底层理论；AI Engineering 表达需要明确转译边界 |
| 综合命题 / 条件性原则 | 8 | 1, 12, 62, 74, 84, 86, 95, 100 | 有可靠组成证据，但当前名称、普遍性或因果解释来自本库综合判断 |

这意味着：**Core 不等于全部都是数学定理；Core 表示它们是全库最值得优先引用的约束。**

## 2. 18 条核验矩阵

| Law | 核验结论 | 依据类型 | 主要来源 | 外部来源能支持什么 | 不能过度声称什么 | 建议措辞 |
|---|---|---|---|---|---|---|
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] | 部分支持 | 工程转译 + 综合判断 | [DeepMind: Language Modeling Is Compression](https://deepmind.google/research/publications/39768/)；[TruthfulQA](https://openai.com/index/truthfulqa/) | 语言建模可从预测—压缩等价视角理解；参数生成不保证事实正确 | 不能说信息论已经证明“LLM 的所有幻觉都由有损压缩导致” | 语言模型可视为压缩式预测器；其生成不是有来源保证的事实查询，事实输出仍需外部锚定 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）\|Law 4]] | 中-强支持 | 直接理论依据 + 工程转译 | [MIT Information Theory notes](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/5d8f16adc3385c9ff2975b121bd620e4_MIT6_441S16_course_notes.pdf)；[Polyanskiy and Wu notes](https://people.lids.mit.edu/yp/homepage/data/simple-IMA.pdf) | 数据处理不等式限制处理后关于源变量的互信息 | 参数知识、逻辑推导和前提中的隐含信息都属于可用信息；“新句子”不等于违反守恒 | 处理不能凭空增加关于未知外部事实的证据；缺信息时应引入数据源，而不是只改提示词 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]] | 中-强支持 | 直接理论依据 + 工程转译 | [Shannon 1959: Coding Theorems for a Discrete Source With a Fidelity Criterion](https://gwern.net/doc/cs/algorithm/information/1959-shannon.pdf)；[Elements of Information Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/047174882X) | 有损编码用失真换取码率；压缩质量依赖保留目标与失真度量 | 不能说所有更短表示都必然丢失任务相关信息；可逆编码和充分统计量是边界 | 当摘要不可逆地缩短表示时，必须显式定义要保留的信息，并验证任务相关失真 |
| [[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）\|Law 7]] | 中-强支持；P1-A 已完成收窄 | 统计学习依据 + 工程转译 | [Ben-David et al. 2010: A Theory of Learning from Different Domains](https://escholarship.org/uc/item/2nv1j9sc) | 训练与测试分布差异会破坏原有泛化保证；跨域性能需要额外假设和证据 | “分布内”不等于“近乎可靠”；插值也可能失败，分布边界通常不可直接观察 | 分布内评测证据不能自动外推到分布外；分布变化时必须重新评测可靠性 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]] | 部分支持，需明显收窄 | 条件性计算原则 + 工程转译 | [Clay Mathematics Institute: P vs NP](https://www.claymath.org/millennium/p-vs-np/)；[Cook 1971](https://doi.org/10.1145/800157.805047)；[Prover-Verifier Games](https://openai.com/index/prover-verifier-games-improve-legibility/) | 某些问题存在可快速检查的证书；输出的可检查性可以被工程化改善 | NP 的定义不证明“一般任务中验证通常远比生成容易”；P vs NP 仍未解决，开放式任务可能没有廉价验证器 | 当任务有客观、廉价、独立的验证器时，生成—验证分工有优势；没有验证器时不能套用 |
| [[laws-of-ai-engineering/02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）\|Law 14]] | 中-强支持 | 概率模型 + 工程转译 | [AgentBench, ICLR 2024](https://arxiv.org/abs/2308.03688)；[METR: Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499) | 长链路增加失败机会；长时任务可靠性需要单独测量 | `pⁿ` 只适用于独立、每步都必须成功且没有纠错的简化模型；真实步骤可能相关或可恢复 | 未验证链路越长，端到端失败机会通常越多；用检查点、反馈和回滚测实际轨迹可靠性 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24]] | 强支持 | 直接理论依据 | [Goodhart 1984](https://link.springer.com/chapter/10.1007/978-1-349-17295-5_4)；[CNA Goodhart report](https://www.cna.org/reports/2022/09/Goodharts-Law-Recognizing-Mitigating-Manipulation-Measures-in-Analysis.pdf) | 代理指标受到优化压力后可能与真实目标脱钩 | 不能泛化为“所有指标都会失效”或“只要优化就必然立刻失真” | 当代理指标承受优化压力时，持续监测它与真实目标的脱钩和被操纵空间 |
| [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]] | 强支持 | 直接理论依据 | [Brier 1950](https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml)；[Dawid 1982](https://fitelson.org/seminar/dawid.pdf) | 概率预测的置信分组应与长期经验频率匹配 | 让 LLM 自报一个百分比并不会自动得到校准概率 | 只有经过样本级评测的置信信号才能用于风险路由和人工转交 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）\|Law 62]] | 部分支持 | 实证研究 + 综合判断 | [Style Over Substance, COLING 2025](https://aclanthology.org/2025.coling-main.21/)；[TruthfulQA](https://openai.com/index/truthfulqa/) | 评价者会受到风格影响，甚至偏好含事实错误但风格更好的答案；模型可流畅地产生错误内容 | 不能说流畅度与正确性在所有任务中统计独立或必然负相关 | 流畅、专业和自信不是正确性的充分证据，并可能使错误更难被发现 |
| [[laws-of-ai-engineering/07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）\|Law 64]] | 中-强支持，但属于哲学立场 | 直接哲学依据 + 工程规范 | [Popper: The Logic of Scientific Discovery](https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447) | 可证伪性是 Popper 提出的科学划界标准；可检验失败条件能提高主张的信息价值 | 不能把它写成所有知识唯一公认的定义；伦理规范、定义和解释性框架不完全适用 | 对经验性工程主张，应说明什么观察会使它失效；把可证伪性作为审计纪律而非唯一知识哲学 |
| [[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）\|Law 74]] | 部分支持 | 决策理论 + 管理启发式 | [Arrow and Fisher 1974](https://academic.oup.com/qje/article-abstract/88/2/312/1861520)；[Amazon 2015 shareholder letter](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/whitepapers/approved/executive-insights/2015-letter-to-shareholders.pdf) | 不确定性与不可逆后果会提高保留选择权和谨慎决策的价值；可逆决策可采用更轻流程 | “决策速度只由可逆性决定”不是通用决策定理；影响大小、时间压力和信息价值也重要 | 在不确定性高且恢复成本大的操作上提高审批和验证；低成本可逆操作可采用轻量流程 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84]] | 部分支持；P1-B 已完成收窄 | 人因工程 + 本库综合命名 | [Parasuraman and Riley 1997](https://web.mit.edu/16.459/www/parasuraman.pdf)；[Lee and See 2004](https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392) | 自动化会发生误用、弃用和过度依赖；适当信任应与系统能力相匹配 | 外部来源没有证明“信任必然比可靠性增长更快”；剪刀差名称是本库综合表达 | 感知能力可能使信任超过实测可靠性；应以评测、监控和失败反馈校准授权范围 |
| [[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] | 原则受支持，但责任主体表述过窄 | 治理规范 + 法律角色分配 | [UNESCO AI Ethics Recommendation](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)；[OECD AI Principles](https://www.oecd.org/en/topics/ai-principles.html)；[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en) | 最终责任与问责应可追溯到自然人或法人；责任按生命周期角色、语境和能力分配 | 不能说责任“永远只在部署者”；提供者、部署者、经营者、组织与专业人员可能承担不同义务 | 不能把 AI 当作最终问责主体；必须按角色和法律语境把责任明确分配给可问责的人或组织 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）\|Law 87]] | 中-强支持 | 新兴安全威胁模型 | [Greshake et al. 2023](https://arxiv.org/abs/2302.12173)；[UK NCSC: Prompt injection is not SQL injection](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) | 检索内容和外部数据中的文本可改变模型行为；当前模型没有传统代码/数据硬边界 | “所有输入都会被执行”过强；准确说法是所有进入上下文的内容都可能影响行为 | 把所有不可信上下文视为潜在指令通道，并以权限、隔离和结果验证限制影响 |
| [[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）\|Law 94]] | 中-强支持 | 直接安全工程依据 + AI 投影 | [Saltzer and Schroeder 1975](https://web.mit.edu/Saltzer/www/publications/memos.html)；[NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) | 最小权限、故障安全默认值和完全仲裁能限制受损组件造成的后果 | 权限并不能解决错误授权、越权漏洞或输出层伤害；提示约束仍可作为纵深防御 | 用最小权限和强制仲裁限制真实动作；把提示约束视为缓解层，不视为安全边界 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）\|Law 95]] | 部分支持；P1-B 已完成收窄 | 多维评价 + 本库综合判断 | [HELM](https://crfm.stanford.edu/2022/11/17/helm.html)；[METR Task-Completion Time Horizons](https://metr.org/time-horizons/) | 能力、校准、鲁棒性、可靠性是不同维度；复杂和长时任务需要单独测成功概率 | 没有稳定证据证明“每一代能力增长都快于可靠性增长”；部分研究也观察到可靠性同步改善 | 能力提升不保证可靠性按比例提升；对新增能力和任务前沿必须重新评测稳定性 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）\|Law 100]] | 综合命题，有间接实证 | 生产率研究 + 认识论综合 | [Noy and Zhang 2023](https://doi.org/10.1126/science.adh2586)；[Dell’Acqua et al.: Jagged Technological Frontier](https://pubsonline.informs.org/doi/pdf/10.1287/orsc.2025.21838) | 生成式 AI 能降低部分知识工作的生产成本；能力边界参差，使用者仍需识别任务边界和检查结果 | 不能证明判断力是“唯一”持续稀缺资源，也不能证明所有判断都无法自动化 | 当生成成本下降时，目标选择、证据判断和风险取舍可能成为新瓶颈；这是需持续验证的工程判断 |
| [[laws-of-ai-engineering/11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）\|Law 102]] | 中-强支持 | 科学哲学 + 建模规范 | [Box 1976: Science and Statistics](https://gwern.net/doc/statistics/decision/1976-box.pdf)；[Popper: The Logic of Scientific Discovery](https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447) | 模型是对现实的简化；经验性理论需要测试条件、适用域和被反驳的可能 | 不能把这条元原则本身包装成无条件数学定理 | 把适用范围、反例和失效条件视为 Law 正文的一部分；超出边界时停止引用 |

## 3. P0 与 P1-A/B 已完成、P1-C/P2 仍待后续裁决的 10 条

本轮没有改正文，但外部核验已经足以把下面 10 条列为后续高优先级措辞审查：

| 优先级 | Law | 当前主要问题 | 后续动作 |
|---|---|---|---|
| P0 ✅ | Law 12 | 从 NP 的条件性验证器推广到“通常所有验证都更容易” | 已收窄到“存在客观、廉价、独立验证器的任务”；见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT\|影响审计]] |
| P0 ✅ | Law 86 | 把角色分布式责任写成“始终由部署者负责” | 已改为自然人/法人可问责，按角色与语境分配；见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT\|影响审计]] |
| P1 ✅ | Law 7 | “分布内近乎可靠”强于统计学习来源 | 已改为“可靠性证据有分布边界”，并同步 Constitution / ADS / Case；见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT\|P1 影响审计]] |
| P1 ✅ | Law 84 | 把过度信任风险写成必然增长速率 | 已改为可测的信任/授权校准失配，并纳入过度信任与信任不足两种方向 |
| P1 ✅ | Law 95 | “能力增长快于可靠性”缺少稳定纵向证据 | 已改为能力与可靠性分维度评价；能力提升不证明可靠性同步，也不预设可靠性滞后 |
| P1 | Law 100 | “判断力唯一持续稀缺”是本库主张而非实证定律 | 标为综合判断并保留可证伪边界 |
| P2 | Law 1 | 压缩视角与幻觉因果链混写 | 区分“压缩视角”“事实无保证”“幻觉机制” |
| P2 | Law 62 | “与正确性无关/甚至负相关”过于绝对 | 改为“不是充分证据，且可诱发评价偏差” |
| P2 | Law 64 | 把 Popper 的划界标准写成唯一知识定义 | 改为经验性工程主张的审计纪律 |
| P2 | Law 74 | 将管理启发式写成覆盖所有决策的强规律 | 加入不确定性、恢复成本、影响和时间压力条件 |

## 4. 本轮裁决

1. Core Laws 的引用优先级继续保留；本轮没有理由删除 18 条中的任何一条。
2. “核心级”表示全库引用价值，不表示 18 条拥有相同的科学硬度。
3. 正式 citation 已集中写入 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCES|Laws 外部依据说明]]；Law family 正文继续保持轻量。
4. Law 12、Law 86、Law 7、Law 84 与 Law 95 已完成；下一轮单独处理 Law 100，禁止将剩余条目一次性机械替换。
5. 全量 102 条核验仍是可选长期项目；Core 18 完成不等于全量项目完成。

## 5. 原始核验轮停手条件

- [x] 18/18 条都有核验结论
- [x] 18/18 条都有至少一个主要来源
- [x] 18/18 条都有外部来源支持边界
- [x] 18/18 条都有建议措辞
- [x] 未修改 11 个 Law family 正文
