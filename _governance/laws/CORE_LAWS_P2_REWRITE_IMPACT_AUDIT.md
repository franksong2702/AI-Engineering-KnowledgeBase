---
type: law-rewrite-impact-audit
aliases: [CoreLawsP2RewriteImpactAudit, Core Laws P2 改写影响审计]
abstraction_layer: 运营机制（正典改写影响审计）
date: 2026-07-10
course: laws-of-ai-engineering
status: p2ab-completed-p2c-pending
scope: Law 64 / Law 1 / Law 62 / Law 74 正典收窄与下游影响
tags: [AI工程, Laws, CoreLaws, P2, 正典改写, 影响审计]
---

# Core Laws P2 改写影响审计

> 本文承接 [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core Laws 外部核验]]。执行状态仍回写 [[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|编辑审计待办清单]]。

## 执行顺序

1. P2-A：Law 64，可证伪性作为经验性工程主张的审计纪律；
2. P2-B：Law 1 + Law 62，成组拆开压缩视角、事实保证和流畅度偏差；
3. P2-C：Law 74，最后处理可逆性、影响与审慎度的高影响依赖。

## P2-A｜Law 64（已完成）

### 正典裁决

[[laws-of-ai-engineering/07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）|Law 64]] 保留编号与 heading，性质从“科学哲学规律”改为“科学哲学审计原则”。

新命题是：

- 对描述现实、指导行动的经验性工程主张，应说明哪些可观察结果会削弱或推翻它；
- 可证伪性是 Popper 提出的科学划界标准，也是有用的工程审计纪律，但不是所有知识唯一公认的定义；
- 数学与逻辑命题、定义、伦理规范、设计价值和探索性框架需要不同的评价方式。

### 下游收束

- Laws INDEX 与 Core 表不再说“不能验证就不配叫定律”，改为经验性 Law 必须声明失败条件。
- Evaluation、Decision Frameworks、Foundation 与 Law 102 的主动转述改为“经验性主张可被证据推翻”。
- ADS Source Map 继续把 Law 64 作为 LAW-01 的辅助来源；其运行时定义已经是可靠验证器条件，不需要改 ID 或机器 YAML。

### 验收目标

- Law 64 heading 保留且唯一；无需迁移 heading 链接。
- 主动正文“可证伪性是所有知识的定义特征”“所有不可证伪表述都不是知识”为 0。
- 全库体检和 `git diff --check` 通过。

## P2-B｜Law 1 + Law 62（已完成）

### 正典裁决

[[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）|Law 1]] 与 [[laws-of-ai-engineering/07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）|Law 62]] 均保留编号与 heading，避免无价值的全库锚点迁移，但降低绝对性：

- Law 1 从“信息论硬规律 / 幻觉单一因果解释”改为“语言建模与压缩视角下的工程转译原则”；核心约束是参数生成没有内建的事实来源保证；
- Law 6 继续单独负责摘要、记忆、上下文、抽帧和转录等实际压缩操作的任务相关损失；
- Law 62 改为“流畅、自信、专业不是正确性的充分证据，并可能诱发评价偏差”；不再主张流畅度与正确性在所有分布中无关或负相关。

### 下游收束

- Constitution `Law 2` 保留编号，改为“参数生成没有事实来源保证”。
- ADS 保留 `LAW-02` ID，heading 改为“参数生成无事实来源保证”；Source Map、Situation Router、8 个 Case heading 依赖与机器 YAML 同步迁移。
- Multimodal 两处把运行时抽帧、转录、缩放从 Law 1 改指 Law 6；“指令是意图的压缩”同样改指 Law 6。
- Laws INDEX / Core 表 / 元信息 schema、总图、Foundation、教材、Evaluation 与 HITL 主动转述同步；集中 citation 保持为研究型入口。

### 验收目标

- Law 1 / Law 62 heading 各保留且唯一；Constitution Law 2 与 ADS LAW-02 新 heading 各唯一。
- 8 个案例链接全部直达新 ADS LAW-02 heading，旧 heading 链接为 0。
- 主动正文“模型是有损压缩，所以会幻觉”“幻觉是原理而非 bug”“流畅度与正确性无关 / 甚至负相关”为 0。
- ADS 编译、Case cross-reference、全库体检和 `git diff --check` 通过。

## P2-C｜Law 74（待执行）

目标：把可逆性放回多因素决策分诊，不再让它单独决定所有审批、速度与自主性边界。
