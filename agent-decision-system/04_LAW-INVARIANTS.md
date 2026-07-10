---
type: agent-decision-system
abstraction_layer: 操作层（机器可调用投影）
role: law-invariants
date: 2026-07-06
audience: AI-Agent
tags: [AgentDecisionSystem, 定律约束, Invariants]
---

# Agent Decision System · 定律约束（04_LAW-INVARIANTS）

> 13 条恒成立的约束。与模式/反模式不同，定律**始终适用**——任何处境都要校验。它们是决策系统的公理层，冲突时按 [[00_PROTOCOL|GLOBAL PRIORITY RULES]] 仲裁。深度→[[laws-of-ai-engineering/00_INDEX|Laws]] / [[foundation-of-ai-engineering/00_INDEX|Foundation]]。
> 每条格式：INVARIANT(不变式) · IMPLICATION(对Agent的含义) · VIOLATION(违反后果) · CHECK(自检) · SOURCE(源 Law 溯源)。
> SOURCE 是主来源的机器可读压缩（编译进 `_machine/laws.yaml`）；含辅助来源与压缩方式的完整人读版见 [[00_PROTOCOL#LAW-INVARIANTS Source Map|PROTOCOL · Source Map]]，二者主来源逐条一致。SOURCE 只提供到 [[laws-of-ai-engineering/00_INDEX|Laws]] 正典的可追溯路径；`LAW-01`–`LAW-13` 与 `Law 1`–`Law 102` 仍是两套独立编号空间，不可互换（见 [[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]]）。

---

## LAW-01 · 先设计可靠验证器（Design for Verifiability）
- **INVARIANT**: 只有任务存在客观、廉价、独立于生成过程的验证器时，核验候选输出才通常可能比从头生成便宜；同源模型复核不是自动验证。
- **IMPLICATION**: 先设计验收器再委托；优先使用测试、schema、来源比对和确定性工具。没有廉价验证器的部分保留判断与不确定性。
- **VIOLATION**: 采信无法验证的输出，或让生成模型换个角色自评通过，等于用运气代替工程，错误会无声流入下游。
- **CHECK**: ☐ 验收标准客观吗？☐ 验证器独立且足够便宜吗？☐ 测过误放和漏报吗？
- **SOURCE**: [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）|Law 12：验证-生成不对称定律]] · [[laws-of-ai-engineering/02_计算与验证定律#Law 13 — 可委托性定律（Delegability Law）|Law 13：可委托性定律]]

## LAW-02 · 参数生成无事实来源保证（Parametric Generation Is Not Provenance）
- **INVARIANT**: 仅凭参数生成事实时，模型不是在查询带来源记录；流畅和自信不是正确性的充分证据。
- **IMPLICATION**: 需要精确事实时接入可验证源（检索/工具），把参数直答当候选而非证据，并核对来源是否真正支持断言。
- **VIOLATION**: 把模型当数据库，采信它自信编造的事实/引用/数字。
- **CHECK**: ☐ 每个关键事实能溯源到外部证据吗？☐ 来源与断言对应吗？☐ 是否把流畅度误当正确性证据？
- **SOURCE**: [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）|Law 1：有损压缩定律]] · [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）|Law 6：压缩必然丢失定律]]

## LAW-03 · 分布证据有边界 + 校准（Distribution-Bounded Evidence + Calibration）
- **INVARIANT**: 可靠性证据只适用于与评测条件充分匹配的目标分布，不能自动外推；置信度必须用目标分布样本校准。
- **IMPLICATION**: 定义目标分布和关键切片，监测漂移；任务、用户、数据或工具链变化时重新评测，并按实测校准授权范围。
- **VIOLATION**: 把旧 benchmark 成绩当模型固有属性，或把“看起来熟悉”当可靠保证，在新分布继续放权。
- **CHECK**: ☐ 评测分布与目标分布匹配吗？☐ 关键切片和边界测过吗？☐ 变化后重做校准了吗？
- **SOURCE**: [[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）|Law 7：分布证据边界定律]] · [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）|Law 26：校准定律]]

