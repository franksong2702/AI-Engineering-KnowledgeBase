---
type: case-library
abstraction_layer: 应用（案例层）
date: 2026-07-06
course: ai-engineering-case-library
category: Agent架构
tags: [案例, Agent架构]
---

# 类二 单 Agent 架构（Case 11–20）
> 决策路由入口：[[agent-decision-system/01_SITUATION-ROUTER#SIT-01 · 我要决定用工作流还是自主 Agent|SIT-01]] / [[agent-decision-system/01_SITUATION-ROUTER#SIT-03 · 任务需要多步推理|SIT-03]] / [[agent-decision-system/01_SITUATION-ROUTER#SIT-04 · 输出要被程序/下游消费|SIT-04]] / [[agent-decision-system/01_SITUATION-ROUTER#SIT-05 · 输出质量不稳，要提质|SIT-05]] / [[agent-decision-system/01_SITUATION-ROUTER#SIT-13 · 任务失败/出错了，要定位和恢复|SIT-13]] / [[agent-decision-system/01_SITUATION-ROUTER#SIT-15 · 模型给了一个自信的答案，我该不该信|SIT-15]] → [[agent-decision-system/01_SITUATION-ROUTER|Situation Router]]

---

## Case 11 · 把分类任务做成了自主 Agent（深度版）

- **Problem**: 一个"给客服邮件分类"的任务被做成了 ReAct Agent，结果分类不稳定、成本是规则方案的百倍。
- **Context**: 5 个固定类别（账单/技术/退换/投诉/其他），日均 8000 封；Agent 版给了搜索历史工单、查知识库两个工具，平均每封邮件跑 4.2 轮循环。
- **Constraints**: 需要稳定、便宜、可规模化；分类错误的代价不对称（投诉被误分的代价 >> 其他）。
- **Analysis**: 步骤完全可预知（读邮件→判类别→输出），却用了自主 Agent。看 trace 发现循环里的工具调用几乎不改变结论——Agent 在"表演调研"：查了历史工单，然后输出和第一轮直觉相同的类别。方差的来源恰是这些无用循环（同一封邮件跑三次，4.2 轮里的随机检索结果不同，偶尔把结论带偏）。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-11 · 确定性优先（Determinism First）|LAW-11]]（确定性优先）· [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-16 · Routing（路由分发）|PAT-16]]（Routing）或单次分类调用，而非 Agent

**Trace 片段（Agent 版的一次"表演调研"）**：

```
mail#4471 "你们 app 又闪退了，第三次了！"
T1: Thought: 可能是技术问题，也可能是投诉。查一下该用户历史工单。
    Action: search_tickets(user=..., top3) → 3 条旧技术工单
T2: Thought: 用户有技术工单历史……但语气愤怒。再查知识库"闪退"。
    Action: kb_search("闪退") → 一篇已知 bug 文档
T3: Thought: 是已知技术问题。分类：技术。
→ 同一封邮件第二次运行：T2 检索到的是退款政策文档（向量近邻抖动），
  最终输出"投诉"。两次运行，两个答案。
```

- **Architecture Decision**: 降级为一次带 few-shot 的分类调用 + schema 输出（枚举约束），温度 0；投诉类加一条硬规则兜底（含"投诉/工商/曝光"等词强制人工复核队列）。不用循环、不给工具。
- **第一次修复与反转**: 直接下线 Agent 换单次调用后，总体准确率升了，但**投诉类的召回率反而降了 4 个点**——原来 Agent 的历史工单检索对"愤怒但表述模糊"的邮件有一点真实增益。处理：不是回退到 Agent，而是把"该用户近 30 天工单数"作为一个字段直接拼进单次调用的输入（把 Agent 的动态检索固化为确定性特征）。**Agent 循环里偶尔有用的动作，常可以提炼成工作流里确定的一步**——这才是正确的降级方式，而非一刀切。
- **Anti-Patterns Avoided**: [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-06 · 过度 Agent 化（Over-Agentization）— 🟠|ANTI-06]]（过度 Agent 化）。
- **Evaluation Method**: 500 封标注邮件的分层评测（按类别，重点看投诉类召回）；每方案跑 3 次测方差；成本按日均量折算月账单。
- **Final Solution**: 单次调用 + 工单数特征 + 投诉硬规则：总体准确率 88%→93%，三次运行结果一致率 99%+（Agent 版约 91%），单封成本降约两个数量级；投诉类召回率恢复并超过 Agent 版。
- **Lessons Learned**: ① 步骤可预知就别用 Agent，"智能"不是默认更好。② 降级前先看 trace 里 Agent 到底做了什么——它偶尔有用的动作可以固化为确定性特征，全盘否定和全盘保留都是懒惰。③ 错误代价不对称的类别配硬规则兜底，别指望调 prompt。④ 数字为教学编排值。

