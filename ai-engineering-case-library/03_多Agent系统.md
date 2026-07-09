---
type: case-library
abstraction_layer: 应用（案例层）
date: 2026-07-06
course: ai-engineering-case-library
category: 多Agent系统
tags: [案例, 多Agent]
---

# 类三 多 Agent 系统（Case 21–30）
> 决策路由入口：[[agent-decision-system/01_SITUATION-ROUTER#SIT-06 · 我在考虑用多个 Agent|SIT-06]] / [[agent-decision-system/01_SITUATION-ROUTER#SIT-09 · 长任务 / 上下文在膨胀|SIT-09]] / [[agent-decision-system/01_SITUATION-ROUTER#SIT-14 · 我要在多个方案间做决策|SIT-14]] → [[agent-decision-system/01_SITUATION-ROUTER|Situation Router]]

---

## Case 21 · 8 个 Agent 做单 Agent 能做的事（深度版）

- **Problem**: 一个"竞品分析报告"任务用了 8 个 Agent（调研员×3、分析师、评论家、编辑、事实核查、总编），成本 8 倍、慢 5 倍，质量没比单 Agent 好。
- **Context**: 为"看起来专业"按人类团队的组织架构设计的多 Agent 系统（[[multi-agent-patterns-handbook/00_INDEX|拟人化分工]]），从没跑过单 Agent 基线。单次任务 token 消耗约 40 万，其中 Agent 间转发的重复上下文占近一半。
- **Constraints**: 需要证明"多"的价值；月预算有限。
- **Analysis**: 逐环节审计发现三类浪费——①三个调研员检索了大量重叠内容（无分工边界）；②"评论家"的意见 90% 被"编辑"原样忽略（对抗环节没有客观锚，沦为仪式——无目的反思（[[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-09 · 无目的反思（Reflection Without Purpose）— 🟠|ANTI-09]]）的多体版)；③每次交接都全量转发对话历史（token 爆炸，违反 [[multi-agent-patterns-handbook/00_INDEX|传结论不传对话]]）。多 Agent 的三个正当理由（上下文隔离/真并行/权限隔离）一个都不占：任务单一主题不需要隔离，环节全是串行，无权限差异。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]] · 规模不经济
- **Relevant Patterns**: 先跑单 Agent 基线

**审计数字（教学编排值）**：

```
8-Agent 版：40万 token/次 · 22 分钟 · 质量评分 7.2/10（盲评）
拆解：有效信息生成 ~35%；重复检索 ~25%；历史转发 ~30%；仪式性评审 ~10%
单 Agent 基线（同模型，一段精心组织的长流程 prompt + 工具）：
        6万 token/次 · 4 分钟 · 质量评分 7.4/10
```

