---
type: course-lab
aliases: [Textbook-Lab-05]
date: 2026-07-10
abstraction_layer: 技巧 + 方法（入门实验）
course: zero-to-agent
chapter: 5
lab: api-batch-pipeline
tags: [AI教程, API, 结构化输出, 重试, 断点续跑, 实验包]
---

# 第 5 章实验包：可恢复的 API 批处理流水线

> 配套章节：[第 5 章 API 编程与结构化输出](../05_API编程与结构化输出.md)。本实验先用本地 mock API 学会稳定的 HTTP、重试、结构化校验、checkpoint 和成本核算，再把唯一的客户端适配层替换为真实模型 API。

## 1. 为什么先用本地 mock API

直接从真实模型 API 起步，会把四类问题混在一起：

- 你的 Python/HTTP 代码错了；
- 密钥、余额或网络有问题；
- 供应商 SDK/接口版本变化；
- 模型输出本身不稳定。

本地 mock API 把后两类暂时拿掉，让你先证明管线可靠。实验通过后，真实供应商只替换 `LocalAPIClient`，checkpoint、重试、错误隔离和 metrics 不应重写。

## 2. 你要交付什么

一个读取 `input.jsonl` 的批处理程序：

```text
读取输入 → 校验 → 调 API → 校验结构化响应 → 写 output.jsonl
                                  └失败→ errors.jsonl
每条终态都写 checkpoint；每次运行写 metrics.json
```

### 机械完成标准

在本地 mock server 运行时，必须同时满足：

1. 首次运行处理 4 条输入：`output.jsonl` 恰好 3 行，`errors.jsonl` 恰好 1 行；
2. `retry-once` 第一次收到 429，程序自动退避后成功；`metrics.json` 的 `api_calls` 为 4；
3. `checkpoint.json` 记录 4 个终态 ID；
4. 原命令再运行一次，输出与错误文件行数不增加，`skipped` 为 4；
5. 代码库与日志中没有真实 API key。

## 3. 开始前自检

### 先修知识

- 已完成 [第 2 章实验包](02_Python文件整理器实验包.md)，会读写文件、JSON 和 traceback；
- 理解 HTTP 状态码、环境变量和“多轮对话由客户端维护”的基本概念；
- 知道为什么重试要求操作幂等。

### 预计时间

- 完成 mock 版本：4–6 小时；
- 再接一个真实供应商：额外 2–4 小时，取决于账号和网络环境。

### 环境检查

```bash
python3 --version
mkdir -p chapter05-api-pipeline
cd chapter05-api-pipeline
python3 -m venv .venv
source .venv/bin/activate
```

本实验的 mock 版本只使用 Python 标准库，不需要 `pip install`。

## 4. 交付物结构

```text
chapter05-api-pipeline/
├── .gitignore
├── mock_api.py
├── pipeline.py
├── input.jsonl
├── output.jsonl       # 运行后生成
├── errors.jsonl       # 运行后生成
├── checkpoint.json    # 运行后生成
└── metrics.json       # 运行后生成
```

`.gitignore`：

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

## 5. 本地 API：这部分直接使用

下面的 mock server 是实验设施，不是你要补的答案。它提供三个确定性行为：普通成功、`retry-once` 首次 429 后成功、空文本由客户端提前拒绝。

