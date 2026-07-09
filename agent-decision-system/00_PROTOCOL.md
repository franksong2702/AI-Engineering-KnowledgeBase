---
type: agent-decision-system
abstraction_layer: 操作层（机器可调用投影）
aliases: [AgentDecisionSystem-PROTOCOL]
role: protocol
date: 2026-07-06
audience: AI-Agent
tags: [AgentDecisionSystem, 操作手册, 协议]
---

# Agent Decision System · 调用协议（00_PROTOCOL）

> AUDIENCE: 未来的 AI Agent（本手册面向机器读者，人也可读）。
> PURPOSE: 把《AI Engineering Knowledge Base》15 本书转成可在推理时直接查询的决策系统。原有书目不变，本系统是它们的操作层投影。
> SELF-CONTAINED: 本决策系统可独立使用，无需读原书；需要深度时再回溯对应书目。

## SYSTEM OVERVIEW

```
本系统 = 1 个协议(本文) + 5 个可查询模块:
  01_SITUATION-ROUTER   ── 核心。输入"你的处境"→输出 6 字段决策
  02_PATTERN-CARDS      ── 20 个"该做什么"的操作卡(When/Decision/Actions/…)
  03_ANTIPATTERN-DETECTORS ── 12 个"别做什么"的检测器(7 字段卡：检测→纠正)
  04_LAW-INVARIANTS     ── 13 条恒成立的约束(始终校验，不可违反)
  05_EVAL-CHECKLIST     ── 上线/交付前必答的评价清单
```

## HOW AN AGENT USES THIS SYSTEM (决策循环)

在任何非平凡任务的规划阶段，执行以下循环：

```
STEP 1 · CLASSIFY   识别你的处境 → 查 01_SITUATION-ROUTER 找匹配条目
STEP 2 · DIAGNOSE   读该条目的 Diagnosis，确认根本问题
STEP 3 · CONSTRAIN  对照 04_LAW-INVARIANTS，列出本处境下不可违反的约束
STEP 4 · SELECT     从 Recommended Patterns 选做法 → 查 02_PATTERN-CARDS 取操作细节
STEP 5 · GUARD      对照 Avoid + 03_ANTIPATTERN-DETECTORS，检查你的方案是否落入陷阱
STEP 6 · PLAN       输出你的行动方案
STEP 7 · VERIFY     对照 Evaluation Checklist + 05_EVAL-CHECKLIST，定义"怎么算做对了"
```

**MANDATORY**: STEP 3 (约束) 和 STEP 7 (验证) 不可跳过。约束防止你造成不可逆损害，验证防止你自信地交付错误。

## OUTPUT FORMAT (决策系统的标准输出)

当 Agent 查询本系统、或向人/其他 Agent 报告一个决策时，用以下 6 字段格式：

```
Situation:            <一句话描述当前处境>
Diagnosis:            <根本问题是什么，属于哪一类>
Relevant Laws:        <本处境下必须尊重的约束，引 04 的 LAW-id>
Recommended Patterns: <该用的做法，引 02 的 PATTERN-id + 一句话理由>
Avoid:                <该避开的陷阱，引 03 的 ANTI-id + 一句话>
Evaluation Checklist: <怎么判断做对了，可勾选的条目>
```

## KNOWLEDGE-UNIT CARD FORMAT (每个知识单元的 7 字段)

02–03 里的每个知识单元卡片，用以下 7 字段（供 Agent 精确取用）；04 的定律卡用 INVARIANT / IMPLICATION / VIOLATION / CHECK / SOURCE 5 字段（SOURCE 为源 Law 溯源行，编号空间仍隔离）；05 的评价问题用 4 字段问答式（见各文件头部声明）：

```
When to use:          <什么条件下适用>
When not to use:      <什么条件下不适用/是过度设计>
Decision criteria:    <可判定的选用判据，尽量二元/可测>
Related concepts:     <关联的 LAW/PATTERN/ANTI id>
Common mistakes:      <采用它时最常见的错误>
Recommended actions:  <具体该做的动作，命令式>
Example reasoning path: <一条示例推理链，展示如何从处境走到应用>
```

## GLOBAL PRIORITY RULES (当条目冲突时的仲裁)

Agent 在应用本系统时，遇到冲突按以下优先级仲裁（高者胜）：

