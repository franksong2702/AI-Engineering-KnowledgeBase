---
type: maintenance-guide
date: 2026-07-08
course: ai-engineering-knowledge-base
abstraction_layer: 运营机制（维护护栏）
tags: [AI工程, KnowledgeBase, Maintenance, 体检, Obsidian]
---

# AI Engineering Knowledge Base · 维护手册

> 本文是给未来的维护者（人、Codex、Claude、Fable 或其他 Agent）看的操作护栏。目标不是解释知识库内容，而是防止结构腐坏：断链、自描述漂移、ID 错配、元数据缺失、机器格式未同步。

## 维护总原则

1. **先分型，再动手**：先判断本轮属于结构修复、内容增量、正典改写、工具脚本、新书立项还是案例扩写。
2. **小批量、可回滚**：一次只做一类改动，避免把正文改写、链接修复、工具脚本混在同一个 diff 里。
3. **正典层谨慎**：`The-Constitution`、`laws-of-ai-engineering`、`agent-decision-system/03_ANTIPATTERN-DETECTORS.md`、`agent-decision-system/04_LAW-INVARIANTS.md` 属于高风险正典层，非明确授权不要改定义。
4. **新增数字要标注性质**：经验量级、编排值、测量值要区分；没有核验的数字不得写成实测结论。
5. **不要统一全库文风**：Laws、Foundation、Textbook、Case Library、Decision System 是不同体裁，不应洗成同一种模型腔。

## 改动类型与权限

| 类型 | 例子 | 默认处理方式 | 风险 |
|---|---|---|---|
| 结构修复 | 断链、frontmatter、aliases、README 自描述 | 可执行，但必须跑体检 | 低 |
| 工具脚本 | `_tools/kb_health_check.py`、`_tools/compile_decision_system.py`、`_tools/upgrade_law_wikilinks.py`、`_tools/audit_remaining_law_references.py` | 可执行，需正反向验证 | 中低 |
| 决策系统机器格式 | `_machine/*.yaml` 编译输出 | 由脚本生成，不手改 | 低 |
| 案例库扩写 | 深度化某几个 Case | 分批执行，保留精简层 | 中 |
| 正典改写 | Laws 定义、Constitution 条目、LAW/ANTI 正典 | 先提案，等确认 | 高 |
| 新书立项 | Multimodal、HCI、Governance | 先写边界和目录，再扩写 | 高 |
| 外部 citation | Laws 理论依据核验 | 必须查源，逐 family 做 | 高 |

## 每次维护后的必跑命令

在知识库根目录运行：

```bash
python3 _tools/kb_health_check.py
```

如果改动涉及 `agent-decision-system/`，还必须运行：

```bash
python3 _tools/compile_decision_system.py
```

如果改动涉及 `agent-decision-system/` ↔ `ai-engineering-case-library/` 的交叉引用，还必须运行：

```bash
python3 _tools/check_ads_case_crossrefs.py
```

如果改动涉及 Laws 引用系统，先审计，再看升级 dry-run：

```bash
python3 _tools/audit_remaining_law_references.py --write --low-sample-limit 0
python3 _tools/upgrade_law_wikilinks.py --list-limit 0
```

验收报告必须包含三件套：

```text
验证命令: <原样命令>
返回结果: <exit code / 关键输出行>
证据路径: <日志/文件/报告路径>
```

## 工具清单

| 工具 | 什么时候用 | 产物 / 判断 |
|---|---|---|
| `_tools/kb_health_check.py` | 每批改动后必跑 | 断链、歧义、元数据、Law heading 语义、ADS ↔ Case crossref guard、README 自描述等结构健康检查 |
| `_tools/compile_decision_system.py` | 改 `agent-decision-system/` 正典 md 后 | 重新生成 `agent-decision-system/_machine/*.yaml`；`--check` 只检查同步、不写文件，供 CI 与只读审查使用 |
| `_tools/check_ads_case_crossrefs.py` | 改 ADS ↔ Case Library 的路由入口、可直达案例、`LAW/PAT/ANTI/Q/SIT` 链接后 | 防止具体 ADS ID 退回文件级链接、裸 ID、缺失 heading、案例 heading 失效 |
| `_tools/upgrade_law_wikilinks.py` | 已确认某个 Law alias 可唯一指向具体 Law heading 时 | 批量把 Laws wikilink 升级到 heading；默认 dry-run，确认后才 `--apply` |
| `_tools/audit_remaining_law_references.py` | 需要重新审计剩余文件级 Laws 链接时 | 生成 [Remaining Candidates](_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md)；它不是活任务队列 |

## 体检脚本检查什么

`_tools/kb_health_check.py` 检查：

1. wikilink 断链；
2. wikilink 歧义；
3. 所有 wikilink 的 heading 是否精确存在；
4. frontmatter、`abstraction_layer`、INDEX aliases；
5. 决策系统 LAW/ANTI ID 标注一致性及有限的近邻短语误配；
6. ADS Markdown 与 `_machine/*.yaml` 是否同步；
7. ADS ↔ Case Library 的具体 ID 是否保持 heading 级一键直达；
8. README 自描述书数/文件数是否过期；
9. 生成环境泄漏关键词。

