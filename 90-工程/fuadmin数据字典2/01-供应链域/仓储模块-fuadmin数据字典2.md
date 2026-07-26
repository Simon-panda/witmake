---
title: 仓储模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 01-供应链域
tags: [工程, 数据字典2, 代码实证, 仓储]
---

# 仓储模块 · fuadmin 数据字典2（代码实证版）
> 域: 01-供应链域 | 表数: 13 | 字段: 291 | 代码锚定: 290(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/01-供应链域/仓储模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_warehouse_inventory` | 仓库库存台账：按库位记录物料实时库存数量、含税单价与供应商，由入出库单回写，供领料与 | 1243 | 💻 |
| `generator_warehouse_inventory_gh` | 仓库库存（广汇站点分表）：同主表，站点隔离的实时库存台账 | 118 | 💻 |
| `generator_warehouse_inventory_tf` | 仓库库存（泰峰站点分表）：同主表，站点隔离的实时库存台账 | 27 | 💻 |
| `generator_warehouse_inventory_zt` | 仓库库存（治通站点分表）：同主表，站点隔离的实时库存台账（0行，未启用） | 0 | 💻 |
| `generator_warehouse_transaction` | 仓库入出库单主单：仓管员创建的入库/出库/申请出库事务（编号、经办人、状态），驱动明 | 151 | 💻 |
| `generator_warehouse_transaction_detail` | 仓库入出库单明细：按物料记录入出库数量、库位、领料人、单价金额与到货/出库状态，关联 | 286 | 💻 |
| `generator_warehouse_transaction_detail_copy1` | 备份副本表：generator_warehouse_transaction_deta | 233 | 🏭 |
| `generator_warehouse_transaction_detail_gh` | 仓库入出库单明细（广汇站点分表）：同主表，站点隔离的出入库事务明细 | 126 | 💻 |
| `generator_warehouse_transaction_detail_tf` | 仓库入出库单明细（泰峰站点分表）：同主表，站点隔离的出入库事务明细 | 27 | 💻 |
| `generator_warehouse_transaction_detail_zt` | 仓库入出库单明细（治通站点分表）：同主表，站点隔离的出入库事务明细（0行，未启用） | 0 | 💻 |
| `generator_warehouse_transaction_gh` | 仓库入出库单（广汇站点分表）：同主表，站点隔离的出入库事务主单 | 50 | 💻 |
| `generator_warehouse_transaction_tf` | 仓库入出库单（泰峰站点分表）：同主表，站点隔离的出入库事务主单 | 20 | 💻 |
| `generator_warehouse_transaction_zt` | 仓库入出库单（治通站点分表）：同主表，站点隔离的出入库事务主单（0行，未启用） | 0 | 💻 |

---

### generator_warehouse_inventory
**定义**：仓库库存台账：按库位记录物料实时库存数量、含税单价与供应商，由入出库单回写，供领料与采购参考 ｜ **流角色**：实时库存台账 ｜ **代码**：`generator/warehouse_inventory/model.py` ｜ **行数(估)**：1243

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `inventory_quantity` | decimal(13,2) | Y | - | 库存数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `project_qrcode` | varchar(50) | Y | - | 入库二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `supplier_material_map_id` | bigint | Y | - | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping | ✅🔗 | →generator_supplier_material_mapping |

### generator_warehouse_inventory_gh
**定义**：仓库库存（广汇站点分表）：同主表，站点隔离的实时库存台账 ｜ **流角色**：实时库存台账(广汇) ｜ **代码**：`generator/warehouse_inventory/model.py` ｜ **行数(估)**：118

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `inventory_quantity` | decimal(13,2) | Y | - | 库存数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `project_qrcode` | varchar(50) | Y | - | 入库二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_gh | ✅🔗 | →generator_supplier_material_mapping_gh |

### generator_warehouse_inventory_tf
**定义**：仓库库存（泰峰站点分表）：同主表，站点隔离的实时库存台账 ｜ **流角色**：实时库存台账(泰峰) ｜ **代码**：`generator/warehouse_inventory/model.py` ｜ **行数(估)**：27

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `inventory_quantity` | decimal(13,2) | Y | - | 库存数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `project_qrcode` | varchar(50) | Y | - | 入库二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_tf | ✅🔗 | →generator_supplier_material_mapping_tf |

### generator_warehouse_inventory_zt
**定义**：仓库库存（治通站点分表）：同主表，站点隔离的实时库存台账（0行，未启用） ｜ **流角色**：实时库存台账(治通) ｜ **代码**：`generator/warehouse_inventory/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `inventory_quantity` | decimal(13,2) | Y | - | 库存数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `project_qrcode` | varchar(50) | Y | - | 入库二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_zt | ✅🔗 | →generator_supplier_material_mapping_zt |

### generator_warehouse_transaction
**定义**：仓库入出库单主单：仓管员创建的入库/出库/申请出库事务（编号、经办人、状态），驱动明细生成与库存变更 ｜ **流角色**：出入库事务主单 ｜ **代码**：`generator/warehouse_transaction/model.py` ｜ **行数(估)**：151

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_operation_type` | int | Y | - | 出入库类型：0入库 1出库 2项目物料余量入库 3申请出库 4其他入库 | ✅⚖️ |  |
| `transaction_number` | varchar(50) | Y | - | 入出库单编号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `operator` | varchar(20) | Y | - | 经办人 | ✅ |  |
| `warehouse_state` | int | Y | - | 出入库状态：0未入库/未出库 1已入库/已出库 2已导出单据 | ✅⚖️ |  |

### generator_warehouse_transaction_detail
**定义**：仓库入出库单明细：按物料记录入出库数量、库位、领料人、单价金额与到货/出库状态，关联采购订单明细回写到货进度 ｜ **流角色**：出入库事务明细 ｜ **代码**：`generator/warehouse_transaction_detail/model.py` ｜ **行数(估)**：286

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `state` | int | Y | - | 状态：0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅⚖️ |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `stock_date` | date | Y | - | 入出库时间 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入出库数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `warehouse_transaction_id` | bigint | Y | MUL | 仓库入出库单；→generator_warehouse_transaction | ✅🔗 | →generator_warehouse_transaction |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID | ✅ | →generator_purchase_requisition_detail(推断) |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人 | ✅ |  |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail | ✅🔗 | →generator_purchase_order_detail |

### generator_warehouse_transaction_detail_copy1
**定义**：备份副本表：generator_warehouse_transaction_detail 的站点备份副本（订单级用purchase_order_id冗余） ｜ **流角色**：备份副本 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/warehouse_transaction_detail/model.py` ｜ **行数(估)**：233

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `state` | int | Y | - | 状态：0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅⚖️ |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `stock_date` | date | Y | - | 入出库时间 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入出库数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `purchase_order_id` | bigint | Y | MUL | [推断]采购订单ID，关联generator_purchase_order（copy1副本表冗余） | 🔍 | →generator_purchase_order(推断) |
| `warehouse_transaction_id` | bigint | Y | MUL | 仓库入出库单；→generator_warehouse_transaction | ✅🔗 | →generator_warehouse_transaction |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID | ✅ | →generator_purchase_requisition_detail(推断) |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人 | ✅ |  |

### generator_warehouse_transaction_detail_gh
**定义**：仓库入出库单明细（广汇站点分表）：同主表，站点隔离的出入库事务明细 ｜ **流角色**：出入库事务明细(广汇) ｜ **代码**：`generator/warehouse_transaction_detail/model.py` ｜ **行数(估)**：126

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `state` | int | Y | - | 状态：0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅⚖️ |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `stock_date` | date | Y | - | 入出库时间 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入出库数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID | ✅ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `warehouse_transaction_id` | bigint | Y | MUL | 仓库入出库单；→generator_warehouse_transaction_gh | ✅🔗 | →generator_warehouse_transaction_gh |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_gh | ✅🔗 | →generator_purchase_order_detail_gh |

### generator_warehouse_transaction_detail_tf
**定义**：仓库入出库单明细（泰峰站点分表）：同主表，站点隔离的出入库事务明细 ｜ **流角色**：出入库事务明细(泰峰) ｜ **代码**：`generator/warehouse_transaction_detail/model.py` ｜ **行数(估)**：27

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `state` | int | Y | - | 状态：0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅⚖️ |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `stock_date` | date | Y | - | 入出库时间 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入出库数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID | ✅ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `warehouse_transaction_id` | bigint | Y | MUL | 仓库入出库单；→generator_warehouse_transaction_tf | ✅🔗 | →generator_warehouse_transaction_tf |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_tf | ✅🔗 | →generator_purchase_order_detail_tf |

### generator_warehouse_transaction_detail_zt
**定义**：仓库入出库单明细（治通站点分表）：同主表，站点隔离的出入库事务明细（0行，未启用） ｜ **流角色**：出入库事务明细(治通) ｜ **代码**：`generator/warehouse_transaction_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `state` | int | Y | - | 状态：0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅⚖️ |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `stock_date` | date | Y | - | 入出库时间 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入出库数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID | ✅ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `warehouse_transaction_id` | bigint | Y | MUL | 仓库入出库单；→generator_warehouse_transaction_zt | ✅🔗 | →generator_warehouse_transaction_zt |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_zt | ✅🔗 | →generator_purchase_order_detail_zt |

### generator_warehouse_transaction_gh
**定义**：仓库入出库单（广汇站点分表）：同主表，站点隔离的出入库事务主单 ｜ **流角色**：出入库事务主单(广汇) ｜ **代码**：`generator/warehouse_transaction/model.py` ｜ **行数(估)**：50

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_operation_type` | int | Y | - | 出入库类型：0入库 1出库 2项目物料余量入库 3申请出库 4其他入库 | ✅⚖️ |  |
| `transaction_number` | varchar(50) | Y | - | 入出库单编号 | ✅ |  |
| `warehouse_state` | int | Y | - | 出入库状态：0未入库/未出库 1已入库/已出库 2已导出单据 | ✅⚖️ |  |
| `operator` | varchar(20) | Y | - | 经办人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_warehouse_transaction_tf
**定义**：仓库入出库单（泰峰站点分表）：同主表，站点隔离的出入库事务主单 ｜ **流角色**：出入库事务主单(泰峰) ｜ **代码**：`generator/warehouse_transaction/model.py` ｜ **行数(估)**：20

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_operation_type` | int | Y | - | 出入库类型：0入库 1出库 2项目物料余量入库 3申请出库 4其他入库 | ✅⚖️ |  |
| `transaction_number` | varchar(50) | Y | - | 入出库单编号 | ✅ |  |
| `warehouse_state` | int | Y | - | 出入库状态：0未入库/未出库 1已入库/已出库 2已导出单据 | ✅⚖️ |  |
| `operator` | varchar(20) | Y | - | 经办人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_warehouse_transaction_zt
**定义**：仓库入出库单（治通站点分表）：同主表，站点隔离的出入库事务主单（0行，未启用） ｜ **流角色**：出入库事务主单(治通) ｜ **代码**：`generator/warehouse_transaction/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_operation_type` | int | Y | - | 出入库类型：0入库 1出库 2项目物料余量入库 3申请出库 4其他入库 | ✅⚖️ |  |
| `transaction_number` | varchar(50) | Y | - | 入出库单编号 | ✅ |  |
| `warehouse_state` | int | Y | - | 出入库状态：0未入库/未出库 1已入库/已出库 2已导出单据 | ✅⚖️ |  |
| `operator` | varchar(20) | Y | - | 经办人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

---

## 同域兄弟模块
- [[01-供应链域/物流模块-fuadmin数据字典2|物流模块]]
- [[01-供应链域/付款模块-fuadmin数据字典2|付款模块]]
- [[01-供应链域/采购模块-fuadmin数据字典2|采购模块]]
- [[01-供应链域/退货模块-fuadmin数据字典2|退货模块]]
- [[01-供应链域/结算模块-fuadmin数据字典2|结算模块]]
- [[01-供应链域/供应商模块-fuadmin数据字典2|供应商模块]]
- [[01-供应链域/01-供应链域-业务流|01-供应链域业务流(代码验证版)]]
