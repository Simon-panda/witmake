# 企微 + Chatwoot + Memos + Dify + OpenClaw + Obsidian 整合方案

> **问题原点**：员工通过企微与 AI 交互 → 对话怎么记住 → 跨工具怎么串起来。
> **一句话结论**：Memos 不是这个场景的正确答案。对话记忆应该做在 Dify 层，Memos 应该用作"人写的备忘录"——两者分工明确。
> **适用对象**：IT 负责人、AI 团队——这是一份集成选型与架构决策文档。

---

## 第一部分：每个工具在这个体系里的角色

在开始谈"怎么串"之前，先把每个工具的定位定死——避免一个工具做不该它做的事。

| 工具                             | 在这个体系里的角色                                            | 不做什么                           |
| ------------------------------ | ---------------------------------------------------- | ------------------------------ |
| **企微（WeChat Work）**            | 用户界面——员工在这里跟 AI 说话、收到告警、点反馈按钮                        | 不存对话历史（企微只管消息通道）               |
| **Dify**                       | AI 大脑——LLM 编排、工作流、RAG 知识库、对话管理、Agent 决策路由            | 不做通知推送（它不面向用户）                 |
| **OpenClaw**                   | 备用 Agent 引擎——部分 Agent 场景可切到 OpenClaw 跑，双引擎互为备份       | 不替代 Dify 做工作流编排                |
| **Chatwoot**                   | 统一会话收件箱——"企微上员工问 AI"的对话，可以在 Chatwoot 后台看到全量记录，支持人工接管 | 不做 AI 推理（它是会话管理，不是 AI 引擎）      |
| **Memos**                      | 人肉备忘录——班组长/工艺随手记的东西：换班备忘、异常发现、经验教训                   | 不做 AI 对话记忆（它不是向量库，没有语义搜索）      |
| **Obsidian**                   | 结构化知识库——SOP、方案文档、技术规范、项目计划                           | 不做实时对话交互（它是长文知识，不是聊天记录）        |
| **MCP Server 层**               | 数据管道——把 MES/刀具/CMM/HR 的数据统一接出来                       | 不做推理或存储                        |
| **向量数据库（DashVector/pgvector）** | 对话长期记忆的存储和检索——"3 个月前张三问过类似的问题"                       | 不做原始对话记录（存的是 embedding，不是原文归档） |
| **MySQL/PostgreSQL**           | 所有结构化数据的落地——告警、状态转移、对话日志、反馈记录                        | 不做语义搜索                         |

---

## 第二部分：Memos 要不要上？要，但不是你想的那个用途

### Memos 的真相

Memos 是一个单二进制文件的轻量笔记工具（Go 语言），核心功能是：
- 写短笔记（类似 Twitter/微博的短内容流）
- 支持 Markdown、标签、图片
- 有 RESTful API
- 可以自部署

**它没有"企业版"**——只有社区开源版，没有官方企业版。社区有人做多用户支持，但不是 Memos 原生的设计意图。

### Memos 在这个体系里的正确用法

`
❌ 错误用法：
   "把员工和 AI 的对话存到 Memos"
   → Memos 没有语义搜索、没有向量化、没有对话管理
   → 你等于用便签纸存聊天记录——能存，但查不到

✅ 正确用法：
   "班组长在巡线时发现 CNC-03 有异响，掏出手机在 Memos 上记一笔"
   → 这条备忘可以被 Dify 的 RAG 检索到
   → 下次有人问"CNC-03 最近有什么异常"，AI 能翻出这条备忘
`

### 具体场景举例

**场景 A：交接班备忘**

`
夜班班组长（凌晨 3:00 巡线）：
  在 Memos 上写：
  "CNC-03 T-2031 今天换刀后首件偏上差 +0.012，我已经调到 +0.005。
   白班注意观察孔径趋势，如果继续漂就提前 200 件换刀。"
  标签：#交接 #CNC03 #T2031

白班班组长（早上 7:00 上班）：
  打开 AI 助手问："昨晚夜班有什么要交接的？"
  AI 从 Memos 里搜到这条备忘，摘要回复
`

**场景 B：工艺经验沉淀**

