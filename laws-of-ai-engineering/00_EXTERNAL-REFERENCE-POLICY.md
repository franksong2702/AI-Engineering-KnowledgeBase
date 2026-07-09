---
type: reference-policy
aliases: [LawsExternalReferencePolicy, Laws外部引用口径]
date: 2026-07-09
course: laws-of-ai-engineering
abstraction_layer: 运营机制（外部引用口径）
stability: 中（Pilot 后形成，待全量核验固化）
tags: [AI工程, Laws, 外部引用, citation, 口径]
---

# Laws 外部引用口径

> 这页定义《Laws of AI Engineering》补 citation 的纪律。目标不是让每条 Law 看起来更“学术”，而是防止理论依据过度声称。

相关入口：[[laws-of-ai-engineering/00_INDEX|Laws 总索引]] · [[00_EXTERNAL-REFERENCES|Laws 外部依据说明]] · [[00_METADATA-SCHEMA|元信息字段说明]] · [[00_REFERENCE-POLICY|Laws 引用策略]] · [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT|外部引用核验 Pilot]]

## 一句话原则

> 外部来源支持到哪里，citation 就只能写到哪里；citation 默认进入 [[00_EXTERNAL-REFERENCES|Laws 外部依据说明]]，不进入每条 Law 正文；AI Engineering 的工程转译必须明说是转译。

## 来源类型

### 1. 直接理论依据

外部来源直接支持当前 Law 的理论依据。

例子：

- Goodhart's Law → Goodhart 原始论文 / 章节。
- Calibration → Brier score / calibration literature。
- Conway's Law → Conway 原文。

在引用说明文档里的写法：

```markdown
- `依据类型`: 直接理论依据
- `主要来源`: ...
- `使用边界`: ...
```

### 2. 工程转译依据

外部来源支持底层理论，但本库把它转译到 AI Engineering。

例子：

- 信息论支持有损压缩边界，但不是直接证明“LLM 一定在某个问题上幻觉”。
- 边际分析支持增量成本/收益判断，但不是直接证明“多采样一定边际递减”。

在引用说明文档里的写法：

```markdown
- `依据类型`: 工程转译依据
- `主要来源`: 来源 A
- `使用边界`: 来源 A 支持底层理论；本条是 AI 系统设计转译。
```

### 3. 类比依据

外部来源是严格理论，但当前 Law 只把它作为类比或上界提醒。

例子：

- 用停机问题提醒复杂自主系统不可完全事前验证。

在引用说明文档里的写法：

```markdown
- `依据类型`: 类比依据
- `使用边界`: 来源 A 支持底层不可判定性；本条不是严格归约。
```

### 4. 综合判断

没有单一外部来源直接提出这条 Law；它由多个外部事实、本库经验和跨书论证综合而成。

例子：

- “信任-可靠性剪刀差”可以由自动化过度信任、人因工程和 LLM 流畅度误导共同支持，但这个名字本身是本库综合命名。

在引用说明文档里的写法：

```markdown
- `依据类型`: 综合判断
- `使用边界`: 来源 A/B 支持组成部分；本条命名和 AI 工程归纳来自本库。
```

### 5. 新兴威胁模型

外部来源来自安全社区、标准组织、产业研究或新论文，尚未成为长期经典理论，但对当前 AI 工程有直接价值。

例子：

- Lethal Trifecta。
- Prompt injection agent security patterns。

在引用说明文档里的写法：

```markdown
- `依据类型`: 新兴威胁模型
- `主要来源`: 来源 A/B/C
- `使用边界`: 来源 A 提出术语；来源 B/C 支持风险链条。
```

## 支撑强度

只用四档：

| 档位 | 意思 | 处理 |
|---|---|---|
| 强 | 来源直接支持当前理论依据 | 可进入正式 citation 文档 |
| 中 | 来源支持底层理论，Law 是转译 / 投影 / 综合 | 可进入正式 citation 文档，但必须标边界 |
| 弱 | 来源只提供背景 | 不进入正式 citation 文档；保留审计意见 |
| 不支持 | 当前写法过度或错误 | 先改理论依据，再谈 citation |

## 禁止事项

- 不要为了“每条都有来源”而补弱 citation。
- 不要把博客当成经典理论来源；除非该博客是某个新术语的一手提出处。
- 不要把“工程转译”写成“论文直接证明”。
- 不要把类比依据写成数学归约。
- 不要未经核验改 Laws 正文。
- 不要用 citation 替代本库自己的适用边界和反例说明。

## 推荐呈现架构

默认采用“三层结构”：

1. **Law 正文层**：保持原有 12 段结构，不在每条 Law 里堆 citation。
2. **章节入口层**：每个 family 文件开头放一个默认折叠的 `cite` callout，指向本章外部依据。
3. **集中 citation 层**：所有来源、支撑强度、使用边界集中写在 [[00_EXTERNAL-REFERENCES|Laws 外部依据说明]]。

推荐章节入口格式：

```markdown
> [!cite]- 本章外部依据
> 研究型 citation、来源强度与工程转译边界见 [[00_EXTERNAL-REFERENCES#01 信息与压缩定律|本章外部依据说明]]。日常阅读可以忽略本块。
```

除非未来另行授权，**不要**在每条 Law 正文下新增 `外部依据` 段落。

## 全量核验流程

1. 先读当前 Law 的“理论依据”。
2. 判定来源类型。
3. 查找优先级来源：原始论文 / 权威教材 / 高引用综述 / 官方标准 / 可信产业一手资料。
4. 记录支撑强度。
5. 若支撑强度为强或中，才进入 [[00_EXTERNAL-REFERENCES|Laws 外部依据说明]]。
6. 若为弱或不支持，先写审计意见，不改正文，也不进入正式 citation 文档。
7. 每个 family 完成后运行：

```bash
python3 _tools/kb_health_check.py
```

## Pilot 结论

Pilot 10 条见 [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT|Laws 外部引用核验 Pilot]]；正式阅读入口见 [[00_EXTERNAL-REFERENCES|Laws 外部依据说明]]。当前裁决：可以继续全量核验，但 citation 默认进入集中说明文档，不自动写进每条 Law 正文。
