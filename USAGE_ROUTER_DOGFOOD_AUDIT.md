---
type: usage-router-dogfood-audit
abstraction_layer: 图谱层（使用路径验收）
date: 2026-07-09
course: ai-engineering-knowledge-base
status: completed
scope: 10 个真实任务的使用路径与 ADS 路由验收
tags: [AI工程, 使用路径, 任务路由, Dogfood, ADS, 审计]
---

# 使用路径与任务路由 Dogfood Audit

> 本文验收 [[03_使用路径与任务路由|使用路径与任务路由]] 是否真的能把真实问题路由到正确的 ADS、案例库和书籍入口。

相关入口：[[03_使用路径与任务路由|使用路径与任务路由]] · [[agent-decision-system/01_SITUATION-ROUTER|ADS Situation Router]] · [[ai-engineering-case-library/00_INDEX|Case Library]] · [[01_编辑审计|编辑审计]]

## 结论摘要

本轮用 10 个真实任务做 dogfood：

- **8 个任务：通过**。使用路径页已有一键入口，能顺畅跳到 ADS SIT、案例和理论书。
- **1 个任务：原本通过但有轻微摩擦，现已修复**。人机协作制度设计能从 ADS 找到 [[agent-decision-system/01_SITUATION-ROUTER#SIT-19 · 我在设计人与 AI 的协作制度|SIT-19]]；审计时使用路径页未单列，现已补入一键入口。
- **1 个结构文案问题，现已修复**。使用路径页原章节标题写“**四种入口**”，但实际列了 A–E 五种入口；现已改为“**五种入口**”。

总体裁决：**使用路径可用，已能承担“任务入口层”的职责；下一步不需要大改，只建议做两个小修。**

## 验收标准

每个任务按同一链路验收：

1. 任务描述是否能在 [[03_使用路径与任务路由|使用路径与任务路由]] 找到入口；
2. 是否能路由到具体 [[agent-decision-system/01_SITUATION-ROUTER|SIT-xx]]；
3. 是否能跳到至少一个相关案例；
4. 是否能回到一本理论/方法书；
5. 是否有明确的“判断句”或行动方向。

判定档位：

- `通过`：5 项都满足。
- `轻微摩擦`：能完成路由，但入口不够显性或需要多跳。
- `需修`：断链、错链、路由错误或关键入口缺失。

---

## 1. 任务需要外部信息或私有材料

**任务描述**：我要让 AI 回答公司内部政策、课程资料或私有知识，模型本身不知道这些材料。

- 使用路径入口：[[03_使用路径与任务路由#任务需要外部信息或私有材料|任务需要外部信息或私有材料]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-02 · 任务需要外部信息或实时数据|SIT-02：任务需要外部信息或实时数据]]
- 案例入口：[[ai-engineering-case-library/01_RAG与知识系统#Case 1 · 企业政策问答答非所问（深度版）|Case 1：企业政策问答答非所问]]；[[ai-engineering-case-library/01_RAG与知识系统#Case 3 · RAG 引用了过时文档|Case 3：RAG 引用了过时文档]]
- 理论入口：[[textbook-zero-to-agent/06_RAG与个人知识库|RAG 与个人知识库]]；[[laws-of-ai-engineering/01_信息与压缩定律#Law 4 — 信息守恒定律（No-Information-From-Nothing Law）|Law 4：信息守恒定律]]
- 判定：通过
- 说明：这是当前路由页最顺的一条路径，适合人和 Agent 直接调用。

## 2. 不确定该用工作流还是自主 Agent

**任务描述**：我有一个自动化任务，不知道应该写固定流程，还是让 Agent 自主规划和行动。

- 使用路径入口：[[03_使用路径与任务路由#不确定该用工作流还是自主 Agent|不确定该用工作流还是自主 Agent]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-01 · 我要决定用工作流还是自主 Agent|SIT-01：工作流还是自主 Agent]]
- 案例入口：[[ai-engineering-case-library/02_Agent架构#Case 11 · 把分类任务做成了自主 Agent（深度版）|Case 11：把分类任务做成了自主 Agent]]；[[ai-engineering-case-library/02_Agent架构#Case 19 · 探索型任务被硬做成固定计划|Case 19：探索型任务被硬做成固定计划]]
- 理论入口：[[textbook-zero-to-agent/07_工具调用与第一个Agent|工具调用与第一个 Agent]]；[[agent-decision-system/02_PATTERN-CARDS#PAT-08 · Pipeline / Prompt Chaining（流水线）|PAT-08：Pipeline]]；[[agent-decision-system/02_PATTERN-CARDS#PAT-02 · ReAct（推理+行动交替）|PAT-02：ReAct]]
- 判定：通过
- 说明：路由能清楚表达“步骤可预知→工作流；步骤依观察变化→Agent”。

## 3. 输出质量不稳，不知道怎么提质

**任务描述**：系统能回答，但质量时好时坏；我不知道是 prompt、模型、数据、评价还是流程问题。

- 使用路径入口：[[03_使用路径与任务路由#输出质量不稳，不知道怎么提质|输出质量不稳，不知道怎么提质]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-05 · 输出质量不稳，要提质|SIT-05：输出质量不稳，要提质]]；必要时接 [[agent-decision-system/01_SITUATION-ROUTER#SIT-10 · 我要评价一个 AI 系统好不好|SIT-10：评价系统好不好]]
- 案例入口：[[ai-engineering-case-library/05_评价与质量#Case 43 · 裁判模型从没和人对齐（深度版）|Case 43：裁判模型从没和人对齐]]；[[ai-engineering-case-library/05_评价与质量#Case 41 · 刷高 benchmark 真实表现没提升（深度版）|Case 41：刷高 benchmark 真实表现没提升]]
- 理论入口：[[evaluation-of-ai-systems/00_INDEX|The Evaluation of AI Systems]]；[[agent-decision-system/05_EVAL-CHECKLIST|ADS Eval Checklist]]
- 判定：通过
- 说明：路线能防止用户直接“调 prompt”，而是先定义什么叫好。

## 4. 模型给了自信答案，我不知道能不能信

**任务描述**：模型回答很流畅、很自信，但我不知道该不该采信。

- 使用路径入口：[[03_使用路径与任务路由#模型给了自信答案，我不知道能不能信|模型给了自信答案，我不知道能不能信]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-15 · 模型给了一个自信的答案，我该不该信|SIT-15：自信答案是否可信]]
- 案例入口：[[ai-engineering-case-library/10_人机与产品决策#Case 92 · 因"模型很强"移除了验证关卡|Case 92：因模型很强移除了验证关卡]]；[[ai-engineering-case-library/10_人机与产品决策#Case 100 · 把评价分数当成最终判断放弃了人的判断（深度版）|Case 100：把评价分数当成最终判断放弃了人的判断]]
- 理论入口：[[The-Constitution-of-AI-Engineering#Law 8 · 信任应随可靠性而非能力增长（Trust-Reliability Scissors）|Constitution Law 8：信任应随可靠性而非能力增长]]；[[laws-of-ai-engineering/09_人机与信任定律#Law 84 — 信任-可靠性剪刀差定律（Trust-Reliability-Scissors Law）|Law 84：信任-可靠性剪刀差定律]]
- 判定：通过
- 说明：路径能把“模型强不强”转换成“这类任务的可靠性有没有被验证”。

## 5. 要处理外部网页、邮件、文档等不可信内容

**任务描述**：Agent 要读网页、邮件、PDF、检索内容或用户上传文档，其中可能藏有恶意指令。

- 使用路径入口：[[03_使用路径与任务路由#要处理外部网页、邮件、文档等不可信内容|要处理外部网页、邮件、文档等不可信内容]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-08 · 我在处理外部/不可信内容|SIT-08：外部/不可信内容]]
- 案例入口：[[ai-engineering-case-library/06_安全与对抗#Case 51 · 邮件正文里的注入指令被执行（深度版）|Case 51：邮件正文里的注入指令被执行]]；[[ai-engineering-case-library/06_安全与对抗#Case 54 · 记忆被投毒长期潜伏（深度版）|Case 54：记忆被投毒长期潜伏]]
- 理论入口：[[laws-of-ai-engineering/10_对抗与安全定律#Law 87 — 一切输入皆指令定律（All-Input-Is-Instruction Law）|Law 87：一切输入皆指令定律]]；[[laws-of-ai-engineering/10_对抗与安全定律#Law 94 — 权限胜过自觉定律（Permission-Over-Restraint Law）|Law 94：权限胜过自觉定律]]
- 判定：通过
- 说明：路径能把“读外部内容”直接转为安全边界与权限设计问题。

## 6. 面临不可逆或高风险操作

**任务描述**：Agent 可能发布内容、删除文件、发消息、扣款、改生产配置或做其他不可逆动作。

- 使用路径入口：[[03_使用路径与任务路由#面临不可逆或高风险操作|面临不可逆或高风险操作]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-07 · 我面临不可逆或高危操作|SIT-07：不可逆或高危操作]]
- 案例入口：[[ai-engineering-case-library/10_人机与产品决策#Case 91 · 全自动发布酿成公关事故（深度版）|Case 91：全自动发布酿成公关事故]]；[[ai-engineering-case-library/04_可靠性与生产#Case 40 · 非幂等操作重试导致重复扣款（深度版）|Case 40：非幂等操作重试导致重复扣款]]
- 理论入口：[[laws-of-ai-engineering/08_可靠性与失败定律#Law 74 — 不可逆性定律（Irreversibility Law）|Law 74：不可逆性定律]]；[[human-ai-collaboration-foundation/00_INDEX|Human-AI Collaboration Foundation]]
- 判定：通过
- 说明：路径能清楚导向“可逆快、不可逆慢；高风险保留人类审批”。

## 7. 系统太贵或成本失控

**任务描述**：系统调用成本太高，或规模化后 token、模型、多 Agent、上下文成本失控。

- 使用路径入口：[[03_使用路径与任务路由#系统太贵或成本失控|系统太贵或成本失控]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-18 · 系统太贵 / 成本失控|SIT-18：成本失控]]
- 案例入口：[[ai-engineering-case-library/07_成本与性能#Case 61 · 简单任务也用最贵的模型（深度版）|Case 61：简单任务也用最贵的模型]]；[[ai-engineering-case-library/07_成本与性能#Case 64 · 上下文无限增长越来越贵（深度版）|Case 64：上下文无限增长越来越贵]]
- 理论入口：[[laws-of-ai-engineering/06_经济与资源定律#Law 52 — 边际定律（Marginal Law）|Law 52：边际定律]]；[[laws-of-ai-engineering/06_经济与资源定律#Law 56 — 成本结构决定架构定律（Cost-Structure-Shapes-Architecture Law）|Law 56：成本结构决定架构定律]]
- 判定：通过
- 说明：路径能把“账单问题”转成“架构与边际收益问题”。

## 8. 系统要上线或交付

**任务描述**：一个 AI 系统已经 demo 可用，准备交付给真实用户或进入生产环境。

- 使用路径入口：[[03_使用路径与任务路由#系统要上线或交付|系统要上线或交付]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-17 · 系统要上线/交付了|SIT-17：系统要上线/交付]]
- 案例入口：[[ai-engineering-case-library/04_可靠性与生产#Case 31 · Demo 惊艳，生产翻车（深度版）|Case 31：Demo 惊艳，生产翻车]]；[[ai-engineering-case-library/04_可靠性与生产#Case 35 · 变更全量上线引发大面积事故|Case 35：变更全量上线引发大面积事故]]
- 理论入口：[[ai-systems-in-production/00_INDEX|AI Systems in Production]]；[[evaluation-of-ai-systems/00_INDEX|The Evaluation of AI Systems]]
- 判定：通过
- 说明：路径能把“上线”从项目结尾改写成可靠性、监控、回滚和持续评价问题。

## 9. 系统在悄悄变差

**任务描述**：系统没有明显报错，但回答质量、检索命中、用户体验或成本效率在持续变差。

- 使用路径入口：[[03_使用路径与任务路由#系统在悄悄变差|系统在悄悄变差]]
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-20 · 系统在悄悄变差（静默退化/漂移）|SIT-20：静默退化/漂移]]
- 案例入口：[[ai-engineering-case-library/04_可靠性与生产#Case 33 · 上线后静默退化半年无人知|Case 33：上线后静默退化半年无人知]]；[[ai-engineering-case-library/04_可靠性与生产#Case 38 · 某环节失败静默跳过污染下游|Case 38：某环节失败静默跳过污染下游]]
- 理论入口：[[ai-systems-in-production/00_INDEX|AI Systems in Production]]；[[laws-of-ai-engineering/08_可靠性与失败定律#Law 76 — 静默降级危险定律（Silent-Degradation-Danger Law）|Law 76：静默降级危险定律]]
- 判定：通过
- 说明：路径能把“没报错但变差”识别为质量监控与漂移问题，而不是普通 bug。

## 10. 我在设计人与 AI 的协作制度

**任务描述**：我要决定哪些事由 AI 做、哪些事由人审批、责任如何划分、界面如何支撑真实判断。

- 使用路径入口：当前没有在“常见任务的一键入口”中单列；可通过 [[03_使用路径与任务路由#B. 我有一个具体任务，不知道怎么设计|B. 我有一个具体任务，不知道怎么设计]] 进入 ADS。
- ADS 路由：[[agent-decision-system/01_SITUATION-ROUTER#SIT-19 · 我在设计人与 AI 的协作制度|SIT-19：人机协作制度设计]]
- 案例入口：[[ai-engineering-case-library/10_人机与产品决策#Case 91 · 全自动发布酿成公关事故（深度版）|Case 91：全自动发布酿成公关事故]]；[[ai-engineering-case-library/10_人机与产品决策#Case 92 · 因"模型很强"移除了验证关卡|Case 92：因模型很强移除了验证关卡]]；[[ai-engineering-case-library/10_人机与产品决策#Case 98 · 决策 Agent 越界替人拍板|Case 98：决策 Agent 越界替人拍板]]
- 理论入口：[[human-ai-collaboration-foundation/00_INDEX|Human-AI Collaboration Foundation]]；[[human-ai-interaction-design/00_INDEX|Human-AI Interaction Design]]
- 判定：轻微摩擦（已修复）
- 说明：ADS 覆盖充分；审计时使用路径页的一键任务入口缺了这个高价值任务，现已补一段“我在设计人与 AI 的协作制度”。

---

## 发现的问题

### P1 · “常见任务的一键入口”缺 SIT-19

状态：✅ 已修复（2026-07-09），已在 [[03_使用路径与任务路由#我在设计人与 AI 的协作制度|使用路径]] 增补 SIT-19 一键入口。

原问题：[[agent-decision-system/01_SITUATION-ROUTER#SIT-19 · 我在设计人与 AI 的协作制度|SIT-19]] 在 ADS 中存在，且与后补书 [[human-ai-collaboration-foundation/00_INDEX|Human-AI Collaboration Foundation]] / [[human-ai-interaction-design/00_INDEX|Human-AI Interaction Design]] 关系很重要；但 [[03_使用路径与任务路由|使用路径与任务路由]] 的“常见任务的一键入口”没有单列。

影响：人或 Agent 仍能通过通用入口进入 ADS，但无法一键直达这个高价值任务。

建议：后续小修时，在“常见任务的一键入口”中补一个小节：

```markdown
### 我在设计人与 AI 的协作制度

- 先看：[[agent-decision-system/01_SITUATION-ROUTER#SIT-19 · 我在设计人与 AI 的协作制度|SIT-19：人机协作制度设计]]
- 案例：[[ai-engineering-case-library/10_人机与产品决策#Case 91 · 全自动发布酿成公关事故（深度版）|Case 91：全自动发布酿成公关事故]]
- 深入：[[human-ai-collaboration-foundation/00_INDEX|Human-AI Collaboration Foundation]] 与 [[human-ai-interaction-design/00_INDEX|Human-AI Interaction Design]]

判断句：协作制度不是让 AI 多做，而是让人和 AI 各自在正确的位置承担正确的判断、行动和责任。
```

### P2 · “四种入口”标题与实际 A–E 五类不一致

状态：✅ 已修复（2026-07-09），标题已改为 [[03_使用路径与任务路由#五种入口|五种入口]]。

原问题：[[03_使用路径与任务路由#五种入口|五种入口]] 当前已修复；原问题是该节实际列了 A–E 五类：快速理解、具体任务、案例样板、系统学习、维护者。

影响：不影响链接和路由，但属于自描述小瑕疵。

状态：已按建议修复为“## 五种入口”。

---

## ADS 裁决

- **Situation**: 新增任务路由页后，需要验证它是否能处理真实任务。
- **Diagnosis**: 这是 [[agent-decision-system/01_SITUATION-ROUTER#SIT-10 · 我要评价一个 AI 系统好不好|SIT-10]] + [[agent-decision-system/01_SITUATION-ROUTER#SIT-14 · 我要在多个方案间做决策|SIT-14]] 的组合：评价新路由层是否有效，并决定是否进入下一批修复。
- **Relevant Laws**: LAW-01 验证优先；LAW-10 简单优先；LAW-12 判断力稀缺；LAW-04 防止把“入口更多”误当成“更好用”。
- **Recommended Patterns**: PAT-15 Guardrails / Validation；PAT-16 Routing；PAT-07 Structured Output。
- **Avoid**: 发现小问题就扩写整套路由；把审计变成新书；跳过真实任务直接自称可用。
- **Evaluation Checklist**: 10 个任务中至少 8 个一跳可用；没有断链；发现的问题能被局部小修解决。

本轮结果：满足。

## 后续建议

小修批次已完成（2026-07-09）：

1. “## 四种入口”已改为“## 五种入口”；
2. [[03_使用路径与任务路由|使用路径与任务路由]] 已增补 SIT-19 的一键入口；
3. 已跑 `kb_health_check.py`。

使用路径层可视为收束。之后再回到更大队列：M3 / M6–M8 / Laws citation 全量核验是否按需启动。
