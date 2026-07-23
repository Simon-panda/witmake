---
title: fuadmin数据字典总览
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引, 已完成]
---

# fuadmin 数据字典总览

> 逆向工程自 fuadmin（MySQL 8.0.29，Django MES/ERP "治通"）｜ 334 基表 / 5,877 字段 ｜ 生成： 2026-07-23
> 用途：**各业务模块 Agent 的基础知识文件**——单文档可独立上岗，跨模块接口支撑协作

## 0. 阅读须知（方法与置信度体系）

本字典由 AI 逆向工程生成，**原始注释覆盖率仅 2.2%**，绝大多数语义为推断。每条推断标注证据来源与置信度：

| 标记 | 含义 |
|------|------|
| `fk` | InnoDB 硬外键（43 个），最高可信 |
| `sample` | 样本数据佐证（唯一索引/枚举值/格式验证） |
| `naming` | 字段命名惯例推断（`<entity>_id`、`<a>_<b>_mapping` 桥表等） |
| 置信度 high/mid/low | 高=可直接采信；中=大概率正确；低=需人工确认（文中标"待确认"） |
| `[脏注释-待清理]` | dump 修复残留垃圾注释（形如 `'xxx_view' is not BASE TABLE`），勿采信 |

全局惯例：`creator_id` 等 `*_id` 多逻辑指向 `system_users.id`（无硬 FK）；`historical*` 为历史快照表（history_type: +新增 / ~修改 / -删除，history_user_id→system_users 硬 FK）；站点后缀 `_gh`=广汇、`_tf`=TF铸造（泰峰）、`_zt`=治通同构分表。

## 1. 全局语义图谱（业务视角）

```mermaid
graph LR
    subgraph 供应端["🏭 供应端"]
        SUP["供应商 supplier"]
        MAT["采购物料 purchase_material"]
        SMM["供应商-物料映射 协议价·税 ✓"]
    end
    subgraph 采购执行["📋 采购执行"]
        PR["采购申请 PR/ZJPR"]
        PO["采购订单 PO"]
        POD["采购明细 回链申请行 ✓"]
        DOC["采购单据 合同/发票"]
        PMSI["到货入库 PMSI单号回写 ✓"]
    end
    subgraph 资金结算["💰 资金结算"]
        PAY["付款申请 直连PO·带索引 ✓"]
        SET["结算单·发票 ⚠️建成未启用"]
        ALLOC["两级分摊核销 ⚠️未启用"]
    end
    subgraph 生产铸造["🔥 生产铸造"]
        PLAN["生产计划 7张批次桥表"]
        CM["制芯批次 S2K-*"]
        RA["生产批次单号 RA5-*"]
        WO["工单/工号 job_code"]
        SHIFT["班次/新排程 ↔工资挂钩 ✓UNI"]
    end
    subgraph 质量追溯["🔍 质量追溯 IATF"]
        QC["检验标准/记录"]
        QR["一物一码 0HKG码系"]
        BOX["箱码AI复核 box_code_verify"]
        BAD["不良登记 bad_product"]
        RW["返工单 rework_header"]
        CMM["CMM三坐标"]
    end
    subgraph 订单交付["📦 订单交付"]
        CUST["客户"]
        CO["客户订单 PD单号 箱×每箱 ✓"]
        SEND["发货扫码 sendout 3.9万"]
        WB["物流运单 waybill"]
    end
    subgraph 人力协同["👥 人力协同"]
        EMP["员工 system_users 锚点"]
        DR["日报/任务 ⭐"]
        ATT["考勤打卡 ⚠️punch_time≠入库时间"]
        SAL["工资/能力评分"]
    end
    供应端 ==>|"supplier_material_map_id ✓实接口"| 采购执行
    SUP --> SMM --> POD
    PR -->|审批流 approval_process JSON| PO
    PO --> POD --> DOC
    POD -->|stock_quantity 累计回写| PMSI
    PO -->|purchase_order_id 主链路| PAY
    PAY -.->|settlement_bill_id 预留·多为空| SET
    SET -.-> ALLOC
    CO --> SEND --> BOX
    CUST --> CO
    SEND --> WB
    QR -->|UPPER()对齐 ⚠️大小写不一致| BOX
    BAD --> RW -->|换码闭环 ✓两模块唯一实体级FK| QR
    QC --> BAD
    QC --> CMM
    PLAN --> CM
    CM -->|一批次对一单号 一单号对多批次 ✓锚点注释| RA
    RA --> WO
    WO --> SHIFT
    EMP -->|填报| DR
    EMP -->|工号字符串对齐 ⚠️无FK| WO
    EMP --> ATT
    SHIFT -->|newscheduling_id| SAL
```

