---
type: agent-decision-system
abstraction_layer: 操作层（机器可调用投影）
role: pattern-cards
date: 2026-07-06
audience: AI-Agent
tags: [AgentDecisionSystem, 模式卡, Patterns]
---

# Agent Decision System · 模式操作卡（02_PATTERN-CARDS）

> 20 个"该做什么"的可调用卡片。每张 7 字段。引用：LAW-xx→[[04_LAW-INVARIANTS]]，ANTI-xx→[[03_ANTIPATTERN-DETECTORS]]。深度→[[llm-design-patterns/00_INDEX|Design Patterns]] / [[multi-agent-patterns-handbook/00_INDEX|Multi-Agent]]。

---

## PAT-01 · Chain-of-Thought（思维链）
- **When to use**: 任务需要多步推理（逻辑/数学/因果/规划）；"直接问错、拆开想就对"的任务。
- **When not to use**: 简单事实检索/分类；已用推理模型；延迟极敏感。
- **Decision criteria**: 任务是否含多步推导？是→用；否→纯开销，别用。
- **Related concepts**: LAW-06(误差累积) · PAT-10(Self-Consistency) · ANTI-09
- **Common mistakes**: 对简单任务滥用(CoT成瘾)；信推理链的形式而不验证结论。
- **Recommended actions**: 要求"先推理后结论"(非先结论后解释)；推理链留档供验证。
- **Example reasoning path**: 处境=多步算术总出错 → LAW-06 单次易错 → 用 PAT-01 让它逐步展开 → 验证每步 → 交付。

## PAT-02 · ReAct（推理+行动交替）
- **When to use**: 任务需要外部信息/操作且下一步依赖中间结果；探索型任务。
- **When not to use**: 纯推理可完成(用CoT更省)；步骤完全固定(用Pipeline)。
- **Decision criteria**: 需要边做边看、动态调整吗？是→用。
- **Related concepts**: PAT-04(Tool Use) · LAW-05(输入皆指令) · PAT-09
- **Common mistakes**: 无最大轮数(死循环)；工具错误被吞(静默失败)；无 trace。
- **Recommended actions**: Thought→Action→Observation 循环；设最大轮数；工具失败返回有用错误以自愈；全程 trace。
- **Example reasoning path**: 处境=查最新数据再算 → 纯推理会编(LAW-02) → ReAct: 搜索→观察→计算→答 → 每步可见。

## PAT-03 · RAG（检索增强生成）
- **When to use**: 需私有/实时/海量/可溯源知识；知识量超上下文。
- **When not to use**: 知识量<上下文一半(直接全塞)；需全局统计(RAG只见片段)。
- **Decision criteria**: 知识是否外部且需溯源？是→用。
- **Related concepts**: LAW-02(幻觉) · LAW-13(信息守恒) · PAT-12
- **Common mistakes**: 只查生成不查检索(80%问题在检索)；纯向量检索(相似≠相关)；检索盲信。
- **Recommended actions**: 混合检索(语义+关键词)+重排；答案带引用；不足时拒答；内容当数据非指令。
- **Example reasoning path**: 处境=问公司政策 → 模型不知(LAW-13) → RAG检索条款→带引用答 → 验证命中率+拒答率。

## PAT-04 · Tool Use / Function Calling
- **When to use**: 需精确计算、实时数据、执行操作等模型固有短板。
- **When not to use**: 纯语言任务；工具可靠性无保障(尤其不可逆)。
- **Decision criteria**: 任务需要模型能力之外的东西吗？是→接工具。
- **Related concepts**: LAW-05(输入皆指令) · LAW-09(可逆性) · PAT-18
- **Common mistakes**: 返回值盲信(ANTI-10)；吞掉工具错误；危险工具无审批；工具描述敷衍。
- **Recommended actions**: 工具描述写清何时用/参数/失败返回什么；返回值当不可信；不可逆操作审批；失败返回有用错误。
- **Example reasoning path**: 处境=要算复利 → 模型算数不可靠 → calculator工具→精确值 → 验证工具返回。

## PAT-05 · Reflection / Critic-Refine（生成-批评-修订）
- **When to use**: 质量重要且值得多倍成本；**有客观信号**(测试/执行/rubric)时最有效。
- **When not to use**: 无客观锚(自评偏宽容，空转)；简单任务；成本敏感。
- **Decision criteria**: 有客观反馈信号吗？无→别反思。
- **Related concepts**: LAW-01(先设计可靠验证器) · ANTI-09 · PAT-06
- **Common mistakes**: 无锚空转(ANTI-09)；越改越坏；无收敛判据。
- **Recommended actions**: 给反思接客观信号；通常≤3轮；检测与修正分离；可跨模型批评破盲区。
- **Example reasoning path**: 处境=代码质量不稳 → 有测试作锚 → 生成→跑测试→按结果批评→修订 → 错误率真降。

