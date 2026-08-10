---
title: TF铸造模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 02-生产铸造域
tags: [工程, 数据字典2, 代码实证, TF铸造]
---

# TF铸造模块 · fuadmin 数据字典2（代码实证版）
> 域: 02-生产铸造域 | 表数: 31 | 字段: 433 | 代码锚定: 408(94%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/02-生产铸造域/TF铸造模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_ingredients` | 原辅料管理 | 660 | 💻 |
| `generator_ingredients_split` | 辅料分装管理 | 1849 | 💻 |
| `generator_tf_add_golduse` | 合金添加剂 | 16127 | 💻 |
| `generator_tf_add_golduse_production_plan` | M2M中间表: generator_tf_add_golduse↔Productio | 16010 | 🔗 |
| `generator_tf_cast_inspection` | 铸件检测记录 | 8052 | 💻 |
| `generator_tf_cast_inspection_production_plan` | M2M中间表: generator_tf_cast_inspection↔Produ | 8005 | 🔗 |
| `generator_tf_coremaking` | 制芯管理 | 1347 | 💻 |
| `generator_tf_coremaking_batch_relation` | 制芯管理-批次号关联 | 1307 | 💻 |
| `generator_tf_furnace_power_display` | 炉台功率展示 | 864008 | 💻 |
| `generator_tf_furnace_situation` | 炉台情况 | 1152 | 💻 |
| `generator_tf_furnace_smelt` | 炉前熔炼 | 15951 | 💻 |
| `generator_tf_furnace_smelt_production_plan` | M2M中间表: generator_tf_furnace_smelt↔Product | 16367 | 🔗 |
| `generator_tf_mould` | 模具 | 39 | 💻 |
| `generator_tf_mould_daily` | 造型信息 | 8712 | 💻 |
| `generator_tf_mould_operate` | 模具操作 | 3596 | 💻 |
| `generator_tf_mould_scanreport` | 模具扫描报告 | 67 | 💻 |
| `generator_tf_pouring_records` | 浇注记录 | 15771 | 💻 |
| `generator_tf_pouring_records_production_plan` | M2M中间表: generator_tf_pouring_records↔Produ | 16010 | 🔗 |
| `generator_tf_product` | 产品信息 | 21 | 💻 |
| `generator_tf_production_plan` | 泰峰生产计划 | 8089 | 💻 |
| `generator_tf_rapid_goldtest` | 快速金相检测 | 7807 | 💻 |
| `generator_tf_rapid_goldtest_production_plan` | M2M中间表: generator_tf_rapid_goldtest↔Produc | 8005 | 🔗 |
| `generator_tf_stove_extract` | 炉前出汤 | 16045 | 💻 |
| `generator_tf_stove_extract_production_plan` | M2M中间表: generator_tf_stove_extract↔Product | 16010 | 🔗 |
| `generator_tf_stove_spectrum` | 合金调整 | 7755 | 💻 |
| `generator_tf_stove_spectrum_production_plan` | M2M中间表: generator_tf_stove_spectrum↔Produc | 8005 | 🔗 |
| `generator_tf_tensile_strength` | 拉伸强度 | 7919 | 💻 |
| `generator_tf_tensile_strength_production_plan` | M2M中间表: generator_tf_tensile_strength↔Prod | 8005 | 🔗 |
| `generator_tf_tilt_information` | 倾角采集信息 | 6147 | 💻 |
| `generator_tf_transfer_cart` | 转运小车 | 13062 | 💻 |
| `generator_tfdl` | 泰峰电炉 | 9 | 💻 |

---

### generator_ingredients
**定义**：原辅料管理 ｜ **代码**：`generator/ingredients/model.py` ｜ **行数(估)**：660

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | int | Y | - | 状态：0注销 1使用 2待入库 3退货 | 💬⚖️ |  |
| `unit` | varchar(20) | Y | - | 单位 | ✅ |  |
| `number` | decimal(10,2) | Y | - | 数量 | ✅ |  |
| `manufacturer` | varchar(30) | Y | - | 供应商名称 | ✅ |  |
| `stock_time` | datetime(6) | Y | - | 入库时间 | ✅ |  |
| `apply_time` | datetime(6) | Y | - | 申请时间 | ✅ |  |
| `i_class` | varchar(20) | Y | - | 类别 | ✅ |  |
| `name` | varchar(30) | Y | - | 辅料名称 | ✅ |  |
| `ingredients_number` | varchar(50) | Y | - | 辅料单号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `use_dept` | varchar(30) | Y | - | 使用范围 | ✅ |  |
| `code` | varchar(30) | Y | - | 编号 | ✅ |  |
| `stock_code` | varchar(40) | Y | - | 入库单号 | ✅ |  |
| `alarm` | json | Y | - | 多拿报警；每次多拿时的部门报警 [{"disabled": false, "interval": 3, "send_info": "", "send_history": "", "interval_unit": "天", "interval_user": "22184 杨小青"}, {"disabled": false, "interval": 1, "send_info": "", "send_history": "", "interval_unit": "天", "interval_user": "10000 郑希钦(集团-总裁)"}] | ✅💬 |  |
| `alarm_btn` | tinyint(1) | Y | - | 报警：是否开启报警 | ✅⚖️ |  |
| `percentage` | decimal(5,2) | Y | - | 余量百分比 | ✅ |  |
| `warning` | json | Y | - | 库存预警；库存在warning的区间值时的报警内容 [{"warning": [0, 60], "disabled": false, "send_info": "赶紧补货", "send_history": "时间:2024-11-05 15:16:34 余量:60.00% 操作人:superadmin 超级管理员\n", "warning_user": "22281 苏杨"}, {"warning": [0, 20], "disabled": false, "send_info": "", "send_history": "", "warning_user": "21725 谢宇航"}] | ✅💬 |  |
| `warning_btn` | tinyint(1) | Y | - | 预警：是否开启预警 | ✅⚖️ |  |
| `PO` | varchar(30) | Y | - | PO | ✅ |  |
| `unit_price` | decimal(11,4) | Y | - | 单价 | ✅ |  |
| `grouping` | tinyint(1) | Y | - | 类目录：是否为类目录（分类节点） | ✅⚖️ |  |
| `parent_id` | bigint | Y | MUL | 上级代码；→generator_ingredients | ✅🔗 | →generator_ingredients |
| `site` | varchar(20) | Y | - | 站点：治通/广汇/泰峰/娄塘 | 💬⚖️ |  |

### generator_ingredients_split
**定义**：辅料分装管理 ｜ **代码**：`generator/ingredients_split/model.py` ｜ **行数(估)**：1849

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock` | json | Y | - | 领用；当entirety为1时才有数据 [{"key": "1", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-02T10:06:17.492Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-05T10:06:17.492Z", "create_user": "T10903 朱钱海", "stock_number": 12.9}, {"key": "2", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-04T10:06:43.741Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-05T10:06:43.741Z", "create_user": "T10903 朱钱海", "stock_number": 40.8}, {"key": "3", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-06T06:57:22.112Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-07T06:57:22.112Z", "create_user": "T10903 朱钱海", "stock_number": 37.5}, {"key": "4", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-07T09:10:44.863Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-08T09:10:44.863Z", "create_user": "T10903 朱钱海", "stock_number": 39.5}, {"key": "5", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-08T07:12:31.789Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-10T07:12:31.789Z", "create_user": "T10903 朱钱海", "stock_number": 38.9}, {"key": "6", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-09T07:12:52.785Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-10T07:12:52.785Z", "create_user": "T10903 朱钱海", "stock_number": 30.5}, {"key": "7", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-11T07:31:37.071Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-12T07:31:37.071Z", "create_user": "T10903 朱钱海", "stock_number": 36.6}, {"key": "8", "disabled": true, "send_time": "", "stock_dept": "江苏泰峰-物流部", "stock_time": "2025-08-10T07:32:02.209Z", "stock_user": "T10903 朱钱海(江苏泰峰-物流部)", "create_time": "2025-08-12T07:32:02.209Z", "create_user": "T10903 朱钱海", "stock_number": 43.9}] | ✅💬 |  |
| `entirety` | int | Y | - | 整体状态；0:单体(state为1时 只会出现1,2,4) 1:整体(state有可能会出现1,2,3和4的情况, 3表示部分领用, 4表示已领用) | ✅💬 |  |
| `in_warehouse_user` | varchar(20) | Y | - | 入库人 | ✅ |  |
| `in_warehouse_time` | datetime(6) | Y | - | 入库时间 | ✅ |  |
| `state` | int | Y | - | 状态：1待入库 2已入库 3部分领用 4已领用 | 💬⚖️ |  |
| `unit` | varchar(20) | Y | - | 单位 | ✅ |  |
| `number` | decimal(10,2) | Y | - | 数量 | ✅ |  |
| `i_class` | varchar(50) | Y | - | 编号 | ✅ |  |
| `name` | varchar(30) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `ingredients_id` | bigint | Y | MUL | 辅料分装；→generator_ingredients | ✅🔗 | →generator_ingredients |
| `stock_dept` | varchar(20) | Y | - | 领用部门：entirety=0时有值，领用人所属部门 | ✅⚖️ |  |
| `stock_time` | datetime(6) | Y | - | 领用时间；当entirety为0时才有数据 2025-08-05T10:06:17.492Z 该字段是领用时间 | ✅💬 |  |
| `stock_user` | varchar(20) | Y | - | 领用人：entirety=0时有值，格式'工号 姓名' | ✅⚖️ |  |
| `index` | varchar(30) | Y | - | 序号 | ✅ |  |
| `bar_code` | varchar(50) | Y | - | 条形码 | ✅ |  |
| `send_time` | datetime(6) | Y | - | 发送信息 | ✅ |  |

### generator_tf_add_golduse
**定义**：合金添加剂 ｜ **代码**：`generator/tf_add_golduse/model.py` ｜ **行数(估)**：16127

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `cover` | int | Y | - | 覆盖片 | ✅ |  |
| `pregnanter` | decimal(5,2) | Y | - | 孕育剂 | ✅ |  |
| `baller` | decimal(5,2) | Y | - | 球化剂 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 添加时间 | ✅ |  |
| `number` | int | Y | - | 包次 | ✅ |  |
| `furnace_number` | int | Y | - | 炉次号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date_only` | date | Y | MUL | 添加日期 | ✅ |  |

### generator_tf_add_golduse_production_plan
**定义**：M2M中间表: generator_tf_add_golduse↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：16010

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tfaddgolduse_id` | bigint | N | MUL | [推断]FK→generator_tf_add_golduse（合金添加剂） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_cast_inspection
**定义**：铸件检测记录 ｜ **代码**：`generator/tf_cast_inspection/model.py` ｜ **行数(估)**：8052

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `inspectors` | varchar(30) | Y | - | 检验者 | ✅ |  |
| `carbide` | decimal(5,2) | Y | - | 碳化物 | ✅ |  |
| `pearlite` | decimal(5,2) | Y | - | 珠光体 | ✅ |  |
| `ball_rate` | decimal(5,2) | Y | - | 球化率 | ✅ |  |
| `type` | varchar(30) | Y | - | 型态 | ✅ |  |
| `measured_hardness` | int | Y | - | 实测硬度 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `furnace_number` | int | Y | - | 炉次号 | ✅ |  |
| `date_only` | date | Y | MUL | 归属时间 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 检测时间 | ✅ |  |

### generator_tf_cast_inspection_production_plan
**定义**：M2M中间表: generator_tf_cast_inspection↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：8005

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tfcastinspection_id` | bigint | N | MUL | [推断]FK→generator_tf_cast_inspection（铸件检测记录） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_coremaking
**定义**：制芯管理 ｜ **代码**：`generator/tf_coremaking/model.py` ｜ **行数(估)**：1347

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `use_log` | json | Y | - | 使用记录 | ✅ |  |
| `bake_log` | json | Y | - | 烘烤记录 | ✅ |  |
| `remaining_qty` | int | Y | - | 剩余数量 | ✅ |  |
| `checkout_time` | datetime(6) | Y | - | 检验时间 | ✅ |  |
| `chromatism` | int | Y | - | 色差；枚举[1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8] | ✅🔢 |  |
| `bad_seam` | varchar(20) | Y | - | 坯缝 | ✅ |  |
| `checkout_u` | varchar(30) | Y | - | 检验人员 | ✅ |  |
| `temper` | int | Y | - | 加热温度 | ✅ |  |
| `handlers` | varchar(30) | Y | - | 生产者 | ✅ |  |
| `number` | int | Y | - | 生产数量 | ✅ |  |
| `crusting` | int | Y | - | 固化时间 | ✅ |  |
| `incrustation` | int | Y | - | 结壳时间 | ✅ |  |
| `date_time` | date | Y | - | 生产日期 | ✅ |  |
| `sand_count_id` | bigint | Y | MUL | 砂批次；→generator_ingredients | ✅🔗 | →generator_ingredients |
| `device_code` | varchar(50) | Y | - | 设备编号 | ✅ |  |
| `tf_product_name` | varchar(30) | Y | - | 产品名称 | ✅ |  |
| `core_number` | varchar(50) | Y | - | 制芯单号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `production_date` | varchar(60) | Y | - | 制造时间 | ✅ |  |
| `mould_id` | bigint | Y | MUL | 模具关联；→generator_tf_mould | ✅🔗 | →generator_tf_mould |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断]掩码同步标记列(V2来源侧)，无代码锚点，非业务字段 | 🔍 |  |
| `exception_declaration` | varchar(255) | Y | - | 异常说明 | ✅ |  |
| `picture` | json | Y | - | 相关图片 | ✅ |  |

### generator_tf_coremaking_batch_relation
**定义**：制芯管理-批次号关联 ｜ **代码**：`generator/tf_coremaking/model.py` ｜ **行数(估)**：1307

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断]主键（自增ID） | 🔍 |  |
| `batch_number` | varchar(120) | N | UNI | 批次号；与主页关联的批次号（提取自use_log） | ✅ |  |
| `coremaking_id` | bigint | N | MUL | 关联制芯管理记录：FK→制芯管理主表，取制芯单号/生产日期 | ✅⚖️ | →generator_tf_coremaking |
| `create_datetime` | datetime | N | - | [推断]创建时间（关联记录写入时间） | 🔍 |  |

### generator_tf_furnace_power_display
**定义**：炉台功率展示 ｜ **代码**：`generator/tf_furnace_power_display/model.py` ｜ **行数(估)**：864008

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `Instantaneous_power_of_furnace_D` | varchar(255) | Y | - | D炉瞬时功率 | ✅ |  |
| `Instantaneous_power_of_furnace_C` | varchar(255) | Y | - | C炉瞬时功率 | ✅ |  |
| `Instantaneous_power_of_furnace_B` | varchar(255) | Y | - | B炉瞬时功率 | ✅ |  |
| `Instantaneous_power_of_furnace_A` | varchar(255) | Y | - | A炉瞬时功率 | ✅ |  |
| `total_instantaneous_power` | varchar(255) | Y | - | 总瞬时功率 | ✅ |  |
| `date` | datetime(6) | Y | - | 日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]掩码同步标记列(V2去向侧)，无代码锚点，非业务字段 | 🔍 |  |
| `total_power` | varchar(255) | Y | - | 总电量 | ✅ |  |

### generator_tf_furnace_situation
**定义**：炉台情况 ｜ **代码**：`generator/tf_furnace_situation/model.py` ｜ **行数(估)**：1152

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `abnormal_production_situation` | varchar(255) | Y | - | 生产异常情况 | ✅ |  |
| `furnace_information` | varchar(255) | Y | - | 筑炉情况 | ✅ |  |
| `date` | date | Y | - | 日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `furnace_number` | varchar(10) | Y | - | 炉号 | ✅ |  |
| `wall_thickness` | double | Y | - | 内径 | ✅ |  |
| `depth` | double | Y | - | 深度 | ✅ |  |

### generator_tf_furnace_smelt
**定义**：炉前熔炼 ｜ **代码**：`generator/tf_furnace_smelt/model.py` ｜ **行数(估)**：15951

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `carbon_Si` | decimal(6,3) | Y | - | Si%(碳硫仪) | ✅ |  |
| `carbon_C` | decimal(6,3) | Y | - | C%(碳硫仪) | ✅ |  |
| `spectrum_Sn` | decimal(6,3) | Y | - | Sn%(光谱) | ✅ |  |
| `spectrum_Mg` | decimal(6,3) | Y | - | Mg%(光谱) | ✅ |  |
| `spectrum_Cu` | decimal(6,3) | Y | - | Cu%(光谱) | ✅ |  |
| `spectrum_Mn` | decimal(6,3) | Y | - | Mn%(光谱) | ✅ |  |
| `spectrum_Si` | decimal(6,3) | Y | - | Si%(光谱) | ✅ |  |
| `spectrum_C` | decimal(6,3) | Y | - | C%(光谱) | ✅ |  |
| `date_time` | datetime(6) | Y | - | 出炉时间 | ✅ |  |
| `state` | int | Y | - | 状态；枚举[1=炉前,2=炉后] | ✅🔢 |  |
| `furnace_number` | int | Y | - | 炉次号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date_only` | date | Y | MUL | 添加日期 | ✅ |  |
| `spectrum_Cr` | decimal(6,3) | Y | - | Cr%(光谱) | ✅ |  |
| `spectrum_P` | decimal(6,3) | Y | - | P%(光谱) | ✅ |  |
| `spectrum_S` | decimal(6,3) | Y | - | S%(光谱) | ✅ |  |

### generator_tf_furnace_smelt_production_plan
**定义**：M2M中间表: generator_tf_furnace_smelt↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：16367

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tffurnacesmelt_id` | bigint | N | MUL | [推断]FK→generator_tf_furnace_smelt（炉前熔炼） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_mould
**定义**：模具 ｜ **代码**：`generator/tf_mould/model.py` ｜ **行数(估)**：39

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `sum_count` | int | Y | - | 总次数 | ✅ |  |
| `entry_time` | date | Y | - | 入厂时间 | ✅ |  |
| `manufacturers` | varchar(255) | Y | - | 生产厂家 | ✅ |  |
| `code` | varchar(255) | Y | - | 模具编号 | ✅ |  |
| `type` | varchar(255) | Y | - | 类型 | ✅ |  |
| `product_name` | varchar(255) | Y | - | 产品名称 | ✅ |  |
| `mould_number` | varchar(255) | Y | - | 模具单号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_tf_mould_daily
**定义**：造型信息 ｜ **代码**：`generator/tf_mould_daily/model.py` ｜ **行数(估)**：8712

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `mould_confirmation` | int | Y | - | 模具确认 | ✅ |  |
| `stop_statistics` | longtext | Y | - | 停机统计 | ✅ |  |
| `updown_model` | int | Y | - | 项目基准 | ✅ |  |
| `mould_number` | int | Y | - | 造型数 | ✅ |  |
| `batch_number` | varchar(30) | Y | - | 批次号 | ✅ |  |
| `tf_product_type` | varchar(30) | Y | - | 材质 | ✅ |  |
| `time` | int | Y | - | 停机时间 | ✅ |  |
| `tf_product_name` | varchar(30) | Y | - | 产品名称 | ✅ |  |
| `serial_number` | int | Y | - | 序号 | ✅ |  |
| `mould_worker` | varchar(50) | Y | - | 造型作业者 | ✅ |  |
| `work_date` | datetime(6) | Y | - | 作业日期 | ✅ |  |
| `classes` | varchar(30) | Y | - | 班次 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `mold_release` | decimal(8,2) | Y | - | 脱模剂 | ✅ |  |
| `strainer` | decimal(8,2) | Y | - | 过滤网数量 | ✅ |  |
| `hardness_down` | int | Y | - | 砂型硬度(下) | ✅ |  |
| `hardness_up` | int | Y | - | 砂型硬度(上) | ✅ |  |
| `height_down` | int | Y | - | 砂型高度(下) | ✅ |  |
| `height_up` | int | Y | - | 砂型高度(上) | ✅ |  |
| `press_down` | decimal(4,2) | Y | - | 射砂压力(下) | ✅ |  |
| `press_up` | decimal(4,2) | Y | - | 射砂压力(上) | ✅ |  |
| `strainer_filter` | varchar(50) | Y | - | 过滤网规格 | ✅ |  |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]掩码同步标记列(V2去向侧)，无代码锚点，非业务字段 | 🔍 |  |

### generator_tf_mould_operate
**定义**：模具操作 ｜ **代码**：`generator/tf_mould_operate/model.py` ｜ **行数(估)**：3596

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `number` | varchar(255) | Y | - | 数量 | ✅ |  |
| `date_time` | varchar(255) | Y | - | 操作时间 | ✅ |  |
| `type` | varchar(255) | Y | - | 模具操作 | ✅ |  |
| `mould_id` | bigint | Y | MUL | 模具信息；→generator_tf_mould | ✅🔗 | →generator_tf_mould |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `img` | varchar(255) | Y | - | 图片 | ✅ |  |

### generator_tf_mould_scanreport
**定义**：模具扫描报告 ｜ **代码**：`generator/tf_mould_scanreport/model.py` ｜ **行数(估)**：67

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `scan_report` | varchar(255) | Y | - | 扫描报告 | ✅ |  |
| `scan_date` | date | Y | - | 扫描日期 | ✅ |  |
| `code_id` | bigint | Y | MUL | 模具；→generator_tf_mould | ✅🔗 | →generator_tf_mould |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `sum_count` | int | Y | - | 总次数 | ✅ |  |

### generator_tf_pouring_records
**定义**：浇注记录 ｜ **代码**：`generator/tf_pouring_records/model.py` ｜ **行数(估)**：15771

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `bad_number` | int | Y | - | 不良箱数 | ✅ |  |
| `last_temper` | int | Y | - | 末箱温度 | ✅ |  |
| `first_temper` | int | Y | - | 首箱温度 | ✅ |  |
| `pouring_temper` | int | Y | - | 浇注包温度 | ✅ |  |
| `pouring_number` | int | Y | - | 浇注箱数 | ✅ |  |
| `number` | int | Y | - | 包次 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 浇注时间 | ✅ |  |
| `furnace_number` | int | Y | - | 炉次号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date_only` | date | Y | MUL | 添加日期 | ✅ |  |

### generator_tf_pouring_records_production_plan
**定义**：M2M中间表: generator_tf_pouring_records↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：16010

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tfpouringrecords_id` | bigint | N | MUL | [推断]FK→generator_tf_pouring_records（浇注记录） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_product
**定义**：产品信息 ｜ **代码**：`generator/tf_product/model.py` ｜ **行数(估)**：21

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | int | Y | - | 状态 | ✅ |  |
| `weight` | decimal(10,2) | Y | - | 重量 | ✅ |  |
| `code` | varchar(30) | Y | - | 产品编号 | ✅ |  |
| `type` | varchar(30) | Y | - | 材质 | ✅ |  |
| `name` | varchar(30) | Y | - | 产品名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `number` | int | Y | - | 计划箱数 | ✅ |  |
| `rigidity_range` | varchar(40) | Y | - | 硬度要求 | ✅ |  |

### generator_tf_production_plan
**定义**：泰峰生产计划 ｜ **代码**：`generator/tf_production_plan/model.py` ｜ **行数(估)**：8089

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `planned_production` | int | Y | - | 计划生产数(箱) | ✅ |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `batch_number` | varchar(30) | Y | - | 批次号 | ✅ |  |
| `serial_number` | int | Y | - | 序号 | ✅ |  |
| `date` | date | Y | - | 生产日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `production_number` | varchar(255) | Y | - | [推断]生产数量（历史遗留列，现模型用planned/actual_production） | 🔍 |  |
| `actual_production` | int | Y | - | 实际生产数(箱) | ✅ |  |
| `batch_status` | int | Y | - | 批次号状态；枚举[0=NO,1=OK] | ✅🔢 |  |
| `error` | int | Y | - | 异常箱数 | ✅ |  |
| `explain` | varchar(255) | Y | - | 异常状况说明 | ✅ |  |
| `first_temper` | int | Y | - | 浇注首温 | ✅ |  |
| `last_temper` | int | Y | - | 浇注末温 | ✅ |  |
| `mode_clean` | int | Y | - | 模具清理；枚举[0=×,1=√] | ✅🔢 |  |
| `quality_signature` | varchar(30) | Y | - | 质检签字 | ✅ |  |
| `responser` | varchar(30) | Y | - | 责任人签字 | ✅ |  |
| `tf_product_name` | varchar(30) | Y | - | 产品名称 | ✅ |  |
| `tf_product_type` | varchar(30) | Y | - | 材质 | ✅ |  |
| `heat_number` | varchar(50) | Y | - | 炉号 | ✅ |  |
| `filter_size` | varchar(20) | Y | - | 过滤网规格 | ✅ |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断]掩码同步标记列(V2来源侧)，无代码锚点，非业务字段 | 🔍 |  |

### generator_tf_rapid_goldtest
**定义**：快速金相检测 ｜ **代码**：`generator/tf_rapid_goldtest/model.py` ｜ **行数(估)**：7807

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `two_ball` | decimal(4,3) | Y | - | 第二包球化率 | ✅ |  |
| `one_ball` | decimal(4,3) | Y | - | 第一包球化率 | ✅ |  |
| `size` | varchar(30) | Y | - | 标准 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 检测时间 | ✅ |  |
| `furnace_number` | int | Y | - | 炉次号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date_only` | date | Y | MUL | 添加日期 | ✅ |  |

### generator_tf_rapid_goldtest_production_plan
**定义**：M2M中间表: generator_tf_rapid_goldtest↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：8005

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tfrapidgoldtest_id` | bigint | N | MUL | [推断]FK→generator_tf_rapid_goldtest（快速金相检测） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_stove_extract
**定义**：炉前出汤 ｜ **代码**：`generator/tf_stove_extract/model.py` ｜ **行数(估)**：16045

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `pour_time` | datetime(6) | Y | - | 浇注时间 | ✅ |  |
| `ball_time` | int | Y | - | 球化时间(s) | ✅ |  |
| `sum` | int | Y | - | 出汤量 | ✅ |  |
| `temper` | int | Y | - | 出汤温度 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 出汤时间 | ✅ |  |
| `number` | int | Y | - | 包次 | ✅ |  |
| `furnace_number` | int | Y | - | 炉次号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date_only` | date | Y | MUL | 添加日期 | ✅ |  |

### generator_tf_stove_extract_production_plan
**定义**：M2M中间表: generator_tf_stove_extract↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：16010

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tfstoveextract_id` | bigint | N | MUL | [推断]FK→generator_tf_stove_extract（炉前出汤） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_stove_spectrum
**定义**：合金调整 ｜ **代码**：`generator/tf_stove_spectrum/model.py` ｜ **行数(估)**：7755

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `sn` | decimal(8,3) | Y | - | 锡 | ✅ |  |
| `cu` | decimal(8,3) | Y | - | 铜 | ✅ |  |
| `sic` | decimal(8,3) | Y | - | 碳化硅 | ✅ |  |
| `mn_iron` | decimal(8,3) | Y | - | 锰铁 | ✅ |  |
| `si_iron` | decimal(8,3) | Y | - | 硅铁 | ✅ |  |
| `carburizers` | decimal(8,3) | Y | - | 增碳剂 | ✅ |  |
| `scrap` | decimal(8,3) | Y | - | 废钢(降碳) | ✅ |  |
| `pig_iron` | decimal(8,3) | Y | - | 生铁 | ✅ |  |
| `return_material` | decimal(8,3) | Y | - | 回炉料 | ✅ |  |
| `iron` | varchar(30) | Y | - | 铁屑 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 调整时间 | ✅ |  |
| `furnace_number` | int | Y | - | 炉次号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date_only` | date | Y | MUL | 添加日期 | ✅ |  |
| `ferrochrome` | decimal(8,3) | Y | - | 铬铁 | ✅ |  |
| `iron_sulfide` | decimal(8,3) | Y | - | 硫化铁 | ✅ |  |

### generator_tf_stove_spectrum_production_plan
**定义**：M2M中间表: generator_tf_stove_spectrum↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：8005

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tfstovespectrum_id` | bigint | N | MUL | [推断]FK→generator_tf_stove_spectrum（合金调整） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_tensile_strength
**定义**：拉伸强度 ｜ **代码**：`generator/tf_tensile_strength/model.py` ｜ **行数(估)**：7919

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `inspetion_person` | varchar(255) | Y | - | 检测人 | ✅ |  |
| `elongation` | decimal(13,4) | Y | - | 伸长率 | ✅ |  |
| `most_strength` | int | Y | - | 非比例延伸强度 | ✅ |  |
| `resist_strength` | int | Y | - | 抗拉强度(Mpa) | ✅ |  |
| `furnace_number` | decimal(13,4) | Y | - | 炉次号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date_only` | date | Y | MUL | 归属时间 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 检测时间 | ✅ |  |

### generator_tf_tensile_strength_production_plan
**定义**：M2M中间表: generator_tf_tensile_strength↔ProductionPlan ｜ **流角色**：多对多关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：8005

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `tftensilestrength_id` | bigint | N | MUL | [推断]FK→generator_tf_tensile_strength（拉伸强度） | 🔍 |  |
| `productionplan_id` | bigint | N | MUL | [推断]FK→generator_tf_production_plan（泰峰生产计划） | 🔍 |  |

### generator_tf_tilt_information
**定义**：倾角采集信息 ｜ **代码**：`generator/tf_tilt_information/model.py` ｜ **行数(估)**：6147

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `angle_sensor_value` | varchar(255) | Y | - | 角度传感器数值 | ✅ |  |
| `batch_number` | varchar(255) | Y | - | 炉次号 | ✅ |  |
| `furnace_number` | varchar(255) | Y | - | 炉号 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]掩码同步标记列(V2去向侧)，无代码锚点，非业务字段 | 🔍 |  |

### generator_tf_transfer_cart
**定义**：转运小车 ｜ **代码**：`generator/tf_transfer_cart/model.py` ｜ **行数(估)**：13062

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `weight` | varchar(255) | Y | - | 重量 | ✅ |  |
| `package_count` | varchar(255) | Y | - | 包数 | ✅ |  |
| `batch_number` | varchar(255) | Y | - | 炉次号 | ✅ |  |
| `furnace_number` | varchar(255) | Y | - | 炉号 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]掩码同步标记列(V2去向侧)，无代码锚点，非业务字段 | 🔍 |  |

### generator_tfdl
**定义**：泰峰电炉 ｜ **代码**：`generator/tfdl/model.py` ｜ **行数(估)**：9

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `input_4` | varchar(255) | Y | - | 平均炉耗 | ✅ |  |
| `input_3` | varchar(255) | Y | - | 总耗电 | ✅ |  |
| `input_2` | varchar(255) | Y | - | 炉数 | ✅ |  |
| `date_picker_1` | date | Y | - | 工作日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

---

## 同域兄弟模块
- [[02-生产铸造域/不良品模块-fuadmin数据字典2|不良品模块]]
- [[02-生产铸造域/新排程模块-fuadmin数据字典2|新排程模块]]
- [[02-生产铸造域/生产计划模块-fuadmin数据字典2|生产计划模块]]
- [[02-生产铸造域/生产模块-fuadmin数据字典2|生产模块]]
- [[02-生产铸造域/二维码追溯模块-fuadmin数据字典2|二维码追溯模块]]
- [[02-生产铸造域/班次模块-fuadmin数据字典2|班次模块]]
- [[02-生产铸造域/02-生产铸造域-业务流|02-生产铸造域业务流(代码验证版)]]
