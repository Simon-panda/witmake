---
title: 物流模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 01-供应链域
tags: [工程, 数据字典2, 代码实证, 物流]
---

# 物流模块 · fuadmin 数据字典2（代码实证版）
> 域: 01-供应链域 | 表数: 11 | 字段: 198 | 代码锚定: 187(94%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/01-供应链域/物流模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_logistics_balance_mode` | 物流结存方式配置：按产品库存定义出入库动作与结存名称（毛坯收入/成品发出等），供物流 | 884 | 💻 |
| `generator_logistics_beginning_record` | 物流期初记录：期初建账时按日期登记产品/零部件的仓库、客户、冻结结存量快照 | 33491 | 💻 |
| `generator_logistics_detail_map` | M2M中间表: 快递物流单↔采购订单明细（含发运数量）（未启用） | 0 | 💻 |
| `generator_logistics_product_stock` | 物流产品库存台账：按公司→产品→零部件三级分类记录仓库/客户/冻结结存量与期初值，物 | 82 | 💻 |
| `generator_logistics_product_stock_copy1` | 备份副本表：generator_logistics_product_stock 的站 | 81 | 🏭 |
| `generator_logistics_push_log` | 物流推送回调日志：记录快递云平台的轨迹推送原文、监控状态与处理结果，供审计重放（未启 | 0 | 💻 |
| `generator_logistics_shipment` | 快递物流单：登记快递公司编码+单号并订阅轨迹查询，缓存查询请求/响应与派揽件员信息（ | 0 | 💻 |
| `generator_logistics_transaction_table` | 物流流转表：记录每笔毛坯/成品出入库结存流水（数量、单据号、PO、结存方式），串联收 | 35471 | 💻 |
| `generator_logistics_transaction_table_copy1` | 备份副本表：generator_logistics_transaction_tabl | 33529 | 🏭 |
| `generator_logistics_waybill` | 物流收/送货单：物流员登记的收发货物单据（单据号、车号、收发货经办人、送货方/收货方 | 15347 | 💻 |
| `generator_logistics_waybill_copy1` | 备份副本表：generator_logistics_waybill 的站点备份副本， | 13963 | 🏭 |

---

### generator_logistics_balance_mode
**定义**：物流结存方式配置：按产品库存定义出入库动作与结存名称（毛坯收入/成品发出等），供物流流转表引用 ｜ **流角色**：结存规则配置 ｜ **代码**：`generator/logistics_balance_mode/model.py` ｜ **行数(估)**：884

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:产品库存） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `mode` | varchar(10) | Y | - | 操作方式：入库/出库 | ✅⚖️ |  |
| `name` | varchar(60) | Y | - | 结存名称：如毛坯收入、成品发出 | ✅⚖️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `product_stock_id` | bigint | Y | MUL | 产品库存；→generator_logistics_product_stock | ✅🔗 | →generator_logistics_product_stock |

### generator_logistics_beginning_record
**定义**：物流期初记录：期初建账时按日期登记产品/零部件的仓库、客户、冻结结存量快照 ｜ **流角色**：期初建账 ｜ **代码**：`generator/logistics_beginning_record/model.py` ｜ **行数(估)**：33491

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `date_time` | date | Y | - | 时间 | ✅ |  |
| `operate` | varchar(20) | Y | - | 记录方式 | ✅ |  |
| `frozen_balance` | int | Y | - | 冻结库存量 | ✅ |  |
| `customer_balance` | int | Y | - | 客户结存量 | ✅ |  |
| `warehouse_balance` | int | Y | - | 仓库结存量 | ✅ |  |
| `type` | varchar(30) | Y | - | 类型 | ✅ |  |
| `name` | varchar(255) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `code` | varchar(255) | Y | - | 编号（界面:产品编号） | ✅🖥️ |  |

### generator_logistics_detail_map
**定义**：M2M中间表: 快递物流单↔采购订单明细（含发运数量）（未启用） ｜ **流角色**：快递-订单关联 ｜ **代码**：`generator/logistics_shipment/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `quantity_shipped` | decimal(13,2) | Y | - | 发运数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `order_detail_id` | bigint | Y | MUL | 采购订单明细；关联采购订单明细；→generator_purchase_order_detail | ✅🔗 | →generator_purchase_order_detail |
| `shipment_id` | bigint | Y | MUL | 物流单；关联物流单；→generator_logistics_shipment | ✅🔗 | →generator_logistics_shipment |

### generator_logistics_product_stock
**定义**：物流产品库存台账：按公司→产品→零部件三级分类记录仓库/客户/冻结结存量与期初值，物流员维护供结存对账 ｜ **流角色**：物流结存主档 ｜ **代码**：`generator/logistics_product_stock/model.py` ｜ **行数(估)**：82

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:上级库存） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `cut` | varchar(10) | Y | - | 结存量切换 | ✅ |  |
| `customer_balance` | int | Y | - | 客户结存量 | ✅ |  |
| `warehouse_balance` | int | Y | - | 仓库结存量 | ✅ |  |
| `name` | varchar(100) | Y | - | 零部件名称（三级分类之第三级）（界面:零部件(三级)） | ✅⚖️🖥️ |  |
| `product` | varchar(100) | Y | - | 产品名称（三级分类之第二级）（界面:产品(二级)） | ✅⚖️🖥️ |  |
| `company` | varchar(100) | Y | MUL | 公司（三级分类之第一级） | ✅⚖️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `is_active` | tinyint(1) | N | - | 是否激活 | ✅ |  |
| `frozen_balance` | int | Y | - | 冻结库存量 | ✅ |  |
| `code` | varchar(255) | Y | - | 编号（界面:产品编号） | ✅🖥️ |  |
| `customer_name` | varchar(100) | Y | - | 客户名称 | ✅ |  |
| `report_format` | json | Y | - | 报表格式（界面:导出格式） | ✅🖥️ |  |
| `Initial_value` | int | N | - | 期初值 | ✅ |  |
| `parent_id` | bigint | Y | MUL | 上级；→generator_logistics_product_stock（界面:上级归属） | ✅🔗🖥️ | →generator_logistics_product_stock |

### generator_logistics_product_stock_copy1
**定义**：备份副本表：generator_logistics_product_stock 的站点备份副本，结构与主表一致 ｜ **流角色**：备份副本 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/logistics_product_stock/model.py` ｜ **行数(估)**：81

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `cut` | varchar(10) | Y | - | 结存量切换 | ✅ |  |
| `customer_balance` | int | Y | - | 客户结存量 | ✅ |  |
| `warehouse_balance` | int | Y | - | 仓库结存量 | ✅ |  |
| `name` | varchar(100) | Y | - | 零部件名称（三级分类之第三级）（界面:原辅料名称） | ✅⚖️🖥️ |  |
| `product` | varchar(100) | Y | - | 产品名称（三级分类之第二级） | ✅⚖️ |  |
| `company` | varchar(100) | Y | MUL | 公司（三级分类之第一级）（界面:所在公司） | ✅⚖️🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `is_active` | tinyint(1) | N | - | 是否激活（界面:状态） | ✅🖥️ |  |
| `frozen_balance` | int | Y | - | 冻结库存量 | ✅ |  |
| `code` | varchar(255) | Y | - | 编号（界面:奖罚单号） | ✅🖥️ |  |
| `customer_name` | varchar(100) | Y | - | 客户名称 | ✅ |  |
| `report_format` | json | Y | - | 报表格式（界面:导出格式） | ✅🖥️ |  |
| `Initial_value` | int | N | - | 期初值 | ✅ |  |
| `parent_id` | bigint | Y | MUL | 上级；→generator_logistics_product_stock（界面:上级归属） | ✅🔗🖥️ | →generator_logistics_product_stock |

### generator_logistics_push_log
**定义**：物流推送回调日志：记录快递云平台的轨迹推送原文、监控状态与处理结果，供审计重放（未启用） ｜ **流角色**：快递回调审计 ｜ **代码**：`generator/logistics_shipment/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `status` | varchar(20) | Y | - | 监控状态；polling/shutdown/abort/updateall（界面:完成状态） | ✅🖥️ |  |
| `raw_payload` | json | Y | - | 原始推送JSON；完整param结构 | ✅ |  |
| `process_result` | varchar(255) | Y | - | 处理结果；云平台处理结果 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `shipment_id` | bigint | Y | MUL | 关联物流单；按com/nu关联；→generator_logistics_shipment | ✅🔗 | →generator_logistics_shipment |

### generator_logistics_shipment
**定义**：快递物流单：登记快递公司编码+单号并订阅轨迹查询，缓存查询请求/响应与派揽件员信息（未启用） ｜ **流角色**：快递轨迹订阅 ｜ **代码**：`generator/logistics_shipment/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:快递公司编码） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `number` | varchar(50) | Y | - | 订阅单号；param.number | ✅ |  |
| `expected_arrival_dt` | date | Y | - | 预计到达时间；arrivalTime解析 | ✅ |  |
| `query_response` | json | Y | - | 查询响应原文；最近一次实时查询响应 | ✅ |  |
| `query_request` | json | Y | - | 查询请求原文；最近一次实时查询请求 | ✅ |  |
| `delivery_man_phone` | varchar(100) | Y | - | 派件员电话；可能多号码逗号分隔 | ✅ |  |
| `delivery_man_name` | varchar(20) | Y | - | 派件员姓名；courierInfo.deliveryManName | ✅ |  |
| `pickup_man_phone` | varchar(100) | Y | - | 揽件员电话；可能多号码逗号分隔 | ✅ |  |
| `pickup_man_name` | varchar(20) | Y | - | 揽件员姓名；courierInfo.pickupManName | ✅ |  |
| `state_code` | varchar(8) | Y | MUL | 基础状态码；0/1/2/3/4/5/8/14等 | ✅ |  |
| `to_text` | varchar(150) | Y | - | 目的地；param.to；resultv2=8建议必填 | ✅ |  |
| `phone` | varchar(20) | Y | - | 电话号码；部分快递公司必填 | ✅ |  |
| `num` | varchar(50) | Y | - | 快递单号；param.num | ✅ |  |
| `com` | varchar(50) | Y | MUL | 快递公司编码；param.com | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |

### generator_logistics_transaction_table
**定义**：物流流转表：记录每笔毛坯/成品出入库结存流水（数量、单据号、PO、结存方式），串联收送货单与产品库存台账 ｜ **流角色**：物流结存流水 ｜ **代码**：`generator/logistics_transaction_table/model.py` ｜ **行数(估)**：35471

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:产品库存） | ✅📦🖥️ |  |
| `remark` | longtext | Y | - | 备注（界面:历史记录） | ✅🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `date_time` | datetime(6) | Y | - | 结存时间（界面:日期） | ✅🖥️ |  |
| `receipt_number` | varchar(255) | Y | - | 单据号 | ✅ |  |
| `number` | int | Y | - | 数量 | ✅ |  |
| `mode` | varchar(80) | Y | - | 结存方式：如'毛坯收入(入库)(仓库结算)'，首括号定出入库、次括号定结算方式 | ✅⚖️ |  |
| `name` | varchar(80) | Y | - | 零部件名称（三级分类之第三级） | ✅⚖️ |  |
| `product` | varchar(80) | Y | - | 产品名称（三级分类之第二级） | ✅⚖️ |  |
| `company` | varchar(80) | Y | - | 公司（三级分类之第一级） | ✅⚖️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `product_stock_id` | bigint | Y | MUL | 产品库存；→generator_logistics_product_stock | ✅🔗 | →generator_logistics_product_stock |
| `po` | varchar(255) | Y | - | PO | ✅ |  |
| `logistics_waybill_id` | bigint | Y | MUL | 单号id；→generator_logistics_waybill | ✅🔗 | →generator_logistics_waybill |
| `code` | varchar(255) | Y | - | 编号 | ✅ |  |
| `balance_mode_id` | bigint | Y | MUL | 产品结存方式；→generator_logistics_balance_mode | ✅🔗 | →generator_logistics_balance_mode |
| `table_remark` | varchar(255) | Y | - | 表格内备注 | ✅ |  |

### generator_logistics_transaction_table_copy1
**定义**：备份副本表：generator_logistics_transaction_table 的站点备份副本，结构与主表一致 ｜ **流角色**：备份副本 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/logistics_transaction_table/model.py` ｜ **行数(估)**：33529

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | longtext | Y | - | 备注 | ✅ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `date_time` | datetime(6) | Y | - | 结存时间（界面:日期） | ✅🖥️ |  |
| `receipt_number` | varchar(255) | Y | - | 单据号 | ✅ |  |
| `number` | int | Y | - | 数量（界面:库存数量） | ✅🖥️ |  |
| `mode` | varchar(80) | Y | - | 结存方式：如'毛坯收入(入库)(仓库结算)'，首括号定出入库、次括号定结算方式（界面:操作方式） | ✅⚖️🖥️ |  |
| `name` | varchar(80) | Y | - | 零部件名称（三级分类之第三级）（界面:原辅料名称） | ✅⚖️🖥️ |  |
| `product` | varchar(80) | Y | - | 产品名称（三级分类之第二级） | ✅⚖️ |  |
| `company` | varchar(80) | Y | - | 公司（三级分类之第一级）（界面:所在公司） | ✅⚖️🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `product_stock_id` | bigint | Y | MUL | 产品库存；→generator_logistics_product_stock | ✅🔗 | →generator_logistics_product_stock |
| `po` | varchar(255) | Y | - | PO | ✅ |  |
| `logistics_waybill_id` | bigint | Y | MUL | 单号id；→generator_logistics_waybill | ✅🔗 | →generator_logistics_waybill |
| `code` | varchar(255) | Y | - | 编号（界面:奖罚单号） | ✅🖥️ |  |
| `balance_mode_id` | bigint | Y | MUL | 产品结存方式；→generator_logistics_balance_mode | ✅🔗 | →generator_logistics_balance_mode |
| `table_remark` | varchar(255) | Y | - | 表格内备注 | ✅ |  |

### generator_logistics_waybill
**定义**：物流收/送货单：物流员登记的收发货物单据（单据号、车号、收发货经办人、送货方/收货方），车辆司机签收人均为文本字段无实体表 ｜ **流角色**：收发货单据登记 ｜ **代码**：`generator/logistics_waybill/model.py` ｜ **行数(估)**：15347

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `data` | json | Y | - | 表格数据（暂未使用） | ✅⚖️ |  |
| `columns` | json | Y | - | 表格头（暂未使用） | ✅⚖️ |  |
| `date_time` | datetime(6) | Y | - | 日期 | ✅ |  |
| `img` | varchar(255) | Y | - | 图片 | ✅ |  |
| `receiver` | varchar(80) | Y | - | 收货经办人 | ✅ |  |
| `pickup_person` | varchar(80) | Y | - | 提货人 | ✅ |  |
| `shipper` | varchar(80) | Y | - | 发货经办人 | ✅ |  |
| `car_number` | varchar(80) | Y | - | 车号 | ✅ |  |
| `consignor` | varchar(100) | Y | - | 送货方 | ✅ |  |
| `consignee` | varchar(100) | Y | - | 收货方 | ✅ |  |
| `receipt_number` | varchar(30) | Y | - | 单据号 | ✅ |  |
| `variety` | varchar(10) | Y | - | 货物种类（暂未使用）（界面:产品） | ✅⚖️🖥️ |  |
| `type` | varchar(10) | Y | - | 货单类型：出库/入库（界面:产品） | ✅⚖️🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |

### generator_logistics_waybill_copy1
**定义**：备份副本表：generator_logistics_waybill 的站点备份副本，结构与主表一致 ｜ **流角色**：备份副本 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/logistics_waybill/model.py` ｜ **行数(估)**：13963

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `data` | json | Y | - | 表格数据（暂未使用） | ✅⚖️ |  |
| `columns` | json | Y | - | 表格头（暂未使用） | ✅⚖️ |  |
| `date_time` | datetime(6) | Y | - | 日期 | ✅ |  |
| `img` | varchar(255) | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `receiver` | varchar(80) | Y | - | 收货经办人 | ✅ |  |
| `pickup_person` | varchar(80) | Y | - | 提货人 | ✅ |  |
| `shipper` | varchar(80) | Y | - | 发货经办人 | ✅ |  |
| `car_number` | varchar(80) | Y | - | 车号 | ✅ |  |
| `consignor` | varchar(100) | Y | - | 送货方 | ✅ |  |
| `consignee` | varchar(100) | Y | - | 收货方 | ✅ |  |
| `receipt_number` | varchar(30) | Y | - | 单据号 | ✅ |  |
| `variety` | varchar(10) | Y | - | 货物种类（暂未使用）（界面:产品） | ✅⚖️🖥️ |  |
| `type` | varchar(10) | Y | - | 货单类型：出库/入库（界面:问题分类） | ✅⚖️🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
