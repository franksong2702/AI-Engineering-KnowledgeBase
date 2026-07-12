---
type: book-expansion-priority-audit
status: read-only-review
date: 2026-07-10
abstraction_layer: 图谱层（内容扩写审计）
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, 内容审计, 扩写优先级, 主编审查]
---

# 十五本书扩写优先级深度审计

> 本文回答一个单一问题：**当前十五本书里，哪些真的需要扩写，先扩哪一本，新增什么才有价值？**
>
> 这是只读审查，不改正文，也不自动成为活任务队列。若后续授权实施，执行项必须登记到 [编辑审计](../../01_编辑审计.md) 的待办清单。

> [!success] P1-A Batch A 执行状态（2026-07-10）
> 用户已授权先做教材第 2/5/7 章试点。三个独立实验包已经落地：[Python 文件整理器](../../textbook-zero-to-agent/labs/02_Python文件整理器实验包.md)、[API 批处理流水线](../../textbook-zero-to-agent/labs/05_API批处理流水线实验包.md)、[裸写文件 Agent](../../textbook-zero-to-agent/labs/07_裸写文件Agent实验包.md)。本审计其余 P1/P2 仍是建议，不因本批自动开工。

> [!success] P1-A Batch B 执行状态（2026-07-12）
> 用户暂时无法安排真实学习者试读，但授权继续工作。保留教学有效性未实证的边界后，第 9/10/12 章三个实验包已经落地：[版本对比评测门禁](../../textbook-zero-to-agent/labs/09_版本对比评测门禁实验包.md)、[安全发布与运行证据](../../textbook-zero-to-agent/labs/10_安全发布与运行证据实验包.md)、[毕业项目交付与评审](../../textbook-zero-to-agent/labs/12_毕业项目交付与评审实验包.md)。六套参考实现均已从 Markdown 抽取并实际运行；P1-A 内容实施收束，但“真实零基础读者独立完成”仍是后验验证项。P1-B 及以后仍需独立立项，不因本批自动开工。

> [!success] P1-B 执行状态（2026-07-12）
> [Evaluation 端到端评价工程样板](../../evaluation-of-ai-systems/08_端到端评价工程样板.md)已落地，复用教材研究助理 Agent，串联评价规格、开发/冻结分集、规则/Judge/人工分工、Judge 校准、重复运行、发布门禁、生产回流和元评价。样例证据包与审计器已实际运行；原七个理论 Part 不改编号、不重复扩写。

> [!success] P1-C 执行状态（2026-07-12）
> [Agent Bible P1-C Scope Audit](AGENT_BIBLE_P1C_SCOPE_AUDIT.md)先完成只读裁决，随后四个 Batch 已按顺序实施：从“深化五个角色”改为“五个能力契约样板”，保留 21 个角色卡目录；新增[共享 schema 与 contracts 层](../../agent-bible/contracts/00_INDEX.md)、50 个契约测试用例定义、5 条终态 trace 样例、Markdown → machine JSON 编译和语义检查。当前未连接真实模型运行时，不把 fixture 校验表述成行为测试通过。未新增 ADS 编号，未全量扩写其余十六个角色。

## 一、先给结论

### 1.1 总判断

**这套知识库不存在“十五本书普遍太薄，需要统一加厚”的问题。**

真正值得扩写的缺口集中在三种地方：

1. **教学入口缺少足够的可执行脚手架**：概念和项目题目都有，但零基础读者还不能只靠书本完成环境搭建、代码实现、故障排查和项目验收。
2. **全库最重要的评价理论缺少一个完整的工程闭环样板**：知道“评什么”和“有哪些评价模式”，还不等于能从零建出评测集、评分器、门禁和持续监控。
3. **角色 Agent 的规格声称可直接投入使用，但生产契约仍偏薄**：有 System Prompt，却缺输入输出 schema、权限、停止/升级条件、测试集和完整 trace。

因此，本轮扩写优先级是：