1. **SAFETY FIRST** — 涉及不可逆/高危操作时，LAW-INVARIANTS 的安全约束(LAW-05 权限、LAW-09 可逆性)压倒一切效率考量。宁可停下问人。
2. **SIMPLICITY DEFAULT** — 有多个可行方案时，默认选最简单的(LAW/原则:简单优先)。复杂/自主/多Agent必须被收益证明，否则降级。
3. **VERIFIABILITY GATE** — 不能被廉价验证的方案是负债；优先选输出可验证的方案(为验证而设计)。
4. **PROXY SKEPTICISM** — 任何被优化的指标都是代理；优化前先问"它会怎么被钻空子"(古德哈特)。
5. **CALIBRATED UNCERTAINTY** — 不确定时显式标注，不伪装确定；信任跟随实测可靠性而非感知能力。

## META-INSTRUCTION (给 Agent 的元指令)

- 本系统是脚手架不是圣经。它有边界（见每条的 When-not-to-use）。遇到系统未覆盖的处境，回退到 04_LAW-INVARIANTS（它们最普适）+ GLOBAL PRIORITY RULES 自行推导。
- 不要机械套用。先判断处境类型（简单任务直接做，别套系统；复杂/高风险/不确定才值得走完决策循环）。
- 当你的方案与某条 LAW-INVARIANT 冲突，是你的方案错，不是定律错——除非你能明确指出该定律在此处境的适用边界失效。
- 记录你的决策路径（Situation→Diagnosis→选择理由），供事后复盘和被验证。

## SOURCE MAP (回溯到原书)

| 模块 | 深度来源(原书) |
|------|--------------|
| LAW-INVARIANTS | [[laws-of-ai-engineering/00_INDEX\|Laws]] · [[foundation-of-ai-engineering/00_INDEX\|Foundation]] |
| PATTERN-CARDS | [[llm-design-patterns/00_INDEX\|Design Patterns]] · [[multi-agent-patterns-handbook/00_INDEX\|Multi-Agent]] · [[agent-bible/00_INDEX\|Agent Bible]] |
| ANTIPATTERN-DETECTORS | [[ai-engineering-anti-patterns/00_INDEX\|Anti-Patterns]] |
| EVAL-CHECKLIST | [[evaluation-of-ai-systems/00_INDEX\|Evaluation]] |
| 数据/模型相关条目 | [[data-foundation-of-ai-systems/00_INDEX\|Data Foundation]] · [[model-adaptation/00_INDEX\|Model Adaptation]] |
| 生产部署相关(SIT-17等) | [[ai-systems-in-production/00_INDEX\|AI Systems in Production]] |
| 多模态输入相关 | [[multimodal-systems/00_INDEX\|Multimodal Systems]] |
| 全库骨架 | [[The-Constitution-of-AI-Engineering\|The Constitution]] |

### LAW-INVARIANTS Source Map

> 这张表只说明 `LAW-01`–`LAW-13` 的来源关系，不改变 [[04_LAW-INVARIANTS|04 LAW-INVARIANTS]] 的运行时定义。  
> `Primary source` 是主来源；`Related source` 是辅助边界、相邻原则或上游模块。组合来源不强行压成单条 Law。

