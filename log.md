# Wiki Log — 智机工业知识库

> **操作日志**。追加模式，记录所有知识库操作。
> 格式：`## [YYYY-MM-DD] action | subject`
> 操作类型：ingest, create, update, query, lint, archive, delete
> 超过 500 条后轮转：重命名为 `log-YYYY.md`，新建此文件。
> Agent 维护——每次操作后追加。

---

## [2026-07-05] create | LLM Wiki 模式初始化

### 基于 Karpathy LLM Wiki 模式建立知识库基础设施

**创建的文件：**
- `SCHEMA.md` — 结构约定、标签分类、页面类型、操作规范
- `index.md` — 内容目录，按域分节，涵盖现有主要页面
- `log.md` — 本文件，操作日志
- `raw/` 目录 — 不可变源材料层（articles/, papers/, transcripts/, assets/）

**背景：**
分析了 Karpathy 的 [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)（最后更新 2026-07-05），对比已有 `llm-wiki` skill (v2.1.0)，确认 skill 已包含全部原文内容并扩展了工程化细节（来源溯源标记、置信度标注、sha256漂移检测、12点Lint等）。

**现有 Vault 诊断：**
- ✅ 内容丰富，覆盖 10+ 域
- ✅ 已使用数字前缀分层目录（PARA-like）
- ❌ 缺少 SCHEMA.md（无统一约定）
- ❌ 缺少 index.md（无内容目录）
- ❌ 缺少 log.md（无操作记录）
- ❌ 缺少 raw/ 层（源材料与合成页面混放）
- ❌ 根目录有 `未命名.md`、`未命名.canvas` 等孤立文件
- ❌ macOS 资源分支文件（`._` 前缀）散落各处

**下一步：全部完成 ✅**
- ✅ 创建 raw/ 目录结构
- ✅ 将 Karpathy LLM Wiki 原文收入 raw/articles/
- ✅ 清理根目录：删除 6 个未命名文件 + 242 个 macOS 资源分支文件
- 为关键页面逐步补充 frontmatter（持续）

---

## [2026-07-05] cleanup | 清理孤立文件与资源分支

**删除的文件：**
- `未命名.md`（空文件，0字节）
- `未命名.canvas`, `未命名 1.canvas`, `未命名 2.canvas`, `未命名 3.canvas`, `未命名 4.canvas`（空画布，各2字节）
- `未命名/` 和 `未命名 1/` 空目录
- 242 个 macOS 资源分支文件（`._` 前缀），分布在 `00-Inbox/`, `10-工作/`, `20-学习/`, `30-项目/`, `40-知识库/` 各子目录

---

## [2026-07-05] update | 批量补充 frontmatter + 源材料入库

**补充 frontmatter 的页面（5个）：**
- `30-项目/企业级数据Agent落地方案.md` — type:project, domain:工程, tags:[AI, agent, text-to-sql, 数据管道, 方案, 语义模型, Skill]
- `30-项目/企业级数据Agent落地方案v2.md` — type:project, domain:工程, tags:[AI, agent, text-to-sql, 主动智能层, MCP, 方案, 语义模型, Skill, 风险目录]; supersedes v1.0
- `90-工程/主动智能层/主动智能层_首批风险清单与架构方案.md` — type:project, domain:工程, tags:[AI, agent, 主动智能层, 风险目录, 预测, 根因分析, CNC, 方案]
- `90-工程/主动智能层/主动智能层_优化版实施方案.md` — type:project, domain:工程, tags:[AI, agent, 主动智能层, 方案, 路线图, 成本模型, 降级方案, 组织变革]
- `90-工程/主动智能层/工作分配与API建设深度拆解.md` — type:project, domain:工程, tags:[AI, agent, MCP, API, 刀具磨损, RACI, 主动智能层, 方案]

**收入 raw/articles/ 的源材料（5个）：**
- `raw/articles/karpathy-llm-wiki-2026-07.md` — Karpathy LLM Wiki gist 原文
- `raw/articles/infoq-data-agent-2026-07.md` — InfoQ 企业数据Agent文章（从v1.0方案中提取）
- `raw/articles/主动智能层_首批风险清单与架构方案.md` — 复制自 90-工程/主动智能层/
- `raw/articles/主动智能层_优化版实施方案.md` — 复制自 90-工程/主动智能层/
- `raw/articles/工作分配与API建设深度拆解.md` — 复制自 90-工程/主动智能层/

**更新 index.md**：新增 `源材料 (raw/articles/)` 节，添加 5 个条目。

## [2026-07-17] create | 治通试漏数据分析 20 维度报告入库（22 页）

**来源**：zt_server_data MySQL 数据库（F:\，治通试漏/检测数据 35 表 700 万条），由 Kanban factory-ops 看板 4 个 Agent（quality/production/equipment/analyst）并行分析产出，原始文件在 F:\zt_analysis\（含可复现 SQL）。

**新建目录**：`70-质量/治通试漏数据分析/`