1. **P1-A：[《从零到 AI Agent 专家》](../../textbook-zero-to-agent/00_INDEX.md)**——扩写教学执行层，不扩写重复理论。
2. **P1-B：[《The Evaluation of AI Systems》](../../evaluation-of-ai-systems/00_INDEX.md)**——增加一个端到端评价工程样板。
3. **P1-C：[《Agent 圣经》](../../agent-bible/00_INDEX.md)**——只深化少数高频 Agent，并先解决“角色封装”与“拟人化分工”的边界。
4. **P2-A：[《AI Systems in Production》](../../ai-systems-in-production/00_INDEX.md)**——补运行手册与模板，不继续加原则性散文。
5. **P2-B：[《The Data Foundation of AI Systems》](../../data-foundation-of-ai-systems/00_INDEX.md)**——补一个完整数据生命周期样板。
6. **P2-C（条件性）：[《Model Adaptation》](../../model-adaptation/00_INDEX.md)**——只有出现真实定制项目时再补决策记录和训练/评价工件。

其余九本当前**不应进入正文扩写队列**。它们有的已经足够完整，有的是刻意承担压缩层职责，还有的越扩越容易重复或过时。

### 1.2 最重要的反对意见

一个多疑的主编会问：**“你是不是又拿字数判断质量？”**

回答：不是。字符数只用于发现“定位与体量是否明显不匹配”的候选，不作为裁决标准。最终判断看五件事：

- 书对读者承诺了什么；
- 当前内容能否独立兑现承诺；
- 扩写能否补出新的能力或工件；
- 新内容是否会与其他书重复；
- 新内容能保值多久、维护成本多大。

例如 [Foundation](../../foundation-of-ai-engineering/00_INDEX.md) 只有约 2.7 万字符，但它的职责就是高密度压缩；继续扩写反而会损害它。相反，教材约 3.8 万字符并不算极短，但它承诺把完全零基础读者带到生产级 Agent，当前缺的不是更多概念，而是可执行的教学桥梁。

---

## 二、审计范围与方法

### 2.1 范围

本轮覆盖知识图谱中十五本书：

1. [从零到 AI Agent 专家](../../textbook-zero-to-agent/00_INDEX.md)
2. [Multi-Agent 架构手册](../../multi-agent-patterns-handbook/00_INDEX.md)
3. [AI 决策框架大全](../../decision-frameworks-guide/00_INDEX.md)
4. [LLM Design Patterns](../../llm-design-patterns/00_INDEX.md)
5. [Agent 圣经](../../agent-bible/00_INDEX.md)
6. [The Laws of AI Engineering](../../laws-of-ai-engineering/00_INDEX.md)
7. [Foundation of AI Engineering](../../foundation-of-ai-engineering/00_INDEX.md)
8. [The Evaluation of AI Systems](../../evaluation-of-ai-systems/00_INDEX.md)
9. [AI Engineering Anti-Patterns](../../ai-engineering-anti-patterns/00_INDEX.md)
10. [The Data Foundation of AI Systems](../../data-foundation-of-ai-systems/00_INDEX.md)
11. [Model Adaptation](../../model-adaptation/00_INDEX.md)
12. [Human-AI Collaboration Foundation](../../human-ai-collaboration-foundation/00_INDEX.md)
13. [AI Systems in Production](../../ai-systems-in-production/00_INDEX.md)
14. [Human-AI Interaction Design](../../human-ai-interaction-design/00_INDEX.md)
15. [Multimodal Systems](../../multimodal-systems/00_INDEX.md)

[The Constitution of AI Engineering](../../The-Constitution-of-AI-Engineering.md) 是压缩宪法，不按普通书籍纳入扩写排序；[Agent Decision System](../../agent-decision-system/00_PROTOCOL.md) 与 [Case Library](../../ai-engineering-case-library/00_INDEX.md) 不是书，但作为“知识是否已经有操作层/案例层落点”的反向校验使用。

### 2.2 做了什么