## PAT-06 · LLM-as-Judge（模型即裁判）
- **When to use**: 规模化评价主观质量；运行时质量闸门；版本对比。
- **When not to use**: 裁判未校准时(玄学)；有代码可客观评分时(用代码更省)。
- **Decision criteria**: 质量主观且需规模化，且裁判能被校准吗？是→用。
- **Related concepts**: LAW-04(古德哈特) · Q-10 · ANTI-03
- **Common mistakes**: 未校准(测的是裁判口味)；位置/长度/自恋偏差；被针对性钻空子。
- **Recommended actions**: 抽样对比人类校准(一致率<阈值改rubric)；逐维度先理由后打分；对比时交换顺序。
- **Example reasoning path**: 处境=万条产出要评质量 → 人工评不过来 → Judge+校准 → 抽检一致率91% → 可用。

## PAT-07 · Structured Output（结构化输出）
- **When to use**: 输出要被程序消费(存库/传下游/触发动作)。
- **When not to use**: 输出给人读的自由文本；过度约束损害质量。
- **Decision criteria**: 下游是机器吗？是→schema约束。
- **Related concepts**: LAW-01(先设计可靠验证器) · LAW-11(确定性优先) · PAT-04
- **Common mistakes**: 靠正则抠散文(脆弱)；深嵌套schema模型易错。
- **Recommended actions**: 用API的schema强制；复杂任务先自由推理再抽成结构。
- **Example reasoning path**: 处境=简历转数据库记录 → 散文难解析 → structured output→合法JSON → 一行反序列化。

## PAT-08 · Pipeline / Prompt Chaining（流水线）
- **When to use**: 任务可分解为固定顺序步骤；单prompt做全部导致质量下降。
- **When not to use**: 任务简单(拆分过度设计)；步骤依输入而变(用Agent)。
- **Decision criteria**: 步骤固定且每步产物可定义吗？是→用。
- **Related concepts**: LAW-11(确定性优先) · 分解降难 · PAT-16
- **Common mistakes**: 早段错误级联到后段；环间上下文丢信息。
- **Recommended actions**: 每段单一职责+格式校验；贵模型只放关键段；可缓存可换模型。
- **Example reasoning path**: 处境=英文技术文转中文教程 → 拆:提取→解释→组织翻译→校对 → 每段可测。

## PAT-09 · Planner-Executor（规划-执行）
- **When to use**: 多步骤有依赖但拆解后每步明确；需人工预审计划。
- **When not to use**: 任务简单/步骤固定；纯探索型(用ReAct)；计划极易失效。
- **Decision criteria**: 需要"先想清楚步骤"且步骤可规划吗？是→用。
- **Related concepts**: LAW-10(简单优先) · PAT-17 · SIT-06
- **Common mistakes**: 计划僵化不重规划；子任务不自包含；执行端约束未被规划考虑。
- **Recommended actions**: 贵模型规划+便宜模型执行；任务自包含；计划失效时受控重规划(≤2-3次)。
- **Example reasoning path**: 处境=写竞品报告 → 拆:定清单(探路)→并行调研→综合 → 探路发现竞品翻倍→重规划。

## PAT-10 · Ensembling / Voting / Self-Consistency（集成投票）
- **When to use**: 答案可离散比对(分类/判断/数学/可测代码)；用成本换可靠性。
- **When not to use**: 开放生成(无法比对)；错误高度相关(同模型稳定同错)。
- **Decision criteria**: 答案可机械比对且错误可去相关吗？是→用。
- **Related concepts**: 集成去相关 · LAW-03(校准) · PAT-06
- **Common mistakes**: 对相关错误投票(放大同一错误+假高置信)；等权而非按可靠性加权。
- **Recommended actions**: 多样化(不同温度/prompt/模型)去相关；票数分布作置信信号；一致度低转人工。
- **Example reasoning path**: 处境=工单分类要可靠 → 5投票者(3同模型高温+2异构) → 全票一致直接采纳,分裂转人工。

