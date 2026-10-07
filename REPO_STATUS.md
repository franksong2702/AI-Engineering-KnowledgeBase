---
type: repo-status
abstraction_layer: 运营机制（Repo 基线说明）
date: 2026-07-09
updated: 2026-07-10
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, GitHub, Repo, Baseline]
---

# AI Engineering Knowledge Base · Public Repo 状态

> 本页说明这套知识库如何作为 public GitHub repo 维护。它不是学习入口；学习入口看 [总入口](README.md)，维护入口看 [维护手册](MAINTENANCE.md)。

## 当前 GitHub 状态（2026-07-10）

- **GitHub repo**：`https://github.com/franksong2702/AI-Engineering-KnowledgeBase`
- **可见性**：public（GitHub API 已确认 `PUBLIC`）
- **默认分支**：`main`
- **Description / Topics**：已设置公开简介与 `ai-engineering`、`ai-agents`、`agentic-ai`、`llm`、`knowledge-base`、`obsidian`、`evaluation`、`chinese` topics。
- **许可证**：Markdown 知识内容与文档采用 `CC-BY-4.0`；`_tools/` 源代码采用 `MIT`；范围见 [LICENSE-NOTICE](LICENSE-NOTICE)。
- **本地 repo 根目录**：`.`（即本文件所在的 `AI-Engineering-KnowledgeBase/` 目录）
- **初始内容 baseline commit**：`9284315`
- **GitHub push 验证 commit**：`61432d5`
- **稳定基线 tag**：`phase1-baseline`（指向 repo 协作护栏完成后的稳定提交；精确 SHA 以 `git rev-parse phase1-baseline` 为准）

## 当前策略

- **repo 根目录**：`.`（即本文件所在的 `AI-Engineering-KnowledgeBase/` 目录）
- **组织策略**：不重排正文书籍、不改中文文件名；公共导航页使用标准相对 Markdown 链接，正文保留 Wiki-link。
- **治理文件策略**：入口级治理文件保留在顶层；审计、计划、强模型 review 快照收纳到 `_governance/`。
- **远端策略**：按 public repo 标准维护；未确认的高风险操作（force-push、删除分支、改写历史）不做。
- **CI 策略**：push / pull request 到 `main` 时运行 `.github/workflows/kb-health-check.yml`，执行 `python3 _tools/kb_health_check.py`。

## v1.0 发布候选状态（2026-07-10）

- **内容架构**：已通过 [M6–M8 立项与 v1.0 收束审计](_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md)，无 Phase 1 / v1.0 内容阻塞项。
- **已知非阻塞边界**：Laws 剩余 61 条按季度风险排序核验；M6/M7 条件性合并立项；M8 只做 dated snapshot。公共入口采用双兼容链接，不维护第二套正文镜像。
- **发布动作**：尚未创建 `v1.0` tag 或 GitHub Release；需在最终 CI 成功后单独决定。

## 为什么不先大搬家

这套库已经有大量 Obsidian wikilink、ADS ↔ Case Library heading 级交叉引用、Laws heading 引用与体检脚本。首次 repo 化如果同时做目录重组，会把两个风险叠在一起：

1. GitHub 上传风险：是否误传临时文件、私人路径、密钥、未脱敏日志或不适合公开的第三方内容；
2. Obsidian 结构风险：链接是否断、歧义是否新增、治理文件是否失去上下文。

因此推荐顺序是：

1. 先提交当前结构作为 baseline；
2. 增加 repo 协作护栏与自动体检；
3. 验证体检通过；
4. 治理审计快照单独收纳到 `_governance/`，不和正文目录重组混在一起。

## 应进入 repo 的文件类型

| 类型 | 处理 | 说明 |
|---|---|---|
| 十五本书正文 | 纳入 | 知识库主体 |
| Case Library / ADS | 纳入 | 应用层与机器层 |
| 顶层入口治理文件 | 纳入 | README、维护手册、编辑审计、协作规则等入口 |
| `_governance/` | 纳入 | 架构审计、Laws 审计、ADS/Case 审计、FABLE5 快照与搬迁计划 |
| `_tools/*.py` | 纳入 | 体检、编译、批量链接维护工具 |
| `_tools/validation_*.log` | 2026-10-07 起不再入库 | Phase 1 期间的 65 个日志已从工作树移除，可在 `git show 8a47fb0:_tools/<文件名>` 取回；新的验证证据写进 PR 描述的"验证命令 / 返回结果 / 证据路径" |
| `.github/workflows/*.yml` | 纳入 | GitHub Actions 自动体检 |
| `.github/pull_request_template.md` | 纳入 | PR 自检模板 |
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
- remote 明确指向当前 public repo，且待提交内容适合公开。

## 后续上传

repo 和 `origin` 已存在，不需要重复创建。push 前先运行本页检查清单并取得明确授权；不要把整个 Obsidian Vault 作为 remote 根目录。

## 当前维护入口

- [总入口](README.md)
- [维护手册](MAINTENANCE.md)
- [编辑审计](01_编辑审计.md)
- [使用路径与任务路由](03_使用路径与任务路由.md)
- [治理文件地图](GOVERNANCE_INDEX.md)
- [Governance Reorg Plan](_governance/GOVERNANCE_REORG_PLAN.md)
- [Agent 工作规则](AGENTS.md)
- [Contributing](CONTRIBUTING.md)

## Repo 优化批次状态

- [x] **Batch 1：Repo 安全护栏** — 已加入 GitHub Actions、PR template、[Contributing](CONTRIBUTING.md)。
- [x] **Batch 2：治理文件可发现性** — 已加入 [治理文件地图](GOVERNANCE_INDEX.md)。
- [x] **Batch 2B：治理文件收纳** — 审计/计划/强模型快照已移动到 `_governance/`，正文目录未移动。
- [x] **Batch 3：Repo 基线管理** — 已设置 `phase1-baseline` tag；tag 指向以实际 Git 结果为准。
- [x] **Batch 4：GitHub / Obsidian 双兼容阅读入口** — README 已重构为公开书架；总图、学习路径、使用路径、公开协作入口、16 个书目/案例 INDEX 与 ADS Protocol 的文件级入口改用标准相对 Markdown 链接；heading 级知识引用继续使用 Wiki-link，不维护第二套镜像。体检已增加公共入口与书目索引的双兼容链接检查。
