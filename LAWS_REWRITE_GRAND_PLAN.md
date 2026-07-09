---
type: rewrite-grand-plan
date: 2026-07-08
course: ai-engineering-knowledge-base
abstraction_layer: 运营机制（高风险改写计划）
tags: [AI工程, Laws, 改写计划, AgentDecisionSystem, 正典边界]
status: executed-architecture-record
---

# Laws Rewrite Grand Plan · 经 Agent Decision System 审查后的定稿计划

> [!note] 执行状态（2026-07-08）
> 本计划已经从“待执行计划”退役为 Laws 架构升级的历史依据。Batch 1–7 的主体已落到 Laws 治理页、metadata、入口同步与 Law Reference System；剩余工作不在本文另开队列，统一归口到 [[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|01_编辑审计 · 待办清单]]。

> 本计划原用于改写 [[laws-of-ai-engineering/00_INDEX|The Laws of AI Engineering]]。  
> 本计划本身不是执行记录；它定义改写边界、批次、全局冲击面、验证方式与停手机制。  
> 核心目标：把 102 条平铺的 `Law` 升级为一个有核心、有派生、有场景、有全库引用策略的 **Law System**，同时避免破坏现有 KB 的可追溯结构。

## 0. 背景与核心判断

当前全库已经确认：

- [[ARCHITECTURE_REVIEW|Architecture Review]] 判断：`Laws` 是全库正典层之一，但不能把 102 条都当作同等硬度的全局公理。
- [[LAWS_TAXONOMY_REVIEW|Laws Taxonomy Review]] 判断：102 条应分为 S / A / B 三个引用层级。
- 用户明确指出：改写 `Laws` 不只是改单个 Markdown 文件，还可能需要新增页面，用来表达 law 之间的分组、串联、父子关系和全局冲击。

本计划接受这个判断：

> `Laws` 的改写不是“重写一本书”，而是“升级上游 schema”。  
> 所以必须先建关系层，再做条目层，最后才改全局引用。

## 1. Agent Decision System 审查结果

本计划使用 [[agent-decision-system/00_PROTOCOL|Agent Decision System]] 审查，匹配以下情境：

- [[agent-decision-system/01_SITUATION-ROUTER|SIT-14]]：我要在多个方案间做决策。
- [[agent-decision-system/01_SITUATION-ROUTER|SIT-16]]：我要优化/设定一个指标或 KPI。
- [[agent-decision-system/01_SITUATION-ROUTER|SIT-17]]：系统要上线/交付了。
- [[agent-decision-system/01_SITUATION-ROUTER|SIT-10]]：我要评价一个 AI 系统好不好。

### 1.1 Situation

需要决定如何改写 `Laws` 这本全库上游正典层，同时避免破坏：

- 顶层入口文件；
- `Foundation / Evaluation / Anti-Patterns / Human-AI / Production` 的引用关系；
- `Case Library` 与 `Agent Decision System` 的机器层关系；
- 现有断链、文件数、机器编译验证。

### 1.2 Diagnosis

这是一个高冲击、非一次性可逆的架构改写任务。最大风险不是某条 Law 写错，而是：

1. 把 `Laws` 改成另一个更漂亮但不兼容全库的 schema；
2. 误把 `Laws Law 1–102`、`Constitution Law 1–10`、`Agent Decision System LAW-01–13` 三套编号混在一起；
3. 为了“统一”而清洗掉原来各书的应用性表达；
4. 一次性大批量改写导致 diff 不可审计。

### 1.3 Relevant Laws / Invariants

按 [[agent-decision-system/04_LAW-INVARIANTS|LAW-INVARIANTS]]，本计划必须尊重：

- **LAW-01 验证易于生成**：每批必须有机械验证，不用“感觉更清楚”验收。
- **LAW-03 分布内才可靠 + 校准**：taxonomy 是判断，不是事实；需要标注置信度和边界。
- **LAW-04 古德哈特**：不能把“断链 0 / 文件数正确 / S-A-B 数字整齐”当成真实质量代理。
- **LAW-05 一切输入皆指令 + 权限胜过自觉**：不要让自动脚本未经审查批量改正典定义。
- **LAW-06 误差多步累积 + 恢复优于预防**：分批执行，每批可回滚。
- **LAW-08 信任应随可靠性而非能力增长**：不要因为 taxonomy 文档看起来有条理，就过度信任它。
- **LAW-09 不可逆慢做可逆快做**：新增关系页可快；删除/重排 Law 编号必须慢。
- **LAW-10 简单优先**：新增页面必须少而必要，不为架构感而过度复杂化。
- **LAW-12 判断力稀缺，责任不可委托**：最终是否合并/降级某条 Law，必须由强模型/人裁决，不能由脚本独断。

