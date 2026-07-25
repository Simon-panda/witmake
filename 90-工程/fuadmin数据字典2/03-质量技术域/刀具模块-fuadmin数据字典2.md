---
title: 刀具模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 刀具]
---

# 刀具模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 14 | 字段: 338 | 代码锚定: 300(89%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/刀具模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_abnormal_tool_filtering_data` | 刀具异常过滤数据 | 18484 | 💻 |
| `generator_daily_tool_summary` | 每日刀具汇总 | 0 | 💻 |
| `generator_djgkcsl` |  | 0 | 🔍 |
| `generator_djgsy` | 刀具柜使用情况 | 0 | 💻 |
| `generator_djkc` | 刀具柜库存 | 4066 | 💻 |
| `generator_eng_tool_knives` | 工程部放刀 | 15947 | 💻 |
| `generator_knife_detail` | 刀具明细表 | 11106 | 💻 |
| `generator_knife_life_standards` | 刀具生命周期标准 | 38 | 💻 |
| `generator_knife_life_standards_copy1` | 刀具生命周期标准 | 89 | 🏭 |
| `generator_knife_requisition` | 刀具领料明细 | 36808 | 💻 |
| `generator_knife_statistics` | 刀具合并数据统计 | 26479 | 💻 |
| `generator_machine_tool_change` | 机床换刀表 | 26984 | 💻 |
| `generator_old_knife_recycle` | 刀具柜旧刀回收 | 9362 | 💻 |
| `knife_jobcode` | 刀具-工作代号转换表 | 389 | 💻 |

---

### generator_abnormal_tool_filtering_data
**定义**：刀具异常过滤数据 ｜ **代码**：`generator/abnormal_tool_filtering_data/model.py` ｜ **行数(估)**：18484

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:条形码） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `barcode` | varchar(255) | Y | - | 条形码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `is_resolved` | tinyint(1) | N | - | 是否解决；标记该异常信息是否已经解决 | ✅ |  |
| `push_datetime` | datetime(6) | Y | - | 推送时间；异常信息推送的具体时间 | ✅ |  |
| `pushed_exception_item` | varchar(255) | Y | - | 推送异常项；记录此次推送的具体异常项 | ✅ |  |

### generator_daily_tool_summary
**定义**：每日刀具汇总 ｜ **代码**：`generator/daily_tool_summary/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:条码） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `date_time` | date | Y | - | 入库时间 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `bar_code` | varchar(255) | Y | - | 条码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_djgkcsl
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:条码） | 🔍🖥️ |  |
| `remark` | varchar(255) | Y | - | （界面:备注） | 🔍🖥️ |  |
| `modifier` | varchar(255) | Y | - | （界面:修改人） | 🔍🖥️ |  |
| `belong_dept` | int | Y | - | （界面:所属部门） | 🔍🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | （界面:未结单） | 🔍🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | （界面:时间） | 🔍🖥️ |  |
| `sort` | int | Y | - | （界面:排序） | 🔍🖥️ |  |
| `数量` | decimal(13,4) | Y | - | 🔍待补充 | 🔍 |  |
| `型号` | varchar(255) | Y | - | 🔍待补充 | 🔍 |  |
| `条码` | varchar(255) | Y | - | 🔍待补充 | 🔍 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_djgsy
**定义**：刀具柜使用情况 ｜ **代码**：`generator/djgsy/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:柜号） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `machine_tool` | varchar(255) | Y | - | 机床 | ✅ |  |
| `number_of_layers` | varchar(255) | Y | - | 层数 | ✅ |  |
| `algorithm_detection_quantity` | varchar(255) | Y | - | 算法检测数量 | ✅ |  |
| `external_inspection_quantity` | varchar(255) | Y | - | 刀具型号（外检）数量 | ✅ |  |
| `old_knife_barcode` | varchar(255) | Y | - | 旧刀二维码 | ✅ |  |
| `new_knife_barcode` | varchar(255) | Y | - | 新刀二维码 | ✅ |  |
| `time_end` | varchar(255) | Y | - | 结束时间 | ✅ |  |
| `time_on` | varchar(255) | Y | - | 开始时间 | ✅ |  |
| `operator` | varchar(255) | Y | - | 操作人 | ✅ |  |
| `action` | varchar(255) | Y | - | 动作 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `CREATE_DATE` | datetime | Y | - | 创建时间 | ✅ |  |
| `CABINET_NUM` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |
| `reason_for_replacement` | varchar(255) | Y | - | 更换原因 | ✅ |  |
| `tool_model` | varchar(255) | Y | - | 刀具型号 | ✅ |  |

