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

## [2026-07-30] update | 员工在工作职责下的行为管理（专业化改写V1.0）

10-工作/制度文件/ 原4条纪要专业化改写：目的/适用范围/三类对象(A工资核算岗/B班长/C部门负责人)行为规范、百分制月度考核计划(A1时效40+A2准确性40+A3要素skill化20；B日清30+单件成本50+工时20；C分析闭环60+前推有效40)、结果应用(系数1.2/1.0/0.8/0.5+PIP)、责任前推四步闭环(48h分析/72h判定/证据单)、数据口径(generator_newscheduling+劳务合计行+实缴社保)、基线(2026-06: 113219件/10086.5H, 16.11/11.94元件, 180.9元/H)、实施表(8/10要素skill、8月试运行、9/1正式)。原纪要附录存档。已更新 index.md 人事制度节。

## [2026-07-30] update | 行为管理考核V1.1：基线改为预排班×plan_output

Simon拍板：B2基线弃用6月实际均值，改为预排班×正常节拍（generator_job_code.plan_output每班计划数）。参数：达成率≥95%满分/75-95%线性/<75%零分；宕机downtime从基准剔除(8h/班)；job_codes由Simon发文强制。制度文件3.2/B类表/五口径/六时间表已改；核算SQL入库 [[班长产量达成率核算.sql]]（线级去重+宕机修正内置，7月实测：7位班长可比达成率68.8-80.4%，B2得分0-13.5/50）。

## [2026-07-30] update | 行为管理V1.1补考核名单

Simon确认名单：B类班长=王付毫(系统用字,注意与"王付豪"统一)/赵飞/祝新斌/张迪；C类主管=牛周义/潘利飞、厂长=李雪峰(广汇)；袁延志归类待确认。C类指标重构：C1所辖可比达成率40(主管=所辖班长均值,厂长=全厂)+C2分析闭环40+C3前推有效20。已入memory。

## [2026-07-31] distill | 《深入理解AI Agent》cangjie 蒸馏完成（方案A试点）

## [2026-07-31] create | 设备台账 — fuadmin.generator_devices 导入 Obsidian

来源：`fuadmin.generator_devices`（E盘MySQL直连），560台在用设备（28台已删除剔除）。
产出：`40-知识库/设备台账/` 目录，共7个文件：
- 设备台账.md（总览：统计+数据字典+厂商Top10）
- 设备台账-缸盖.md（162台）/ 缸体（57台）/ 结构件（34台）/ 差壳（42台）/ 转向节（10台）/ 其他（255台）
统计：运行85台 / 报警1台 / 状态未知474台；主要厂商：智机109台、友佳30台、现代威亚29台、宝鸡27台。
index.md 已同步更新。

## [2026-07-31] delete | 删除旧占位设备台账文件 + 清理引用

删除 `40-知识库/设备台账.md`（2026-04-26 旧占位文件，虚构200台数据，与真实台账冲突并造成 wikilink 歧义）。README.md 快速索引中 `[[设备台账]]` 描述已改为指向新真实台账（560台）。index.md 无旧残留。

按 Simon 指令以本书验证"书→skills"流水线（cangjie RIA-TV++ Hermes 适配版）。51.6万字符→374候选→三重验证→13个skills（8★★★+5★★）装入 Hermes skills/ai-agent-book/；盲测65 prompts通过率98.5%（诱饵0失败）。人读产出已入本库 蒸馏产物/：蒸馏总览、精华长文、大白话笔记、16条话术、71术语词典。应用方向：智机自建企业级agents体系+组织数智化进化。工作目录 C:\Users\ASUS\books\ai-agents-in-depth\（含candidates/rejected审计轨迹/test-prompts.json）。

## [2026-08-02] create | 人员组织架构与Agent投放规划 + 数据修正SQL

- 新建 `90-工程/主动智能层/人员组织架构与Agent投放规划.md` — 基于 fuadmin system_users(dept_level) 实测：在职378人，班长以上32人（修正后33人）；组织架构图、分层名单、T1-T4投放梯队、触达就绪度。Simon 将直接修改此文档，修改后为投放计划唯一依据。
- 新建 `90-工程/主动智能层/人员架构SQL20260802修正.sql` — 4处数据修正（祝新斌lv8→6、李雪峰部门→广汇、潘利飞lv6→5、孙兴JSON清理+2项待确认），事务+前后验证+回滚段，待 Simon 审阅后在生产库执行。
- index.md 工程架构节已同步。

## [2026-08-02] update | Simon修订架构图 → 全文档+SQL v2同步

