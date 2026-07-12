---
type: law-reference-system-closure
date: 2026-07-08
course: AI-Engineering-KnowledgeBase
abstraction_layer: 运营机制（引用系统收束）
status: closed-for-system-maintenance
aliases: [Law引用系统收束说明, LawsReferenceClosure]
tags: [AI工程, Laws, 引用系统, 维护, Obsidian]
---

# Law Reference System Closure｜引用系统收束说明

> 这页说明：Law 引用系统现在算“收束”到什么程度，以及后续 Agent 应该怎么维护。  
> 相关入口：[[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] · [[_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES|Remaining Candidates]] · [[_governance/laws/LAW_REFERENCE_AUDIT|Law Reference Audit]]

## 一句话结论

> [!note] 2026-07-09 状态更新
> 61 个中确信度候选已由 Fable 5 逐条裁决完毕：22 处升级、2 处去链、37 处裁决为保留（终态，非待办）。`audit_remaining_law_references.py` 现报 high_confidence=0；本页"剩余工作怎么看"一节的队列已清空，后续仅在新内容引入新候选时按本页流程处理。

Law 引用系统已经从“靠人工记忆”变成“有策略、有脚本、有健康检查”的维护状态。

后续不应该再困在 Laws 里做无限清理；只有当某个剩余候选真的能明确指向某条 Law 时，才继续收窄。

## 本轮完成了什么

### 1. 具体 Law 引用优先跳到 heading

已经按你的要求，把能确定的 Laws 引用升级为具体 Law heading，而不是只跳到 family/index 文件。

本轮 7E-patch 处理的是“原来属于中确信度，但读上下文后已经足够明确”的 alias，例如：

- `停机问题` → Law 21
- `忽略方差` → Law 23
- `优化 benchmark 而非真实能力` → Law 24
- `校准差` / `置信度应匹配准确率` → Law 26
- `忽略基率` / `罕见事件判断错误` → Law 27
- `过拟合测试集` → Law 30
- `长尾主导失败` → Law 31
- `紧耦合` → Law 50
- `地图当疆域` → Law 65
- `诚实的无知` → Law 67
- `技能退化` / `用户能力退化` / `让人退化` → Law 82
- `一切进入上下文的文本都可能是指令` → Law 87
- `持久化攻击面` → Law 92
- `涌现` → Law 101

处理方式不是手工一条条改，而是把这些 alias 加入 `_tools/upgrade_law_wikilinks.py` 的显式白名单，再用脚本批量生成正确 heading。

### 2. 剩余候选现在可以重复生成

新增脚本：`_tools/audit_remaining_law_references.py`

它会重新生成 [[_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES|剩余候选审计]]，并把剩余文件级 Laws 链接分成三类：

1. **高确信度候选**：升级脚本已经能识别，应该先跑 `_tools/upgrade_law_wikilinks.py --apply`。
2. **中确信度候选**：语义像某条 Law，但 alias 不是正典标题，需要读上下文。
3. **低确信度 / 不建议改**：整本书、family、治理页、导航页，应该保持文件级链接。

当前状态：

- 高确信度候选：0
- 中确信度候选：61
- 低确信度 / 不建议改：158

这里的“剩余 219 个文件级 Laws 链接”不是 219 个待修 bug。大部分是本来就应该保留的入口、family 或治理链接。

### 3. 健康检查负责防止未来回退

现有 `_tools/kb_health_check.py` 已经能检查：

- 断链；
- 歧义链接；
- 表格里的 wikilink alias pipe；
- Law alias、family 文件、heading 三者是否一致；
- Laws 元信息 schema；
- README 自描述文件数。

也就是说，未来如果有人把 `Law 24` 链到错误 family，或者 heading 写错，健康检查应该失败。

## 后续维护规则

### 可以自动处理的情况

只有满足下面条件，才适合加入 `_tools/upgrade_law_wikilinks.py` 的 alias 白名单：

1. 这个 alias 已经是 wikilink；
2. 链接目标已经指向 Laws 系统或某个 Laws family；
3. 读上下文后能明确对应唯一 Law；
4. 这个 alias 不会明显误伤其他 Law 或普通工程含义。

例子：`未测试即坏的` 可以指向 Law 78；`评测` 不行，因为它太泛。

### 不应该自动处理的情况

以下情况不要为了“清零”而改：

- 指向 [[laws-of-ai-engineering/00_INDEX|Laws INDEX]]、[[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]]、[[laws-of-ai-engineering/00_REFERENCE-POLICY|Reference Policy]] 的导航链接；
- 指向某个 family 总览的链接，例如“统计与泛化定律（第 22–32 条）”；
- alias 是复合问题，例如 `prompt injection、越狱、数据泄露`；
- alias 太短或太泛，例如 `评测`、`验证`、`泄漏`、`回归`；
- 语义可能跨多条 Law，例如“无法止损”可能涉及不可逆性、恢复、爆炸半径。

## 未来 Agent 的标准流程

如果未来继续维护 Law 引用，请按这个流程：

```bash
# 1. 查看是否还有脚本可机械升级的高确信度候选
python3 _tools/audit_remaining_law_references.py --write --low-sample-limit 0

# 2. 如果 A 区不为 0，先看 dry-run
python3 _tools/upgrade_law_wikilinks.py --list-limit 80

# 3. 确认后再写入
python3 _tools/upgrade_law_wikilinks.py --apply

# 4. 重新生成剩余审计
python3 _tools/audit_remaining_law_references.py --write --low-sample-limit 0

# 5. 最终验收
python3 _tools/upgrade_law_wikilinks.py --list-limit 0
python3 _tools/kb_health_check.py
```

如果第 5 步里 `changed_links=0`，且健康检查通过，就不要继续强行清理。

## 当前剩余工作怎么看

现在剩下的 61 个中确信度项，不是系统债，而是内容判断队列。

执行归口：这些候选是否继续处理，以 [[01_编辑审计#待办清单（后续批次的唯一有效位置，做完即勾）|01_编辑审计 · 待办清单]] 为准；本页只说明 Law Reference System 的收束边界与维护方法，不另立活队列。

它们可以未来按主题慢慢处理，例如：

- Anti-Patterns 里的安全/可靠性/复杂度表达；
- Evaluation 里的方差、分布不匹配、评测污染；
- Human-AI Collaboration 里的审批、责任、技能退化边界。

但它们不应该阻塞全局 Knowledge Base 的 architecture review、taxonomy review 或其他书的优化。

## 收束后的判断

Law 引用系统现在已经可以交给脚本和健康检查维护。

下一步应该把注意力拉回整个 AI Engineering Knowledge Base：看各本书之间的架构关系、重复内容、学习路径、案例库和决策系统之间的映射，而不是继续手工追逐每一个 Laws 链接。
