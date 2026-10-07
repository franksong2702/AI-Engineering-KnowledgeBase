---
type: editorial-changelog
abstraction_layer: 运营机制（编辑修复记录归档）
date: 2026-10-07
course: ai-engineering-knowledge-base
tags: [AI工程, KnowledgeBase, 编辑审计, 变更记录]
---

# 编辑修复记录与已完成待办（归档）

> 本页由 [[01_编辑审计|编辑审计]] 于 2026-10-07 拆出（治理材料瘦身）。内容**原文迁移、未改写**，用于追溯"某处为什么长成现在这样"。
> 这里不是活任务队列。新任务只登记在 [[01_编辑审计#待办清单（后续批次的唯一有效位置，做完即勾）|编辑审计 · 待办清单]]；完成后，修复记录追加到本页第一节末尾，已勾选的待办移到第二节。

## 修复轮记录（2026-07-07，Fable 5 总审后的 P0/P1/P2）

- **P0（结构校对）**：自描述统一（当时口径十二本/131 文件，后随后续新书补齐更新为现状）；清除生成环境泄漏链接 13 处；决策系统与案例库 ID 引用全量校正；353 处 `[[00_INDEX]]` 歧义链接改为路径式；幽灵链接清零；14 个 INDEX 补 aliases。
- **P1（一致性）**：信息守恒收编为 LAW-13；C1/C2/C4 调和确认落地并回写状态；abstraction_layer 131/131 全覆盖；三本补充书定位诚实化；数字断言加"经验量级"标注、Laws"真实案例"改"典型案例"；R1/R2 正典指定按事实分工落地。
- **P2（内容增量）**：《Data Foundation》《Model Adaptation》全书扩写（工程手册/反例边界/验收清单，v1.0）；《Human-AI Collaboration》06–08 扩写；案例库 5 个深度版样板（Case 1/11/21/41/51）；教材 12 章自测题；`_tools/` 体检脚本与决策系统 YAML 编译器入库；Laws 全书试点 `stability` 字段。
- **P2 追加（2026-07-07 同日）**：新书《AI Systems in Production》（M4，6 Part，v1.0 直接按扩写标准写成），全库自描述同步为十三本/138 文件。
- **P2 追加二（2026-07-07 同日）**：《Human-AI Collaboration》其余 7 章（01–05/09/10）扩写完成，全书升 v1.0——补充四书全部达到扩写标准。
- **P2 追加六（2026-07-09，M3 新书）**：《Multimodal Systems》全书落地（INDEX + 6 章），第十五本书。按 `_governance/content/M3_MULTIMODAL_SCOPE_REVIEW.md` 立项边界执行：模态扩展层定位、只引用不新增定律、反模式具名不设 ID（Reference Policy 防串号条款的首次新书实践）。全库自描述同步 14→15 本 / 171→178 文件（README/总图/宪法/PROTOCOL/使用路径/学习路径），体检脚本口径同步。SIT-21 与多模态案例按立项审计要求推迟到独立批次（已入待办）。写作过程中体检抓到本书 3 处错链（Law 7 错指家族、Law 5 半角括号），已修——验证器对作者本人依然有效。
- **P2 追加五（2026-07-09，全库通读）**：主编级通读完成（Laws 11 族逐条深读 + 宪法 + Foundation/圣经/决策框架 + 教学/模式/警示/案例层抽样）。**修复**：35 处 Laws 跨文件死锚 `[[#Law N]]`（体检新增防回归检查）；9 处"定律 N"串号/错链（三套小清单互串——手册定律 1/2 错标 ×4、DP 定律 4/5 错链 ×2、"元指令"等错指 Laws INDEX ×3），REFERENCE-POLICY 已补防串号条款。**增量**：SIT-18 成本失控 / SIT-19 人机协作制度 / SIT-20 静默退化——三个缺口全部来自五本后补书籍，ADS 总条目 72→75，编译与交叉校验同步。**裁定**：宪法不立项 v2，落地 v1.1 边界注记（三个新命题指路不收编）。通读全程记录见 `_governance/fable5/FABLE5_深读笔记.md`。内容质量结论：全库无内容性错误，Laws/Foundation 是最高质量层，Foundation 第七章为全库最有原创价值的单章。
- **P2 追加六（2026-07-09，案例库双层维护 Batch A）**：五个原本缺旗舰样板的类别已各补一个深度版：[[ai-engineering-case-library/04_可靠性与生产#Case 31 · Demo 惊艳，生产翻车（深度版）|Case 31]]、[[ai-engineering-case-library/07_成本与性能#Case 61 · 简单任务也用最贵的模型（深度版）|Case 61]]、[[ai-engineering-case-library/08_记忆与上下文#Case 73 · 长任务上下文腐烂决策变差（深度版）|Case 73]]、[[ai-engineering-case-library/09_数据与模型定制#Case 81 · 想微调注入公司知识（深度版）|Case 81]]、[[ai-engineering-case-library/10_人机与产品决策#Case 91 · 全自动发布酿成公关事故（深度版）|Case 91]]。案例库现在 10 类各有一个深度旗舰样板；Batch B/C 是否继续作为后续增量另行判断。
- **P2 追加七（2026-07-09，案例库双层维护 Batch B/C）**：Batch B 已补齐后补五类的第二深度样板（Case 40/64/75/88/100）；Batch C 按保守口径给原有五类各加一个精选样板（Case 5/14/27/43/54），未写每组第二候选，避免超过“每类 1–2 个深度样板”的边界。案例库现为 100 案精简层 + 20 个深度样板（十类各 2 个），双层结构维护收束。
- **P2 追加八（2026-07-09，季度定期重估低风险方案）**：新增 [[QUARTERLY_REEVALUATION_PROTOCOL|季度定期重估协议]] 与 `_tools/ai-kb-quarterly-reevaluation.ics` 可导入日历样例；维护手册已补季度节奏。未安装系统定时任务，未写入真实日历；后续若要启用需手动导入或另行确认。
- **P2 追加九（2026-07-09，外部引用核验 Pilot）**：完成 Laws “理论依据”字段外部来源核验 Pilot 10 条（Law 1/4/6/16/24/26/39/52/84/88），产物为 [[_governance/laws/LAW_EXTERNAL_REFERENCE_AUDIT|Laws 外部引用核验 Pilot]] 与 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCE-POLICY|Laws 外部引用口径]]。本轮只核验与定口径，未改 102 条 Law 正文；全量 citation 项目仍未完成。
- **P2 追加四（2026-07-09）**：机器层收官——ADS 13 条 invariant 补 SOURCE 溯源行（含编译器 5 字段严格校验）；61 个中确信度 Law 候选逐条裁决完毕（22 升级/2 去链/37 保留为终态），顺带修正两处既有错锚（"上下文即状态"误指 Law 7、"数据处理不等式"误指系统与控制家族）；卡内 SOURCE 与并行产生的 PROTOCOL Source Map 逐条核对——12 条一致、LAW-10 按后者补齐为 Law 41+99，并声明主从（卡内=主来源机器版，PROTOCOL=含辅助来源人读版）。Law Reference System 至此真正收束。
- **P2 追加三（2026-07-08）**：新书《Human-AI Interaction Design》（M5，6 章，v1.0，Fable 5 主笔）；与 Collaboration 的边界对照表立于其 INDEX；全库自描述同步为十四本/158 文件；同轮审校本文（修"自declare"错字、补三段结构声明）。
- **P2 追加十三（2026-07-10，多模态操作层收束）**：M3 写完后补齐操作层闭环：新增 [[agent-decision-system/01_SITUATION-ROUTER#SIT-21 · 我在做多模态输入 / 截图 / 语音 / 视频驱动的 Agent|SIT-21 多模态输入情境]]；新增 [[ai-engineering-case-library/11_多模态系统|多模态案例分册]] Case 101–108（截图误点、OCR 关键字段、图片注入、语音旁人指令、视频抽帧、视觉不确定性、媒体日志隐私、过度授权）；案例库更新为 108 个案例。同步编译器与 ADS↔Case cross-reference guard 口径（21 个 SIT / 11 个案例类）。
- **P2 追加十四（2026-07-10，Core Laws 外部核验）**：完成 [[laws-of-ai-engineering/00_CORE-LAWS|18 条 Core Laws]] 的外部来源与表述边界核验，逐条矩阵见 [[_governance/laws/CORE_LAWS_EXTERNAL_REFERENCE_AUDIT|Core Laws 外部引用核验]]，正式来源集中写入 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCES|Laws 外部依据说明]]。裁决为 2 条直接强支持、8 条底层强支持加工程转译、8 条综合命题或条件性原则；本轮没有修改 11 个 Law family 正文。Law 12 与 Law 86 列为后续正文收窄 P0，另有 8 条列为 P1/P2；全量 102 条仍未核验。
- **P2 追加十五（2026-07-10，Core Laws P0 正典收窄）**：已完成 Law 12 / Law 86 正文改写与全库语义影响修复；Law 12 收窄为“存在客观、廉价、独立验证器时”的条件性工程原则，Law 86 改为问责不能止于 AI、自然人/法人按角色与语境分配。编号与 heading 不变，影响清单见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|P0 改写影响审计]]。Constitution 与 ADS invariant 在本批先登记，后续已由 B1.2 原子收束。
- **P2 追加十六（2026-07-10，P0 下游正典收束）**：Constitution `Law 1` 保留编号并改为“有可靠验证器时，验证可低于生成”；ADS 保留 `LAW-01` / `LAW-12` ID，分别改为“先设计可靠验证器”和“判断力稀缺，问责不能止于 AI”。同步 Source Map、Situation Router、Pattern Cards、Eval Checklist、7 个 Case heading 依赖（LAW-01 ×3、LAW-12 ×4）与 `_machine` 编译产物；旧主动表述清零，ADS 编译、Case cross-reference 与全库体检全部通过。
- **P2 追加十七（2026-07-10，Core Laws P1-A）**：Law 7 保留编号，heading 从“分布内可靠定律”改为“分布证据边界定律”；撤销“分布内近乎可靠”的充分条件错觉，改为可靠性证据不能自动跨分布外推、变化后必须重评。Constitution `Law 3`、ADS `LAW-03`、8 个 Case heading 依赖、机器 YAML 与全库高确信度转述已同步；详见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 影响审计]]。
- **P2 追加十八（2026-07-10，Core Laws P1-B）**：Law 84 / Law 95 保留编号与 heading，撤销两条“增长速率必然分叉”的过强断言。Law 84 改为信任/授权与实测可靠性的双向校准风险，Law 95 改为能力与可靠性必须分维度评价；Constitution `Law 8`、ADS `LAW-08`、Core 表、关系图与教学/应用层主动转述已同步。详见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 影响审计]]。
- **P2 追加十九（2026-07-10，Core Laws P1-C）**：Law 100 保留编号与 heading，性质改为“经济认识论综合命题”；撤销“判断力是唯一持续稀缺资源”“所有判断只能留给人”的强断言，改为生成降本后需按任务验证的判断瓶颈。Constitution `Law 10` 改为条件性表述，ADS 保留 `LAW-12` ID 并改为“关键判断显式化，问责不能止于 AI”；4 个 Case heading、Foundation 根命题与全库高确信度转述已同步。详见 [[_governance/laws/CORE_LAWS_P1_REWRITE_IMPACT_AUDIT|P1 影响审计]]。
- **P2 追加二十（2026-07-10，Law 96 相邻命题收窄）**：完成 [[_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT|Law 96 任务重组审计]]；保留编号，heading 从“抽象上移定律”改为“任务重组定律”，性质降为演化综合命题。新定义覆盖替代、增强、重组与新任务，不再预言人的工作必然持续上移；Foundation 与 Human-AI 的主动转述、Taxonomy heading 和集中 citation 已同步。
- **P2 追加二十一（2026-07-10，Core Laws P2-A）**：Law 64 保留编号与 heading，性质改为“科学哲学审计原则”；可证伪性收窄为经验性工程主张的审计纪律，不再充当所有知识的唯一定义。Laws INDEX / Core 表、Evaluation、Decision Frameworks、Foundation、Law 102 与集中 citation 已同步；详见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 影响审计]]。
- **P2 追加二十二（2026-07-10，Core Laws P2-B）**：Law 1 / Law 62 保留编号与 heading；Law 1 从“压缩单一导致幻觉”的硬因果说法收窄为参数生成没有内建事实来源保证，Law 6 单独负责实际压缩操作损失；Law 62 收窄为流畅、自信与专业不是正确性的充分证据，并可能诱发评价偏差。Constitution `Law 2`、ADS `LAW-02`、8 个 Case heading、机器 YAML 与教学/应用层主动转述同步；详见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 影响审计]]。
- **P2 追加二十三（2026-07-10，Core Laws P2-C）**：Law 74 保留编号与 heading，性质改为“条件性决策原则”；撤销“可逆性单独决定速度、审批和自主边界”的二元口号，改为后果、爆炸半径、恢复能力、不确定性、时间压力与等待信息价值共同分诊。Constitution `Law 9`、ADS `LAW-09`、PAT-18、8 个 Case heading、机器 YAML 及人机协作/交互/评价层主动规则同步；详见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 影响审计]]。
- **P2 追加二十四（2026-07-10，非 Core Laws 风险排序外部核验）**：按主动 heading 入链、强模态与安全/可靠性风险选出 18 条高影响非 Core Law，集中 citation 已写入 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCES|Laws 外部依据说明]]，全库去重覆盖提升到 **41/102**。其中 Law 47/72/79 保留正文，Law 2/3/21/25/30/31/36/41/42/63/71/76/77/92/99 共 15 条收窄：纠正 softmax、停机问题、可观测性/可控性、热力学熵等过度理论化解释，并撤销“必然退化、唯一手段、恢复应对一切、简单必然存活”等绝对措辞。编号与 heading 全部保留；Constitution、ADS、Foundation、Evaluation、Production、Anti-patterns、Multimodal 与 Human-AI 高确信度主动转述已同步。逐条裁决见 [[_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT|非 Core 风险排序核验]]；剩余 61 条回到季度候选池，不机械清零。
- **P2 追加二十五（2026-07-10，M6–M8 与 v1.0 收束）**：完成 [[_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW|M6–M8 立项与 v1.0 收束审计]]。裁决：M6 治理深化与 M7 组织采纳未来合并为一个组织级运行层，只有出现明确读者/组织场景、真实案例、法域边界和维护责任时才立项；M8 继续排除在正典外，只允许 dated snapshot。三者均不阻塞当前版本，知识库内容架构进入 v1.0 发布候选；本轮不创建 `v1.0` tag 或 GitHub Release。
- **P2 追加二十六（2026-10-07，总编辑 Review 低风险机械修复）**：①Constitution 开头删除过期的“179 文件 / 约 400 单元”口径（实际 203），文件数只在 README 维护一处；体检“自描述一致性”新增守卫：Constitution 与总图出现的文件数必须等于实际值（已做反向测试，可拦截）。②教材第 5/7 章示例代码的模型名改为可配置常量 `MODEL`（默认 `claude-sonnet-5-5`，可用 `ANTHROPIC_MODEL` 覆盖），并更正“system 也是 messages 中的 role”这一说法与 Anthropic API 不符之处。③Multi-Agent 手册选型决策树补“第 0 步：单 Agent / 工作流能否解决”，与手册“有罪推定”声明及教材 7.7 对齐。未改任何 Law / ADS / Constitution 定义。同轮 Review 的其余建议（教材 07-24/07-31 扩写补审校登记、Q4 季度重估逾期、治理材料瘦身、多 Agent 手册加厚、新系统形态覆盖、真实事故附录、v1.0 tag）待入队裁决。
- **P2 追加二十七（2026-10-07，教材扩写审校 + 2026-Q4 季度重估）**：①补审 07-24 扩写（8e07f25）与 07-31 iCloud 合并（b71107b → 15e824f，第 1/4 章以 iCloud 版为准）：12 章正文 Python 代码块全部能通过语法解析；六个配实验包章节的"项目"规格只做了标点规范化，实验包仍一一对应；修正 20 余处问题：pass@k 与 pass^k 混用（第 9 章）、"写出来的字就是思考的全部"缺 CoT 忠实性边界（第 3 章）、word2vec 类比与 LLM / RAG embedding 混用、"本质上是同一套计算"、"聪明几百万倍"（第 4 章）、Pydantic 可空字段注释错误与 SDK 重试叠加（第 5 章）、Contextual Retrieval 描述不准（第 6 章）、示例代码未设环境变量即崩（第 2 章）、"自主性与可靠性成反比"等绝对化措辞（第 8/10/11 章），并给新增数字补"经验量级"。教材 INDEX 不准确的"保持不变"说明已更正。②清除公开文档中的本机绝对路径（MAINTENANCE、季度协议、launchd 样例），体检"环境泄漏"新增 macOS 用户目录绝对路径守卫；`_tools/validation_*.log` 中仍有 11 个文件含该路径，随日志瘦身另行处理。③完成 [[_governance/reevaluation/REEVALUATION_2026_Q4|2026-Q4 方法层季度重估]] 报告（KEEP 27 / BOUNDARY 15 / HISTORY_CANDIDATE 3 / ESCALATE 3），待人裁决。全库文件数 203 → 204。
- **P2 追加二十八（2026-10-07，2026-Q4 重估 ESCALATE 三项执行）**：①LDP 与 Multi-Agent 手册的"跨模式定律"改称"跨模式原则"，现行文档 36 处引用（含 Laws 03/04 影响段与 REFERENCE-POLICY 防串号条款）同步，治理快照保留原文；体检新增旧称残留守卫。②新增 [[multi-agent-patterns-handbook/16_子Agent委派SubAgent|Multi-Agent 模式 16 子 Agent 委派]]，接入 INDEX 地图、决策树、成本表与教材 8.5；全库文件数 204 → 205。③长时程 / 编码 Agent 边界补在 LDP 的 ReAct、RAG、Context Compression、Planner-Executor 与 Multi-Agent Planner-Executor 五处。未改任何 Law 定义、ADS 定义或宪法。
- **P2 追加二十九（2026-10-07，2026-Q4 重估收尾）**：按维护者"全部按报告建议执行"的裁决，落地剩余 11 条 BOUNDARY 与 3 条 HISTORY_CANDIDATE：新建 [[llm-design-patterns/06_历史模式|LDP 历史模式]]，收录 Tree Search / ToT、Least-to-Most、Step-back 原文与退役说明；家族二第 5 节改写为"意图澄清"；两本方法层书的理由、边界、数字标注同步更新；Laws 02 与 Multi-Agent 03 中指向已退役模式的链接改指历史模式。全库文件数 205 → 206。ADS PAT-20 未改，另列待办。本轮季度重估完成。
- **P2 追加三十（2026-10-07，ADS PAT-20 改写）**：按维护者裁决，ADS PAT-20 由 Tree Search / ToT 改为 [[agent-decision-system/02_PATTERN-CARDS#PAT-20 · Generate-Verify Search（带外部验证器的生成-验证搜索）|Generate-Verify Search]]：只在存在客观、廉价、独立于生成过程的验证器时使用，明确排除"模型自评"；ID 不变，无 Case heading 依赖需迁移。`compile_decision_system.py`（76 条，严格校验 OK）、`check_ads_case_crossrefs.py` 与全库体检通过。

- **P2 追加三十一（2026-10-07，治理材料瘦身）**：①编辑审计拆分：原始审计（重复/矛盾/缺失/层级）原样保留；30 条修复记录与全部已完成待办原文迁至本页；待办清单标题不变（6 处外部锚点仍有效），只放未完成项，并补入总编辑 Review 尚未执行的 10 条建议（待裁决）。编辑审计从 260 行降到约 210 行，其中活队列约 30 行。②`_tools/validation_*.log` 65 个文件（约 304K）移出工作树并加入 `.gitignore`，历史可从 git 取回；验证证据改写在 PR 描述里。③README 首屏去掉内部治理用语，版本状态与 Laws 核验进度移到"维护与贡献"。④术语检查豁免表随文件拆分更新（19 + 12）。全库文件数 206 → 207。

- **P2 追加三十二（2026-10-07，v1.0 发布）**：按维护者裁决，依次以 merge commit 合并总编辑 Review 的 PR #3–#8（合并后 main 与 #8 分支内容逐字节一致，main 上 CI 通过），随后更新 README、REPO_STATUS 与 GOVERNANCE_INDEX 的版本状态，创建 `v1.0` tag 与 [GitHub Release](https://github.com/franksong2702/AI-Engineering-KnowledgeBase/releases/tag/v1.0)。待办清单中的"v1.0 tag / GitHub Release"一项已完成并移出。

### 补遗：原误置于待办清单标题下的三条记录

- **P2 追加十（2026-07-09，Laws citation 呈现架构）**：采纳“正文轻量入口 + 集中 citation 文档”的方案，新增 [[laws-of-ai-engineering/00_EXTERNAL-REFERENCES|Laws 外部依据说明]]，并在 11 个 Law family 文件开头加入默认折叠的 `cite` callout。原则：Law 正文不堆 citation；研究型阅读从集中入口进入。
- **P2 追加十一（2026-07-09，学习路径 / 使用路径收束）**：新增 [[03_使用路径与任务路由|使用路径与任务路由]]，把“长期怎么读”和“有具体任务时从哪里进入”分开：学习走 [[02_学习路径与未来扩展|长期学习路径]]，做事走 ADS，找样板走 Case Library，维护走 [[MAINTENANCE|维护手册]] 与本文待办清单。README 与总图已接入该入口。
- **P2 追加十二（2026-07-09，使用路径 Dogfood Audit）**：完成 [[_governance/usage-router/USAGE_ROUTER_DOGFOOD_AUDIT|使用路径与任务路由 Dogfood Audit]]，用 10 个真实任务验收“任务→使用路径→ADS→案例→书籍”链路。结论：8 个通过、1 个轻微摩擦（SIT-19 人机协作制度设计未进入常见任务一键入口）、1 个文案小错（“四种入口”实际 A–E 五类）。本轮先审计；随后低风险小修已完成：[[03_使用路径与任务路由#五种入口|五种入口]] 标题修正，且 [[03_使用路径与任务路由#我在设计人与 AI 的协作制度|SIT-19 人机协作制度设计入口]] 已补齐。

---

## 已完成待办归档（截至 2026-10-07）

**内容增量**
- [x] 🔴 P1-A《从零到 AI Agent 专家》关键章实验包——✅ 已完成（2026-07-10 至 2026-07-12）：第 2/5/7 章试点后，第 9/10/12 章继续补齐版本评测门禁、安全发布证据与毕业项目审计；六套实验包统一包含环境自检、可运行 Starter、分步任务、预期产物、故障排查、机械验收、100 分 rubric 与参考实现，参考代码均已从 Markdown 抽取并实际运行。课程 INDEX 与六章均已接入。技术可执行性已验证；真实零基础学习者试读因用户暂无时间未执行，教学有效性仍待后验观察。详见 [[_governance/content/BOOK_EXPANSION_PRIORITY_AUDIT|十五本书扩写优先级审计]]。
- [x] 🔴 P1-B《The Evaluation of AI Systems》端到端样板——✅ 已完成（2026-07-12）：新增 [[evaluation-of-ai-systems/08_端到端评价工程样板|实践附录]]，用研究助理 Agent 串联评价规格、开发/冻结数据、规则/Judge/人工评分器、Judge 校准、重复运行、发布门禁、生产回流与元评价；证据包审计器 5 项测试与样例集成验证通过。原七个理论 Part 保持不变。
- [x] 🔴 P1-C《Agent 圣经》五个能力契约样板——✅ 已完成（2026-07-12）：按 [[_governance/content/AGENT_BIBLE_P1C_SCOPE_AUDIT|立项审计]]分四批实施。收窄 INDEX 的“直接进生产”承诺；新增 [[agent-bible/contracts/00_INDEX|能力契约层]]与共享 schema；研究取证、独立事实核查、架构取舍、根因诊断、标准化评审共 5 个契约，含 50 个契约测试用例定义和 5 条终态 trace 样例；Markdown 严格编译到单一 machine JSON，体检接入同步、权限、ADS ID 与语义校验。当前未连接真实模型运行时，不把 fixture 校验表述成行为测试已通过。未新增 Agent/ADS 编号，未扩写其余十六个角色。
- [x] 🟡 案例库双层结构维护——✅ 已完成（2026-07-09）：保持 100 案广覆盖精简层，升级 20 个深度样板（十类各 2 个；清单见 [[ai-engineering-case-library/00_INDEX|案例库总索引]] 与 [[_governance/ads-case/CASE_LIBRARY_DOUBLE_LAYER_MAINTENANCE_AUDIT|候选审计]]）。未全量深度化，剩余 80 个案例保持快读层。
- [x] 🔴 M3《Multimodal Systems》新书——✅ 已完成（2026-07-09，Fable 5）：6 章 + INDEX，按立项审计边界执行（模态扩展层、编号纪律、止损判据自检通过）
- [x] 🟡 SIT-21（多模态输入情境）评估与实施——✅ 已完成（2026-07-10）：新增 [[agent-decision-system/01_SITUATION-ROUTER#SIT-21 · 我在做多模态输入 / 截图 / 语音 / 视频驱动的 Agent|SIT-21]]，编译器与交叉校验口径同步到 21 个情境
- [x] 🟡 多模态案例 5–8 个——✅ 已完成（2026-07-10）：新开 [[ai-engineering-case-library/11_多模态系统|11_多模态系统]]，补 Case 101–108 共 8 个精简案例，并接入 SIT-21 路由
- [x] 🔴 M5《Human-AI Interaction Design》新书——✅ 已完成（2026-07-08，Fable 5）：6 章 v1.0，边界对照表在其 INDEX（政策正典在 Collaboration，界面正典在本书）
- [x] 🔴 M6–M8 立项裁决——✅ 已完成（2026-07-10）：M6/M7 不分别写泛化新书，未来按触发条件合并为组织级运行层；M8 只做带日期和版本的任务型快照。三者均不阻塞 v1.0，详见 [[_governance/content/M6_M8_SCOPE_AND_VERSION_READINESS_REVIEW|收束审计]]。

**一致性深水区**
- [x] 🔴 Core Laws P0 正典收窄（Law 12 / Law 86）——✅ 已完成（2026-07-10）：两条正典与主动教学/应用正文已同步；Constitution 与 ADS invariant 的后续迁移也已由 B1.2 收束，详见 [[_governance/laws/CORE_LAWS_P0_REWRITE_IMPACT_AUDIT|影响审计]]。
- [x] 🔴 P0 下游正典收束（Constitution + ADS）——✅ 已完成（2026-07-10）：保留 Constitution `Law 1` 与 ADS `LAW-01/LAW-12` 编号，更新定义、全部 heading 依赖和机器 YAML；旧主动表述 0，编译/交叉引用/体检通过。
- [x] 🔴 Core Laws P1-A（Law 7）——✅ 已完成（2026-07-10）：保留 Law 7 / Constitution Law 3 / ADS LAW-03 编号，统一为“可靠性证据有分布边界”；旧主动表述 0，8 个 Case heading 已迁移，编译/交叉引用/体检通过。
- [x] 🔴 Core Laws P1-B（Law 84 / Law 95）——✅ 已完成（2026-07-10）：保留两条 Law heading 与 ADS LAW-08 ID；撤销必然增长速率断言，改为信任校准风险与能力/可靠性分维度评价；机器 YAML 与全库主动转述同步。
- [x] 🔴 Core Laws P1-C（Law 100）——✅ 已完成（2026-07-10）：保留 Law 100 heading 与 ADS LAW-12 ID；改为按任务验证的条件性判断瓶颈，明确可自动化判断与可问责关键判断的边界；4 个 Case heading、机器 YAML 与全库主动转述同步。
- [x] 🔴 Law 96 相邻命题审计——✅ 已完成（2026-07-10）：改为“任务重组定律”，保留 Law 96 编号并降为演化综合命题；外部依据、裁决和影响清单见 [[_governance/laws/LAW96_TASK_RECOMPOSITION_AUDIT|审计]]。
- [x] 🔴 Core Laws P2-A（Law 64）——✅ 已完成（2026-07-10）：保留编号与 heading，改为经验性工程主张的审计纪律；规范、定义、数学与启发式边界已明确，详见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 影响审计]]。
- [x] 🔴 Core Laws P2-B（Law 1 / Law 62）——✅ 已完成（2026-07-10）：保留两条 Law heading，拆开参数事实边界、运行时压缩损失与具体幻觉机制；Constitution / ADS / 8 个 Case heading 与主动转述已同步，详见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 影响审计]]。
- [x] 🔴 Core Laws P2-C（Law 74）——✅ 已完成（2026-07-10）：保留 Law 74 heading 与 ADS LAW-09 ID；多因素风险/恢复分诊已同步 Constitution、PAT-18、8 个 Case heading、HITL 与高影响应用层，详见 [[_governance/laws/CORE_LAWS_P2_REWRITE_IMPACT_AUDIT|P2 影响审计]]。
- [x] 🟡 Law Reference System 剩余中确信度候选分主题裁决——✅ 已完成（2026-07-09，Fable 5 逐条裁决 61 条）：22 处升级到具体 Law heading、2 处去链（"回归"被误锚统计回归均值，实为软件回归语境）、37 处裁决为**保留文件级**（复合概念/alias 过泛/跨多条 Law，裁决即终态，勿再重审）。停手条件已达成：high_confidence=0、changed_links=0、体检通过
- [x] 🟡 ADS `LAW-01`–`LAW-13` 与源 Law 的可追溯对照——已落到 [[agent-decision-system/00_PROTOCOL#LAW-INVARIANTS Source Map|00_PROTOCOL · LAW-INVARIANTS Source Map]]；未改 invariant 定义；机器格式仍由 `_tools/compile_decision_system.py` 校验
- [x] 🟢 决策系统 md 字段格式再收紧一档，`_tools/compile_decision_system.py` 从启发式解析升级为严格校验（解析失败即报错）（2026-07-08 已完成）

**运营机制**
- [x] 🔴 2026-Q4 季度重估裁决——✅ 已完成（2026-10-07）：3 条 ESCALATE、15 条 BOUNDARY、3 条 HISTORY_CANDIDATE 全部按裁决执行，详见 [[_governance/reevaluation/REEVALUATION_2026_Q4|报告的裁决记录]]。Swarm 留到 2027-Q1 复看。
- [x] 🟡 ADS PAT-20（Tree Search / ToT）同步——✅ 已完成（2026-10-07，维护者裁决：改为带外部验证器的搜索）：PAT-20 保留 ID，改写为"Generate-Verify Search"，八个字段与快速索引同步，机器 YAML 已重新编译；反模式 AP-54 中的成本链接改指 LDP 历史模式。
- [x] 🟢 体检脚本定时化（低风险版）——维护手册已入库，提供每周 launchd 样例但未安装；真正启用系统定时任务需另行确认（2026-07-08 已完成）
- [x] 🟢 Fable 5 架构收束建议入队——`_governance/fable5/FABLE5_架构收束REVIEW.md` 的可执行结论已归入本清单；该 Review 退役为治理快照（2026-07-08）
- [x] 🟢 README 文件地图与 Human-AI 横切定位收束（2026-07-08）
- [x] 🟢 MAINTENANCE 工具清单、命名规范、治理快照生命周期收束（2026-07-08）
- [x] 🟡 "定期重估"上日历——✅ 已完成（2026-07-09，低风险版）：[[QUARTERLY_REEVALUATION_PROTOCOL|季度定期重估协议]] 已入库，`_tools/ai-kb-quarterly-reevaluation.ics` 提供可导入日历样例；未安装系统任务、未写入真实日历。
- [x] 🟢 使用路径 Dogfood 小修——✅ 已完成（2026-07-09）：根据 [[_governance/usage-router/USAGE_ROUTER_DOGFOOD_AUDIT|Dogfood Audit]]，已把 [[03_使用路径与任务路由#五种入口|“五种入口”]] 标题修正，并在“常见任务的一键入口”补 [[agent-decision-system/01_SITUATION-ROUTER#SIT-19 · 我在设计人与 AI 的协作制度|SIT-19 人机协作制度设计]]；体检通过。
- [x] 🟡（可选）风险排序的外部引用核验——✅ 已完成（2026-07-10）：在既有 23 条基础上新增核验 18 条高影响非 Core Law，全库去重覆盖 **41/102**；15 条正典收窄、3 条保留正文，集中 citation 与下游主动转述同步。剩余 61 条为季度候选池，不机械清零；详见 [[_governance/laws/NON_CORE_LAWS_RISK_RANKED_EXTERNAL_AUDIT|风险排序核验]]。

**2026-10-07 补记**
- [x] 🟡 v1.0 tag / GitHub Release——✅ 已完成（2026-10-07）：见 P2 追加三十二。
