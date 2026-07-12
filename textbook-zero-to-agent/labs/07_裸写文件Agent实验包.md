---
type: course-lab
aliases: [Textbook-Lab-07]
date: 2026-07-10
abstraction_layer: 技巧 + 方法（入门实验）
course: zero-to-agent
chapter: 7
lab: bare-file-agent
tags: [AI教程, Agent, 工具调用, 权限, Trace, 实验包]
---

# 第 7 章实验包：裸写一个有边界的文件 Agent

> 配套章节：[第 7 章 工具调用与第一个 Agent](../07_工具调用与第一个Agent.md)。目标不是做一个“很聪明”的 Agent，而是亲手写出最小循环，并证明它有权限边界、终止条件、失败反馈和可审计 trace。

## 1. 你要交付什么

一个不用 Agent 框架的文件 Agent：

```text
用户任务
  ↓
模型适配层给出：一句行动计划 + 工具调用意图
  ↓
代码侧校验权限并执行工具
  ↓
结构化结果回到模型适配层
  ↓
继续 / 完成 / 受控停止
```

工具集固定为：

- `list_files`：列出 sandbox 内文件；
- `read_file`：读取 sandbox 内文本文件；
- `search_text`：在 sandbox 内搜索文本；
- `write_file`：写文件，必须经过审批函数。

本实验使用 `ScriptedModel` 模拟模型决策，因此不需要 API key，也不会把网络问题混入 Agent 循环。最后接真实模型时，只替换模型适配层。

### 关于“思考”的边界

trace 只记录**一句可审计的行动计划**，例如“先列出文件，再决定读取哪个”，不要求模型暴露隐藏思维链。可审计的是行动依据、工具参数、工具结果和停止原因，不是假装一段生成出来的长推理就是真实内部过程。

## 2. 机械完成标准

必须同时满足：

1. `python3 -m unittest -v` 显示 5 个测试全部 `OK`；
2. happy path 能在 sandbox 内生成 `index.md`；
3. `../outside.txt` 路径逃逸被代码层拒绝；
4. 未批准的 `write_file` 不产生文件；
5. 连续两次完全相同的工具调用在第二次执行前停止；
6. 达到最大轮数时停止并报告 `max_steps`，不伪装成功；
7. `trace.jsonl` 能逐步回答：模型想调用什么、代码实际执行了什么、为什么停止。

## 3. 开始前自检

### 先修知识

- 已完成 [第 5 章实验包](05_API批处理流水线实验包.md)，理解客户端适配层、结构化响应和重试预算；
- 理解函数、类、JSON、异常和单元测试；
- 能解释“模型只生成调用意图，执行权在代码侧”。

### 预计时间

- 完成脚本模型版本：5–8 小时；
- 再接真实模型：额外 2–4 小时。

### 环境检查

```bash
python3 --version
mkdir -p chapter07-bare-agent/workspace
cd chapter07-bare-agent
python3 -m venv .venv
source .venv/bin/activate
printf '# A\n' > workspace/a.md
```

本实验只使用 Python 标准库。

## 4. 交付物结构

```text
chapter07-bare-agent/
├── .gitignore
├── agent.py
├── test_agent.py
├── script.json
├── trace.jsonl       # 运行后生成
└── workspace/
    ├── a.md
    └── index.md      # Agent 获批后生成
```

## 5. Starter：先搭循环骨架

<!-- starter-file: agent.py -->
```python
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict


@dataclass(frozen=True)
class ModelReply:
    plan: str
    tool_call: ToolCall | None = None
    final: str | None = None


class AgentStopped(RuntimeError):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class ScriptedModel:
    def __init__(self, replies: list[dict]):
        self.replies = replies
        self.position = 0

    def next(self, messages: list[dict]) -> ModelReply:
        # TODO: 逐条把 JSON script 转成 ModelReply；耗尽时显式停止。
        raise NotImplementedError


class FileTools:
    def __init__(self, root: Path):
        self.root = root.resolve()

    def resolve_inside_root(self, user_path: str) -> Path:
        # TODO: 拒绝绝对路径和 ../ 逃逸；不能只做字符串前缀判断。
        raise NotImplementedError

    def execute(self, call: ToolCall, approve: Callable[[ToolCall], bool]) -> dict:
        # TODO: 四个工具；所有失败返回 {"ok": false, "error": ...}。
        raise NotImplementedError


class Agent:
    def __init__(self, model, tools: FileTools, trace_path: Path, max_steps: int = 15):
        self.model = model
        self.tools = tools
        self.trace_path = trace_path
        self.max_steps = max_steps

    def run(self, task: str, approve: Callable[[ToolCall], bool]) -> str:
        # TODO: 模型→工具→结果循环；重复调用熔断；max_steps；trace。
        raise NotImplementedError
```