- 逐本核对 INDEX 的定位、承诺、边界和与其他书的分工；
- 逐章扫描结构、章节体量、项目/练习/反例/边界/验收/失败模式等构件；
- 对高优先级候选和高重叠书组做关键章节深读；
- 对教材—多 Agent、Multi-Agent—Design Patterns、Collaboration—Interaction Design 等高重叠组合做重复风险检查；
- 用 [ADS 评价清单](../../agent-decision-system/05_EVAL-CHECKLIST.md) 的三个问题复核结论：
  - Q-01：扩写服务的真实目标是什么？
  - Q-04：新增质量是否值得新增维护成本？
  - Q-05：是不是把“字符数”这个代理误当成质量？
- 用 [LAW-10 简单优先](../../agent-decision-system/04_LAW-INVARIANTS.md) 反查：删掉这项扩写会不会损害必要功能？如果不会，就不立项。

### 2.3 统一评分口径

“扩写收益分”不是书的质量分，而是**现在投入扩写的预期收益**。权重如下：

| 维度 | 权重 | 人话解释 |
|---|---:|---|
| 定位/承诺缺口 | 35% | 书现在说自己能做到的，正文是否还撑不起来？ |
| 全局杠杆 | 20% | 扩写后会不会改善多个学习路径和下游模块？ |
| 可操作工件缺口 | 25% | 缺的是能真正落地的案例、模板、代码、rubric 或协议吗？ |
| 内容保值期 | 10% | 新增内容能否跨模型和工具版本长期有效？ |
| 非重复性 | 10% | 新内容是否已有主要定义位置，扩写会不会只是复制？ |

分数差距在 5 分以内不要过度解读；它用于排队，不是假装精确测量内容价值。

---

## 三、当前体量与结构基线

> 字符数是 Python Unicode 字符计数，含 Markdown 与 frontmatter；只用于横向发现异常，不等同于字数或质量。

| 书 | 正文章节/家族文件 | 总字符 | 章节中位字符 | 当前体裁判断 |
|---|---:|---:|---:|---|
| [从零到 AI Agent 专家](../../textbook-zero-to-agent/00_INDEX.md) | 12 | 38,495 | 2,873 | 课程讲义 + 项目路线 |
| [Multi-Agent 架构手册](../../multi-agent-patterns-handbook/00_INDEX.md) | 15 | 34,769 | 1,962 | 模式卡手册 |
| [AI 决策框架大全](../../decision-frameworks-guide/00_INDEX.md) | 6 | 38,904 | 5,804 | 27 个决策框架工具箱 |
| [LLM Design Patterns](../../llm-design-patterns/00_INDEX.md) | 5 | 38,152 | 6,567 | 24 个模式工具箱 |
| [Agent 圣经](../../agent-bible/00_INDEX.md) | 5 | 28,623 | 5,637 | 21 个角色 Agent 规格 |
| [The Laws of AI Engineering](../../laws-of-ai-engineering/00_INDEX.md) | 11 | 159,109 | 9,557 | 102 条 Law + 治理层 |
| [Foundation](../../foundation-of-ai-engineering/00_INDEX.md) | 8 | 27,312 | 2,897 | 高密度原则与判断蒸馏 |
| [Evaluation](../../evaluation-of-ai-systems/00_INDEX.md) | 7 | 43,592 | 5,210 | 评价理论 + 方法框架 |
| [Anti-Patterns](../../ai-engineering-anti-patterns/00_INDEX.md) | 8 | 81,705 | 9,409 | 102 个反模式 + Top 20 |
| [Data Foundation](../../data-foundation-of-ai-systems/00_INDEX.md) | 5 | 25,807 | 4,474 | 输入侧工程手册 |
| [Model Adaptation](../../model-adaptation/00_INDEX.md) | 5 | 24,177 | 4,166 | 模型定制决策手册 |
| [Human-AI Collaboration](../../human-ai-collaboration-foundation/00_INDEX.md) | 10 | 44,042 | 3,868 | 人机协作制度设计手册 |
| [Production](../../ai-systems-in-production/00_INDEX.md) | 6 | 24,475 | 3,164 | 生产运行原则与清单 |
| [Human-AI Interaction](../../human-ai-interaction-design/00_INDEX.md) | 6 | 31,109 | 4,284 | AI 交互设计手册 |
| [Multimodal Systems](../../multimodal-systems/00_INDEX.md) | 6 | 30,220 | 4,279 | 模态扩展层 |

