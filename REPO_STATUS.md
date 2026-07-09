---
type: repo-status
abstraction_layer: 运营机制（Repo 基线说明）
date: 2026-07-09
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, GitHub, Repo, Baseline]
---

# AI Engineering Knowledge Base · Private Repo 状态

> 本页说明这套知识库如何作为 private GitHub repo 维护。它不是学习入口；学习入口看 [[README|总入口]]，维护入口看 [[MAINTENANCE|维护手册]]。

## 当前策略

- **repo 根目录**：`02_Learn/05_AI_Lessons/AI-Engineering-KnowledgeBase/`
- **组织策略**：不重排正文书籍、不改中文文件名、不把 Wiki-link 转成 Markdown link。
- **顶层治理文件**：进入 private repo，保留在当前顶层，作为 Phase 1 baseline 的历史依据。
- **远端策略**：只上传 private GitHub repo；没有明确确认前不创建远端、不 push。

## 为什么不先大搬家

这套库已经有大量 Obsidian wikilink、ADS ↔ Case Library heading 级交叉引用、Laws heading 引用与体检脚本。首次 repo 化如果同时做目录重组，会把两个风险叠在一起：

1. GitHub 上传风险：是否误传临时文件、是否 remote/private 配置正确；
2. Obsidian 结构风险：链接是否断、歧义是否新增、治理文件是否失去上下文。

因此推荐顺序是：

1. 先提交当前结构作为 baseline；
2. 验证体检通过；
3. 如仍想整理治理文件，再单独做 `_governance/` 收纳批次。

## 应进入 repo 的文件类型

| 类型 | 处理 | 说明 |
|---|---|---|
| 十四本书正文 | 纳入 | 知识库主体 |
| Case Library / ADS | 纳入 | 应用层与机器层 |
| 顶层治理文件 | 纳入 | 记录架构、审计、收束依据 |
| `_tools/*.py` | 纳入 | 体检、编译、批量链接维护工具 |
| `_tools/validation_*.log` | 纳入 Phase 1 baseline | 作为本阶段维护证据；未来可按需清理 |
| `__pycache__/`、`.DS_Store`、真实密钥 | 排除 | 由 `.gitignore` 防止误提交 |

## GitHub 上传前检查清单

在 repo 根目录执行：

```bash
python3 _tools/kb_health_check.py
find . -type d -name __pycache__ -o -name .DS_Store
find . -type f \( -name '.env' -o -name '*.pem' -o -name '*.key' -o -name '*.p12' -o -name '*.pfx' \)
git status --short
```

必须满足：

- `kb_health_check.py` 输出 `体检通过 ✅`；
- 没有真实 secret/key 文件准备提交；
- `.gitignore` 已排除运行时缓存；
- remote 明确指向 private repo。

## 后续如需真正上传

确认 repo 名称后，可在本目录执行类似命令：

```bash
gh repo create <owner>/<repo-name> --private --source=. --remote=origin --push
```

如果不用 GitHub CLI，也可以手动创建 private repo 后：

```bash
git remote add origin git@github.com:<owner>/<repo-name>.git
git push -u origin main
```

> 注意：以上命令只有在确认 private repo 名称后执行；不要把整个 Obsidian Vault 作为 remote 根目录。

## 当前维护入口

- [[README|总入口]]
- [[MAINTENANCE|维护手册]]
- [[01_编辑审计|编辑审计]]
- [[03_使用路径与任务路由|使用路径与任务路由]]
- [[AGENTS|Agent 工作规则]]
