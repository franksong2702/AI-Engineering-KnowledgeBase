---
type: course-lab
aliases: [Textbook-Lab-02]
date: 2026-07-10
abstraction_layer: 技巧 + 方法（入门实验）
course: zero-to-agent
chapter: 2
lab: file-reporter
tags: [AI教程, Python, 实验包, 文件处理, Git]
---

# 第 2 章实验包：Python 文件整理器

> 配套章节：[第 2 章 Python 与开发环境速成](../02_Python与开发环境速成.md)。本页不再讲一遍 Python 语法，而是把章节项目变成一套可以独立完成、独立验收的实验。

## 1. 你要交付什么

写一个命令行工具，扫描指定目录并生成 Markdown 报告。报告至少包含：

- 文件总数与总字节数；
- 按扩展名统计的文件数与体积；
- 超过指定天数未修改的文件清单；
- 对无扩展名、嵌套目录、空目录和不存在目录的明确处理。

### 机械完成标准

下面三条必须同时满足：

1. `python3 -m unittest -v` 显示 5 个测试全部 `OK`；
2. `python3 file_reporter.py sample --days 30 --output report.md` 返回 exit 0，且生成 `report.md`；
3. `git log --oneline` 至少能看到 3 个有意义的阶段提交，而不是最后一次性提交。

“代码看起来差不多”不算完成。

## 2. 开始前自检

### 先修知识

- 会运行 Python 文件；
- 知道列表、字典、函数、`if/for`、`try/except` 的基本作用；
- 会执行 `git init/add/commit/log/diff`。

### 预计时间

- 有一点 Python 基础：2–4 小时；
- 完全零基础：6–10 小时，可以分两天完成。

### 环境检查

```bash
python3 --version
git --version
mkdir -p chapter02-file-reporter
cd chapter02-file-reporter
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip --version
git init
```

通过判据：Python 为 3.11 或更高版本；`python3 -m pip --version` 显示的路径位于当前 `.venv` 中。

## 3. 交付物结构

最终目录应接近：

```text
chapter02-file-reporter/
├── .gitignore
├── file_reporter.py
├── test_file_reporter.py
├── sample/
│   ├── notes/
│   │   └── a.md
│   ├── data/
│   │   └── items.json
│   └── README
└── report.md
```

`.gitignore` 至少包含：

```gitignore
.venv/
__pycache__/
*.pyc
```

不要把 `.venv` 提交进 Git。

## 4. Starter：先让测试变红

先创建下面两个文件。Starter 可以运行 `--help`，但测试会失败；这正是你要逐步修复的起点。

<!-- starter-file: file_reporter.py -->
```python
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FileInfo:
    relative_path: str
    suffix: str
    size: int
    mtime: float


def collect_files(root: Path) -> list[FileInfo]:
    """递归读取 root 下的普通文件，并返回相对路径。"""
    raise NotImplementedError("TODO: collect_files")


def summarize(files: list[FileInfo]) -> dict[str, dict[str, int]]:
    """按扩展名汇总 count 与 bytes。"""
    raise NotImplementedError("TODO: summarize")


def find_stale(files: list[FileInfo], cutoff_ts: float) -> list[FileInfo]:
    """返回修改时间早于 cutoff_ts 的文件。"""
    raise NotImplementedError("TODO: find_stale")


def render_report(root: Path, files: list[FileInfo], cutoff_ts: float) -> str:
    """生成 Markdown 报告。"""
    raise NotImplementedError("TODO: render_report")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="扫描目录并生成 Markdown 报告")
    parser.add_argument("root", type=Path)
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--output", type=Path, default=Path("report.md"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    # TODO: 校验参数、计算 cutoff、调用四个函数并写入输出文件。
    print("Starter 已就绪，请完成 TODO。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

<!-- starter-file: test_file_reporter.py -->
```python
import os
import tempfile
import unittest
from pathlib import Path

from file_reporter import collect_files, find_stale, render_report, summarize


class FileReporterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "nested").mkdir()
        (self.root / "a.md").write_text("abc", encoding="utf-8")
        (self.root / "nested" / "b.md").write_text("12345", encoding="utf-8")
        (self.root / "data.json").write_text("{}", encoding="utf-8")
        (self.root / "README").write_text("x", encoding="utf-8")
        os.utime(self.root / "a.md", (100, 100))

    def tearDown(self):
        self.tmp.cleanup()

    def test_collects_nested_files_with_relative_paths(self):
        files = collect_files(self.root)
        self.assertEqual(
            {f.relative_path for f in files},
            {"a.md", "nested/b.md", "data.json", "README"},
        )

    def test_summarizes_count_and_bytes(self):
        stats = summarize(collect_files(self.root))
        self.assertEqual(stats[".md"], {"count": 2, "bytes": 8})
        self.assertEqual(stats["[无扩展名]"]["count"], 1)

    def test_finds_stale_files(self):
        stale = find_stale(collect_files(self.root), cutoff_ts=101)
        self.assertEqual([f.relative_path for f in stale], ["a.md"])

    def test_renders_required_sections(self):
        report = render_report(self.root, collect_files(self.root), cutoff_ts=101)
        self.assertIn("# 文件扫描报告", report)
        self.assertIn("## 按扩展名统计", report)
        self.assertIn("## 过期文件", report)

    def test_missing_root_is_explicit_error(self):
        with self.assertRaises(FileNotFoundError):
            collect_files(self.root / "missing")


if __name__ == "__main__":
    unittest.main()
```

先运行：

```bash
python3 -m unittest -v
```

预期：测试失败并指出 `NotImplementedError`。如果连测试都没有被发现，先修文件名、工作目录或 import，不要开始写业务逻辑。

## 5. 分步任务与检查点

| 步骤 | 要做什么 | 机械检查 | 建议 Git 提交 |
|---|---|---|---|
| 1 | 完成 `collect_files` | 第 1、5 个测试通过 | `feat: scan files recursively` |
| 2 | 完成 `summarize` 与无扩展名规则 | 第 2 个测试通过 | `feat: summarize file types` |
| 3 | 完成 `find_stale` | 第 3 个测试通过 | 可与步骤 2 合并 |
| 4 | 完成 Markdown 渲染 | 第 4 个测试通过 | `feat: render markdown report` |
| 5 | 完成 CLI、参数校验与写文件 | 示例命令 exit 0 | `feat: add command line interface` |
| 6 | 人工增加一个权限错误或不可读文件测试 | 错误明确，不伪装成功 | `test: cover failure paths` |

约束：

- `root` 不存在或不是目录时，错误必须显式；
- 扫描顺序要稳定，报告中的表格和文件清单按字母排序；
- 扩展名统一转小写；无扩展名统一记为 `[无扩展名]`；
- 不要因为单个文件在扫描后被删除就让错误静默消失；要么报告错误，要么明确跳过并告警。

## 6. 准备样例数据

```bash
mkdir -p sample/notes sample/data
printf '# A\n' > sample/notes/a.md
printf '{"id": 1}\n' > sample/data/items.json
printf 'no suffix\n' > sample/README
python3 file_reporter.py sample --days 30 --output report.md
```

报告结构至少应为：

```markdown
# 文件扫描报告

- 扫描目录：`.../sample`
- 文件总数：3
- 总字节数：...

## 按扩展名统计

| 扩展名 | 文件数 | 字节数 |
|---|---:|---:|
| .json | 1 | ... |
| .md | 1 | ... |
| [无扩展名] | 1 | ... |

## 过期文件
```

不要逐字匹配示例中的绝对路径和字节数；它们依环境和样例内容变化。应匹配的是结构、统计逻辑和稳定排序。

## 7. 常见失败：按顺序排查

| 现象 | 常见原因 | 排查顺序 |
|---|---|---|
| `ModuleNotFoundError` | 不在项目目录运行；文件名拼错 | `pwd` → `ls` → 确认两个 `.py` 同目录 |
| `PermissionError` | 扫到无权读取的目录/文件 | 看 traceback 最后一行 → 确认是哪一个路径 → 决定显式失败还是记录后跳过 |
| 测试显示 0 个 | 文件名不是 `test_*.py`；测试类/方法未以 `test` 开头 | `python3 -m unittest discover -v` |
| `.MD` 和 `.md` 被分开 | suffix 未 `.lower()` | 打印两个文件的 suffix，修正规则 |
| 旧文件判断相反 | 把 `>` 和 `<` 写反 | 画时间线：`mtime < cutoff` 才是过期 |
| 报告每次顺序不同 | 依赖文件系统遍历顺序 | 对文件和统计 key 显式 `sorted()` |
| Git 出现几千个文件 | 把 `.venv` 加进暂存区 | 补 `.gitignore`，再 `git rm -r --cached .venv` |

纪律：把完整报错和触发输入留在学习日志里。只贴“它不工作”给 AI，会训练出你最不需要的调试习惯。

## 8. 评分 rubric（100 分）

| 维度 | 分值 | 合格判据 |
|---|---:|---|
| 正确性 | 30 | 5 个自动测试全过；统计结果正确 |
| 失败处理 | 15 | 不存在目录显式失败；至少覆盖一个运行时异常 |
| 报告可读性 | 15 | 标题、摘要、统计表、过期清单齐全且排序稳定 |
| 代码可读性 | 15 | 函数职责清楚；变量有意义；无整段复制重复 |
| 测试质量 | 15 | 覆盖嵌套、无扩展名、旧文件与错误路径 |
| Git 过程 | 10 | 至少 3 个阶段提交；能用 diff 解释变化 |

判定：

- **合格（70–84）**：功能和必测失败路径成立；
- **良好（85–94）**：错误处理、测试和提交过程都可信；
- **优秀（95–100）**：再增加命令行边界测试、不可读文件处理或人类可读的大小格式，且没有破坏简单性。

加功能不自动加分。为了“高级”引入数据库、Web UI 或 Agent 反而可能扣分。

## 9. 参考实现

先完成自己的版本并提交，再展开对照。参考实现只展示一种满足契约的写法，不是唯一答案。

<details>
<summary>展开 file_reporter.py 参考实现</summary>

<!-- reference-file: file_reporter.py -->
```python
from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FileInfo:
    relative_path: str
    suffix: str
    size: int
    mtime: float