这张表支持两个相反结论：

1. 教材和 Production 的主题跨度明显大于单章承载量，值得检查“是否缺执行层”；
2. Laws、Anti-Patterns 已经非常大，继续扩写不是默认好事。

---

## 四、扩写优先级总表

| 排名 | 书 | 扩写收益分 | 裁决 | 最有价值的新增物 |
|---:|---|---:|---|---|
| 1 | [从零到 AI Agent 专家](../../textbook-zero-to-agent/00_INDEX.md) | 94 | **P1-A，优先扩写** | 实验手册、可运行脚手架、故障排查、项目 rubric |
| 2 | [Evaluation](../../evaluation-of-ai-systems/00_INDEX.md) | 88 | **P1-B，优先扩写** | 一个端到端评价工程样板 |
| 3 | [Agent 圣经](../../agent-bible/00_INDEX.md) | 82 | **P1-C，选择性深化** | 5 个生产级 Agent 契约与 trace |
| 4 | [Production](../../ai-systems-in-production/00_INDEX.md) | 76 | **P2-A，补工件** | SLO、trace schema、发布门禁、事故 runbook |
| 5 | [Data Foundation](../../data-foundation-of-ai-systems/00_INDEX.md) | 66 | **P2-B，补样板** | 一个完整数据生命周期案例与 manifest |
| 6 | [Model Adaptation](../../model-adaptation/00_INDEX.md) | 58 | **P2-C，条件性** | 真实项目触发后的训练/评价/退役记录 |
| 7 | [Multi-Agent 手册](../../multi-agent-patterns-handbook/00_INDEX.md) | 50 | 不做全书扩写 | 最多补 2–3 个可复现对照实验 |
| 8 | [Human-AI Interaction](../../human-ai-interaction-design/00_INDEX.md) | 48 | 不扩正文 | 若优化，补界面示意图和交互走查，不补散文 |
| 9 | [Multimodal Systems](../../multimodal-systems/00_INDEX.md) | 47 | 条件性维护 | 真实模态项目暴露缺口后补证据包 |
| 10 | [LLM Design Patterns](../../llm-design-patterns/00_INDEX.md) | 45 | 不扩写 | 按季度更新/退役方法，不继续堆模式 |
| 11 | [Foundation](../../foundation-of-ai-engineering/00_INDEX.md) | 42 | **禁止惯性扩写** | 保持压缩密度，只修边界或事实 |
| 12 | [Laws](../../laws-of-ai-engineering/00_INDEX.md) | 41 | **禁止内容加厚** | 做证据核验和收窄，不增加“Law 数量” |
| 13 | [Human-AI Collaboration](../../human-ai-collaboration-foundation/00_INDEX.md) | 40 | 不扩写 | 现有十章已形成完整制度闭环 |
| 14 | [AI 决策框架大全](../../decision-frameworks-guide/00_INDEX.md) | 38 | 不扩写 | 更多应用应进入案例库，不复制框架说明 |
| 15 | [Anti-Patterns](../../ai-engineering-anti-patterns/00_INDEX.md) | 36 | **禁止全量深化** | 深度失败叙事继续放 Case Library |

再次强调：低分不代表书差。例如 Foundation 和 Laws 是全库最高价值资产之一；它们分低，是因为**继续加内容的边际价值低、稀释风险高**。

---

## 五、P1：三项最值得做的扩写

## 5.1 P1-A《从零到 AI Agent 专家》：扩“怎么学会”，不要扩“还要知道什么”

### 当前优点

