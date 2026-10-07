---
type: maintenance-protocol
abstraction_layer: 运营机制（定期重估）
date: 2026-07-09
course: ai-engineering-knowledge-base
status: calendar-sample-ready-not-installed
tags: [AI工程, 维护, 定期重估, 日历]
---

# 季度定期重估协议

> 目的：每季度用一句问题扫描方法层：**“如果模型强 100 倍，这条还成立吗？”**
>
> 本文只定义维护协议和可导入日历样例；不代表已经安装系统定时任务，也不代表已经写入真实日历。

## 1. 为什么需要定期重估

AI Engineering 知识库里有两类知识：

1. **慢变量**：例如可靠性、可验证性、不可逆性、古德哈特、责任边界。这些即使模型变强，也大概率仍成立。
2. **方法层技巧**：例如某些 prompting pattern、多 Agent 协作模式、推理组织方式、上下文管理做法。这些会被模型能力、上下文窗口、工具调用能力和成本结构改变。

季度重估只扫第二类，不重新审判整套知识库。

## 2. 重估范围

默认范围只包括两本方法层书：

- [《LLM Design Patterns》](llm-design-patterns/00_INDEX.md)
- [《Multi-Agent Patterns Handbook》](multi-agent-patterns-handbook/00_INDEX.md)

不默认扫描：

- [宪法](The-Constitution-of-AI-Engineering.md)：除非强模型或人明确提出 v2 立项。
- [Laws](laws-of-ai-engineering/00_INDEX.md)：Laws 是规律层，不按季度轻易改写。
- [Agent Decision System](agent-decision-system/00_PROTOCOL.md) 正式定义：只在上游核心定义变化后同步，不因季度例行检查直接改定义。
- [Case Library](ai-engineering-case-library/00_INDEX.md)：案例可作为证据，但不是本轮重估主体。

## 3. 分工边界

| 工作 | 可委托便宜模型 | 必须强模型或人裁决 |
|---|---:|---:|
| 收集疑似过时条目 | ✅ |  |
| 列出被新模型能力削弱的 pattern | ✅ |  |
| 找出与新书或新核心定义冲突的段落 | ✅ |  |
| 判断是否移入“历史区” |  | ✅ |
| 改写核心定义 |  | ✅ |
| 修改 ADS / Laws / 宪法 |  | ✅ |

一句话：**证据收集可以下放；移历史区和核心定义改写不能下放。**

## 4. 每季度执行步骤

1. 运行结构体检：

```bash
cd /path/to/AI-Engineering-KnowledgeBase   # 换成你本机的仓库根目录
python3 _tools/kb_health_check.py
```

2. 读取两本方法层书的 INDEX 与目录页：
   - `llm-design-patterns/00_INDEX.md`
   - `multi-agent-patterns-handbook/00_INDEX.md`

3. 对每个 pattern / 方法条目问四个问题：
   - 如果模型推理能力强 100 倍，这条还成立吗？
   - 如果上下文窗口和工具调用强 100 倍，这条还成立吗？
   - 如果模型调用成本下降 100 倍，这条还成立吗？
   - 如果这条不再默认成立，它是应该补“适用边界”，还是进入“历史区候选”？

4. 输出一份季度报告，建议命名：

```text
REEVALUATION_YYYY_QN.md
```

5. 报告只做裁决建议，不直接搬动章节。真正改写前必须由强模型或人确认。

## 5. 裁决标签

季度报告中的每个候选条目只使用下面四个标签：

| 标签 | 意思 | 允许自动改正文吗 |
|---|---|---:|
| `KEEP` | 仍是推荐方法，不改 | 否 |
| `BOUNDARY` | 仍有用，但需要补适用边界 | 否 |
| `HISTORY_CANDIDATE` | 可能应移入历史区 | 否 |
| `ESCALATE` | 影响核心定义或架构，需要强模型或人判断 | 否 |

注意：这些标签都不是自动改写授权。

## 6. 季度报告模板

```markdown
---
type: quarterly-reevaluation-report
abstraction_layer: 运营机制（定期重估报告）
date: YYYY-MM-DD
course: ai-engineering-knowledge-base
quarter: YYYY-QN
status: draft-for-human-or-strong-model-review
tags: [AI工程, 定期重估, 方法层]
---

# YYYY-QN 方法层季度重估

## 本轮范围

- [LLM Design Patterns](llm-design-patterns/00_INDEX.md)
- [Multi-Agent Patterns Handbook](multi-agent-patterns-handbook/00_INDEX.md)

## 结论摘要

- KEEP：N 条
- BOUNDARY：N 条
- HISTORY_CANDIDATE：N 条
- ESCALATE：N 条

## 候选明细

| 文件 | 条目 | 标签 | 证据 | 建议动作 |
|---|---|---|---|---|
|  |  | KEEP / BOUNDARY / HISTORY_CANDIDATE / ESCALATE |  |  |

## 不改动声明

本报告只是季度重估建议；未授权时不移动历史区、不改写核心定义、不修改 ADS/Laws/宪法。
```

## 7. 日历样例

可导入日历样例位于：

```text
_tools/ai-kb-quarterly-reevaluation.ics
```

默认设置：

- 从 **2026-10-01 09:30（Asia/Shanghai）** 开始；
- 每 3 个月重复一次；
- 事件标题：`AI KB 定期重估：模型强 100 倍这条还成立吗`；
- 时长 60 分钟；
- 只提醒“执行季度重估协议”，不自动运行脚本。

导入前请先打开 `.ics` 文件检查时间是否合适。若要改时间，直接改 `.ics` 里的 `DTSTART` / `DTEND`。

## 8. 完成定义

一次季度重估只有在下面三件事都完成时，才算完成：

1. 生成季度报告；
2. 强模型或人完成 `BOUNDARY / HISTORY_CANDIDATE / ESCALATE` 的裁决；
3. 若发生正文改动，重新运行 `python3 _tools/kb_health_check.py` 并记录验证结果。

如果只生成候选报告，没有裁决，不要把条目标记为“已重估完成”。
