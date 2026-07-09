---
type: knowledge-base-shelf
abstraction_layer: 图谱层（导航入口）
date: 2026-07-06
course: ai-engineering-knowledge-base
tags: [AI工程, 书架, 导航, 总入口]
---

# AI Engineering Knowledge Base · 总入口

> 十四本书（核心九本 + 补充五本）+ 案例库 + 决策系统 + 一套知识图谱，169 个文件，一个统一的理论体系。
> 本页是**无歧义导航**——所有链接用完整路径，点击直达（解决了各书 INDEX 同名的问题）。

> [!important] Law System 口径
> [[laws-of-ai-engineering/00_INDEX|The Laws of AI Engineering]] 现在按 **Law System** 使用：它是全库的约束库，不是 102 条同等硬度的口号合集。入口层优先引用 [[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]]；A/B 级 Law 只在相关 family 或具体场景中引用。注意三套编号不能混用：`Law 1–102` 属于 Laws，Constitution 内部 `Law 1–10` 是压缩编号，Agent Decision System 的 `LAW-01–LAW-13` 是运行时操作编号。

## 文件地图：哪些是正文，哪些是治理文件

如果你只是读这套知识库，从本页、[[00_Knowledge-Graph-总图|总图]]、[[02_学习路径与未来扩展|学习路径]]、[[03_使用路径与任务路由|使用路径与任务路由]]、十四本书、案例库和 [[agent-decision-system/00_PROTOCOL|Agent Decision System]] 开始即可。

如果你是维护者，先看：

- [[MAINTENANCE|维护手册]]：改动规则、必跑命令、工具清单、命名规范。
- [[01_编辑审计|编辑审计]]：唯一活任务队列；做下一批前先看这里。
- [[GOVERNANCE_INDEX|治理文件地图]]：解释顶层审计、计划、FABLE5 快照各自是什么，避免误开任务队列。
- [[AGENTS|Agent 工作规则]]、[[CONTRIBUTING|Contributing]] 与 [[REPO_STATUS|Repo 状态]]：private GitHub repo 化后的 Agent 边界、协作流程、上传前检查与远端操作边界。
- `_tools/`：体检、编译、Law 引用升级与候选审计脚本。

以下是治理依据或审阅快照，不是普通读者必须阅读的正文，也不另立活任务队列：

- [[ARCHITECTURE_REVIEW|Architecture Review]]：全局架构判断依据。
- [[LAWS_TAXONOMY_REVIEW|Laws Taxonomy Review]] 与 [[LAWS_REWRITE_GRAND_PLAN|Laws Rewrite Grand Plan]]：Laws 升级为 Law System 的历史依据。
- [[LAW_REFERENCE_AUDIT|Law Reference Audit]]、[[LAW_REFERENCE_SYSTEM_CLOSURE|Law Reference Closure]]、[[LAW_REFERENCE_REMAINING_CANDIDATES|Remaining Candidates]]：Law 引用系统的审计与收束记录。
- [[ADS_LAW_SOURCE_MAP_AUDIT|ADS Law Source Map Audit]]：ADS `LAW-01`–`LAW-13` 与 Laws / Foundation 来源关系的只读审计。
- `FABLE5_总审报告.md`、`FABLE5_架构收束REVIEW.md`：外部强模型审阅快照；可作为依据，但执行口径仍以 [[01_编辑审计|编辑审计]] 和 [[MAINTENANCE|维护手册]] 为准。

## 只有 20 页时间？先读这一部

- [[The-Constitution-of-AI-Engineering|📜 《The Constitution of AI Engineering》—— 全库极限压缩]] — 60 条骨架（10 定律 · 10 原则 · 10 模式 · 10 反模式 · 10 评价问题 · 10 能力），每条含"为什么重要/违反会怎样/如何应用/如何判断做对"。读完这一部，就拥有整个体系的骨架。**自包含，可独立阅读。**

## 你是 AI Agent？直接调用这个决策系统

- [[agent-decision-system/00_PROTOCOL|🤖 Agent Decision System —— 机器可调用的操作层]] — 把全库转成推理时可查询的决策系统（原书不变）。含：调用协议 + 情境路由器（输入处境→输出6字段决策）+ 20张模式卡 + 12个反模式检测器 + 13条定律约束 + 10问评价清单。面向未来 AI Agent，也可人读。
  - 核心入口：[[agent-decision-system/01_SITUATION-ROUTER|情境路由器（20 个处境→决策）]]

## 先读这里：知识图谱

如果你想先理解整个体系的骨架，从这三篇开始：

- [[00_Knowledge-Graph-总图|📐 总图：统一理论框架与知识地图]] — 十四本书如何从一个根命题派生
- [[01_编辑审计|🔍 编辑审计：重复/矛盾/缺失/层级问题]] — 这套库诚实的自我审视
- [[02_学习路径与未来扩展|🧭 学习路径与未来扩展]] — 长期怎么读、往哪长
- [[03_使用路径与任务路由|🧭 使用路径与任务路由]] — 有具体目标/问题/系统时，从 ADS、案例库还是书籍进入