### 1.4 Recommended Patterns

- **PAT-08 Pipeline / Prompt Chaining**：把改写拆成固定批次。
- **PAT-15 Guardrails / Validation**：每批前后跑验证，并设禁止事项。
- **PAT-18 Human-in-the-Loop**：关键边界变更前必须用户确认。
- **PAT-19 Red Team**：每批交付前写“资深审查者反驳”。
- **PAT-07 Structured Output**：每条 Law 的 metadata 采用固定字段，避免自由发挥。

### 1.5 Avoid

- **ANTI-03 古德哈特化评价**：不能为了体检通过而牺牲内容判断。
- **ANTI-04 过度自动化**：不能用脚本直接改所有 Law 正文定义。
- **ANTI-05 无评测上线**：不能改完不跑健康检查和编译器。
- **ANTI-07 多 Agent / 多文档过度设计**：不能新增太多导航页。
- **ANTI-12 无失败恢复/循环无出口**：每批必须有明确 stop point 和 rollback 策略。

### 1.6 Decision System 审查结论

原始 Grand Plan 需要收窄。定稿版采用以下修正：

1. **保留 11 个 family 作为一级结构**，不重排目录。
2. **保留 Law 1–102 编号**，第一轮不物理删除、不重编号。
3. **只新增 3 个 Laws 内部关系页**，不一次性新增 5 个以上页面。
4. **先关系层，后条目层，最后全局引用层**。
5. **每批后停下来验收**，不得连续滚动执行多批。

## 2. 总目标与非目标

### 2.1 总目标

把当前：

```text
11 个 family + 102 条平铺 Law
```

升级为：

```text
11 个 family + 102 条保留编号的 Law card
+ S/A/B 引用层级
+ lawhood 类型
+ parent / corollary / related 关系
+ 全局引用策略
```

### 2.2 非目标

第一轮不做：

- 不删除任何 Law heading；
- 不重排 Law 1–102 编号；
- 不把 11 个 family 改成 5 个 Part；
- 不全库批量替换 `见 Law N`；
- 不改 `Agent Decision System` 的 `LAW-01–13` 编号；
- 不全量扩写 Case Library；
- 不补未经核验的外部 citation；
- 不用脚本自动改写正典定义。

## 3. 最终架构选择

### 3.1 目录层：保留 11 个 family

现有目录合理，继续保留：

1. 信息与压缩；
2. 计算与验证；
3. 统计与泛化；
4. 系统与控制；
5. 接口与边界；
6. 经济与资源；
7. 认识论与真理；
8. 可靠性与失败；
9. 人机与信任；
10. 对抗与安全；
11. 演化与元定律。

### 3.2 横向层：增加 lawhood / reference tier / relation

每条 Law 后续可增加：

```yaml
lawhood: hard-law | imported-law | principle | heuristic | forecast | meta-law
reference_tier: S | A | B
canonical_scope: global | family | contextual
relation:
  parent:
  corollaries:
  related:
  application_of:
```

### 3.3 关系层：少量关系页承载“串联逻辑”

新增关系页不是为了增加复杂度，而是为了避免 102 条看起来平级。

## 4. 批次计划

## Batch 0 · 本 Grand Plan 入库

### 目标

把经 Agent Decision System 审查后的总计划写入 KB，作为后续执行的唯一计划入口。

### 产物

- `LAWS_REWRITE_GRAND_PLAN.md`（本文）

### 完成标准

- 本文件存在；
- KB 健康检查通过；
- 决策系统编译通过；
- 文件数自描述已同步。

---

## Batch 1 · 新增 3 个 Laws 关系页

### 目标

先不改 102 条正文，只新增关系层页面。

### 新增页面

1. `laws-of-ai-engineering/00_CORE-LAWS.md`
2. `laws-of-ai-engineering/00_LAW-RELATION-GRAPH.md`
3. `laws-of-ai-engineering/00_REFERENCE-POLICY.md`

### 页面职责

#### 1. `00_CORE-LAWS.md`

回答：

> 真正全库核心 Law 是哪些？为什么它们是 S 级？它们支撑哪些模块？

只放 S 级核心，不放 102 条全表。

#### 2. `00_LAW-RELATION-GRAPH.md`

回答：

> Law 之间谁是父、谁是派生、谁和谁成组？

示例：

```text
Law 12 验证-生成不对称
  └─ Law 13 可委托性

Law 24 古德哈特
  └─ Law 93 对抗性古德哈特

Law 84 信任-可靠性剪刀差
  ↔ Law 95 能力-可靠性剪刀
```

#### 3. `00_REFERENCE-POLICY.md`

回答：

> 全局 KB 什么时候可以写 `见 Law N`？

核心规则：