## PAT-11 · Context Compression（上下文压缩）
- **When to use**: 对话/任务长到接近窗口；大量历史对当前无关。
- **When not to use**: 任务短上下文充裕；每个细节都可能后续需要。
- **Decision criteria**: 上下文在膨胀且部分已无关吗？是→压缩。
- **Related concepts**: LAW-07(上下文即状态) · 信噪比 · PAT-12
- **Common mistakes**: 通用摘要丢掉后续需要的关键细节；压错=状态错。
- **Recommended actions**: 压为状态摘要(明确保留什么)；细节外置可检索；保留最近N轮原文。
- **Example reasoning path**: 处境=50轮任务上下文将爆 → 每10轮压为状态摘要 → 丢搜索垃圾留结论 → 可断点恢复。

## PAT-12 · Memory Retrieval（记忆机制）
- **When to use**: 需跨会话记住用户/上下文；长任务保持状态；Agent积累经验。
- **When not to use**: 一次性无状态任务；隐私敏感不许长存。
- **Decision criteria**: 需要跨调用的连续性/个性化吗？是→用。
- **Related concepts**: LAW-07 · PAT-03 · LAW-05(记忆是攻击面)
- **Common mistakes**: 记忆倾倒(ANTI-08)；检索错误记忆；无遗忘/更新；记忆污染潜伏。
- **Recommended actions**: 分层(短期上下文/中期状态/长期外部检索)；带时间戳+置信度；有遗忘机制；写入校验。
- **Example reasoning path**: 处境=个人助理需记偏好 → 分层记忆 → 检索相关记忆注入 → 冲突时最新覆盖旧。

## PAT-13 · Map-Reduce（分片并行-聚合）
- **When to use**: 大量、分片间弱耦合的同构任务(逐章摘要/批量处理/逐文件扫描)。
- **When not to use**: 分片强依赖(伏笔跨片)；数据量小；需全局统计。
- **Decision criteria**: 数据超上下文且单片可独立处理吗？是→用。
- **Related concepts**: 有效注意力有限 · PAT-11 · 分解降难
- **Common mistakes**: 跨片信息丢失；Reduce成瓶颈超窗口。
- **Recommended actions**: 按语义边界切(可重叠)；Mapper用便宜模型;Reduce可分层;片结果带定位信息。
- **Example reasoning path**: 处境=总结300页报告 → 切30片并行Map→抽论点 → Reduce合并+溯源表 → 覆盖率报告。

## PAT-14 · Debate / Committee（辩论/委员会）
- **When to use**: 高风险、无标准答案、理由比结论重要的判断。
- **When not to use**: 有客观答案的简单问题；成本敏感；同源伪多样。
- **Decision criteria**: 判断高风险且需暴露隐藏假设/最强反驳吗？是→用。
- **Related concepts**: LAW-03 · 集成去相关 · SIT-14
- **Common mistakes**: 从众级联(立场泄漏)；同源辩手伪多样；主席篡改。
- **Recommended actions**: 独立意见先行(防从众)；须回应最强论点(非稻草人)；真差异化成员;主席审计。
- **Example reasoning path**: 处境=判断研究结论是否可信 → 辩手正反论证→交锋暴露样本偏差 → 裁判:有条件可信+保留分歧。

## PAT-15 · Guardrails / Validation（护栏）
- **When to use**: 面向真实用户的生产系统；有合规/安全红线；处理不可信输入。
- **When not to use**: 内部原型(过早加护栏拖慢)；护栏成本>风险。
- **Decision criteria**: 有明确红线且面向真实用户吗？是→必须有。
- **Related concepts**: LAW-05(权限胜过自觉) · 纵深防御 · ANTI-10
- **Common mistakes**: 只靠system prompt(可绕过)；只防用户输入忘检索/工具返回；过严误杀。
- **Recommended actions**: 输入侧+输出侧双护栏;规则层先过确定性,模型层判模糊;监控误杀率。
- **Example reasoning path**: 处境=客服回复出站 → 规则拦红线措辞→模型判合规 → 注入被输出护栏拦下。

## PAT-16 · Routing（路由分发）
- **When to use**: 输入异构可分3-10类且处理逻辑不同；模型成本分层。
- **When not to use**: 输入同质；类别边界极模糊(丢意图)。
- **Decision criteria**: 输入能被分成处理逻辑不同的少数类吗？是→用。
- **Related concepts**: LAW-10 · 关注点分离 · PAT-08
- **Common mistakes**: Router单点(分错全错)；类别体系腐烂(other涨)；Router加工内容引偏见。
- **Recommended actions**: Router只贴标签+置信度;低置信转默认/人工;级联(规则先接确定流量)。
- **Example reasoning path**: 处境=客服多类请求 → Router分类→退款/技术/账单各专属handler → 80%简单流量走便宜通道。