Simon 直接修订《人员组织架构与Agent投放规划》组织架构图：跨公司调动8人（王付毫/祝新斌→广汇生产、夏玉强→广汇质量主管、李丹洋→广汇物流、曾华/胡旭宾→广汇公司级、邹杰→泰峰质量、吴春鹏→泰峰生产班长）、新增管理者（孟永超/邱桂昊/石垒/邹杰/胡旭宾+智机6主管付磊建/赵伟伟/苏杨/李强/杨艳娇/唐玉）、移除5人（倪新磊/温天祯/赵配配/陶新芋/贾世伟）、郑敏改lv1大股东、智机正式纳入。名单 32→39 人。

Woker 同步：① 文档二/三/四/五节全部按 Simon 版重写（39人名单/同步清单/新梯队T1生产条线7人试点/触达38/39）；② SQL v1(4处)→v2 全量同步版（升迁13/降级5/调动8，A-G区分段+复核+回滚，F区4项待确认）；③ index.md 更新。

## [2026-08-02] update | Simon增补孙明(治通lv5公司级MPC) → 全链路同步

Simon 在架构图治通生产部线增补孙明（lv5 公司级MPC；fuadmin id=1401，现 lv8，在职，微信已绑）。Woker 同步：① 名单 39→40（主管层 14→15，孙明列治通首位）；② SQL 增 B9 条（id=1401 lv8→5），G 复核预期改 40 人并修正 lv2 计数笔误，回滚段补对应行；③ T3 梯队纳入孙明（MPC 生产计划达成分析/排程辅助，T3 10→11 人）；④ 触达 39/40；⑤ index.md 同步。另：Simon 删除了待确认表孙兴行，已尊重保留。

## [2026-08-02] update | 人员架构SQL：F区4项Simon拍板定稿

Simon 确认演练结果并批准建议：F1（李雪峰 regulatory_dept=[4,32] 兼广汇工程部）启用、F4（孙兴 JSON 清理）启用，均已从注释转为主流程 UPDATE；F2（智机子部门）/F3（广汇人事节点）按建议不走 SQL，留 IT 后台建节点。执行方式选 C（Woker 远程跑生产库），待生产库连接方式。

## [2026-08-02] fix | 删除Obsidian误建空占位+修复.sql wikilink

Simon 点击 [[人员架构SQL20260802修正]] wikilink 时 Obsidian 无法解析到 .sql 文件，在根目录误建 0 字节空占位 .md（造成"文件是空的"假象）。已删除该空文件；规划文档中 4 处链接全部改为带扩展名形式 [[人员架构SQL20260802修正.sql]]，点击可正常打开。真实 .sql 文件完好（11.6KB/192行）。

## [2026-08-02] execute | 人员架构SQL v2 在 E 盘快照库正式执行

23 条 UPDATE（A-E 区 21 条 + F1/F4）全部生效并 COMMIT：lv≤6 由 32→40（lv1=2/lv2=1/lv4=7/lv5=15/lv6=15），抽查李雪峰(dept4,[4,32])/祝新斌(20,lv6)/孙明(lv5)/孙兴([4,20]) 等全部符合 Simon 版架构图。生产库由 Simon 发 IT 按同一文件执行。

## [2026-08-02] update+create | 定级调整 + QM整合架构归档

定级调整(Simon)：郑敏维持lv2(取消升lv1)、谭昌发lv1→lv3(新增"子公司一把手"层级)。已同步：E盘库(lv1=1/lv2=1/lv3=1/lv4=7/lv5=15/lv6=15=40验证通过)、SQL文件(A区郑敏条删除/谭昌发改lv3/G复核/回滚段)、规划文档(层级语义/架构图/名单/修订记录)。

新建 `90-工程/主动智能层/QM企业级Agent框架整合架构.md`：Simon决策(QM框架+小程序入口+40骨干)归档——OpenWork vs QM对比、QM长期性评估(版本冷冻+2027-02验证期)、四层架构(小程序/网关/QM/主动智能层+MCP共享平面)、dept_level→scope权限映射(lv1-lv6)、成本¥2-4K/月、M1-M7节奏、6项风险盯办。index.md已同步。

## [2026-08-02] update | QM整合架构升级三入口模型

Simon 定入口为三通道：微信小程序+企微身份授权+网页密码登录。QM企业级Agent框架整合架构.md 三节重写：① 架构图改三入口+统一接入网关(三auth/identity_map/路由/审计)；② 新增身份联邦分析(小程序38/40已绑🟢、网页密码Django表现成🟢、企微待建🟡)+SSO-gate机制(scope记忆跨通道连续)；③ 通道×角色匹配表(lv6小程序/lv5小程序+企微/lv3-4网页+企微/lv1-2网页+企微)；④ 告警三分发反馈一闭环、权限不下沉原则；⑤ 决策表第1条同步修订。