## Case 12 · God Agent 什么都做但都做不好

- **Problem**: 一个客服 Agent 同时处理查询、退款、投诉、技术、账单，system prompt 长到自相矛盾，每类都平庸。
- **Context**: 单个 Agent 塞满所有规则。
- **Constraints**: 各类处理逻辑差异大。
- **Analysis**: 职责混杂导致上下文污染、无法单独优化、规则冲突。违反关注点分离。
- **Relevant Laws**: 关注点分离 · 信噪比
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-16 · Routing（路由分发）|PAT-16]]（Routing 分发给专门 handler）
- **Architecture Decision**: Router 先分类，分发给 5 个单一职责的 handler，每个 prompt 短而专。
- **Anti-Patterns Avoided**: God Agent（ANTI 精神）。
- **Evaluation Method**: 分类别评测每个 handler 的质量。
- **Final Solution**: 路由 + 专门 handler，每类质量显著提升，可独立优化。
- **Lessons Learned**: 一个 Agent 只做一件事。职责能用"且"列出五个 = 该拆。

## Case 13 · Agent 陷入死循环烧钱

- **Problem**: 一个研究 Agent 陷入"再搜一个来源就更完整"的循环，无限搜索，一夜烧掉大量额度。
- **Context**: 自主研究 Agent，无终止条件。
- **Constraints**: 成本可控，任务要能结束。
- **Analysis**: 循环无出口，依赖 Agent 自己判断"够了"，但它永不满足。
- **Relevant Laws**: 停机与预算 · [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-02 · ReAct（推理+行动交替）|PAT-02]]（ReAct + 终止条件）
- **Architecture Decision**: 设最大轮数 + 预算上限 + "连续无新信息即停"。
- **Anti-Patterns Avoided**: [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-12 · 无失败恢复/循环无出口（No Recovery / Loop Without Exit）— 🟠|ANTI-12]]（循环无出口）。
- **Evaluation Method**: 构造会诱发死循环的输入，验证在预算内安全终止。
- **Final Solution**: 三重保险，Agent 在预算内产出报告。
- **Lessons Learned**: 每个自主循环必须有显式终止条件。别信 Agent 自己会停。

## Case 14 · Agent 静默失败编造结果（深度版）