<!-- fixture-file: mock_api.py -->
```python
from __future__ import annotations

import json
from collections import defaultdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


ATTEMPTS: dict[str, int] = defaultdict(int)


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status: int, payload: dict, headers: dict | None = None) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:
        if self.path != "/v1/extract":
            self.send_json(404, {"error": "not_found"})
            return
        if self.headers.get("Authorization") != "Bearer local-demo-key":
            self.send_json(401, {"error": "invalid_api_key"})
            return

        length = int(self.headers.get("Content-Length", "0"))
        try:
            payload = json.loads(self.rfile.read(length))
            item_id = str(payload["id"])
            text = str(payload["text"])
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            self.send_json(400, {"error": "invalid_request"})
            return

        ATTEMPTS[item_id] += 1
        if item_id == "retry-once" and ATTEMPTS[item_id] == 1:
            self.send_json(429, {"error": "rate_limited"}, {"Retry-After": "0.05"})
            return

        words = [word.strip("，。！？,.!?") for word in text.split() if word.strip()]
        result = {
            "summary": text[:40],
            "tags": sorted(set(words[:3])),
            "confidence": "high" if len(text) >= 8 else "medium",
        }
        self.send_json(
            200,
            {
                "request_id": self.headers.get("Idempotency-Key", item_id),
                "data": result,
                "usage": {
                    "input_tokens": max(1, len(text) // 4),
                    "output_tokens": max(1, len(json.dumps(result, ensure_ascii=False)) // 4),
                },
            },
        )

    def log_message(self, format: str, *args) -> None:
        return


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8765), Handler)
    print("mock API: http://127.0.0.1:8765/v1/extract")
    server.serve_forever()
```

创建输入：

<!-- fixture-file: input.jsonl -->
```jsonl
{"id":"a1","text":"Agent 系统必须显式记录失败。"}
{"id":"retry-once","text":"限流是可重试错误，但重试必须有预算。"}
{"id":"a3","text":"结构化输出把模型结果变成程序可消费的数据。"}
{"id":"empty","text":""}
```

终端 A：

```bash
python3 mock_api.py
```

通过判据：看到本地地址，进程保持运行；不要关闭这个终端。

## 6. Starter：把可靠性留成 TODO

<!-- starter-file: pipeline.py -->
```python
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class APIError(RuntimeError):
    def __init__(self, status: int, message: str, retry_after: float | None = None):
        super().__init__(message)
        self.status = status
        self.retry_after = retry_after


class LocalAPIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.calls = 0

    def extract(self, item: dict[str, Any]) -> dict[str, Any]:
        # TODO: 用 urllib.request POST JSON；把 HTTPError 转成 APIError。
        raise NotImplementedError


def call_with_retry(client: LocalAPIClient, item: dict, max_attempts: int = 3) -> dict:
    # TODO: 只重试 RETRYABLE_STATUS；指数退避；超过预算显式失败。
    raise NotImplementedError


def load_jsonl(path: Path) -> list[dict]:
    # TODO: 逐行解析；空行跳过；重复 id 显式失败。
    raise NotImplementedError


def validate_response(payload: dict) -> dict:
    # TODO: 校验 data.summary/tags/confidence 与 usage。
    raise NotImplementedError


def run(args: argparse.Namespace) -> dict:
    # TODO: 恢复已处理 ID、逐条隔离错误、原子写 checkpoint、汇总 metrics。
    raise NotImplementedError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--base-url", default="http://127.0.0.1:8765")
    parser.add_argument("--output", type=Path, default=Path("output.jsonl"))
    parser.add_argument("--errors", type=Path, default=Path("errors.jsonl"))
    parser.add_argument("--checkpoint", type=Path, default=Path("checkpoint.json"))
    parser.add_argument("--metrics", type=Path, default=Path("metrics.json"))
    parser.add_argument("--input-rate-per-million", type=float, default=0.0)
    parser.add_argument("--output-rate-per-million", type=float, default=0.0)
    return parser.parse_args()


if __name__ == "__main__":
    os.environ.setdefault("LAB_API_KEY", "")
    metrics = run(parse_args())
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
```

先确认 Starter 至少能被解释器读取：

```bash
python3 -m py_compile pipeline.py mock_api.py
```

## 7. 分步任务与检查点

| 步骤 | 要做什么 | 机械检查 |
|---|---|---|
| 1 | `load_jsonl`：解析与重复 ID 检查 | 4 条输入被读入；手动复制一个 ID 后程序显式失败 |
| 2 | `LocalAPIClient.extract`：鉴权、JSON、超时、错误转换 | 普通输入得到 200；错误状态保留 status/body |
| 3 | `call_with_retry`：有限退避 | `retry-once` 发生 2 次调用后成功；永久错误不无限重试 |
| 4 | `validate_response`：结构契约 | 缺字段、错类型时进入 errors，不污染 output |
| 5 | checkpoint + 断点续跑 | 第二次运行不增加 output/errors 行数 |
| 6 | metrics | 成功/失败/跳过/API 调用/token/估算成本齐全 |