- **Architecture Decision**: 降级为单 Agent + 两个确定性组件：检索去重的资料准备段（工作流），和一次带 rubric 的出口自检（保留了"评论家"里唯一有效的部分——对照检查清单，而非自由评论）。
- **第一次修复与反转**: 最初只是砍掉 3 个明显冗余的 Agent（8→5），成本降了但质量掉了 0.5 分——因为砍的时候把"事实核查"也当冗余砍了，而它是唯一接了搜索工具做交叉验证的环节。回滚后按"砍掉它系统会变差吗"逐个检验：7 个环节里只有事实核查通过检验。**"有罪推定"要逐个执行，不是氛围性地砍一半。**
- **Anti-Patterns Avoided**: [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-07 · 多 Agent 过度设计（Multi-Agent Overkill）— 🟠|ANTI-07]]（多 Agent 过度设计）；[[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-09 · 无目的反思（Reflection Without Purpose）— 🟠|ANTI-09]]（无目的反思——无锚评审仪式是其多体版）。
- **Evaluation Method**: 单 vs 多的质量（盲评 + rubric）/成本/延迟三维对照，各跑 20 个任务取分布（[[agent-decision-system/05_EVAL-CHECKLIST#Q-02 · 它可靠吗——看分布不是峰值？🔴|Q-02]]：看分布不是单次）。
- **Final Solution**: 单 Agent + 资料准备工作流 + 出口自检 + 保留事实核查：成本降约 80%，延迟降到 1/5，质量持平略升；事实错误率（核查环节的存在价值）与 8-Agent 版相当。
- **Lessons Learned**: ① 对多 Agent 有罪推定，且逐个环节执行"砍掉会变差吗"，不是氛围性精简。② 拟人化分工（按人类职位设 Agent）是多 Agent 过度设计的头号来源——组织架构不是信息架构。③ 对抗/评审环节没有客观锚就是仪式。④ 降级不是全砍：把有效环节固化下来（事实核查、rubric 自检）。⑤ 数字为教学编排值。

## Case 22 · Agent 间传完整对话历史导致爆炸

- **Problem**: 5 个 Agent 互相传递完整对话历史，第三轮上下文就爆了，每个 Agent 被无关信息淹没。
- **Context**: Agent 间直接转发全部过程。
- **Constraints**: token 和质量。
- **Analysis**: 通信爆炸——传过程而非结论，token 指数增长，噪声跨 Agent 传染。
- **Relevant Laws**: 信噪比 · [[agent-decision-system/04_LAW-INVARIANTS#LAW-07 · 上下文即状态（Context Is State）|LAW-07]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-17 · Orchestrator-Workers（协调者-执行者）|PAT-17]]（传结构化结论）
- **Architecture Decision**: Agent 间只传结构化结论 + 证据 + 置信度，不传原始对话；任务描述自包含。
- **Anti-Patterns Avoided**: 通信爆炸。
- **Evaluation Method**: 测量通信 token 占比和信息传递无损率。
- **Final Solution**: 结论式通信，token 大降，质量提升。
- **Lessons Learned**: 传结论不传对话。Agent 间通信要瘦。

## Case 23 · 委员会全是同一个模型的伪多样

- **Problem**: 一个"专家委员会"由 5 个同模型同 prompt 的 Agent 组成，意见几乎一致，"审议"毫无价值。
- **Context**: 用多个同源 Agent 模拟多视角。
- **Constraints**: 需要真正的多视角。
- **Analysis**: 伪多样性——同模型换头衔不产生不同视角。集成的收益需要错误去相关。
- **Relevant Laws**: 集成去相关 · Multi-Agent 定律 2
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-14 · Debate / Committee（辩论/委员会）|PAT-14]]（真差异化的委员会）
- **Architecture Decision**: 用不同基座模型 + 不同知识/工具配置的成员，或干脆合并（若无真多样）。
- **Anti-Patterns Avoided**: 重复角色 / 伪多样。
- **Evaluation Method**: 测量成员输出的相关性（高相关=伪多样）。
- **Final Solution**: 异构成员，视角真正多样，审议产生价值。
- **Lessons Learned**: 多视角要靠真差异化（不同模型/知识/工具），不是换头衔。

## Case 24 · 共识成瘾碾压了正确的少数派

- **Problem**: 一个多 Agent 决策系统，一个 Agent 正确地反对，但系统为"达成共识"采纳了错误的多数意见。
- **Context**: 系统执着于让所有 Agent 一致。
- **Constraints**: 高质量判断优先于一致。
- **Analysis**: 共识成瘾——为一致牺牲正确性，抹杀了正确的少数派。
- **Relevant Laws**: 贝叶斯更新 · 集成去相关
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-14 · Debate / Committee（辩论/委员会）|PAT-14]]（保留少数派的委员会）
- **Architecture Decision**: 独立意见先行防从众；基于论据裁决而非追求趋同；保留少数派意见。
- **Anti-Patterns Avoided**: 共识成瘾。
- **Evaluation Method**: 测少数派正确意见的存活率。
- **Final Solution**: 保留分歧的审议机制，正确的少数意见被采纳。
- **Lessons Learned**: 高质量的分歧胜过低质量的共识。别为一致牺牲正确。

## Case 25 · 协调者过载成了瓶颈

- **Problem**: 一个 orchestrator 既分派又执行又管状态又决策，上下文很快超限，成为系统瓶颈和单点故障。
- **Context**: 强大的中心协调者。
- **Constraints**: 可扩展、无单点。
- **Analysis**: 协调者过载——God Agent 的多 Agent 版，成了瓶颈和单点。
- **Relevant Laws**: 瓶颈定律 · 单点故障 · 关注点分离
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-09 · Planner-Executor（规划-执行）|PAT-09]]（协调-执行分离）
- **Architecture Decision**: 协调者只做协调（拆解/分派/汇总），执行给 workers，状态外置到文件。
- **Anti-Patterns Avoided**: 协调者过载。
- **Evaluation Method**: 测协调者的上下文占用和是否成瓶颈。
- **Final Solution**: 轻量协调者 + 独立 workers，瓶颈消除。
- **Lessons Learned**: 协调者只协调。别让它又协调又干活。

