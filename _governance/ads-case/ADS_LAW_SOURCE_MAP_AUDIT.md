---
type: ads-law-source-map-audit
date: 2026-07-08
course: ai-engineering-knowledge-base
abstraction_layer: 操作层（源流追溯审计）
status: implemented-in-protocol-source-map
tags: [AI工程, AgentDecisionSystem, Laws, SourceMap, 审计]
---

# ADS LAW Source Map Audit｜运行时约束来源审计

> 本页是 Batch D 的只读审计。目标是回答：`agent-decision-system/04_LAW-INVARIANTS.md` 里的 `LAW-01`–`LAW-13`，分别可以追溯到 Laws 1–102 的哪些 Law，哪些又来自 Foundation / Evaluation / Human-AI 等上游判断。  
> 本页不改 ADS 正典定义，不改 `_machine/*.yaml`，也不把 ADS 编号改成 Laws 编号。

> [!note] 执行状态（2026-07-08）
> 本审计的写入建议已落到 [[agent-decision-system/00_PROTOCOL#LAW-INVARIANTS Source Map|00_PROTOCOL · LAW-INVARIANTS Source Map]]。  
> 执行边界保持不变：不改 [[agent-decision-system/04_LAW-INVARIANTS|04 LAW-INVARIANTS]] 的运行时定义，不改 ADS `LAW-01`–`LAW-13` 编号。
>
> 2026-07-10 后续状态：在 Core Laws 外部核验后，`LAW-01`、`LAW-03`、`LAW-08`、`LAW-12` 已获独立授权并在保留 ID 的前提下更新运行时定义；本页表格保留为当时的来源审计快照。现行定义见 [[agent-decision-system/04_LAW-INVARIANTS|ADS LAW-INVARIANTS]]，改写影响见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|P0 影响审计]] 与 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 影响审计]]。

