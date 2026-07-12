---
type: law-rewrite-impact-audit
aliases: [CoreLawsP1RewriteImpactAudit, Core Laws P1 改写影响审计]
abstraction_layer: 运营机制（正典改写影响审计）
date: 2026-07-10
course: laws-of-ai-engineering
status: p1-completed
scope: Law 7 / Law 84 / Law 95 / Law 100 正典收窄与下游影响
tags: [AI工程, Laws, CoreLaws, P1, 正典改写, 影响审计]
---

# Core Laws P1 改写影响审计

> 本文承接 [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core Laws 外部核验]]，记录 P1 四条正典的分批改写与全库影响。它不是新任务队列；执行状态仍回写 [[01_编辑审计#待办清单（后续批次的唯一有效位置，做完即勾）|编辑审计待办清单]]。

## 执行纪律

P1 不做四条一次性机械替换，而按语义耦合拆成三批：

1. P1-A：Law 7，单独处理分布与可靠性证据边界；
2. P1-B：Law 84 + Law 95，成组区分人类信任失配与模型能力/可靠性失配；
3. P1-C：Law 100，单独审查全库“判断力稀缺”根命题。

每批都要同步 Constitution、ADS、Case heading 和机器 YAML；不能只改 Laws 正文。

## P1-A｜Law 7（已完成）

### 正典裁决

[[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）|Law 7]] 保留编号，heading 从“分布内可靠定律”改为“分布证据边界定律”。

新命题不是“分布内可靠、分布外不可靠”，而是：

- 可靠性证据只对与评测条件充分匹配的目标分布成立，不能自动跨分布外推；
- “分布内”不是可靠性的充分条件，同分布仍可能有覆盖不足、噪声、长尾子群和校准问题；
- 任务、用户、数据、时间或工具链变化时，必须重新评测证据能否迁移。

### 下游收束

- [[The-Constitution-of-AI-Engineering#Law 3 · 可靠性证据有分布边界（Distribution-Bounded Evidence）|Constitution · Law 3]] 保留内部编号并改写四问。
- [[agent-decision-system/04_LAW-INVARIANTS#LAW-03 · 分布证据有边界 + 校准（Distribution-Bounded Evidence + Calibration）|ADS LAW-03]] 保留 ID，重写 invariant/check，并同步 Source Map、Situation Router 和 `_machine`。
- 8 个 Case Library `LAW-03` heading 目标已迁移；数据、评价、Foundation、多模态、教材、总图与学习路径中的高确信度旧转述已同步。
- 与 Law 95 重叠的“能力前沿必然是可靠性洼地”只移除对 Law 7 的错误因果归因；Law 95 的增长速率主张留到 P1-B 正式裁决。

### 验收结果

- 旧 Law 7 / Constitution Law 3 / ADS LAW-03 heading：0。
- 主动正文“分布内才可靠 / 分布内近乎可靠”：0。
- ADS `LAW-03` ID 保留，Case heading 迁移 8 处。
- ADS 编译、ADS↔Case cross-reference、全库体检、`git diff --check`：全部通过。

## P1-B｜Law 84 + Law 95（已完成）

### 正典裁决

[[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）|Law 84]] 与 [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）|Law 95]] 均保留编号与 heading，避免破坏已稳定的引用坐标；“剪刀”只表示可能出现、需要测量的失配，不再表示必然的增长速率。

- Law 84 收窄为**人机关系侧的校准风险**：能力展示、流畅度或权威感可能让信任和授权超过目标任务上的实测可靠性；也可能出现信任不足。方向不是宿命，失配才是风险。
- Law 95 收窄为**模型评价侧的维度分离**：能力提升不证明可靠性按比例提升，新增能力与使用边界必须重新评测；同时不预设可靠性一定滞后。
- 两条可成组引用，但不能互相替代：Law 84 约束人的信任与授权，Law 95 约束模型能力与可靠性的证据关系。

### 下游收束

- [[The-Constitution-of-AI-Engineering#Law 8 · 信任应随可靠性而非能力增长（Trust-Reliability Scissors）|Constitution · Law 8]] 保留编号与 heading，改为以目标分布评测、运行监控和失败反馈校准信任，同时覆盖过度信任与信任不足。
- [[agent-decision-system/04_LAW-INVARIANTS#LAW-08 · 信任应随可靠性而非能力增长（Trust-Reliability Scissors）|ADS LAW-08]] 保留 ID，重写 invariant / violation / check；Source Map 明确剪刀差不是必然增长速率。
- Core Laws 表、Laws INDEX、关系图、知识总图、Foundation、Evaluation、Human-AI 两书、Anti-patterns 与案例库中的主动转述已同步；heading 未变化，因此不需要 Case heading 迁移。

### 验收目标

- Law 84 / Law 95 / ADS LAW-08 heading 均保留且唯一。
- 主动正文不再声称“信任必然比可靠性增长更快”或“能力增长必然快于可靠性”。
- ADS 编译、ADS↔Case cross-reference、全库体检、`git diff --check` 全部通过。

## P1-C｜Law 100（已完成）

### 正典裁决

[[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）|Law 100]] 保留编号与 heading，定律性质从“经济认识论规律”改为“经济认识论综合命题”。

新命题不是“知识不再稀缺、判断永远由人承担”，而是：

- 当 AI 显著降低某类知识获取与候选生成成本时，目标选择、证据判断、风险取舍和责任归属**可能**上升为瓶颈；
- 判断力稀缺是需要按任务验证的相对稀缺；数据、领域知识、算力、协调、执行或合法性也可能是实际瓶颈；
- 标准明确、低风险且有可靠验证器的判断可以自动化；高后果、目标冲突和证据不足的判断必须有信息、有权限、可问责的角色。

### 下游收束

- Constitution `Law 10` 保留编号，heading 改为“生成变便宜时，关键判断可能成为瓶颈”；尾声从“把判断留给人”改为“让关键判断有标准、有归属”。
- ADS 保留 `LAW-12` ID，heading 改为“关键判断显式化，问责不能止于 AI”；4 个 Case heading 依赖已迁移，Source Map、Situation Router、Eval Checklist 与机器 YAML 同步。
- Foundation 的元命题三与第七章核心段落改为持续寻找真实瓶颈；Laws INDEX / Core 表、学习路径、评价、决策框架、数据治理、人机协作、教材与模型定制中的高确信度旧转述已同步。
- Law 100 的 heading 未变化，因此 Law 100 直接引用无需迁移；本批没有把“判断力”一词机械清零，保留领域判断、工程判断力与具体高后果场景中的正常用法。

### 验收目标

- Law 100 正典 heading 保留且唯一；旧的“唯一持续稀缺”“不适用范围为无”“所有判断只能留给人”等主动断言为 0。
- Constitution Law 10 / ADS LAW-12 旧 heading 为 0；ADS `LAW-12` ID 保留，4 个 Case heading 依赖迁移。
- ADS 编译、ADS↔Case cross-reference、全库体检、`git diff --check` 全部通过。

## P1 总结

P1-A/B/C 的共同收束不是降低工程价值，而是把三个强口号改成可审计命题：分布证据不能无条件外推；能力、可靠性与信任必须分开测；判断是否成为瓶颈也必须按任务验证。P1 到此结束，P2 另批处理。
