---
type: external-references
aliases: [LawsExternalReferences, Laws外部依据说明]
date: 2026-07-10
course: laws-of-ai-engineering
abstraction_layer: 运营机制（外部依据入口）
stability: 中（已核验 41/102；其余按风险排序推进）
tags: [AI工程, Laws, 外部依据, citation, 研究入口]
---

# Laws 外部依据说明

> 这页是《The Laws of AI Engineering》的研究型 citation 入口。正文仍然优先服务日常阅读与工程调用；外部来源、支撑强度和转译边界集中放在这里。

相关入口：[[laws-of-ai-engineering/00_INDEX|Laws 总索引]] · [[00_CORE-LAWS|Core Laws]] · [[00_EXTERNAL-REFERENCE-POLICY|外部引用口径]] · [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core 18 核验记录]] · [[_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT|非 Core 风险排序核验]] · [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT|Pilot 10 条审计]]

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

## 全库核验进度

合并 Pilot、Core、Law 96 与本轮风险排序批次并按 Law 编号去重后，已核验 **41/102 条**。本轮新增 18 条非 Core 高影响 Law，选择与正文裁决见 [[_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT|风险排序外部核验]]。剩余 61 条不是“遗漏待清零”，而是后续按引用影响与主张风险重新排序的候选池。

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

### Law 2 — 上下文即状态定律

