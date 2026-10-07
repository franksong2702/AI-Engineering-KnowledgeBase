---
type: quarterly-reevaluation-report
abstraction_layer: 运营机制（定期重估报告）
date: 2026-10-07
course: ai-engineering-knowledge-base
quarter: 2026-Q4
status: adjudicated-and-executed
tags: [AI工程, 定期重估, 方法层]
---

# 2026-Q4 方法层季度重估

> 按 [[QUARTERLY_REEVALUATION_PROTOCOL|季度定期重估协议]] 执行的第一次季度重估。计划日期 2026-10-01，实际执行 2026-10-07（晚 6 天）。
> 本报告只给出**裁决建议**；按协议，`BOUNDARY / HISTORY_CANDIDATE / ESCALATE` 须由人或强模型确认后才算本轮完成，确认前不改正文。

## 本轮范围

- [[llm-design-patterns/00_INDEX|LLM Design Patterns]]：INDEX + 5 个家族共 24 个模式
- [[multi-agent-patterns-handbook/00_INDEX|Multi-Agent Patterns Handbook]]：INDEX + 15 个模式

每个条目回答协议的四问：推理能力强 100 倍、上下文与工具调用强 100 倍、调用成本降 100 倍时还成立吗？若不再默认成立，是补适用边界，还是进入历史区候选？

结构体检：`python3 _tools/kb_health_check.py` → exit 0，体检通过。

## 结论摘要

| 标签 | 条数 | 含义 |
|---|---:|---|
| KEEP | 27 | 仍是推荐方法，不改 |
| BOUNDARY | 15 | 仍有用，但需要补适用边界或改写理由 |
| HISTORY_CANDIDATE | 3 | 作为独立的提示技巧，可能应移入历史区 |
| ESCALATE | 3 | 影响跨书约定或书的结构，需要人裁决 |

（Step-back / Rephrase 一行拆成两个条目分别计数，因此合计比明细表行数多 1。）

**一句话结论**：两本书的骨架经得起"强 100 倍"的追问。会被冲刷的主要是**以提示技巧形式存在的推理模式**（推理模型已经把它们内化了）和**以"上下文装不下"为理由的模式**（这个理由会消失，但注意力稀释、并行、可观测性这些理由还在）。最大的缺口不在已有条目，而在**缺了 2026 年最常见的多 Agent 形态**（主 Agent 派生子 Agent、交错式计划）。

## 候选明细 · LLM Design Patterns