### 重试纪律

- 只重试 429、500、502、503、504 和瞬时网络错误；
- 400/401/403/422 属于请求或权限问题，原样重试通常没有意义；
- `max_attempts` 是**总尝试次数**，不是“失败后再试几次”；
- 每条请求带稳定的 `Idempotency-Key`；真实 API 是否支持该 header 要查官方文档，但你自己的业务写操作仍必须另做幂等保护。

### 成本口径

命令里的费率由使用者传入，不把任何供应商当前价格写死在教材：

```text
估算成本 = 输入 token / 1,000,000 × 输入费率
         + 输出 token / 1,000,000 × 输出费率
```

下面验证命令使用 `1` 和 `2` 作为**练习用编排值**，不代表任何供应商价格。

## 8. 首次运行与验收

终端 B：

```bash
export LAB_API_KEY=local-demo-key
python3 pipeline.py input.jsonl \
  --input-rate-per-million 1 \
  --output-rate-per-million 2
```

运行后检查：

```bash
python3 - <<'PY'
import json
from pathlib import Path

def lines(name):
    p = Path(name)
    return [x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]

metrics = json.loads(Path("metrics.json").read_text(encoding="utf-8"))
checkpoint = json.loads(Path("checkpoint.json").read_text(encoding="utf-8"))
assert len(lines("output.jsonl")) == 3
assert len(lines("errors.jsonl")) == 1
assert metrics["success"] == 3 and metrics["failed"] == 1
assert metrics["api_calls"] == 4
assert len(checkpoint["processed_ids"]) == 4
print("first-run verification: OK")
PY
```

再运行同一条 pipeline 命令，然后检查：

```bash
python3 - <<'PY'
import json
from pathlib import Path
metrics = json.loads(Path("metrics.json").read_text(encoding="utf-8"))
assert metrics["skipped"] == 4
assert len(Path("output.jsonl").read_text(encoding="utf-8").splitlines()) == 3
assert len(Path("errors.jsonl").read_text(encoding="utf-8").splitlines()) == 1
print("resume verification: OK")
PY
```

## 9. 常见失败：先分层再修

| 现象 | 属于哪层 | 排查顺序 |
|---|---|---|
| `Connection refused` | 服务/网络 | mock server 是否仍在 → URL/端口 → 防火墙 |
| 401 | 鉴权 | `echo "$LAB_API_KEY"` 是否为空 → header 是否为 Bearer → 不要打印完整真实 key |
| 429 后立即崩 | 恢复 | HTTPError 是否转成 APIError → status 是否在重试集合 → 预算是否大于 1 |
| 同一条输出重复出现 | 状态/幂等 | output/error 已有 ID 是否并入恢复集合 → checkpoint 是否原子写 |
| 一个坏输入让整批停止 | 错误隔离 | `try/except` 是否包在“单条处理”而非“整个批次”外层 |
| JSON 合法但字段不对 | 契约 | 是否只做 `json.loads` 而没做字段/类型校验 |
| 成本统计明显不对 | 度量 | token 来自响应 usage 还是自己猜 → 输入/输出费率是否颠倒 |
| 第二次运行仍调用 API | checkpoint | `processed_ids` 是否在处理前加载 → ID 类型是否一会儿数字一会儿字符串 |

不要用“多重 `except Exception: pass`”消灭报错。那会把可查失败变成静默污染。

## 10. 评分 rubric（100 分）

| 维度 | 分值 | 合格判据 |
|---|---:|---|
| HTTP 与鉴权 | 15 | 请求、header、超时、错误 body 可查 |
| 重试与预算 | 20 | 只重试瞬时错误；429 恢复；无无限重试 |
| 结构化契约 | 15 | 字段和类型都校验；坏响应进入错误流 |
| 断点续跑 | 20 | 第二次运行零重复；checkpoint 原子写 |
| 错误隔离 | 10 | 单条失败不终止整批；错误记录含 ID 与原因 |
| 度量与成本 | 10 | 调用/token/成本口径可解释，费率不写死 |
| 安全 | 10 | 无真实密钥入库；日志不打印完整密钥 |

