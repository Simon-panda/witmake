---
title: 企业级数据Agent落地方案 v2.0：主动智能 + 智能取数的统一架构
created: 2026-07-05
updated: 2026-07-05
type: project
domain: 工程
tags: [AI, agent, text-to-sql, 主动智能层, MCP, 方案, 语义模型, Skill, 风险目录]
sources:
  - raw/articles/infoq-data-agent-2026-07.md
  - raw/articles/active-intelligence-risk-catalog-2026-06.md
  - raw/articles/active-intelligence-optimized-plan-2026-06.md
  - raw/articles/active-intelligence-work-assignment-2026-06.md
confidence: high
supersedes: "[[企业级数据Agent落地方案]]"
---

# 企业级数据Agent落地方案 v2.0：主动智能 + 智能取数的统一架构

> **版本**：v2.0（重大升级）
> **编制日期**：2026-07-05
> **适用对象**：机加工制造企业（200台CNC，40+产线）
> **关联文档**：
> - [[企业级数据Agent落地方案]]（v1.0 — 基于InfoQ原文的单线方案）
> - [[主动智能层_首批风险清单与架构方案]]（预测+定位统一引擎）
> - [[主动智能层_优化版实施方案]]（6阶段路线+数据审计+降级方案）
> - [[工作分配与API建设深度拆解]]（MCP Server架构+刀具磨损深度案例）

---

## 目录