图例：✓=已验证（FK/唯一索引/样本）｜⚠️=重要陷阱｜实线=已验证关系｜虚线=预留/推断关系

## 2. 模块导航（按业务域）

### 01-供应链域（109表）——供应商→采购→入库→结算→付款

| 模块 | 表数 | 一句话 | 文档 |
|---|---|---|---|
| purchase-采购 | 43 | 申请→订单→明细→单据全链路+16张历史快照 | [[采购模块-fuadmin数据字典]] |
| settlement-结算 | 24 | 对账/开票/两级付款分摊，⚠️全部0行建成未启用 | [[结算模块-fuadmin数据字典]] |
| warehouse-仓储 | 13 | 入库/出库/库存/库位，PMSI入库单号回写采购 | [[仓储模块-fuadmin数据字典]] |
| logistics-物流 | 11 | 发货/运单/签收；车辆司机为文本字段非实体 | [[物流模块-fuadmin数据字典]] |
| supplier-供应商 | 8 | 供应商主数据+协议价映射（采购取价枢纽） | [[供应商模块-fuadmin数据字典]] |
| payment-付款 | 8 | 付款申请双回链：采购单（主）+结算单（预留） | [[付款模块-fuadmin数据字典]] |
| return-退货 | 2 | 质量退货按0HKG二维码一物一码逐件登记 | [[退货模块-fuadmin数据字典]] |

### 02-生产铸造域（61表）

| 模块 | 表数 | 一句话 | 文档 |
|---|---|---|---|
| tf-TF铸造 | 31 | 制芯→浇铸→打箱，批次桥表追溯主通道 | [[TF铸造模块-fuadmin数据字典]] |
| qrcode-二维码追溯 | 12 | 现役4表：发货扫码→箱码复核→换码；新结构未启用 | [[二维码追溯模块-fuadmin数据字典]] |
| plan-生产计划 | 6 | 生产计划与排产 | [[生产计划模块-fuadmin数据字典]] |
| production-生产 | 3 | 生产执行/跟踪 | [[生产模块-fuadmin数据字典]] |
| shift-班次 | 3 | 排班模板+实例，白/夜班 | [[班次模块-fuadmin数据字典]] |
| newscheduling-新排程 | 2 | ⭐报工核心：产量/工时/工废/料废/宕机，工资挂钩 | [[新排程模块-fuadmin数据字典]] |
| bad-不良品 | 4 | 不良登记→返工，两套口径勿相加 | [[不良品模块-fuadmin数据字典]] |

### 03-质量技术域（52表）