- 十二章路线合理，从认知、Python、Prompt、API、RAG、Agent、评测一路到生产与毕业设计；
- 每章都有学习目标、练习、项目、错误清单、推荐 Prompt 和自测题；
- [第 7 章](../../textbook-zero-to-agent/07_工具调用与第一个Agent.md) 的“裸写 Agent 循环”和 [第 9 章](../../textbook-zero-to-agent/09_评测与可靠性工程.md) 的“先建评测再优化”方向正确；
- 项目递进关系已经存在，不需要重排十二章。

### 真正的问题

这本书当前更像**一套优秀的课程大纲和讲义**，还不是一套零基础学习者可以独立完成的课程。

最明显的承诺缺口：

- [第 2 章 Python](../../textbook-zero-to-agent/02_Python与开发环境速成.md) 用约 2,500 字承载 3–4 周学习目标，却没有可运行示例、环境自检、常见报错对照和参考答案；
- [第 5 章 API](../../textbook-zero-to-agent/05_API编程与结构化输出.md) 要求重试、流式、断点续跑和成本统计，但没有一套完整参考实现；
- [第 7 章 Agent](../../textbook-zero-to-agent/07_工具调用与第一个Agent.md) 要求裸写约 200 行文件 Agent，却没有 starter、最终版本、测试任务和 trace 样例；
- [第 9 章 Evaluation](../../textbook-zero-to-agent/09_评测与可靠性工程.md) 要求搭评测体系，但缺评测数据格式、评分脚本和版本对比报告样板；
- [第 10 章生产](../../textbook-zero-to-agent/10_安全与生产部署.md) 要求部署、红队与监控，却没有部署清单、攻击用例格式和运行证据样板；
- [第 12 章毕业设计](../../textbook-zero-to-agent/12_专家之路.md) 有高标准，但没有阶段里程碑、评分 rubric 和不合格样例。

### 应该怎么扩

不是把每章“知识点”从 8 条改成 20 条，而是给关键章补统一的**实验包**：

1. `开始前自检`：环境、先修知识、预计时间；
2. `Starter`：最小可运行骨架；
3. `逐步任务`：每一步都有可机械判定的完成标准；
4. `预期产物`：目录结构、示例输出、trace 或报告；
5. `常见失败`：报错现象 → 原因 → 排查顺序；
6. `验收 rubric`：合格、良好、优秀分别是什么；
7. `参考实现/答案`：与题目分离，允许先做后对照；
8. `向深书跳转`：概念深度交给主要定义该概念的书，不在教材重复讲一遍。

### 推荐批次

- **先做试点**：第 2、5、7 章——它们决定零基础读者能否跨过“会看”到“会做”；
- 试点格式成立后，再做第 9、10、12 章；
- 其余章节先不加厚。

### 停手条件

一个没有现成项目代码的零基础读者，能够只按章节说明完成项目；遇到常见失败能按文档定位；第三方按 rubric 能独立判断是否合格。达成后停止，不以字数为目标。

## 5.2 P1-B《The Evaluation of AI Systems》：补一条从理论到运行的完整链

### 当前优点

这是全库理论质量最高的模块之一：

- 对能力、可靠性、价值和自主性的区分清楚；
- 单 Agent、多 Agent、自我评价、人类评价的覆盖完整；
- [Part 6](../../evaluation-of-ai-systems/06_评价设计模式.md) 已讲 Benchmark、HITL、Judge、对抗测试、红队、持续评价和回归测试；
- 与 Laws、Production、Human-AI Collaboration 的口径已经调和。

### 真正的问题

读完后，读者知道“该评什么、有哪些方法”，但仍可能不知道如何把它们组装成一个真实评价系统。当前缺少的是**一份从需求到发布决定的完整工程证据链**，不是更多评价定义。

### 应该怎么扩

增加一个新的实践 Part 或附录，例如“端到端评价工程样板”，只用一个贯穿案例演示：