def collect_files(root: Path) -> list[FileInfo]:
    root = root.expanduser()
    if not root.exists():
        raise FileNotFoundError(f"目录不存在：{root}")
    if not root.is_dir():
        raise NotADirectoryError(f"不是目录：{root}")

    files: list[FileInfo] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        stat = path.stat()
        files.append(
            FileInfo(
                relative_path=path.relative_to(root).as_posix(),
                suffix=path.suffix.lower() or "[无扩展名]",
                size=stat.st_size,
                mtime=stat.st_mtime,
            )
        )
    return files


def summarize(files: list[FileInfo]) -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = {}
    for file in files:
        bucket = stats.setdefault(file.suffix, {"count": 0, "bytes": 0})
        bucket["count"] += 1
        bucket["bytes"] += file.size
    return stats


def find_stale(files: list[FileInfo], cutoff_ts: float) -> list[FileInfo]:
    return sorted(
        (file for file in files if file.mtime < cutoff_ts),
        key=lambda file: file.relative_path,
    )


def render_report(root: Path, files: list[FileInfo], cutoff_ts: float) -> str:
    stats = summarize(files)
    stale = find_stale(files, cutoff_ts)
    lines = [
        "# 文件扫描报告",
        "",
        f"- 扫描目录：`{root.resolve()}`",
        f"- 文件总数：{len(files)}",
        f"- 总字节数：{sum(file.size for file in files)}",
        "",
        "## 按扩展名统计",
        "",
        "| 扩展名 | 文件数 | 字节数 |",
        "|---|---:|---:|",
    ]
    for suffix in sorted(stats):
        item = stats[suffix]
        lines.append(f"| {suffix} | {item['count']} | {item['bytes']} |")

    lines.extend(["", "## 过期文件", ""])
    if stale:
        lines.extend(f"- `{file.relative_path}`" for file in stale)
    else:
        lines.append("- 无")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="扫描目录并生成 Markdown 报告")
    parser.add_argument("root", type=Path)
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--output", type=Path, default=Path("report.md"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.days < 0:
        raise ValueError("--days 不能小于 0")
    files = collect_files(args.root)
    cutoff_ts = time.time() - args.days * 24 * 60 * 60
    report = render_report(args.root, files, cutoff_ts)
    args.output.write_text(report, encoding="utf-8")
    print(f"已生成：{args.output}（{len(files)} 个文件）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

</details>

参考实现应与上面的 `test_file_reporter.py` 配合运行。对照时不要只看代码长什么样，逐项回答：你的接口是否满足同一测试？你的错误是否更明确？你的版本有没有不必要的复杂度？

## 10. 学习复盘

完成后在学习日志回答：

1. 哪个失败是测试先发现、而不是你肉眼发现的？
2. 哪个函数最难定义输入输出？为什么？
3. Git 的哪一次提交最值得保留？如果没有 Git，你会怎样恢复？
4. 如果让 AI 写了大部分代码，你真正掌握的是哪一部分？拿掉 AI 后，你至少还能解释和修改什么？

下一章会把“清楚定义输入、输出和验收”升级成 Prompt 规格；到 [第 5 章实验包](05_API批处理流水线实验包.md)，同一套文件处理会接上 API、重试、checkpoint 和成本统计。
