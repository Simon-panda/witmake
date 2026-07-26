---
title: 生产计划模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 02-生产铸造域
tags: [工程, 数据字典2, 代码实证, 生产计划]
---

# 生产计划模块 · fuadmin 数据字典2（代码实证版）
> 域: 02-生产铸造域 | 表数: 6 | 字段: 88 | 代码锚定: 87(99%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/02-生产铸造域/生产计划模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_plan_delivery_plan` | 发货需求计划 | 520 | 💻 |
| `generator_plan_delivery_plan_log` | 发货计划操作记录 | 707 | 💻 |
| `generator_plan_inventory_snapshot` | 库存盘点 | 799 | 💻 |
| `generator_plan_monthly_start_stock` | 月度起始数 | 4 | 💻 |
| `generator_plan_product_config` | 产品计划主数据 | 46 | 💻 |
| `generator_scheduling` | 排班表 | 4379 | 💻 |

---

### generator_plan_delivery_plan
**定义**：发货需求计划 ｜ **代码**：`generator/delivery/model.py` ｜ **行数(估)**：520

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `period_type` | varchar(10) | N | - | 计划周期；枚举[year=年计划,month=月计划,day=日计划] | ✅🔢 |  |
| `plan_date` | date | N | - | 计划日期；年取1月1日，月取当月1日，日取当天 | ✅ |  |
| `year` | int | N | - | 年份：冗余字段，方便聚合查询 | ✅⚖️ |  |
| `month` | int | Y | - | 月份：日/月计划才有值 | ✅⚖️ |  |
| `demand_qty` | int | N | - | 需求量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `customer_order_id` | bigint | Y | MUL | 生成的订单；→generator_customer_order | ✅🔗 | →generator_customer_order |
| `product_config_id` | bigint | N | MUL | 产品；→generator_plan_product_config | ✅🔗 | →generator_plan_product_config |

### generator_plan_delivery_plan_log
**定义**：发货计划操作记录 ｜ **代码**：`generator/delivery/model.py` ｜ **行数(估)**：707

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断]主键（自增ID） | 🔍 |  |
| `plan_snapshot` | varchar(200) | N | - | 计划标识；产品/站点/周期/日期，冗余便于删除后回溯 | ✅ |  |
| `action` | varchar(20) | N | - | 操作类型；枚举[create=创建,update=修改,delete=删除,gen_order=生成订单] | ✅🔢 |  |
| `old_value` | int | Y | - | 修改前需求量 | ✅ |  |
| `new_value` | int | Y | - | 修改后需求量 | ✅ |  |
| `operator` | varchar(50) | N | - | 操作人 | ✅ |  |
| `operate_time` | datetime(6) | N | - | 操作时间 | ✅ |  |
| `remark` | varchar(255) | Y | - | 备注 | ✅ |  |
| `delivery_plan_id` | bigint | Y | MUL | 发货计划；→generator_plan_delivery_plan | ✅🔗 | →generator_plan_delivery_plan |

### generator_plan_inventory_snapshot
**定义**：库存盘点 ｜ **代码**：`generator/delivery/model.py` ｜ **行数(估)**：799

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `snapshot_date` | date | N | - | 盘点日期；本次盘点的日期 | ✅ |  |
| `finished_stock` | int | N | - | 库存成品数 | ✅ |  |
| `scrap_stock` | int | N | - | 库存报废品数 | ✅ |  |
| `blank_stock` | int | N | - | 毛坯库存 | ✅ |  |
| `in_process_qty` | int | N | - | 生产流转中(待入+品质过程数) | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `product_config_id` | bigint | N | MUL | 产品；→generator_plan_product_config | ✅🔗 | →generator_plan_product_config |
| `repair_stock` | int | N | - | 返修库存 | ✅ |  |
| `customer_stock` | int | N | - | 客户方库存；已提前发货存放在客户仓库、尚未被客户生产消耗的数量 | ✅ |  |

### generator_plan_monthly_start_stock
**定义**：月度起始数 ｜ **代码**：`generator/delivery/model.py` ｜ **行数(估)**：4

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `product_name` | varchar(50) | N | MUL | 产品名称 | ✅ |  |
| `year` | int | N | - | 年份 | ✅ |  |
| `month` | int | N | - | 月份 | ✅ |  |
| `start_stock` | int | N | - | 月度起始数；该月差额行的初始值（期初在途/库存） | ✅ |  |
| `expected_total_demand` | int | N | - | 预计总订单需求 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_plan_product_config
**定义**：产品计划主数据 ｜ **代码**：`generator/delivery/model.py` ｜ **行数(估)**：46

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `product_name` | varchar(50) | N | MUL | 产品名称 | ✅ |  |
| `customer_name` | varchar(50) | N | - | 对应客户 | ✅ |  |
| `part_number` | varchar(50) | Y | - | 零件号 | ✅ |  |
| `box_capacity` | int | Y | - | 装箱量/SNP：每箱数量（合并后唯一保留字段） | ✅⚖️ |  |
| `daily_capacity` | int | Y | - | 日产能(SMP) | ✅ |  |
| `production_line` | varchar(50) | Y | - | 产线/接口 | ✅ |  |
| `contact_person` | varchar(50) | Y | - | 客户端对接人 | ✅ |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `site` | varchar(20) | N | - | 站点；治通 / 广汇 / 泰峰 | ✅ |  |

### generator_scheduling
**定义**：排班表 ｜ **代码**：`generator/scheduling/model.py` ｜ **行数(估)**：4379

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | MUL | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `actual_output` | int | Y | - | 实际生产数量 | ✅ |  |
| `work_hours` | decimal(13,1) | Y | - | 工作时间 | ✅ |  |
| `date` | date | Y | - | 日期 | ✅ |  |
| `day_night` | varchar(255) | Y | - | 早/晚班 | ✅ |  |
| `work_state` | varchar(255) | Y | - | 工作状态 | ✅ |  |
| `code_id` | bigint | Y | MUL | 工号；→system_users | ✅🔗 | →system_users |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `production_line_id` | bigint | Y | MUL | 工序产线；→generator_production_line | ✅🔗 | →generator_production_line |
| `train_user_code_id` | bigint | Y | MUL | 培训人ID；→system_users | ✅🔗 | →system_users |
| `plan_output` | int | Y | - | 计划生产数量 | ✅ |  |
| `downtime` | int | Y | - | 停机时间 | ✅ |  |

---

## 同域兄弟模块
- [[02-生产铸造域/不良品模块-fuadmin数据字典2|不良品模块]]
- [[02-生产铸造域/新排程模块-fuadmin数据字典2|新排程模块]]
- [[02-生产铸造域/生产模块-fuadmin数据字典2|生产模块]]
- [[02-生产铸造域/二维码追溯模块-fuadmin数据字典2|二维码追溯模块]]
- [[02-生产铸造域/班次模块-fuadmin数据字典2|班次模块]]
- [[02-生产铸造域/TF铸造模块-fuadmin数据字典2|TF铸造模块]]
- [[02-生产铸造域/02-生产铸造域-业务流|02-生产铸造域业务流(代码验证版)]]