- **合格（70–84）**：首轮与续跑验收通过；
- **良好（85–94）**：再覆盖坏 JSON、超时和 checkpoint 损坏；
- **优秀（95–100）**：把客户端替换成真实 API 后，管线其他代码无需改动，并保留同一套离线回归测试。

## 11. 参考实现

先完成并提交自己的版本，再展开。参考实现使用标准库 `urllib`，只对本地 mock API 的协议负责。

<details>
<summary>展开 pipeline.py 参考实现</summary>

<!-- reference-file: pipeline.py -->
```python
from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class APIError(RuntimeError):
    def __init__(self, status: int, message: str, retry_after: float | None = None):
        super().__init__(message)
        self.status = status
        self.retry_after = retry_after


class LocalAPIClient:
    def __init__(self, base_url: str, api_key: str, timeout: float = 3.0):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.calls = 0

    def extract(self, item: dict[str, Any]) -> dict[str, Any]:
        self.calls += 1
        body = json.dumps(
            {"id": str(item["id"]), "text": str(item["text"])},
            ensure_ascii=False,
        ).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url}/v1/extract",
            data=body,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "Idempotency-Key": str(item["id"]),
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            retry_after = exc.headers.get("Retry-After")
            raise APIError(
                exc.code,
                f"HTTP {exc.code}: {raw}",
                float(retry_after) if retry_after else None,
            ) from exc
        except urllib.error.URLError as exc:
            raise APIError(503, f"network error: {exc.reason}") from exc


def call_with_retry(
    client: LocalAPIClient,
    item: dict,
    max_attempts: int = 3,
    base_delay: float = 0.05,
) -> dict:
    for attempt in range(max_attempts):
        try:
            return client.extract(item)
        except APIError as exc:
            is_last = attempt == max_attempts - 1
            if exc.status not in RETRYABLE_STATUS or is_last:
                raise
            delay = exc.retry_after if exc.retry_after is not None else base_delay * (2**attempt)
            time.sleep(delay)
    raise AssertionError("unreachable")


def load_jsonl(path: Path) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
            item_id = str(item["id"])
            item["text"]
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            raise ValueError(f"{path}:{line_no} 输入格式错误：{exc}") from exc
        if item_id in seen:
            raise ValueError(f"{path}:{line_no} 重复 id：{item_id}")
        seen.add(item_id)
        item["id"] = item_id
        items.append(item)
    return items


def validate_response(payload: dict) -> dict:
    data = payload.get("data")
    usage = payload.get("usage")
    if not isinstance(data, dict) or not isinstance(usage, dict):
        raise ValueError("响应缺少 data 或 usage")
    if not isinstance(data.get("summary"), str):
        raise ValueError("data.summary 必须是字符串")
    if not isinstance(data.get("tags"), list) or not all(
        isinstance(tag, str) for tag in data["tags"]
    ):
        raise ValueError("data.tags 必须是字符串列表")
    if data.get("confidence") not in {"high", "medium", "low"}:
        raise ValueError("data.confidence 非法")
    for key in ("input_tokens", "output_tokens"):
        if not isinstance(usage.get(key), int) or usage[key] < 0:
            raise ValueError(f"usage.{key} 必须是非负整数")
    return payload


def read_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def jsonl_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    ids: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            ids.add(str(json.loads(raw)["id"]))
    return ids


def append_jsonl(path: Path, payload: dict) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        handle.flush()


def write_json_atomic(path: Path, payload: dict) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(path)


def run(args: argparse.Namespace) -> dict:
    api_key = os.environ.get("LAB_API_KEY", "")
    if not api_key:
        raise RuntimeError("缺少 LAB_API_KEY 环境变量")

    items = load_jsonl(args.input)
    checkpoint = read_json(args.checkpoint, {"processed_ids": []})
    processed = {str(value) for value in checkpoint.get("processed_ids", [])}
    processed |= jsonl_ids(args.output) | jsonl_ids(args.errors)

    client = LocalAPIClient(args.base_url, api_key)
    metrics = {
        "processed": 0,
        "success": 0,
        "failed": 0,
        "skipped": 0,
        "api_calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "input_rate_per_million": args.input_rate_per_million,
        "output_rate_per_million": args.output_rate_per_million,
        "estimated_cost": 0.0,
    }

    for item in items:
        item_id = str(item["id"])
        if item_id in processed:
            metrics["skipped"] += 1
            continue

        try:
            text = item.get("text")
            if not isinstance(text, str) or not text.strip():
                raise ValueError("text 必须是非空字符串")
            response = validate_response(call_with_retry(client, item))
            usage = response["usage"]
            append_jsonl(
                args.output,
                {
                    "id": item_id,
                    "result": response["data"],
                    "usage": usage,
                    "request_id": response.get("request_id"),
                },
            )
            metrics["success"] += 1
            metrics["input_tokens"] += usage["input_tokens"]
            metrics["output_tokens"] += usage["output_tokens"]
        except (APIError, ValueError) as exc:
            append_jsonl(
                args.errors,
                {"id": item_id, "error_type": type(exc).__name__, "message": str(exc)},
            )
            metrics["failed"] += 1

        processed.add(item_id)
        metrics["processed"] += 1
        write_json_atomic(args.checkpoint, {"processed_ids": sorted(processed)})

    metrics["api_calls"] = client.calls
    metrics["estimated_cost"] = round(
        metrics["input_tokens"] / 1_000_000 * args.input_rate_per_million
        + metrics["output_tokens"] / 1_000_000 * args.output_rate_per_million,
        8,
    )
    write_json_atomic(args.metrics, metrics)
    return metrics


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--base-url", default="http://127.0.0.1:8765")
    parser.add_argument("--output", type=Path, default=Path("output.jsonl"))
    parser.add_argument("--errors", type=Path, default=Path("errors.jsonl"))
    parser.add_argument("--checkpoint", type=Path, default=Path("checkpoint.json"))
    parser.add_argument("--metrics", type=Path, default=Path("metrics.json"))
    parser.add_argument("--input-rate-per-million", type=float, default=0.0)
    parser.add_argument("--output-rate-per-million", type=float, default=0.0)
    return parser.parse_args()


if __name__ == "__main__":
    metrics = run(parse_args())
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
```