它不判断内容是否正确、citation 是否充分、章节是否足够深；这些仍需要主编判断。

Law 引用系统的当前收束边界见 [Law Reference System Closure](_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md)。如果升级脚本显示 `changed_links=0` 且体检通过，不要为了“清零”继续强行处理中确信度候选。

## 决策系统编译规则

`_tools/compile_decision_system.py` 把 `agent-decision-system` 的 Markdown 正典编译到：

```text
agent-decision-system/_machine/
```

维护规则：

- `_machine/*.yaml` 是生成物，不手改；
- 改 Markdown 后重跑编译器；
- 只想确认机器文件是否同步时运行 `python3 _tools/compile_decision_system.py --check`；该模式不写文件，CI 会通过总健康检查间接执行它；
- 编译器会严格校验条目数量、ID 序列、必填字段、空字段、重复字段、悬空引用和 ANTI severity；
- 编译失败时先修 Markdown 或 schema，不要绕过脚本。

## 文件命名与治理快照生命周期

命名本身是分层信号，后续新增文件按下面规则处理：

- **知识正文 / 入口页**：优先沿用现有数字前缀与中文标题，例如 `00_...`、`01_...`，或放入对应书的文件夹。
- **治理与维护文件**：可使用大写英文或明确的治理名，例如 `MAINTENANCE.md`、`_governance/laws/LAWS_TAXONOMY_REVIEW.md`、`_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md`。
- **外部模型审阅快照**：保留署名前缀，例如 `FABLE5_...`。这类文件是依据，不是活任务队列；可执行结论必须登记回 [编辑审计 · 待办清单](01_编辑审计.md)。
- **生成式审计文件**：例如 [Remaining Candidates](_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md)，必须能由脚本重复生成；不要手工把它改成永久计划书。

治理快照的生命周期规则：

1. 新快照必须写明它是“只读审查 / 计划 / 执行记录 / 收束说明”中的哪一种。
2. 快照可以提出建议，但不能另开活队列。
3. 当一个计划被执行完或被新口径取代，应在文件顶部补状态 note，并回链到 [编辑审计](01_编辑审计.md) 或 [维护手册](MAINTENANCE.md)。
4. 不为了整理而重命名或搬迁旧快照；用 README 文件地图解释即可。

## 元数据字段边界

- `abstraction_layer` 是全库字段，所有正文与治理 md 都应有。
- `stability` 当前只作为 Laws / 正典层 / 治理层的稳定性提示，不要求全库铺开。没有 `stability` 不等于“不稳定”，只是该层级不使用这个字段。
- Laws 每条定律的 `定律元信息` 以 [Metadata Schema](laws-of-ai-engineering/00_METADATA-SCHEMA.md) 为准；不要把这套字段机械复制到普通章节或案例里。

## 禁止事项

- 不要一轮全量重写任何一本书。
- 不要为润色而改变知识层级。
- 不要删除有意保留的多视角重复。
- 不要未经核验补外部 citation。
- 不要把经验数字写成实测数字。
- 不要手改 `agent-decision-system/_machine/*.yaml`。
- 不要在未确认的情况下安装系统定时任务。
- 不要在未确认边界前新增整本书。

## 可选：每周体检

低风险做法是手动运行：

```bash
cd '/Users/xuefusong/syncthings/Obsidian/Obsidian Vault/02_Learn/05_AI_Lessons/AI-Engineering-KnowledgeBase'
python3 _tools/kb_health_check.py
```

如果需要 macOS 自动定时体检，可参考样例：

```text
_tools/com.xuefusong.ai-kb-health-check.plist.example
```

注意：样例文件不会自动生效。只有在明确确认后，才可以复制到 `~/Library/LaunchAgents/` 并用 `launchctl` 启用。

## 推荐维护节奏

- **每次改动后**：跑 `kb_health_check.py`。
- **改 agent-decision-system 后**：跑 `compile_decision_system.py` + `kb_health_check.py`。
- **每周**：只跑体检，确认结构未腐坏。
- **每季度**：按 [季度定期重估协议](QUARTERLY_REEVALUATION_PROTOCOL.md) 扫描方法层两本书，问题是“模型强 100 倍这条还成立吗”；是否移入历史区必须由强模型或人裁决。

## 可选：季度定期重估日历样例

低风险做法是手动导入日历样例：

```text
_tools/ai-kb-quarterly-reevaluation.ics
```

注意：该 `.ics` 文件只是样例，不会自动写入系统日历。只有你手动打开/导入它，日历事件才会出现。导入后每季度按 [季度定期重估协议](QUARTERLY_REEVALUATION_PROTOCOL.md) 执行；证据收集可下放，移历史区和正典改写必须由强模型或人裁决。

## 当前后续批次入口

剩余工作以 [01_编辑审计 · 待办清单](01_编辑审计.md) 为准。做完一项后，更新该清单，并附验证命令。
