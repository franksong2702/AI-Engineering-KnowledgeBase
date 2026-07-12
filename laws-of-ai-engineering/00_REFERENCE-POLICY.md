---
type: law-reference-policy
date: 2026-07-08
course: laws-of-ai-engineering
abstraction_layer: 运营机制（引用策略）
stability: 中高（维护规则，随 taxonomy 调整）
tags: [AI工程, Laws, 引用策略, Obsidian, 定义边界]
---

# Reference Policy｜Laws 引用策略

> 本页回答一个问题：全局 Knowledge Base 什么时候可以写“见 Law N”，什么时候不应该写？

相关入口：[[laws-of-ai-engineering/00_INDEX|Laws INDEX]] · [[00_CORE-LAWS|Core Laws]] · [[00_LAW-RELATION-GRAPH|Law Relation Graph]] · [[_governance/laws/LAWS_TAXONOMY_REVIEW|Laws Taxonomy Review]] · [[_governance/laws/LAW_REFERENCE_AUDIT|Law Reference Audit]] · [[_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES|Remaining Candidates]] · [[_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE|Law Reference Closure]]

## 核心判断

102 条 Law 不是同一硬度，也不应该同等频繁地被全库引用。

| 层级 | 用途 | 引用范围 | 典型动作 |
|---|---|---|---|
| S | 全库核心 law | README、总图、宪法、Foundation、Evaluation、Agent Decision System 等入口或核心模块 | 可以作为稳定 cross-reference，但仍需说明适用边界 |
| A | family anchor / 重要工程原则 | 与该 family 直接相关的模块首次定义处 | 适合在专题页做一次“来源/约束”说明 |
| B | contextual principle / heuristic | 具体场景、具体案例、具体风险提示 | 不做全库铺开；只在直接有用时引用 |

完整 S 级清单见 [[00_CORE-LAWS|Core Laws]]；关系分组见 [[00_LAW-RELATION-GRAPH|Law Relation Graph]]。

## 禁止的引用方式

1. **禁止搜索替换式加链接**：不要把全库所有“校准”“不可逆”“古德哈特”“可靠性”自动改成 Law 链接。
2. **禁止把 B 级原则写成全库公理**：B 级条目可以有价值，但它们通常依赖具体场景、技术代际或工程条件。
3. **禁止混用三套编号系统**：`Law 12`、`LAW-12`、`Constitution Law 12` 不是同一个命名空间。
4. **禁止用 Law 链接掩盖论证缺口**：如果正文没有解释为什么适用，就不要只写“见 Law N”。
5. **禁止让案例库继承全部 102 条 Laws**：案例库主要承接 [[agent-decision-system/00_PROTOCOL|Agent Decision System]] 的操作约束，只在必要处补 Laws 来源。

## 三套编号边界