## 核心九本（按抽象层排列，越上越保值）

### 元规律 / 原则层（最保值，先建地基）

- [[foundation-of-ai-engineering/00_INDEX|① The Foundation of AI Engineering]] — 隐性知识蒸馏，7 章
  *判断力、稀缺性转移、必须掌握的能力、值得记忆的原则*
- [[laws-of-ai-engineering/00_INDEX|② The Laws of AI Engineering]] — Law System，102 条
  *全库约束库：少数 [[laws-of-ai-engineering/00_CORE-LAWS|Core Laws]] 可作全局正典引用，其余按 family/contextual 边界使用*

### 判断层（闭环）

- [[evaluation-of-ai-systems/00_INDEX|③ The Evaluation of AI Systems]] — 评价理论，7 部
  *如何判断一个 AI/Agent/多体系统是否优秀*

### 方法层（可复用做法，会随能力重洗）

- [[llm-design-patterns/00_INDEX|④ LLM Design Patterns]] — 推理与推断模式，24 个
  *CoT/ReAct/RAG/反思/裁判/编排…*
- [[multi-agent-patterns-handbook/00_INDEX|⑤ Multi-Agent 架构手册]] — 多体协调模式，15 个
  *Pipeline/Planner-Executor/委员会/投票/红蓝对抗…*
- [[decision-frameworks-guide/00_INDEX|⑥ AI 决策框架大全]] — 决策工具箱，27 个
  *第一性原理/可逆性/期望值/古德哈特/OODA…*
- [[agent-bible/00_INDEX|⑦ Agent 圣经]] — Agent 角色落地，21 个
  *研究员/CEO/架构师/评审/调试/教师…（含可复制的 System Prompt）*

### 避坑层（方法的镜像）

- [[ai-engineering-anti-patterns/00_INDEX|⑧ AI Engineering Anti-Patterns]] — 反模式，102 个
  *过度Agent化/多Agent泛滥/记忆倾倒/无目的反思/刷分…*

### 入口层（教学封装）

- [[textbook-zero-to-agent/00_INDEX|⑨ 从零到 Agent 专家]] — 入门教材，12 章
  *零基础到 Agent 专家的完整路径*

## 补充书（填补审计发现的缺失领域）

- [[data-foundation-of-ai-systems/00_INDEX|⑩ The Data Foundation of AI Systems]] — 数据工程（新增，补 M1，v1.0 扩写版）
  *数据质量/管线/标注合成/数据评价与治理*
- [[model-adaptation/00_INDEX|⑪ Model Adaptation]] — 模型定制（新增，补 M2，v1.0 扩写版）
  *优化阶梯/微调/对齐RLHF-DPO/蒸馏与开源部署*
- [[human-ai-collaboration-foundation/00_INDEX|⑫ Human-AI Collaboration Foundation]] — 人机长期协作 / 横切治理层（新增，v1.0 扩写版）
  *人机分工/HITL/信任/自动化偏见/权限/责任/AI Supervisor/长期关系*
- [[ai-systems-in-production/00_INDEX|⑬ AI Systems in Production]] — 生产部署与运维（新增，补 M4，v1.0）
  *Demo到生产/Serving与延迟/可观测性/发布与变更/成本工程/故障与降级*
- [[human-ai-interaction-design/00_INDEX|⑭ Human-AI Interaction Design]] — 人机交互界面设计（新增，补 M5，v1.0）
  *交互第一性/不确定性呈现/过程与控制/输入塑造/协作制度界面化/交互暗模式*

## 应用层与机器层

- [[ai-engineering-case-library/00_INDEX|📚 AI Engineering Case Library]] — 100 个真实系统设计案例，演示如何调用整个知识体系解决真实问题。
- [[agent-decision-system/00_PROTOCOL|🤖 Agent Decision System]] — 机器可调用的决策系统（见上方"你是 AI Agent？"）。

## 三条长期学习路径（详见[[02_学习路径与未来扩展|学习路径]]；有具体任务先看[[03_使用路径与任务路由|使用路径]]）

| 你是谁 | 主线 | 时长 |
|--------|------|------|
| 完全零基础 | ⑨教材为主线，其余按需插入深化 | 6–9 月 |
| 有经验工程师 | ①Foundation→②Laws→③Evaluation→⑧Anti-Patterns | 4–6 周 |
| 技术管理者 | ①Foundation→⑥决策框架→③Evaluation(Part1/5/7) | 1–2 周 |

## 如果只有一天

读 [[foundation-of-ai-engineering/00_INDEX|Foundation]] 七章 + [[laws-of-ai-engineering/00_INDEX|Laws]] 的"十条定律之上的定律" + [[ai-engineering-anti-patterns/08_最应避免的20个错误|Anti-Patterns 的 Top 20]]。这是整个知识库的最小可用内核。

## 一句话总纲

**这套库从一个根命题派生：用不可靠的概率部件造可靠系统，而生成廉价、验证稀缺。越靠近这个根（公理/原则）的知识越保值，越远（方法/技巧）的越易过时——按"投入与保值期成正比"分配你的学习精力。**