## PAT-17 · Orchestrator-Workers（协调者-执行者）
- **When to use**: 子任务数量/内容依输入动态变化；拆解需要智能。
- **When not to use**: 拆解方式固定(用MapReduce)；单层协调够(无需层级)；简单任务。
- **Decision criteria**: 子任务动态且异构吗？是→用。
- **Related concepts**: PAT-09 · SIT-06 · 上下文隔离
- **Common mistakes**: 协调者过载(瓶颈+单点)；子任务不自包含；静默失败向上传染。
- **Recommended actions**: 协调者只协调(执行给workers,状态外置);子任务自包含;结论带置信度+抽查。
- **Example reasoning path**: 处境=研究开放问题 → 动态拆4子任务→独立worker并行 → 合成;矛盾时发起核查子任务。

## PAT-18 · Human-in-the-Loop（人在回路）
- **When to use**: 不可逆/高风险/需价值判断的操作；高不确定输出。
- **When not to use**: 可逆、低风险、高可靠的操作(此处人在回路是浪费)。
- **Decision criteria**: 后果大、难恢复、证据不足或涉及不可委托判断，且人能在行动前看见关键证据并有效干预吗？
- **Related concepts**: LAW-09(风险与恢复分诊) · 责任不可委托 · SIT-07
- **Common mistakes**: 无干预点(启动即失控)；审批点在错误位置(可逆的审批、不可逆的放手)；自动化悖论(人失去接管力)。
- **Recommended actions**: 先用限权、自动验证、灰度和回滚降低风险；剩余高风险再设有证据、有时间、有能力的人工控制点；持续测真实拦截率。
- **Example reasoning path**: 处境=Agent要发对外邮件 → 评估受众范围/可撤回性/证据质量(LAW-09) → 小范围内部通知可规则校验后发送，高影响外发在发送前由有上下文的人确认。

## PAT-19 · Red Team（红队）
- **When to use**: 安全性评价;有害行为检测;高风险系统上线前;致命三重奏组件。
- **When not to use**: 无对抗者的非安全场景;成本远超风险。
- **Decision criteria**: 失败代价高且有人会主动攻击吗?是→用。
- **Related concepts**: LAW-05 · 攻防不对称 · SIT-17
- **Common mistakes**: 红队想象力=覆盖上限;一次性而非持续;声称"绝对安全"。
- **Recommended actions**: 多样化红队;攻击库沉淀为回归集;持续红队(更新即重跑);只声称"已防已知攻击"。
- **Example reasoning path**: 处境=客服Agent上线前 → 红队生成30攻击→攻破8→蓝队加固→复测 → 交付风险报告。

## PAT-20 · Tree Search / Tree-of-Thoughts（树搜索）
- **When to use**: 解空间大、需探索多路径回溯的高难度问题(单CoT/投票都撑不住)。
- **When not to use**: 绝大多数日常任务(成本5-30×);线性推理已够;评估器不可靠。
- **Decision criteria**: 是需要探索+回溯的真难题且有可靠中间评估吗?是→用。
- **Related concepts**: PAT-01 · 计算换质量 · 质量有成本
- **Common mistakes**: 对普通任务滥用(成本暴涨);评估器不准则南辕北辙;过度工程。
- **Recommended actions**: 先穷尽便宜的(CoT/投票);每步生成多候选+评估剪枝+回溯;严控预算。
- **Example reasoning path**: 处境=复杂规划谜题CoT卡死 → 上ToT:每步多候选→评估剪死路→回溯 → 找到解(代价几十倍,仅值此类难题)。

---

## 快速索引（按处境反查模式）

| 你的处境 | 首选模式 |
|---------|---------|
| 多步推理 | PAT-01, PAT-10, PAT-20(难题) |
| 需外部知识/能力 | PAT-03, PAT-04 |
| 要提质/把关 | PAT-05, PAT-06, PAT-14(高风险) |
| 输出给机器 | PAT-07 |
| 组织多次调用 | PAT-08, PAT-16, PAT-09, PAT-17, PAT-13 |
| 长任务/记忆 | PAT-11, PAT-12 |
| 安全/不可逆 | PAT-15, PAT-18, PAT-19 |