先确认语法和 import：

```bash
python3 -m py_compile agent.py
```

## 6. 分步任务

| 步骤 | 要做什么 | 机械检查 |
|---|---|---|
| 1 | 实现 `ScriptedModel.next` | 能依次返回工具调用和 final；script 用尽显式报 `script_exhausted` |
| 2 | 实现 sandbox 路径解析 | 允许 `a.md`/`.`；拒绝绝对路径和 `../` |
| 3 | 实现四个工具 | 每个返回结构化结果；失败不抛裸 traceback 给模型 |
| 4 | 实现 write 审批 | 审批为 false 时不写入，结果标 `approval_denied` |
| 5 | 实现 Agent 循环 | 工具结果回填 messages；final 才算完成 |
| 6 | 加重复调用熔断与最大轮数 | 两类停止均写 trace 并抛 `AgentStopped` |
| 7 | 写 5 个测试 | happy path、路径逃逸、审批、重复调用、max steps |

### 工具结果契约

成功：

```json
{"ok": true, "data": {"content": "..."}}
```

失败：

```json
{"ok": false, "error": {"type": "FileNotFoundError", "message": "文件不存在：missing.md"}}
```

失败结果要帮助下一步决策，但不能泄露 sandbox 外部路径、密钥或无关 traceback。

### 审批契约

审批函数接收**完整的 ToolCall**，而不是一句“是否同意写文件”。人至少要看到：

- 写哪个相对路径；
- 写入内容摘要或完整内容；
- 是否覆盖已有文件。

本实验的 CLI 用 `--approve-writes` 模拟同意；测试里用 lambda 明确批准或拒绝。真实产品必须设计可见的审批界面，不能把审批藏在 prompt 里。

## 7. 测试 Starter

先创建测试，再让实现逐项变绿。

<!-- starter-file: test_agent.py -->
```python
import json
import tempfile
import unittest
from pathlib import Path

from agent import Agent, AgentStopped, FileTools, ScriptedModel, ToolCall


class AgentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "a.md").write_text("# A\n", encoding="utf-8")
        self.trace = self.root / "trace.jsonl"

    def tearDown(self):
        self.tmp.cleanup()

    def agent(self, replies, max_steps=15):
        return Agent(ScriptedModel(replies), FileTools(self.root), self.trace, max_steps)

    def test_happy_path_writes_inside_sandbox(self):
        replies = [
            {"plan": "先列目录", "tool": "list_files", "arguments": {"path": "."}},
            {"plan": "读取标题", "tool": "read_file", "arguments": {"path": "a.md"}},
            {
                "plan": "写目录",
                "tool": "write_file",
                "arguments": {"path": "index.md", "content": "- [A](a.md)\n"},
            },
            {"plan": "任务完成", "final": "已生成 index.md"},
        ]
        result = self.agent(replies).run("生成目录", approve=lambda call: True)
        self.assertEqual(result, "已生成 index.md")
        self.assertTrue((self.root / "index.md").exists())
        self.assertGreaterEqual(len(self.trace.read_text().splitlines()), 7)

    def test_path_escape_is_rejected(self):
        result = FileTools(self.root).execute(
            ToolCall("read_file", {"path": "../outside.txt"}),
            approve=lambda call: True,
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["error"]["type"], "PermissionError")

    def test_write_requires_approval(self):
        result = FileTools(self.root).execute(
            ToolCall("write_file", {"path": "denied.md", "content": "x"}),
            approve=lambda call: False,
        )
        self.assertFalse(result["ok"])
        self.assertFalse((self.root / "denied.md").exists())

    def test_repeated_identical_call_stops_before_second_execution(self):
        replies = [
            {"plan": "读取", "tool": "read_file", "arguments": {"path": "a.md"}},
            {"plan": "原样重试", "tool": "read_file", "arguments": {"path": "a.md"}},
        ]
        with self.assertRaises(AgentStopped) as caught:
            self.agent(replies).run("重复测试", approve=lambda call: True)
        self.assertEqual(caught.exception.reason, "repeated_tool_call")

    def test_max_steps_is_explicit_stop(self):
        replies = [
            {"plan": "列目录", "tool": "list_files", "arguments": {"path": "."}},
            {"plan": "读文件", "tool": "read_file", "arguments": {"path": "a.md"}},
            {"plan": "还想继续", "tool": "search_text", "arguments": {"path": ".", "query": "A"}},
        ]
        with self.assertRaises(AgentStopped) as caught:
            self.agent(replies, max_steps=2).run("轮数测试", approve=lambda call: True)
        self.assertEqual(caught.exception.reason, "max_steps")


if __name__ == "__main__":
    unittest.main()
```