> [!warning] 第四、五套小清单：手册内部定律（2026-07-09 通读后补）
> 除三套主编号外，[[multi-agent-patterns-handbook/00_INDEX#五条跨模式定律|Multi-Agent 手册有 5 条跨模式定律]]、[[llm-design-patterns/00_INDEX#六条跨模式定律|Design Patterns 有 6 条跨模式定律]]。引用它们**必须带书名前缀并链到该手册 INDEX 的对应小节**（如"Multi-Agent 定律 1：上下文隔离"），禁止裸写"定律 N"或链到 Laws INDEX——通读曾清出 9 处此类串号/错链。

| 命名空间 | 形式 | 所属文件/模块 | 含义 |
|---|---|---|---|
| Laws | `Law 1`–`Law 102` | [[laws-of-ai-engineering/00_INDEX\|The Laws of AI Engineering]] | 底层规律、原则、启发式的编号体系 |
| Constitution | 内部 `Law 1`–`Law 10` | [[The-Constitution-of-AI-Engineering]] | 全库极限压缩后的 10 条宪法级原则 |
| Agent Decision System | `LAW-01`–`LAW-13` | [[agent-decision-system/04_LAW-INVARIANTS\|LAW-INVARIANTS]] | Agent 运行时的操作约束 |

写引用时必须让读者一眼看出你在引用哪套系统。必要时用完整链接而不是裸编号。

## 模块级引用策略

| 模块 | 推荐策略 | 不推荐策略 |
|---|---|---|
| [[README\|README]] | 只引用少数 S 级核心，说明全库地基 | 列出 102 条或把 README 变成 Laws 摘要 |
| [[00_Knowledge-Graph-总图\|知识图谱总图]] | 用 S 级解释模块之间的逻辑依赖 | 把每条边都追溯到一个 Law |
| [[02_学习路径与未来扩展\|学习路径]] | 在关键学习阶段提示应掌握的核心 Law | 为每个学习任务都补 Law 链接 |
| [[The-Constitution-of-AI-Engineering\|Constitution]] | 说明 Constitution 与 Laws 的编号边界和来源关系 | 用 Laws 1–102 改写 Constitution 内部 10 条 |
| [[foundation-of-ai-engineering/00_INDEX\|Foundation]] | 在 first principles 处引用 Law 12、Law 1/4/6、Law 7、Law 24 等 | 把工程原则全部归因到 Laws |
| [[evaluation-of-ai-systems/00_INDEX\|Evaluation]] | 重点引用 Law 12、Law 24、Law 26、Law 62、Law 64 | 把所有评测方法都硬连到 Laws |
| [[ai-engineering-anti-patterns/00_INDEX\|Anti-Patterns]] | 只在反模式根因清晰对应时引用 S/A Law | 为每个反模式都补一个 Law |
| [[human-ai-collaboration-foundation/00_INDEX\|Human-AI Collaboration]] | 引用 Law 74、Law 84、Law 86、Law 95、Law 100 | 混淆信任、能力、责任三类问题 |
| [[ai-engineering-case-library/00_INDEX\|Case Library]] | 优先保持 Agent Decision System ID；必要时补核心 Laws 来源 | 把案例库改成 Laws 注释本 |
| [[agent-decision-system/00_PROTOCOL\|Agent Decision System]] | 保持 `LAW-01`–`LAW-13`，只在 source map 中解释与 Core Laws 的关系 | 把 102 条 Laws 直接塞进 runtime protocol |

## 引用格式建议

如果引用的是某一条具体 Law，优先链接到具体标题。这样读者点进去以后直接看到那条 Law，而不是只跳到 family 文件首页。

```markdown
见 [[laws-of-ai-engineering/02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）|Law 12：验证-生成不对称定律]]。
```

如果引用的是本书内部相邻页面，可以使用短链接：

```markdown
见 [[02_计算与验证定律#Law 12 — 验证-生成不对称定律（Verification-Generation Asymmetry Law）|Law 12：验证-生成不对称定律]]。
```

只有在引用整本书、某个 family、Core Laws、关系图、治理页，或者目标没有稳定 Law 标题时，才使用文件级链接。

维护规则：`kb_health_check.py` 会检查 `Law N：标题` alias、目标 family 文件、`#Law N — ...` heading 三者是否一致；任何一个写错，体检都应该失败。修正时不要猜标题，直接按报错里的“应为「...」”替换链接 heading。

## 批量修正机制

不要手工一个链接一个链接改。需要先审计，再批量升级。

审计剩余候选时，使用：

```bash
# 重新生成剩余文件级 Laws 链接清单
python3 _tools/audit_remaining_law_references.py --write --low-sample-limit 0
```

需要批量升级或修正 Law 链接时，使用：

```bash
# 只看会改什么，不写文件
python3 _tools/upgrade_law_wikilinks.py

# 确认范围后再实际写入
python3 _tools/upgrade_law_wikilinks.py --apply
```

这个脚本只处理已经写成 wikilink 的 Laws 引用；不会把普通正文里的 `Law N` 自动变成链接。它能识别 `Law N：标题` alias，也能识别与 Law 中文标题精确匹配的 alias（例如“古德哈特定律”“古德哈特”），然后从真实的 `## Law N — ...` 标题生成 heading，不手写锚点。

当前 Law 引用系统的收束状态见 [[_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE|Law Reference Closure]]；剩余中确信度候选见 [[_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES|Remaining Candidates]]。

## 每次引用维护的验收标准

任何全库 Law reference pass 完成时，至少检查：

1. `kb_health_check.py` 通过；
2. 无断链、无歧义链接；
3. 没有把 `LAW-01`–`LAW-13` 与 `Law 1`–`Law 102` 混写；
4. Case Library 没有被误改成 Laws 注释本；
5. 抽样阅读确认新链接确实帮助理解，而不是制造噪音。

## 当前阶段的结论

先建立引用规则，再做全局链接修复。否则最容易出现的问题是：看似 cross-reference 变多了，实际把读者从一个清晰知识图谱带进编号迷宫。