`
工艺工程师（调试过程中）：
  在 Memos 上记：
  "BR-2031-A 用 T-2031 时，如果换山东 X 钢那批次料，转速降 10%，
   否则刀具寿命对半砍。已验证 3 次。"
  标签：#工艺经验 #BR2031A

3 个月后新来的工艺工程师：
  问 AI："T-2031 加工 BR-2031-A 有什么要注意的？"
  AI 从 Memos 召回这条备忘 + Obsidian 里的正式 SOP
`

### 结论：Memos 不需要"企业版"，社区版就够

Memos 在这个体系里是**"人写 → AI 读"**的单向管道。一个人写，AI 通过 API 拉取。不需要多租户、不需要权限体系、不需要工作流——这些需求在 Dify 和企微里已经覆盖了。

---

## 第三部分：对话记忆——真正该怎么做

### 你要解决的问题拆开看

"记住员工的对话"听起来是一个需求，实际上是三个：

| 层次 | 需求 | 存储位置 | 检索方式 |
|---|---|---|---|
| **会话内记忆** | 同一轮对话里，AI 记得你 3 分钟前说了什么 | LLM 上下文窗口 | 不需要额外存储 |
| **跨会话记忆** | 3 天后你回来问"上次那个刀补问题解决了吗"，AI 记得 | 向量数据库 + Dify 对话管理 | 语义检索 → 注入当前 Prompt |
| **组织记忆** | 所有员工的对话中，提取出共性问题、高频异常、经验沉淀 | Obsidian（人工整理）+ Memos（随手记）+ 向量库（自动索引） | 混合检索 |

### 推荐方案：Dify 对话管理 + 向量库（不是 Memos）

`
┌─────────────────────────────────────────────────────────┐
│                    员工通过企微提问                        │
│               "CNC-03 T-2031 还能用多久？"                 │
└────────────────────────┬────────────────────────────────┘
                         │ 企微消息回调
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  Chatwoot（会话收件箱）                     │
│  - 接收企微消息，创建 Conversation                        │
│  - Webhook → Dify                                         │
│  - 如果 AI 答不上来 → 标记为"待人工"                      │
│  - 支持人工客服在 Chatwoot 后台直接回复                     │
└────────────────────────┬────────────────────────────────┘
                         │ Webhook
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   Dify（AI 大脑）                          │
│                                                          │
│  ① 接收消息                                               │
│  ② 从向量库检索相关历史对话                                │
│     - "这个员工 3 天前问过刀具寿命问题"                    │
│     - "CNC-03 最近一周有 3 个人问过类似问题"               │
│  ③ 从 Memos 检索相关备忘                                  │
│     - "夜班交接备忘提到 T-2031"                           │
│  ④ 从 Obsidian 知识库检索相关 SOP                          │
│     - "T-2031 标准寿命 1200 件"                           │
│  ⑤ 从 MCP Server 拉实时数据                               │
│     - "当前 T-2031 已加工 847 件，剩余 29.4%"             │
│  ⑥ 组装 Prompt → LLM 生成回答                             │
│                                                          │
│  ⑦ 把本轮对话存入向量库（供下次检索）                        │
│  ⑧ 把对话摘要写入 MySQL（供审计）                           │
│  ⑨ 如果 LLM 不确定 → 回传 Chatwoot 标记"待人工"           │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    企微（回复员工）                         │
│  AI 直接回复，或者人工在 Chatwoot 后台回复                   │
└─────────────────────────────────────────────────────────┘
`

### 对话记忆的数据流

`python
# 伪代码——一次完整的"记住+回答"流程

def handle_employee_message(employee_id, message):
    # Step 1: 查这个员工的历史
    history = vector_db.search(
        query=message,
        filter={"employee_id": employee_id},
        top_k=5
    )

    # Step 2: 查全局相关对话（跨员工）
    global_context = vector_db.search(
        query=message,
        filter={"domain": "tool_life"},  # 按领域限定
        top_k=3
    )

    # Step 3: 拉实时数据
    tool_data = tool_mcp.query(tool_id="T-2031")
    shift_notes = memos_api.search(tags=["交接", "CNC03", "T2031"])
    sop = obsidian_kb.search(query="T-2031 寿命")

    # Step 4: 组装 Prompt
    prompt = f"""
    你是机加工 AI 助手。员工 {employee_id} 问：{message}

    [该员工最近对话]:
    {format_history(history)}

    [全局相关对话]:
    {format_history(global_context)}

    [实时数据]:
    T-2031 当前寿命：{tool_data.remaining_life_pct}%
    累计加工：{tool_data.total_parts_cut} 件

    [班组长备忘]:
    {format_memos(shift_notes)}

    [相关 SOP]:
    {format_sop(sop)}

    请基于以上信息回答。如果不确定，请明确说明。
    """

    answer = llm.generate(prompt)

    # Step 5: 存入记忆
    vector_db.insert(
        text=f"员工{employee_id}问: {message}\nAI答: {answer}",
        metadata={
            "employee_id": employee_id,
            "timestamp": now(),
            "domain": classify_domain(message),
            "requires_followup": answer.contains_uncertainty()
        }
    )

    # Step 6: 如果不确定，标记到 Chatwoot
    if answer.contains_uncertainty():
        chatwoot.tag_conversation(conversation_id, "needs_human")

    return answer
`