关联正文：[[01_信息与压缩定律#Law 2 — 上下文即状态定律（Context-is-State Law）|Law 2：上下文即状态定律]]

- `依据类型`: 模型架构事实 + 系统工程转译
- `支撑强度`: 中
- `主要来源`: [Vaswani et al. 2017, Attention Is All You Need](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- `可支撑的说法`: 标准请求式 Transformer 推理只直接使用当前调用提供的输入；跨调用连续性需要由系统保存、检索并重新提供状态。
- `使用边界`: 不能写成“所有模型永远无状态”或“上下文窗口是系统唯一状态”。服务端会话、外部记忆、缓存、工具与在线学习都可能持有状态；本 Law 约束的是调用边界上的显式状态管理。
- `正文处理`: 本轮收窄为架构条件，不再把特定部署方式写成所有 AI 系统的数学硬规律。

### Law 3 — 信噪比定律

关联正文：[[01_信息与压缩定律#Law 3 — 信噪比定律（Signal-to-Noise Law）|Law 3：信噪比定律]]

- `依据类型`: 长上下文实证 + 工程原则
- `支撑强度`: 中
- `主要来源`: [Liu et al. 2024, Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/)
- `可支撑的说法`: 长上下文中信息的位置、相关性与干扰会影响任务表现；增加上下文并不自动增加可用证据。
- `使用边界`: softmax 归一化不能证明“每个新增 token 都必然降低质量”。相关补充信息可能改善结果；是否有害必须在目标任务、模型和上下文构造上测量。
- `正文处理`: 本轮删除“数学证明、必然稀释、几乎无例外”等过强表述。

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
- `正文处理`: ✅ 已于 2026-07-10 完成正式定义、Constitution、ADS 与主动正文的 P1-A 收窄；编号保留，heading 已迁移。

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
- `正文处理`: ✅ 已于 2026-07-10 完成正式定义收窄与全库主动正文同步；见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|P0 改写影响审计]]。

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

### Law 21 — 停机与预算定律

关联正文：[[02_计算与验证定律#Law 21 — 停机与预算定律（Termination-Budget Law）|Law 21：停机与预算定律]]

- `依据类型`: 可计算性边界 + 生产系统护栏
- `支撑强度`: 中-强
- `主要来源`: [Turing 1936, On Computable Numbers](https://doi.org/10.1112/plms/s2-42.1.230)；[Google SRE, Handling Overload](https://sre.google/sre-book/handling-overload/)
- `可支撑的说法`: 不存在能为所有程序普遍判定停机的算法；生产系统需要用截止时间、预算、取消和过载控制限制无界工作。
- `使用边界`: 停机问题不直接证明“每个循环都必须设置同一种固定最大步数”，也不能替系统选择正确预算。长期服务可持续运行，但每个工作单元仍应有资源与取消边界。
- `正文处理`: 本轮从“停机问题的直接硬定律”降为有理论背景的工程护栏。

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

### Law 25 — 分布漂移定律

关联正文：[[03_统计与泛化定律#Law 25 — 分布漂移定律（Distribution Shift Law）|Law 25：分布漂移定律]]

- `依据类型`: 统计学习理论 + 生产监控转译
- `支撑强度`: 中-强
- `主要来源`: [Ben-David et al. 2010, A Theory of Learning from Different Domains](https://proceedings.mlr.press/v9/david10a.html)
- `可支撑的说法`: 源分布上的表现不能无条件外推到目标分布；跨域表现依赖分布差异、假设空间和可迁移结构。
- `使用边界`: 分布发生变化不等于性能必然下降；变化可能无关、被模型吸收，甚至改善表现。正确动作是重新验证，不是预先断言退化。
- `正文处理`: 本轮改为“既有证据失去自动外推资格”，不再声称漂移必然导致性能退化。

### Law 26 — 校准定律

关联正文：[[03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）|Law 26：校准定律]]

- `依据类型`: 直接理论依据
- `支撑强度`: 强
- `主要来源`: [Brier 1950](https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml)；[Dawid 1982](https://fitelson.org/seminar/dawid.pdf)
- `可支撑的说法`: 概率预测质量不仅取决于是否给出答案，也取决于置信度是否与实际频率匹配。
- `使用边界`: Brier score 与 well-calibrated forecaster 可以支撑校准概念；具体到 LLM 置信表达仍需工程评价设计。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 30 — 过拟合定律

关联正文：[[03_统计与泛化定律#Law 30 — 过拟合定律（Overfitting Law）|Law 30：过拟合定律]]

- `依据类型`: 自适应数据分析 + 评测治理
- `支撑强度`: 中-强
- `主要来源`: [Dwork et al. 2015, The Reusable Holdout](https://arxiv.org/abs/1506.02629)
- `可支撑的说法`: 反复依据同一评测反馈做自适应修改，会增加对该评测集过拟合和结果失真的风险。
- `使用边界`: 过拟合风险并不等于每次重复评测都“迟早必然失败”；风险取决于样本量、反馈粒度、修改自由度、独立验证与数据刷新机制。
- `正文处理`: 本轮删除“统计学铁律”和“持续刷迟早过拟合”的必然措辞。

### Law 31 — 长尾定律

关联正文：[[03_统计与泛化定律#Law 31 — 长尾定律（Long-Tail Law）|Law 31：长尾定律]]

- `依据类型`: 大规模系统实证 + 场景化工程转译
- `支撑强度`: 中
- `主要来源`: [Dean and Barroso 2013, The Tail at Scale](https://research.google/pubs/the-tail-at-scale/)
- `可支撑的说法`: 在大规模在线系统中，少量慢请求或罕见事件可能显著影响整体体验；平均指标会掩盖尾部风险。
- `使用边界`: 不能假设所有真实输入都服从幂律，也不能未经测量就断言罕见样本必然主导失败。应先定义目标分布，再按切片和后果测量长尾贡献。
- `正文处理`: 本轮把“罕见情况总和往往主导失败”改为需要数据验证的条件性风险。

---

## 04 系统与控制定律

关联章节：[[04_系统与控制定律]]

### Law 36 — 可观测性定律

关联正文：[[04_系统与控制定律#Law 36 — 可观测性定律（Observability Law）|Law 36：可观测性定律]]

- `依据类型`: 控制理论概念 + 运维工程转译
- `支撑强度`: 中-强
- `主要来源`: [Kalman 1960, On the General Theory of Control Systems](https://boletin.math.org.mx/pdf/2/5/BSMM%282%29.5.102-119.pdf)；[OpenTelemetry, Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- `可支撑的说法`: 可观测性描述从输出推断内部状态的能力；生产系统通过日志、指标和追踪理解并排查行为。
- `使用边界`: 控制理论中的可观测性与可控性是两个不同性质，不能写成前者在数学上必然是后者的前提。遥测也不自动等于理解，更不保证系统可控制。
- `正文处理`: 本轮删除“可观测性是可控性的前提”和“唯一抓手”，保留其诊断、评测与运维价值。

### Law 39 — 康威定律

关联正文：[[04_系统与控制定律#Law 39 — 康威定律（Conway's Law）|Law 39：康威定律]]

- `依据类型`: 直接理论依据 + AI 系统投影
- `支撑强度`: 中-强
- `主要来源`: [Conway 1968, How Do Committees Invent?](https://www.melconway.com/Home/pdf/committees.pdf)；[Conway HTML mirror](https://www.melconway.com/research/committees.html)
- `可支撑的说法`: 组织沟通结构会影响系统设计结构。
- `使用边界`: 多 Agent 分工、上下文边界、团队协作结构是本库把 Conway 定律投影到 AI 工程后的表达。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。

### Law 41 — 复杂度累积定律

关联正文：[[04_系统与控制定律#Law 41 — 复杂度累积定律（Complexity-Accumulation Law）|Law 41：复杂度累积定律]]

- `依据类型`: 软件演化经验规律 + 工程原则
- `支撑强度`: 中
- `主要来源`: [Lehman et al., Laws of Software Evolution](https://cs.uwaterloo.ca/~a78khan/cs446/additional-material/scribe/27-refactoring/Lehman-LawsOfSoftwareEvolution.pdf)
- `可支撑的说法`: 持续演化的 E-type 软件若不投入工作维持或降低复杂度，复杂度往往会上升。
- `使用边界`: 该经验规律不覆盖所有系统，也不证明复杂度只会单向增加、交互必然超线性或软件复杂度等同热力学熵。删除、模块化和重构可以降低复杂度。
- `正文处理`: 本轮把绝对规律改为有适用域、可被主动逆转的演化倾向。

### Law 42 — 优雅降级定律

关联正文：[[04_系统与控制定律#Law 42 — 优雅降级定律（Graceful-Degradation Law）|Law 42：优雅降级定律]]

- `依据类型`: 站点可靠性工程原则
- `支撑强度`: 中-强
- `主要来源`: [Google SRE, Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- `可支撑的说法`: 在过载或局部故障时，有计划地减少非关键工作可保护核心服务并限制级联失效。
- `使用边界`: 降级路径会增加复杂度，必须被测试、监控且保持语义诚实；涉及安全、完整性或错误结果可能造成伤害时，应选择 fail closed，而不是勉强返回部分结果。
- `正文处理`: 本轮补入安全边界，不再把“部分服务总好过停止”当作普遍规则。

---

## 05 接口与边界定律

关联章节：[[05_接口与边界定律]]

### Law 47 — 最小权限定律

关联正文：[[05_接口与边界定律#Law 47 — 最小权限定律（Least-Privilege Law）|Law 47：最小权限定律]]

- `依据类型`: 直接安全工程原则
- `支撑强度`: 强
- `主要来源`: [Saltzer and Schroeder 1975, The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939)
- `可支撑的说法`: 每个程序和用户只应获得完成任务所需的最小权限；缩小权限能限制错误或受损组件造成的损害。
- `使用边界`: 最小权限不能替代授权正确性、完整仲裁、隔离、审计和撤销机制；权限过细也会增加运营复杂度，应按任务与风险设计。
- `正文处理`: 当前正文边界充分，本轮只补集中 citation，不改写。

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

### Law 63 — 不确定性外显定律

关联正文：[[07_认识论与真理定律#Law 63 — 不确定性外显定律（Surface-Uncertainty Law）|Law 63：不确定性外显定律]]

- `依据类型`: 选择性预测 + 概率校准实证
- `支撑强度`: 中-强
- `主要来源`: [Geifman and El-Yaniv 2019, SelectiveNet](https://proceedings.mlr.press/v97/geifman19a.html)；[Guo et al. 2017, On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html)
- `可支撑的说法`: 系统可以通过选择性预测、拒答与校准来管理风险；置信表达需要用真实结果检验。
- `使用边界`: 模型自报的“我不确定”或百分比不自动可信。只有经过任务级校准、能触发差异化行动且不会误导用户的不确定性信号才有工程价值。
- `正文处理`: 本轮把“主动表达”收窄为“经过验证、可行动的不确定性外显”。

### Law 64 — 可证伪性定律

关联正文：[[07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）|Law 64：可证伪性定律]]

- `依据类型`: 直接哲学依据 + 工程规范
- `支撑强度`: 中-强
- `主要来源`: [Popper, The Logic of Scientific Discovery](https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447)
- `可支撑的说法`: 可证伪性是 Popper 提出的科学划界标准；明确失败条件能提高经验性主张的可检验性。
- `使用边界`: 它不是所有知识唯一公认的定义；伦理规范、定义、数学命题和解释性框架需要不同评价方式。
- `正文处理`: ✅ 已于 2026-07-10 完成 P2-A 正式定义与主动正文收窄；保留 Law 64 编号与 heading，改为经验性工程主张的审计纪律。见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 改写影响审计]]。

---

## 08 可靠性与失败定律

关联章节：[[08_可靠性与失败定律]]

### Law 71 — 显式失败定律

关联正文：[[08_可靠性与失败定律#Law 71 — 显式失败定律（Fail-Loudly Law）|Law 71：显式失败定律]]

- `依据类型`: 故障语义 + 站点可靠性工程
- `支撑强度`: 中
- `主要来源`: [Schneider 1984, Byzantine Generals in Action: Implementing Fail-Stop Processors](https://doi.org/10.1145/357369.357374)；[Google SRE, Service Best Practices](https://sre.google/sre-book/service-best-practices/)
- `可支撑的说法`: 系统应让调用方能区分成功、降级和失败，避免把错误结果伪装成正常成功。
- `使用边界`: “显式”不等于所有故障都立即崩溃或停止。应按风险选择 fail closed、fail open、重试或受控降级，同时保留可见状态与告警。
- `正文处理`: 本轮从“所有失败都应报错停止”收窄为失败语义必须真实、可检测。

### Law 72 — 爆炸半径定律

关联正文：[[08_可靠性与失败定律#Law 72 — 爆炸半径定律（Blast-Radius Law）|Law 72：爆炸半径定律]]

- `依据类型`: 直接可靠性工程原则
- `支撑强度`: 强
- `主要来源`: [AWS Well-Architected, Use Fault Isolation to Protect Your Workload](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.html)
- `可支撑的说法`: 故障隔离边界能限制故障影响范围，避免单个组件或分区失效扩散到整个工作负载。
- `使用边界`: 隔离会增加成本和架构复杂度；边界应由风险、依赖关系和恢复目标决定，而不是无限拆分。
- `正文处理`: 当前正文边界充分，本轮只补集中 citation，不改写。

### Law 74 — 不可逆性定律

关联正文：[[08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）|Law 74：不可逆性定律]]

- `依据类型`: 决策理论 + 管理启发式
- `支撑强度`: 中
- `主要来源`: [Arrow and Fisher 1974](https://academic.oup.com/qje/article-abstract/88/2/312/1861520)；[Amazon 2015 shareholder letter](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/whitepapers/approved/executive-insights/2015-letter-to-shareholders.pdf)
- `可支撑的说法`: 不确定性与不可逆后果会提高保留选择权和谨慎决策的价值；可逆决策可采用更轻流程。
- `使用边界`: 决策速度不只由可逆性决定；影响大小、时间压力、信息价值和恢复成本同样重要。单向门/双向门首先是管理启发式，不是覆盖所有决策的数学定理。
- `正文处理`: P2-C 已完成收窄；正文改为后果、恢复能力与情境变量共同分诊。

### Law 76 — 静默降级危险定律

关联正文：[[08_可靠性与失败定律#Law 76 — 静默降级危险定律（Silent-Degradation-Danger Law）|Law 76：静默降级危险定律]]

- `依据类型`: 站点可靠性工程监控原则
- `支撑强度`: 中
- `主要来源`: [Google SRE, Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- `可支撑的说法`: 仅看组件是否存活会漏掉用户可见质量下降；黑盒与白盒监控、SLO 和症状指标有助于发现被掩盖的退化。
- `使用边界`: 静默退化不在所有情境下都比突然崩溃危险，持续评测也不是唯一检测手段；监控、抽样、审计、用户反馈和业务指标都可能提供证据。
- `正文处理`: 本轮删除“更危险”和“唯一手段”的无条件比较。

### Law 77 — 恢复优于预防定律

关联正文：[[08_可靠性与失败定律#Law 77 — 恢复优于预防定律（Recovery-Over-Prevention Law）|Law 77：恢复优于预防定律]]

- `依据类型`: 恢复导向计算系统原则
- `支撑强度`: 中
- `主要来源`: [Patterson et al. 2002, Recovery Oriented Computing](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2002/5574.html)
- `可支撑的说法`: 恢复时间、故障隔离、回滚和可演练恢复应成为一等设计目标，而不能只追求更长的无故障时间。
- `使用边界`: 恢复不能处理所有故障，也不总比预防重要。不可逆伤害、安全事故和法律违规通常要求预防优先；可恢复故障则应平衡预防成本与恢复能力。
- `正文处理`: 本轮把“恢复优于预防”解释为条件性资源取舍，而不是通用排序。

---

## 09 人机与信任定律

关联章节：[[09_人机与信任定律]]

### Law 79 — 人在回路定律

关联正文：[[09_人机与信任定律#Law 79 — 人在回路定律（Human-in-the-Loop Law）|Law 79：人在回路定律]]

- `依据类型`: 人因工程 + 自动化监督研究
- `支撑强度`: 中-强
- `主要来源`: [Bainbridge 1983, Ironies of Automation](https://doi.org/10.1016/0005-1098(83)90046-8)
- `可支撑的说法`: 自动化会改变人类监督者的工作，长期被动监控与突然接管可能削弱有效控制；人工环节必须有证据、时间和实际干预能力。
- `使用边界`: 有人点击确认不等于风险降低。若人无法理解、验证或及时拦截，HITL 只制造控制假象；低风险且自动控制充分的动作也不必无差别审批。
- `正文处理`: P2-C 已按“重大剩余风险 + 有效人工控制”收窄，本轮只补集中 citation。

### Law 84 — 信任-可靠性剪刀差定律

关联正文：[[09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）|Law 84：信任-可靠性剪刀差定律]]

- `依据类型`: 综合判断
- `支撑强度`: 中
- `主要来源`: [Parasuraman and Riley 1997](https://web.mit.edu/16.459/www/parasuraman.pdf)；[Lee and See 2004](https://journals.sagepub.com/doi/10.1518/hfes.46.1.50_30392)
- `可支撑的说法`: 自动化系统存在 misuse / overreliance 等人因风险；适当信任应与系统能力相匹配。
- `使用边界`: “信任-可靠性剪刀差”是本库综合命名；来源没有证明信任必然比可靠性增长更快。
- `正文处理`: ✅ 已于 2026-07-10 完成 P1-B 正式定义收窄与全库主动正文同步；保留“剪刀差”名称，但明确它是可测失配风险，不是必然增长曲线。见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 改写影响审计]]。

### Law 86 — 责任不可委托定律

关联正文：[[09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）|Law 86：责任不可委托定律]]

- `依据类型`: 治理规范 + 法律角色分配
- `支撑强度`: 中
- `主要来源`: [UNESCO AI Ethics Recommendation](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence)；[OECD AI Principles](https://www.oecd.org/en/topics/ai-principles.html)；[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en)
- `可支撑的说法`: 最终责任与问责应可追溯到自然人或法人；责任应基于生命周期角色、语境和行动能力分配。
- `使用边界`: 不能把责任一律归给“部署者”。提供者、部署者、经营者、组织与专业人员可能承担不同义务；具体法律责任取决于司法辖区与场景。
- `正文处理`: ✅ 已于 2026-07-10 完成正式定义收窄与全库主动正文同步；见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|P0 改写影响审计]]。

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

### Law 92 — 数据即攻击面定律

关联正文：[[10_对抗与安全定律#Law 92 — 数据即攻击面定律（Data-Is-Attack-Surface Law）|Law 92：数据即攻击面定律]]

- `依据类型`: 新兴 AI 安全实证 + 威胁建模转译
- `支撑强度`: 中-强
- `主要来源`: [Greshake et al. 2023, Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- `可支撑的说法`: 检索网页、文档和其他第三方数据可以携带间接注入内容并改变模型或工具行为，因此数据通道需要进入威胁模型。
- `使用边界`: 攻击面由信任边界、可控性和行为影响决定，不是每个字节风险相同；“内部数据”也可能被污染，不能因来源标签而自动豁免。
- `正文处理`: 本轮改为按信任边界和行为影响建模，不再把“外部/内部”当作安全分界。

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
- `正文处理`: ✅ 已于 2026-07-10 完成 P1-B 正式定义收窄与全库主动正文同步；保留编号与 heading，改为能力和可靠性分维度评价，不预设可靠性必然滞后。见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 改写影响审计]]。

### Law 96 — 任务重组定律

关联正文：[[11_演化与元定律#Law 96 — 任务重组定律（Task-Recomposition Law）|Law 96：任务重组定律]]

- `依据类型`: 任务型劳动经济学 + 工作场景实证 + 本库综合转译
- `支撑强度`: 中
- `主要来源`: [Autor 2015](https://doi.org/10.1257/jep.29.3.3)；[Acemoglu & Restrepo 2019](https://doi.org/10.1257/jep.33.2.3)；[Brynjolfsson, Li & Raymond 2023/2025](https://www.nber.org/papers/w31161)；[ILO 2025](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure)
- `可支撑的说法`: 自动化会替代部分任务，也会与劳动互补、创造新任务，并对不同经验水平和职业产生不同影响；分析单位应落到任务而不是把岗位看成整体。
- `使用边界`: 这些来源不能证明“人的工作必然持续上移”或“执行层最终几乎完全由 AI 接管”。任务还可能消失、下沉、标准化、保持不变或重新组合。
- `正文处理`: ✅ 已于 2026-07-10 将“抽象上移定律”改为“任务重组定律”，保留 Law 96 编号并降为演化综合命题；见 [[_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT|Law 96 任务重组审计]]。

### Law 99 — 简单性存活定律

关联正文：[[11_演化与元定律#Law 99 — 简单性存活定律（Simplicity-Survives Law）|Law 99：简单性存活定律]]

- `依据类型`: 软件工程原则 + 安全设计原则
- `支撑强度`: 中
- `主要来源`: [Brooks 1987, No Silver Bullet](https://doi.org/10.1109/MC.1987.1663532)；[Saltzer and Schroeder 1975, Economy of Mechanism](https://doi.org/10.1109/PROC.1975.9939)
- `可支撑的说法`: 软件存在不可消除的本质复杂度；较小、较简单的保护机制更容易被理解、验证和正确实现。
- `使用边界`: 简单方案并不天然更可靠或更能“存活”。必要的冗余、隔离和控制会增加结构复杂度却降低风险；应比较满足需求后的全生命周期复杂度，而不是追求最少组件。
- `正文处理`: 本轮把“简单必胜”收窄为在满足功能与风险要求后优先选择更低生命周期复杂度。

### Law 100 — 判断力稀缺定律

关联正文：[[11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）|Law 100：判断力稀缺定律]]

- `依据类型`: 生产率研究 + 认识论综合
- `支撑强度`: 中
- `主要来源`: [Noy and Zhang 2023](https://doi.org/10.1126/science.adh2586)；[Dell’Acqua et al., Jagged Technological Frontier](https://pubsonline.informs.org/doi/pdf/10.1287/orsc.2025.21838)
- `可支撑的说法`: 生成式 AI 能降低部分知识工作的生产成本；能力边界参差，使用者仍需识别任务边界并检查结果。
- `使用边界`: 这些研究不能证明判断力是“唯一”持续稀缺资源，也不能证明所有判断都无法自动化。本条是需持续验证的本库综合命题。
- `正文处理`: ✅ 已于 2026-07-10 完成 P1-C 正式定义收窄与全库主动正文同步；保留 Law 100 编号与 heading，改为需要按任务验证的条件性判断瓶颈，不再声称判断力是唯一持续稀缺资源。见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 改写影响审计]]。

### Law 102 — 定律有边界定律

关联正文：[[11_演化与元定律#Law 102 — 定律有边界定律（元定律 / Meta-Law: Every Law Has Boundaries）|Law 102：定律有边界定律]]

- `依据类型`: 科学哲学 + 建模规范
- `支撑强度`: 中-强
- `主要来源`: [Box 1976, Science and Statistics](https://gwern.net/doc/statistics/decision/1976-box.pdf)；[Popper, The Logic of Scientific Discovery](https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447)
- `可支撑的说法`: 模型是现实的简化；经验性理论需要测试条件、适用域和被反驳的可能。
- `使用边界`: 这是一条建模与审查元原则，不是无条件数学定理；它要求包括自身在内的工程 Law 都声明边界。
- `正文处理`: 不进入 Law 正文；正文只保留章节入口。