## Case 26 · 子 Agent 任务不自包含跑偏

- **Problem**: 协调者派任务"继续之前的分析"，子 Agent 没有"之前"的上下文，只能瞎猜，产出跑偏。
- **Context**: 假设子 Agent 有全局视野。
- **Constraints**: 子 Agent 上下文隔离。
- **Analysis**: 子任务不自包含。子 Agent 看不到协调者的上下文。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-07 · 上下文即状态（Context Is State）|LAW-07]]（上下文即状态）
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-17 · Orchestrator-Workers（协调者-执行者）|PAT-17]]（自包含任务描述）
- **Architecture Decision**: 任务描述包含子 Agent 需要的全部背景，不依赖它"知道"上文。
- **Anti-Patterns Avoided**: 子任务不自包含。
- **Evaluation Method**: 检查任务描述能否被无上下文的 Agent 独立理解。
- **Final Solution**: 自包含任务描述，子 Agent 不再跑偏。
- **Lessons Learned**: 子 Agent 有独立上下文。任务书必须自包含。

## Case 27 · 一个 Agent 的幻觉污染了全系统（深度版）

- **Problem**: 研究 Agent 编造了一个数据，核查 Agent 没核出来，撰写 Agent 当真引用，最终报告建立在假数据上。
- **Context**: 多 Agent 流水线分为 Researcher → Checker → Writer。Researcher 负责找资料，Checker 负责“审核”，Writer 负责成稿。每个 Agent 只收到上游结论摘要，没有收到证据包。
- **Constraints**: 关键事实必须可追溯；上游错误不能被下游放大；核查必须核证据，不是核语气。
- **Analysis**: 多 Agent 会把一个局部幻觉变成系统级事实。下游 Agent 天然倾向相信上游角色已经完成职责；如果结论不带证据、置信度和来源，Checker 很容易只检查格式与合理性，而不是重新验证事实。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-06 · 误差多步累积 + 恢复优于预防（Error Compounding + Recovery）|LAW-06]]（误差沿链累积） · [[agent-decision-system/04_LAW-INVARIANTS#LAW-08 · 信任应随可靠性而非能力增长（Trust-Reliability Scissors）|LAW-08]]（不能因角色名而过度信任） · [[agent-decision-system/04_LAW-INVARIANTS#LAW-01 · 验证易于生成（Verification > Generation）|LAW-01]]（关键事实要验证）
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-17 · Orchestrator-Workers（协调者-执行者）|PAT-17]]（带证据的 worker 输出） + [[agent-decision-system/02_PATTERN-CARDS#PAT-06 · LLM-as-Judge（模型即裁判）|PAT-06]]（校准后的检查） + [[agent-decision-system/02_PATTERN-CARDS#PAT-15 · Guardrails / Validation（护栏）|PAT-15]]（关键事实护栏）

**Trace 片段（幻觉传播）**：

```text
Researcher output:
“2024 年该市场增长率为 23%，来源：行业报告。”   # 无链接、无页码

Checker output:
“结论结构完整，数字看起来合理，通过。”             # 检查了语气和格式，没有查来源

Writer output:
“由于 2024 年市场增长率达到 23%，我们建议加大投入。”

人工复核：所谓行业报告不存在，23% 是 Researcher 编出来的。
```

- **Architecture Decision**: Worker 输出不再是纯结论，而是 evidence packet：`claim`、`source_url/path`、`quote_or_table_ref`、`confidence`、`verification_status`。Checker 的任务从“看结论是否合理”改为“抽样打开来源、验证 claim 是否被证据支持”。Writer 只能引用 `verified=true` 的关键事实。
- **第一次修复与反转**: 第一版修复是“新增一个 Checker Agent”。结果失败仍然发生，因为 Checker 没有证据，也没有核查 rubric，只能评价文本是否像真的。反转点是：多一个角色不等于多一层可靠性；只有证据边界和验证职责清楚，角色才有意义。
- **Anti-Patterns Avoided**: [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-10 · 工具返回值盲信（Tool Output Blind Trust）— 🟠|ANTI-10]]（下游盲信上游） · [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-07 · 多 Agent 过度设计（Multi-Agent Overkill）— 🟠|ANTI-07]]（加角色但不加可靠性） · [[agent-decision-system/03_ANTIPATTERN-DETECTORS#ANTI-01 · 静默失败（Silent Failure）— 🔴最危险|ANTI-01]]（假事实静默传播）
- **Evaluation Method**: [[agent-decision-system/05_EVAL-CHECKLIST#Q-08 · 对自主系统：轨迹合理吗，不只结果？🔴（仅自主系统）|Q-08]] + [[agent-decision-system/05_EVAL-CHECKLIST#Q-07 · 它的置信度校准吗？🟠|Q-07]]。故意注入一个假 claim，检查它是否被证据包、Checker、Writer 三层拦住。
- **Final Solution**: 所有关键 claim 必须带证据包；Checker 抽查来源；Writer 只使用已验证事实。系统允许交付“该数据未找到可靠来源”，不允许把无来源数字写成结论。
- **Lessons Learned**: ① 多 Agent 放大协作能力，也放大错误传播。② 角色名不是可靠性机制。③ 结论必须带证据、置信度和验证状态。④ 没有证据包的 Checker 只是另一个会说话的模型。
## Case 28 · 多 Agent 涌现出互相恭维的循环

- **Problem**: 一个"自组织"多 Agent 系统涌现出互相赞同和补充的循环，跑很久没产出可用结论，成本高企。
- **Context**: 去中心化，让 Agent"自由讨论涌现方案"。
- **Constraints**: 要收敛、要可控。
- **Analysis**: 去中心化浪漫主义——自由讨论在生产中不收敛、不可控，涌现出恭维循环。
- **Relevant Laws**: 停机与预算 · 涌现不可预测 · [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]]
- **Relevant Patterns**: [[agent-decision-system/02_PATTERN-CARDS#PAT-09 · Planner-Executor（规划-执行）|PAT-09]]/[[agent-decision-system/02_PATTERN-CARDS#PAT-17 · Orchestrator-Workers（协调者-执行者）|PAT-17]]（中心化编排）+ 明确终止
- **Architecture Decision**: 改用中心化 orchestrator + 明确终止条件；监控涌现行为。
- **Anti-Patterns Avoided**: 去中心化浪漫主义 + 涌现盲区。
- **Evaluation Method**: 监控涌现行为（不只测设计的行为）。
- **Final Solution**: 中心化编排，收敛可控。
- **Lessons Learned**: 默认从中心化开始。"Agent 自由讨论涌现"在生产里几乎总是灾难。

## Case 29 · 层级太深导致传话失真

- **Problem**: 一个三层 Agent 系统，根协调者基于层层失真的摘要做决策，与实际严重脱节。
- **Context**: 过早引入多层层级。
- **Constraints**: 决策要基于真实情况。
- **Analysis**: 层级过深，每层交信息损耗税，根节点看到的是"摘要的摘要"。
- **Relevant Laws**: 层级信息损耗 · [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]]
- **Relevant Patterns**: 扁平化 + 关键信息越级直达
- **Architecture Decision**: 扁平化到单层协调；关键数字/风险项设越级直达通道（原样上传不逐层改写）。
- **Anti-Patterns Avoided**: 层级过深。
- **Evaluation Method**: 测信息从叶到根的失真度。
- **Final Solution**: 扁平结构 + 关键信息直达，决策贴合现实。
- **Lessons Learned**: 层级是被逼出来的，不是设计出来的。先试单层，关键信息设直达通道。

## Case 30 · 多 Agent 掩盖了单体的根本缺陷

- **Problem**: 一个 Agent 因缺乏评测而不可靠，团队拆成 5 个 Agent 想解决，结果 5 个都不可靠，还多了协调地狱。
- **Context**: 把多 Agent 当银弹。
- **Constraints**: 先解决根本问题。
- **Analysis**: 单体的根本缺陷（缺评测）不会因拆成多个而消失——现在有 5 个有同样缺陷的 Agent 加通信问题。
- **Relevant Laws**: [[agent-decision-system/04_LAW-INVARIANTS#LAW-10 · 简单优先（Simplicity First）|LAW-10]] · 何时多 Agent
- **Relevant Patterns**: 先把单 Agent 调好（评测/prompt/逻辑）
- **Architecture Decision**: 回退——先给单 Agent 建评测调好，再判断是否真需要多 Agent。
- **Anti-Patterns Avoided**: 多 Agent 掩盖单体缺陷。
- **Evaluation Method**: 先建评测确认单 Agent 达标。
- **Final Solution**: 单 Agent 加评测调好后，发现根本不需要多 Agent。
- **Lessons Learned**: 先单体达标再编排。拆成多个不会修复根本缺陷。
