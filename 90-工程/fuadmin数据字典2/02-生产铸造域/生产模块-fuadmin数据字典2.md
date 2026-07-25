---
title: 生产模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 02-生产铸造域
tags: [工程, 数据字典2, 代码实证, 生产]
---

# 生产模块 · fuadmin 数据字典2（代码实证版）
> 域: 02-生产铸造域 | 表数: 3 | 字段: 58 | 代码锚定: 54(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/02-生产铸造域/生产模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_production_knife_issue` | 生产部领刀 | 21764 | 💻 |
| `generator_production_line` | 工序产线管理 | 166 | 💻 |
| `generator_production_tracking` | 生产跟踪单 | 0 | 💻 |

---

### generator_production_knife_issue
**定义**：生产部领刀 ｜ **代码**：`generator/production_knife_issue/model.py` ｜ **行数(估)**：21764

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `factory_name` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `receiver_name` | varchar(255) | Y | - | 领刀人 | ✅ |  |
| `layer_number` | varchar(255) | Y | - | 层数 | ✅ |  |
| `cabinet_number` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `model_number` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier_name` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `barcode` | varchar(255) | Y | - | 条码 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]掩码同步标记列(V2去向侧)，无代码锚点，非业务字段 | 🔍 |  |

### generator_production_line
**定义**：工序产线管理 ｜ **代码**：`generator/production_line/model.py` ｜ **行数(估)**：166

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:产线名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 排序 | ✅ |  |
| `status` | varchar(255) | Y | - | 状态（界面:启用） | ✅🖥️ |  |
| `process_state` | varchar(255) | Y | - | 产线状态 | ✅ |  |
| `type` | varchar(255) | Y | - | 工作类型 | ✅ |  |
| `name` | varchar(255) | Y | UNI | 产线名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 上级产线；→generator_production_line | ✅🔗 | →generator_production_line |

### generator_production_tracking
**定义**：生产跟踪单 ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:产品） | ✅📦🖥️ |  |
| `remark` | longtext | Y | - | 备注 | ✅ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `tracking_number` | varchar(50) | N | UNI | 跟踪单号 | ✅ |  |
| `product_name` | varchar(100) | Y | - | 产品名称 | ✅ |  |
| `total_quantity` | int | N | - | 总数量 | ✅ |  |
| `current_quantity` | int | N | - | 当前数量 | ✅ |  |
| `current_sequence` | int | N | - | 当前工序顺序 | ✅ |  |
| `process_status` | varchar(20) | N | - | 工序状态；pending/in_progress/completed | ✅ |  |
| `status` | varchar(20) | N | - | 跟踪单状态；pending/in_progress/completed/scrapped | ✅ |  |
| `source_type` | varchar(20) | Y | - | 来源类型；plan/manual/order | ✅ |  |
| `source_id` | int | Y | - | 来源ID | ✅ |  |
| `source_number` | varchar(50) | Y | - | 来源单号 | ✅ |  |
| `plan_start_date` | date | Y | - | 计划开始日期 | ✅ |  |
| `plan_end_date` | date | Y | - | 计划完成日期 | ✅ |  |
| `actual_start_date` | date | Y | - | 实际开始日期 | ✅ |  |
| `actual_end_date` | date | Y | - | 实际完成日期 | ✅ |  |
| `site` | varchar(20) | Y | - | 工作地点 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `product_id` | bigint | Y | MUL | 产品；→generator_product | ✅🔗 | →generator_product |
| `current_route_step_id` | bigint | Y | MUL | 当前路线步骤；→track_route_step | ✅🔗 | →track_route_step |
| `current_station_id` | bigint | Y | MUL | 当前站点；→track_station | ✅🔗 | →track_station |
| `route_id` | bigint | Y | MUL | 工艺路线；→track_route | ✅🔗 | →track_route |
