---
title: 项目模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 04-订单项目域
tags: [工程, 数据字典2, 代码实证, 项目]
---

# 项目模块 · fuadmin 数据字典2（代码实证版）
> 域: 04-订单项目域 | 表数: 13 | 字段: 283 | 代码锚定: 269(95%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/04-订单项目域/项目模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_project_attendance` | 项目出勤 | 7094 | 💻 |
| `generator_project_info` | 项目信息 | 325 | 💻 |
| `generator_project_material_summary` | 项目物料入出库记录单 | 1319 | 💻 |
| `generator_project_material_summary_detail` | 项目物料入出库记录单明细 | 4044 | 💻 |
| `generator_project_material_summary_detail_copy1` | 项目物料入出库记录单明细 | 3361 | 🏭 |
| `generator_project_material_summary_detail_gh` | 项目物料入出库记录单明细 | 0 | 💻 |
| `generator_project_material_summary_detail_tf` | 项目物料入出库记录单明细 | 0 | 💻 |
| `generator_project_material_summary_detail_zt` | 项目物料入出库记录单明细 | 0 | 💻 |
| `generator_project_material_summary_gh` | 项目物料入出库记录单 | 0 | 💻 |
| `generator_project_material_summary_tf` | 项目物料入出库记录单 | 0 | 💻 |
| `generator_project_material_summary_zt` | 项目物料入出库记录单 | 0 | 💻 |
| `generator_project_personal` | 项目个人清单 | 3052 | 💻 |
| `generator_project_schedule` | 项目进度 | 2840 | 💻 |

---

### generator_project_attendance
**定义**：项目出勤 ｜ **代码**：`generator/project_personal/model.py` ｜ **行数(估)**：7094

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `date` | date | Y | - | 日期 | ✅ |  |
| `user_id` | bigint | Y | MUL | 人员信息；→system_users | ✅🔗 | →system_users |
| `working_hours` | varchar(30) | Y | - | 工作小时（界面:工作记录） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_project_info
**定义**：项目信息 ｜ **代码**：`generator/project_info/model.py` ｜ **行数(估)**：325

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:项目号） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `history` | json | Y | - | 历史操作记录 | ✅ |  |
| `msg_info` | json | Y | - | 留言信息 | ✅ |  |
| `users` | json | Y | - | 参与人 | ✅ |  |
| `state` | int | Y | - | 状态；未启动 1/进行中 2/暂停 3/撤销 4/已完成 5/归档 6 | ✅💬 |  |
| `end_time` | date | Y | - | 计划结束时间 | ✅ |  |
| `start_time` | date | Y | - | 计划开始时间 | ✅ |  |
| `require` | varchar(500) | Y | - | 项目要求 | ✅ |  |
| `name` | varchar(30) | Y | - | 项目名称 | ✅ |  |
| `code` | varchar(30) | Y | UNI | 项目号 | ✅ |  |
| `work_station` | varchar(30) | Y | - | 工作站 | ✅ |  |
| `production_line` | varchar(30) | Y | - | 产线 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `read_users` | json | Y | - | 可阅读（界面:阅读人） | ✅🖥️ |  |
| `parent_id` | bigint | Y | MUL | 上级；→generator_project_info（界面:上级归属） | ✅🔗🖥️ | →generator_project_info |
| `delivery_time` | datetime | Y | - | 项目交付时间 | ✅ |  |
| `product` | varchar(30) | Y | - | 产品 | ✅ |  |
| `is_delete` | tinyint(1) | Y | - | 是否删除；是否删除(软删除标记)（界面:封存） | ✅📦🖥️ |  |
| `project` | varchar(30) | Y | - | 项目归属；治通 泰峰 智机 广汇 | ✅💬 |  |

### generator_project_material_summary
**定义**：项目物料入出库记录单 ｜ **代码**：`generator/project_material_summary/model.py` ｜ **行数(估)**：1319

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:出入库类型） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `summary_number` | varchar(50) | Y | - | 项目入出库记录单编号（界面:入出库单编号） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `bound_type` | int | Y | - | 出入库类型；入库或出库操作；0是入库 1是出库 2是申请出库 | ✅💬 |  |
| `operator` | varchar(20) | Y | - | 经办人 | ✅ |  |
| `bound_state` | int | Y | - | 出入库状态；0是未入库/未出库 1是已入库/已出库 2是已导出单据 | ✅💬 |  |

### generator_project_material_summary_detail
**定义**：项目物料入出库记录单明细 ｜ **代码**：`generator/project_material_summary_detail/model.py` ｜ **行数(估)**：4044

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:物料入出库单） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称（界面:请选择或输入项目名称） | ✅🖥️ |  |
| `project_number` | varchar(50) | Y | - | 项目号（界面:请选择或输入项目号） | ✅🖥️ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `project_qrcode` | varchar(50) | Y | - | 项目入库二维码（界面:入库码） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `project_material_summary_id` | bigint | Y | MUL | 项目物料入出库记录单；→generator_project_material_summary | ✅🔗 | →generator_project_material_summary |
| `stock_date` | date | Y | - | 出入库日期；入库或出库日期（界面:入出库时间） | ✅🖥️ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 出入库数量；入库或出库数量（界面:入出库数量） | ✅🖥️ |  |
| `state` | int | Y | - | 状态；0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅💬 |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail |

### generator_project_material_summary_detail_copy1
**定义**：项目物料入出库记录单明细 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/project_material_summary_detail/model.py` ｜ **行数(估)**：3361

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `project_qrcode` | varchar(50) | Y | - | 项目入库二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `project_material_summary_id` | bigint | Y | MUL | 项目物料入出库记录单；→generator_project_material_summary | ✅🔗 | →generator_project_material_summary |
| `purchase_order_id` | bigint | Y | MUL | （界面:采购订单ID） | 🔍🖥️ | →generator_purchase_order(推断) |
| `stock_date` | date | Y | - | 出入库日期；入库或出库日期（界面:库位） | ✅🖥️ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 出入库数量；入库或出库数量（界面:单位） | ✅🖥️ |  |
| `state` | int | Y | - | 状态；0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅💬 |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |

### generator_project_material_summary_detail_gh
**定义**：项目物料入出库记录单明细 ｜ **代码**：`generator/project_material_summary_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `state` | int | Y | - | 状态；0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅💬 |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 出入库数量；入库或出库数量（界面:单位） | ✅🖥️ |  |
| `stock_date` | date | Y | - | 出入库日期；入库或出库日期（界面:库位） | ✅🖥️ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `project_qrcode` | varchar(50) | Y | - | 项目入库二维码 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `project_material_summary_id` | bigint | Y | MUL | 项目物料入出库记录单；→generator_project_material_summary_gh | ✅🔗 | →generator_project_material_summary_gh |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_gh（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail_gh |

### generator_project_material_summary_detail_tf
**定义**：项目物料入出库记录单明细 ｜ **代码**：`generator/project_material_summary_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `state` | int | Y | - | 状态；0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅💬 |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 出入库数量；入库或出库数量（界面:单位） | ✅🖥️ |  |
| `stock_date` | date | Y | - | 出入库日期；入库或出库日期（界面:库位） | ✅🖥️ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `project_qrcode` | varchar(50) | Y | - | 项目入库二维码 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `project_material_summary_id` | bigint | Y | MUL | 项目物料入出库记录单；→generator_project_material_summary_tf | ✅🔗 | →generator_project_material_summary_tf |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_tf（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail_tf |

### generator_project_material_summary_detail_zt
**定义**：项目物料入出库记录单明细 ｜ **代码**：`generator/project_material_summary_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `state` | int | Y | - | 状态；0退换货 1全部到货 2未全部到货 3已入库 4未出库 5已出库 6已导出(入库) 7已导出(出库) | ✅💬 |  |
| `remaining_quantity` | decimal(13,2) | Y | - | 结存数量 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 出入库数量；入库或出库数量（界面:单位） | ✅🖥️ |  |
| `stock_date` | date | Y | - | 出入库日期；入库或出库日期（界面:库位） | ✅🖥️ |  |
| `location` | varchar(50) | Y | - | 库位 | ✅ |  |
| `recipient` | varchar(20) | Y | - | 领料人 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `project_qrcode` | varchar(50) | Y | - | 项目入库二维码 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `project_material_summary_id` | bigint | Y | MUL | 项目物料入出库记录单；→generator_project_material_summary_zt | ✅🔗 | →generator_project_material_summary_zt |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_zt（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail_zt |

### generator_project_material_summary_gh
**定义**：项目物料入出库记录单 ｜ **代码**：`generator/project_material_summary/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `summary_number` | varchar(50) | Y | - | 项目入出库记录单编号（界面:入出库单编号） | ✅🖥️ |  |
| `bound_type` | int | Y | - | 出入库类型；入库或出库操作；0是入库 1是出库 2是申请出库 | ✅💬 |  |
| `bound_state` | int | Y | - | 出入库状态；0是未入库/未出库 1是已入库/已出库 2是已导出单据 | ✅💬 |  |
| `operator` | varchar(20) | Y | - | 经办人（界面:操作员） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_project_material_summary_tf
**定义**：项目物料入出库记录单 ｜ **代码**：`generator/project_material_summary/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `summary_number` | varchar(50) | Y | - | 项目入出库记录单编号（界面:入出库单编号） | ✅🖥️ |  |
| `bound_type` | int | Y | - | 出入库类型；入库或出库操作；0是入库 1是出库 2是申请出库 | ✅💬 |  |
| `bound_state` | int | Y | - | 出入库状态；0是未入库/未出库 1是已入库/已出库 2是已导出单据 | ✅💬 |  |
| `operator` | varchar(20) | Y | - | 经办人（界面:操作员） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_project_material_summary_zt
**定义**：项目物料入出库记录单 ｜ **代码**：`generator/project_material_summary/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `summary_number` | varchar(50) | Y | - | 项目入出库记录单编号（界面:入出库单编号） | ✅🖥️ |  |
| `bound_type` | int | Y | - | 出入库类型；入库或出库操作；0是入库 1是出库 2是申请出库 | ✅💬 |  |
| `bound_state` | int | Y | - | 出入库状态；0是未入库/未出库 1是已入库/已出库 2是已导出单据 | ✅💬 |  |
| `operator` | varchar(20) | Y | - | 经办人（界面:操作员） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_project_personal
**定义**：项目个人清单 ｜ **代码**：`generator/project_personal/model.py` ｜ **行数(估)**：3052

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:项目信息） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `total_planned_worktime` | decimal(10,2) | Y | - | 下发项目总计划用时(H)（界面:下发总计划用时） | ✅🖥️ |  |
| `total_planned_time` | decimal(10,2) | Y | - | 总计划用时(H) | ✅ |  |
| `output_value` | decimal(10,2) | Y | - | 个人分摊产值(元) | ✅ |  |
| `workload` | decimal(10,2) | Y | - | 工作量占比(%) | ✅ |  |
| `project_commission` | decimal(10,2) | Y | - | 项目提成(%) | ✅ |  |
| `price` | decimal(10,2) | Y | - | 售价(元) | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `project_info` | varchar(80) | N | - | 项目信息 | ✅ |  |
| `user` | varchar(30) | N | - | 项目执行人（界面:人员） | ✅🖥️ |  |
| `difficulty` | decimal(4,2) | Y | - | 难度系数 | ✅ |  |
| `personal_average` | decimal(10,2) | Y | - | 个人平均价值(元) | ✅ |  |
| `content` | varchar(160) | Y | - | 项目类型及内容 | ✅ |  |
| `name` | varchar(100) | Y | - | 具体名称 | ✅ |  |
| `man_hour` | decimal(10,2) | Y | - | 初始累计工时(H) | ✅ |  |

### generator_project_schedule
**定义**：项目进度 ｜ **代码**：`generator/project_schedule/model.py` ｜ **行数(估)**：2840

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:任务名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `state` | int | Y | - | 任务状态 | ✅ |  |
| `end_time` | date | Y | - | 结束时间 | ✅ |  |
| `start_time` | date | Y | - | 开始时间 | ✅ |  |
| `progress` | int | Y | - | 进度 | ✅ |  |
| `user` | varchar(255) | Y | - | 执行人 | ✅ |  |
| `name` | varchar(50) | Y | - | 任务名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 父项目；→generator_project_schedule（界面:上级归属） | ✅🔗🖥️ | →generator_project_schedule |
| `project_info_id` | bigint | Y | MUL | 项目信息；→generator_project_info | ✅🔗 | →generator_project_info |
| `planned_end` | date | Y | - | 计划结束 | ✅ |  |
| `planned_start` | date | Y | - | 计划开始 | ✅ |  |
