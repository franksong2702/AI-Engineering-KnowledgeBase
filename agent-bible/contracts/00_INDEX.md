---
type: handbook-contract-index
aliases: [AgentBible-Contracts-INDEX]
date: 2026-07-12
abstraction_layer: 方法（能力运行规则层）
course: agent-bible
tags: [Agent, 能力运行规则, JSONSchema, 权限, Trace, 测试]
---

# Agent Bible · 五项能力的运行规则

> 这里不是五个“虚拟员工”，而是五套可由同一个执行器加载的运行规则。角色名称帮助人找到入口；真正约束运行的是输入输出字段、工具权限、状态、预算、停止/升级条件、测试和 trace。

## 先读

1. [运行规则的字段说明](00_CONTRACT-SCHEMA.md)：所有字段是什么意思、自动生成文件从哪里来。
2. [研究取证](01_研究取证.md)：发现和综合外部证据。
3. [独立事实核查](02_独立事实核查.md)：逐论断独立验证。
4. [架构取舍设计](03_架构取舍设计.md)：把需求与约束编译成架构决策。
5. [根因诊断](04_根因诊断.md)：用假设—证据—实验链定位故障。
6. [标准化评审](05_标准化评审.md)：依据外部 rubric 作可校准裁决。

## 五项能力不是五个常驻 Agent

默认做法是：一个执行器根据任务选择一套运行规则，在隔离上下文中执行。只有以下至少一项成立时，才拆为独立调用：

- 需要隔离上下文，防止作者结论污染独立核查；
- 需要不同工具或知识源；
- 需要不同权限，尤其读写、执行和外发边界；
- 需要真正并行；
- 需要独立评价者降低同源偏差。

仅仅换一个头衔不构成拆分理由。相关反模式见 [AP-6 拟人化分工](../../ai-engineering-anti-patterns/01_Agent架构反模式.md)。

## 角色卡与运行规则的关系

| 层 | 回答什么 | 是否可直接约束执行器 |
|---|---|---|
| [Agent Bible 角色卡](../00_INDEX.md) | 这个职能负责什么、常见 prompt 与失败是什么 | 否；它是设计起点 |
| 本目录运行规则 | 输入、工具、权限、状态、失败、终止和验收是什么 | 是；需由运行时实际执行 |
| [ADS](../../agent-decision-system/00_PROTOCOL.md) | 当前处境是否该用 Agent、必须遵守什么跨任务纪律 | 是；位于运行规则上游 |
| [Evaluation](../../evaluation-of-ai-systems/08_端到端评价工程样板.md) | 如何用数据证明运行规则可靠 | 是；位于发布与运行反馈层 |

## 人工维护的内容与自动生成文件

- 唯一维护源：本目录五个能力页面中的 `agent-contract`、`agent-tests`、`agent-trace` JSON block；
- 编译：`python3 _tools/compile_agent_contracts.py`；
- 防漂移：`python3 _tools/compile_agent_contracts.py --check`；
- 语义检查：`python3 _tools/check_agent_contracts.py`；
- 自动生成文件：`_machine/contracts.json`，禁止手工修改。

Markdown 负责解释，严格 JSON 供程序直接读取。两者不各维护一份独立事实。

> [!warning] 当前验证边界
> 仓库内检查器验证的是：运行规则的结构、50 个测试用例定义、权限约束、ADS 引用和 5 条示例 trace 能否一致生成。它没有连接真实模型和工具运行时，因此不能证明某个模型已经通过这 50 个行为测试。接入具体执行器后，必须按 `agent-tests` 重放并保存真实 trace，才能决定是否发布该能力。
