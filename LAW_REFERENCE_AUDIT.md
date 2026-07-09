---
type: law-reference-audit
date: 2026-07-08
course: ai-engineering-knowledge-base
abstraction_layer: 图谱层（正典一致性审计）
tags: [AI工程, Laws, 正典, 审计, 维护]
---

# 七条核心定律援引盘点报告

> 本报告对应 [[01_编辑审计|编辑审计]] 待办中的“各书正文援引七条核心定律处统一为‘见 Law N’格式”。  
> 本轮只做盘点与改/留建议，不改正文定义、不批量替换、不做 citation 核验。

> [!note] Batch 6 更新
> 本报告最初以“七条核心定律”作为扫描口径；后续 Laws 已升级为 [[laws-of-ai-engineering/00_INDEX|Law System]]，入口层引用应优先看 [[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]] 和 [[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]]。因此，本报告继续作为引用候选清单保留，但执行顺序与是否加链接以 Reference Policy 为准。

## 1. 本轮结论

当前知识库已经把 Laws 升级为 [[laws-of-ai-engineering/00_INDEX|Law System]]，并用 [[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]] 管理全库核心引用。但跨书正文里的援引方式仍不完全一致：有的写成核心概念，有的写成应用性展开，有的已有链接，有的只有短语。

**不建议全库机械替换。** 正确做法是把引用分成三类：

1. **必须改**：入口页、总图、学习路径、README、宪法等“导览层”出现核心定律时，应显式标注“见 Law N”。
2. **建议改**：各书 INDEX 或章节开头首次定义/总结这些定律时，应补一个正典链接。
3. **建议保留**：正文里的应用性表述、案例分析、具体 checklist，不要为了统一而洗成同一种句式。

一句话：**统一的是正典指向，不是统一文风。**

## 2. 当前采用的七条正典口径