---

## 第四部分：六个工具的组合架构图

`mermaid
flowchart TD
  subgraph 用户层["用户层"]
    WX["企微<br/>员工交互入口"]
    CW_UI["Chatwoot 后台<br/>人工客服/HR查看"]
    OB_UI["Obsidian<br/>知识库管理"]
    MEMOS_UI["Memos<br/>备忘记录"]
  end

  subgraph 会话层["会话层"]
    CW["Chatwoot<br/>统一会话管理<br/>· 接收企微消息<br/>· 对话归档<br/>· 人工接管"]  
  end

  subgraph AI层["AI 推理层"]
    DIFY["Dify<br/>LLM编排+工作流<br/>· RAG知识检索<br/>· Agent决策<br/>· 对话管理"]
    OC["OpenClaw<br/>备用Agent引擎<br/>· 部分场景分流"]
  end

  subgraph 记忆层["记忆与知识层"]
    VDB["向量数据库<br/>DashVector/pgvector<br/>· 对话embedding<br/>· 语义搜索"]
    MYSQL["MySQL<br/>· 对话记录归档<br/>· 告警+状态机<br/>· 审计日志"]
    MEMOS["Memos<br/>· 人写的备忘<br/>· AI可检索"]  
    OB["Obsidian<br/>· 正式SOP<br/>· 方案文档<br/>· 技术规范"]
  end

  subgraph 数据层["数据接入层（MCP）"]
    MCP["MCP Server 集群<br/>刀具/三坐标/对刀仪/MES/HR/SPC"]
  end

  WX <-->|"消息收发"| CW
  CW <-->|"Webhook"| DIFY
  DIFY <-->|"备援"| OC
  DIFY -->|"检索"| VDB
  DIFY -->|"检索"| MEMOS
  DIFY -->|"检索"| OB
  DIFY -->|"实时数据"| MCP
  DIFY -->|"写入日志"| MYSQL
  DIFY -->|"标记待人工"| CW
  CW_UI -->|"人工回复"| CW
  MEMOS_UI -->|"备忘写入"| MEMOS
  OB_UI -->|"文档管理"| OB

  style 记忆层 fill:#fef9e7,stroke:#e67e22
  style AI层 fill:#e8f0ff,stroke:#48f
  style 会话层 fill:#e8f8e8,stroke:#4a4
`

---

## 第五部分：为什么不用 Memos 存对话记忆（技术对比）

| 维度                 | Memos                | Dify 对话管理 + 向量库           |
| ------------------ | -------------------- | ------------------------- |
| **语义搜索**           | 不支持（只能关键词模糊匹配）       | 原生支持（embedding 向量检索）      |
| **"3 天前张三问过类似问题"** | 查不到（除非手工加标签、翻页找）     | 自动检索（向量相似度 > 0.85 召回）     |
| **多轮对话上下文**        | 不保留（Memos 按时间线，不按对话） | Dify 原生管理 Conversation ID |
| **自动摘要**           | 不支持                  | Dify 工作流可配置"每日对话摘要"       |
| **API 集成**         | 有 RESTful API        | Dify 原生 API + 向量库高性能查询    |
| **权限管理**           | 无（谁都能看）              | Dify 有应用级权限               |
| **数据量**            | 适合几百条备忘              | 适合百万级对话 embedding         |
| **部署复杂度**          | 极简（单二进制）             | 需要 Dify + 向量库（但你已经在用了）    |

**结论：不是 Memos 不好，是它的设计目标和"对话记忆"不匹配。就像你不会用微信聊天记录来写 SOP——工具要用对地方。**

