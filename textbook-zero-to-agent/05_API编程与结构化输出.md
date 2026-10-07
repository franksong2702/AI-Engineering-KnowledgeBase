---
type: course-chapter
abstraction_layer: 技巧 + 方法（入门封装）
date: 2026-07-06
updated: 2026-07-24
course: zero-to-agent
chapter: 5
stage: 2
tags: [AI教程, API, 结构化输出]
---

# 第 5 章 API 编程与结构化输出

> 分水岭章节：从"使用 AI 产品"跨越到"用 AI 构建产品"。API（应用程序接口）让 LLM 从一个你聊天的对象，变成你程序里一个**可以被代码调用的组件**。之前你在网页里手动问，现在你写代码，让程序自动地问一千次、一万次，并把结果接住、处理、存储。

## 学习目标

- 独立完成 API 调用全流程：鉴权、发请求、处理响应、控制成本
- 让 LLM 稳定输出可被程序解析的结构化数据（JSON）
- 掌握生产级基本功：错误重试、流式输出、多轮对话的状态管理

---

## 5.1 一次 API 调用的解剖

调用 AI API 本质就是给对方服务器发一个 HTTP 请求，附上你的问题，收回它的回答。用官方 SDK 写出来大致长这样（以类 Anthropic/OpenAI 风格为例，各家 API 细节略有差异，以官方文档为准）：

```python
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])  # 密钥从环境变量读
# 模型名会随版本更新：写成可配置常量，以官方模型列表为准，不要散落在代码各处
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5-5")

resp = client.messages.create(
    model=MODEL,                        # 用哪个模型
    max_tokens=1024,                    # 最多生成多少 token（成本与长度的闸门）
    temperature=0,                      # 第 4 章的旋钮：0=稳定
    system="你是简洁的中文助理。",       # system prompt：持久规则
    messages=[
        {"role": "user", "content": "用一句话解释什么是 API"}
    ],
)
print(resp.content[0].text)
print(resp.usage)   # 里面有 input_tokens / output_tokens——你的成本凭据
```

几个必须理解的部件：**endpoint**（你请求的地址，SDK 帮你填好了）、**API key**（你的身份凭证，务必环境变量存放）、**messages 数组**（对话历史，每条有 `role`：user / assistant；system prompt 在 Anthropic API 里通过单独的 `system` 参数传，OpenAI 风格则作为 `role: system` 的消息）、**max_tokens**（输出上限）、**temperature**（随机性）。

这里有一个第 1 章就埋下、现在必须彻底理解的核心认知：**多轮对话 = 每次把完整历史重发一遍，服务端是无状态的。** 你想让模型"记得"上一句，就得把上一轮的 user 和 assistant 消息都放进 `messages` 里一起发过去。服务器不替你存任何东西。

## 5.2 结构化输出：从"请求 JSON"到"强制 JSON"

第 3 章你学会了在 prompt 里"请"模型输出 JSON。但"请"意味着它**可能不从**——偶尔多写一句"好的，这是您要的 JSON："，你的程序解析就崩了。生产系统受不了这种偶发失败。

升级方案是**结构化输出 / schema 强制**。你用 Pydantic（Python 的数据校验库）先定义好你要的数据长什么样，把这个 schema 交给 API，得到的输出**保证是合法、符合结构**的对象：

```python
from pydantic import BaseModel

class JobInfo(BaseModel):        # 定义你要的数据结构
    title: str
    company: str
    salary_range: str | None     # 允许值为 null（字段本身仍须出现；想让字段可省略要再加默认值 = None）
    skills: list[str]

# 把 JobInfo 的 schema 传给支持 structured outputs 的 API，
# 模型的输出会被约束成这个结构，你直接拿到一个 JobInfo 对象。
```

体会这个升级的本质：**从"请求"变成了"契约"。** 前者你要写一堆容错代码去解析可能不合规的文本；后者输出合法是被保证的。**这正是所有工具调用（第 7 章）的基础**——Agent 要调工具，靠的就是模型输出一个结构严格的"调用请求"。