1. 写评价规格：真实目标、风险、任务分布、判定门；
2. 建数据集：典型/边界/对抗、训练调优集/冻结验证集；
3. 选择评分器：代码规则、Judge、人审分别负责什么；
4. 校准 Judge：人工金标、一致率、偏差测试；
5. 处理非确定性：重复运行、通过率与置信区间；
6. 设发布门禁：提升、回归、成本、延迟如何共同裁决；
7. 接生产监控：代理信号、漂移、真实失败回流；
8. 做元评价：这套评价有没有开始被优化、污染或过时。

最好直接复用教材研究 Agent 或 Case Library 的一个深度案例，让 Evaluation、Textbook、Production 三层连成一条链。

### 停手条件

读者能拿样板替换自己的任务字段，产出一份可运行的评价规格、数据集 schema、评分器组合和发布决定记录；不需要再新增长篇理论章节。

## 5.3 P1-C《Agent 圣经》：先纠正产品承诺，再深化五个 Agent

### 当前优点

- 21 个 Agent 都有职责、输入、输出、System Prompt、Memory、工具、评价、失败模式和最佳实践；
- INDEX 已明确“Agent 是能力封装，不是人的复刻”；
- System Prompt 的方向大体正确，尤其研究员、架构师、事实核查和质量审查角色。

### 真正的问题

每个 Agent 正文通常只有约 1,000–1,250 字。作为“角色卡”足够，作为 INDEX 所说的“可直接复制、配上 Memory 和工具就能进生产”还不够：

- 输入/输出只是自然语言描述，没有 schema；
- 工具列出名称，没有权限、失败返回和不可用时的降级；
- Memory 只有三层方向，没有写入、更新、冲突和遗忘协议；
- 没有停止条件、升级人工条件、预算和重复失败处理；
- 评价标准没有配测试集与反例；
- 没有完整执行 trace，读者看不到规格如何真的约束行为。

还有一个架构风险：虽然 INDEX 已反对拟人化，但 21 个条目仍以 CEO、CTO、PM 等人类职位组织。若无脑把 21 个都加厚，会和 [Anti-Patterns 的拟人化分工警告](../../ai-engineering-anti-patterns/01_Agent架构反模式.md)形成新的张力。

### 应该怎么扩

不要全量扩写。先选五个与本知识库维护和 AI 工程交付最相关的能力型 Agent：

1. 研究员；
2. 事实核查员；
3. 架构师；
4. 调试专家；
5. 通用评审。

每个增加：

- 程序可以检查的输入/输出规则；
- 工具与权限矩阵；
- 状态/记忆 schema；
- 停止、阻塞、升级与失败协议；
- 5 个正常用例 + 5 个反例/对抗用例；
- 一个完整 trace；
- 与 [ADS](../../agent-decision-system/00_PROTOCOL.md) 的 LAW/PAT/ANTI/Q 对照；
- “何时根本不该用这个角色 Agent”。

### 停手条件

五个 Agent 能用同一套 contract 结构比较，测试用例可复跑，且每个角色的存在理由能由工具/上下文/权限差异说明，而不是仅靠职位名称说明。

---

## 六、P2：有价值，但不要先于 P1

## 6.1 P2-A《AI Systems in Production》：加运维工件，不加更多口号

### 当前判断

六个 Part 的内容密度高，已经覆盖生产分级、延迟、背压、可观测性、发布、成本、降级和事故复盘。它不是“写得不好”，也不需要把每章扩成基础设施百科。

缺口在于读者还没有一套可以直接拿走的生产工件：

- L1/L2/L3 生产就绪评审表；
- SLO/SLI 定义模板；
- 最小 trace schema 示例；
- 六类变更的发布门禁与回滚矩阵；
- 单任务成本模型；
- 错误输出型事故 runbook；
- 一次从报警、止血、圈定影响面到回灌评测集的完整事故记录。

建议用“附录/运行手册”承载，不稀释六章主线。

## 6.2 P2-B《Data Foundation》：加一个贯穿全生命周期的数据产品案例

### 当前判断

