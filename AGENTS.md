---
type: maintenance-policy
abstraction_layer: 运营机制（Repo 与 Agent 护栏）
date: 2026-07-09
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, Agent规则, GitHub, 维护]
---

# AGENTS.md — AI Engineering Knowledge Base 工作规则

> 本文件面向未来接手这个公开 GitHub repo 的 Agent。它不是知识正文；真正的维护规则仍以 [维护手册](MAINTENANCE.md) 与 [编辑审计](01_编辑审计.md) 为准。

## 1. Repo 边界

- 本目录 `AI-Engineering-KnowledgeBase/` 是 repo 根目录。
- 不要把整个 Obsidian Vault 变成 Git repo。
- 不要在未确认前改动本目录之外的 vault 文件。
- 这是 public repo 口径；不要写入私人路径、密钥、真实账号 token、未脱敏日志或不应公开的个人材料。

## 2. Obsidian 原生格式

- 保留 Markdown、YAML frontmatter、Wiki-link：`[[note]]`、`[[folder/note|alias]]`、`[[file#heading|alias]]`。
- README、三份公共导航页以及各书 `00_INDEX` 的文件级入口使用标准相对 Markdown 链接，确保 GitHub 与 Obsidian 都能点击；README 允许不带 YAML frontmatter。
- 两端 heading slug 规则不同；正文和书目中的 heading 级知识引用继续使用 Obsidian Wiki-link，不为 GitHub 强行降级精度。
- 正文继续保留 Wiki-link；不要为了 GitHub 网页显示，把全库 Wiki-link 批量改成普通 Markdown 链接。
- 中文文件名、书内目录和现有编号结构保持不动；除非明确授权，不做大规模搬迁或重命名。

## 3. 活任务来源

- 唯一活任务队列：[编辑审计 · 待办清单](01_编辑审计.md)。
- 其他审计/计划/FABLE5 文件是依据或快照，不另开任务队列。
- 若审计快照与编辑审计冲突，以 [编辑审计](01_编辑审计.md) 为准。

## 4. 治理文件进入 repo 的原则

- 顶层治理文件可以进入 repo，因为它们记录了这套库为什么长成现在这样；写入前必须确认内容适合公开。
- 不要在首次 repo 化时顺手搬迁这些治理文件；先保留现状，形成可回滚 baseline。
- 如果以后要收纳到 `_governance/`，必须单独成批执行，并同步更新所有 wikilink 后跑体检。

## 5. 必跑验证

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

完成报告必须包含：

```text
验证命令: <原样命令>
返回结果: <exit code / 关键输出行>
证据路径: <日志/文件/报告路径>
```

## 6. Git / GitHub 操作边界

- 可以在本地小批量 commit。
- 不要在未得到明确授权前 push、force-push、改 remote、删除分支或重写历史。
- 上传 GitHub 前按 public repo 标准检查密钥、私人路径、未脱敏日志和第三方内容许可。
- 若要接入 CI，先只跑 `_tools/kb_health_check.py`，不要引入复杂构建链。

## 7. 高风险区

以下区域非明确授权不要改定义：

- [The Constitution of AI Engineering](The-Constitution-of-AI-Engineering.md)
- [The Laws of AI Engineering](laws-of-ai-engineering/00_INDEX.md) 的 Law 定义
- [ADS Antipattern Detectors](agent-decision-system/03_ANTIPATTERN-DETECTORS.md)
- [ADS Law Invariants](agent-decision-system/04_LAW-INVARIANTS.md)

能机械修的结构问题可以修；正典判断、整本书立项、外部 citation 全量扩展需要先提案。