- [v2.0 升级说明：为什么需要重构](#v20-升级说明为什么需要重构)
- [第一部分：双源合流——InfoQ + 主动智能层的交叉增强](#第一部分双源合流infoq--主动智能层的交叉增强)
- [第二部分：统一架构——问守双模Agent引擎](#第二部分统一架构问守双模agent引擎)
- [第三部分：数据接入层——MCP Server替代全量入仓](#第三部分数据接入层mcp-server替代全量入仓)
- [第四部分：声明式风险目录 + 语义模型双轨制](#第四部分声明式风险目录--语义模型双轨制)
- [第五部分：七阶段实施路线（融合版）](#第五部分七阶段实施路线融合版)
- [第六部分：关键技术深化](#第六部分关键技术深化)
- [第七部分：刀具磨损→尺寸分析——制造业Agent的深度案例](#第七部分刀具磨损尺寸分析制造业agent的深度案例)
- [第八部分：组织变革对接——从7×12到6×12的量化路径](#第八部分组织变革对接从7×12到6×12的量化路径)
- [第九部分：成本模型与ROI（精确版）](#第九部分成本模型与roi精确版)
- [第十部分：方案自身的风险管理](#第十部分方案自身的风险管理)
- [附录：v1.0→v2.0变更对照表](#附录v10v20变更对照表)

---

# v2.0 升级说明：为什么需要重构

v1.0 方案基于 InfoQ《从 AI 取数到智能分析》一文，构建了以**自然语言取数+语义建模+Skill分析**为主线的五阶段路线图。这是一个优秀的"被动智能"方案——用户问，Agent答。

但在读到"主动智能层"文件夹下的3篇文章后，发现了一个关键缺失：**v1.0只有"问"模式，没有"守"模式。**

| 维度 | v1.0（InfoQ驱动） | 主动智能层3篇 | v2.0目标 |
|------|-------------------|---------------|----------|
| 核心交互 | 用户提问→Agent回答 | Agent持续巡检→主动推送告警 | 双模式统一引擎 |
| 数据接入 | 全量入仓（SQLite/PostgreSQL） | MCP Server封装已有系统 | MCP Server优先，按需入仓 |
| 第一阶段 | 数据基础建设（入仓+治理） | Phase 0空壳跑通（信任先行） | 信任优先，三条低成本风险首发 |
| 风险/规则管理 | 语义模型（YAML指标+维度） | 声明式风险目录（YAML触发条件） | 双轨制：语义模型+风险目录 |
| 上线策略 | 功能完成后直接上线 | 影子模式→人工验证→真推送 | 全部功能经影子模式验证 |
| 容错设计 | 未涉及 | 三层降级+手动SOP | 完整降级方案 |
| 组织变革 | 定性描述 | 定量放行标准+分步过渡 | 数据驱动的组织变革路线 |
| 成本 | 粗略估算 | ¥3,400/月MVP精确模型 | 精确双层成本模型 |

**v2.0的核心命题**：InfoQ的Data Agent解决"怎么聪明地回答"，主动智能层解决"怎么可靠地守护"。两者共享同一套数据接入层、同一个Agent引擎、同一条通知通道。v2.0将它们融合为一个**制造业智能中枢**——问守双模，一体两面。

---

# 第一部分：双源合流——InfoQ + 主动智能层的交叉增强

## 1.1 两套方法论的关键交叉点

### 交叉点1：Multi-Agent ← → 统一Agent引擎

**InfoQ**：Supervisor Agent + Data Scope Agent + Data Discovery Agent + SQL Generator Agent — 四层Agent协作处理自然语言查询。

**主动智能层**：一个统一Agent引擎，Predictive模式（持续巡检→告警）+ Reactive模式（事件触发→根因定位），80%代码复用。

**v2.0融合**：统一Agent引擎内建两种"人格"——
- **Query Personality（问）**：加载语义模型，接收NL问题，走Text-to-SQL/DSL路径
- **Watch Personality（守）**：加载风险目录，定时巡检数据源，走规则/ML推理路径

两者共享：数据接入MCP Server → 上下文管理器 → 通知路由网关 → 反馈闭环。

### 交叉点2：语义模型 ← → 声明式风险目录

**InfoQ**：语义模型（YAML）封装指标/维度/过滤条件，作为LLM与物理表之间的翻译层。四步循环（AI辅助建模→语义驱动查询→反馈回流→专家优化）。

**主动智能层**：风险目录（YAML）封装风险ID/触发条件/数据源/推送目标，声明式配置不硬编码。

**v2.0融合**：语义模型和风险目录共享同一套底层元数据（表Schema、字段描述、业务规则），但服务于不同模式：
- 语义模型 → Query模式：当用户问"昨天OEE是多少"
- 风险目录 → Watch模式：当系统检测到"OEE连续3天下降>10%"

### 交叉点3：Skill机制 ← → 刀具磨损分析链

**InfoQ**：Skill = 多步骤的标准化分析流程（指标下钻→维度拆解→贡献度分析→根因定位→报告生成）。

**主动智能层**：刀具磨损→尺寸分析四步依存链（寿命分析→磨损尺寸关联→换刀后自动刀补→最佳刀补时机）。

**v2.0融合**：刀具磨损分析链是最适合做成Skill的案例——它是一个标准的多步骤分析流程，每一步有明确的输入/输出/算法，可复用，可验证。v2.0将刀具分析链作为**首个制造业深度Skill**纳入方案。

### 交叉点4：渐进式元数据披露 ← → 数据就绪度审计

**InfoQ**：三层元数据加载（L1业务域→L2表发现→L3深度Schema），防止上下文腐化。

**主动智能层**：每条风险上线前强制数据就绪度审计（数据源接口类型/当前状态/完整度/时效/负责人）。

**v2.0融合**：数据就绪度审计作为L0前置层——在Agent加载任何元数据之前，先检查数据源是否可访问。审计不通过的数据源标记为"不可用"，Agent在L1阶段就不会将其纳入候选范围。

### 交叉点5：Human-in-loop ← → 影子模式 + 反馈闭环

**InfoQ**：两层确认机制（数据域确认+候选表确认），用户确认后Agent才继续。

**主动智能层**：影子模式（跑在后台记录"如果上线会推什么"，人工验证24小时再开推送）+ 反馈按钮（👍/👎/🔄/❓自动调整阈值）。

**v2.0融合**：所有Agent输出（无论是查询结果还是告警推送）都经过两阶段验证：
- 开发阶段：影子模式（离线回放历史数据，验证准确率）
- 上线后：反馈闭环（用户点赞/点踩/纠正 → 自动调整 → 回流标注数据）

## 1.2 融合后的完整能力矩阵

```
                    ┌──────────────────────────────────────────┐
                    │         制造业智能中枢 (v2.0)              │
                    │                                          │
                    │   ┌──────────────┐  ┌──────────────┐    │
                    │   │  Query Mode  │  │  Watch Mode  │    │
                    │   │   (问模式)    │  │   (守模式)    │    │
                    │   │              │  │              │    │
                    │   │ • NL取数     │  │ • 持续巡检   │    │
                    │   │ • 语义模型   │  │ • 风险目录   │    │
                    │   │ • Skill分析  │  │ • 主动告警   │    │
                    │   │ • 可视化     │  │ • 自动定位   │    │
                    │   └──────┬───────┘  └──────┬───────┘    │
                    │          │                  │            │
                    │          └────────┬─────────┘            │
                    │                   │                      │
                    │     ┌─────────────┴─────────────┐        │
                    │     │     统一 Agent 引擎        │        │
                    │     │  规则推理 + ML + LLM解释   │        │
                    │     └─────────────┬─────────────┘        │
                    │                   │                      │
                    │     ┌─────────────┴─────────────┐        │
                    │     │     MCP Server 数据接入层   │        │
                    │     │ 刀具 | 三坐标 | 对刀仪 |    │        │
                    │     │ MES |  HR  |  SPC | 报工   │        │
                    │     └─────────────┬─────────────┘        │
                    │                   │                      │
                    │     ┌─────────────┴─────────────┐        │
                    │     │       已有系统 (不改)       │        │
                    │     └───────────────────────────┘        │
                    └──────────────────────────────────────────┘
```

---

# 第二部分：统一架构——问守双模Agent引擎

## 2.1 架构核心判断

**为什么不做两套系统？**

InfoQ的Data Agent和主动智能层的Risk Agent本质上共享：
- 同一个数据接入层（查同一批MCP Server）
- 同一种上下文管理机制（渐进式加载/卸载）
- 同一种推理模式（规则+ML+LLM分层推理）
- 同一条通知通道（企微推送）
- 同一个反馈闭环（用户反馈→标注→回流）

**80%代码复用，只在触发方式和推理目标上不同。**

## 2.2 双模式详细设计

### Query Mode（问模式）——用户主动

```
触发：用户在飞书/Hermes/Web输入自然语言问题
流程：
  意图识别 → 路由判断(Text-to-SQL / Text-to-DSL)
  → 语义模型加载 → SQL/DSL生成 → 执行
  → 结果展示(表格/图表) → 反馈收集
```

**核心组件**：
- Supervisor Agent（意图识别+路由）
- Data Scope Agent（数据域定位）
- Data Discovery Agent（表/字段发现 + Human-in-loop确认）
- SQL/DSL Generator Agent（多路并行生成+选优+验证修复）
- 语义模型引擎（DSL→SQL确定性翻译）
- Skill Runner（多步骤分析流程执行）

### Watch Mode（守模式）——系统主动

```
触发：定时巡检(cron) / 事件驱动(换刀事件/换班事件)
流程：
  加载风险目录 → 获取数据源(通过MCP Server)
  → 规则/ML推理 → 判断是否触发
  → 告警状态机(创建→发送→确认→关闭)
  → 升级管理(超时未响应→推上级)
  → 反馈闭环(用户按钮→调整阈值)
```

**核心组件**：
- 风险目录加载器（解析YAML，验证schema，热加载）
- 规则推理引擎（条件表达式评估，单元测试）
- ML推理引擎（刀具寿命预测/XGBoost，客诉模式复发/LLM）
- 告警状态机（CREATED→SENT→ACKNOWLEDGED→CLOSED + 升级超时）
- 风暴保护（熔断器：1分钟>100条→熔断；同类型>30条→熔断该类型）
- 告警聚合与抑制（根因聚合、接收人聚合、时间窗聚合）
- 通知路由网关（干跑模式、企微/短信/电话多通道）
- 沙箱回放引擎（指定时间窗回放历史数据，不真实通知）

### 双模式路由

```
用户/系统事件
      │
      ▼
┌─────────────┐
│  意图识别    │
│  (Supervisor)│
└──────┬──────┘
       │
   ┌───┴───┐
   │       │
   ▼       ▼
用户提问   系统事件/定时
   │       │
   ▼       ▼
Query Mode  Watch Mode
   │       │
   ▼       ▼
语义模型    风险目录
   │       │
   ▼       ▼
SQL/DSL    规则/ML推理
   │       │
   └───┬───┘
       ▼
  通知/展示
       │
       ▼
  反馈闭环
```

## 2.3 共享组件设计

### 上下文管理器（共享）

```
┌─────────────────────────────────────────┐
│           上下文管理器                    │
│                                         │
│  L-1 (前置): 数据就绪度审计结果          │
│  标记哪些数据源可用/不可用                │
│                                         │
│  L0 (对话开始): 用户画像 + 最近记忆       │
│  ~500 tokens                            │
│                                         │
│  L1 (意图后): 业务域/风险域清单           │
│  ~800 tokens                            │
│                                         │
│  L2 (确认后): 表Schema / 风险定义详情     │
│  ~2,000 tokens                          │
│                                         │
│  L3 (执行中): 中间结果引用(DataFrame路径) │
│  ~200 tokens (仅路径引用,不含数据)        │
│                                         │
│  卸载策略: 每进入下一层,卸载上一层非必需   │
└─────────────────────────────────────────┘
```

### 文件系统上下文（共享）

```
~/.hermes/manufacturing-intelligence/
├── mcp_servers/               # MCP Server配置
│   ├── tool_mgmt.yaml
│   ├── cmm.yaml
│   ├── presetter.yaml
│   ├── mes.yaml
│   ├── hr.yaml
│   └── spc.yaml
├── catalog/                   # 元数据目录
│   ├── domains/               # 业务域定义
│   ├── tables/                # 表Schema
│   └── glossary.yaml          # 业务术语表
├── semantic_models/           # 语义模型 (Query模式)
│   ├── oee.yaml
│   ├── quality_rate.yaml
│   └── tool_cost.yaml
├── risk_catalog/              # 风险目录 (Watch模式)
│   ├── tool_life.yaml
│   ├── spc_trend.yaml
│   ├── competency.yaml
│   └── ...
├── skills/                    # 分析Skill (两种模式共用)
│   ├── oee-attribution.md
│   ├── quality-root-cause.md
│   ├── tool-wear-analysis.md  # ★ 新增：刀具磨损分析链
│   └── shift-handover-check.md
├── knowledge/                 # 业务知识库
│   ├── rules/                 # 业务规则
│   ├── samples/               # SQL样例
│   └── faq/
├── sandbox/                   # 沙箱工作区
│   └── session_{id}/
├── evaluation/                # 评测体系
│   ├── test_sets/             # Query评测集
│   ├── shadow_runs/           # Watch影子模式记录
│   └── results/
└── profiles/                  # 用户画像
    ├── simon.yaml
    ├── shift_leader_01.yaml
    └── ...
```

### 通知路由网关（共享）

```yaml
notification_gateway:
  channels:
    - type: "wecom"
      priority: "high"
      targets:
        - role: "shift_leader"
          action: "push_card"  # 可交互卡片
        - role: "operator"
          action: "push_text"
    - type: "feishu"
      priority: "medium"
      targets:
        - role: "manager"
          action: "push_card"
  
  modes:
    dry_run: true   # 干跑模式：推理但不推送
    shadow: true    # 影子模式：推送但标记为[测试]
    live: false     # 生产模式：真实推送
  
  escalation:
    timeout: 300    # 5分钟未确认 → 升级
    chain: ["直属上级", "部门主管", "厂长"]
  
  quiet_hours:
    enabled: true
    start: "22:00"
    end: "06:00"
    action: "queue"  # 排队，到时间再推送（紧急除外）
```

---

# 第三部分：数据接入层——MCP Server替代全量入仓

## 3.1 架构决策：为什么不全部入仓

v1.0 方案推荐将所有数据导入SQLite/PostgreSQL统一管理。这是一个"理想状态"方案，但在制造业场景下存在三个现实问题：

1. **系统异构严重**：刀具管理系统可能是SQL Server，三坐标可能是文件/PDF，对刀仪可能是SQLite本地库，MES可能是Oracle。全量入仓意味着要为每个系统开发ETL管道，维护成本和维护风险都很高。

2. **实时性要求**：Watch模式需要近乎实时的数据（刀具剩余寿命、设备报警信号）。如果走"先入仓再查询"，延迟至少是ETL周期（可能数分钟到数小时）。

3. **数据主权**：不改动原有系统是铁律。直接在原系统上只读查询，风险远低于数据迁移。

**v2.0方案**：**MCP Server优先，按需入仓**。

## 3.2 MCP Server清单

每个MCP Server是一个独立的小服务，把已有系统的数据库/接口包装成标准化JSON API。只读查询，不改原有系统。

### Server 1: 刀具管理 MCP

```yaml
server: tool-management-mcp
source: 刀具管理系统 (SQL Server / 自建库)
endpoints:
  - GET /tool/{tool_id}/status
    returns: {tool_id, machine, installed_at, total_parts_cut, 
              rated_life, remaining_life_pct, preset_value, 
              current_wear_um, last_measured_at}
  - GET /tool/{tool_id}/history
    returns: [{date, parts_cut, wear_um, event_type}, ...]
  - GET /machine/{machine_id}/tools
    returns: [{tool_id, position, status}, ...]
workload: IT 1人 + AI 1人 | 3天
precondition: 刀具管理系统开放查询权限
```

### Server 2: 三坐标/CMM MCP

```yaml
server: cmm-mcp
source: 三坐标报告数据库 (SPC系统子表 或 文件)
endpoints:
  - GET /measurement/{part_no}/{feature}
    params: {time_range, limit}
    returns: {part_no, feature, nominal, upper_tol, lower_tol,
              measurements: [{time, value, tool_id}, ...]}
  - GET /measurement/trend/{part_no}/{feature}
    returns: [{time, value, moving_avg, cp, cpk}, ...]
workload: IT 1人 + AI 1人 | 3天
precondition: CMM报告数据库只读权限
note: 如果三坐标只有PDF报告，需OCR解析——建议推动厂商开放API
```

### Server 3: 对刀仪 MCP

```yaml
server: presetter-mcp
source: 对刀仪本地数据库 (SQLite / CSV通过RS232)
endpoints:
  - GET /presetter/tool/{tool_id}
    returns: {tool_id, history: [{date, preset, wear}, ...]}
  - GET /presetter/latest/{machine_id}
    returns: [{tool_id, preset, wear, measured_at}, ...]
workload: IT 1人 | 3天
precondition: 对刀仪数据接口文档
note: 如为RS232串口CSV输出，需中间程序解析后入中间库
```

### Server 4: MES工序流转 MCP

```yaml
server: mes-mcp
source: MES系统 (Oracle/MySQL/SQL Server)
endpoints:
  - GET /machine/{machine_id}/current
    returns: {machine, order_no, part_no, current_process,
              parts_produced, last_tool_change, 
              tool_changed_from, tool_changed_to}
  - GET /order/{order_no}/progress
    returns: {order_no, status, processes: [{name, status, qty}, ...]}
  - GET /shift/handover
    returns: [{from_shift, to_shift, pending_items, timestamp}, ...]
workload: IT 1人 | 2天
precondition: MES API已可用 或 数据库只读权限
```

### Server 5: HR技能矩阵 MCP

```yaml
server: hr-mcp
source: HR系统 或 Excel
endpoints:
  - GET /employee/{employee_id}/competency
    returns: {employee, process, competency_level, hours_worked, 
              last_assessment}
  - GET /shift/{shift_id}/roster
    returns: [{employee, machine, process, competency}, ...]
workload: IT 1人 | 1天
precondition: HR系统开放 或 Excel已结构化导入
```

### Server 6: SPC MCP

```yaml
server: spc-mcp
source: SPC系统数据库
endpoints:
  - GET /spc/{part_no}/{process}/{feature}
    params: {time_range}
    returns: {measurements: [{time, value, usl, lsl}, ...],
              stats: {cp, cpk, pp, ppk, x_bar, sigma}}
  - GET /spc/violations
    returns: [{part_no, process, feature, rule, time, values}, ...]
workload: IT 1人 + 质量 1人 | 2天
precondition: SPC数据库权限
```

### Server 7: 报工统计 MCP（自建）

```yaml
server: production-stats-mcp
source: 已有的SQLite入仓数据（由现有管道维护）
endpoints:
  - GET /production/daily
    params: {date, shift, machine_id}
    returns: {planned_qty, actual_qty, completion_rate,
              process_scrap, material_scrap, downtime_min, total_hours}
  - GET /production/trend
    params: {start_date, end_date, metric}
    returns: [{date, value}, ...]
workload: 已就绪（利用现有管道）
```

## 3.3 数据流架构

```
┌──────────────────────────────────────────────────────┐
│                    已有系统 (不改)                     │
│  刀具SQL Server  三坐标DB  对刀仪  MES  HR  SPC  报工  │
└──────┬────────┬──────┬──────┬─────┬────┬──────┬──────┘
       │        │      │      │     │    │      │
       ▼        ▼      ▼      ▼     ▼    ▼      ▼
┌──────────────────────────────────────────────────────┐
│              MCP Server 层 (新做, 只读)               │
│  刀具MCP  CMM MCP  对刀仪  MES  HR  SPC  报工        │
│                    MCP      MCP  MCP  MCP   MCP      │
└──────────────────────┬───────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────┐
│               Agent 引擎 (新做)                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │ Query Mode  │  │ Watch Mode  │  │ Skill引擎   │  │
│  │ (问模式)    │  │ (守模式)    │  │             │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│  ┌─────────────────────────────────────────────────┐ │
│  │  共享: 上下文管理 | 文件系统 | 沙箱 | 通知网关    │ │
│  └─────────────────────────────────────────────────┘ │
└──────────────────────┬───────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────┐
│                    输出层                              │
│  企微告警卡片 | 飞书日报 | Web看板 | Hermes TUI       │
└──────────────────────────────────────────────────────┘
```

---

# 第四部分：声明式风险目录 + 语义模型双轨制

## 4.1 为什么需要两条轨道

**语义模型（Query Mode）**：回答"是多少"的问题。
- 封装指标计算逻辑（OEE = 稼动率 × 性能效率 × 良品率）
- 封装维度层次（设备→产线→车间→工厂）
- 封装过滤条件模板（时间范围、设备筛选）

**风险目录（Watch Mode）**：回答"会不会出事"的问题。
- 封装触发条件（刀具剩余寿命 < P10）
- 封装数据源路径（从哪个MCP Server取什么数据）
- 封装推送策略（推给谁、什么时候推、不响应怎么升级）

**两者的交叉**：风险目录的触发条件可能引用语义模型的指标。比如：
```yaml
risk:
  name: "OEE连续下降"
  trigger:
    metric: "semantic_model.oee.oee"  # ← 引用语义模型
    condition: "连续3天下降 AND 累计降幅 > 10%"
```

## 4.2 风险目录设计（来自主动智能层）

### 原则

1. **声明式配置，不是硬编码**：每条风险是一个YAML文件，放在`risk_catalog/`目录下
2. **LLM只解释，不打分**：规则的推理和评分用确定性逻辑（规则引擎/ML模型），LLM只负责生成人类可读的解释文本
3. **每条风险独立可测**：可以用`--risk-id=TOOL_LIFE_CRITICAL --dry-run`单独测试一条风险

### 首批10条风险清单

| ID | 名称 | 类别 | 触发类型 | 数据源 | 就绪度 |
|----|------|------|----------|--------|--------|
| R01 | 刀具寿命临界 | 设备 | 实时 | 刀具MCP | 待审计 |
| R02 | 同型刀具寿命异常 | 设备 | 周期(日) | 刀具MCP | 待审计 |
| R03 | 设备报警未处理 | 设备 | 实时 | MES MCP | 待审计 |
| R04 | 首件未检 | 质量 | 事件驱动 | MES MCP | ⚠️ 部分就绪 |
| R05 | SPC趋势违规 | 质量 | 实时 | SPC MCP | 待审计 |
| R06 | 客诉模式复发 | 质量 | 周期(周) | 客诉记录+LLM | 待审计 |
| R07 | 员工独立作业能力不达标 | 人员 | 事件驱动 | HR MCP | ✅ 接近就绪 |
| R08 | 新员工前24h | 人员 | 事件驱动 | HR MCP | 待审计 |
| R09 | 新批次未验证 | 来料 | 事件驱动 | MES MCP | 待审计 |
| R10 | 班次交接遗留未闭环 | 流程 | 周期(30min) | MES MCP | ✅ 接近就绪 |

### 风险定义模板

```yaml
risk_id: TOOL_LIFE_CRITICAL
name: 刀具寿命临界
category: 设备
severity: 高
version: 1.0.0
status: shadow  # shadow | live | paused

data_sources:
  - server: tool-management-mcp
    endpoint: GET /tool/{tool_id}/status
    refresh: 60s  # 每60秒刷新一次
  - server: tool-management-mcp
    endpoint: GET /tool/{tool_id}/history
    params:
      days: 30
    refresh: 3600s

trigger:
  type: threshold
  logic: |
    tool.remaining_life_pct < tool_type.p10_threshold
    AND tool.is_active == true
    AND machine.status == "running"
  params:
    default_p10_threshold: 15  # 默认P10阈值%，会被动态计算覆盖

notification:
  targets:
    - role: operator
      channel: wecom
      template: "tool_life_critical_operator"
    - role: shift_leader
      channel: wecom
      template: "tool_life_critical_leader"
  escalation:
    timeout: 300  # 5分钟
    next_level:
      - role: production_manager
        channel: wecom

suppression:
  cooldown: 600  # 同一刀具10分钟内不重复告警
  aggregation:
    by: [machine_id]  # 同一设备的多把刀聚合为一条

feedback:
  buttons: [acknowledge, snooze_30m, false_alarm, escalate]
  auto_adjust:
    - if: "feedback.false_alarm > 3 in 7d"
      action: "increase_threshold_by_5pct"

human_readable:
  summary: "{{machine_id}}上的{{tool_id}}刀具剩余寿命仅{{remaining_life_pct}}%，低于该型号P10阈值{{p10_threshold}}%"
  recommendation: "建议在{{estimated_parts_remaining}}件内安排换刀。当前已加工{{total_parts_cut}}件，额定寿命{{rated_life}}件。"
```

## 4.3 语义模型设计（来自InfoQ，增强版）

v1.0的语义模型设计保留，新增与风险目录的交叉引用：

```yaml
semantic_model:
  name: "oee"
  display_name: "设备综合效率(OEE)"
  
  # ★ 新增：风险规则引用
  watch_rules:
    - risk_id: "OEE_CONSECUTIVE_DECLINE"  # 关联的风险规则
      trigger: "oee < baseline * 0.8 AND trend == 'down'"
    
  dimensions: 
    # ... (同v1.0)
    
  measures:
    - name: "oee"
      # ★ 新增：该指标也可被风险目录作为触发条件引用
      aliases: ["risk_catalog.OEE_CONSECUTIVE_DECLINE.metric"]
```

---

# 第五部分：七阶段实施路线（融合版）

v1.0是五阶段（数据基础→取数Agent→语义建模→Skill→自主运营）。
v2.0融合主动智能层的六阶段，加上v1.0的数据分析深化阶段，形成七阶段：

```
Phase 0    Phase 1A    Phase 1B    Phase 2    Phase 3    Phase 4    Phase 5
空壳跑通 → 信任建立 → 双模MVP  → 全量上线 → 深度分析 → 模型升级 → 自主运营
(2周)     (2周)      (6周)      (8周)      (6周)      (持续)     (持续)
```

**关键变化**：
- Phase 0（新增）：先跑通一条假告警的全链路，验证基础设施
- Phase 1A（新增）：三条"极低成本"风险先行，建立信任
- Phase 1B（融合）：问模式+守模式同时上线MVP，试点1条产线
- Phase 2：全量扩展至40+产线 + 反馈闭环
- Phase 3（新增）：Skill深度分析（含刀具磨损分析链）
- Phase 4：ML替换纯规则 + 自动定位
- Phase 5：自主运营 + 组织变革（7×12→6×12）

## Phase 0：空壳跑通（第1-2周）

> **"制造业的信任，一次就够了。"**

**目标**：一条假告警从产生到推送，全链路不丢不漏。

**做什么**：

1. 部署一个最小Python服务：
   - 一个"Hello World"假风险（hardcode，不查任何数据源）
   - 告警状态机骨架（CREATED → SENT → ACKNOWLEDGED → CLOSED）
   - 企微推送通道（发到项目组自己的群，不推生产线）

2. 验证时序：
   - 告警产生→推送：<10秒
   - 确认→状态变更→日志落库：<3秒
   - 超时5分钟未响应→升级推送：<10秒偏差

3. 部署基础设施：
   - Redis延迟升级队列
   - MySQL告警库（alert + alert_state_transition表）
   - 最简Web管理台（一页，看今天的告警列表）

4. 搭建开发环境：
   - Hermes Agent配置文件
   - MCP Server开发框架（第一个空壳Server）
   - 沙箱回放引擎骨架

**交付物**：
- 企微群收到一条"测试告警"并可点击确认
- 状态流转日志完整入库
- 升级倒计时验证通过（时间扭曲测试）

**为什么Phase 0必须存在**：如果没有这一步，Phase 1A第一次推送真告警时，通道断了/状态丢了/升级没触发——用户的第一印象就毁了。后续再好的功能也难以挽回信任。

## Phase 1A：信任建立——三条低成本风险（第3-4周）

> **"让第一个用上系统的班组长说'这东西有用'。"**

**MVP风险重选（与主动智能层一致）**：

| 风险 | 数据源 | 为什么第一个做 |
|------|--------|---------------|
| R10: 班次交接遗留未闭环 | MES交接班模块（已有） | 纯SQL，不依赖新数据采集，误报率极低，直接解决7×12→6×12的交接风险 |
| R07: 员工独立作业能力不达标 | 排班表+技能矩阵（HR已有） | 不需要传感器，不需要实时信号，Excel就能验出效果 |
| R04: 首件未检 | MES工序流转+质量检验模块 | IATF红线，风险价值明确 |

**同时**：
- 启动数据就绪度审计（10条风险逐条过）
- 搭建2-3个核心MCP Server（MES、HR）
- 开发影子模式引擎

**交付物**：
- 3条风险在试点产线运行
- 每条风险过去2周的数据回放验证通过
- 班组长每日收到≤3条告警（不是30条）
- 反馈按钮被点过至少20次
- Query模式基础框架搭建完成（SQLite+报工数据已可用）

## Phase 1B：双模MVP——问守合体（第5-10周）

> **"问模式和守模式在试点产线上同时跑起来。"**

### 守模式（Watch Mode）

补上7条风险，试点产线跑满10条：

| 风险 | 前置条件 | 影子模式要求 |
|------|----------|-------------|
| R01: 刀具寿命临界 | 刀具MCP Server就绪 | 3天影子 → 人工验证 → 推送 |
| R02: 同型刀具寿命异常 | ≥30天刀具更换历史 | 需历史数据回放验证 |
| R03: 设备报警未处理 | MES报警信号实时接入 | 2天影子 |
| R05: SPC趋势违规 | SPC MCP Server就绪 | 3天影子 |
| R06: 客诉模式复发 | ≥50条结构化客诉历史 | LLM推理通道验证 |
| R08: 新员工前24h | 排班+技能矩阵 | 1天影子 |
| R09: 新批次未验证 | 来料检验+批次上线记录 | 2天影子 |

**注意事项（严格遵守）**：
- 每条风险上线前必须跑影子模式
- 数据就绪度审计不通过的，跳过，不硬上
- 第一版接受误报率<25%

### 问模式（Query Mode）

搭建完整Multi-Agent取数链路：
- Supervisor Agent（意图识别+路由）
- Data Scope Agent + Data Discovery Agent
- SQL Generator Agent（多路并行+验证修复）
- 报工统计语义模型上线
- OEE语义模型上线

**交付物**：
- 试点产线10条风险全部运行，误报率<25%
- Query模式可回答≥20类常见问题，L1准确率≥80%
- 闭环率>60%

## Phase 2：全量上线+反馈闭环（第11-18周）

**目标**：从1条产线扩展到全厂40+产线，误报率压到12%。

**做什么**：

1. **逐条产线接入**：每条新产线先跑3天影子模式，不批量铺开
2. **周三复盘会**：AI团队+班组长+质量工程师，15分钟，看本周误报/漏报Top3，现场调阈值
3. **反馈闭环上线**：用户👍/👎/🔄/❓ → 自动调整阈值权重
4. **Query模式完善**：
   - 个性化能力（用户画像+持久化记忆）
   - 混合路由（Text-to-SQL / Text-to-DSL）
   - 评测集构建（基于线上真实SQL，目标≥200条）
5. **培训**（Phase 1A就开始，不是等到这里）：
   - 班组长：反馈按钮、日报、指派（1h×3轮）
   - 操作工：告警来了做什么、什么不是告警（30min）
   - 业务专家：调阈值、提新风险需求（2h）

**定量放行标准**：

| 指标 | Phase 2完成标准 | 数据来源 |
|------|----------------|----------|
| 守模式误报率 | <12% | 告警反馈数据 |
| 守模式闭环率 | >80% | 告警状态机 |
| 问模式L1准确率 | ≥90% | 评测Pipeline |
| 问模式L2准确率 | ≥80% | 评测Pipeline |
| 系统可用率 | >99.5% | 运维监控 |
| 培训覆盖率 | 100%（核心人员） | 培训记录 |

## Phase 3：深度分析Skill（第19-24周）

**目标**：从取数工具进化为分析平台，Skill机制规模化。

### 核心Skill开发

| 优先级 | Skill名称 | 核心能力 | 来源 |
|--------|-----------|----------|------|
| P0 | OEE归因分析 | 指标下钻→维度拆解→贡献度→根因→报告 | InfoQ方法论 |
| P0 | 刀具磨损分析链 | 寿命分析→磨损尺寸关联→刀补建议→最佳时机 | 主动智能层深度案例 |
| P1 | 质量根因分析 | 四维度拆解→交叉分析→根因推断 | 融合两者 |
| P1 | 刀具成本优化 | 成本基线→寿命分析→供应商对比→建议 | v1.0扩展 |
| P2 | 交期风险预警 | 订单进度→瓶颈识别→延迟预测 | 业务需求 |

### Skill Builder

- 初期：Markdown模板+人工创建
- 中期：对话式创建（"帮我创建一个分析XX的Skill"）
- 支持离线回放验证

## Phase 4：模型升级+自动定位（第25周起，持续）

1. **ML替换纯规则**：
   - 刀具寿命预测：P10阈值 → XGBoost回归（需6个月+数据）
   - 客诉模式匹配：关键词 → LLM语义匹配
   - SPC趋势检测：Western Electric规则 → 异常检测模型

2. **自动定位v1**：
   - 输入：零件号+不良现象
   - Agent从MES/QMS/刀具/SPC数据反推根因+推荐责任人
   - 目标：从"查5个系统30分钟"到"1个查询30秒"

3. **风险目录扩充**：从10条→20+条

## Phase 5：自主运营+组织变革（与Phase 2并行启动）

### 自动化运营

- 调度Agent定时运行监控Skill
- 检测异常后通过飞书/微信推送预警
- 用户可直接回复预警消息触发深度分析
- 月度运营报告自动生成

### 组织变革路线（详见第八部分）

---

# 第六部分：关键技术深化

## 6.1 数据就绪度审计（来自主动智能层）

**这是v1.0完全缺失的一块，也是最容易让项目翻车的。**

```yaml
# 审计模板
审计编号: AUDIT-2026-001
风险ID: TOOL_LIFE_CRITICAL
审计日期: 2026-07-10
审计人: IT负责人

依赖数据源:
  - 源: 刀具管理系统
    接口类型: DB直连 (SQL Server)
    当前状态: 未接入
    数据完整度: 未知
    数据时效: 实时
    负责人: 设备主管 张工
    就绪动作: "开放刀具剩余寿命查询只读权限，IT联调2天"
    
  - 源: 对刀仪
    接口类型: 文件导入 (RS232 → CSV)
    当前状态: 未接入
    数据完整度: 未知
    数据时效: 按次
    负责人: IT 李工
    就绪动作: "写中间程序解析CSV入库，预计3天"

结论: 待整改后重新审计
预计就绪日期: 2026-07-17
```

**10条风险逐条审计。结论为"暂无数据源"的，不要硬上，改用影子模式积累数据。**

## 6.2 影子模式（来自主动智能层）

**每条新功能/新风险/新Skill在上线前必须经过影子模式验证。**

```
影子模式工作流:
1. 部署新功能，但notification_gateway.mode = "shadow"
2. 系统正常推理，但推送消息标记为[测试]，只发到项目组群
3. 运行24小时（风险）或回放2周历史数据（查询/Skill）
4. 人工验证：误报/漏报/准确率是否达标
5. 达标 → mode改为"live"，正式推送
   不达标 → 调整参数/规则，重新影子模式
```

**沙箱回放引擎**：

```python
class SandboxReplayEngine:
    """离线回放历史数据，验证新功能效果"""
    
    def replay(self, risk_id: str, time_window: tuple):
        """
        指定时间窗回放历史数据
        输出："如果当时上线了，会推送什么"
        不产生真实通知
        """
        start, end = time_window
        events = []
        
        for timestamp in self._generate_timestamps(start, end):
            # 加载当时的数据快照
            snapshot = self._load_snapshot(risk_id, timestamp)
            # 运行推理
            result = self._run_inference(risk_id, snapshot)
            # 记录（不推送）
            events.append({
                'timestamp': timestamp,
                'would_trigger': result.triggered,
                'would_push_to': result.targets,
                'reason': result.reason
            })
        
        # 生成对比报告
        actual_incidents = self._load_actual_incidents(start, end)
        return self._compare(events, actual_incidents)
```

## 6.3 告警状态机 + 风暴保护（来自主动智能层）

### 告警状态机

```
CREATED → SENT → ACKNOWLEDGED → CLOSED
                 ↘ 超时5min → ESCALATED → ACKNOWLEDGED → CLOSED
                 ↘ 用户snooze → SNOOZED → (到期) → SENT
                 ↘ 用户标记误报 → FALSE_ALARM → CLOSED
```

### 风暴保护（熔断器）

```python
class StormProtection:
    def __init__(self):
        self.window_1min = []
        self.by_type = {}
        
    def check(self, alert):
        """返回 True = 允许发送, False = 熔断"""
        now = time.time()
        
        # 规则1: 1分钟内 > 100条 → 全局熔断
        self.window_1min = [t for t in self.window_1min if now - t < 60]
        self.window_1min.append(now)
        if len(self.window_1min) > 100:
            self._circuit_break("global", "1分钟内告警>100条")
            return False
        
        # 规则2: 同类型 > 30条 → 该类型熔断
        type_count = self.by_type.get(alert.type, [])
        type_count = [t for t in type_count if now - t < 60]
        type_count.append(now)
        self.by_type[alert.type] = type_count
        if len(type_count) > 30:
            self._circuit_break(alert.type, f"{alert.type}类型告警>30条/分钟")
            return False
        
        return True
```

### 告警聚合与抑制

| 策略 | 规则 | 示例 |
|------|------|------|
| 根因聚合 | 同一设备的多把刀同时告警→聚合为一条 | "CNC-03上3把刀具寿命临界" |
| 接收人聚合 | 同一接收人5分钟内多条→合并 | 不逐条推送，推一条摘要 |
| 时间窗抑制 | 同一刀具10分钟内不重复 | 冷却期=600秒 |

## 6.4 三层降级方案（来自主动智能层）

**系统挂了怎么办？——生产制造必须回答的问题。**

| 级别 | 触发条件 | 降级动作 | 恢复动作 |
|------|----------|----------|----------|
| **一级降级** | Python Agent引擎不可用 | 告警暂停推送，企微群发"系统维护中"，班组长恢复手动巡检 | 引擎恢复→一次性回放积压告警 |
| **二级降级** | 某数据源（刀具/MES）不可用 | 仅暂停依赖该数据源的风险，其他风险继续运行 | 数据源恢复→自动恢复关联风险 |
| **三级降级** | 企微推送通道不可用 | 告警写库不推送，Web管理台保留完整记录 | 通道恢复→一次性回放 |

**手动SOP（A4纸，每个班组长一份）**：

```
┌─────────────────────────────────────────┐
│   AI助手维护中 — 手动巡检清单            │
│   生效时间：接到"系统维护中"通知起        │
│                                         │
│  每2小时检查：                           │
│  □ 刀具管理系统：剩余寿命<20% → 标记换刀  │
│  □ MES：设备报警列表 → 逐条确认          │
│  □ 交接班：待办项是否已闭环              │
│  □ 首件：换班/换刀后首件已检             │
│                                         │
│  异常处理：                              │
│  → 常规问题：按现有流程处理               │
│  → 紧急问题：电话通知上级（不依赖企微）    │
│                                         │
│  系统恢复后：                            │
│  → 登录Web管理台查看积压告警              │
│  → 逐条确认/关闭                         │
└─────────────────────────────────────────┘
```

---

# 第七部分：刀具磨损→尺寸分析——制造业Agent的深度案例

> 这是"主动智能层"第三篇文章的深度案例，也是v2.0中最重要的制造业专用Skill。

## 7.1 场景设定

CNC-03机床上，T-2031镗刀加工BR-2031-A零件孔径（名义Φ35.000，公差+0.015/-0.000）。刀每加工一件磨损一点→孔径逐渐变大→接近公差上限需要调刀补或换刀。

**已有数据**：刀具更换记录（时间/型号/加工件数）、三坐标报告（孔径实测值）、对刀仪数据（预设值/实际磨损量）

## 7.2 分析链四步依存

```
分析1: 刀具寿命分布 (P10/P50/异常检测)
         │
         ▼
分析2: 磨损→尺寸关联 (三阶段分段线性回归)
         │
         ├──→ 分析3: 换刀后自动刀补建议
         │
         └──→ 分析4: 最佳刀补时机优化
```

**不能跳步**。没有寿命数据，磨损-尺寸关系是零散的。没有磨损-尺寸关系，自动刀补就是猜。

## 7.3 分析2：刀具寿命（基础）

```python
def analyze_tool_life(tool_type: str, days: int = 90):
    """
    从刀具更换记录中统计寿命分布
    """
    cycles = tool_mcp.get_life_cycles(tool_type, days)
    
    lifespans = [c.parts_cut for c in cycles]
    
    return {
        'P10': np.percentile(lifespans, 10),   # 只有10%的刀活不到这个数
        'P50': np.percentile(lifespans, 50),    # 中位寿命
        'P90': np.percentile(lifespans, 90),    # 90%的刀能活过这个数
        'mean': np.mean(lifespans),
        'std': np.std(lifespans),
        'anomalies': [c for c in cycles if c.parts_cut < np.percentile(lifespans, 5)],
        # ↑ 异常短的周期——可能是来料问题/参数问题
    }

# 动态阈值（优于固定阈值）
# T-2031 加工铝合金: P10=850 → 预警阈值=850×1.05=893件
# T-1542 加工铸铁:   P10=420 → 预警阈值=420×1.05=441件
```

## 7.4 分析3：磨损→尺寸关联（核心）

**关键发现**：关系不是线性的，分三个阶段。

```
阶段1 (前20%寿命): 初期快磨 — 涂层磨合期，磨损快但尺寸影响小
阶段2 (中间60%寿命): 稳态磨损 — 线性关系，每100件孔径稳定变大~0.5μm
阶段3 (后20%寿命): 末期加速 — 磨损加速，尺寸漂移也加速
```

```python
def fit_wear_to_dimension(tool_id: str, cycle_id: str):
    """
    分段线性回归：磨损→尺寸漂移
    """
    # 1. 拉对齐数据
    wear = presetter_mcp.get_wear_curve(tool_id, cycle_id)
    dims = cmm_mcp.get_deviation_curve(tool_id, cycle_id)
    aligned = align_by_part_count(wear, dims)
    
    n = len(aligned)
    p1 = aligned[:int(n*0.2)]        # 前20%
    p2 = aligned[int(n*0.2):int(n*0.8)]  # 中间60%
    p3 = aligned[int(n*0.8):]        # 后20%
    
    # 稳态段最关键
    slope_p2, r2 = linear_regression(p2.x, p2.y)
    
    return {
        'phase2_slope_um_per_100': slope_p2 * 100,  # 每100件孔径变化
        'phase2_r2': r2,
        'acceleration_point': int(n * 0.8),          # 末期加速起点
        'conclusion': generate_conclusion(slope_p2, tool_life_p10),
    }

# 输出示例：
# ┌────────────────────────────────────────────┐
# │ T-2031 | BR-2031-A 孔径 | 最近10个周期       │
# │ 稳态磨损系数: 0.0052 μm/件 (R²=0.89)        │
# │ → 每加工100件，孔径增大0.52μm               │
# │ 末期加速点: ~960件（在P10=850件之后）        │
# │ 结论: 刀具寿命(P10)先到瓶颈，尺寸公差不是瓶颈  │
# └────────────────────────────────────────────┘
```

## 7.5 分析4：换刀后自动刀补建议

```python
def compute_new_offset_after_tool_change(machine_id: str):
    """
    换刀后自动计算新刀补值
    """
    change = tool_mcp.get_last_change(machine_id)
    
    # 对刀仪数据
    preset_new = presetter_mcp.get_preset(change.new_tool_id)
    wear_old = presetter_mcp.get_last_wear(change.old_tool_id)
    
    # 换刀前最后5件的尺寸偏差
    last_parts = cmm_mcp.get_recent(change.part_no, change.feature, 
                                     before=change.time, limit=5)
    avg_dev = mean(p.actual - p.nominal for p in last_parts)
    
    # 计算新刀补
    wear_factor = 0.7  # 工艺工程师给定，30次换刀后可回归精确值
    offset_correction = wear_old * wear_factor - avg_dev
    new_offset = change.old_offset - offset_correction
    
    return {
        'new_offset': round(new_offset, 3),
        'confidence': 0.85,
        'recommendation': f"T-2031已更换，建议刀补从{change.old_offset}调整到{new_offset}",
    }
```

## 7.6 分析5：最佳刀补时机优化

**目标函数**：min(停机调整成本 + 超差风险成本)

```python
def optimal_offset_timing(tool_id, current_parts, current_dev):
    """
    四场景决策矩阵
    """
    wear_coef = get_wear_coefficient(tool_id)     # 从分析3来
    remaining_tool_life = get_p10(tool_id) - current_parts
    remaining_tolerance = TOLERANCE_BAND - current_dev
    
    # 还能撑多少件（从尺寸角度）
    parts_to_overtol = remaining_tolerance / wear_coef
    
    if wear_coef < 0.003 and TOLERANCE_BAND > 20:
        return "策略A: 换刀时一起调刀补，刀具寿命期内不单独调"
    elif wear_coef < 0.003 and TOLERANCE_BAND <= 20:
        return f"策略B: 每{parts_to_overtol * 0.6:.0f}件调一次刀补，不等换刀"
    elif wear_coef >= 0.01 and TOLERANCE_BAND <= 20:
        return "策略C: 磨损过快+公差窄 → 检查来料硬度和切削参数，根本原因可能不在刀"
    elif current_parts > get_acceleration_point(tool_id):
        return "策略D: 已进入末期加速阶段 → 提前50件换刀，不在末期调刀补"
    
    # 经验规则
    if current_dev > TOLERANCE_BAND * 0.65 and remaining_tool_life > 50:
        return "立即调整刀补"
    if current_dev > TOLERANCE_BAND * 0.80:
        return "必须调整（无论代价）"
```

## 7.7 将分析链封装为Skill

```markdown
---
name: tool-wear-analysis
display_name: 刀具磨损全链分析
triggers:
  - keywords: ["刀具磨损", "刀补", "刀具寿命", "换刀"]
  - events: ["TOOL_CHANGE", "CMM_OUT_OF_TREND"]
version: 1.0.0
---

# 刀具磨损全链分析 Skill

## Step 1: 寿命基线
查询目标刀具型号的历史寿命分布 → 输出P10/P50/P90 + 当前刀具位置

## Step 2: 磨损-尺寸关联
拉取对刀仪+三坐标对齐数据 → 分段线性回归 → 输出稳态磨损系数

## Step 3: 干预建议
基于Step 1+2的结果 → 四场景决策矩阵 → 输出换刀/调刀补建议

## Step 4: 报告
生成结构化报告 → 推送给工艺工程师和操作工

验证: 每一步中间结果可查看, 可回放历史数据验证
```

---

# 第八部分：组织变革对接——从7×12到6×12的量化路径

> 这是"主动智能层"的核心组织目标，v1.0未涉及。

## 8.1 放行标准（与厂长、HR经理共同确认）

| 指标 | 目标值 | 数据来源 | 当前状态 |
|------|--------|----------|----------|
| 10条风险综合误报率 | <10% | 告警反馈数据 | 待建设 |
| 10条风险综合闭环率 | >85% | 告警状态机 | 待建设 |
| 系统可用率（uptime） | >99.5% | 运维监控 | 待建设 |
| 用户满意度（班组长NPS） | ≥+30 | 匿名问卷 | 待调研 |
| 无P0事故运行时长 | ≥3个月 | 事故记录 | 待建设 |

## 8.2 分步过渡路线

```
达标确认
    │
    ▼
第1个月: 选2个班组长自愿试点 6×12
    │  (选择最信任系统的、数据反馈最积极的)
    │
    ▼
第2-3个月: 扩大到4-6个班组长
    │  (前提: 试点班组无P0事故)
    │
    ▼
第4-6个月: 全量切换
    │  (前提: 扩大组P0事故=0)
    │
    ▼
持续监控: 
  - 每周统计"不在场风险"指标
  - 任何一个月P0事故>0 → 暂停扩展 → 回滚到上一阶段
```

## 8.3 "不在场风险"持续监控

| 监控指标 | 频率 | 判定标准 |
|----------|------|----------|
| 告警升级次数 | 每周 | ↓ 或持平 = 安全 |
| 未闭环告警数 | 每周 | ↓ 或持平 = 安全 |
| 真实生产异常数 | 每周 | ↓ 或持平 = 安全 |

**如果三个数字连续4周不升反降 → 就是6×12的最好证据。**

---

# 第九部分：成本模型与ROI（精确版）

## 9.1 云资源成本（基于阿里云）

| 项目 | 用途 | Phase 0-1A | Phase 1B-2 | Phase 3-5 |
|------|------|------------|------------|-----------|
| ECS 2台(4C8G) | Agent引擎+Web管理台 | ¥600 | ¥1,200 | ¥1,200 |
| RDS MySQL | 告警+状态机+评测数据 | ¥400 | ¥800 | ¥800 |
| Redis | 延迟升级队列 | ¥200 | ¥400 | ¥400 |
| LLM API (DeepSeek) | Query模式+Skill推理 | ¥200 | ¥800 | ¥1,500 |
| 企微推送 | 通知通道 | ¥0 | ¥0 | ¥0 |
| **月度合计** | | **¥1,400** | **¥3,200** | **¥3,900** |

**年度预算**：约¥35,000-47,000（Phase 2全量后）。

> 对比主动智能层原方案（¥3,400/月MVP），v2.0因融合Query模式增加了LLM调用成本和评测基础设施，但Query模式带来的效率提升远超这笔成本。

## 9.2 人力投入

| 阶段 | 数据工程师 | AI运维 | 业务专家 | Simon | 合计人月 |
|------|-----------|--------|----------|-------|----------|
| Phase 0 (2周) | 0.3 | 0.3 | - | 0.1 | 0.7 |
| Phase 1A (2周) | 0.3 | 0.3 | 0.2 | 0.1 | 0.9 |
| Phase 1B (6周) | 0.8 | 1.0 | 0.5 | 0.2 | 2.5 |
| Phase 2 (8周) | 0.5 | 0.8 | 0.8 | 0.3 | 2.4 |
| Phase 3 (6周) | 0.3 | 0.8 | 0.6 | 0.2 | 1.9 |
| Phase 4-5 (持续) | 0.3 | 0.5 | 0.3 | 0.2 | 1.3/月 |
| **合计（首年）** | | | | | **~12人月** |

## 9.3 ROI预估

| 场景 | 当前耗时 | 目标耗时 | 月度频次 | 月节省时间 |
|------|----------|----------|----------|------------|
| 查询生产数据 | 5-10min | 10s | 60次 | ~8h |
| 班次交接检查 | 15min | 自动(0min) | 60次 | ~15h |
| OEE异常排查 | 2-4h | 5min | 4次 | ~14h |
| 刀具寿命监控 | 2h/天(手工) | 自动(0min) | 30天 | ~60h |
| 质量归因分析 | 4h | 30min | 4次 | ~14h |
| 月报汇总 | 1-2天 | 30min | 1次 | ~14h |
| **月度合计** | | | | **~125h** |

按综合时薪¥80计算，月度直接节省¥10,000，年度¥120,000。
对比年度总成本约¥47,000（云资源）+ 12人月人力，ROI在第一年即可转正。

---

# 第十部分：方案自身的风险管理

做主动智能层+Data Agent，这个方案本身也有风险：

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|----------|
| 数据源接口对接超预期 | 高 | Phase 1B延期 | 提前1周做接口联调，审计前置 |
| 班组长不点反馈按钮 | 中 | 没数据调阈值 | Phase 1A选最积极班组试点，HR经理亲自带 |
| LLM调用费用超预算 | 低 | 月成本翻倍 | Query模式用缓存，日调用量封顶；Watch模式LLM仅用于R06 |
| 刀具管理系统接口不可用 | 中 | R01/R02无法上线 | 先上R04/R07/R10等不依赖刀具的风险 |
| 三坐标只有PDF无数据库 | 中 | CMM MCP延期 | 推动厂商开放API；短期用CSV导出+手动导入过渡 |
| Agent生成的SQL被误执行 | 低 | 数据污染 | Sandbox强制只读；生产写操作需人工审批 |
| 告警疲劳（推送太多） | 中 | 用户忽略告警 | Phase 1A严格控制日推送≤3条；聚合+抑制+冷却 |
| 组织变革受阻 | 中 | 7×12→6×12延期 | 用数据说话；先自愿试点，不强推 |
| 关键人员离职 | 低 | 知识断层 | 文档>人；Skill机制本身就是知识沉淀 |

---

# 附录：v1.0→v2.0变更对照表

| 维度 | v1.0 (InfoQ单线) | v2.0 (双源融合) | 变更理由 |
|------|------------------|-----------------|----------|
| **核心范式** | 被动问答（问模式） | 问守双模（Query+Watch） | 主动智能层补充了"守"的完整方法论 |
| **阶段数** | 5阶段 | 7阶段（加Phase 0+1A，拆分深度分析） | 信任先行，基础设施和业务风险解耦 |
| **第一阶段** | 数据入仓+元数据治理 | Phase 0空壳跑通+信任建立 | "制造业的信任，一次就够了" |
| **数据接入** | 全量入仓（SQLite） | MCP Server优先，按需入仓 | 异构系统不改动，实时性更好 |
| **MVP策略** | 全面铺开 | 三条低成本风险先行 | 信任>功能，低成本>高价值排序 |
| **规则管理** | 语义模型（单一） | 语义模型+风险目录（双轨） | 回答"是多少"和"会不会出事"需要不同结构 |
| **上线验证** | 无 | 影子模式（全部功能强制） | 制造业不容"先上线再调试" |
| **容错设计** | 无 | 三层降级+手动SOP | 生产制造必须回答"系统挂了怎么办" |
| **组织变革** | 定性描述 | 定量放行标准+分步过渡 | 7×12→6×12需要数据驱动，不能凭感觉 |
| **成本模型** | 粗略估算 | 分阶段精确估算+ROI计算 | 厂长批预算需要数字 |
| **深度案例** | 无 | 刀具磨损→尺寸四步分析链 | 主动智能层第三篇提供的制造业专属深度案例 |
| **团队分工** | 角色定义 | RACI矩阵（谁干/谁拍板/谁知情） | 明确边界，减少推诿 |
| **自身风险** | 7条通用风险 | 9条方案特有风险+缓解措施 | 做方案的人也要管方案的风险 |

---

## 核心结论

v1.0的InfoQ Data Agent方案解决了"**怎么聪明地回答**"的问题——架构是对的，阶段划分也是合理的。

v2.0融合主动智能层后，回答了v1.0没回答的五个关键问题：

1. **怎么让用户第一次就信任？** → Phase 0空壳跑通 + Phase 1A三条低成本风险先行
2. **数据不完美怎么办？** → 数据就绪度审计先行，不满足不硬上；MCP Server封装而非全量入仓
3. **系统挂了生产怎么办？** → 三层降级 + A4纸手动SOP
4. **怎么从工具变成组织变革的驱动力？** → 定量放行标准 + 分步过渡路线 + 不在场风险持续监控
5. **怎么让Agent从被动回答变成主动守护？** → 问守双模统一引擎，80%代码复用

**一句话总结**：InfoQ教我们造一个聪明的"问答机器人"，主动智能层教我们造一个可靠的"数字班组长"。v2.0把两者合为一体——它既能在你问的时候精准回答，也能在你不在的时候替你盯着。

---

> **文档版本**：v2.0
> **编制**：Woker（Hermes Agent）+ Simon
> **最后更新**：2026-07-05
> **关联文档**：
> - [[企业级数据Agent落地方案]]（v1.0 — InfoQ单线方案）
> - [[主动智能层_首批风险清单与架构方案]]
> - [[主动智能层_优化版实施方案]]
> - [[工作分配与API建设深度拆解]]
> - [[产线数据管道架构]]
> - [[OEE分析体系]]
> - [[日报分析系统]]