## 8. Happy path 脚本与 CLI 验收

<!-- fixture-file: script.json -->
```json
{
  "replies": [
    {"plan": "先查看工作区文件", "tool": "list_files", "arguments": {"path": "."}},
    {"plan": "读取 Markdown 标题", "tool": "read_file", "arguments": {"path": "a.md"}},
    {"plan": "把标题写入目录", "tool": "write_file", "arguments": {"path": "index.md", "content": "- [A](a.md)\n"}},
    {"plan": "目标文件已生成", "final": "已生成 index.md"}
  ]
}
```

参考实现提供 CLI。运行：

```bash
python3 agent.py \
  --root workspace \
  --script script.json \
  --trace trace.jsonl \
  --approve-writes
```

通过判据：

```bash
test -f workspace/index.md
grep -q 'A' workspace/index.md
python3 - <<'PY'
import json
from pathlib import Path
events = [json.loads(x) for x in Path("trace.jsonl").read_text().splitlines()]
assert events[-1]["event"] == "final"
assert any(e["event"] == "tool_result" and e["tool"] == "write_file" for e in events)
print("agent trace verification: OK")
PY
```

## 9. Trace 最小字段

每行一个 JSON 事件，至少包含：

| 事件 | 必填字段 |
|---|---|
| `model_reply` | step、plan、tool/final |
| `tool_result` | step、tool、arguments、result |
| `stop` | step、reason |
| `final` | step、answer |

trace 的目标不是展示“它多聪明”，而是让你能回答：

- 哪一步第一次偏离？
- 模型选错工具，还是工具执行错？
- 失败信息有没有让下一步更容易纠正？
- 写操作有没有真的经过代码侧批准？
- 停止是正常完成、重复调用，还是预算耗尽？

## 10. 常见失败：先判层

| 现象 | 诊断 | 修复方向 |
|---|---|---|
| 模型反复读同一文件 | 决策层无进展 | 重复调用签名熔断；把已有结果明确回填 |
| `../` 仍能读到外部文件 | 权限层漏洞 | 必须比较 `resolve()` 后的父子关系，不做字符串前缀判断 |
| prompt 写“不要越界”但代码允许 | 把提示当权限 | 路径和工具权限放代码层强制 |
| write 被拒后文件仍出现 | 审批发生在执行后 | 先审批，再创建目录/写文件 |
| 工具失败后 Agent 当成功继续 | 错误契约不清 | 返回 `ok=false` 与明确 error；禁止空字符串假成功 |
| 最后一轮没 final 却报告完成 | 终止语义错误 | 只有明确 final 才算成功；max_steps 必须是失败/阻塞状态 |
| trace 只有自然语言总结 | 不可审计 | 工具名、参数、结果、停止原因写结构化事件 |
| 测试全靠真实模型 | 方差污染 | 用 ScriptedModel 测控制流；真实模型只做额外集成测试 |

## 11. 评分 rubric（100 分）

| 维度 | 分值 | 合格判据 |
|---|---:|---|
| Agent 循环 | 20 | 工具结果回填；只有 final 成功；max steps 有界 |
| 权限边界 | 20 | sandbox 防逃逸；写操作审批在执行前 |
| 失败与恢复 | 15 | 工具错误结构化；重复调用熔断；不伪装成功 |
| 可观测性 | 15 | 四类 trace 事件齐全，可定位首次偏离 |
| 测试 | 20 | 5 个测试全过，且控制流不依赖真实模型 |
| 简单性 | 10 | 无框架、无无关功能；模型适配层可替换 |