**入库页面（22个）：**
- `治通试漏数据分析-总报告.md` — 执行摘要+5大跨报告验证发现+P0/P1/P2统一行动清单
- `zt_server_data数据库上下文.md` — 35表结构/连接/数据陷阱
- 数据地基：`A1-数据质量审计.md`、`A2-主数据对齐.md`
- 质量：`Q1-密封合格率基线.md`、`Q2-50T缸盖不良主因.md`、`Q3-缸体密封失效模式.md`、`Q4-断芯尺寸过程能力.md`、`Q5-燃高SPC.md`、`Q6-差壳出货质量.md`、`Q7-泄漏量漂移监控.md`
- 生产：`P1-生产线产量与型号结构.md`、`P2-检测节拍分析.md`、`P3-追溯链贯通率.md`、`P4-差壳出货物流.md`、`P5-型号切换pattern.md`、`P6-班次对比.md`
- 设备：`E1-设备利用率画像.md`、`E2-设备异常信号.md`、`E3-打码设备健康度.md`、`E4-视觉检测效能.md`、`E5-差壳重码溯源.md`

**更新 index.md**：新增 `质量管理 (70-质量/)` 节及全部 22 个条目。

## [2026-07-17] rename | 70-质量/治通试漏数据分析 → 70-质量/治通SQL20260718分析

按 Simon 要求重命名文件夹，index.md 章节名同步更新。页面文件名与 wikilinks 不受影响。

## [2026-07-23] create | fuadmin数据字典 54页入 90-工程/fuadmin数据字典/

治通MES/ERP（fuadmin库）逆向工程：334基表/5,877字段全覆盖，产出总览（语义图谱+数据陷阱TOP10）、关联矩阵（288条）、54份模块agent基础文件、字段备注整改计划（5,621条建议+remediation.sql）。原始注释覆盖率仅2.2%，语义推断均标依据与置信度。已更新 index.md 工程架构节。

## [2026-07-24] create | fuadmin数据字典2 63页入 90-工程/fuadmin数据字典2/

治通MES/ERP 源码级重解析：解压 backend(Django)+web(Vue3) 源码，AST解析150个model文件(280类/3,010字段)，代码×DB对齐 5,321/5,877字段(90.5%)有程序锚点。语义来源升级为 verbose_name/help_text/choices枚举/行内注释；6个业务域多agent并行精修(A1/A2/A4/A6完成,A3/A5规则兜底)，枚举全解码，594条关联(544代码级)。前端label提取3,070条做第三重佐证。产出63份文档：总览/7域模块字典/业务流代码验证版/关联图谱2/新旧差异报告(2,608条旧推断升级实证)。已更新 index.md。流水线脚本在 C:\Users\ASUS\{parse_models,align_code_db,synth_baseline,build_dict2}.py，中间产物在 fuadmin-code-analysis\。

## [2026-07-27] create | 深入理解AI-Agent 开源书籍入 40-知识库/深入理解AI-Agent/

李博杰《深入理解 AI Agent：设计原理与工程实践》（github.com/bojieli/ai-agent-book，22.2k⭐，Apache-2.0）全书入库：引言+10章+后记+思考题参考答案共13个markdown（1.4MB正文）+133张配图（images/），sparse-checkout 经 gh-proxy 镜像拉取。章节文件按中文章节名重命名，图片相对路径保持有效。另建入口页「深入理解AI-Agent-总索引」（含章节导航、核心公式、与本厂MCP/数据Agent/多Agent系统的关联映射）。配套PDF（11MB）入 raw/assets/。92个实验代码未入库（依赖外部仓库，链接保留在入口页）。已更新 index.md 知识库节。

## [2026-07-28] migrate+update | MySQL迁移F→E + fuadmin字典2备注落库

①MySQL 8.0.29物理迁移：F:/mysql-8.0.29-winx64+F:/mysql-data(15.49GB) → E盘对应路径，robocopy 5分15秒(521MB/s)。三库完整(fuadmin 355/zt_server_data 35/zt_produce 43表，6403列)，大表行数抽查一致。当前E盘库console模式运行(proc_6836c5497012)；服务MySQLZT注册仍指F盘(STOPPED)，需管理员修正(命令见执行报告)。F盘原目录保留。②字典2备注落库：remediation2.sql(表级334+列级5855条)执行44秒，表备注100%、列备注99.3%(6325/6369)，44列未覆盖均为视图；1条json超长已截断修复。SQL+快照归档 90-工程/fuadmin数据字典2/附件/，报告 [[fuadmin字段备注整改执行报告2]]。已更新 index.md。

## [2026-07-28] fix | MySQLZT服务注册修正完成

Simon管理员PowerShell执行：sc.exe delete(实际已删,标记删除在mysqld停止后生效)→E盘mysqld --install→sc.exe start。验证：服务RUNNING、BINARY_PATH=E盘、@@datadir=E:/mysql-data、三库表数完整、备注覆盖率保持(列6325/6369,表355/355)。重启自启恢复。坑：PowerShell中sc是Set-Content别名,须用sc.exe。

## [2026-07-28] create | 智机日报7月提交情况分析入 10-工作/人事/

数据源 fuadmin.generator_liqiang_report_journals（快照窗口7/1~7/21，15工作日）：38人提交436条。分档：优秀8/良好11/一般8/偏差4/异常7。7月零提交5人中3人离职合理（孙永金/宋家伟/袁明），李秀娟7/10离职，李丹洋在职零提交为真异常；张方印6月全勤7/9起断交。人事部换血：刘文婕7/13入职补位。账号映射走 system_users.wechat_id（37/38可映射）。报告 [[智机日报7月提交情况分析]]。