初版“纲要过薄”的问题已经在 v1.0 扩写中解决。五章现在都有工程手册、边界和验收清单，继续逐章加定义的收益已经不高。

剩余高价值缺口是：没有一个数据集从来源进入、过合同/schema、生成 manifest、做质量报告、版本化、漂移告警、触发修复、最后影响下游模型的完整案例。

建议只加一个贯穿案例和对应模板：

- 数据合同；
- manifest；
- 六维质量报告；
- 训练/评测隔离与近重复检查记录；
- 漂移响应记录；
- 数据事故复盘。

## 6.3 P2-C《Model Adaptation》：真实项目触发后再补

### 当前判断

这本书当前最有价值的是克制：先走 prompt/RAG/工具，定制是最后手段；五章已经覆盖微调、对齐、蒸馏、自部署和评价风险。它不是当前公共读者的首要缺口，而且具体训练配方过时很快。

只有出现真实的微调、蒸馏或自部署项目时，才值得新增：

- “为什么不使用更简单方案”的立项记录；
- 数据—模型—评测三者版本互链的 manifest；
- 基座 + 最优 prompt 的对照；
- 目标/通用/安全三件套评测；
- 成本 TCO；
- 半年重新立项与退役记录。

不要新增“当前主流模型/框架/参数配方大全”；那会把慢变量知识库拖成快速过时的工具快照。

---

## 七、九本不应进入正文扩写队列的书

| 书 | 为什么现在不扩 | 如果未来要改善，做什么 |
|---|---|---|
| [Multi-Agent 手册](../../multi-agent-patterns-handbook/00_INDEX.md) | 15 个模式均有十问结构，模式卡作为查阅材料已经够用；与 LLM Design Patterns 重叠高 | 最多给 2–3 个高频模式做“单 Agent 基线 vs 多 Agent”可复现实验，不全量加代码 |
| [Human-AI Interaction](../../human-ai-interaction-design/00_INDEX.md) | 六章已有原则、模式、工程手册、失败、评价、验收；文字层完整 | 补审批界面、置信呈现、撤销/拒答等示意图和走查，不再加同义散文 |
| [Multimodal Systems](../../multimodal-systems/00_INDEX.md) | 立项边界明确：它是模态扩展层，不是 CV/ASR/机器人教材；六章结构闭合 | 真实项目暴露新的感知/取证缺口后补证据包，不能为“更全”变成模型能力综述 |
| [LLM Design Patterns](../../llm-design-patterns/00_INDEX.md) | 24 个模式已覆盖方法层；与 Multi-Agent 有明确的定义分工；方法会随模型能力重洗 | 按季度更新、合并或退役，不继续堆新模式和产品教程 |
| [Foundation](../../foundation-of-ai-engineering/00_INDEX.md) | 它的价值来自压缩密度、判断和原创综合，不来自篇幅 | 只在外部证据推翻、边界改变或下游误读时修订 |
| [Laws](../../laws-of-ai-engineering/00_INDEX.md) | 102 条已经足够多；当前工作方向应是 lawhood、证据和边界，不是加字数或加 Law | 继续风险排序核验剩余引用；必要时收窄、合并解释，不增加权威感填充 |
| [Human-AI Collaboration](../../human-ai-collaboration-foundation/00_INDEX.md) | 十章都已按统一八段结构扩写，制度层闭环完整；与 Interaction Design 边界清晰 | 只在真实组织案例暴露制度缺口时补案例或校准指标 |
| [AI 决策框架大全](../../decision-frameworks-guide/00_INDEX.md) | 27 个框架的九问结构完整；继续加案例会迅速重复 Case Library | 新应用进入案例库，并从案例回链框架；不在框架正文堆行业案例 |
| [Anti-Patterns](../../ai-engineering-anti-patterns/00_INDEX.md) | 102 个反模式已形成完整负空间；全量深化会制造 102 篇重复长文 | 失败反转和工程细节继续进入 Case Library 的深度样板层 |

---

## 八、全局架构冲击审查