| 模块 | 表数 | 一句话 | 文档 |
|---|---|---|---|
| knife-刀具 | 14 | 刀具库存/领用/换刀/回收全生命周期 | [[刀具模块-fuadmin数据字典]] |
| tool-工具工装 | 5 | 工具工装台账 | [[工具工装模块-fuadmin数据字典]] |
| fixture-工装夹具 | 3 | 夹具台账与使用 | [[工装夹具模块-fuadmin数据字典]] |
| inspection-质量检验 | 5 | 检验标准/记录/快速响应 | [[质量检验模块-fuadmin数据字典]] |
| product-产品 | 6 | 产品主数据/型号 | [[产品模块-fuadmin数据字典]] |
| measuring-测量计量 | 3 | 仪器台账/校准/CMM三坐标 | [[测量计量模块-fuadmin数据字典]] |
| equipment-设备 | 5 | 点检/保养/维修工单/维修报告（DJDH/BYDH/BXDH单号） | [[设备模块-fuadmin数据字典]] |
| device-设备装置 | 4 | 设备台账锚点（internal_code），切削液检查 | [[设备装置模块-fuadmin数据字典]] |
| maintenance-维修保养 | 2 | ⚠️试点残留（3+9行），勿用于统计 | [[维修保养模块-fuadmin数据字典]] |
| process-工艺技术 | 2 | jgdm日产记录（V2迁移）；在制品库存未启用 | [[工艺技术模块-fuadmin数据字典]] |

### 04-订单项目域（21表）

| 模块 | 表数 | 一句话 | 文档 |
|---|---|---|---|
| project-项目 | 13 | 项目台账/人员/物料归集；detail_copy1两版口径并存 | [[项目模块-fuadmin数据字典]] |
| order-订单 | 5 | 客户订单 PD单号，箱数×每箱=总数 | [[订单模块-fuadmin数据字典]] |
| finance-财务 | 2 | 财务辅助 | [[财务模块-fuadmin数据字典]] |
| customer-客户 | 1 | 客户主数据 | [[客户模块-fuadmin数据字典]] |

### 05-人事系统域（46表）

| 模块 | 表数 | 一句话 | 文档 |
|---|---|---|---|
| system-用户权限 | 28 | system_users 员工锚点+部门/角色/权限 | [[用户权限模块-fuadmin数据字典]] |
| hr-人力能力 | 13 | 能力评分/人力矩阵/工号/花名册/工资/假期 | [[人力能力模块-fuadmin数据字典]] |
| dailyreport-日报任务 | 4 | ⭐日报/日任务/月任务，提交审核流 | [[日报任务模块-fuadmin数据字典]] |
| att-考勤打卡 | 1 | 打卡流水（疫情期体温/口罩字段遗留） | [[考勤打卡模块-fuadmin数据字典]] |

### 06-其他定制（67表）+ 07-框架表（16表）

| 模块 | 一句话 | 文档 |
|---|---|---|
| 零散模块总览 | 专机/外部对接/试验表16组导航（三角梁视觉/E38边缘检验/5S/报警等） | [[零散模块总览-fuadmin数据字典]] |
| django-auth框架 | Django标准表16张，auth闲置/admin日志/celery调度 | [[django-auth框架-fuadmin数据字典]] |

## 3. 跨模块主干业务流（已验证）

```
供应商 ──映射协议价──> 采购申请(PR) ─审批─> 采购订单(PO) ─> 采购明细
                                                          │
            ┌─────────────────────────────────────────────┤
            ▼                                             ▼
      到货入库(PMSI回写) ──> 库存                        采购单据(合同/发票)
            │                                             │
            ▼                                             ▼
      检验(合格/退货0HKG码) ──> 生产/铸造(批次) ──> 发货扫码 ─> 箱码复核 ─> 客户
                                                          │
      付款申请 ◄──purchase_order_id(主链路)─────────────────┘
      结算单/发票/两级分摊 【已建成未启用，预留】
```

质量闭环：不良登记 → 返工单 →（两模块唯一实体级 FK）→ 换码 → 追溯码系统
人力闭环：排班 → 报工(newscheduling) → 工资(salary.newscheduling_id UNIQUE 挂钩)

## 4. 重要数据陷阱 TOP10（所有 Agent 必读）

