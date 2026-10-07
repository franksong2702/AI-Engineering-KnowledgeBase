# AI Engineering Knowledge Base

> 一套以“**用不可靠的概率部件构造可靠系统**”为主线的中文 AI Engineering 知识库。
>
> 十五本书（核心九本 + 补充六本）+ Case Library + Agent Decision System + 知识图谱，207 个文件。主要语言：简体中文。

[![KB Health Check](https://github.com/franksong2702/AI-Engineering-KnowledgeBase/actions/workflows/kb-health-check.yml/badge.svg)](https://github.com/franksong2702/AI-Engineering-KnowledgeBase/actions/workflows/kb-health-check.yml)


## 30 秒选择入口

| 你是谁 / 你要做什么 | 建议从这里开始 |
|---|---|
| 第一次系统学习 AI Agent | [《从零到 Agent 专家》](textbook-zero-to-agent/00_INDEX.md) |
| 有工程经验，想先建立整体框架 | [Constitution](The-Constitution-of-AI-Engineering.md) → [Foundation](foundation-of-ai-engineering/00_INDEX.md) → [Laws](laws-of-ai-engineering/00_INDEX.md) |
| 只有 20 页时间 | [《The Constitution of AI Engineering》](The-Constitution-of-AI-Engineering.md) |
| 已经有具体任务或系统问题 | [使用路径与任务路由](03_使用路径与任务路由.md) |
| 想直接看真实案例 | [AI Engineering Case Library](ai-engineering-case-library/00_INDEX.md) |
| 你是 AI Agent | [Agent Decision System](agent-decision-system/00_PROTOCOL.md) |
| 想理解十五本书之间的关系 | [Knowledge Graph 总图](00_Knowledge-Graph-总图.md) |

进一步阅读：

- [长期学习路径与未来扩展](02_学习路径与未来扩展.md)
- [任务型使用路径](03_使用路径与任务路由.md)
- [全库统一理论图](00_Knowledge-Graph-总图.md)

## 核心九本

| # | 层级 | 书 | 解决的问题 |
|---:|---|---|---|
| 1 | 元规律 | [The Foundation of AI Engineering](foundation-of-ai-engineering/00_INDEX.md) | 什么知识最保值，工程判断力如何形成 |
| 2 | 约束库 | [The Laws of AI Engineering](laws-of-ai-engineering/00_INDEX.md) | AI 系统受到哪些底层约束 |
| 3 | 判断层 | [The Evaluation of AI Systems](evaluation-of-ai-systems/00_INDEX.md) | 如何判断系统是否真的优秀、可靠、可用 |
| 4 | 方法层 | [LLM Design Patterns](llm-design-patterns/00_INDEX.md) | 推理、检索、反思、裁判与编排模式 |
| 5 | 方法层 | [Multi-Agent 架构手册](multi-agent-patterns-handbook/00_INDEX.md) | 多 Agent 如何分工与协调 |
| 6 | 方法层 | [AI 决策框架大全](decision-frameworks-guide/00_INDEX.md) | 如何做取舍、分析不确定性与二阶效应 |
| 7 | 角色与运行规则层 | [Agent 圣经](agent-bible/00_INDEX.md) | 21 个角色卡；5 个高频能力另有可测试、供程序直接读取的运行规则 |
| 8 | 避坑层 | [AI Engineering Anti-Patterns](ai-engineering-anti-patterns/00_INDEX.md) | 102 个常见错误及其修复方向 |
| 9 | 教学入口 | [从零到 Agent 专家](textbook-zero-to-agent/00_INDEX.md) | 从零基础到可以设计 Agent 系统 |

## 补充六本

| # | 书 | 解决的问题 |
|---:|---|---|
| 10 | [The Data Foundation of AI Systems](data-foundation-of-ai-systems/00_INDEX.md) | 数据质量、管线、标注、漂移与治理 |
| 11 | [Model Adaptation](model-adaptation/00_INDEX.md) | Prompt / RAG 之后何时微调、对齐与蒸馏 |
| 12 | [Human-AI Collaboration Foundation](human-ai-collaboration-foundation/00_INDEX.md) | 人机分工、信任、权限、责任与长期协作 |
| 13 | [AI Systems in Production](ai-systems-in-production/00_INDEX.md) | Serving、可观测性、发布、成本与故障治理 |
| 14 | [Human-AI Interaction Design](human-ai-interaction-design/00_INDEX.md) | 如何把协作政策实现成可理解、可控制的界面 |
| 15 | [Multimodal Systems](multimodal-systems/00_INDEX.md) | 图像、语音、视频带来的感知、证据与安全问题 |

## 应用层与机器层

- [AI Engineering Case Library](ai-engineering-case-library/00_INDEX.md)：108 个典型案例，其中 20 个是深度样板。
- [Agent Decision System](agent-decision-system/00_PROTOCOL.md)：21 个情境路由、20 张模式卡、12 个反模式检测器、13 条运行时约束和 10 问评价清单。

## Law System 使用口径

> **重要：Law System 口径**——[The Laws of AI Engineering](laws-of-ai-engineering/00_INDEX.md) 是一套**约束库**，不是 102 条同等硬度的口号合集。入口层优先使用 [Core Laws](laws-of-ai-engineering/00_CORE-LAWS.md)；其他 Law 应按 family 和具体场景引用。

三套编号彼此独立：

- `Law 1–102`：Laws 的正式编号；
- Constitution `Law 1–10`：面向读者的压缩编号；
- Agent Decision System `LAW-01–LAW-13`：运行时操作编号。

外部依据集中见 [Laws 外部依据说明](laws-of-ai-engineering/00_EXTERNAL-REFERENCES.md)。并非每条 Law 都已逐条找到外部来源；读到一条 Law 时，可以先看它标注的"定律性质"判断硬度。

## 在 Obsidian 中使用

1. Clone 或下载本仓库；
2. 在 Obsidian 中把仓库目录作为 Vault 打开，或放进现有 Vault；
3. 从本 README、[学习路径](02_学习路径与未来扩展.md)或[任务路由](03_使用路径与任务路由.md)开始。

本仓库采用“双兼容”策略：

- README 和公共导航页使用标准相对 Markdown 链接，GitHub 与 Obsidian 均可点击；
- 正文保留 Obsidian Wiki-link，以维持 heading 级知识图谱和本地阅读体验；
- 不为 GitHub 网页显示而物理重排十五本书目录，也不维护第二套正文镜像。

## 维护与贡献

普通读者不需要阅读治理文件。维护者和贡献者从这里进入。

**版本状态**：内容架构已通过 [M6–M8 立项与 v1.0 收束审计](_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md)，可以进入 v1.0 发布候选；`v1.0` Git tag / GitHub Release 尚未创建。 Laws 外部核验进度：41/102 条，其余按风险排入季度候选池。

入口：

- [Contributing](CONTRIBUTING.md)
- [维护手册](MAINTENANCE.md)
- [Agent 工作规则](AGENTS.md)
- [编辑审计与唯一活任务队列](01_编辑审计.md)
- [Governance Index](GOVERNANCE_INDEX.md)
- [Repo 状态](REPO_STATUS.md)

提交改动前至少运行：

```bash
python3 _tools/kb_health_check.py
```

GitHub Actions 会在 push / pull request 时执行同一套结构体检。CI 能发现断链、歧义、元数据和 ADS ↔ Case Library 一致性问题，但不能替代内容审查。

## 许可证

- Markdown 知识内容和文档：[Creative Commons Attribution 4.0 International](LICENSE)（`CC-BY-4.0`）；
- `_tools/` 下的源代码：[MIT License](_tools/LICENSE)；
- 完整适用范围与最近许可证规则见 [LICENSE-NOTICE](LICENSE-NOTICE)。

引用或再分发知识内容时，建议注明：`AI Engineering Knowledge Base contributors`、仓库链接以及 `CC BY 4.0`。

## 一句话总纲

**生成越来越便宜，可靠验证、证据设计与工程判断仍然稀缺；AI Engineering 的任务，是把不可靠的概率能力约束成可验证、可恢复、可问责的系统。**