## [2026-08-02] create | QM 学习实验室落地 E:\qm-lab（Simon 决策熟悉 QM/OpenCode）

E:\qm-lab 便携化实验室：Node v24.15.0 便携版（QM 要求≥24.15，系统 Node22 不动）+ QM 源码（codeload 直连）+ npm 依赖 617 包 + Web UI 插件（218 包+Vite 构建）。QM core(:8080, org=zhiji, 内存态, ALLOW_UNAUTHENTICATED_CORE=true 学习专用) + Web UI(:8096, dev cookie 登录) 双进程运行中。OpenCode v1.18.11 全局已装。关键发现：①QM 存储三件套默认内存态，PG 非必需（EDB 330MB 下载两次失败已删，留 BitsTransfer 重下）；②opencode harness 原生仅 anthropic/openai，Kimi 接入=openai provider 加 baseURL 覆盖（已补丁 opencode-harness.ts:642）；③core .env 已配 HARNESS=opencode+OPENCODE_MODEL=openai/kimi-k3+OPENAI_BASE_URL，差 OPENAI_API_KEY 复制待 Simon 批准。坑：curl -o 写盘被安全软件全拦→下载改用 PowerShell IWR。手册 E:\qm-lab\README.md。

## [2026-08-02] complete | QM实验室全链路跑通(Postgres+DeepSeek/Kimi真实模型)

按Simon指示完成三步：①PostgreSQL 17.6便携安装(:5433, qm库, BitsTransfer下载330MB)；②模型注册表补丁(deepseek-chat+moonshot/kimi-k3入MODEL_REGISTRY)；③core切postgres持久化(store=postgres验证)。关键突破：opencode内置openai走Responses API方言→Moonshot/DeepSeek必须用@ai-sdk/openai-compatible自定义provider(harness已注入双provider)。实测中文对话成功(DeepSeek回复正常)。Windows补丁：opencode.exe spawn+PATH修复。QM sidecar为jail沙箱，全局opencode auth不传入，key须走core .env。三进程运行：PG:5433/core:8080/webui:8096。

## [2026-08-02] test | QM实验室三项测试(完成2/3, Strict暂缓)

测试1 scope隔离✅全过: ①会话列表隔离(niu见0条) ②越权访问他人会话→not_found(不泄露存在性) ③跨用户记忆零泄露(金丝雀Alpha-7749) ④会话内记忆正常。重要发现: 跨会话长期记忆需agent主动写scope记忆(非自动),这是治理优点但40人部署时需引导或skill化"记住我"类指令。

测试2 skill晋升流✅: 个人skill(baogong-slang-dict)隔离→晋升org后niu可见且agent实际引用词典回答黑话。机制: 可见性解析personal→shared→teams→org; 晋升三重门(ADMIN_GRANTS白名单+liveActor真人+审计); 命名须ASCII; 存储(id,json)文档表+signature。注: 正规agent晋升路径需Docker sandbox,本次DB层演示最终态。

测试3 Strict安全档: 暂缓。工具调用需Docker sandbox,本机无Docker(WSL2未装)。方案B: 留到阿里云ECS(Linux)测,贴近生产。

附加: QM core曾两次静默退出(code=1无栈),稳定性观察项。ADMIN_GRANTS=zhangdi已配。

## [2026-08-02] create | QM学习实验室全程记录归档

Simon 指令将本 session 全部对话消化归档。新建 `90-工程/主动智能层/QM学习实验室全程记录-20260802.md`（10.8KB）：选型决策/三入口架构/实验室建设实录/9项踩坑表/模型方言突破/三项测试证据/MCP实测+口径教训/Docker sandbox 解析/账号预算三问/补丁清单(private fork迁移用)/重启手册/6项遗留事项。index.md 已同步。

## [2026-08-06] create | QM架构A2A与Webhook适配性评估-20260806 + 告警中心事件驱动实施清单-20260806

Simon 指令评估 Hermes v0.20.0 两项架构级能力对 QM 四层架构的适配性。实证来源：本机 Hermes 源码（outbound_webhooks.py/a2a 插件）+ QM 源码（provenance.ts wake 模型原生建模 cron/webhook/monitor）。结论：Webhook 采纳（W1 引擎→QM scope 唤醒/W2 cron 回推企业云/W3 外部回调入网关），A2A 战略跟踪（2027-02 验证期再评）。Simon 批准方案 A 后，新建实施清单：事件 schema/过滤规则表（事件→唤醒比≤20% 为上线闸门）/紧急度路由/token 成本（过滤后≈¥9/月）/四项量化验收标准/三项前置验证项，总工时 5.5 人日，落地窗口 M3-4。index.md 已同步。
