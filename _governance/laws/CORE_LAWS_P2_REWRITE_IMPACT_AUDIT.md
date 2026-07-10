---
type: law-rewrite-impact-audit
aliases: [CoreLawsP2RewriteImpactAudit, Core Laws P2 改写影响审计]
abstraction_layer: 运营机制（正典改写影响审计）
date: 2026-07-10
course: laws-of-ai-engineering
status: p2a-completed-p2bc-pending
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

## P2-B｜Law 1 + Law 62（待执行）

目标：区分参数生成的事实无来源保证、压缩视角和具体幻觉机制；把流畅度收窄为“不是正确性的充分证据，并可能诱发评价偏差”。

## P2-C｜Law 74（待执行）

目标：把可逆性放回多因素决策分诊，不再让它单独决定所有审批、速度与自主性边界。