| 文件 | 条目 | 标签 | 证据（四问） | 建议动作 |
|---|---|---|---|---|
| 00_INDEX | 六条跨模式"定律"之 3："推理类模式的收益取决于任务是否'分布内'" | BOUNDARY | 正文论证的其实是"任务难度与模型现有能力"，不是分布；而 Law 7 已在 2026-07-10 收窄为"分布证据边界"，这里沿用的是旧口径 | 改为"取决于任务难度是否超出模型现有能力"，去掉"分布内"字样 |
| 00_INDEX | 成本/成熟度速查表 | BOUNDARY | 数字没有"经验量级"标注（违反维护手册第 4 条）；CoT 的 1-1.5× 没有计入推理模型的思考 token | 加注"经验量级"；CoT 一行注明"推理模型的思考 token 另计" |
| 01_推理模式 | 家族导语："模型的'思考'就是生成 token——不给空间就等于不让它思考" | BOUNDARY | 推理强 100 倍：推理模型有不可见或摘要化的思考过程；且写出来的推理不一定忠实（教材 3.3 已于本轮修正同一说法） | 改为"生成中间步骤能给模型更多计算步骤"，并补一句忠实性边界 |
| 01_推理模式 | 1. Chain-of-Thought | BOUNDARY | 推理强 100 倍：手写"一步步想"的提质作用基本被内化；"可审计"这一面保留，但需要附忠实性前提 | 已有"三重口径"注记；建议补"推理模型下默认不手写 CoT，需要审计时要求结构化理由 + 外部核验" |
| 01_推理模式 | 2. Self-Consistency | KEEP | 成本降 100 倍时更划算；"相关错误不能靠投票消除"是慢变量 | — |
| 01_推理模式 | 3. ReAct | BOUNDARY | 循环本身是 Agent 的定义，不会过时；但示例里用文本解析 `Thought:/Action:` 的写法，已被原生 tool use API 取代 | 保留模式；Prompt 示例注明"现代做法用 API 原生工具调用，文本解析版是历史形态" |
| 01_推理模式 | 4. Tree Search / ToT | HISTORY_CANDIDATE | 推理强 100 倍：**提示层**的 ToT（LLM 自己生成 + 自己评估）已被推理模型的内部搜索吸收，生产中很少见；**带外部验证器的搜索**（程序搜索、可执行测试）仍然有效 | 拆分：提示层 ToT 进历史区；"外部验证器 + 搜索"并入 Self-Consistency 的"未来方向"，或作为 Generate-Verify 的一节 |
| 01_推理模式 | 5. Least-to-Most | HISTORY_CANDIDATE | 推理强 100 倍：作为独立提示技巧已无必要，案例（末字母拼接等）是 2022 年的基准任务，当代模型可以直接完成；"按依赖顺序分解"的思想已由 Planner-Executor 覆盖 | 进历史区，在 Planner-Executor 的分解策略中留一句话 |
| 01_推理模式 | 6. Self-Critique / Reflexion | KEEP | 正文已写明"有客观反馈信号才有效"，这是慢变量 | 顺带核对"第 3 轮后常是布朗运动"这类修辞，补"经验量级" |
| 02_提示结构模式 | 1. Few-shot | KEEP | 能力再强，示例仍是传达"格式与口径"成本最低的方式 | — |
| 02_提示结构模式 | 2. Role / Persona | KEEP | 正文已写明"只影响风格，不影响能力上限" | — |
| 02_提示结构模式 | 3. Structured Output | KEEP | 慢变量（接口契约）。"未来方向"里的约束解码普及已成现实 | "未来方向"改为现在时 |
| 02_提示结构模式 | 4. Prompt Chaining | BOUNDARY | 推理强 100 倍时，"混合任务互相干扰"这个理由变弱；可测试、可观测、可换模型、可缓存这些工程理由不变 | "为什么存在"的首要理由从"质量"改为"可测试与可控" |
| 02_提示结构模式 | 5. Step-back / Rephrase | HISTORY_CANDIDATE（Step-back）/ KEEP（Rephrase 澄清） | Step-back 作为提示技巧已被推理模型内化；Rephrase 中"先澄清意图、必要时回问用户"处理的是**信息缺失**，不是能力不足，模型再强也成立 | 拆分：Step-back 进历史区；Rephrase 改名为"意图澄清"保留 |
| 03_知识与记忆模式 | 1. RAG | BOUNDARY | 上下文强 100 倍：已有边界讨论（长上下文吃掉"装不下才做的 RAG"）。新缺口：工具能力变强后，**Agent 自主检索**（grep、文件浏览、多轮搜索）在代码库等场景正在取代向量检索；"80% 的问题在检索环节"没有标注 | 补"Agentic search vs 向量检索"的选择边界；数字加"经验量级" |
| 03_知识与记忆模式 | 2. Memory Retrieval | KEEP | 无状态是 API 的结构性事实 | — |
| 03_知识与记忆模式 | 3. Tool Use | KEEP | Agent 的定义性特征。"未来方向"里的 MCP、computer use 已经落地 | "未来方向"改为现在时，并链到教材 8.6 |
| 03_知识与记忆模式 | 4. Context Compression | KEEP | 上下文强 100 倍时需求下降，但 context rot 和成本仍在 | — |
| 04_质量控制模式 | 1. Critic-Refine | KEEP | 慢变量：有锚才有效 | — |
| 04_质量控制模式 | 2. LLM-as-Judge | KEEP | 校准纪律是慢变量 | — |
| 04_质量控制模式 | 3. Debate | BOUNDARY | 同源辩论的收益证据不稳定；成本降 100 倍时诱惑更大，更需要"真差异化"这个前提 | "什么时候使用"补硬前提：辩手必须在模型、证据或工具上有真实差异 |
| 04_质量控制模式 | 4. Ensembling / Voting | KEEP | 独立性前提是数学事实 | — |
| 04_质量控制模式 | 5. Guardrails | KEEP | 纵深防御是慢变量 | — |
| 05_编排模式 | 1. Planner-Executor | BOUNDARY | 推理强 100 倍：静态的"先规划完再执行"在弱化，主流已转向**交错式计划**（Agent 循环内维护 todo 列表并随时更新）；"未来方向"里的交错规划已是现实 | 把交错式计划升为主形态，静态两段式作为特例 |
| 05_编排模式 | 2. Map-Reduce | BOUNDARY | 上下文强 100 倍时"装不下"的理由消失；注意力稀释、并行降延迟、单片可复现这些理由仍在 | "为什么存在"改为以并行与上下文隔离为主 |
| 05_编排模式 | 3. Routing | KEEP | 成本降 100 倍时"按价分流"的动机变弱，但按能力和权限分流仍然成立 | 可选：注明模型路由的收益随价格差缩小 |
| 05_编排模式 | 4. Orchestrator-Workers | KEEP | — | — |