- **合格（70–84）**：全部机械完成标准通过；
- **良好（85–94）**：再补工具超时、覆盖写入和损坏 script 测试；
- **优秀（95–100）**：接入真实模型后，五个离线测试仍保持确定性通过，并增加 3 个未预先调过的真实任务失败分析。

## 12. 参考实现

先让自己的测试逐项变绿，再展开对照。

<details>
<summary>展开 agent.py 参考实现</summary>

<!-- reference-file: agent.py -->
```python
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict


@dataclass(frozen=True)
class ModelReply:
    plan: str
    tool_call: ToolCall | None = None
    final: str | None = None


class AgentStopped(RuntimeError):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class ScriptedModel:
    def __init__(self, replies: list[dict]):
        self.replies = replies
        self.position = 0

    def next(self, messages: list[dict]) -> ModelReply:
        if self.position >= len(self.replies):
            raise AgentStopped("script_exhausted")
        raw = self.replies[self.position]
        self.position += 1
        plan = str(raw.get("plan", ""))
        if "final" in raw:
            return ModelReply(plan=plan, final=str(raw["final"]))
        if "tool" not in raw or "arguments" not in raw:
            raise AgentStopped("invalid_model_reply")
        return ModelReply(
            plan=plan,
            tool_call=ToolCall(str(raw["tool"]), dict(raw["arguments"])),
        )


class FileTools:
    def __init__(self, root: Path):
        self.root = root.resolve()
        if not self.root.is_dir():
            raise NotADirectoryError(f"sandbox 不存在或不是目录：{root}")

    def resolve_inside_root(self, user_path: str) -> Path:
        raw = Path(user_path)
        if raw.is_absolute():
            raise PermissionError("禁止绝对路径")
        candidate = (self.root / raw).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise PermissionError(f"路径逃逸 sandbox：{user_path}")
        return candidate

    def execute(self, call: ToolCall, approve: Callable[[ToolCall], bool]) -> dict:
        try:
            if call.name == "list_files":
                path = self.resolve_inside_root(str(call.arguments.get("path", ".")))
                if not path.is_dir():
                    raise NotADirectoryError(f"不是目录：{call.arguments.get('path', '.')}")
                files = [
                    item.relative_to(self.root).as_posix()
                    for item in sorted(path.rglob("*"))
                    if item.is_file()
                ]
                return {"ok": True, "data": {"files": files}}

            if call.name == "read_file":
                path = self.resolve_inside_root(str(call.arguments["path"]))
                return {"ok": True, "data": {"content": path.read_text(encoding="utf-8")}}

            if call.name == "search_text":
                path = self.resolve_inside_root(str(call.arguments.get("path", ".")))
                query = str(call.arguments["query"])
                matches = []
                candidates = [path] if path.is_file() else sorted(path.rglob("*"))
                for item in candidates:
                    if not item.is_file():
                        continue
                    try:
                        lines = item.read_text(encoding="utf-8").splitlines()
                    except UnicodeDecodeError:
                        continue
                    for line_no, line in enumerate(lines, start=1):
                        if query in line:
                            matches.append(
                                {
                                    "path": item.relative_to(self.root).as_posix(),
                                    "line": line_no,
                                    "text": line,
                                }
                            )
                return {"ok": True, "data": {"matches": matches}}

            if call.name == "write_file":
                path = self.resolve_inside_root(str(call.arguments["path"]))
                if not approve(call):
                    return {
                        "ok": False,
                        "error": {"type": "ApprovalDenied", "message": "用户未批准写入"},
                    }
                path.parent.mkdir(parents=True, exist_ok=True)
                content = str(call.arguments["content"])
                path.write_text(content, encoding="utf-8")
                return {
                    "ok": True,
                    "data": {"path": path.relative_to(self.root).as_posix(), "bytes": len(content.encode())},
                }

            raise ValueError(f"未知工具：{call.name}")
        except (KeyError, OSError, ValueError) as exc:
            return {
                "ok": False,
                "error": {"type": type(exc).__name__, "message": str(exc)},
            }


class Agent:
    def __init__(self, model, tools: FileTools, trace_path: Path, max_steps: int = 15):
        if max_steps < 1:
            raise ValueError("max_steps 必须大于 0")
        self.model = model
        self.tools = tools
        self.trace_path = trace_path
        self.max_steps = max_steps
        self.trace_path.parent.mkdir(parents=True, exist_ok=True)
        self.trace_path.write_text("", encoding="utf-8")

    def trace(self, payload: dict) -> None:
        with self.trace_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")

    @staticmethod
    def signature(call: ToolCall) -> str:
        return json.dumps(
            {"name": call.name, "arguments": call.arguments},
            ensure_ascii=False,
            sort_keys=True,
        )

    def run(self, task: str, approve: Callable[[ToolCall], bool]) -> str:
        messages: list[dict] = [{"role": "user", "content": task}]
        previous_signature: str | None = None

        for step in range(1, self.max_steps + 1):
            reply = self.model.next(messages)
            self.trace(
                {
                    "event": "model_reply",
                    "step": step,
                    "plan": reply.plan,
                    "tool": reply.tool_call.name if reply.tool_call else None,
                    "arguments": reply.tool_call.arguments if reply.tool_call else None,
                    "final": reply.final,
                }
            )

            if reply.final is not None:
                self.trace({"event": "final", "step": step, "answer": reply.final})
                return reply.final
            if reply.tool_call is None:
                self.trace({"event": "stop", "step": step, "reason": "invalid_model_reply"})
                raise AgentStopped("invalid_model_reply")

            current_signature = self.signature(reply.tool_call)
            if current_signature == previous_signature:
                self.trace({"event": "stop", "step": step, "reason": "repeated_tool_call"})
                raise AgentStopped("repeated_tool_call")
            previous_signature = current_signature

            result = self.tools.execute(reply.tool_call, approve)
            self.trace(
                {
                    "event": "tool_result",
                    "step": step,
                    "tool": reply.tool_call.name,
                    "arguments": reply.tool_call.arguments,
                    "result": result,
                }
            )
            messages.append(
                {
                    "role": "assistant",
                    "tool_call": {
                        "name": reply.tool_call.name,
                        "arguments": reply.tool_call.arguments,
                    },
                }
            )
            messages.append({"role": "tool", "content": result})

        self.trace({"event": "stop", "step": self.max_steps, "reason": "max_steps"})
        raise AgentStopped("max_steps")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--trace", type=Path, default=Path("trace.jsonl"))
    parser.add_argument("--max-steps", type=int, default=15)
    parser.add_argument("--approve-writes", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script = json.loads(args.script.read_text(encoding="utf-8"))
    model = ScriptedModel(script["replies"])
    agent = Agent(model, FileTools(args.root), args.trace, args.max_steps)
    try:
        answer = agent.run("按脚本完成文件任务", approve=lambda call: args.approve_writes)
    except AgentStopped as exc:
        print(f"Agent 受控停止：{exc.reason}")
        return 2
    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

</details>

参考实现与上面的 `test_agent.py` 配套。它不是生产框架，而是把控制流暴露到最小程度，方便你看清每一条安全与可靠性纪律落在哪一行代码里。

## 13. 接真实模型时只替换哪里

保留 `FileTools`、`Agent`、测试和 trace，只实现：

```python
class ProviderModel:
    def next(self, messages: list[dict]) -> ModelReply:
        """把供应商当前 tool-use 响应适配成 ModelReply。"""
```

接入时以供应商当前官方文档为准，并增加三类集成测试：

1. 模型在不需要工具时能直接 final；
2. 工具报错后模型能换方法，而不是原样重复；
3. 写操作被拒后模型诚实报告未完成，不声称已经写入。

如果接入真实模型后你把路径校验、审批或停止预算搬进 prompt，说明架构退步了：这些控制必须留在代码侧。

## 14. 学习复盘

1. 哪些行为由模型决定，哪些必须由代码决定？
2. 重复调用熔断为什么在第二次执行前触发，而不是执行十次后再分析？
3. “工具报错”和“Agent 失败”有什么区别？什么情况下 Agent 可以换方法继续？
4. trace 中哪一个字段最能帮助你定位第一次偏离？
5. 如果把四个工具扩成四十个，哪一层会先出问题？为什么更好的默认不是“继续加工具”？

完成后再回到 [第 8 章 Agent 设计模式与架构](../08_Agent设计模式与架构.md)：此时你看到的 Pattern、Memory、MCP 和子 Agent，不再是名词，而是对这个最小循环的不同扩展。
