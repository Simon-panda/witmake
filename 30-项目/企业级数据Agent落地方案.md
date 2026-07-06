---
title: 从AI取数到智能分析：机加工企业数据Agent多阶段演进与工程化落地方案
created: 2026-07-05
updated: 2026-07-05
type: project
domain: 工程
tags: [AI, agent, text-to-sql, 数据管道, 方案, 语义模型, Skill]
sources: [raw/articles/infoq-data-agent-2026-07.md]
confidence: high
---

# 从AI取数到智能分析：机加工企业数据Agent多阶段演进与工程化落地方案

> **来源**：InfoQ《从 AI 取数到智能分析：企业级数据 Agent 的多阶段演进与工程化落地》
> **编制日期**：2026-07-05
> **适用对象**：机加工制造企业（200台CNC规模）
> **关联文档**：[[产线数据管道架构]] | [[OEE分析体系]] | [[日报分析系统]]

---

## 目录

- [第一部分：原文收录](#第一部分原文收录)
- [第二部分：机加工企业数据现状诊断](#第二部分机加工企业数据现状诊断)
- [第三部分：总体方案架构](#第三部分总体方案架构)
- [第四部分：分阶段实施方案](#第四部分分阶段实施方案)
- [第五部分：关键技术设计](#第五部分关键技术设计)
- [第六部分：组织与运营保障](#第六部分组织与运营保障)
- [第七部分：投入产出分析](#第七部分投入产出分析)
- [第八部分：风险与应对](#第八部分风险与应对)
- [附录：工具链与参考资源](#附录工具链与参考资源)

---

# 第一部分：原文收录

> 以下为 InfoQ 原文完整转载，作者 QCon。

## 1 背景与挑战：从BI演进到AI原生数据消费

数据消费的发展通常被划分为四个阶段。1.0时代是传统BI时代，以SAP等系统为代表，报表交付高度依赖IT团队通过编写SQL来实现。2.0时代迈入了自助式BI，Dashboard成为主流。以我所在公司的数据平台为例，Dashboard的月活大约有两万多，但在这两万多用户中，只有不到百分之十是数据的生产者，也就是报表的编辑者。这说明绝大部分人的数据消费，依然要指望着少数的BI同学进行手工操作。到了3.0的增强分析时代，开始引入AI作为辅助，但主要的分析流程依然由人驱动。而现在，我们正大踏步跨入4.0——AI原生Agent时代。在这个阶段，数据消费者终于可以直接通过自然语言提交需求，Agent则能够自主完成从取数到智能分析的全过程。

我们团队对AI取数的探索始于2024年。起初，我们对Text-to-SQL这条路信心满满，因为学术界当时的Benchmark数据非常亮眼。在Spider这类榜单上，一些State-of-the-art的解决方案准确率可以达到85%到91%，这甚至已经接近了人类标注员的水平。基于这份信息，我们设计了一个初代Text-to-SQL的Demo架构，不到一周就完成了搭建。当时的技术方案采用了典型的RAG链路：我们把平台上近三十天内有访问记录的大约一百万张表做了Embedding索引，用户提问后，系统通过向量近似检索召回相关的表，然后利用这些表的元数据构造Prompt，交给大模型一步生成SQL。

然而，这套方案上线后的效果非常差。我们构造了一个内部评测集来摸底，甚至还是简化版本的评测集。但就在这个评测集上，找表的平均倒数排名仅能达到56%左右，而Text-to-SQL的执行准确率更是不到40%。更令人沮丧的是，就连最基本的语法准确率也徘徊在百分之五六十。差不多同一时间，Spider发布了2.0版本的Benchmark，这个新版本号称是基于企业真实OLAP场景构造的评测集。当时比较先进的商业化模型GPT-4o，其裸模型在Spider 2.0上能达到的准确率只有百分之十左右。结合Spider 2.0的这个数据和我们的初版实践，我们得出了一个残酷的结论：**企业级OLAP场景下的Text-to-SQL，是一件极其困难的事情。**

## 2 Text2SQL技术演进之路

面对前期的技术难点，我们对初代Demo和种子用户的负反馈进行了深入分析，归纳出了五大核心问题。**第一是找表不准。** 数仓有着严格的分层，每一层之间和内部都存在大量结构相似、只有细微区别的表。对于Embedding模型来说，通过语义相似性检索去区分这种微弱的差异是非常困难的，结果往往会召回看起来相关但实际上完全错误的表。**第二是SQL语义错误。** 第一版架构仅仅使用了表元数据，严重缺失了业务规则和数据口径，导致生成的SQL虽然能跑出结果，但计算逻辑和数据结论完全不对。**第三是SQL语法错误。** 大模型经常会混用MySQL、PostgreSQL等专有语法，而我们的底层引擎是Presto或StarRocks，这些不兼容的语法会导致SQL直接报错。同时，模型幻觉也频繁出现，比如编造出表中根本不存在的数据列，甚至引用其他表的列。**第四是交互体验差。** 系统里的找数、取数等功能入口各自独立，用户需要在不同模块间来回切换，体验感很差，系统响应时间也慢。**第五是评测缺失。** 我们当初只构造了一个仅包含五十多条数据的极简评测集，完全脱离了生产环境，即便把Agent调校到很高的分数，也不敢放心交给业务使用。

带着这五大核心问题，我们开启了Text-to-SQL的技术演进之路。这段路可以总结为五次关键的跃迁，每一次都由真实的生产痛点所驱动。

### 2.1 第一次跃迁：Multi-Agent + 元数据渐进式披露

第一次跃迁是从单链路RAG转变为Multi-Agent加元数据渐进式披露的解决方案，主要解决找数和体验割裂的问题。

其核心设计在于Multi-Agent架构。系统被分为两层。**上层是Supervisor Agent**，负责背景知识加载、意图识别以及任务的拆解与编排，然后把具体任务交接给下层的专业子Agent。**下层是专业Agent层**，包含了三个关键角色：Data Scope Clarity Agent负责确认用户问题归属的数据域；Data Discovery Agent负责在已确认的数据域内精准找到相关的表；而生成SQL的Agent则基于已确认的表元数据和业务知识，完成最终的SQL生成。

在这个过程中，我们加入了两层**Human-in-loop机制**。在Data Scope Clarity Agent找到业务域后，会引入用户确认环节；在Data Discovery Agent找到相似表后，同样会引入用户确认。只有用户确认通过，Agent才会进入下一步。这种两层确认体系能够确保Agent的推理过程不走偏。

另一个重点设计是**元数据的渐进式披露**。传统的RAG系统习惯于一次性通过相似性检索召回所有候选信息，但假设召回了十几张表，每张表又有上百个字段，如果把这些表描述、Schema和列描述全部塞进上下文，真正有价值的信息可能只占其中一到三张表，这会造成极大的上下文浪费和严重的上下文腐化问题。

针对这点，我们引入了三层元数据披露逻辑：
- **第一层：业务域定位** — 基于意图识别和公司已有的业务域基础元数据，直接在百万级表中定位出用户问题所命中的数据域，将范围从百万级缩小到域内的数百张表。
- **第二层：域内表发现** — 基于语义检索、热度排名，结合表的语义规则，从数百张表中进一步挑选出候选表并交由用户确认。
- **第三层：深度知识展开** — 只有当用户确认后，才加载这些候选表的完整Schema、字段和关联业务规则。

找到了正确的表之后，流程进入**SQL生成阶段**。整个生成Workflow被拆分为四个步骤：第一步引入歧义和缺失检测；第二步多路并行生成候选SQL（自校正模式、任务分治模式、简单直接生成模式）；第三步选优环节，由Agent从中挑选出最优的一个；第四步验证和修复，先用SQL编译器验证语法错误，修复后再交出可执行的SQL。

为了支撑高质量生成，我们将相关的上下文信息分为四层：
1. **Hive表元数据** — 表名、表描述、字段名、字段描述等基础信息
2. **业务域知识文档（Mart）** — 仓库建模介绍、数据使用帮助文档及FAQ
3. **Topic运营知识** — BI同学补充的业务口径、业务术语，与专有表或语义模型绑定
4. **技术类元数据** — 高质量SQL硬样例、Sample Data、表统计数据（行数、列分布、枚举值）

### 2.2 第二次跃迁：用户画像与持久化记忆

引入Multi-Agent后，效果和体验的割裂问题有了很大改观，但很快遇到了新的痛点：**AI的回答千篇一律**。比如，同样是问"GMV为什么下跌"，新加坡运营的同学关心的是他负责的特定市场订单表，而全球财务的同学则关注全局财务汇总的GMV数据。

为了解决这个问题，引入了**双层个性化体系**：

**第一层：用户画像** — 从权限平台等系统拉取用户的组织架构、角色、所属区域、数据权限等静态数据，在对话开始前就将其加载到上下文中，这样Agent在开口前就已经"认识"了用户。如果线上询问的是新加坡的运营同学，Agent就会倾向于推荐新加坡市场相关的数据表，并在生成SQL的查询条件里自动加上 region='SG'。

**第二层：用户记忆** — 实现了跨Session的持久化偏好记忆。用户在平台上的交互行为，比如点赞、点踩、经常搜索的表、曾经做过的口径确认、配置的数据映射等，都会被持久化存储。在用户发起新一轮对话时，系统会基于相似性规则，将相关的历史记忆加载到上下文中，实现Agent"越用越懂你"的效果。

### 2.3 第三次跃迁：语义建模

有了个性化能力和多路生成的SQL框架，依然发现纯靠大模型生成SQL的准确率很难突破预期的天花板。分析总结了三重挑战：
1. **业务语义理解** — 需要推断GMV的口径、活跃用户的定义，多步加工过程中的幻觉会不断累加
2. **表关联推理** — OLAP场景下的数据加工需要复杂的多表Join，关联链路因数仓层级的复杂性而极难推导
3. **SQL的物理实现** — 分区的选择、数据表查询分区范围的确定、各种函数语法的混用

对此，第三次跃迁是**引入语义模型**，作为一个数据抽象层，充当大模型与底层物理数据之间的桥梁。做了三件事：
1. 将业务数据映射到物理表字段和计算逻辑上
2. 预定义好标准指标、维度和过滤条件，使得大模型不再需要从零开始推理业务逻辑
3. 让语义模型封装技术的复杂性，对外呈现得像一张统一的宽表或Cube

例如，计算"昨天新加坡区域的GMV"，在纯Text-to-SQL模式下需要推断统计口径、定位物理表和字段、绑定过滤条件、确定聚合维度。而基于语义模型，系统只需要生成一个极其简单的DSL，描述清楚统计指标、时间范围和区域，剩下的DSL到SQL映射就不再依赖大模型生成，而是由语义引擎以工程化的、确定性的方式翻译为可执行的SQL。

最终选择了**混合Workflow**的方式：用户问题提交后，先经过一个意图识别与复杂度评估环节。如果问题简单且偏探索性，就走传统的Text-to-SQL链路；如果问题涉及复杂的计算逻辑且有可用的语义模型，就走Text-to-DSL链路。

为了缩短语义模型构建的工作量，设计了**辅助语义建模Agent**（Beta阶段）。它的输入包含三类元数据：表结构和字段描述等基础元数据、线上运行的SQL、公司现有报表平台上已配置的数据集和看板。拿到这些信息后，语义建模Agent基于用户的建模意图执行四项操作：指标推荐、维度识别、关键路径发现、数据关系识别与映射填充。生成的是语义模型的草案，需要交由数据专家审核确认后才上线。

语义模型上线后，建立了一个"**四步循环**"来持续优化：AI辅助建模 → 语义驱动查询（打Beta标签） → 线上反馈回流给数据专家Review → 优化后重新上线。形成了"建模、查询、验证、优化"的反馈闭环。

### 2.4 第四次跃迁：Agent工程底座

第四次跃迁是设计一套包含文件系统上下文和Sandbox等工具的复杂Agent工程底座，用以支撑复杂分析和长时间稳定运行。

**文件系统上下文**：在Data Agent场景下，模型上下文比一般的聊天Agent要复杂得多。引入了虚拟的文件系统，把各类知识按层级结构组织起来。在对话开始时只加载最上层的元数据；在确定数据域时加载L1层的业务域知识；只有用户确认了具体的表之后才展开最详细的信息。那些在当前阶段不再需要的信息，会被择机从上下文窗口中卸载下来。此外，文件系统上下文另一个重要作用是缓存多步分析产生的中间结果——将取到的数据以标准化DataFrame方式存储到文件系统中，模型上下文中只保留一个Reference或数据路径。

**隔离环境（Sandbox）**：给每个Session中运行的Agent都提供了一个权限隔离和资源隔离的沙箱环境。批处理执行和Python代码执行全都在沙箱环境中完成，有效防止恶意Prompt利用工具进行破坏性操作。

### 2.5 第五次跃迁：Skill机制

第五次跃迁引入了Skill机制，使用户能够自定义多步骤的流程化分析主题，最终实现了从取数到场景化分析的转变。

这里的Skill实现遵从Anthropic的Agent Skill规范，但在Data Agent语境下，Skill指的是由数据分析师定义的、多步骤的、复杂的数据分析流程。

以归因分析为例，一个典型的归因Skill可以包含五步流程：
1. **指标下钻** — 通过SQL拉取时间序列数据，观察指标趋势
2. **维度拆解** — 按国家、品类、渠道等可用维度进行拆解
3. **贡献度分析** — 依据维度拆解，进行计算和分析贡献度排名，执行交叉分析逻辑
4. **根因定位** — 找到根因，按影响因子排序定位出根本原因
5. **报告生成** — 生成结构化的分析报告

基于Skill的分析方式为Data Agent带来了三大价值：
- **可复用** — 一次定义，全员触发，把资深分析师脑中的标准分析流程变成平台级资产
- **可信赖** — 固定的流程保证了论证的严谨性，每一步计算过程可追溯、可验证
- **可扩展** — 提供了Skill Builder和Skill Runner，用户可自定义任何分析Skills

## 3 Data Agent工程体系

AI取数的准确性问题得到阶段性解决后，另外一个核心挑战浮现了出来：**如何保证Agent在线上能够24小时稳定运行，并拥有完整的评测和运营闭环？**

工程体系全貌被划分为**技术体系、评测体系和运营体系**三大部分。技术体系内部又细分为六大块：知识管理、文件系统上下文、隔离环境、Agent工具箱、Agent Skill以及个性化能力。

### 3.1 评测体系建设

在评测集建设上的关键转变：最早一版的评测集由QA团队帮忙生成，只有五六十条数据，严重脱离真实的业务场景。后来转变思路，**基于线上真实使用的SQL来构造评测集**。面向特定的分析主题或重点优化领域进行表的选择，搜索线上被执行成功且执行频繁的SQL，以及源自成熟稳定报表平台的SQL，然后让大模型依据这些SQL"反向生成"出对应的自然语言问题。生成的问题全部交由人工Review，审核通过后才积攒到评测集中。最终积累了一个包含数千条数据的评测集。

在结果比较方面，经历了三次探索：
- **AST抽象语法树比较** — 效果差，相同语义逻辑可以有多种表达方式
- **基于大模型的准确性比较** — 简单场景不错，复杂场景中效果不理想
- **执行准确性比较（最终方案）** — 对时间字段做归一化处理，基于编辑距离算法计算列名一致性，对浮点数设计基于残差和容差的数据比较策略

### 3.2 元数据治理实践

平台上有大量的Hive表完全没有表描述和列描述。设计了一个**AI与人工协同的四步治理流程**：
1. **表分组** — 按照业务过程和数仓的层级，将具有相同业务语义的表放到同一组内
2. **AI生成描述** — 以表组为基本单位，AI依赖业务域建模知识、用户帮助文档和FAQ生成候选描述
3. **人工Review** — 候选描述必须交给业务方负责人或表的Owner逐条人工审核
4. **血缘扩散** — 把已经治理好的核心表，通过血缘关系将其描述和计算逻辑自动扩散到下游表

治理效果：AI生成的语义描述直接被业务方采纳的比例高达70%；中等规模OLAP表的治理时间从30分钟缩小到10分钟（节省67%）；通过血缘机制，仅治理了两千张核心表就覆盖了十五万张以上的表；找表阶段的准确度最高提升了15个百分点。

### 3.3 运营闭环

运营闭环做了三步：
1. **线上准确率评估** — 基于线上反馈采集（隐式反馈+显式反馈+人工标注）构建线上准确率评估系统
2. **知识管理和Topic运营** — Topic相当于一个私域的业务域概念，BI同学可以把自己经常使用的表放到一个独立的Topic里，完全绕开繁琐的找表过程
3. **效果验证和数据回流** — 运营同学可以快速验证补充的业务知识或规则效果，所有上线效果都有看板和监控，标注数据和用户记忆回流到算法平台

## 4 基于Skill的场景化分析支持

最早尝试让Agent做自由归因或自由探索分析时，暴露了很大的问题：Agent经常会绕过关键维度的下钻和交叉分析，直接给出一个结论。去咨询专业的BI同学，得到的反馈是：无论结论对错，他们都"不敢用"。因为分析过程是个黑箱，他们不知道数据是怎么一步步得来的，结论完全无法验证。

为了保证分析过程的可信与可靠，引入了Skill机制，在模型的自主分析和可定制的流程化分析之间寻找一个平衡点。以归因分析为例：

用户提问"帮我分析上周GMV下跌的原因" → Agent识别意图 → 匹配到相关Skill描述 → 完整Markdown定义加载到上下文 → Agent严格按照定义好的流程一步步执行 → 每一步都输出中间结论和结果。

这种机制实现了**中间步骤可追溯、异常可回归、流程不可跳过、结果可验证**，从而极大地提升了分析结论的可信性。

## 5 总结与展望

回顾整个Data Agent从AI取数工具到面向分析场景的全过程，通过Multi-Agent、个性化与语义模型提升了准确性，通过包含Sandbox和文件系统上下文的工程底座来支持多步骤、长时间稳定运行，并最终引入Skill机制，使分析师和BI团队能够定制和沉淀分析流程到平台上。

关于未来的四个趋势判断：
1. **Agent Harness的演进** — Harness就像是Agent的操作系统。调优Prompt等工作随着模型进化边际效益降低，但状态管理、上下文管理、从个性化到通用化的转变无论模型如何进化都必须去做。未来工具应该是通用化的场景，比如给它"一台电脑"、一个可操作和接收反馈的环境作为通用工具。
2. **Agent First的理念** — 未来的数据平台应该是为了Agent而设计的，而不是把Agent当作平台上的一个附加工具。Agent将会成为人与数据交互的新界面。
3. **从AI工具到AI员工的转变** — 1.0时代的SQL取数助手是一个工具；2.0时代它变得更像一个支持分析的助手；而在3.0时代，Agent正在向一种"数字劳动力"演进。其关键点是Schedule Channel和Agent Skills的自我生成与进化能力。
4. **Agent治理** — Agent究竟聪不聪明、效果好不好，都需要伴随可追溯性、可控性和可持续的评估能力。这是让我们敢在生产环境下大规模落地Agent的先决条件。

---

# 第二部分：机加工企业数据现状诊断

## 2.1 当前数据资产盘点

基于现有系统梳理，我们的数据资产可分为以下六大类：

### 2.1.1 生产运营数据

| 数据类别 | 当前形态 | 数据量级 | 更新频率 | 质量评级 |
|----------|----------|----------|----------|----------|
| 报工统计 | Excel（多sheet） | 每日1-2份 | 日更 | ★★★ |
| 产线明细 | Excel | 每日1份 | 日更 | ★★★ |
| 设备运行状态 | FANUC系统/手工记录 | ~200台 | 实时/班次 | ★★ |
| 刀具管理记录 | 手工/系统混合 | 数百把刀具 | 不定期 | ★★ |
| 质量检验记录 | Excel/纸质混合 | 按批次 | 批次 | ★★ |
| 日报 | Obsidian Markdown | 每日数份 | 日更 | ★★★ |

### 2.1.2 当前数据管道的技术现状

- **已建立**：Excel → Gateway → cache → sync cron → data/production/ 的文件流管道
- **已建立**：产量简报 cron（8b0b，1440m）、早间简报 cron（bfa，1440m）
- **已建立**：日报归档 cron（65ed，12h）→ Obsidian 月度文件
- **已有能力**：Hermes Agent 作为编排引擎，具备文件系统访问、终端执行、浏览器操作、定时调度能力
- **已有能力**：Python 数据处理（pandas、openpyxl）、数据分析脚本

### 2.1.3 关键KPI体系

基于管理需求，当前关注的核心指标体系：

| 层级 | 指标 | 当前计算方式 | 数据源 |
|------|------|-------------|--------|
| ★³ | 设备OEE（稼动率、故障率、MTBF） | Excel手工 | 报工统计 |
| ★³ | 良品率（一次通过率、废品率） | Excel手工 | 质量记录+报工统计 |
| ★² | 生产效率（节拍时间、换模时间） | 部分手工估算 | 产线明细 |
| ★² | 成本控制（刀具成本、能耗成本） | 月度汇总 | 刀具管理+电费单 |
| ★¹ | 交期管理（订单完成率、准时交付率） | 手工跟踪 | 订单表 |

## 2.2 数据痛点分析

对标原文中提到的五大核心问题，映射到我们的实际场景：

### 2.2.1 "找表不准"——映射为"找数不准"

**原文问题**：数仓分层导致大量结构相似的表，Embedding模型难以区分。

**我们的对应问题**：
- 报工统计和产线明细的时间窗口不同（产线明细覆盖全天含前夜班，报工统计的"夜班"是当晚），经常混淆
- 多个Excel文件的列名相似但含义不同（如不同sheet的"工废"统计口径可能不一致）
- 日报内容分散在Obsidian的多个文件中，缺乏统一检索
- 缺乏元数据管理系统——没有表的描述、字段的业务含义文档

### 2.2.2 "SQL语义错误"——映射为"计算口径不统一"

**原文问题**：缺失业务规则和数据口径导致计算逻辑错误。

**我们的对应问题**：
- OEE计算方式未标准化——不同人理解的"计划运行时间"可能不同
- "工废"和"料废"的归因标准不统一
- 刀具寿命计算中"正常磨损"和"异常破损"的边界模糊
- 缺乏数据字典/业务术语表

### 2.2.3 "语法错误"——映射为"公式/脚本错误"

**原文问题**：大模型混用数据库方言。

**我们的对应问题**：
- Python脚本中字段名拼写错误
- Excel公式引用错误（跨sheet引用断裂）
- 数据管道中列映射错误（如inlineStr vs sharedStrings的处理差异）

### 2.2.4 "交互体验差"——映射为"信息查询效率低"

**原文问题**：找数、取数等功能入口割裂。

**我们的对应问题**：
- 管理者要获取"昨天OEE是多少"需要：找Excel → 打开 → 找到对应sheet → 人工计算
- 多个系统（飞书、微信、Obsidian、Excel）之间切换
- 日报信息需要手动汇总才能得到全局视图
- 缺乏统一的数据查询入口

### 2.2.5 "评测缺失"——映射为"数据验证缺失"

**原文问题**：评测集脱离生产环境。

**我们的对应问题**：
- 数据管道是否有异常缺乏自动化检测
- 计算结果正确性依赖人工抽查
- 没有回归测试机制——改了脚本不知道是否破坏了其他功能

## 2.3 与标杆实践的差距分析

| 维度 | 原文标杆实践 | 我方当前状态 | 差距评级 |
|------|-------------|-------------|----------|
| 数据基础设施 | 百万级表的数仓+Hive Metastore | Excel为主+部分数据库 | ★★★★★ |
| 元数据治理 | AI辅助+人工Review+血缘扩散 | 基本空白 | ★★★★★ |
| 取数能力 | Multi-Agent Text-to-SQL | 手工+脚本 | ★★★★★ |
| 语义建模 | 指标/维度/过滤条件预定义 | 无 | ★★★★★ |
| 个性化 | 用户画像+持久化记忆 | 无 | ★★★★ |
| 评测体系 | 基于线上SQL的评测集+执行准确性比较 | 无自动化评测 | ★★★★★ |
| 运营闭环 | 反馈采集+标注+数据回流 | 无 | ★★★★★ |
| 场景化分析 | Skill机制+多步骤流程 | 固定脚本 | ★★★★ |

---

# 第三部分：总体方案架构

## 3.1 愿景与目标

### 3.1.1 愿景

打造机加工行业的"**AI原生数据消费平台**"——管理者通过自然语言即可获取生产数据、进行归因分析、生成决策报告，实现从"人找数据"到"数据找人"的范式转变。

### 3.1.2 三阶段目标

| 阶段 | 时间 | 目标 | 核心指标 |
|------|------|------|----------|
| 短期（可问） | 0-3个月 | 自然语言查询生产数据 | 常见问题回答准确率≥80% |
| 中期（可信） | 3-6个月 | 语义模型驱动的可靠分析 | 关键KPI计算准确率≥95% |
| 长期（可用） | 6-12个月 | Skill驱动的场景化自主分析 | 分析报告可直接用于管理决策 |

## 3.2 技术架构总览

```
┌─────────────────────────────────────────────────────────────┐
│                    用户交互层 (Chat UI)                       │
│  飞书Bot │ 微信 │ Hermes TUI │ Web Dashboard │ 定时推送      │
├─────────────────────────────────────────────────────────────┤
│                    Supervisor Agent                          │
│  意图识别 │ 任务编排 │ 上下文管理 │ 路由决策                   │
├─────────────────────────────────────────────────────────────┤
│                    专业Agent层                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │Data Scope│  │  Data    │  │   SQL    │  │ Analysis │   │
│  │  Agent   │  │Discovery │  │ Generator│  │  Agent   │   │
│  │ (数据域) │  │  Agent   │  │  Agent   │  │ (分析)   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
├─────────────────────────────────────────────────────────────┤
│                    语义模型层                                │
│  指标定义 │ 维度定义 │ 过滤条件 │ DSL→SQL引擎                  │
├─────────────────────────────────────────────────────────────┤
│                    工程底座                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ 文件系统 │  │ Sandbox  │  │  Skill   │  │  评测    │   │
│  │  上下文  │  │  沙箱    │  │  引擎    │  │  体系    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
├─────────────────────────────────────────────────────────────┤
│                    数据层                                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ SQLite/  │  │  元数据  │  │  知识库  │  │  用户    │   │
│  │PostgreSQL│  │   仓库   │  │ (Mart)   │  │  画像    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
├─────────────────────────────────────────────────────────────┤
│                    数据接入层                                │
│  Excel管道 │ FANUC采集 │ 日报同步 │ 飞书数据 │ 手工录入      │
└─────────────────────────────────────────────────────────────┘
```

## 3.3 数据架构设计

### 3.3.1 数据分层

参照数据仓库分层理念，为机加工场景设计简化的四层架构：

```
┌─────────────────────────────────────────┐
│  ADS (应用数据服务层)                     │
│  日报视图 │ OEE汇总表 │ 质量趋势 │ 成本看板 │
├─────────────────────────────────────────┤
│  DWS (数据汇总层)                         │
│  日产量汇总 │ 周OEE汇总 │ 月成本汇总       │
├─────────────────────────────────────────┤
│  DWD (明细数据层)                         │
│  报工明细 │ 产线明细 │ 质量记录 │ 刀具记录  │
├─────────────────────────────────────────┤
│  ODS (原始数据层)                         │
│  原始Excel │ 设备日志 │ 日报Markdown       │
└─────────────────────────────────────────┘
```

### 3.3.2 核心数据模型

#### 生产事实表（fact_production）

| 字段 | 类型 | 说明 |
|------|------|------|
| production_date | DATE | 生产日期 |
| shift | VARCHAR | 班次（白班/夜班） |
| process_code | VARCHAR | 工序编码 |
| machine_id | VARCHAR | 设备编号 |
| planned_qty | INTEGER | 计划产量 |
| actual_qty | INTEGER | 实际产量 |
| completion_rate | DECIMAL | 完成率 |
| process_scrap | INTEGER | 工废数量 |
| material_scrap | INTEGER | 料废数量 |
| downtime_min | INTEGER | 宕机时间（分钟） |
| total_hours | DECIMAL | 总工时 |
| approval_status | VARCHAR | 审批状态 |

#### 设备维度表（dim_machine）

| 字段 | 类型 | 说明 |
|------|------|------|
| machine_id | VARCHAR | 设备编号（主键） |
| machine_name | VARCHAR | 设备名称 |
| machine_type | VARCHAR | 设备类型（车床/铣床/加工中心） |
| control_system | VARCHAR | 控制系统（FANUC/Mazak/西门子） |
| workshop | VARCHAR | 所属车间 |
| production_line | VARCHAR | 所属产线 |
| install_date | DATE | 安装日期 |

#### 工序维度表（dim_process）

| 字段 | 类型 | 说明 |
|------|------|------|
| process_code | VARCHAR | 工序编码（主键） |
| process_name | VARCHAR | 工序名称 |
| process_category | VARCHAR | 工序类别（粗加工/精加工/热处理） |
| standard_cycle_time | DECIMAL | 标准节拍时间（分钟） |
| standard_changeover_time | DECIMAL | 标准换模时间（分钟） |

## 3.4 实施路线图总览

```
Phase 1 (Month 1-2)         Phase 2 (Month 2-4)         Phase 3 (Month 4-6)
┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
│  数据基础建设      │  ──→  │  智能取数Agent    │  ──→  │  语义建模+准确率  │
│                  │       │                  │       │                  │
│ • 数据入仓        │       │ • Multi-Agent架构 │       │ • 制造业KPI语义   │
│ • 元数据治理      │       │ • 渐进式元数据    │       │ • 混合路由        │
│ • 数据字典        │       │ • 基础问答        │       │ • 评测体系        │
│ • 质量监控        │       │ • 用户画像        │       │ • 辅助建模Agent   │
└──────────────────┘       └──────────────────┘       └──────────────────┘
        │                           │                           │
        ▼                           ▼                           ▼
Phase 4 (Month 6-9)         Phase 5 (Month 9-12)
┌──────────────────┐       ┌──────────────────┐
│  场景化Skill      │  ──→  │  自主运营+进化    │
│                  │       │                  │
│ • OEE归因Skill   │       │ • 自动化调度      │
│ • 质量分析Skill   │       │ • 主动预警        │
│ • 成本分析Skill   │       │ • 模型微调        │
│ • Skill Builder  │       │ • AI员工化        │
└──────────────────┘       └──────────────────┘
```

---

# 第四部分：分阶段实施方案

## 4.1 第一阶段：数据基础建设（第1-2个月）

> **核心原则**：做Data Agent不能只盯着模型和工程架构，数据质量这块脏活、累活，也必须下苦功夫去做。

### 4.1.1 任务1：数据入仓（Week 1-3）

**目标**：将现有的Excel数据、日报数据统一导入结构化数据库。

**具体步骤**：

**Step 1：选型决策**

| 方案 | 优点 | 缺点 | 推荐度 |
|------|------|------|--------|
| SQLite | 零运维、本地化、够用 | 并发能力弱 | ★★★★★（首选） |
| PostgreSQL | 功能完整、扩展性强 | 需安装运维 | ★★★ |
| DuckDB | 分析型、嵌入式 | 生态较小 | ★★★ |

**推荐方案**：SQLite，理由——
- 数据量级（日增量KB-MB级）完全在SQLite承载范围内
- 零运维成本，适合当前团队规模
- 与Python pandas天然集成
- 后续可无缝迁移至PostgreSQL

**Step 2：建立自动化入仓管道**

```python
# 伪代码：报工统计入仓流程
def sync_production_stats(excel_path, db_path):
    """
    1. 读取Excel所有sheet
    2. 解析inlineStr（注意与sharedStrings的区别）
    3. 列映射：A=工序, B=计划, C=实产, D=完成率, E=工废, F=料废, G=宕机, H=总工时, I=审批
    4. 跳过Row3（合计行）和Row4（列标题行）
    5. 写入fact_production表
    6. 验证：行数一致性、关键字段非空
    """
    pass
```

**Step 3：数据质量控制规则**

| 规则编号 | 规则内容 | 严重级别 | 处理方式 |
|----------|----------|----------|----------|
| QC-001 | 计划产量 > 0 | ERROR | 拒绝入仓 |
| QC-002 | 实产 > 计划 * 1.5 | WARN | 标记异常 |
| QC-003 | 完成率 = 实产/计划（±5%容差） | WARN | 自动修正 |
| QC-004 | 工废 + 料废 ≤ 实产 | ERROR | 拒绝入仓 |
| QC-005 | 宕机时间 ≤ 总工时 | ERROR | 拒绝入仓 |
| QC-006 | 生产日期不跨天（注意夜班时间窗口） | WARN | 标记待确认 |

**Step 4：日报入仓**

将Obsidian中的日报Markdown文件结构化提取：
- 日期、作者、工序、产量、问题描述、处理措施
- 使用已有的daily-report-analysis skill进行文本提取
- 存入日报事实表（fact_daily_report）

**验证标准**：
- 所有历史Excel数据成功导入（≥99%成功率）
- 新增数据自动入仓（延迟≤5分钟）
- 数据质量检查通过率≥95%

### 4.1.2 任务2：元数据治理（Week 2-4）

**目标**：建立完整的元数据管理体系，让"找数"不再困难。

**Step 1：建立数据字典**

参照原文中AI辅助+人工Review的模式：

```markdown
## 报工统计-工序字段 (process_code)

**业务含义**：生产过程中各工序的编码标识
**数据来源**：报工统计Excel - A列
**编码规则**：工序大类(2位)-工序细类(3位)-设备类型(2位)
**示例值**：CC-001-L1 (粗车-外圆-L1号车床)
**关联表**：fact_production.process_code, dim_process.process_code
**注意事项**：同一工序在不同设备上可能有不同编码，需结合machine_id使用
**治理状态**：✅ 已审核 | 审核人：徐经理 | 审核日期：2026-07-01
```

**Step 2：分组治理**

参照原文的四步治理法：

1. **表分组**：按业务域将数据表分组
   - 生产域：报工统计、产线明细、产量日报
   - 质量域：检验记录、不良品追踪、SPC数据
   - 设备域：运行状态、故障记录、保养记录
   - 成本域：刀具成本、能耗、物料消耗
   - 人员域：日报、考勤、技能等级

2. **AI生成描述**：基于已有脚本、配置文件、历史对话生成候选描述
   - 利用Hermes Agent的上下文理解能力
   - 引用已沉淀的skill中的业务规则

3. **人工Review**：
   - 生产域 → 徐经理审核
   - 质量域 → 质量主管审核
   - 设备域 → 设备主管审核
   - 成本域 → 财务审核

4. **血缘扩散**：
   - 报工统计 → 产线明细（时间窗口关系）
   - 报工统计 → OEE计算（派生关系）
   - 产量数据 → 成本分析（依赖关系）

**验证标准**：
- 核心表（报工统计、产线明细、日报、质量记录）100%有完整描述
- 所有字段有业务含义描述
- 业务术语表覆盖≥50个常用术语

### 4.1.3 任务3：建立Topic概念（Week 3-4）

**目标**：为不同角色的用户建立专属数据域。

参照原文的Topic运营理念：

| Topic名称 | 目标用户 | 包含的表 | 核心指标 |
|-----------|----------|----------|----------|
| 生产管理 | 生产经理（Simon） | 报工统计、产线明细 | 产量、OEE、完成率 |
| 质量管理 | 质量主管 | 检验记录、不良品追踪 | 一次通过率、废品率、PPM |
| 设备管理 | 设备主管 | 运行状态、故障记录 | MTBF、MTTR、稼动率 |
| 成本管理 | 财务 | 刀具成本、能耗 | 单件成本、刀具损耗率 |
| 人事管理 | HR | 考勤、技能等级 | 出勤率、技能达标率 |

**实现方式**：
- Topic = 数据库视图（View）+ 预定义查询模板
- 每个Topic绑定到对应的语义模型（后续Phase构建）
- 用户进入Topic后，Agent自动限定在该数据域内操作

## 4.2 第二阶段：智能取数Agent（第3-5个月）

> **核心原则**：先解决"找得到、取得出"，再解决"算得对、分析得透"。

### 4.2.1 任务1：Multi-Agent架构搭建

**目标**：搭建原文中的两层Agent架构，实现自然语言取数。

**Agent定义**：

#### Supervisor Agent（编排层）

```
角色：生产数据管家
职责：
  1. 接收用户自然语言问题
  2. 加载用户画像（角色、关注指标、常用Topic）
  3. 意图识别 → 路由到对应的Data Scope Agent
  4. 管理上下文生命周期
  5. 结果汇总与呈现
```

#### Data Scope Agent（数据域定位）

```
角色：数据域导航员
职责：
  1. 根据问题确定所属业务域（生产/质量/设备/成本）
  2. 如果模糊，向用户确认（Human-in-loop）
  3. 激活对应的Topic上下文
输入："昨天白班的产量是多少"
输出：{domain: "生产管理", topic: "生产管理", confidence: 0.95}
```

#### Data Discovery Agent（表发现）

```
角色：表/字段定位专家
职责：
  1. 在已确认的数据域内找到相关表
  2. 基于元数据描述进行精准匹配
  3. 候选表提交用户确认（Human-in-loop）
  4. 加载确认后的表的完整Schema
输入：{domain: "生产管理", question: "昨天白班的产量"}
输出：{tables: ["fact_production"], fields: ["actual_qty", "production_date", "shift"]}
```

#### SQL Generator Agent（SQL生成）

```
角色：SQL编写专家
职责：
  1. 基于确认的表和字段生成SQL
  2. 多路并行生成（自校正+任务分治+直接生成）
  3. 选优
  4. 语法验证与修复
  5. 执行并返回结果
```

**技术实现要点**：

利用Hermes Agent的现有能力作为基础：
- 工具调用 = Agent之间的任务交接
- 利用delegate_task实现子Agent并行执行
- 上下文管理利用session持久化

**示例交互流程**：

```
用户: 昨天白班的产量是多少？

Supervisor Agent:
  → 加载用户画像：Simon，生产经理，关注产量/OEE
  → 意图识别：产量查询，时间=昨天，班次=白班
  → 路由到生产管理Data Scope Agent

Data Scope Agent:
  → 确认数据域：生产管理 (confidence: 0.97)
  → 自动确认（置信度高，跳过Human-in-loop）

Data Discovery Agent:
  → 候选表：[fact_production (匹配度0.95), dws_daily_summary (匹配度0.82)]
  → 向用户确认：是否查fact_production表？
  
用户: 确认

SQL Generator Agent:
  → 生成三条候选SQL：
    1. (自校正) SELECT SUM(actual_qty) FROM fact_production WHERE production_date='2026-07-04' AND shift='白班'
    2. (任务分治) 同逻辑但拆分子查询
    3. (直接生成) 同上
  → 选优：所有等价，选方案1
  → 语法验证：通过 (SQLite dialect)
  → 执行 → 返回结果

Agent 回复:
  昨天白班总产量：1,250件 ✓
  分设备明细：
  | 设备编号 | 设备名称 | 计划 | 实际 | 完成率 |
  |----------|----------|------|------|--------|
  | M-001    | L1车床   | 500  | 480  | 96.0%  |
  | M-002    | L2车床   | 400  | 410  | 102.5% |
  | M-003    | V1加工中心| 350  | 360  | 102.9% |
  ...
```

### 4.2.2 任务2：渐进式元数据披露

**目标**：防止上下文窗口过载，实现精准信息加载。

**三层加载机制**：

```
用户提问: "昨天白班产量"
  │
  ▼
L1 加载: 用户画像 (200 tokens)
  ├── 角色：生产经理
  ├── 关注指标：产量、OEE、完成率
  └── 常用Topic：生产管理
  │
  ▼
L2 加载: 业务域元数据 (800 tokens)
  ├── 生产管理域描述
  ├── 包含的表清单（仅表名+一句话描述）
  └── 不加载Schema细节
  │
  ▼
用户确认表: fact_production
  │
  ▼
L3 加载: 完整Schema + 业务规则 (2,000 tokens)
  ├── 所有字段名+类型+业务描述
  ├── 相关业务规则（夜班时间窗口、工废口径）
  ├── 字段枚举值（shift: 白班/夜班）
  └── 常见查询模板
```

**上下文卸载机制**：
- L2加载后，L1中的非必要信息（如用户技能等级、考勤记录等）卸载
- L3加载后，L2中的"其他表信息"卸载
- SQL执行完成后，Schema信息卸载，仅保留结果

### 4.2.3 任务3：个性化能力建设

**目标**：让Agent"认识"每个用户，提供差异化服务。

**用户画像定义**：

```yaml
user_profile:
  user_id: "simon"
  name: "Simon"
  role: "生产经理/总经理"
  focus_metrics: ["OEE", "良品率", "产量", "刀具成本"]
  default_topic: "生产管理"
  permission_level: "full_access"
  preferred_time_range: "昨日"  # 默认时间范围
  preferred_output: "表格+趋势图"  # 输出偏好
  
  # 个性化规则
  rules:
    - when_asking: "产量"
      default: "所有设备汇总 + Top 5设备明细"
    - when_asking: "OEE"
      default: "分设备 + 分班次"
      
  # 记忆（跨Session）
  memory:
    - last_query: "昨天白班产量"  # 最近查询
    - frequent_tables: ["fact_production", "dws_daily_summary"]
    - confirmed_metrics:  # 已确认的口径
        - "产量=actual_qty，不含试制件"
        - "OEE=稼动率×性能效率×良品率"
```

**实现方式**：
- 存储位置：SQLite中的user_profile表和user_memory表
- 加载时机：每次对话开始时自动加载
- 更新机制：用户每次交互后自动更新记忆

## 4.3 第三阶段：语义建模与准确率提升（第5-7个月）

> **核心原则**：语义模型是准确率从60%提升到95%的关键桥梁。

### 4.3.1 任务1：制造业KPI语义模型设计

**目标**：将核心制造KPI固化为语义模型，消除大模型推理的不确定性。

**语义模型示例1：OEE**

```yaml
semantic_model:
  name: "oee"
  display_name: "设备综合效率(OEE)"
  description: "衡量设备综合利用效率的核心指标"
  
  dimensions:
    - name: "machine_id"
      type: "string"
      display_name: "设备编号"
      source: "fact_production.machine_id"
      join: "dim_machine.machine_id"
      
    - name: "production_date"
      type: "date"
      display_name: "生产日期"
      source: "fact_production.production_date"
      
    - name: "shift"
      type: "string"
      display_name: "班次"
      source: "fact_production.shift"
      values: ["白班", "夜班"]
      
    - name: "workshop"
      type: "string"
      display_name: "车间"
      source: "dim_machine.workshop"
  
  measures:
    - name: "availability"
      display_name: "稼动率"
      formula: "(total_hours * 60 - downtime_min) / (total_hours * 60)"
      unit: "%"
      
    - name: "performance"
      display_name: "性能效率"
      formula: "actual_qty * standard_cycle_time / ((total_hours * 60) - downtime_min)"
      unit: "%"
      
    - name: "quality_rate"
      display_name: "良品率"
      formula: "(actual_qty - process_scrap - material_scrap) / actual_qty"
      unit: "%"
      
    - name: "oee"
      display_name: "OEE"
      formula: "availability * performance * quality_rate"
      unit: "%"
      
    - name: "mtbf"
      display_name: "平均故障间隔"
      formula: "total_hours / count(distinct failure_events)"
      unit: "小时"
  
  filters:
    - name: "time_range"
      type: "date_range"
      default: "yesterday"
      
    - name: "machine_filter"
      type: "string[]"
      description: "设备编号列表，空=全部"
      
  default_queries:
    - name: "昨日OEE总览"
      dsl: "SELECT oee, availability, performance, quality_rate FROM oee WHERE time_range='yesterday'"
    - name: "本月OEE趋势"
      dsl: "SELECT production_date, oee FROM oee WHERE time_range='this_month'"
```

**语义模型示例2：良品率**

```yaml
semantic_model:
  name: "quality_rate"
  display_name: "良品率分析"
  
  dimensions:
    - name: "process_code"
      display_name: "工序"
    - name: "machine_id"
      display_name: "设备"
    - name: "production_date"
      display_name: "日期"
    - name: "scrap_type"
      display_name: "废品类型"
      values: ["工废", "料废"]
      
  measures:
    - name: "first_pass_yield"
      display_name: "一次通过率"
      formula: "(actual_qty - process_scrap) / actual_qty"
      
    - name: "total_scrap_rate"
      display_name: "总废品率"
      formula: "(process_scrap + material_scrap) / actual_qty"
      
    - name: "process_scrap_rate"
      display_name: "工废率"
      formula: "process_scrap / actual_qty"
      
    - name: "material_scrap_rate"
      display_name: "料废率"
      formula: "material_scrap / actual_qty"
```

**语义模型示例3：刀具成本**

```yaml
semantic_model:
  name: "tool_cost"
  display_name: "刀具成本分析"
  
  dimensions:
    - name: "tool_id"
      display_name: "刀具编号"
    - name: "tool_type"
      display_name: "刀具类型"
    - name: "machine_id"
      display_name: "使用设备"
    - name: "period"
      display_name: "统计周期"
      
  measures:
    - name: "tool_cost_per_part"
      display_name: "单件刀具成本"
      formula: "sum(tool_cost) / sum(actual_qty)"
      unit: "元/件"
      
    - name: "tool_life_actual"
      display_name: "实际刀具寿命"
      formula: "sum(parts_produced)"
      unit: "件"
      
    - name: "tool_cost_ratio"
      display_name: "刀具成本占比"
      formula: "sum(tool_cost) / sum(total_cost)"
      unit: "%"
```

### 4.3.2 任务2：混合路由设计

**目标**：根据问题复杂度智能选择Text-to-SQL或Text-to-DSL路径。

```
用户问题
    │
    ▼
┌─────────────┐
│ 复杂度评估   │
│ (Agent+规则) │
└──────┬──────┘
       │
   ┌───┴───┐
   │       │
   ▼       ▼
简单/探索  复杂计算
   │       │
   ▼       ▼
Text-to-SQL  Text-to-DSL
   │       │
   ▼       ▼
物理SQL      DSL → 语义引擎 → SQL
   │       │
   └───┬───┘
       ▼
   执行 → 可视化 → 返回
```

**路由规则**：

```yaml
routing_rules:
  # 走Text-to-DSL的场景
  dsl_path:
    - keywords: ["OEE", "稼动率", "MTBF", "良品率", "刀具成本", "换模时间"]
    - question_patterns:
        - ".*趋势.*"
        - ".*对比.*"
        - ".*归因.*"
        - ".*排行.*"
    - user_config:
        - topic绑定语义模型 → 强制DSL
        
  # 走Text-to-SQL的场景
  sql_path:
    - keywords: ["查一下", "看看", "有没有", "是多少"]
    - question_patterns:
        - ".*(昨天|今天|这周).*(产量|数量|多少).*"
    - exploration: true  # 探索性查询
    
  # 默认规则
  default: "auto"  # 由Agent自主判断
```

### 4.3.3 任务3：辅助建模Agent（定制版）

**目标**：参照原文的辅助语义建模Agent，定制机加工版本。

**输入数据源**：
1. **基础元数据**：数据字典、表结构、字段描述
2. **历史查询**：Hermes session history中的生产数据查询记录
3. **已有脚本**：daily-report-analysis、production简报等skill脚本
4. **报表模板**：日报模板、早间简报模板、周报模板

**Agent工作流**：

```
输入：用户的建模意图（如"我想建一个OEE的语义模型"）
  │
  ▼
Step 1: 指标推荐
  从历史查询中提取高频指标 → 推荐候选指标清单
  输出：[OEE, 稼动率, 性能效率, 良品率, MTBF, MTTR]
  │
  ▼
Step 2: 维度识别
  从表结构中识别可用维度 → 推荐候选维度
  输出：[设备, 日期, 班次, 车间, 工序]
  │
  ▼
Step 3: 关键路径发现
  从现有脚本和查询中提取计算逻辑 → 生成formula草案
  输出：OEE = (总工时*60 - 宕机) / (总工时*60) * 实际/(实际+工废+料废) * ...
  │
  ▼
Step 4: 映射填充
  将指标/维度映射到物理表字段 → 生成完整语义模型草案
  │
  ▼
输出：语义模型YAML草案 → 提交人工审核
```

### 4.3.4 任务4：评测体系建设

**目标**：建立可靠的离线评测基准，确保每次改动都有数据支撑。

**评测集构建**（参照原文方法论）：

**Step 1：收集线上真实SQL**

```sql
-- 从已有的脚本和查询日志中收集
-- 来源1：daily-report-analysis skill中的查询
-- 来源2：production简报 cron中的查询
-- 来源3：手工编写的分析查询
```

**Step 2：反向生成自然语言问题**

```
SQL: SELECT machine_id, SUM(actual_qty) FROM fact_production 
     WHERE production_date='2026-07-04' AND shift='白班' 
     GROUP BY machine_id

↓ 反向生成（AI辅助） ↓

问题1: "昨天白班各设备的产量是多少？"
问题2: "2026年7月4号白班，列出每个设备的实际产量"
问题3: "昨天白天每台机器做了多少件？"
```

**Step 3：人工Review并入库**

每个问题标记：
- 难度等级（L1-简单/L2-中等/L3-复杂）
- 分析主题（产量/OEE/质量/成本）
- 标准答案SQL
- 标准答案结果集

**Step 4：评测Pipeline**

```python
def evaluate_agent(test_set, agent):
    """
    对评测集中的每条数据：
    1. 输入问题 → Agent生成SQL
    2. 执行生成的SQL → 获取结果集A
    3. 执行标准答案SQL → 获取结果集B
    4. 比较结果集A和B（执行准确性比较）
    5. 统计准确率
    """
    results = []
    for case in test_set:
        generated_sql = agent.query(case['question'])
        result_a = execute_sql(generated_sql)
        result_b = case['expected_result']
        score = compare_results(result_a, result_b)
        results.append({
            'question': case['question'],
            'difficulty': case['difficulty'],
            'score': score,
            'generated_sql': generated_sql,
            'expected_sql': case['expected_sql']
        })
    
    # 统计
    by_difficulty = group_by(results, 'difficulty')
    return {
        'overall_accuracy': mean([r['score'] for r in results]),
        'l1_accuracy': mean([r['score'] for r in by_difficulty['L1']]),
        'l2_accuracy': mean([r['score'] for r in by_difficulty['L2']]),
        'l3_accuracy': mean([r['score'] for r in by_difficulty['L3']]),
    }
```

**结果比较策略**：

| 数据类型 | 比较方法 | 容差 |
|----------|----------|------|
| 整数（产量、数量） | 精确匹配 | 0 |
| 浮点（OEE、比例） | 残差比较 | ±0.01 |
| 时间字段 | 归一化后比较 | 同日即可 |
| 列名 | 编辑距离 | 允许别名差异 |
| 排序 | ORDER BY归一化后比较 | 不关注顺序 |

**评测频率**：
- 每次Agent配置变更 → 自动运行
- 每次语义模型更新 → 自动运行
- 每周基线评测 → 自动运行并生成报告
- 模型切换 → 全量评测

## 4.4 第四阶段：场景化分析Skill（第7-10个月）

> **核心原则**：Skill = 资深分析师脑中的标准流程 → 平台级可复用资产。

### 4.4.1 任务1：Skill引擎搭建

**目标**：搭建符合Anthropic Agent Skill规范的Skill执行引擎。

**Skill定义格式**：

```markdown
---
name: oee-attribution
display_name: OEE归因分析
version: 1.0.0
author: Simon
category: 生产分析
triggers:
  - keywords: ["OEE下降", "OEE异常", "稼动率下降", "效率降低"]
  - patterns: [".*为什么.*OEE.*", ".*OEE.*原因.*"]
description: >
  当OEE出现下降时，按标准流程进行归因分析：
  指标下钻 → 维度拆解 → 贡献度分析 → 根因定位 → 报告生成
---

# OEE归因分析 Skill

## Step 1: 指标下钻

**目标**：确定OEE下降的时间范围和幅度。

1. 查询指定时间范围内的OEE日趋势
   ```sql
   SELECT production_date, oee, availability, performance, quality_rate
   FROM semantic_model.oee
   WHERE production_date BETWEEN {start_date} AND {end_date}
   ORDER BY production_date
   ```

2. 识别下降点：比较同比/环比，标记OEE下降超过{x}%的日期
3. 输出：下降起始日期、下降幅度、三个子指标的变化

## Step 2: 维度拆解

**目标**：确定是哪个维度导致了下降。

1. 按设备拆解：
   ```sql
   SELECT machine_id, oee, availability, performance, quality_rate
   FROM semantic_model.oee
   WHERE production_date = {target_date}
   ORDER BY oee ASC
   ```

2. 按班次拆解：
   ```sql
   SELECT shift, oee, availability, performance, quality_rate
   FROM semantic_model.oee
   WHERE production_date = {target_date}
   ```

3. 按工序拆解：
   ```sql
   SELECT process_code, avg(oee)
   FROM semantic_model.oee
   WHERE production_date = {target_date}
   GROUP BY process_code
   ```

4. 输出：受影响最大的Top 5设备/工序

## Step 3: 贡献度分析

**目标**：量化各子指标对OEE下降的贡献。

1. 计算各子指标变化：
   - ΔAvailability = availability_actual - availability_baseline
   - ΔPerformance = performance_actual - performance_baseline
   - ΔQuality = quality_rate_actual - quality_rate_baseline

2. 计算贡献度：
   - Contribution_availability = ΔAvailability / (ΔAvailability + ΔPerformance + ΔQuality)
   - Contribution_performance = ΔPerformance / (ΔAvailability + ΔPerformance + ΔQuality)
   - Contribution_quality = ΔQuality / (ΔAvailability + ΔPerformance + ΔQuality)

3. 交叉分析：Top 5低OEE设备的子指标贡献度
4. 输出：主要贡献因子排序

## Step 4: 根因定位

**目标**：定位导致OEE下降的根本原因。

1. 如果主要贡献是稼动率下降 → 查询宕机记录：
   ```sql
   SELECT machine_id, downtime_min, failure_reason
   FROM fact_production
   WHERE production_date = {target_date}
   ORDER BY downtime_min DESC
   ```

2. 如果主要贡献是性能效率下降 → 查询节拍时间：
   - 对比实际节拍 vs 标准节拍
   - 检查换模时间是否异常

3. 如果主要贡献是良品率下降 → 查询质量记录：
   - 按废品类型分拆（工废/料废）
   - 按工序分拆
   - 关联日报中的质量问题描述

4. 输出：排名前3的根因及影响量化

## Step 5: 报告生成

**目标**：生成结构化的分析报告。

报告模板：
```markdown
# OEE归因分析报告

**分析周期**：{start_date} - {end_date}
**分析触发**：OEE从{baseline}下降至{actual}（降幅{delta}%）

## 1. 趋势概览
[OEE趋势图]

## 2. 维度拆解
### 受影响Top 5设备
| 排名 | 设备 | OEE | 稼动率 | 性能效率 | 良品率 | 变化 |
|------|------|-----|--------|----------|--------|------|

### 受影响Top 3工序
...

## 3. 贡献度分析
各子指标贡献度：
- 稼动率：{contribution}% — {analysis}
- 性能效率：{contribution}% — {analysis}
- 良品率：{contribution}% — {analysis}

## 4. 根因定位
1. **主要原因**：{root_cause} 
   - 影响幅度：{impact}
   - 影响设备：{machines}
   - 建议措施：{suggestions}

2. **次要原因**：...

## 5. 建议与行动计划
...
```

**验证**：每一步产生的中间结果需展示给用户，任何步骤可暂停并调整参数。
```

### 4.4.2 任务2：核心Skill库建设

**优先级排序**：

| 优先级 | Skill名称 | 业务价值 | 开发复杂度 | 目标上线 |
|--------|-----------|----------|------------|----------|
| P0 | OEE归因分析 | ★★★★★ | ★★★ | Month 8 |
| P0 | 产量趋势分析 | ★★★★★ | ★★ | Month 7 |
| P1 | 质量根因分析 | ★★★★ | ★★★★ | Month 8 |
| P1 | 刀具成本优化 | ★★★★ | ★★★ | Month 9 |
| P2 | 交期风险预警 | ★★★ | ★★★ | Month 9 |
| P2 | 设备健康度评估 | ★★★ | ★★★★ | Month 10 |
| P2 | 能耗异常分析 | ★★ | ★★★ | Month 10 |

**Skill 2：质量根因分析**

```markdown
---
name: quality-root-cause
display_name: 质量根因分析
triggers:
  - keywords: ["良品率下降", "废品率上升", "质量异常"]
  - patterns: [".*为什么.*废品.*", ".*质量.*原因.*"]
---

# 质量根因分析 Skill

## Step 1: 不良趋势确认
查询指定时间范围内的废品率趋势，确认异常的统计显著性

## Step 2: 四维度拆解
- 按工序拆解：哪个工序废品最多？
- 按设备拆解：哪台设备废品率异常？
- 按废品类型拆解：工废 vs 料废比例变化
- 按班次拆解：是否存在班次差异

## Step 3: 交叉分析
交叉维度分析：特定设备 × 特定工序 × 特定废品类型

## Step 4: 根因推断
基于日报文本分析关联质量问题描述
结合刀具更换记录判断是否刀具寿命末期

## Step 5: 报告
```

**Skill 3：刀具成本优化分析**

```markdown
---
name: tool-cost-optimization
display_name: 刀具成本优化分析
triggers:
  - keywords: ["刀具成本", "刀具寿命", "换刀"]
---

# 刀具成本优化分析 Skill

## Step 1: 成本基线
查询月度/周度刀具成本趋势，计算单件刀具成本

## Step 2: 寿命分析
按刀具类型统计实际寿命 vs 理论寿命
识别提前报废或过度使用的刀具

## Step 3: 供应商对比
如果使用多个品牌/供应商，对比成本-寿命比

## Step 4: 优化建议
基于数据给出：换刀策略调整建议、品牌选择建议
```

### 4.4.3 任务3：Skill Builder

**目标**：让BI/分析人员可以自助创建Skill。

**设计要点**：
- 可视化流程编辑器（类似n8n或LangFlow的低代码方式）
- 或Markdown编辑器（类似Claude Code的Skill Creator）
- 支持：定义步骤 → 绑定语义模型 → 添加逻辑判断 → 测试 → 发布

**实现路径**：
1. 初期（Month 7）：Markdown模板 + 人工创建
2. 中期（Month 9）：基于Hermes Agent的对话式Skill创建（"帮我创建一个分析刀具成本的Skill"）
3. 远期（Month 12+）：独立的Skill Builder UI

## 4.5 第五阶段：自主运营与持续进化（第10-12个月）

> **核心原则**：从"工具"进化为"数字员工"。

### 4.5.1 任务1：自动化调度与主动预警

**目标**：Agent能够主动发现异常并推送预警，而非被动等待查询。

**实现方式**：
- 利用Hermes cron机制，定时运行监控Skill
- 检测到异常后通过飞书/微信推送预警
- 用户可以直接回复预警消息进行分析

**预警规则示例**：

| 预警编号 | 触发条件 | 严重级别 | 推送渠道 |
|----------|----------|----------|----------|
| ALERT-01 | 单日OEE < 基准值*80% | 红色 | 飞书+微信 |
| ALERT-02 | 废品率 > 3% | 橙色 | 飞书 |
| ALERT-03 | 连续3天产量递减 | 黄色 | 飞书 |
| ALERT-04 | 刀具寿命 < 理论值*70% | 黄色 | 飞书 |
| ALERT-05 | 设备宕机 > 2小时 | 红色 | 飞书+微信+电话 |

### 4.5.2 任务2：模型微调（可选）

**目标**：基于积累的标注数据，微调自有模型。

**数据积累**：
- 用户交互日志（问题-SQL对）
- 人工标注数据（正确/错误的生成结果）
- 用户反馈（点赞/点踩）
- Topic中验证过的业务规则

**微调策略**：
- 初期使用云端大模型API（DeepSeek/GPT/Claude）
- 积累≥5000条高质量标注数据后，考虑微调
- 微调后的模型部署在本地或私有云

### 4.5.3 任务3：Agent治理

**目标**：建立可追溯、可评估、可控制的Agent治理体系。

**治理维度**：

| 维度 | 指标 | 监控方式 |
|------|------|----------|
| 准确性 | SQL执行准确率≥95%（语义模型路径）| 评测Pipeline |
| 安全性 | Sandbox执行无越权操作 | 沙箱日志审计 |
| 可追溯 | 每次查询可回溯到原始数据和计算逻辑 | 查询日志 |
| 响应时间 | 简单查询<3s，复杂分析<30s | 性能监控 |
| 覆盖率 | 支持的查询类型覆盖80%+日常需求 | 需求匹配率统计 |
| 用户满意度 | NPS≥50 | 定期调研 |

---

# 第五部分：关键技术设计

## 5.1 元数据治理方案

### 5.1.1 治理流程（详细版）

参照原文的AI+人工协同四步法，定制机加工版本：

```
┌─────────────────────────────────────────────┐
│ Step 1: 表分组                              │
│ 输入：所有数据表                             │
│ 输出：表分组清单 + 分组业务描述               │
│ 工具：AI辅助分组 + 人工确认                   │
├─────────────────────────────────────────────┤
│ Step 2: AI生成描述                          │
│ 输入：分组后的表 + 已有脚本/文档              │
│ 输出：候选表描述 + 候选字段描述               │
│ 工具：Hermes Agent + 知识库检索              │
├─────────────────────────────────────────────┤
│ Step 3: 人工Review                          │
│ 输入：AI生成的候选描述                       │
│ 输出：审核通过的描述（采纳/修改/补充）         │
│ 工具：Obsidian审核模板                       │
├─────────────────────────────────────────────┤
│ Step 4: 血缘扩散                            │
│ 输入：已治理的核心表                         │
│ 输出：下游表的自动描述                       │
│ 工具：依赖分析脚本 → 人工确认                 │
└─────────────────────────────────────────────┘
```

### 5.1.2 字段描述模板

每个字段的统一描述模板：

```
字段名称：[field_name]
中文名称：[display_name]
业务含义：[一句话描述这个字段在业务中代表什么]
数据类型：[type]
取值范围：[min-max 或枚举值]
数据来源：[哪个系统/Excel的哪一列]
计算逻辑：[如果是派生字段，说明计算方式]
关联字段：[与其他字段的关系]
注意事项：[使用时需要注意的陷阱]
示例值：[2-3个典型值]
治理状态：[待治理/已提交/已审核]
审核人：[name]
审核日期：[date]
```

### 5.1.3 术语表（首批50个核心术语）

| 序号 | 术语 | 英文 | 定义 | 关联字段/表 | 计算公式 |
|------|------|------|------|-------------|----------|
| 1 | 计划产量 | Planned Qty | 排产计划中设定的目标产量 | fact_production.planned_qty | - |
| 2 | 实际产量 | Actual Qty | 实际完成的合格品数量 | fact_production.actual_qty | - |
| 3 | 完成率 | Completion Rate | 实际产量/计划产量 | - | actual/planned |
| 4 | 工废 | Process Scrap | 加工过程中因工艺问题产生的废品 | fact_production.process_scrap | - |
| 5 | 料废 | Material Scrap | 因原材料问题产生的废品 | fact_production.material_scrap | - |
| 6 | 宕机时间 | Downtime | 设备因故障/换模/调机等原因停止运行的时间 | fact_production.downtime_min | - |
| 7 | 总工时 | Total Hours | 班次计划运行的总时间 | fact_production.total_hours | - |
| 8 | 稼动率 | Availability | 设备实际运行时间占总可用时间的比例 | - | (总工时*60-宕机)/(总工时*60) |
| 9 | 性能效率 | Performance | 实际产出速度与理论最大速度的比值 | - | 实际*标准节拍/实际运行时间 |
| 10 | 良品率 | Quality Rate | 合格品占总产出的比例 | - | (实际-工废-料废)/实际 |
| ... | ... | ... | ... | ... | ... |

(完整术语表应包含所有工序名称、设备类型、质量指标等，建议终态≥100条)

## 5.2 Multi-Agent架构设计

### 5.2.1 Agent间通信协议

所有Agent之间通过结构化JSON通信：

```json
{
  "message_id": "uuid",
  "from_agent": "supervisor",
  "to_agent": "data_discovery",
  "type": "task_delegation",
  "payload": {
    "domain": "生产管理",
    "question": "昨天白班产量",
    "context": {
      "user_profile": {...},
      "confirmed_domain": "生产管理"
    }
  },
  "timestamp": "2026-07-05T08:00:00Z"
}
```

### 5.2.2 Human-in-loop触发规则

| 场景 | 是否触发确认 | 条件 |
|------|-------------|------|
| 数据域定位 | 触发 | confidence < 0.9 |
| 数据域定位 | 跳过 | confidence ≥ 0.9 |
| 表发现 | 触发 | 候选表 > 3 或有歧义 |
| 表发现 | 跳过 | 唯一匹配 + confidence ≥ 0.95 |
| 歧义指标 | 触发 | 多个相似指标（如两个GMV定义）|
| SQL执行 | 不触发 | 自动执行 |

### 5.2.3 上下文管理策略

| 阶段 | 加载内容 | Token估算 | 卸载内容 |
|------|----------|-----------|----------|
| 对话开始 | 用户画像 + 最近记忆 | ~500 | - |
| L1-业务域定位 | 业务域清单 + 域描述 | ~1,000 | - |
| L2-表发现 | 候选表元数据（仅名称+一行描述） | ~800 | 其他域信息 |
| L3-深度知识 | 确认表的完整Schema + 业务规则 | ~2,500 | 未选中的表信息 |
| SQL生成 | 表Schema + 相关SQL样例 + 技术元数据 | ~3,000 | 业务域清单 |
| 结果展示 | 查询结果 + 可视化参数 | ~1,000 | Schema信息 |

## 5.3 文件系统上下文设计

**目录结构**：

```
~/.hermes/data-agent/
├── catalog/                    # 元数据目录
│   ├── domains/                # 业务域定义
│   │   ├── production.yaml
│   │   ├── quality.yaml
│   │   ├── equipment.yaml
│   │   └── cost.yaml
│   ├── tables/                 # 表Schema
│   │   ├── fact_production.yaml
│   │   ├── dim_machine.yaml
│   │   └── ...
│   └── glossary.yaml           # 业务术语表
├── semantic_models/            # 语义模型
│   ├── oee.yaml
│   ├── quality_rate.yaml
│   └── tool_cost.yaml
├── skills/                     # 分析Skill
│   ├── oee-attribution.md
│   ├── quality-root-cause.md
│   └── tool-cost-optimization.md
├── knowledge/                  # 业务知识库
│   ├── rules/                  # 业务规则
│   ├── samples/                # SQL样例
│   └── faq/                    # 常见问题
├── sandbox/                    # 沙箱工作区（per session）
│   ├── session_{id}/
│   │   ├── intermediate/       # 中间结果
│   │   ├── scripts/            # 生成的脚本
│   │   └── output/             # 最终输出
├── evaluation/                 # 评测相关
│   ├── test_sets/              # 评测集
│   └── results/                # 评测结果
└── profiles/                   # 用户画像
    ├── simon.yaml
    └── ...
```

**加载策略**：

```python
class FileSystemContext:
    """文件系统上下文管理器"""
    
    def load_level(self, level: str, params: dict) -> dict:
        """按层级加载上下文"""
        if level == "L1_domain":
            # 加载业务域列表（仅名称+描述）
            return self._load_yaml("catalog/domains/")
        elif level == "L2_tables":
            # 加载指定域内的表清单
            domain = params['domain']
            return self._load_table_index(domain)
        elif level == "L3_schema":
            # 加载完整表Schema
            tables = params['tables']
            return self._load_full_schema(tables)
        # ...
    
    def unload(self, keys: list):
        """卸载指定的上下文"""
        for key in keys:
            self.context.pop(key, None)
    
    def store_intermediate(self, session_id: str, name: str, data):
        """存储中间结果到文件系统"""
        path = f"sandbox/{session_id}/intermediate/{name}.parquet"
        data.to_parquet(path)
        return {"ref": path}  # 只返回引用，不返回数据
    
    def load_intermediate(self, ref: str):
        """从文件系统加载中间结果"""
        return pd.read_parquet(ref)
```

## 5.4 Sandbox设计

**安全策略**：

| 能力 | 限制 |
|------|------|
| 文件访问 | 仅限 sandbox/session_{id}/ 目录 |
| 数据库访问 | 只读连接（SELECT only） |
| 网络访问 | 禁止（离线执行） |
| Python执行 | 白名单模块（pandas, numpy, matplotlib, json, csv） |
| 系统调用 | 禁止 |
| 资源限制 | 内存≤512MB, CPU≤2核, 超时≤60s |
| 写操作 | 仅限 sandbox/session_{id}/output/ |

## 5.5 评测体系详细设计

### 5.5.1 评测集结构

```yaml
test_set:
  name: "production_baseline_v1"
  version: "1.0.0"
  created: "2026-07-05"
  total_cases: 500
  by_topic:
    production: 200
    quality: 120
    equipment: 100
    cost: 80
  by_difficulty:
    L1_simple: 200  # 单表单字段查询
    L2_medium: 200   # 多表关联/聚合
    L3_complex: 100  # 多步分析/复杂口径
  
  cases:
    - id: "P-001"
      question: "昨天白班的总产量是多少？"
      difficulty: "L1"
      topic: "production"
      expected_sql: |
        SELECT SUM(actual_qty) 
        FROM fact_production 
        WHERE production_date = '2026-07-04' 
        AND shift = '白班'
      expected_result_hash: "a1b2c3d4"
      tags: ["产量", "单表", "聚合"]
      
    - id: "P-050"
      question: "上周OEE最低的5台设备是哪些？各自的OEE、稼动率、性能效率、良品率分别是多少？"
      difficulty: "L2"
      topic: "production"
      expected_sql: |
        SELECT machine_id, 
               (total_hours*60-downtime_min)/(total_hours*60) as availability,
               ...
        FROM fact_production
        WHERE production_date BETWEEN '2026-06-28' AND '2026-07-04'
        GROUP BY machine_id
        ORDER BY oee ASC
        LIMIT 5
      expected_result_hash: "e5f6g7h8"
      tags: ["OEE", "排行", "多指标"]
```

### 5.5.2 持续评测Pipeline

```
代码变更/配置变更/模型切换
        │
        ▼
  ┌──────────┐
  │ 触发评测  │
  └────┬─────┘
       │
       ▼
  ┌──────────┐
  │ 加载评测集│
  └────┬─────┘
       │
       ▼
  ┌──────────┐
  │ 逐条执行  │ (并行)
  │ Agent查询 │
  └────┬─────┘
       │
       ▼
  ┌──────────┐
  │ 结果比较  │
  └────┬─────┘
       │
       ▼
  ┌──────────┐
  │ 生成报告  │ → 对比上次评测
  └────┬─────┘   → 按主题/难度分组
       │         → 标记regression
       ▼
  ┌──────────┐
  │ 通知/告警 │ (准确率下降>5% → 告警)
  └──────────┘
```

---

# 第六部分：组织与运营保障

## 6.1 团队配置

### 6.1.1 角色定义

| 角色 | 人数 | 职责 | 技能要求 |
|------|------|------|----------|
| 数据负责人（Simon） | 1 | 整体规划、推动、决策 | 业务理解、数据思维 |
| 数据工程师/管理员 | 1 | 数据入仓、管道维护、元数据治理 | Python、SQL、ETL |
| 业务专家 | 2-3 | 数据审核、语义建模、Skill设计 | 生产/质量/设备专业知识 |
| AI Agent运维 | 0.5 | Agent调优、评测监控、异常处理 | AI基础知识、Hermes操作 |

> **关于AI Agent运维角色**：考虑到当前团队规模和Hermes Agent作为编排引擎的能力，该角色初期可由Simon兼任（利用Hermes的自动化能力降低人工运维成本），后期如有需要再配专人。

### 6.1.2 协作模式

```
                     ┌─────────────┐
                     │  Simon      │
                     │ (数据负责人) │
                     └──────┬──────┘
                            │
           ┌────────────────┼────────────────┐
           │                │                │
     ┌─────▼─────┐   ┌─────▼─────┐   ┌─────▼─────┐
     │ 数据工程师 │   │ 业务专家   │   │AI Agent   │
     │ (管道/治理)│   │ (审核/建模)│   │ (运维/调优)│
     └───────────┘   └───────────┘   └───────────┘
           │                │                │
           └────────────────┼────────────────┘
                            │
                     ┌─────▼─────┐
                     │ Hermes    │
                     │ Agent     │
                     │ (自动化编排)│
                     └───────────┘
```

## 6.2 运营闭环

### 6.2.1 运营流程

参照原文的运营闭环，定制为：

```
        ┌──────────────────────┐
        │  1. 用户使用Agent查询  │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  2. 反馈采集          │
        │  • 点赞/点踩          │
        │  • SQL复制执行         │
        │  • 追问/纠正          │
        │  • 人工标注           │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  3. 问题分类与优先级   │
        │  • 找表不准 → 优化元数据│
        │  • 计算错误 → 优化语义 │
        │  • 体验差 → 优化流程   │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  4. 优化迭代          │
        │  • 元数据/语义模型更新 │
        │  • Skill调整          │
        │  • 评测验证           │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  5. 效果验证 → 上线   │
        └──────────────────────┘
```

### 6.2.2 周度运营Checklist

| 任务 | 频率 | 负责人 | 产出 |
|------|------|--------|------|
| 查看Agent使用统计 | 每周 | AI运维 | 使用量、高频问题 |
| 抽查Agent回答质量 | 每周 | 业务专家 | 抽查记录、问题清单 |
| 元数据补充/修正 | 每周 | 数据工程师 | 更新记录 |
| 评测结果Review | 每周 | AI运维 | 准确性趋势报告 |
| 新Skill需求收集 | 每周 | Simon | 需求清单 |

### 6.2.3 月度运营Checklist

| 任务 | 频率 | 产出 |
|------|------|------|
| 月度准确率报告 | 每月 | 按Topic/难度分组的准确率 |
| 语义模型Review | 每月 | 模型更新建议 |
| 用户满意度调研 | 每月 | NPS分数 + 改进建议 |
| 路线图Review | 每月 | 下月优先级调整 |

## 6.3 培训计划

### 6.3.1 分角色培训

| 培训对象 | 内容 | 时长 | 目标 |
|----------|------|------|------|
| 全体管理者 | "如何用自然语言查询数据" | 1小时 | 能用Agent完成80%日常查询 |
| 业务专家 | "如何审核元数据和语义模型" | 2小时 | 能独立完成审核流程 |
| 数据工程师 | "数据管道维护和评测操作" | 3小时 | 能独立运维和调优 |
| 分析人员 | "如何创建自定义Skill" | 2小时 | 能创建基础分析Skill |

### 6.3.2 培训材料清单

1. 《Data Agent使用手册》— 常见问题示例集
2. 《元数据审核指南》— 审核标准和模板
3. 《Skill创建指南》— Markdown模板 + 示例
4. 《故障排查手册》— 常见问题及解决方案

---

# 第七部分：投入产出分析

## 7.1 资源投入估算

### 7.1.1 人力投入

| 阶段 | 角色 | 投入比例 | 人月 |
|------|------|----------|------|
| Phase 1 (Month 1-2) | 数据工程师 | 80% | 1.6 |
| Phase 1 | 业务专家 | 20% | 0.4 |
| Phase 1 | Simon | 10% | 0.2 |
| Phase 2 (Month 3-5) | 数据工程师 | 60% | 1.8 |
| Phase 2 | AI运维 | 40% | 1.2 |
| Phase 2 | 业务专家 | 10% | 0.3 |
| Phase 3 (Month 6-8) | 数据工程师 | 40% | 1.2 |
| Phase 3 | AI运维 | 50% | 1.5 |
| Phase 3 | 业务专家 | 30% | 0.9 |
| Phase 4-5 (Month 9-12) | AI运维 | 30% | 1.2 |
| Phase 4-5 | 业务专家 | 20% | 0.8 |
| **合计** | | | **~11.1人月** |

### 7.1.2 技术成本

| 项目 | 方案 | 月成本估算 |
|------|------|------------|
| 大模型API调用 | DeepSeek API（国内直连） | ¥500-2,000/月 |
| 数据库 | SQLite（零成本） | ¥0 |
| 计算资源 | 现有服务器复用 | ¥0 |
| Hermes Agent | 现有部署 | ¥0 |
| **年度总成本** | | **约¥6,000-24,000** |

> 注：模型API成本取决于调用量。初期月调用量预估在5000-20000次，按DeepSeek V3的定价（¥1/百万token输入 + ¥2/百万token输出），月成本可控在¥2,000以内。

## 7.2 预期收益

### 7.2.1 效率提升

| 场景 | 当前耗时 | 目标耗时 | 效率提升 |
|------|----------|----------|----------|
| 查询昨日产量 | 5-10分钟（找Excel→打开→定位→汇总） | 10秒 | **95%+** |
| 生成日报汇总 | 30-60分钟（查看多个日报→汇总→撰写） | 2分钟（Agent自动生成） | **95%+** |
| OEE异常归因分析 | 2-4小时（跨多个数据源排查） | 5分钟（Skill自动分析） | **95%+** |
| 月度成本分析 | 1-2天（收集数据→Excel处理→报告） | 30分钟（Agent生成+人工审核） | **75%+** |
| 数据口径确认 | 反复沟通+人工计算 | Agent自动使用已确认口径 | **100%** |

### 7.2.2 管理价值

| 价值维度 | 当前状态 | 目标状态 |
|----------|----------|----------|
| 决策时效 | 被动获取，延迟1-3天 | 实时查询，秒级响应 |
| 数据一致性 | 多人口径不统一 | 统一语义模型保证一致性 |
| 分析深度 | 表层统计 | 多维度交叉归因+根因定位 |
| 知识沉淀 | 依赖个人经验 | Skill机制将经验固化为平台资产 |
| 管理覆盖面 | 管理者精力有限 | Agent 7×24自动化监控+主动预警 |

---

# 第八部分：风险与应对

| 风险编号 | 风险描述 | 概率 | 影响 | 应对策略 |
|----------|----------|------|------|----------|
| R-01 | 数据治理推进困难（业务方不配合） | 中 | 高 | 先做最小可行治理（核心20张表），用效果说服；Simon亲自推动 |
| R-02 | 大模型生成准确率达不到预期 | 中 | 高 | 优先走语义模型路径；降低初期期望，从简单查询开始 |
| R-03 | Excel数据质量差导致入仓困难 | 高 | 中 | 建立数据质量检查+异常标记机制；逐步推动源头改善 |
| R-04 | 团队对AI工具抵触或不信任 | 中 | 中 | 渐进引入，先让团队体验"省力"的查询功能，再推分析功能 |
| R-05 | 大模型API不稳定或被墙 | 低 | 高 | 配置多模型备用（DeepSeek主+OpenRouter备）；关键场景使用本地模型 |
| R-06 | 过度依赖Agent导致人工判断力退化 | 低 | 中 | Skill设计保留人工确认环节；关键决策仍需人工审核 |
| R-07 | 数据安全风险（生产数据泄露） | 低 | 高 | 敏感数据脱敏；私有化部署；API调用不传输原始数据；Sandbox隔离 |

---

# 附录：工具链与参考资源

## A.1 核心工具选型

| 工具 | 用途 | 选型理由 |
|------|------|----------|
| SQLite | 本地数据仓库 | 零运维、足够用、Python原生支持 |
| Pandas | 数据ETL处理 | 最成熟的Python数据处理库 |
| DeepSeek API | 大模型推理 | 国内直连、性价比高、中文能力强 |
| Hermes Agent | 编排引擎 | 已有部署，cron+terminal+Agent能力完备 |
| Obsidian | 知识管理 | 已有基础设施，适合元数据和Skill存储 |

## A.2 关键技术参考

- **Multi-Agent架构**：参考原文的Supervisor+专业Agent两层设计
- **Text-to-SQL**：Spider 2.0 Benchmark揭示了企业级OLAP场景的真实难度
- **语义建模**：类似Cube.js的数据抽象层理念
- **Agent Skill**：Anthropic的Agent Skill规范（MCP + Skill定义格式）
- **评测体系**：执行准确性比较（优于AST比较和大模型比较）

## A.3 里程碑检查清单

### Phase 1 完成标志
- [ ] 所有历史Excel数据入仓（成功率≥99%）
- [ ] 数据字典覆盖核心50个字段
- [ ] 数据质量自动检查运行
- [ ] 5个Topic定义完成

### Phase 2 完成标志
- [ ] Multi-Agent架构可回答≥20类常见问题
- [ ] 简单查询（L1）准确率≥80%
- [ ] 用户画像实现（≥3个角色）
- [ ] Human-in-loop机制运行

### Phase 3 完成标志
- [ ] ≥5个语义模型上线
- [ ] 语义模型路径准确率≥95%
- [ ] 评测集≥200条
- [ ] 评测Pipeline自动化运行

### Phase 4 完成标志
- [ ] ≥3个核心Skill上线
- [ ] OEE归因分析Skill实际使用≥10次
- [ ] 用户可自助创建基础Skill

### Phase 5 完成标志
- [ ] 自动化预警上线（≥5条规则）
- [ ] 月度运营报告自动生成
- [ ] 用户NPS≥50

## A.4 原文核心方法论速查卡

> 此卡为快速查阅设计，便于实施过程中随时回顾原文精髓。

### 五大核心问题 → 五次技术跃迁

| 问题 | 跃迁方案 | 关键技术点 |
|------|----------|------------|
| 找表不准 | Multi-Agent + 渐进式披露 | Supervisor+子Agent，三层加载 |
| SQL语义错误 | 语义建模 | DSL→SQL确定性翻译 |
| SQL语法错误 | 多路生成+验证修复 | 3路并行+编译器验证 |
| 交互体验差 | 统一入口+Human-in-loop | 两层确认机制 |
| 评测缺失 | 线上SQL反向生成评测集 | 执行准确性比较 |

### 三个"不能只盯着"

1. **不能只盯着模型和工程架构**——数据质量这块脏活必须做（元数据治理让找表准确率+15%）
2. **不能只盯着线下评测**——线下高分≠线上好用（建立运营闭环）
3. **不能只盯着取数**——分析过程的可信性比结论本身更重要（Skill机制保证可追溯）

### 四层上下文知识

1. **Hive表元数据** — 最基础的表名/字段信息
2. **业务域知识文档（Mart）** — 仓库建模、使用文档、FAQ
3. **Topic运营知识** — BI同学补充的业务口径和术语
4. **技术类元数据** — 高质量SQL样例、Sample Data、表统计

---

> **文档版本**：v1.0
> **编制**：Woker（Hermes Agent）+ Simon
> **最后更新**：2026-07-05
> **下次Review**：2026-08-05（Phase 1结束后）
> **关联文档**：
> - [[产线数据管道架构]]
> - [[OEE分析体系]]
> - [[日报分析系统]]
> - [[元数据治理模板]]
> - [[Skill创建模板]]
