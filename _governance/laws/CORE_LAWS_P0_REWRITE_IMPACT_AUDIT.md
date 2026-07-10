---
type: law-rewrite-impact-audit
aliases: [CoreLawsP0RewriteImpactAudit, Law 12 86 改写影响审计]
abstraction_layer: 运营机制（正典改写影响审计）
date: 2026-07-10
course: laws-of-ai-engineering
status: completed-downstream-closed
scope: Law 12 / Law 86 正典收窄、全库语义影响与 Constitution / ADS 下游收束
tags: [AI工程, Laws, CoreLaws, 正典改写, 影响审计]
---

# Core Laws P0 改写影响审计｜Law 12 / Law 86

> 本文记录 [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）|Law 12]] 与 [[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）|Law 86]] 在外部依据核验后进行正文收窄时，对全库产生的语义影响、已修正文和明确延期项。
>
> 它是改写审计，不是新任务队列；后续任务仍以 [[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|编辑审计待办清单]] 为准。

## 1. 为什么必须做影响审计

两条 Law 都是跨书高频正典。若只改 Law 本文而不改依赖它的解释，会形成“链接能点开，但上下文仍在传播旧命题”的语义断链。

改写前的 heading 级引用基线：

| 正典 | 链接数 | 涉及文件数 | 主要旧风险 |
|---|---:|---:|---|
| Law 12 | 32 | 25 | 把条件性工程原则写成由 P vs NP 证明的普遍数学定理 |
| Law 86 | 26 | 21 | 把问责不能止于 AI 收窄成“永远由单一部署者或具体个人担责” |

本批保持两个 Law 的编号与 heading 不变，因此既有 heading 链接不需要迁移；需要修的是链接周围的解释。

## 2. 正典改写结果

### Law 12

新边界：只有任务存在**客观、廉价、独立于生成过程的验证器**时，核验候选输出才通常可能比从头生成便宜。开放研究、战略判断、价值取舍、证据不可得或同源 Judge 复核，不自动满足这个条件。

特别澄清：NP 中“可快速检查证书”的严格例子不能推出“一般任务的验证都比生成容易”，P vs NP 仍未解决。

### Law 86

新边界：任务和操作可以委托给 AI，但问责不能停在“AI 做的”。责任必须继续追溯到可问责的自然人或法人，并按提供、部署、运营、专业使用、授权和组织治理等角色与语境分配；它不默认只落在某一个部署者或最后点击确认的人身上。

特别澄清：多人或多组织共同承担不同义务，不等于责任真空；真正的问题是角色、权限、信息和控制能力没有明确对齐。

## 3. 已同步修正的主动正文

### 全局正典与关系层

