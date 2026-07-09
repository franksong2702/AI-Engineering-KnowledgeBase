---
type: maintenance-policy
abstraction_layer: 运营机制（Repo 与 Agent 护栏）
date: 2026-07-09
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, Agent规则, GitHub, 维护]
---

# AGENTS.md — AI Engineering Knowledge Base 工作规则

> 本文件面向未来接手这个 private GitHub repo 的 Agent。它不是知识正文；真正的维护规则仍以 [[MAINTENANCE|维护手册]] 与 [[01_编辑审计|编辑审计]] 为准。

## 1. Repo 边界

- 本目录 `AI-Engineering-KnowledgeBase/` 是 repo 根目录。
- 不要把整个 Obsidian Vault 变成 Git repo。
- 不要在未确认前改动本目录之外的 vault 文件。
- 这是 private repo 口径；不要把私人路径、密钥、真实账号 token、未脱敏日志推到公开仓库。

## 2. Obsidian 原生格式

- 保留 Markdown、YAML frontmatter、Wiki-link：`[[note]]`、`[[folder/note|alias]]`、`[[file#heading|alias]]`。
- 不要为了 GitHub 网页显示，把全库 Wiki-link 批量改成普通 Markdown 链接。
- 中文文件名、书内目录和现有编号结构保持不动；除非明确授权，不做大规模搬迁或重命名。

## 3. 活任务来源

- 唯一活任务队列：[[01_编辑审计#待办清单（后续批次的唯一正典位置，做完即勾）|编辑审计 · 待办清单]]。
- 其他审计/计划/FABLE5 文件是依据或快照，不另开任务队列。
- 若审计快照与编辑审计冲突，以 [[01_编辑审计|编辑审计]] 为准。

## 4. 治理文件进入 repo 的原则

- 顶层治理文件要进入 private repo，因为它们记录了这套库为什么长成现在这样。
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
- 不要在未得到明确授权前 push、force-push、改 remote、创建公开 repo、删除分支或重写历史。
- 上传 GitHub 前先确认 repo 是 private。
- 若要接入 CI，先只跑 `_tools/kb_health_check.py`，不要引入复杂构建链。

## 7. 高风险区

以下区域非明确授权不要改定义：

- [[The-Constitution-of-AI-Engineering|The Constitution of AI Engineering]]
- [[laws-of-ai-engineering/00_INDEX|The Laws of AI Engineering]] 的 Law 定义
- [[agent-decision-system/03_ANTIPATTERN-DETECTORS|ADS Antipattern Detectors]]
- [[agent-decision-system/04_LAW-INVARIANTS|ADS Law Invariants]]

能机械修的结构问题可以修；正典判断、整本书立项、外部 citation 全量扩展需要先提案。
