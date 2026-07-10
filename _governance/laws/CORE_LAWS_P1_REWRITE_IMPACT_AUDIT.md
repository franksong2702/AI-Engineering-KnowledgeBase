---
type: law-rewrite-impact-audit
aliases: [CoreLawsP1RewriteImpactAudit, Core Laws P1 改写影响审计]
abstraction_layer: 运营机制（正典改写影响审计）
date: 2026-07-10
course: laws-of-ai-engineering
status: p1a-completed-p1bc-pending
scope: Law 7 / Law 84 / Law 95 / Law 100 正典收窄与下游影响
tags: [AI工程, Laws, CoreLaws, P1, 正典改写, 影响审计]
---

# Core Laws P1 改写影响审计

> 本文承接 [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core Laws 外部核验]]，记录 P1 四条正典的分批改写与全库影响。它不是新任务队列；执行状态仍回写 [[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|编辑审计待办清单]]。

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

## P1-B｜Law 84 + Law 95（待执行）

目标：撤销“信任必然比可靠性增长更快”和“能力增长必然快于可靠性”的增长速率断言，保留两类可观察的校准失配风险，并明确人机侧与模型侧分工。

## P1-C｜Law 100（待执行）

目标：把“判断力是唯一持续稀缺资源”改为可证伪的综合判断；保留目标选择、证据判断和风险取舍可能成为瓶颈的工程价值，不声称所有判断都无法自动化。