- [[laws-of-ai-engineering/00_INDEX|Laws INDEX]]：撤销 Law 12 的“数学/物理级”例子，核心口号改为带验证器条件的版本。
- [[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]]：补 Law 12 适用条件与 Law 86 的角色分配边界。
- [[laws-of-ai-engineering/00_LAW-RELATION-GRAPH|Law Relation Graph]]：同步 Law 12→13、Law 12 vs 14、Law 74 vs 86 的关系说明。
- [[00_Knowledge-Graph-总图|知识图谱总图]]：保留“生成廉价 → 验证稀缺”作为工程趋势判断，但撤销“验证易于生成”的无条件数学口径。
- [[laws-of-ai-engineering/08_可靠性与失败定律#Law 78 — 测试即真理定律（Untested-Is-Broken Law）|Law 78]]：与 Law 12 的关系改为“有可靠、廉价验证器时”。

### Foundation 与 Evaluation

- [[foundation-of-ai-engineering/01_未来20年不变的规律|未来 20 年不变的规律]]、[[foundation-of-ai-engineering/03_必须掌握的能力|必须掌握的能力]]、[[foundation-of-ai-engineering/04_最值得记忆的设计原则|最值得记忆的设计原则]]、[[foundation-of-ai-engineering/05_最值得写进教材的知识|最值得写进教材的知识]]、[[foundation-of-ai-engineering/06_AI设计AI的原则|AI 设计 AI 的原则]]：撤销“除非 P=NP”“验证总是更容易”“责任永远在某个人”等过强转述，保留“为验证而设计”和“问责不能止于 AI”的工程价值。
- [[evaluation-of-ai-systems/00_INDEX|Evaluation INDEX]]、[[evaluation-of-ai-systems/05_人类评价|人类评价]]、[[evaluation-of-ai-systems/07_未来趋势|未来趋势]]：把评价的核心地位解释为“标准、证据和验证器稀缺”，不再把人类即时判断称为天然正确的终极 ground truth。

### 人机协作与应用层

- [[human-ai-collaboration-foundation/00_INDEX|Human-AI Collaboration INDEX]]、[[human-ai-collaboration-foundation/01_人机分工原则|人机分工原则]]、[[human-ai-collaboration-foundation/05_避免盖章者陷阱|避免盖章者陷阱]]、[[human-ai-collaboration-foundation/07_责任边界设计|责任边界设计]]、[[human-ai-collaboration-foundation/09_长期协作关系|长期协作关系]]：责任矩阵从“一个具体担责人”升级为自然人/法人角色链，强调责任与权限、信息、控制能力按角色对齐。
- [[ai-systems-in-production/01_从Demo到生产|从 Demo 到生产]]：把监控问题改写为主动创造独立失败信号。
- [[data-foundation-of-ai-systems/03_标注与合成|标注与合成]]、[[data-foundation-of-ai-systems/05_数据治理与伦理|数据治理与伦理]]：区分真实数据的经验锚点、人和制度定义的价值标准、以及角色化的数据责任。
- [[multimodal-systems/00_INDEX|Multimodal Systems INDEX]]、[[multimodal-systems/01_多模态系统的第一性|多模态系统的第一性]]、[[multimodal-systems/04_多模态评价与证据|多模态评价与证据]]：从“Law 12 被侵蚀”改为“廉价独立验证器条件更难满足”。
- [[llm-design-patterns/01_推理模式|推理模式]]：说明可检查输出只有接上可靠验证器，才产生 Law 12 的成本杠杆。
- [[ai-engineering-case-library/05_评价与质量|评价与质量案例]]、[[ai-engineering-case-library/10_人机与产品决策|人机与产品决策案例]]：撤销“人类天然是终极 ground truth”和“责任一律在人”的教学短句。

## 4. 经审计后保留的引用

下面几类引用与新正典兼容，无需为了统一文风机械改写：

- [[human-ai-interaction-design/02_不确定性与边界的呈现|不确定性与边界的呈现]] 已明确用来源链接降低核验成本，满足 Law 12 的条件。
- [[ai-engineering-anti-patterns/01_Agent架构反模式|Agent 架构反模式]]、[[ai-engineering-anti-patterns/06_工作流反模式|工作流反模式]]、[[ai-engineering-anti-patterns/08_最应避免的20个错误|最应避免的 20 个错误]] 只使用“问责不能交给 AI”的方向性含义，没有指定唯一责任人。
- [[human-ai-interaction-design/05_协作制度的界面实现|协作制度的界面实现]] 与 [[multimodal-systems/06_多模态安全与反模式|多模态安全与反模式]] 分别要求责任角色可辨和问责链可取证，与 Law 86 新边界一致。
- [[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] 中的 Law 12/86 仅作为链接格式与模块选用示例，不承担旧定义。

## 5. 高风险下游正典收束（Batch B1.2）

以下位置在 B1.1 中被明确延期；2026-07-10 获得独立授权后，已按同一批次原子迁移，Laws 正典与运行时压缩不再分叉：

1. [[The-Constitution-of-AI-Engineering#Law 1 · 有可靠验证器时，验证可低于生成（Conditional Verification Leverage）|Constitution · Law 1]]：保留 Constitution 内部 `Law 1` 编号，heading 与四问改为带验证器条件的压缩表达。
2. [[agent-decision-system/04_LAW-INVARIANTS#LAW-01 · 先设计可靠验证器（Design for Verifiability）|ADS LAW-01]]：保留 `LAW-01` ID，重命名并把 invariant 改成“先确认客观、廉价、独立验证器”；同步 Source Map、Situation Router、Pattern Cards、Case heading 链接和机器 YAML。
3. [[agent-decision-system/04_LAW-INVARIANTS#LAW-12 · 判断力稀缺，问责不能止于 AI（Judgment Scarce + Traceable Accountability）|ADS LAW-12]]：保留 `LAW-12` ID，把单一部署者责任改成按自然人/法人角色追溯；同步人读与机器依赖。
4. `_governance/` 中的旧审计表保留当时的扫描词和历史判断，只加状态回链，不洗改历史数据。

> [!note] 范围边界
> B1.2 只收束 ADS `LAW-12` 的“问责”半边；“判断力稀缺”来自 Law 100，仍属于 [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT#3. P0 与 P1-A 已完成、其余 P1/P2 仍待后续裁决的 10 条|Core Laws 审计的 P1]]，本批没有提前裁决。

B1.2 的停手目标是：**除明确标识为历史快照的治理文件外，Constitution、ADS 正典、机器产物和 Case heading 依赖中的旧强表述全部清零。**

## 6. 验收状态

- [x] Law 12 / Law 86 的编号和 heading 未改变，且各自在全库只出现一个正典定义。
- [x] 主动正文中“P vs NP 证明普遍验证更容易”的旧命题为 0。
- [x] 主动正文中“责任永远只在部署者/某一个具体的人”的旧命题为 0。
- [x] B1.1 验收时，Constitution 与 ADS 的延期项已被扫描命令明确排除并记录，没有假装清零。
- [x] 全库 heading / wikilink 体检通过。
- [x] `git diff --check` 通过。

改写后的 heading 级链接实测：

| 正典 | 链接数 | 涉及文件数 | 说明 |
|---|---:|---:|---|
| Law 12 | 34 | 27 | 新增一个主动正文直达链接和本影响审计链接；原 heading 未迁移 |
| Law 86 | 27 | 22 | 新增本影响审计链接；原 heading 未迁移 |

验证记录（2026-07-10）：

- 定向语义断言：`canonical_headings=2/2 exact_once`，`active_old_strong_claims=0`。
- `python3 _tools/kb_health_check.py`：通过；181 个 Markdown，断链 0、heading 异常 0、ADS machine 同步正常。
- `git diff --check`：exit 0。

## 7. Batch B1.2 验收状态

- [x] Constitution `Law 1` 编号保留，旧 heading 与无条件命题清零。
- [x] ADS `LAW-01` / `LAW-12` ID 保留，新 heading 在所有 Case 链接中精确匹配。
- [x] `00_PROTOCOL`、Situation Router、Pattern Cards、Eval Checklist 与 machine YAML 同步。
- [x] `compile_decision_system.py --check`、`check_ads_case_crossrefs.py`、`kb_health_check.py` 全部通过。

验证记录（2026-07-10）：

- `python3 _tools/compile_decision_system.py --check`：总条目 76；严格校验与机器同步均为 OK。
- `python3 _tools/check_ads_case_crossrefs.py`：Case→ADS heading 级链接 382 处，heading 错误 0；21/21 情境可直达案例。
- `python3 _tools/kb_health_check.py`：181 个 Markdown，断链 0、heading 异常 0，体检通过。
- 主动正文旧 heading / 旧强表述扫描：0。