## LAW-04 · 古德哈特（Goodhart）
- **INVARIANT**: 任何指标成为优化目标就与真实目标脱钩；随优化能力增强而加剧。
- **IMPLICATION**: 优化前问"它会怎么被钻空子"；多代理交叉；保密评测集；用真实目标锚定。
- **VIOLATION**: 刷高代理(分数/满意度/奖励)，真实价值脱钩甚至反向。
- **CHECK**: ☐ 指标改善时真实目标也被独立验证改善了吗？
- **SOURCE**: [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）|Law 24：古德哈特定律]] · [[laws-of-ai-engineering/10_对抗与安全定律#Law 93 — 对抗性古德哈特定律（Adversarial-Goodhart Law）|Law 93：对抗性古德哈特定律]]

## LAW-05 · 一切输入皆指令 + 权限胜过自觉（Input-Is-Instruction + Permission）
- **INVARIANT**: 进入上下文的任何文本都可能是指令；约束行为靠权限不靠提示。
- **IMPLICATION**: 外部内容当不可信；最小权限；砍致命三重奏一角(读私有+接触不可信+对外发送)。
- **VIOLATION**: prompt injection——藏在网页/工具返回的伪指令被执行，数据泄露。
- **CHECK**: ☐ 即使被完全说服，模型有权限造成实际损害吗？
- **SOURCE**: [[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）|Law 87：一切输入皆指令定律]] · [[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）|Law 94：权限胜过自觉定律]]

## LAW-06 · 误差多步累积 + 恢复优于预防（Error Compounding + Recovery）
- **INVARIANT**: 多步成功率≈各步之积，指数衰减；故障不可避免，快速恢复应对一切。
- **IMPLICATION**: 长任务分解为可验证小步+纠错反馈；检查点+幂等重试。
- **VIOLATION**: 长链条无验证的自主流程几乎从不端到端成功；一步失败丢全部进度。
- **CHECK**: ☐ 链条里有纠错点吗？☐ 中断能从检查点恢复吗？
- **SOURCE**: [[laws-of-ai-engineering/02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）|Law 14：误差累积定律]] · [[laws-of-ai-engineering/08_可靠性与失败定律#Law 77 — 恢复优于预防定律（Recovery-Over-Prevention Law）|Law 77：恢复优于预防定律]]

## LAW-07 · 上下文即状态（Context Is State）
- **INVARIANT**: 模型无状态，上下文是唯一"当下现实"；记忆/工具本质是管理"什么进上下文"。
- **IMPLICATION**: 状态显式存外部+重注入；上下文只放当前决策需要的最小充分信息。
- **VIOLATION**: 假设模型"记得"，长任务失忆、行为不连贯。
- **CHECK**: ☐ 任何"记忆"背后都有显式外部存储+重注入吗？
- **SOURCE**: [[laws-of-ai-engineering/01_信息与压缩定律#Law 2 — 上下文即状态定律（Context-is-State Law）|Law 2：上下文即状态定律]]

## LAW-08 · 信任应随可靠性而非能力增长（Trust-Reliability Scissors）
- **INVARIANT**: 感知能力不等于实测可靠性；信任和授权可能过高或过低，必须按目标任务证据校准。
- **IMPLICATION**: 用评测、监控和失败反馈校准信任；按任务与风险分层，不因“看起来更强”就扩大权限。
- **VIOLATION**: 过度信任导致超范围授权和事故；信任不足导致重复核验、拒用和价值损失。
- **CHECK**: ☐ 每类任务的可靠性、授权范围和核验频率匹配吗？☐ 失败后会更新信任吗？
- **SOURCE**: [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）|Law 84：信任-可靠性剪刀差定律]] · [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）|Law 95：能力-可靠性剪刀定律]]

## LAW-09 · 按后果与恢复能力分配审慎度（Risk-Adjusted Caution）
- **INVARIANT**: 可逆性影响恢复成本，但审慎度还取决于后果、爆炸半径、不确定性、时间压力和等待信息价值。
- **IMPLICATION**: 低影响且易恢复的动作走轻流程；高影响、难恢复或证据不足的动作提高验证、限权、灰度、回滚和人工控制强度。
- **VIOLATION**: 把“可回滚”误当低风险，或把“不可逆”机械变成等待和确认弹窗，导致级联事故、错失止损窗口或审批盖章化。
- **CHECK**: ☐ 最坏后果和爆炸半径多大？☐ 多久能发现并恢复？☐ 等待能获得什么信息，时间压力是什么？☐ 当前控制真的拦截过错误吗？
- **SOURCE**: [[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）|Law 74：不可逆性定律]]

## LAW-10 · 简单优先（Simplicity First）
- **INVARIANT**: 复杂度只增不减除非主动偿还；AI让加复杂度太容易。
- **IMPLICATION**: 能用一次调用不用工作流，能用工作流不用Agent，能用单Agent不用多Agent；加前先想减什么。
- **VIOLATION**: 系统膨胀到无人理解，改动风险高，被复杂度压垮。
- **CHECK**: ☐ 每个部件都为它带来的复杂度辩护了吗？☐ 复杂/自主/多Agent被收益证明了吗？
- **SOURCE**: [[laws-of-ai-engineering/04_系统与控制定律#Law 41 — 复杂度累积定律（Complexity-Accumulation Law）|Law 41：复杂度累积定律]] · [[laws-of-ai-engineering/11_演化与元定律#Law 99 — 简单性存活定律（Simplicity-Survives Law）|Law 99：简单性存活定律]]

## LAW-11 · 确定性优先（Determinism First）
- **INVARIANT**: 确定性组件可靠可测便宜可预测；模型方差是成本。
- **IMPLICATION**: 能用代码/规则可靠完成的别用模型；步骤可预知用工作流，只有依输入而变才用Agent。
- **VIOLATION**: 把可预知流程做成自主Agent，白引入方差、成本、不可控。
- **CHECK**: ☐ 不确定性被限制在确实需要它的最小范围吗？
- **SOURCE**: [[laws-of-ai-engineering/02_计算与验证定律#Law 18 — 确定性优先定律（Determinism-First Law）|Law 18：确定性优先定律]]

## LAW-12 · 关键判断显式化，问责不能止于 AI（Explicit Judgment + Traceable Accountability）
- **INVARIANT**: 生成成本下降后，目标、证据门槛和风险取舍可能成为控制点；可自动化的判断必须有明确标准与验证，剩余关键判断必须显式归属。问责不能止于 AI，必须按角色追溯到可问责的自然人或法人。
- **IMPLICATION**: 自动化标准明确、低风险且可验证的判断；把高后果、目标冲突和证据不足的判断交给有信息、有权限的角色，并明确提供、部署、授权、运营、审批和事故处置责任。
- **VIOLATION**: 无标准地把判断全部交给 AI，或把所有判断都留给人却不给证据、权限和责任边界；再用“AI 自动决定的”或“人点过确认”结束追问。
- **CHECK**: ☐ 哪些判断可自动化，依据和验证器是什么？☐ 剩余关键判断由谁负责？☐ 每个责任角色都有匹配的信息与控制权吗？
- **SOURCE**: [[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）|Law 100：判断力稀缺定律]] · [[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）|Law 86：责任不可委托定律]]

---

## LAW-13 · 信息守恒，垃圾进垃圾出（Information Conservation / GIGO）
- **INVARIANT**: 系统不能创造输入中不存在的信息；数据质量是一切下游(模型/架构/评价)不可逾越的上限。
- **IMPLICATION**: 表现差先查输入再查系统；提纯优于扩量；需要新信息时外接来源(检索/工具)，别指望加工凭空产生。
- **VIOLATION**: 用完美架构处理垃圾数据，产出精致的垃圾；上游缺失的信息下游无法补救。
- **CHECK**: ☐ 喂给系统的数据质量，配得上我对输出的期待吗？
- **SOURCE**: [[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）|Law 4：信息守恒定律]]

---

## 全局校验（任何决策都先过这三层）

```
INVARIANT LAYER (不可违反):
  安全约束 LAW-05, LAW-09  ── 不可逆/高危时压倒一切效率考量,宁可停下问人
  信息约束 LAW-02, LAW-04, LAW-13 ── 事实外置+溯源; 代理≠真实目标; 垃圾进垃圾出
  可靠约束 LAW-03, LAW-08  ── 分布变化后重评; 信任跟随实测

DEFAULT LAYER (强默认,除非有明确理由偏离):
  LAW-10 简单优先 · LAW-11 确定性优先 · LAW-01 先设计可靠验证器

META (最终锚点):
  LAW-12 判断有主,问责可追溯
```

**若你面临本决策系统未覆盖的处境**：仅凭这 13 条 + [[00_PROTOCOL|GLOBAL PRIORITY RULES]]，你已能推导出大多数正确决策。它们是倒金字塔的顶端——掌握这 13 条，就能重新推导出底下数百个方法和反模式。
