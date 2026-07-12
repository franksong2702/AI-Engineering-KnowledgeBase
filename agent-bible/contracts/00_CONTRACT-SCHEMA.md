---
type: handbook-contract-schema
aliases: [AgentBible-Contract-Schema]
date: 2026-07-12
abstraction_layer: 方法（能力运行规则层）
course: agent-bible
tags: [Agent, 运行规则, 字段说明, 权限, Memory, Trace, 测试]
---

# Agent 运行规则：每个字段到底管什么

> 这不是为了让页面显得正式。每个字段都对应一种真实失败：缺输入会逼 Agent 猜、工具无权限会越权、没有终止条件会循环、没有失败状态会伪装成功、没有 trace 会无法复盘。

## 1. 人读的十四段

| 段 | 人话解释 | 缺失会怎样 |
|---|---|---|
| 能力与版本 | 当前加载的能力和规则版本 | 运行记录无法知道用了哪版规则 |
| 何时使用 | 什么条件满足才值得调用 | 简单任务也被过度 Agent 化 |
| 何时不用 | 更简单方案及邻近能力边界 | 五个能力退化为换头衔 |
| 输入 schema | 调用前必须提供什么 | 信息不足时靠猜补齐 |
| 输出 schema | 成功、部分完成、受阻如何返回 | 失败被包装成正常答案 |
| 工具与权限 | 能读、写、执行或外发什么 | Prompt 约束代替真实权限 |
| 状态 schema | 本次任务已经做到哪里 | 长任务失忆、重复劳动 |
| Memory policy | 哪些状态能跨任务保留 | 错误或敏感数据永久污染记忆 |
| 预算 | 最大步骤、工具次数和时间 | 无限循环或成本失控 |
| 停止/受阻/升级 | 三种终态分别何时触发 | 不知道什么时候该停或问人 |
| 失败协议 | 工具坏、证据不足、校验失败怎么办 | 静默跳过或伪装成功 |
| Trace schema | 记录哪些可审计事件 | 无法解释工具和停止原因 |
| ADS 对照 | 受哪些跨任务纪律约束 | 在本书里另造一套 Law/Pattern |
| 评价套件 | 如何证明规则真的生效 | 只有漂亮的字段结构，没有行为证据 |

机器 block 另外保留 `source_role`，用于回到原始角色卡，不把它当能力差异。

## 2. 三种 tagged JSON block

每个能力页必须各有一次：

````text
<!-- agent-contract -->
```json
{ ...契约... }
```

<!-- agent-tests -->
```json
{ "cases": [ ...正好 10 条... ] }
```

<!-- agent-trace -->
```json
{ "events": [ ...完整终态 trace... ] }
```
````

生成脚本只读取带标记的 block；普通示例 JSON 不会误入自动生成文件。

## 3. 输入和输出

输入输出采用 JSON Schema 的稳定子集：`type`、`properties`、`required`、`additionalProperties`。编译器验证结构，实际运行时仍需由执行器使用 JSON Schema validator 或等价逻辑拒绝非法输入。

所有输出都必须包含：

```json
{
  "status": "completed | partial | blocked | escalated",
  "summary": "给人看的简短结论",
  "evidence": [],
  "open_issues": [],
  "stop_reason": "程序可以直接解析的终止原因"
}
```

`partial` 不是失败伪装；它必须明确已经完成什么、缺什么、为什么继续不值得或不安全。

## 4. 权限

每项工具都要写：

- `name`：稳定工具名；
- `permission`：`read / write / execute / external_send`；
- `scope`：允许访问的对象；
- `side_effect`：是否产生外部状态变化；
- `approval_required`：是否需要人类审批；
- `when_unavailable`：工具不可用时如何降级。

没有列出的工具默认禁止。System Prompt 里的“请不要越权”不是权限实现。

## 5. 状态与长期记忆

`state_schema` 只描述当前任务状态。`memory_policy` 另外规定：允许跨任务保存什么、禁止保存什么、写入条件、来源与时间、冲突处理和过期/删除。

默认原则：先不写长期记忆。只有跨任务复用收益能覆盖污染、隐私和维护成本时才开启。

## 6. 终止与失败

- `stop`：任务已达到验收标准；
- `block`：缺信息、工具或证据，继续也无法可靠完成；
- `escalate`：风险、权限或价值判断要求交给有责任的人；
- `failure_protocol`：说明工具失败、schema 失败、重复调用和预算耗尽的处理。

三者必须在输出和 trace 中使用相同的机器状态，不能正文说“受阻”、JSON 却写 `completed`。

## 7. 测试与 trace

每个能力正好十个测试：五个 `normal`、五个 `adversarial`。正常组也要包括工具失败、证据不足、部分完成或预算边界，不能都是 happy path。

测试验证的是：预期状态、允许的工具、禁止的工具和停止原因。最终文字是否流畅不是主要判据。

本库自带检查器只验证测试定义完整且内部一致，不假装执行了模型。实际运行时必须由适配器把每条用例送入执行器，再把真实状态、工具和停止原因与本页规则比较。

trace 只记录行动与证据，不要求隐藏思维链。统一事件：

```text
task_received → input_validated → state_updated → tool_requested
→ tool_allowed/tool_denied → tool_result → evidence_recorded
→ completed/blocked/escalated
```

五个运行规则页面中的 trace 是格式样例，不是生产运行证据。真实系统必须重新生成，并按隐私策略脱敏。

## 8. 编译和验证

```bash
python3 _tools/compile_agent_contracts.py
python3 _tools/compile_agent_contracts.py --check
python3 _tools/check_agent_contracts.py
```

第一条生成 JSON 文件；第二条检查文档与生成文件是否一致；第三条检查五个能力、十个用例、终态 trace、权限和 ADS 引用。三条都通过，才允许声称运行规则与生成文件同步。