</details>

## 12. 接真实 API 时只替换哪里

保留 `run`、checkpoint、错误流、metrics 与验收脚本，只新增一个真实供应商 adapter，实现同一个方法：

```python
class ProviderClient:
    def extract(self, item: dict) -> dict:
        """返回与 validate_response 契约一致的 payload。"""
```

实现时以供应商**当前官方文档**为准，不从本教材复制可能过时的 SDK 调用。接入后至少重新测试：

- 401/403；
- 429；
- 超时；
- 返回合法 JSON 但字段缺失；
- 中断后续跑；
- 费率变化时无需改代码，只改运行参数。

如果接真实 API 后你重写了整个 pipeline，说明客户端边界没有设计好。

## 13. 学习复盘

1. 哪些错误应该重试，哪些重试只是在重复浪费？
2. 为什么 output、errors 和 checkpoint 要共同参与恢复，而不能只信 checkpoint？
3. 如果程序在“写 output 后、写 checkpoint 前”崩溃，下一次会发生什么？你的设计防住了吗？
4. 结构化输出“JSON 合法”和“业务字段正确”为什么是两层不同的验证？
5. 当你把 mock adapter 换成真实供应商时，哪些文件不需要改？这就是接口设计的成绩单。

下一步：[第 7 章实验包](07_裸写文件Agent实验包.md) 会把这里的“调用—结果—恢复”升级为 Agent 循环，并加入工具权限、重复调用熔断与 trace。