| # | 陷阱 | 影响 | 应对 |
|---|---|---|---|
| 1 | **settlement 结算 24 表全部 0 行** | 当现役统计会得 0 | 付款走 payment 直连 PO 口径；结算为预留设计 |
| 2 | **人员弱引用**：全库用"工号+姓名"字符串（如"21578 某某"）或工号前缀，无 FK | JOIN 失败 | 按工号前缀拆分对碰 system_users |
| 3 | **站点分表** `_gh/_tf/_zt`：同构；`_zt` 除物料表（2017老数据）外全 0 | 重复/污染统计 | 默认查无后缀现役表，跨站点需 UNION 并标注 |
| 4 | **批次编码双轨**：制芯 S2K-* ≠ 生产单号 RA5-* | 追溯断链 | 经 7 张 *_production_plan 桥表转换，勿直接对碰 |
| 5 | **箱码大小写不一致**（UMPxx/umpxx） | 匹配丢失 | 对碰统一 `UPPER()` |
| 6 | **考勤 punch_time ≠ 入库时间**（脱机缓存批量上传，样本 2025-10 打卡 2026-05 入库） | 考勤统计错位 | 一律用 punch_time，勿用 create_datetime |
| 7 | **非标准 JSON**：`cc_personnel` 等为 Python repr（`['21931 某某']`） | json.loads 报错 | 用 `ast.literal_eval` 解析 |
| 8 | **同名字段类型漂移**：`inspection_states`/`rate`/`furnace_number` 在不同表 int/varchar/decimal 不一 | UNION/比较报错 | 显式 CAST；以各表字典为准 |
| 9 | **两套口径并存**：bad_product(正式) vs defective_product(日报)；maintenance_records 两表；detail_copy1 头/行两版 | 数字翻倍 | 认准各模块避坑节指定口径，勿相加 |
| 10 | **脏注释**：8 条 `'xxx_view' is not BASE TABLE' 残留 | 误导语义 | 已标记 [脏注释-待清理]，勿采信 |

另：`create_datetime` 存在 `0000-00-00` 迁移遗留（时间过滤报错，需 NULLIF）；`_MASK_TO_V2`/`_MUSID_SYNC_V2` 为 V2 迁移同步字段（业务查询忽略）。

## 5. 字段备注整改计划（给软件工程师）

- **现状**：字段注释覆盖率 2.2%（141/6,403），新人上手与 AI 理解的最大瓶颈
- **产出**：`90-工程/fuadmin数据字典/字段备注整改计划.md` + `remediation.sql`
- **总量**：5,621 条建议注释（P0 高优先 3,035 / P1 1,470 / P2 低置信 1,116 + 8 条脏注释清理）
- **流程**：按 P0→P1→P2 分批，工程师评审（重点 P2 低置信与"待确认"项）→ 执行 ALTER
- **原则**：建议注释由命名+样本+Django 惯例推断，**评审前勿直接执行**；低置信项是排雷重点

## 6. 作为 Agent 基础文件的使用指南

**独立上岗**：每个模块文档 = 概述（业务定位）+ 上岗指南（核心实体/业务流/SQL 场景/避坑）+ 全字段字典 + ER + 跨模块接口。把单个 .md 喂给对应模块 Agent 即可工作。

**分工协作**：跨模块需求（如采购 Agent 需供应商协议价）→ 查本文 §2 导航定位目标模块 → 查目标模块文档"5 跨模块接口"节拿到确切关联字段与置信度。

**写作纪律**：Agent 产出查询前必读目标模块"2.4 避坑提示"；凡文档标"待确认"处禁止臆造，应向软件工程师/业务确认后回写文档。

**关联文件**：
- 全局关联矩阵（288 条，跨模块 146）：`关联矩阵.md`
- 全局物理关系图（模块级 Mermaid）：`全局物理关系图.mmd`
- 语义图谱 JSON-LD（387 节点，供程序消费）：`fuadmin-graph.jsonld`
- 整改计划与 SQL：`字段备注整改计划.md` / `remediation.sql`