相关入口：[[agent-decision-system/04_LAW-INVARIANTS|ADS LAW-INVARIANTS]] · [[agent-decision-system/00_PROTOCOL|ADS Protocol]] · [[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]] · [[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] · [[01_编辑审计|编辑审计待办]]

## 审计边界

- `LAW-01`–`LAW-13` 是 **Agent Decision System 的运行时编号**。
- `Law 1`–`Law 102` 是 **The Laws of AI Engineering 的正典编号**。
- 本审计只建立“来源关系”，不做编号统一。
- 关系类型分四类：
  - **直接压缩**：ADS 这条基本就是某条 Law 的运行时压缩版。
  - **组合压缩**：ADS 这条由多条 Law 合成，不能写成单一来源。
  - **跨层来源**：除了 Laws，还明显来自 Foundation / Evaluation / Human-AI 等上游模块。
  - **边界提醒**：只适合做 related source，不宜写成 primary source。

## 一句话结论

13 条 ADS LAW 中，大约 7 条可以安全写入一个清晰的 primary source；其余更适合写成 source bundle。下一步如果要落到 ADS 正典，建议先在 [[agent-decision-system/00_PROTOCOL|00_PROTOCOL]] 的 SOURCE MAP 加一张 13 行对照表，而不是逐条改写 invariant 定义。

## Source Map 总表

| ADS LAW | 当前运行时含义 | Primary source | Related source | 关系类型 | 置信度 | 是否建议写入 ADS |
|---|---|---|---|---|---|---|
| `LAW-01` 验证易于生成 | 方案必须为验证而设计 | [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 13 — 可委托性定律（Delegability Law）\|Law 13]]；[[laws-of-ai-engineering/07_认识论与真理定律#Law 64 — 可证伪性定律（Falsifiability Law）\|Law 64]] | 直接压缩 | 高 | 建议写入 primary + related |
| `LAW-02` 压缩必然有损→会幻觉 | 不把模型当数据库，事实外置 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] + [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]] | [[laws-of-ai-engineering/01_信息与压缩定律#Law 5 — 检索优于记忆定律（Retrieval-Over-Memorization Law）\|Law 5]]；[[laws-of-ai-engineering/07_认识论与真理定律#Law 62 — 流畅度非正确性定律（Fluency-Is-Not-Truth Law）\|Law 62]] | 组合压缩 | 高 | 建议写 source bundle，不写单一 primary |
| `LAW-03` 分布内才可靠 + 校准 | 可委托性取决于分布与置信校准 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布证据边界定律（Distribution-Bounded Evidence Law）\|Law 7]] + [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]] | [[laws-of-ai-engineering/03_统计与泛化定律#Law 25 — 分布漂移定律（Distribution Shift Law）\|Law 25]]；[[laws-of-ai-engineering/07_认识论与真理定律#Law 63 — 不确定性外显定律（Surface-Uncertainty Law）\|Law 63]] | 组合压缩 | 高 | 建议写 source bundle |
| `LAW-04` 古德哈特 | 代理指标被优化后会脱钩 | [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24]] | [[laws-of-ai-engineering/10_对抗与安全定律#Law 93 — 对抗性古德哈特定律（Adversarial-Goodhart Law）\|Law 93]]；Evaluation | 直接压缩 | 高 | 建议写入 primary |
| `LAW-05` 一切输入皆指令 + 权限胜过自觉 | 外部内容不可信，权限硬边界优先 | [[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）\|Law 87]] + [[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）\|Law 94]] | [[laws-of-ai-engineering/05_接口与边界定律#Law 47 — 最小权限定律（Least-Privilege Law）\|Law 47]]；[[laws-of-ai-engineering/10_对抗与安全定律#Law 88 — 致命三重奏定律（Lethal-Trifecta Law）\|Law 88]]；[[laws-of-ai-engineering/10_对抗与安全定律#Law 90 — 无可靠转义定律（No-Reliable-Escaping Law）\|Law 90]]；[[laws-of-ai-engineering/10_对抗与安全定律#Law 92 — 数据即攻击面定律（Data-Is-Attack-Surface Law）\|Law 92]] | 组合压缩 | 高 | 建议写 source bundle |
| `LAW-06` 误差多步累积 + 恢复优于预防 | 长链路要分解、检查点、幂等恢复 | [[laws-of-ai-engineering/02_计算与验证定律#Law 14 — 误差累积定律（Error Compounding Law）\|Law 14]] + [[laws-of-ai-engineering/08_可靠性与失败定律#Law 77 — 恢复优于预防定律（Recovery-Over-Prevention Law）\|Law 77]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 17 — 幂等性定律（Idempotency Law）\|Law 17]]；[[laws-of-ai-engineering/02_计算与验证定律#Law 21 — 停机与预算定律（Termination-Budget Law）\|Law 21]]；[[laws-of-ai-engineering/04_系统与控制定律#Law 42 — 优雅降级定律（Graceful-Degradation Law）\|Law 42]] | 组合压缩 | 高 | 建议写 source bundle |
| `LAW-07` 上下文即状态 | 状态必须显式外置并重注入 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 2 — 上下文即状态定律（Context-is-State Law）\|Law 2]] | [[laws-of-ai-engineering/01_信息与压缩定律#Law 6 — 压缩必然丢失定律（Compression-Loses Law）\|Law 6]]；[[laws-of-ai-engineering/01_信息与压缩定律#Law 10 — 有效注意力有限定律（Finite-Effective-Attention Law）\|Law 10]] | 直接压缩 | 高 | 建议写入 primary |
| `LAW-08` 信任应随可靠性而非能力增长 | 信任和权限必须跟随实测可靠性 | [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84]] | [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）\|Law 95]]；[[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]]；Human-AI Collaboration | 直接压缩 + 成组 | 高 | 建议写入 primary + related |
| `LAW-09` 不可逆慢做可逆快做 | 可逆性决定审批和速度 | [[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）\|Law 74]] | [[laws-of-ai-engineering/08_可靠性与失败定律#Law 72 — 爆炸半径定律（Blast-Radius Law）\|Law 72]]；[[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] | 直接压缩 | 高 | 建议写入 primary + related |
| `LAW-10` 简单优先 | 复杂度必须为收益辩护 | [[laws-of-ai-engineering/04_系统与控制定律#Law 41 — 复杂度累积定律（Complexity-Accumulation Law）\|Law 41]] + [[laws-of-ai-engineering/11_演化与元定律#Law 99 — 简单性存活定律（Simplicity-Survives Law）\|Law 99]] | Foundation 简单优先；[[laws-of-ai-engineering/06_经济与资源定律#Law 57 — 规模效应定律（Scale-Effects Law）\|Law 57]] | 组合压缩 / 跨层来源 | 中高 | 建议写 source bundle，避免写成单一 Law |
| `LAW-11` 确定性优先 | 能用确定性方法就不要引入模型方差 | [[laws-of-ai-engineering/02_计算与验证定律#Law 18 — 确定性优先定律（Determinism-First Law）\|Law 18]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 13 — 可委托性定律（Delegability Law）\|Law 13]]；[[laws-of-ai-engineering/03_统计与泛化定律#Law 23 — 偏差-方差定律（Bias-Variance Law）\|Law 23]] | 直接压缩 | 高 | 建议写入 primary |
| `LAW-12` 判断力稀缺，责任不可委托 | 执行可委托，判断与责任不能外包 | [[laws-of-ai-engineering/11_演化与元定律#Law 100 — 判断力稀缺定律（Judgment-Is-Scarce Law）\|Law 100]] + [[laws-of-ai-engineering/09_人机与信任定律#Law 86 — 责任不可委托定律（Accountability-Cannot-Be-Delegated Law）\|Law 86]] | [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]]；Foundation；Human-AI Collaboration | 组合压缩 / 跨层来源 | 高 | 建议写 source bundle |
| `LAW-13` 信息守恒，垃圾进垃圾出 | 没有输入信息，下游不能凭空补救 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）\|Law 4]] | [[laws-of-ai-engineering/01_信息与压缩定律#Law 5 — 检索优于记忆定律（Retrieval-Over-Memorization Law）\|Law 5]]；Data Foundation；[[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1]] | 直接压缩 + 上游数据前提 | 高 | 建议写入 primary + related |

## 按置信度分类

### 可以安全写入 primary source 的条目

这些条目可以在下一步写入 ADS source map，但仍保留 ADS 自己的编号：

- `LAW-01` → Law 12
- `LAW-04` → Law 24
- `LAW-07` → Law 2
- `LAW-08` → Law 84
- `LAW-09` → Law 74
- `LAW-11` → Law 18
- `LAW-13` → Law 4

### 应写成 source bundle 的条目

这些条目不是单条 Law 的压缩，下一步不应硬写 primary-only：

- `LAW-02` → Law 1 + Law 6，另有关联 Law 5 / Law 62。
- `LAW-03` → Law 7 + Law 26，另有关联 Law 25 / Law 63。
- `LAW-05` → Law 87 + Law 94，另有关联 Law 47 / Law 88 / Law 90 / Law 92。
- `LAW-06` → Law 14 + Law 77，另有关联 Law 17 / Law 21 / Law 42。
- `LAW-10` → Law 41 + Law 99，并带 Foundation 的简单优先判断。
- `LAW-12` → Law 100 + Law 86，并带 Foundation / Human-AI 的责任边界。

## 建议的下一步写入方式

如果后续要把本审计落进 ADS 正典，我建议只做一件事：

在 [[agent-decision-system/00_PROTOCOL|00_PROTOCOL]] 的 `SOURCE MAP` 下面新增一张 13 行表：

```text
ADS LAW | Source type | Primary Laws | Related Laws / Modules | Note
```

不要先改 [[agent-decision-system/04_LAW-INVARIANTS|04_LAW-INVARIANTS]] 的定义文本。原因：

1. `04_LAW-INVARIANTS` 是运行时压缩层，保持短促有用比解释来源更重要。
2. `00_PROTOCOL` 本来就有 SOURCE MAP，是最适合放追溯关系的位置。
3. 先放表格，后续如果需要机器格式，再修改 `_tools/compile_decision_system.py` 让 YAML 带 `source` 字段。

## 不应做的事

1. 不要把 ADS `LAW-01`–`LAW-13` 改名成 Laws `Law 1`–`Law 102`。
2. 不要把 102 条 Laws 全塞进 ADS 运行时协议。
3. 不要因为有 source map，就把 ADS invariant 定义改长。
4. 不要把 `LAW-10` 简单优先只映射到 Law 99；它同时依赖复杂度累积、简单性存活和 Foundation 判断。
5. 不要把 `LAW-12` 只映射到 Law 100；责任不可委托同样是核心来源。
6. 不要把 related source 当 primary source；例如 Law 95 是 `LAW-08` 的相关边界，不是主来源。

## 本轮结论

ADS 的 13 条 LAW-INVARIANTS 不是 Laws 的子目录，而是全库正典经过运行时压缩后的“操作层不变式”。

这套映射是可建立的，但正确形态是：

```text
Laws / Foundation / Evaluation / Human-AI
  → source map
  → ADS LAW-01..13
  → Situation Router / Pattern Cards / Case Library
```

下一步可以安全做的是 `00_PROTOCOL` 的 source map 表；不建议马上改 `04_LAW-INVARIANTS` 正文。