关于缺失值有个实操要点：一定要在 schema 和 prompt 里明确"**没有的信息填 null，禁止推测**"，否则模型会为了填满字段而编造（幻觉）。

## 5.3 错误处理现实主义：网络一定会出问题

在本地跑通了不代表能上线。真实的 API 会**超时、限流（返回 429）、过载（返回 529）**。你的代码必须假设这些一定会发生。

标配武器是**指数退避重试（exponential backoff）**：失败了别马上重试（那只会加剧拥堵），而是等 1 秒、再失败等 2 秒、再等 4 秒……逐步拉长间隔，并设一个最大重试次数：

```python
import time
from anthropic import APIStatusError

def call_with_retry(fn, max_retries=5):
    for attempt in range(max_retries):
        try:
            return fn()
        except APIStatusError as e:
            if e.status_code in (429, 529) and attempt < max_retries - 1:
                wait = 2 ** attempt          # 1, 2, 4, 8... 秒
                time.sleep(wait)
                continue
            raise                            # 不可重试的错误，或次数用尽，抛出
```

两点补充：一是官方 SDK 通常**已内置**对 429/5xx 的自动重试（可用 `max_retries` 参数调整），自己再包一层时要算清总次数，别重试叠重试；二是生产里的等待时间要加一点**随机抖动（jitter）**，避免大量客户端在同一时刻一起重试。

还有一个前提概念必须配套：**幂等（idempotent）**。重试意味着同一个操作可能被执行两次。如果操作是"读一段文本"，执行两次无害；但如果是"给用户扣款"，重试就会扣两次钱。所以**只对幂等的、可安全重复的操作做自动重试**，非幂等操作要额外设计防重（如去重 ID）。

## 5.4 成本工程：上线前的那道乘法

这是最容易被新手忽略、却最容易杀死项目的一环。成本 = 输入 token + 输出 token（各有单价）。危险在于**规模**：

> 单次成本 × 日调用量 = 真实账单

一个 demo 里单次花 5 毛钱的功能，感觉很便宜。但如果上线后每天被调用 10 万次，就是**每天 5 万元**。很多"好主意"就死在这道乘法上。**所以成本估算是设计阶段的事，不是上线后才算。**

两个降本杠杆要知道：

- **Prompt caching（提示缓存）**：如果你每次请求都带一大段相同的前缀（比如很长的 system prompt 或固定的参考资料），可以把这段缓存起来，重复使用时大幅降价。**推论：把固定不变的内容放在 prompt 开头，让它可被缓存。**
- **批处理 API**：如果任务不急（可以等几小时），用批处理接口通常能换到约半价。

## 5.5 流式输出：改善体感，不改善总量

**流式输出（streaming）**是让模型逐 token 地把回答"吐"出来，像打字机一样，而不是憋到全部生成完才一次性返回。

它改善的是**体感延迟**：用户等待的从"总生成时长"变成了"首个 token 出现的时长"——哪怕总共要 10 秒，用户 0.5 秒就看到字开始蹦出来，感觉快多了。

但要清醒：它**不改善总耗时，也不改善成本**。总的 token 数、总的计算量、总的钱一分不少。它纯粹是个体验优化。

## 5.6 SDK vs 裸 HTTP：理解一次，日常用 SDK

你可以用最原始的方式（裸 `requests.post` 拼 HTTP）调 API，也可以用官方 SDK。区别是：SDK 已经帮你处理好了重试、流式、鉴权、错误类型这些**脏活累活**。

建议：**亲手用裸 HTTP 调通一次**，理解底层到底发生了什么（请求头、请求体、响应结构）；理解之后，**日常一律用 SDK**——重复造轮子没有意义，而且你自己造的轮子多半没 SDK 稳。

---

## 练习