扩写不能只看单书。按当前知识图谱，新增内容必须守住以下边界：

### 8.1 教材只负责教学封装，不能重新定义核心内容

教材新增的概念解释必须回链到 Laws、Evaluation、Patterns、Production 等主要定义位置；教材真正独有的资产是学习顺序、实验、项目和 rubric。若把其他书的理论整段复制进教材，会产生重复定义和维护分叉。

### 8.2 Evaluation 的新增章必须成为下游接口，不是第八套术语

评价样板应被教材项目、Production 发布门禁、Data/Model 评测和 ADS Q 清单共同复用。它要输出工件，而不是再发明一组编号。

### 8.3 Agent Bible 不能变成第二套 ADS

Agent Bible 定义角色级规格，ADS 定义跨角色的决策纪律。深化 Agent 时引用 ADS，不复制或新建 LAW/PAT/ANTI/Q 编号。

### 8.4 Production/Data/Model 的新增内容应优先是模板和案例

三本的原则层已经够用。继续写原则会与 Laws/Foundation/Evaluation 重叠；新增价值应是可复用工件、完整案例和失败记录。

### 8.5 不为统一格式洗平体裁差异

教材需要教学脚手架，Laws 需要严谨边界，Foundation 需要压缩，手册需要查阅效率，案例需要失败反转。扩写不能把十五本书全部改成“原则—模式—清单”的同一种模型腔。

---

## 九、若后续实施，推荐顺序

### Batch A：教材实验包试点

- 第 2、5、7 章；
- 只建立统一实验包格式；
- 试点经真实学习者或独立 Agent 按文档完成后，再扩到第 9、10、12 章。

状态：第 2/5/7 章于 2026-07-10 完成；第 9/10/12 章在 2026-07-12 经独立 Agent 技术复核后完成。真实学习者试读因暂无时间未执行，不得把技术验证表述成教学效果验证。

### Batch B：Evaluation 端到端样板

- 用教材研究 Agent 或一个深度 Case 做贯穿案例；
- 产出评价规格、数据 schema、评分器、校准、门禁和持续监控记录。

状态：✅ 已完成（2026-07-12），见 [实践附录](../../evaluation-of-ai-systems/08_端到端评价工程样板.md)。

### Batch C：Agent Bible 五个生产级样板

- 先写“能力封装而非职位模仿”的边界；
- 深化研究员、事实核查员、架构师、调试专家、通用评审；
- 与 ADS 对齐，不新增编号空间。

状态：✅ 已完成（2026-07-12）。实施架构按后续 [P1-C 立项审计](AGENT_BIBLE_P1C_SCOPE_AUDIT.md)收窄为五个能力契约，不部署拟人化五 Agent 组织。

### Batch D：Production 运行手册附录

- SLO、trace、发布矩阵、成本模型、事故 runbook；
- 不改六章理论骨架。

### Batch E：Data 样板；Model 条件性等待

- Data 做一个完整生命周期样板；
- Model 不预写，等真实项目触发。

每个 Batch 单独审查、单独提交；不要把五本书同时展开成一个大改写。

---

## 十、最终裁决

如果现在只能投资一轮内容工作，选择**教材实验包**，因为它直接修复“读者看懂但做不出来”的入口断层，并能把其余专题书的价值真正编译给学习者。

如果只能投资一项全库基础设施内容，选择**Evaluation 端到端样板**，因为它把“用不可靠部件造可靠系统”的根命题变成可运行的反馈闭环。

如果只能修一个名实不符的位置，选择**Agent Bible 的五个生产级样板**，因为当前角色卡可用作 prompt 起点，但还不应被称为生产级规格。

**不建议做的事**：按字符数从薄到厚灌水、十五本统一扩写、给 Laws/Anti-Patterns 继续加条目、在教材复制所有深书、给快变方法补大量厂商教程。

这轮审计的总原则是：

> **扩写不是让书变厚，而是让它兑现原本承诺。没有新增能力、工件或可验证教学结果的文字，不叫扩写，叫填充。**