## 候选明细 · Multi-Agent Patterns Handbook

| 文件 | 条目 | 标签 | 证据（四问） | 建议动作 |
|---|---|---|---|---|
| 00_INDEX | 五条跨模式"定律" | KEEP（内容）/ 命名见 ESCALATE-1 | 五条内容都是慢变量；第 5 条已标"经验量级" | — |
| 00_INDEX | 选型决策树 | KEEP | PR #3 已补"第 0 步：单 Agent / 工作流能否解决" | — |
| 01 | Pipeline | KEEP | — | — |
| 02 | MapReduce | BOUNDARY | 同 LDP Map-Reduce | 同上 |
| 03 | Tree | KEEP | 异构分解与上下文隔离不受影响 | — |
| 04 | Recursive | BOUNDARY | 上下文强 100 倍时，"摘要的摘要"这类场景大幅减少；目录树、依赖链这类结构性递归仍然成立 | 适用场景删去或降级"递归总结超长文本" |
| 05 | Planner-Executor | BOUNDARY | 同 LDP | 同上 |
| 06 | Hierarchical | KEEP | 已写明"被逼出来才用" | — |
| 07 | DynamicRouting | KEEP | — | — |
| 08 | MixtureOfExperts | BOUNDARY | 名称与模型架构里的 MoE（稀疏专家层）同名，新手容易误解；同基座的伪多样问题正文已提及 | 开头加一句"与模型架构的 MoE 不是一回事" |
| 09 | Reflection | KEEP | — | — |
| 10 | Judge | KEEP | — | — |
| 11 | Committee | BOUNDARY | 同 Debate：成本降低会放大"伪多样"的滥用 | 补"真差异化"的硬前提 |
| 12 | Voting | KEEP | — | — |
| 13 | RedBlueTeam | KEEP | — | — |
| 14 | Swarm | KEEP | 已标"实验性、生产用例少"；成本降 100 倍时可能变得可行，属于观察项而非历史项 | 下季度复看 |
| 15 | Blackboard | KEEP | — | — |

## ESCALATE（需要人裁决）