1. 完成第一次 API 调用：发"你好"，打印响应对象的每个字段并解释含义（包括 usage 里的 token 数）。
2. 写一个命令行聊天程序：维护 messages 列表实现多轮记忆，加一个 `/clear` 命令清空历史——亲手实现"记忆"，破除对话有状态的错觉。
3. 结构化抽取：给 5 段招聘启事文本，用 schema 强制输出 `{职位, 公司, 薪资范围, 技能要求[]}`，处理"薪资没写"的缺失情况。
4. 故意触发限流（快速循环调用），实现指数退避重试装饰器。
5. 计算你第 3 题项目跑 10000 次的成本，再用 prompt caching 思路优化 prompt 结构，重新计算。

## 项目

**批量文本处理流水线**：选一个真实数据源（如你收藏的 50 篇文章、或导出的聊天记录），构建一个脚本：读取 → 分批调 API 做结构化抽取（摘要、标签、实体）→ 存为 JSON/CSV → 生成统计报告。硬性要求：有重试和断点续跑（中断后不重复处理已完成的）、有成本统计、错误的条目单独记录而不是让整个流水线崩掉。这三个要求就是生产系统的缩影。

> [!tip] 配套实验包
> [打开《可恢复的 API 批处理流水线实验包》](labs/05_API批处理流水线实验包.md)：先用本地 mock API 验证 HTTP、429 退避、结构契约、checkpoint、错误隔离和成本口径，再只替换客户端适配层接真实 API。

## 阅读资料

- Anthropic API 文档 + OpenAI API 文档——精读 messages、tool use、structured outputs 章节
- OpenAI Cookbook（github.com/openai/openai-cookbook）——工程模式的示例库
- Pydantic 官方文档的基础部分——schema 定义的事实标准
- 任选一家的 prompt caching 文档——成本工程的关键杠杆

## 容易犯的错误

- **API key 泄露**：写死在代码里、提交到 GitHub、贴在提问帖里。永远用环境变量，泄露立即轮换。
- **用正则从散文里抠 JSON**：不用 JSON mode/structured outputs，靠字符串处理硬解析，脆弱且不必要。
- **无限重试或不重试**：前者放大故障（还烧钱），后者一次网络抖动就崩。指数退避 + 最大次数 + 只重试可重试的错误码。
- **对话历史无限增长**：多轮应用不做截断/摘要，越聊越贵越慢，最后超窗口报错。
- **先写完再算成本**：规模化后才发现单价不可行。成本估算是设计阶段的事。

## 推荐 Prompt

（这是给你项目里 LLM 调用的示例——注意它同时用了角色、规则、格式契约、缺失值约定）

```
你是数据抽取引擎。从输入文本中抽取字段，严格按 schema 输出 JSON。
规则：
- 文本中没有的信息填 null，禁止推测
- 不确定时在 confidence 字段标 low
- 只输出 JSON，无任何解释文字
```

## 推荐 Agent

- **Claude Code / Cursor**：本章起成为主力开发环境。练习让它写流水线骨架，你负责 review 重试逻辑和成本计算——这两处最容易被 AI 写得似是而非
- **API Playground / Console**（Anthropic Workbench、OpenAI Playground）：调参数看效果的最快途径，先 playground 验证再写代码

## 自测题

1. **"多轮对话 = 每次把完整历史重发一遍"——这个事实推出哪两个工程结论？**
   要点：①长对话成本线性膨胀（要压缩/截断历史）；②"记忆"必须自己管理（服务端无状态），想让它记住就得显式重注入。
2. **从"prompt 里求 JSON"升级到 schema 强制的本质区别是什么？**
   要点：前者是请求（模型可能不从，要容错解析），后者是契约（输出保证合法）——把 LLM 从聊天对象变成软件组件。
3. **遇到 429 的标准处理是什么？为什么幂等设计是它的前提？**
   要点：指数退避重试；重试可能造成同一操作执行两次，非幂等操作（如重复扣款）重试反而制造事故。
4. **上线前的"那道乘法"是什么？举例说明它怎么杀死一个好主意。**
   要点：单次成本 × 日调用量；单次 0.5 元的功能日调用 10 万次 = 每天 5 万元——demo 很棒、规模化不可行。
5. **流式输出改善的是什么指标？它不改善什么？**
   要点：改善体感延迟（首 token 时间）；不改善总耗时和成本。
