---
type: handbook-pattern
abstraction_layer: 方法（会随能力重洗）
date: 2026-07-06
course: multi-agent-patterns
pattern: dynamic-routing
family: 控制调度型
tags: [MultiAgent, 路由, 分诊]
---

# 模式 07 动态路由 Dynamic Routing

## 为什么存在

一个 prompt 想通吃所有输入类型，结果是"什么都会一点，什么都不精"——退款请求和技术故障需要完全不同的处理逻辑，塞进同一个 prompt 互相稀释。路由模式先**分诊**再**分发**：轻量 Router 判断输入属于哪类，交给该类的专属 Handler。**关注点分离 + 按需付费**（简单请求走便宜通道）。

## 适合解决什么问题

输入异构的服务型系统：客服（咨询/投诉/退款/技术）、内容审核（按违规类型分流）、代码请求（bug修复/新功能/解释）、模型成本分层（简单问题给小模型，难题给大模型——路由的特殊应用"model routing"）。判据：输入能被划分为 3-10 个处理逻辑显著不同的类别。

## Agent 如何协作

两层：Router（一次轻量调用，只做分类）→ Handler（各类别专属 Agent，深度处理）。Handler 之间互不知晓。进阶：Handler 发现分错了可以退回 Router 重分（一次为限）。

## 信息如何传递

原始输入 + Router 的分类标签与置信度 → 对应 Handler。**Router 不加工内容只贴标签**——它加工得越多，越容易引入偏见污染下游。Handler 的输出直接返回用户，不再经过 Router。

## 什么时候结束

Handler 完成即结束（单跳，天然有界）。异常：Router 置信度低于阈值 → 走默认通道或人工；Handler 拒收 → 重路由一次 → 再失败进死信队列。

## 优点

- 每个 Handler 的 prompt 短而专，质量和可维护性远超万能 prompt
- 成本精准：80% 的简单流量走便宜小模型
- 增量演化友好：新增类别 = 加一个 Handler + 更新 Router 标签集，不动存量
- Router 的分类日志本身是宝贵的业务数据（什么请求最多、什么在增长）

## 缺点

- **Router 是单点**：分错全错，且 Handler 通常无力发现自己收错了活
- 边界模糊的输入（一条消息既投诉又要退款）强行单标签会丢意图
- 类别体系会腐烂：业务演化后"其他"类占比悄悄涨到 40%
- 长尾类别的 Handler 维护成本高但调用量小

## Prompt 示例

（Router——注意置信度和"其他"的设计）

```
把用户消息分类到且仅到一个类别：
- refund: 退款退货诉求
- tech: 产品故障与使用问题
- billing: 账单扣费疑问
- complaint: 情绪性投诉（无具体诉求）
- other: 以上皆非
输出 JSON：{"category": "...", "confidence": 0-1, "signals": "分类依据的关键词",
"secondary": "若明显含第二意图则标注，否则 null"}
规则：confidence < 0.7 时宁可标 other；不要试图回答用户问题。
```

## Workflow 示例

```
用户消息流入
  → [Router] (小模型, ~0.3s) 分类+置信度
     ├─ confidence ≥ 0.7 → 对应 Handler
     │    ├─ [refund Handler] 查订单工具 + 政策库 RAG → 处理
     │    ├─ [tech Handler] 故障排查树 + 知识库 → 处理
     │    └─ ...
     ├─ confidence < 0.7 → [通用 Handler] 或人工队列
     └─ secondary ≠ null → 主 Handler 处理后追加提示"另检测到X需求"
监控：每周统计 other 占比与 Handler 拒收率 → 触发类别体系检修
```

## 未来还能如何改进

- **级联路由**：规则/正则先接住确定性流量（免费），拿不准的才进 LLM Router——大部分生产系统的正确形态
- **Handler 反馈闭环**：Handler 报告"这单不像我的活"，累积数据自动改进 Router 的 few-shot 示例
- **多标签路由**：复合意图派发给多个 Handler 并行处理再合并回复
- **在线学习路由**：用真实分类纠错数据微调专用小模型 Router，成本和延迟都降一个量级