1. **方法层书里的"定律"命名。** LDP 的"六条跨模式定律"、Multi-Agent 手册的"五条跨模式定律"，与 Laws 1–102、宪法 Law 1–10、ADS LAW-01–13 共用"定律"一词。审计记录里已经发生过串号（手册定律 1/2 错标 ×4、DP 定律错链 ×2）。建议统一改称"跨模式原则"。这涉及跨书引用（例如 LDP 里出现的"Multi-Agent 手册定律 2"），需要一次原子批次完成。
2. **Multi-Agent 手册缺少 2026 年最常见的形态：子 Agent / Agent-as-Tool。** 主 Agent 在循环中按需派生子 Agent，子 Agent 在独立上下文里完成任务，只回传结论。教材 8.5 和手册"定律 1"都把它当作多 Agent 的核心收益，但 15 个模式里没有一个专门讲它（Orchestrator-Workers 偏向一次性拆解，Hierarchical 偏向固定层级）。是否新增第 16 个模式，属于书的结构变更。
3. **长时程 / 编码 Agent 的方法层。** 交错式计划（todo 列表）、Agent 自主检索、检查点与恢复、上下文压缩策略，正在成为 Agent 工程的主流做法，目前分散在 LDP 的"未来方向"里。是按"补边界"处理，还是作为一个新家族或 ADS 的新 SIT 立项，需要人裁决（与总编辑 Review 第 7 条同源）。

## 裁决记录（2026-10-07，维护者）

| 项 | 裁决 | 执行 |
|---|---|---|
| ESCALATE-1 "定律"改称"原则" | 同意 | 已执行：两本方法层书 INDEX 小节改名，全库 36 处现行引用同步，治理快照保留原文；体检新增旧称残留守卫 |
| ESCALATE-2 子 Agent 模式立项 | 同意 | 已执行：新增 [[multi-agent-patterns-handbook/16_子Agent委派SubAgent\|模式 16 子 Agent 委派]]，接入手册 INDEX 地图、决策树、成本表与教材 8.5 |
| ESCALATE-3 长时程 / 编码 Agent | 先补边界，不单独立项 | 已执行：在 LDP 的 ReAct、RAG、Context Compression、Planner-Executor 与 Multi-Agent 手册的 Planner-Executor 五处补边界说明 |

随 ESCALATE-3 一并落地的 BOUNDARY 条目：LDP ReAct（原生 tool use）、LDP RAG（agentic search 部分；数字标注仍待办）、LDP Planner-Executor、Multi-Agent Planner-Executor。

**其余条目（2026-10-07 第二次裁决：全部按报告建议执行）**：
- 11 条 BOUNDARY 全部落地：LDP 原则 3 改写、成本表补经验量级与思考 token 说明、家族一导语、CoT 推理模型用法、Prompt Chaining 理由、RAG 数字标注、Debate 硬前提、LDP / Multi-Agent 两处 Map-Reduce 理由、Recursive 适用面、MoE 名称提示、Committee 硬前提。
- 3 条 HISTORY_CANDIDATE 全部移入新建的 [[llm-design-patterns/06_历史模式|LDP 历史模式]]：原文完整保留，每节加退役说明与思想去向（ToT 中带外部验证器的搜索 → Self-Consistency；Least-to-Most 的分解思想 → Planner-Executor；Rephrase 改写为家族二第 5 节"意图澄清"）。
- 报告中 KEEP 条目附带的小修一并完成：Self-Critique 数字标注、Structured Output 与 Tool Use 的"未来方向"改为现在时、Routing 价差说明。
- 唯一未执行项：Swarm"下季度复看"，留到 2027-Q1。

**本轮重估完成**（2026-10-07）。体检通过，文件数 205 → 206。

**遗留同步事项（不在本轮授权内）**：ADS 的 PAT-20（Tree Search / ToT 模式卡）仍按原样推荐 ToT。按季度协议，重估不直接修改 ADS；是否把 PAT-20 改为"带外部验证器的搜索"或标注退役，需单独决定，已登记到编辑审计待办。

## 历史区去向说明

协议没有规定历史区放在哪里。建议做法：在原书末尾加一个"历史模式"附录，保留原文并标注"何时、为何退役"，不删内容，链接不断。这能延续这套库"淘汰的方法也是教材"的立场（Foundation 第 2 章）。

## 不改动声明

本报告只是季度重估建议；未授权时不移动历史区、不改写核心定义、不修改 ADS/Laws/宪法。