### generator_djkc
**定义**：刀具柜库存 ｜ **代码**：`generator/djkc/model.py` ｜ **行数(估)**：4066

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:工厂） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `input_number_3` | int | Y | - | 数量 | ✅ |  |
| `input_2` | varchar(255) | Y | - | 型号 | ✅ |  |
| `input_1` | varchar(255) | Y | - | 条码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `input_number_2` | int | Y | - | 理想库存 | ✅ |  |
| `input_number_1` | int | Y | - | 安全库存 | ✅ |  |
| `input_5` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `input_6` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_eng_tool_knives
**定义**：工程部放刀 ｜ **代码**：`generator/eng_tool_knives/model.py` ｜ **行数(估)**：15947

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
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `knife_leader` | varchar(255) | Y | - | 领刀人 | ✅ |  |
| `number_of_layers` | varchar(255) | Y | - | 层数 | ✅ |  |
| `cabinet_number` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `bar_code` | varchar(255) | Y | - | 条码 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_knife_detail
**定义**：刀具明细表 ｜ **代码**：`generator/knife_detail/model.py` ｜ **行数(估)**：11106

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:条码） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `cabinet_number` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `machine_tool` | varchar(255) | Y | - | 机床 | ✅ |  |
| `production_line` | varchar(255) | Y | - | 产线 | ✅ |  |
| `is_in_cabinet` | varchar(255) | Y | - | 是否在柜 | ✅ |  |
| `new_knife_quantity` | varchar(255) | Y | - | 新刀数量 | ✅ |  |
| `used_knife_layer_count` | varchar(255) | Y | - | 旧刀层数 | ✅ |  |
| `new_knife_layer_count` | varchar(255) | Y | - | 新刀层数 | ✅ |  |
| `new_knife_column_count` | varchar(255) | Y | - | 新刀列数 | ✅ |  |
| `online_knife_processing_volume` | varchar(255) | Y | - | 在线刀具加工量 | ✅ |  |
| `offline_knife_processing_volume` | varchar(255) | Y | - | 下线刀具加工量 | ✅ |  |
| `knife_recycling_person` | varchar(255) | Y | - | 回收人 | ✅ |  |
| `knife_recycling_time` | varchar(255) | Y | - | 回收时间 | ✅ |  |
| `knife_dismounting_person` | varchar(255) | Y | - | 换下人 | ✅ |  |
| `knife_dismounting_time` | varchar(255) | Y | - | 换下时间 | ✅ |  |
| `knife_mounting_person` | varchar(255) | Y | - | 装上人 | ✅ |  |
| `knife_mounting_time` | varchar(255) | Y | - | 装上时间 | ✅ |  |
| `knife_placing_person` | varchar(255) | Y | - | 放刀人 | ✅ |  |
| `knife_placing_time` | varchar(255) | Y | - | 放刀时间 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `barcode` | varchar(255) | Y | - | 条码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `knife_usage_hours` | varchar(255) | Y | - | 刀具使用时间 (小时) | ✅ |  |
| `used_knife_quantity` | varchar(255) | Y | - | 旧刀数量 | ✅ |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_knife_life_standards
**定义**：刀具生命周期标准 ｜ **代码**：`generator/knife_life__standards/model.py` ｜ **行数(估)**：38

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `tool_model` | varchar(100) | Y | - | 刀具型号 | ✅ |  |
| `production` | varchar(20) | Y | - | 产品（界面:选择工作代号） | ✅🖥️ |  |
| `std_completed_quatitiy` | int | Y | - | 加工量标准值 | ✅ |  |
| `std_usage_hour` | double | Y | - | 时间标准值 | ✅ |  |
| `production_line_id` | varchar(100) | Y | - | 产线 | ✅ | →generator_production_line(推断) |
| `bar_code` | varchar(100) | Y | - | 条码（界面:条形码） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_knife_life_standards_copy1
**定义**：刀具生命周期标准 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/knife_life__standards/model.py` ｜ **行数(估)**：89

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `tool_model` | varchar(100) | Y | - | 刀具型号 | ✅ |  |
| `production` | varchar(20) | Y | - | 产品（界面:选择工作代号） | ✅🖥️ |  |
| `std_completed_quatitiy` | int | Y | - | 加工量标准值 | ✅ |  |
| `std_usage_hour` | double | Y | - | 时间标准值 | ✅ |  |
| `production_line_id` | varchar(100) | Y | - | 产线 | ✅ | →generator_production_line(推断) |
| `bar_code` | varchar(100) | Y | - | 条码（界面:条形码） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_knife_requisition
**定义**：刀具领料明细 ｜ **代码**：`generator/knife_requisition/model.py` ｜ **行数(估)**：36808

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:月份） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 备注 | ✅ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `newbar_code` | varchar(20) | Y | - | 新条码 | ✅ |  |
| `trade_in` | varchar(20) | Y | - | 以旧换新 | ✅ |  |
| `use_dept` | varchar(20) | Y | - | 使用部门 | ✅ |  |
| `dept` | varchar(20) | Y | - | 部门 | ✅ |  |
| `material_handler` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `money` | decimal(10,3) | Y | - | 金额 | ✅ |  |
| `unit_price` | decimal(10,3) | Y | - | 单价 | ✅ |  |
| `number` | int | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `name` | varchar(80) | Y | - | 产品名称 | ✅ |  |
| `bar_code` | varchar(20) | Y | - | 条形码 | ✅ |  |
| `subclass` | varchar(20) | Y | - | 次类别 | ✅ |  |
| `classes` | varchar(20) | Y | - | 类别 | ✅ |  |
| `project` | varchar(20) | Y | - | 项目 | ✅ |  |
| `supplier` | varchar(50) | Y | - | 供应商 | ✅ |  |
| `date_time` | date | Y | - | 日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `month_time` | varchar(20) | Y | - | 月份 | ✅ |  |
| `PO` | varchar(20) | Y | - | PO（界面:部门） | ✅🖥️ |  |
| `abnormal_info` | json | Y | - | 异常信息 | ✅ |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | 🔍待补充 | 🔍 |  |

### generator_knife_statistics
**定义**：刀具合并数据统计 ｜ **代码**：`generator/knife_statistics/model.py` ｜ **行数(估)**：26479

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:使用部门） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `combined_production_line` | varchar(100) | Y | - | 合并产线 | ✅ |  |
| `combined_tool_model` | varchar(80) | Y | - | 合并刀具型号 | ✅ |  |
| `online_tool_processing_quantity` | int | Y | - | 在线刀具加工量 | ✅ |  |
| `offline_tool_processing_quantity` | int | Y | - | 下线刀具加工量 | ✅ |  |
| `tool_usage_hours` | double | Y | - | 刀具使用时间(小时) | ✅ |  |
| `line_number` | varchar(10) | Y | - | 线号 | ✅ |  |
| `blade_change_time_old` | datetime(6) | Y | - | 换刀片时间_as_old | ✅ |  |
| `installed_new_blade_barcode` | varchar(255) | Y | - | 此时放上去新刀片的条码 | ✅ |  |
| `blade_model_old` | varchar(80) | Y | - | 换刀片型号_as_old | ✅ |  |
| `old_blade_barcode_after_change` | varchar(255) | Y | - | 换刀片旧刀条码 | ✅ |  |
| `blade_change_production_line_old` | varchar(100) | Y | - | 换刀片产线_as_old | ✅ |  |
| `blade_change_machine_old` | varchar(50) | Y | - | 换刀片机床_as_old | ✅ |  |
| `blade_changer_old` | varchar(20) | Y | - | 换刀片换刀人_as_old | ✅ |  |
| `blade_change_factory_old` | varchar(20) | Y | - | 换刀片工厂_as_old | ✅ |  |
| `blade_change_time_new` | datetime(6) | Y | - | 换刀片时间_as_new | ✅ |  |
| `new_blade_barcode_after_change` | varchar(255) | Y | - | 换刀片新刀条码 | ✅ |  |
| `blade_model_new` | varchar(80) | Y | - | 换刀片型号_as_new | ✅ |  |
| `removed_old_blade_barcode` | varchar(255) | Y | - | 此时取下来旧刀片的条码 | ✅ |  |
| `blade_change_production_line_new` | varchar(100) | Y | - | 换刀片产线_as_new | ✅ |  |
| `blade_change_machine_new` | varchar(50) | Y | - | 换刀片机床_as_new | ✅ |  |
| `blade_changer_new` | varchar(20) | Y | - | 换刀片换刀人_as_new | ✅ |  |
| `blade_change_factory_new` | varchar(20) | Y | - | 换刀片工厂_as_new | ✅ |  |
| `return_time` | datetime(6) | Y | - | 返库时间 | ✅ |  |
| `return_barcode` | varchar(255) | Y | - | 返库条码 | ✅ |  |
| `return_model` | varchar(80) | Y | - | 返库型号 | ✅ |  |
| `return_factory` | varchar(20) | Y | - | 返库工厂 | ✅ |  |
| `production_department_knife_receiving_time` | datetime(6) | Y | - | 生产部领刀时间 | ✅ |  |
| `production_department_knife_barcode` | varchar(255) | Y | - | 生产部领刀条码 | ✅ |  |
| `production_department_knife_model` | varchar(80) | Y | - | 生产部领刀型号 | ✅ |  |
| `production_department_knife_receiving_layer` | int | Y | - | 生产部领刀层数 | ✅ |  |
| `production_department_knife_receiver` | varchar(20) | Y | - | 生产部领刀人 | ✅ |  |
| `production_department_knife_receiving_factory` | varchar(20) | Y | - | 生产部领刀工厂 | ✅ |  |
| `engineering_department_knife_receiving_time` | datetime(6) | Y | - | 工程部领刀时间 | ✅ |  |
| `engineering_department_knife_barcode` | varchar(255) | Y | - | 工程部领刀条码 | ✅ |  |
| `engineering_department_knife_model` | varchar(80) | Y | - | 工程部领刀型号 | ✅ |  |
| `engineering_department_knife_receiver` | varchar(20) | Y | - | 工程部领刀人 | ✅ |  |
| `engineering_department_knife_receiving_factory` | varchar(20) | Y | - | 工程部领刀工厂 | ✅ |  |
| `input_time_old` | datetime(6) | Y | - | 录入时间_as_old | ✅ |  |
| `installed_new_knife_barcode` | varchar(255) | Y | - | 此时放上去新刀的条码 | ✅ |  |
| `update_time_old` | datetime(6) | Y | - | 更新时间_as_old | ✅ |  |
| `shift_old` | varchar(20) | Y | - | 班次_as_old | ✅ |  |
| `knife_change_reason_old` | varchar(255) | Y | - | 更换原因_as_old | ✅ |  |
| `knife_model_old` | varchar(80) | Y | - | 刀具型号_as_old | ✅ |  |
| `old_knife_barcode_after_change` | varchar(255) | Y | - | 换刀旧刀条码 | ✅ |  |
| `knife_change_production_line_old` | varchar(100) | Y | - | 换刀产线_as_old | ✅ |  |
| `machine_knife_changer_old` | varchar(20) | Y | - | 机床换刀人_as_old | ✅ |  |
| `knife_change_factory_old` | varchar(20) | Y | - | 换刀工厂_as_old | ✅ |  |
| `input_time_new` | datetime(6) | Y | - | 录入时间_as_new | ✅ |  |
| `new_knife_barcode_after_change` | varchar(255) | Y | - | 换刀新刀条码 | ✅ |  |
| `update_time_new` | datetime(6) | Y | - | 更新时间_as_new | ✅ |  |
| `shift_new` | varchar(20) | Y | - | 班次_as_new | ✅ |  |
| `knife_change_reason_new` | varchar(255) | Y | - | 更换原因_as_new | ✅ |  |
| `knife_model_new` | varchar(80) | Y | - | 刀具型号_as_new | ✅ |  |
| `removed_old_knife_barcode` | varchar(255) | Y | - | 此时取下来旧刀的条码 | ✅ |  |
| `knife_change_production_line_new` | varchar(100) | Y | - | 换刀产线_as_new | ✅ |  |
| `machine_knife_changer_new` | varchar(20) | Y | - | 机床换刀人_as_new | ✅ |  |
| `knife_change_factory_new` | varchar(20) | Y | - | 换刀工厂_as_new | ✅ |  |
| `tool_cabinet_old_knife_recycling_time` | datetime(6) | Y | - | 刀具柜旧刀回收时间 | ✅ |  |
| `tool_cabinet_old_knife_recycling_barcode` | varchar(255) | Y | - | 刀具柜旧刀回收条码 | ✅ |  |
| `tool_cabinet_old_knife_recycling_model` | varchar(80) | Y | - | 刀具柜旧刀回收型号 | ✅ |  |
| `tool_cabinet_old_knife_recycling_layer` | int | Y | - | 刀具柜旧刀回收层数 | ✅ |  |
| `tool_cabinet_old_knife_recycling_admin` | varchar(20) | Y | - | 刀具柜旧刀回收管理员 | ✅ |  |
| `tool_cabinet_old_knife_recycling_factory` | varchar(20) | Y | - | 刀具柜旧刀回收工厂 | ✅ |  |
| `tool_cabinet_knife_storage_time` | datetime(6) | Y | - | 刀具柜放刀时间 | ✅ |  |
| `tool_cabinet_knife_storage_barcode` | varchar(255) | Y | - | 刀具柜放刀条码 | ✅ |  |
| `tool_cabinet_knife_storage_model` | varchar(80) | Y | - | 刀具柜放刀型号 | ✅ |  |
| `tool_cabinet_knife_storage_layer` | int | Y | - | 刀具柜放刀层数 | ✅ |  |
| `tool_cabinet_knife_receiver` | varchar(20) | Y | - | 刀具柜领刀人 | ✅ |  |
| `tool_cabinet_knife_storage_factory` | varchar(20) | Y | - | 刀具柜放刀工厂 | ✅ |  |
| `material_issue_date` | datetime(6) | Y | - | 发料日期 | ✅ |  |
| `project` | varchar(20) | Y | - | 项目 | ✅ |  |
| `sub_category` | varchar(20) | Y | - | 次类别 | ✅ |  |
| `barcode` | varchar(20) | Y | - | 条形码 | ✅ |  |
| `has_material_record` | varchar(255) | Y | - | 是否有领料记录 | ✅ |  |
| `cabinet_number` | varchar(10) | Y | - | 柜号 | ✅ |  |
| `supplier` | varchar(50) | Y | - | 供应商 | ✅ |  |
| `material_name` | varchar(80) | Y | - | 领料产品名称 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `quantity` | int | Y | - | 数量 | ✅ |  |
| `unit_price` | decimal(10,3) | Y | - | 单价 | ✅ |  |
| `amount` | decimal(10,3) | Y | - | 金额 | ✅ |  |
| `material_receiver` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `department` | varchar(20) | Y | - | 部门 | ✅ |  |
| `use_department` | varchar(20) | Y | - | 使用部门 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `barcode_extraction` | varchar(20) | Y | - | 提取条码 | ✅ |  |
| `supplier_extraction` | varchar(50) | Y | - | 提取供应商 | ✅ |  |
| `merge_barcodes` | varchar(50) | Y | - | 合并条码（界面:合并产条码） | ✅🖥️ |  |
| `merge_time` | varchar(50) | Y | - | 合并时间 | ✅ |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | 🔍待补充 | 🔍 |  |

### generator_machine_tool_change
**定义**：机床换刀表 ｜ **代码**：`generator/machine_tool_change/model.py` ｜ **行数(估)**：26984

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:录入时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `cabinet_id` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `tool_changer` | varchar(255) | Y | - | 换刀人 | ✅ |  |
| `tool_order` | varchar(255) | Y | - | 刀序 | ✅ |  |
| `machine_tool` | varchar(255) | Y | - | 机床 | ✅ |  |
| `production_line_id` | varchar(255) | Y | - | 产线 | ✅ | →generator_production_line(推断) |
| `old_tool_supplier` | varchar(255) | Y | - | 旧刀供应商 | ✅ |  |
| `old_bar_code` | varchar(255) | Y | - | 旧刀条码 | ✅ |  |
| `model` | varchar(255) | Y | - | 刀具型号 | ✅ |  |
| `new_tool_supplier` | varchar(255) | Y | - | 新刀供应商 | ✅ |  |
| `change_reason` | varchar(255) | Y | - | 更换原因 | ✅ |  |
| `working_shift` | varchar(255) | Y | - | 班次 | ✅ |  |
| `update_time` | datetime | Y | - | 更新时间 | ✅ |  |
| `status` | varchar(255) | Y | - | 状态 | ✅ |  |
| `inspector` | varchar(255) | Y | - | 检验员 | ✅ |  |
| `tool_change_qrcode` | varchar(255) | Y | - | 换刀首件二维码 | ✅ |  |
| `processing_quantity_machine` | varchar(255) | Y | - | 加工数量-机 | ✅ |  |
| `processing_data_worker` | varchar(255) | Y | - | 加工数据-人 | ✅ |  |
| `bar_code` | varchar(255) | Y | - | 新刀条码 | ✅ |  |
| `date_time` | datetime | Y | - | 录入时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | _MASK_TO_V2 | ✅ |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | 🔍待补充 | 🔍 |  |

### generator_old_knife_recycle
**定义**：刀具柜旧刀回收 ｜ **代码**：`generator/old_knife_recycle/model.py` ｜ **行数(估)**：9362

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
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `admin` | varchar(255) | Y | - | 管理员 | ✅ |  |
| `layer_number` | varchar(255) | Y | - | 层数 | ✅ |  |
| `cabinet_number` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `barcode` | varchar(255) | Y | - | 条码 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |

### knife_jobcode
**定义**：刀具-工作代号转换表 ｜ **代码**：`translation/models.py` ｜ **行数(估)**：389

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `line_name` | varchar(255) | Y | - | 产线（界面:产线/工序） | ✅🖥️ |  |
| `name` | varchar(255) | Y | - | 全称（界面:原辅料名称） | ✅🖥️ |  |
| `internal_code` | varchar(255) | Y | - | 厂内编号 | ✅ |  |
| `is_auto` | int | N | - | 匹配方式；0 手动匹配 1程序匹配 2废弃匹配 | ✅💬 |  |
| `job_code_id` | bigint | N | MUL | →generator_job_code | 🔗 | →generator_job_code |
| `eng_name` | varchar(255) | Y | - | 英文标签 | ✅ |  |