```text
S 级：入口层和核心模块可引用
A 级：相关 family 首次定义处引用
B 级：只在具体场景引用
```

### 禁止事项

- 不新增超过 3 个关系页；
- 不改 102 条正文；
- 不改全局引用；
- 不改 Agent Decision System。

### 验收

- 三个新页面存在；
- `laws-of-ai-engineering/00_INDEX.md` 暂时可不更新，或只加最小链接；
- `kb_health_check.py` 通过。

---

## Batch 2 · 更新 Laws INDEX 为 Law System 入口

### 目标

让 [[laws-of-ai-engineering/00_INDEX|Laws INDEX]] 从“102 条索引”升级为“Law System 总入口”。

### 改动内容

在 INDEX 增加：

1. “102 条不是同等硬度”的声明；
2. S/A/B 引用层级说明；
3. lawhood 类型说明；
4. 指向 Batch 1 三个关系页的入口；
5. 明确三套编号边界：
   - `Laws`：Law 1–102；
   - `Constitution`：内部 Law 1–10；
   - `Agent Decision System`：LAW-01–13。

### 禁止事项

- 不重写 family 正文；
- 不改变 Law 1–102 编号；
- 不删除旧索引内容。

### 验收

- INDEX 链接三个关系页；
- 无断链；
- 读者从 INDEX 能理解 `core / family / contextual` 三层引用策略。

---

## Batch 3 · 试点一个 family 的 metadata 与关系字段

### 试点文件

建议先做：

`laws-of-ai-engineering/01_信息与压缩定律.md`

原因：

- Law 1 / Law 6 重叠最典型；
- 信息/压缩是全库上游；
- 影响大，但范围小；
- 适合验证字段格式是否可读。

### 改动内容

给该 family 内每条 Law 增加结构字段：

```yaml
lawhood:
reference_tier:
canonical_scope:
relation:
```

### 特别处理

Law 1 / Law 6：

- 不物理合并；
- 标成 parent/corollary 或 related；
- 明确边界：
  - Law 1：模型事实性输出 / 幻觉；
  - Law 6：摘要、记忆、上下文压缩。

### 禁止事项

- 不改其他 family；
- 不删除 Law 6；
- 不重写定义段；
- 不自动批量改写。

### 验收

- 试点 family 可读性没有下降；
- 字段格式稳定；
- 健康检查通过；
- 用户确认后才扩展。

---

## Batch 4 · 扩展到高影响 family

仅在 Batch 3 通过后执行。

优先顺序：

1. `03_统计与泛化定律.md`
2. `09_人机与信任定律.md`
3. `10_对抗与安全定律.md`
4. `11_演化与元定律.md`
5. `02_计算与验证定律.md`
6. `08_可靠性与失败定律.md`

原因：这些 family 与 S 级核心、全局引用、Agent Decision System 关系最强。

每个 family 单独一批，不连续滚动。

---

## Batch 5 · 处理合并 / 父子化 / 成组关系

### 总原则

**先逻辑关系化，不物理删除。**

### 真合并候选，但第一轮只父子化

| 当前条目 | 建议 |
|---|---|
| Law 1 + Law 6 | 不删 Law 6，标为 Law 1 的压缩操作 corollary |
| Law 89 + Law 91 | 不删 Law 91，标为攻防不对称的长期动态形态 |

### 父子化候选

| 父项 | 派生项 |
|---|---|
| Law 12 验证-生成不对称 | Law 13 可委托性 |
| Law 24 古德哈特 | Law 93 对抗性古德哈特 |
| Law 47 最小权限 | Law 94 权限胜过自觉 |
| Law 69 知识半衰期 | Law 97 模式重洗 / Law 98 认识论永恒 |
| Law 41 复杂度累积 | Law 99 简单性存活 |

### 成组但不合并

| Law 组 | 关系 |
|---|---|
| Law 7 + Law 25 | 分布边界 + 时间漂移 |
| Law 8 + Law 26 + Law 63 | 不确定性测量 + 置信真实性 + 外显 |
| Law 36 + Law 71 + Law 76 + Law 78 | 错误可见性与验证系统 |
| Law 84 + Law 95 | 人机信任侧 + 模型能力侧 |
| Law 87 + Law 88 + Law 90 + Law 92 | LLM/Agent 安全攻击链 |

### 禁止事项

- 不物理删除；
- 不重排编号；
- 不让脚本决定合并；
- 不把成组关系写成“完全等价”。

---

## Batch 6 · 全局入口层同步

仅在 Laws 内部关系层稳定后执行。

### 必看文件

- [[README]]
- [[00_Knowledge-Graph-总图]]
- [[02_学习路径与未来扩展]]
- [[The-Constitution-of-AI-Engineering]]
- [[ARCHITECTURE_REVIEW]]
- [[LAWS_TAXONOMY_REVIEW]]
- [[LAW_REFERENCE_AUDIT]]