历史扫描以 [[laws-of-ai-engineering/00_INDEX|Laws INDEX]] 早期“七条核心定律”口径为准；后续执行以 [[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]] 与 [[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] 为准：

| 核心定律 | 正典位置 | 推荐援引写法 |
|---|---|---|
| 验证易于生成 | [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）\|Law 12]] | 验证易于生成（见 Law 12） |
| 压缩必然有损 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 1 — 有损压缩定律（Lossy Compression Law）\|Law 1/6]] | 压缩必然有损（见 Law 1/6） |
| 分布内才可靠 | [[laws-of-ai-engineering/01_信息与压缩定律#Law 7 — 分布内可靠定律（In-Distribution Reliability Law）\|Law 7]] | 分布内才可靠（见 Law 7） |
| 古德哈特定律 | [[laws-of-ai-engineering/03_统计与泛化定律#Law 24 — 古德哈特定律（Goodhart's Law）\|Law 24]] | 古德哈特定律（见 Law 24） |
| 校准定律 | [[laws-of-ai-engineering/03_统计与泛化定律#Law 26 — 校准定律（Calibration Law）\|Law 26]] | 校准（见 Law 26） |
| 不可逆性定律 | [[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）\|Law 74]] | 不可逆性（见 Law 74） |
| 信任-可靠性剪刀差 | [[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）\|Law 84]] | 信任-可靠性剪刀差（见 Law 84） |

补充：能力-可靠性剪刀在当前体系里更接近 [[laws-of-ai-engineering/11_演化与元定律#Law 95 — 能力-可靠性剪刀定律（Capability-Reliability-Scissors Law）|Law 95]]，并与 Law 84 互相解释；不要把它粗暴并入 Law 84，也不要把它当成与 Law 84 完全无关的新定律。

## 3. 扫描概览

扫描范围：排除 `FABLE5*`、`MAINTENANCE.md`、`_tools/` 和本报告，覆盖 138 个内容/结构 Markdown 文件。结果是粗扫，不等于全部都要修改。

| 核心定律 | 命中文件数 | 命中次数 | 判断 |
|---|---:|---:|---|
| 验证易于生成 | 24 | 47 | 导览层多次出现，应补 Law 12 指向 |
| 压缩必然有损 | 20 | 40 | 与分布内可靠、幻觉、RAG 多处连用，适合在导览层补 Law 1/6 |
| 分布内才可靠 | 14 | 21 | 命中较少，主要是核心概念，应统一首次援引 |
| 古德哈特 | 51 | 140 | 分布最广，不应逐处改；只处理定义性/入口性出现 |
| 校准 | 65 | 356 | 大量是普通工程词或评价术语，强烈不建议全量加链接 |
| 不可逆性 | 50 | 307 | 大量是决策/权限场景应用，不建议全量加链接 |
| 信任-可靠性剪刀差 | 45 | 186 | 人机协作、评价、案例库中高度集中；应统一“Law 84 / Law 95”的边界 |

## 4. 高优先级候选修改点

以下是后续真正改正文时的第一批候选。它们共同特点是：读者会把这些文件当入口或正典压缩层，因此“见 Law N”的价值高，且改动小。

### 4.1 [[00_Knowledge-Graph-总图|总图]]

建议处理：

- 在“根命题/星系图/隐藏主线”里，首次出现“验证易于生成、压缩有损、分布内可靠、古德哈特、信任-可靠性剪刀差”时补正典指向。
- 不需要给每个图节点都加链接，否则会破坏图的可读性。

推荐方式：在图后加一个短注，而不是改图本身：

```md
注：图中七条核心定律的权威定义见 [[laws-of-ai-engineering/00_INDEX|Laws INDEX · 七条核心定律正典声明]]。
```

### 4.2 [[02_学习路径与未来扩展|学习路径与未来扩展]]

用户当前选中的这句：

```text
分布内可靠 ← 压缩有损
```

建议改成更可读但不破坏拓扑的形式：

```text
分布内可靠（见 Law 7） ← 压缩有损（见 Law 1/6）
```

或在拓扑图后补解释：

> 因为模型是训练分布的有损压缩（Law 1/6），所以它在分布内更可靠、在分布外更容易失真（Law 7）。

这是一个低风险、高收益的小改动。

### 4.3 [[README|README]]

README 的压缩句里出现“生成廉价、验证稀缺”，建议补一个不打断阅读的括注：

```md
生成廉价、验证稀缺（见 Law 12）
```

README 不适合塞完整解释，只要把读者导向 Laws 正典即可。

### 4.4 [[The-Constitution-of-AI-Engineering|The Constitution]]

宪法内部也有 Law 1–10，但它的编号是“宪法压缩编号”，不是 Laws 全书编号。建议在开头加一行编号说明：

> 说明：本章 Law 1–10 是宪法内部压缩编号；完整正典编号、适用边界与验证方法以 [[laws-of-ai-engineering/00_INDEX|Laws]] 为准。

这样可以避免读者把“宪法 Law 4 古德哈特”和“Laws 全书 Law 24 古德哈特”混淆。

### 4.5 [[01_编辑审计|编辑审计]] R2 历史措辞

R2 里目前的七条写法与当前 Laws INDEX 的七条正典声明不完全一致：

- R2 写到“能力-可靠性剪刀”；
- 当前 Laws INDEX 的七条里有“压缩必然有损”，而能力-可靠性更接近 Law 95 的能力版。

建议后续微调 R2 的说明，让它明确：当前七条以 Laws INDEX 为准；能力-可靠性剪刀作为 Law 95 与 Law 84 的邻近定律处理。

## 5. 中优先级候选修改点

这些文件不是总入口，但承担各书入口或章节入口角色，可以只在首次出现时补正典指向。

### 5.1 Foundation

候选文件：

- [[foundation-of-ai-engineering/01_未来20年不变的规律|未来20年不变的规律]]
- [[foundation-of-ai-engineering/05_最值得写进教材的知识|最值得写进教材的知识]]
- [[foundation-of-ai-engineering/08_结语|结语]]

建议：只在首次定义性出现处加“见 Law N”。不要改 Foundation 的语气，因为它是原则/判断层，不是 Laws 的复制品。

### 5.2 Evaluation

候选文件：

- [[evaluation-of-ai-systems/00_INDEX|Evaluation INDEX]]
- [[evaluation-of-ai-systems/01_评价的基础理论|评价的基础理论]]
- [[evaluation-of-ai-systems/06_评价设计模式|评价设计模式]]
- [[evaluation-of-ai-systems/07_未来趋势|未来趋势]]

建议：古德哈特、校准、信任-可靠性在这里大量出现，但它们是评价理论的正文内容。只需要在 INDEX 或 Part 1 的首次定义处补正典链接；正文内不要每次都补。

### 5.3 Human-AI Collaboration

候选文件：

- [[human-ai-collaboration-foundation/03_建立正确信任|建立正确信任]]
- [[human-ai-collaboration-foundation/04_对抗自动化偏见|对抗自动化偏见]]
- [[human-ai-collaboration-foundation/10_失败模式与评价|失败模式与评价]]

建议：这些文件主要是 Law 84 的应用层。首次出现“信任-可靠性剪刀差”时明确“见 Law 84”；提到“能力-可靠性剪刀”时可补“能力版见 Law 95”。

### 5.4 AI Systems in Production / Data Foundation / Model Adaptation

候选文件：

- [[ai-systems-in-production/03_可观测性|可观测性]]
- [[ai-systems-in-production/05_成本工程|成本工程]]
- [[data-foundation-of-ai-systems/04_数据评价与漂移|数据评价与漂移]]
- [[model-adaptation/03_对齐与偏好|对齐与偏好]]
- [[model-adaptation/05_定制的评价与风险|定制的评价与风险]]

建议：只在章节开头或小节标题附近补 Law 指向。尤其古德哈特在对齐、成本、数据评价里是应用性展开，不要改成单薄的“见 Law 24”而删掉原有工程语境。

## 6. 低优先级或不建议改的区域

### 6.1 Case Library

案例库中很多地方已经通过 `LAW-xx / PAT-xx / ANTI-xx / Q-xx` 指向决策系统。这里的目标不是让每个案例再连回 Laws，而是保持案例可读。

建议只处理两类：

1. “Relevant Laws” 明确列核心定律但没有链接；
2. 把“能力-可靠性剪刀”和“信任-可靠性剪刀差”混用的地方。

例如 [[ai-engineering-case-library/04_可靠性与生产|可靠性与生产]] 中“能力-可靠性剪刀 · 长尾定律”需要后续判断：它更像 Law 95，还是本案例实际想表达 Law 84。

### 6.2 Decision System

[[agent-decision-system/04_LAW-INVARIANTS|LAW-INVARIANTS]] 已经是操作层正典投影，不建议在这轮为了“见 Law N”再改。它有自己的 `LAW-01` 到 `LAW-13` 编号，与 Laws 全书编号不是一套编号系统。

如果要改，应另开“编号对照表”任务，不要混入本次正文援引统一。

### 6.3 高频普通词：校准 / 不可逆

“校准”和“不可逆”在很多地方是普通工程动作，不总是在引用 Law 26 或 Law 74。

不建议把所有“校准”改成“校准（见 Law 26）”，也不建议把所有“不可逆”改成“不可逆性（见 Law 74）”。这样会让文本变重，而且产生假正典化。

## 7. 建议的后续执行批次

### 批次 A：入口层微改，低风险 —— ✅ 已由 Batch 6 覆盖主体入口

已同步：

- [[00_Knowledge-Graph-总图|总图]]
- [[02_学习路径与未来扩展|学习路径与未来扩展]]
- [[README|README]]
- [[The-Constitution-of-AI-Engineering|The Constitution]]

目标已从“七条核心定律在哪里”升级为“Law System 怎么用”：入口层说明了 Laws/Core Laws/S-A-B/三套编号边界。[[01_编辑审计|编辑审计]] R2 属于历史审计记录，暂不在 Batch 6 中改写。

验收：

```bash
python3 _tools/kb_health_check.py
```

并人工抽查入口层是否只增加正典指向，没有改写定义。

### 批次 B：各书 INDEX / 章节首次出现

范围：Foundation、Evaluation、Human-AI Collaboration、Data Foundation、Model Adaptation、Production 的 INDEX 或章节开头。

目标：每本书的第一次定义性援引有 Law 指向，后文应用不重复打断。

验收：抽检每本书 1–2 处，确认“正典链接清楚、原有应用语境保留”。

### 批次 C：Case Library 混用点

范围：只处理“Relevant Laws”或明确混用“能力-可靠性 / 信任-可靠性”的案例。

目标：保持案例短小，但核心定律指向不混乱。

验收：跑健康检查；抽查被改案例仍保持案例库体裁，不变成理论讲义。

## 8. 禁止做法

- 不要全库搜索替换“古德哈特 → 古德哈特（见 Law 24）”。
- 不要把每个“校准”“不可逆”都变成 Law 链接。
- 不要为了统一正典而删除各书自己的应用性解释。
- 不要把 Laws 全书编号、宪法压缩编号、Decision System 的 `LAW-xx` 操作编号混成一套。
- 不要在本任务中补外部 citation；那是另一项高风险核验项目。

## 9. 我的建议

下一步如果要真正改正文，建议进入 Batch 7：各书 INDEX / 章节首次出现的分层引用修复。入口层主体已由 Batch 6 同步，后续不应重复做同一批次。历史上用户选中的这句仍可作为 Batch 7 的参考例子：

```text
分布内可靠 ← 压缩有损
```

这句话背后的关系是：**模型是训练分布的有损压缩，所以分布内更可靠、分布外更易失真**。如果加上 Law 指向，读者会更容易从学习路径跳到 Laws 正典。