| ADS LAW | Source type | Primary source | Related source / note |
|---|---|---|---|
| `LAW-01` 验证易于生成 | 直接压缩 | [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 13 — 可委托性定律（Delegability Law）\|Law 13]]；[[laws-of-ai-engineering/07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）\|Law 64]] |
| `LAW-02` 压缩必然有损→会幻觉 | 组合压缩 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] + [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]] | [[laws-of-ai-engineering/01_信息与压缩定律#Law 5 — 检索优于记忆定律（Retrieval-Over-Memorization Law）\|Law 5]]；[[laws-of-ai-engineering/07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）\|Law 62]] |
| `LAW-03` 分布内才可靠 + 校准 | 组合压缩 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布内可靠定律（In-Distribution Reliability Law）\|Law 7]] + [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]] | [[laws-of-ai-engineering/03_统计与泛化定律#Law 25 — 分布漂移定律（Distribution Shift Law）\|Law 25]]；[[laws-of-ai-engineering/07_认识论与真理定律#Law 63 — 不确定性外显定律（Surface-Uncertainty Law）\|Law 63]] |
| `LAW-04` 古德哈特 | 直接压缩 | [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24]] | [[laws-of-ai-engineering/10_对抗与安全定律#Law 93 — 对抗性古德哈特定律（Adversarial-Goodhart Law）\|Law 93]]；[[evaluation-of-ai-systems/00_INDEX\|Evaluation]] |
| `LAW-05` 一切输入皆指令 + 权限胜过自觉 | 组合压缩 | [[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）\|Law 87]] + [[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）\|Law 94]] | [[laws-of-ai-engineering/05_接口与边界定律#Law 47 — 最小权限定律（Least-Privilege Law）\|Law 47]]；[[laws-of-ai-engineering/10_对抗与安全定律#Law 88 — 致命三重奏定律（Lethal-Trifecta Law）\|Law 88]]；[[laws-of-ai-engineering/10_对抗与安全定律#Law 90 — 无可靠转义定律（No-Reliable-Escaping Law）\|Law 90]]；[[laws-of-ai-engineering/10_对抗与安全定律#Law 92 — 数据即攻击面定律（Data-Is-Attack-Surface Law）\|Law 92]] |
| `LAW-06` 误差多步累积 + 恢复优于预防 | 组合压缩 | [[laws-of-ai-engineering/02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）\|Law 14]] + [[laws-of-ai-engineering/08_可靠性与失败定律#Law 77 — 恢复优于预防定律（Recovery-Over-Prevention Law）\|Law 77]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 17 — 幂等性定律（Idempotency Law）\|Law 17]]；[[laws-of-ai-engineering/02_计算与验证定律#Law 21 — 停机与预算定律（Termination-Budget Law）\|Law 21]]；[[laws-of-ai-engineering/04_系统与控制定律#Law 42 — 优雅降级定律（Graceful-Degradation Law）\|Law 42]] |
| `LAW-07` 上下文即状态 | 直接压缩 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 2 — 上下文即状态定律（Context-is-State Law）\|Law 2]] | [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]]；[[laws-of-ai-engineering/01_信息与压缩定律#Law 10 — 有效注意力有限定律（Finite-Effective-Attention Law）\|Law 10]] |
| `LAW-08` 信任应随可靠性而非能力增长 | 直接压缩 + 成组 | [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84]] | [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）\|Law 95]]；[[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]]；[[human-ai-collaboration-foundation/00_INDEX\|Human-AI Collaboration]] |
| `LAW-09` 不可逆慢做可逆快做 | 直接压缩 | [[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）\|Law 74]] | [[laws-of-ai-engineering/08_可靠性与失败定律#Law 72 — 爆炸半径定律（Blast-Radius Law）\|Law 72]]；[[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] |
| `LAW-10` 简单优先 | 组合压缩 / 跨层来源 | [[laws-of-ai-engineering/04_系统与控制定律#Law 41 — 复杂度累积定律（Complexity-Accumulation Law）\|Law 41]] + [[laws-of-ai-engineering/11_演化与元定律#Law 99 — 简单性存活定律（Simplicity-Survives Law）\|Law 99]] | [[foundation-of-ai-engineering/00_INDEX\|Foundation]] 的简单优先判断；[[laws-of-ai-engineering/06_经济与资源定律#Law 57 — 规模效应定律（Scale-Effects Law）\|Law 57]] |
| `LAW-11` 确定性优先 | 直接压缩 | [[laws-of-ai-engineering/02_计算与验证定律#Law 18 — 确定性优先定律（Determinism-First Law）\|Law 18]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 13 — 可委托性定律（Delegability Law）\|Law 13]]；[[laws-of-ai-engineering/03_统计与泛化定律#Law 23 — 偏差-方差定律（Bias-Variance Law）\|Law 23]] |
| `LAW-12` 判断力稀缺，责任不可委托 | 组合压缩 / 跨层来源 | [[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）\|Law 100]] + [[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]]；[[foundation-of-ai-engineering/00_INDEX\|Foundation]]；[[human-ai-collaboration-foundation/00_INDEX\|Human-AI Collaboration]] |
| `LAW-13` 信息守恒，垃圾进垃圾出 | 直接压缩 + 上游数据前提 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）\|Law 4]] | [[laws-of-ai-engineering/01_信息与压缩定律#Law 5 — 检索优于记忆定律（Retrieval-Over-Memorization Law）\|Law 5]]；[[data-foundation-of-ai-systems/00_INDEX\|Data Foundation]]；[[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] |

→ 从这里开始：[[01_SITUATION-ROUTER|01 情境路由器]]