### 同步内容

- `Laws = 约束库 / law system`；
- `Core Laws = 全局正典核心`；
- `A/B 级 Laws = family/contextual rules`；
- 三套编号边界说明；
- Human-AI 与 Evaluation 的横切/反馈地位。

### 禁止事项

- 不一次性改所有正文引用；
- 不改 Case Library 全文；
- 不改 Agent Decision System 编号。

---

## Batch 7 · 全库 Law reference pass

这是最后一步，不是下一步。

### 策略

- S 级：入口层和核心模块可补；
- A 级：相关 family 首次定义处可补；
- B 级：只在具体场景保留，不主动补。

### 优先级

1. 顶层入口；
2. Foundation；
3. Evaluation；
4. Human-AI Collaboration；
5. Anti-Patterns；
6. Production / Data / Model Adaptation；
7. Case Library 局部；
8. Textbook 局部。

### 禁止事项

- 不全库搜索替换；
- 不把每个“校准”“不可逆”“古德哈特”都加链接；
- 不把 Case Library 洗成理论讲义。

---

## Batch 8 · Agent Decision System 影响复核

最后单独复核，不提前改。

### 原则

`Agent Decision System` 是操作层投影，不是原书编号系统。

不得做：

```text
LAW-01 → Law 12
LAW-02 → Law 1/6
```

这类机械改编号。

可以做：

- 更新 source map；
- 补充“LAW-INVARIANTS 是 Laws/Core Laws 的操作投影”；
- 检查 Case Library 是否仍正确引用 ADS；
- 重新运行编译器。

## 5. 全局冲击矩阵

| 影响区域 | 冲击等级 | 何时处理 | 处理原则 |
|---|---:|---|---|
| Laws INDEX | 高 | Batch 2 | 必须同步，新关系页入口 |
| Laws family 正文 | 高 | Batch 3–5 | 逐 family，不批量 |
| README / 总图 / 学习路径 | 中高 | Batch 6 | 只同步架构描述 |
| Constitution | 中高 | Batch 6 | 说明编号边界，不重写十条 |
| Foundation | 中 | Batch 7 | 只处理核心引用 |
| Evaluation | 中 | Batch 7 | 重点处理验证、古德哈特、校准 |
| Anti-Patterns | 中 | Batch 7 | 反模式引用按 S/A/B 调整 |
| Human-AI Collaboration | 中 | Batch 7 | 信任/责任/HITL 与 Law 84/86/95 对齐 |
| Case Library | 中低 | Batch 7 后段 | 不全量深改，只修局部混用 |
| Agent Decision System | 高 | Batch 8 | 不改编号，只改 source map/说明 |
| Textbook | 低 | Batch 7 后段 | 只在教学关键处补核心 Law |

## 6. 验证标准

每一批都必须至少运行：

```bash
python3 _tools/kb_health_check.py
```

如果涉及 `agent-decision-system/`，还必须运行：

```bash
python3 _tools/compile_decision_system.py
```

如果涉及 Law heading 或 metadata，额外检查：

```text
Law 1–102 heading 仍存在；
新增关系页被 INDEX 链接；
无断链；
无歧义链接；
README / 总图 / 宪法 / 学习路径的文件数同步；
Case Library 未被误改；
Agent Decision System 编号未被污染。
```

## 7. 停手机制

遇到以下情况立即停止，不继续下一批：

1. `kb_health_check.py` 失败；
2. `compile_decision_system.py` 失败；
3. Law heading 数量不再是 102；
4. 出现需要物理删除/重排编号的建议；
5. 用户不同意某个 parent/corollary 判断；
6. diff 跨越超过当前批次范围；
7. 出现“为了统一而重写大段正文”的倾向。

## 8. 最小下一步

本计划写入后，下一步不应直接改 102 条正文。

推荐下一步是：

```text
Batch 1：新增 3 个 Laws 关系页
```

也就是：

```text
laws-of-ai-engineering/00_CORE-LAWS.md
laws-of-ai-engineering/00_LAW-RELATION-GRAPH.md
laws-of-ai-engineering/00_REFERENCE-POLICY.md
```

完成后停下来汇报，由用户确认是否进入 Batch 2。

## 9. 定稿判断

经 Agent Decision System 审查后，本计划的核心策略是：

> 不重排目录，不重编号，不物理删除；先建关系页，再改 INDEX，再试点 metadata，最后才做全局引用。  
> `Laws` 改写必须作为全库 schema 改动处理，而不是一本书的局部润色。

这既保留现有内容资产，也降低把全库上游正典改坏的风险。