---

## 第六部分：部署顺序与优先级

### 短期（2 周内）——对话能跑起来

`
1. Dify 对话应用搭建（1 天）
   - 创建一个"机加工 AI 助手"应用
   - 配置系统 Prompt（你是谁、你能回答什么）
   - 接通通义千问 LLM

2. 企微 → Chatwoot → Dify 消息通路（3 天）
   - 企微应用配置消息回调 URL → 指向 Chatwoot
   - Chatwoot Webhook → 指向 Dify API
   - 验证：员工在企微说话 → AI 回答回来

3. 对话日志写入 MySQL（1 天）
   - 每轮对话写一条记录：employee_id, question, answer, timestamp
   - Dify 工作流里加一个"写日志"节点

4. 向量库部署（2 天）
   - 用阿里云 DashVector（已在阿里云生态内）
   - Dify 知识库连接 DashVector
   - 写一个定时任务：每天把 MySQL 里的新对话 embedding 后写入向量库
`

### 中期（4 周内）——记忆生效

`
5. Dify RAG 配置（2 天）
   - 把向量库作为知识库接入 Dify
   - 配置检索策略：先搜历史对话 → 再搜 Obsidian → 最后搜 Memos

6. Memos 部署 + API 打通（2 天）
   - 部署 Memos（docker 一行命令）
   - 让 Dify 通过 HTTP 调用 Memos API 检索备忘

7. Memos 使用培训（1 天）
   - 教会班组长和工艺工程师怎么用
   - 核心习惯：换班时花 2 分钟写 3 条备忘
`

### 长期（2 个月后）——记忆智能

`
8. 对话自动摘要（1 周）
   - 每天凌晨自动把昨天的对话生成摘要
   - 推送给 HR 经理："昨天员工问了 47 个问题，高频话题：刀具寿命(12)、交接班(8)、尺寸偏差(6)"

9. 自动提炼知识（2 周）
   - 当某类问题被问了 10 次以上 → 自动建议 HR 经理："要不要把这段写进 SOP？"
   - 一键从对话生成 Obsidian 知识库条目

10. OpenClaw 分流（1 周）
    - 简单查询（"T-2031 剩余寿命"） → Dify 处理
    - 复杂推理（"这个零件不良的原因可能是什么"） → OpenClaw 处理
    - 双引擎路由规则在 Chatwoot Webhook 层做
`

---

## 第七部分：成本估算

| 项目 | 月度费用 | 说明 |
|---|---|---|
| Dify Cloud 团队版 | ¥500 | 对话管理 + 工作流编排 |
| 阿里云 DashVector | ¥300 | 对话 embedding 存储（10 万条级别） |
| Chatwoot 自部署 | ¥0（ECS ¥200） | 开源版自部署在 ECS 上 |
| Memos 自部署 | ¥0（同上 ECS） | Docker 一行命令 |
| Obsidian | ¥0 | 已有 |
| 企微 | ¥0 | 已有 |
| 通义千问 Token | ¥300-800 | 按日对话量 200-500 轮估算 |
| ECS（Chatwoot + Memos） | ¥200 | 2C4G 即可 |
| MySQL（对话日志） | ¥0（复用现有 RDS） | 告警库旁边加一张 conversation_logs 表 |
| **月度合计** | **¥1,500-2,000** | 不含已有基础设施 |

---

## 第八部分：一句话总结

`
企微      = 员工的手和眼（在哪用）
Chatwoot  = 对话的记录本（谁说了什么）
Dify      = AI 的大脑（怎么回答）
向量库     = AI 的长期记忆（记得什么）
Memos     = 人的便利贴（随手记了什么经验）
Obsidian  = 公司的说明书（标准是什么）
MCP       = 数据的管道（实时数据从哪来）
`

**Memos 不需要"企业版"。对话记忆的正确做法是 Dify + 向量数据库，Memos 的正确用法是"人的备忘 → AI 检索"。两者互补，不互相替代。**

---

*文档生成日期：2026-07-12*
*建议下一步：①确认企微消息回调 URL 能否指向自部署服务（网段/防火墙） / ②评估 Chatwoot 自部署 vs 直接用 Dify 收企微消息（如果对话量不大，可以先跳过 Chatwoot，简化第一版） / ③给班组长做 15 分钟 Memos 试用——看他们愿不愿写*
