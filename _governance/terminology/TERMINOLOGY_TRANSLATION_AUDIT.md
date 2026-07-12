---
type: terminology-translation-audit
status: completed
date: 2026-07-12
abstraction_layer: 运营机制（术语治理）
course: ai-engineering-knowledge-base
tags: [术语, 翻译, 人话, 可读性, 审计]
---

# “正典”与“机器……”术语翻译审计

> 本表是本轮逐文件裁决账本。基线扫描（修改前）发现：“正典”319 处 / 54 个文件；“机器契约、机器版本、机器文件、机器可读、机器消费、机器投影、机器格式、机器版”合计 43 处 / 20 个文件。代码标识符、路径与 JSON 字段不在机械替换范围。

## 裁决规则

1. 当前入口、正文、维护文件、ADS 与仍在执行的内容审计：逐处按语境改写。
2. `_governance/fable5/`：保留署名快照原文。
3. 其他已归档治理审计：保留历史原文；当前读者从 Governance Index 获得术语说明。
4. 技术标识符如 `_machine`、`contract_version`、脚本名保留；正文第一次出现时说人话。
5. 不使用全库字符串替换；同一个旧词可能分别改成“唯一维护位置、权威定义、主要定义位置、自动生成文件、程序可以直接解析”等。

## 实施结果

- 当前有效文档中的目标术语：**0 处**。
- 历史原文与本审计中的保留项：**231 处 / 21 个精确豁免文件**；不使用目录级通配。
- `01_编辑审计.md` 是混合文件：现行说明与活队列已经改写，2026-07-06 审计原文和按日期完成记录保留原话。
- 历史文件只允许修复失效链接等技术性问题，不借此重写当时的判断和作者措辞。
- 防回归工具：`python3 _tools/check_plain_language_terms.py`；总健康检查会自动调用它。工具不仅固定 21 个豁免文件，还固定每个文件当前允许保留的数量；历史文件新增或减少目标词都要求先人工复核并更新本审计。

## 翻译对照

| 原表达承担的意思 | 当前正文优先写法 |
|---|---|
| 内容只能在一处维护 | 唯一维护位置 / 唯一需要人工维护的主版本 |
| 某处定义说了算 | 权威定义 / 以此处定义为准 |
| 一个概念主要在哪本书讲 | 主要定义位置 / 内容归属 |
| 高层规则集合 | 核心规则层 |
| 给程序读取的生成物 | 自动生成的 JSON/YAML 文件 |
| machine-readable | 程序可以直接解析 / 固定结构 |
| machine-consumable | 供程序或下游工具直接读取 |
| compiler/compile（面向普通读者） | 生成脚本 / 从文档生成 JSON 或 YAML |

## 逐文件裁决