- **Problem**: 一个文件处理 Agent 遇到读不了的文件时不报错，而是编了个看似合理的结果继续，污染最终输出。
- **Context**: Agent 需要读取 20 个文件、抽取关键信息、汇总成报告。工具 `read_file()` 在权限不足或文件损坏时返回空字符串，Agent 没有区分“文件为空”和“读取失败”。
- **Constraints**: 工具错误必须显式暴露；中间失败不能伪装成成功；最终报告必须能追溯每个结论来自哪些文件。
- **Analysis**: 静默失败比显性失败危险。显性失败会中断流程，静默失败会把错误状态伪装成正常输入，让后续每一步都在坏状态上继续。这里模型不是“恶意编造”，而是在缺失信息处用语言流畅性补洞。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-06 · 误差多步累积 + 恢复优于预防（Error Compounding + Recovery）|LAW-06]]（错误沿链累积） · [[agent-decision-system/04_LAW-INVARIANTS#LAW-07 · 上下文即状态（Context Is State）|LAW-07]]（空结果进入状态） · [[agent-decision-system/04_LAW-INVARIANTS#LAW-01 · 先设计可靠验证器（Design for Verifiability）|LAW-01]]（生成结果必须可验证）
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-04 · Tool Use / Function Calling|PAT-04]]（ typed tool result） + [[agent-decision-system/02_PATTERN-CARDS#PAT-15 · Guardrails / Validation（护栏）|PAT-15]]（中间结果校验）

**Trace 片段（工具错误被吞）**：

```text
read_file("contract_17.pdf") -> ""   # 实际是 PermissionDenied，但工具只返回空字符串
Agent thought: “该文件似乎没有有效内容。”
extract_terms -> “合同 17 未包含特殊付款条款。”
final_report -> “20 份合同均无特殊付款条款。”

真实情况：contract_17.pdf 根本没读到，里面恰好有最重要的例外条款。
```

- **Architecture Decision**: 工具返回值必须类型化：`ok=true/false`、`error_code`、`source_ref`、`content_hash`、`content` 分开。Agent 不能把 `ok=false` 的结果放进正常分析；缺失文件进入 blocking issue 或 partial report。最终报告必须列出“已读取文件/失败文件/跳过文件”。
- **第一次修复与反转**: 第一版修复是在 system prompt 里写“遇到错误不要编造”。但工具仍返回空字符串，模型根本不知道这是错误。反转点是：不能要求模型从语义上猜工具状态；工具协议必须把失败作为一等结果返回。
- **Anti-Patterns Avoided**: [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-01 · 静默失败（Silent Failure）— 🔴最危险|ANTI-01]]（失败伪装成功） · [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-10 · 工具返回值盲信（Tool Output Blind Trust）— 🟠|ANTI-10]]（把空返回当正常内容）
- **Evaluation Method**: [[agent-decision-system/05_EVAL-CHECKLIST#Q-08 · 对自主系统：轨迹合理吗，不只结果？🔴（仅自主系统）|Q-08]] + [[agent-decision-system/05_EVAL-CHECKLIST#Q-03 · 它错得起吗——失败廉价可查？🔴|Q-03]]。故障注入：权限不足、文件损坏、工具超时、部分读取，检查 Agent 是否显式报告而非补洞。
- **Final Solution**: 工具协议显式化失败；Agent 输出支持 partial result；最终报告带 coverage 表。读不到文件时系统宁可交付“不完整但诚实”的报告，也不交付“完整但假的”报告。
- **Lessons Learned**: ① Agent 最危险的不是失败，是失败后假装成功。② 错误处理不能只写在 prompt 里，必须写进工具协议。③ partial report 比伪完整报告更可靠。④ trace 是调试 Agent 的生命线。
## Case 15 · 无 trace 的 Agent 无法调试

- **Problem**: 一个多步 Agent 偶尔给错结果，但没有 trace，团队花数周也定位不了是哪步。
- **Context**: 只记录最终输出。
- **Constraints**: 需要能调试。
- **Analysis**: 不可观测的系统无法调试。黑箱 Agent。
- **Relevant Laws**: 可观测性
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-02 · ReAct（推理+行动交替）|PAT-02]]（ReAct + 全程 trace）
- **Architecture Decision**: 记录每轮的 Thought/Action/Observation，加 trace id。
- **Anti-Patterns Avoided**: 黑箱 Agent。
- **Evaluation Method**: 注入错误，测量有无 trace 的定位速度。
- **Final Solution**: 加 trace 后诡异 bug 几分钟定位到某步工具返回空。
- **Lessons Learned**: trace 是 Agent 的 print 调试法，第一天就要有。

## Case 16 · Agent 照字面执行酿成损失

- **Problem**: 用户说"把这些文件清理一下"，Agent 理解为"删除"并执行，用户其实想"整理归类"。
- **Context**: 文件助手 Agent，有删除权限。
- **Constraints**: 歧义指令 + 不可逆操作。
- **Analysis**: 意图字面主义 + 不可逆操作无审批。指令是意图的有损压缩，歧义时该问不该猜。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-09 · 不可逆慢做可逆快做（Reversibility Governs Caution）|LAW-09]]（可逆性）· 意图-指令鸿沟 · [[agent-decision-system/04_LAW-INVARIANTS#LAW-12 · 判断力稀缺，问责不能止于 AI（Judgment Scarce + Traceable Accountability）|LAW-12]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-18 · Human-in-the-Loop（人在回路）|PAT-18]]（不可逆操作前确认）+ 澄清而非猜
- **Architecture Decision**: 歧义指令先反问澄清；删除类不可逆操作前必须确认。
- **Anti-Patterns Avoided**: 意图字面主义 + [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-04 · 过度自动化（Over-Automation）— 🔴|ANTI-04]]（不可逆全自动）。
- **Evaluation Method**: 用歧义指令测试是否澄清；不可逆操作是否有确认。
- **Final Solution**: 澄清层 + 不可逆确认，避免了误删。
- **Lessons Learned**: 服务真实意图而非字面；不可逆操作永远确认。

## Case 17 · 给 Agent 太多工具反而变差

- **Problem**: 给 Agent 配了 20 个工具后，它经常选错工具或纠结，不如只有 5 个时可靠。
- **Context**: 不断加工具"以防万一"。
- **Constraints**: 需要好的工具选择。
- **Analysis**: 工具太多导致选择困难，决策质量下降。能力堆砌 ≠ 有用。
- **Relevant Laws**: 复杂度累积 · [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-04 · Tool Use / Function Calling|PAT-04]]（少而专）
- **Architecture Decision**: 砍到 5-6 个核心工具；低频工具按需动态加载或路由。
- **Anti-Patterns Avoided**: 能力堆砌。
- **Evaluation Method**: 对比工具数量与工具选择准确率。
- **Final Solution**: 精简工具集，选择准确率和可靠性回升。
- **Lessons Learned**: 工具从 3-5 个起步。多不等于强，选择成本是真实的。