| 文件 | “正典”基线 | “机器……”基线 | 裁决 | 理由 |
|---|---:|---:|---|---|
| [01_编辑审计.md](../../01_编辑审计.md) | 33 | 3 | 混合文件：现行段落改写，历史原文保留 | 活队列要说人话；早期审计和已完成记录保留成文时措辞 |
| [02_学习路径与未来扩展.md](../../02_学习路径与未来扩展.md) | 3 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [03_使用路径与任务路由.md](../../03_使用路径与任务路由.md) | 2 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [AGENTS.md](../../AGENTS.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | 3 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [GOVERNANCE_INDEX.md](../../GOVERNANCE_INDEX.md) | 5 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [MAINTENANCE.md](../../MAINTENANCE.md) | 10 | 4 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [QUARTERLY_REEVALUATION_PROTOCOL.md](../../QUARTERLY_REEVALUATION_PROTOCOL.md) | 8 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [README.md](../../README.md) | 1 | 1 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [The-Constitution-of-AI-Engineering.md](../../The-Constitution-of-AI-Engineering.md) | 4 | 1 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [_governance/ads-case/ADS_LAW_SOURCE_MAP_AUDIT.md](../../_governance/ads-case/ADS_LAW_SOURCE_MAP_AUDIT.md) | 5 | 1 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/architecture/ARCHITECTURE_REVIEW.md](../../_governance/architecture/ARCHITECTURE_REVIEW.md) | 27 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/content/AGENT_BIBLE_P1C_SCOPE_AUDIT.md](../../_governance/content/AGENT_BIBLE_P1C_SCOPE_AUDIT.md) | 3 | 2 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [_governance/content/BOOK_EXPANSION_PRIORITY_AUDIT.md](../../_governance/content/BOOK_EXPANSION_PRIORITY_AUDIT.md) | 6 | 1 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md](../../_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW.md) | 5 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/fable5/FABLE5_REVIEW_PROMPT.md](../../_governance/fable5/FABLE5_REVIEW_PROMPT.md) | 3 | 0 | 保留署名快照原文 | 外部模型署名审阅记录，不反向改写作者措辞 |
| [_governance/fable5/FABLE5_总审报告.md](../../_governance/fable5/FABLE5_总审报告.md) | 19 | 4 | 保留署名快照原文 | 外部模型署名审阅记录，不反向改写作者措辞 |
| [_governance/fable5/FABLE5_架构收束REVIEW.md](../../_governance/fable5/FABLE5_架构收束REVIEW.md) | 49 | 5 | 保留署名快照原文 | 外部模型署名审阅记录，不反向改写作者措辞 |
| [_governance/fable5/FABLE5_深读笔记.md](../../_governance/fable5/FABLE5_深读笔记.md) | 5 | 0 | 保留署名快照原文 | 外部模型署名审阅记录，不反向改写作者措辞 |
| [_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT.md](../../_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT.md) | 4 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT.md](../../_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT.md) | 14 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT.md](../../_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT.md) | 9 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT.md](../../_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT.md) | 8 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT.md](../../_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT.md) | 1 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/LAWS_REWRITE_GRAND_PLAN.md](../../_governance/laws/LAWS_REWRITE_GRAND_PLAN.md) | 8 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/LAWS_TAXONOMY_REVIEW.md](../../_governance/laws/LAWS_TAXONOMY_REVIEW.md) | 12 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT.md](../../_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT.md) | 1 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/LAW_REFERENCE_AUDIT.md](../../_governance/laws/LAW_REFERENCE_AUDIT.md) | 20 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md](../../_governance/laws/LAW_REFERENCE_REMAINING_CANDIDATES.md) | 2 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md](../../_governance/laws/LAW_REFERENCE_SYSTEM_CLOSURE.md) | 2 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT.md](../../_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT.md) | 1 | 0 | 保留归档审计原文 | 治理历史快照；当前执行口径已回到编辑审计与维护手册 |
| [agent-bible/00_INDEX.md](../../agent-bible/00_INDEX.md) | 0 | 1 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-bible/contracts/00_CONTRACT-SCHEMA.md](../../agent-bible/contracts/00_CONTRACT-SCHEMA.md) | 0 | 3 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-bible/contracts/00_INDEX.md](../../agent-bible/contracts/00_INDEX.md) | 0 | 4 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-bible/contracts/01_研究取证.md](../../agent-bible/contracts/01_研究取证.md) | 0 | 2 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-bible/contracts/02_独立事实核查.md](../../agent-bible/contracts/02_独立事实核查.md) | 0 | 2 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-bible/contracts/03_架构取舍设计.md](../../agent-bible/contracts/03_架构取舍设计.md) | 0 | 2 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-bible/contracts/04_根因诊断.md](../../agent-bible/contracts/04_根因诊断.md) | 0 | 2 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-bible/contracts/05_标准化评审.md](../../agent-bible/contracts/05_标准化评审.md) | 0 | 2 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-decision-system/01_SITUATION-ROUTER.md](../../agent-decision-system/01_SITUATION-ROUTER.md) | 0 | 1 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [agent-decision-system/04_LAW-INVARIANTS.md](../../agent-decision-system/04_LAW-INVARIANTS.md) | 1 | 1 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [ai-engineering-anti-patterns/00_INDEX.md](../../ai-engineering-anti-patterns/00_INDEX.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [evaluation-of-ai-systems/01_评价的基础理论.md](../../evaluation-of-ai-systems/01_评价的基础理论.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [foundation-of-ai-engineering/00_INDEX.md](../../foundation-of-ai-engineering/00_INDEX.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [human-ai-interaction-design/00_INDEX.md](../../human-ai-interaction-design/00_INDEX.md) | 3 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [human-ai-interaction-design/05_协作制度的界面实现.md](../../human-ai-interaction-design/05_协作制度的界面实现.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [human-ai-interaction-design/06_交互反模式与评价.md](../../human-ai-interaction-design/06_交互反模式与评价.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [laws-of-ai-engineering/00_CORE-LAWS.md](../../laws-of-ai-engineering/00_CORE-LAWS.md) | 2 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [laws-of-ai-engineering/00_EXTERNAL-REFERENCES.md](../../laws-of-ai-engineering/00_EXTERNAL-REFERENCES.md) | 7 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [laws-of-ai-engineering/00_INDEX.md](../../laws-of-ai-engineering/00_INDEX.md) | 5 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [laws-of-ai-engineering/00_METADATA-SCHEMA.md](../../laws-of-ai-engineering/00_METADATA-SCHEMA.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [laws-of-ai-engineering/00_REFERENCE-POLICY.md](../../laws-of-ai-engineering/00_REFERENCE-POLICY.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [llm-design-patterns/02_提示结构模式.md](../../llm-design-patterns/02_提示结构模式.md) | 0 | 1 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [llm-design-patterns/04_质量控制模式.md](../../llm-design-patterns/04_质量控制模式.md) | 2 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [llm-design-patterns/05_编排模式.md](../../llm-design-patterns/05_编排模式.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multi-agent-patterns-handbook/02_MapReduce.md](../../multi-agent-patterns-handbook/02_MapReduce.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multi-agent-patterns-handbook/03_树状分解Tree.md](../../multi-agent-patterns-handbook/03_树状分解Tree.md) | 2 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multi-agent-patterns-handbook/05_Planner-Executor.md](../../multi-agent-patterns-handbook/05_Planner-Executor.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multi-agent-patterns-handbook/10_裁判Judge.md](../../multi-agent-patterns-handbook/10_裁判Judge.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multi-agent-patterns-handbook/11_委员会Committee.md](../../multi-agent-patterns-handbook/11_委员会Committee.md) | 1 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multimodal-systems/00_INDEX.md](../../multimodal-systems/00_INDEX.md) | 4 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multimodal-systems/03_跨模态上下文与状态.md](../../multimodal-systems/03_跨模态上下文与状态.md) | 3 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multimodal-systems/04_多模态评价与证据.md](../../multimodal-systems/04_多模态评价与证据.md) | 2 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |
| [multimodal-systems/05_多模态生产系统.md](../../multimodal-systems/05_多模态生产系统.md) | 2 | 0 | 当前有效文档：逐处改写 | 读者入口、正文、当前维护或仍在执行的审计 |

## 完成判据

- 当前有效文档中的候选词全部归零或进入精确允许清单；
- 历史快照残留只出现在本表声明的保留文件；
- 人读正文不再用晦涩词代替简单说明；
- JSON 字段、脚本名和生成链保持兼容；
- 链接、ADS、能力规则生成文件和全库体检通过。