## Case 18 · Agent 的 system prompt 当架构用

- **Problem**: 所有安全约束、业务逻辑、流程都写在 Agent 的 system prompt 里，一次 prompt injection 绕过了全部"约束"。
- **Context**: 提示即架构。
- **Constraints**: 安全约束必须可靠。
- **Analysis**: 提示层约束可被绕过，不是可靠防线。约束行为要靠权限。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-05 · 一切输入皆指令 + 权限胜过自觉（Input-Is-Instruction + Permission）|LAW-05]]（权限胜过自觉）· 确定性优先
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-15 · Guardrails / Validation（护栏）|PAT-15]]（Guardrails）+ 权限层
- **Architecture Decision**: 确定性逻辑移到代码，安全约束移到权限层，prompt 只管语言理解。
- **Anti-Patterns Avoided**: 提示即架构。
- **Evaluation Method**: 红队测试 prompt 约束能否被绕过，权限层是否兜住。
- **Final Solution**: 关键约束在权限层，即使 prompt 被绕过也无法造成实际破坏。
- **Lessons Learned**: 靠权限不靠自觉。prompt 的"禁止"是缓解，权限才是防御。

## Case 19 · 探索型任务被硬做成固定计划

- **Problem**: 一个探索性研究任务被制定了精确的 20 步计划，执行到第 2 步就发现现实完全不同，计划全废。
- **Context**: 用 Planner 给探索型任务做详细规划。
- **Constraints**: 任务的下一步依赖当前发现。
- **Analysis**: 有些任务无法事前规划（不可预验证），该边做边想。
- **Relevant Laws**: 不可预验证 · [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-02 · ReAct（推理+行动交替）|PAT-02]]（ReAct 边做边看）而非 [[agent-decision-system/02_PATTERN-CARDS#PAT-09 · Planner-Executor（规划-执行）|PAT-09]] 的僵化规划
- **Architecture Decision**: 探索型任务用 ReAct + 轻量的滚动规划（每步后更新），不预设固定 20 步。
- **Anti-Patterns Avoided**: 过度规划。
- **Evaluation Method**: 对比固定规划 vs 滚动规划的完成率。
- **Final Solution**: ReAct + 交错规划，适应了探索中的变化。
- **Lessons Learned**: 可规划的规划，需探索的边做边看。别给探索型任务上僵化计划。

## Case 20 · Agent 被赋予不匹配的自主权

- **Problem**: 一个新 Agent 在一个它可靠性还没验证的任务上被授予完全自主权，第一周就自主执行了一个错误的对外操作。
- **Context**: 追求全自动，未分诊可逆性。
- **Constraints**: 该任务不可逆、高风险。
- **Analysis**: 自主性没被可靠性和可逆性证明。在不可逆高风险任务上的高自主 = 纯风险。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-09 · 不可逆慢做可逆快做（Reversibility Governs Caution）|LAW-09]]（可逆性）· [[agent-decision-system/04_LAW-INVARIANTS#LAW-08 · 信任应随可靠性而非能力增长（Trust-Reliability Scissors）|LAW-08]]（信任-可靠性剪刀）· [[agent-decision-system/04_LAW-INVARIANTS#LAW-12 · 判断力稀缺，问责不能止于 AI（Judgment Scarce + Traceable Accountability）|LAW-12]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-18 · Human-in-the-Loop（人在回路）|PAT-18]]（人在回路）
- **Architecture Decision**: 自主性匹配可靠性——新任务先人工审批，积累可靠性数据后再逐步放开。
- **Anti-Patterns Avoided**: [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-04 · 过度自动化（Over-Automation）— 🔴|ANTI-04]] + 自主性错配。
- **Evaluation Method**: [[agent-decision-system/05_EVAL-CHECKLIST#Q-02 · 它可靠吗——看分布不是峰值？🔴|Q-02]]（先测可靠性分布）再决定自主程度。
- **Final Solution**: 分级授权，可靠性证明到哪，自主放开到哪。
- **Lessons Learned**: 自主是成本不是美德。授予的自主性必须被可靠性和可逆性证明。
