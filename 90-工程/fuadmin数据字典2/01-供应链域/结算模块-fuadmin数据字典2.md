---
title: 结算模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 01-供应链域
tags: [工程, 数据字典2, 代码实证, 结算]
---

# 结算模块 · fuadmin 数据字典2（代码实证版）
> 域: 01-供应链域 | 表数: 24 | 字段: 336 | 代码锚定: 312(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/01-供应链域/结算模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_settlement_bill` | 与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未启用） | 0 | 💻 |
| `generator_settlement_bill_detail` | 结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（未启用） | 0 | 💻 |
| `generator_settlement_bill_detail_gh` | 广汇站点分表：结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（ | 0 | 💻 |
| `generator_settlement_bill_detail_tf` | 泰峰站点分表：结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（ | 0 | 💻 |
| `generator_settlement_bill_detail_zt` | 治通站点分表：结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（ | 0 | 💻 |
| `generator_settlement_bill_gh` | 广汇站点分表：与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未 | 0 | 💻 |
| `generator_settlement_bill_tf` | 泰峰站点分表：与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未 | 0 | 💻 |
| `generator_settlement_bill_zt` | 治通站点分表：与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未 | 0 | 💻 |
| `generator_settlement_invoice` | 供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） | 0 | 💻 |
| `generator_settlement_invoice_detail` | 结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启用） | 0 | 💻 |
| `generator_settlement_invoice_detail_gh` | 广汇站点分表：结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启 | 0 | 💻 |
| `generator_settlement_invoice_detail_tf` | 泰峰站点分表：结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启 | 0 | 💻 |
| `generator_settlement_invoice_detail_zt` | 治通站点分表：结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启 | 0 | 💻 |
| `generator_settlement_invoice_gh` | 广汇站点分表：供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） | 0 | 💻 |
| `generator_settlement_invoice_payment_allocation` | 结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） | 0 | 💻 |
| `generator_settlement_invoice_payment_allocation_gh` | 广汇站点分表：结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） | 0 | 💻 |
| `generator_settlement_invoice_payment_allocation_tf` | 泰峰站点分表：结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） | 0 | 💻 |
| `generator_settlement_invoice_payment_allocation_zt` | 治通站点分表：结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） | 0 | 💻 |
| `generator_settlement_invoice_tf` | 泰峰站点分表：供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） | 0 | 💻 |
| `generator_settlement_invoice_zt` | 治通站点分表：供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） | 0 | 💻 |
| `generator_settlement_payment_allocation` | 付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） | 0 | 💻 |
| `generator_settlement_payment_allocation_gh` | 广汇站点分表：付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） | 0 | 💻 |
| `generator_settlement_payment_allocation_tf` | 泰峰站点分表：付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） | 0 | 💻 |
| `generator_settlement_payment_allocation_zt` | 治通站点分表：付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） | 0 | 💻 |

---

### generator_settlement_bill
**定义**：与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未启用） ｜ **流角色**：结算链起点：结算单头（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `bill_number` | varchar(50) | Y | UNI | 结算单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 结算总金额 | ✅ |  |
| `invoiced_amount` | decimal(13,2) | Y | - | 已开票金额 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `settlement_type` | varchar(30) | Y | - | 结算类型 | ✅ |  |
| `state` | int | Y | - | 结算状态；0草稿 1处理中 100已作废 | ✅ |  |
| `is_closed` | tinyint(1) | N | - | 是否关闭 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_settlement_bill_detail
**定义**：结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（未启用） ｜ **流角色**：结算行：分摊采购订单明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `source_purchase_order_detail_id` | bigint | Y | - | 来源采购订单明细ID；来源采购订单明细ID快照 | ✅ |  |
| `allocated_quantity` | decimal(13,2) | Y | - | 结算数量 | ✅ |  |
| `allocated_amount` | decimal(13,2) | Y | - | 结算金额（界面:分配金额） | ✅🖥️ |  |
| `quantity_basis` | varchar(30) | Y | - | 开票数量口径；order_quantity按订单数量，inbound_quantity按入库数量 | ✅ |  |
| `source_snapshot` | json | Y | - | 来源明细快照；来源订单明细的不可变快照 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill | ✅🔗 | →generator_settlement_bill |

### generator_settlement_bill_detail_gh
**定义**：广汇站点分表：结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（未启用） ｜ **流角色**：结算行：分摊采购订单明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `source_purchase_order_detail_id` | bigint | Y | - | 来源采购订单明细ID；来源采购订单明细ID快照 | ✅ |  |
| `allocated_quantity` | decimal(13,2) | Y | - | 结算数量 | ✅ |  |
| `allocated_amount` | decimal(13,2) | Y | - | 结算金额（界面:分配金额） | ✅🖥️ |  |
| `quantity_basis` | varchar(30) | Y | - | 开票数量口径；order_quantity按订单数量，inbound_quantity按入库数量 | ✅ |  |
| `source_snapshot` | json | Y | - | 来源明细快照；来源订单明细的不可变快照 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_gh（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail_gh |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill_gh | ✅🔗 | →generator_settlement_bill_gh |

### generator_settlement_bill_detail_tf
**定义**：泰峰站点分表：结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（未启用） ｜ **流角色**：结算行：分摊采购订单明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `source_purchase_order_detail_id` | bigint | Y | - | 来源采购订单明细ID；来源采购订单明细ID快照 | ✅ |  |
| `allocated_quantity` | decimal(13,2) | Y | - | 结算数量 | ✅ |  |
| `allocated_amount` | decimal(13,2) | Y | - | 结算金额（界面:分配金额） | ✅🖥️ |  |
| `quantity_basis` | varchar(30) | Y | - | 开票数量口径；order_quantity按订单数量，inbound_quantity按入库数量 | ✅ |  |
| `source_snapshot` | json | Y | - | 来源明细快照；来源订单明细的不可变快照 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_tf（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail_tf |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill_tf | ✅🔗 | →generator_settlement_bill_tf |

### generator_settlement_bill_detail_zt
**定义**：治通站点分表：结算单行，分摊自采购订单明细并保留来源快照，按订单/入库数量口径结算（未启用） ｜ **流角色**：结算行：分摊采购订单明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `source_purchase_order_detail_id` | bigint | Y | - | 来源采购订单明细ID；来源采购订单明细ID快照 | ✅ |  |
| `allocated_quantity` | decimal(13,2) | Y | - | 结算数量 | ✅ |  |
| `allocated_amount` | decimal(13,2) | Y | - | 结算金额（界面:分配金额） | ✅🖥️ |  |
| `quantity_basis` | varchar(30) | Y | - | 开票数量口径；order_quantity按订单数量，inbound_quantity按入库数量 | ✅ |  |
| `source_snapshot` | json | Y | - | 来源明细快照；来源订单明细的不可变快照 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_detail_id` | bigint | Y | MUL | 采购订单明细；→generator_purchase_order_detail_zt（界面:采购订单明细ID） | ✅🔗🖥️ | →generator_purchase_order_detail_zt |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill_zt | ✅🔗 | →generator_settlement_bill_zt |

### generator_settlement_bill_gh
**定义**：广汇站点分表：与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未启用） ｜ **流角色**：结算链起点：结算单头（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `bill_number` | varchar(50) | Y | UNI | 结算单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 结算总金额 | ✅ |  |
| `invoiced_amount` | decimal(13,2) | Y | - | 已开票金额 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `settlement_type` | varchar(30) | Y | - | 结算类型 | ✅ |  |
| `state` | int | Y | - | 结算状态；0草稿 1处理中 100已作废 | ✅ |  |
| `is_closed` | tinyint(1) | N | - | 是否关闭 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_settlement_bill_tf
**定义**：泰峰站点分表：与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未启用） ｜ **流角色**：结算链起点：结算单头（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `bill_number` | varchar(50) | Y | UNI | 结算单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 结算总金额 | ✅ |  |
| `invoiced_amount` | decimal(13,2) | Y | - | 已开票金额 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `settlement_type` | varchar(30) | Y | - | 结算类型 | ✅ |  |
| `state` | int | Y | - | 结算状态；0草稿 1处理中 100已作废 | ✅ |  |
| `is_closed` | tinyint(1) | N | - | 是否关闭 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_settlement_bill_zt
**定义**：治通站点分表：与供应商对账的结算单头，记录结算总额、已开票、已付、未付与关闭标志（未启用） ｜ **流角色**：结算链起点：结算单头（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `bill_number` | varchar(50) | Y | UNI | 结算单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 结算总金额 | ✅ |  |
| `invoiced_amount` | decimal(13,2) | Y | - | 已开票金额 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `settlement_type` | varchar(30) | Y | - | 结算类型 | ✅ |  |
| `state` | int | Y | - | 结算状态；0草稿 1处理中 100已作废 | ✅ |  |
| `is_closed` | tinyint(1) | N | - | 是否关闭 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_settlement_invoice
**定义**：供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） ｜ **流角色**：发票登记：挂结算单（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_code` | varchar(50) | Y | - | 发票代码 | ✅ |  |
| `invoice_number` | varchar(50) | Y | - | 发票号码 | ✅ |  |
| `invoice_date` | date | Y | - | 开票日期 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 发票金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 发票未付金额 | ✅ |  |
| `state` | int | Y | - | 发票支付状态；0草稿 1未支付 2部分支付 3全部支付 100已作废 | ✅ |  |
| `file_url` | json | Y | - | 发票附件（界面:上传附件） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill | ✅🔗 | →generator_settlement_bill |

### generator_settlement_invoice_detail
**定义**：结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启用） ｜ **流角色**：发票行：开票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_quantity` | decimal(13,2) | Y | - | 开票数量 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 开票含税单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 开票税率（界面:税点(%)） | ✅🖥️ |  |
| `invoice_amount` | decimal(13,2) | Y | - | 开票金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail | ✅🔗 | →generator_settlement_bill_detail |
| `settlement_invoice_id` | bigint | Y | MUL | 结算发票；→generator_settlement_invoice | ✅🔗 | →generator_settlement_invoice |

### generator_settlement_invoice_detail_gh
**定义**：广汇站点分表：结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启用） ｜ **流角色**：发票行：开票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_quantity` | decimal(13,2) | Y | - | 开票数量 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 开票含税单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 开票税率（界面:税点(%)） | ✅🖥️ |  |
| `invoice_amount` | decimal(13,2) | Y | - | 开票金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail_gh | ✅🔗 | →generator_settlement_bill_detail_gh |
| `settlement_invoice_id` | bigint | Y | MUL | 结算发票；→generator_settlement_invoice_gh | ✅🔗 | →generator_settlement_invoice_gh |

### generator_settlement_invoice_detail_tf
**定义**：泰峰站点分表：结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启用） ｜ **流角色**：发票行：开票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_quantity` | decimal(13,2) | Y | - | 开票数量 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 开票含税单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 开票税率（界面:税点(%)） | ✅🖥️ |  |
| `invoice_amount` | decimal(13,2) | Y | - | 开票金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail_tf | ✅🔗 | →generator_settlement_bill_detail_tf |
| `settlement_invoice_id` | bigint | Y | MUL | 结算发票；→generator_settlement_invoice_tf | ✅🔗 | →generator_settlement_invoice_tf |

### generator_settlement_invoice_detail_zt
**定义**：治通站点分表：结算发票行，回链结算单行，记录开票数量、含税单价、税率与开票金额（未启用） ｜ **流角色**：发票行：开票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_quantity` | decimal(13,2) | Y | - | 开票数量 | ✅ |  |
| `unit_price` | decimal(15,4) | Y | - | 开票含税单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 开票税率（界面:税点(%)） | ✅🖥️ |  |
| `invoice_amount` | decimal(13,2) | Y | - | 开票金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail_zt | ✅🔗 | →generator_settlement_bill_detail_zt |
| `settlement_invoice_id` | bigint | Y | MUL | 结算发票；→generator_settlement_invoice_zt | ✅🔗 | →generator_settlement_invoice_zt |

### generator_settlement_invoice_gh
**定义**：广汇站点分表：供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） ｜ **流角色**：发票登记：挂结算单（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_code` | varchar(50) | Y | - | 发票代码 | ✅ |  |
| `invoice_number` | varchar(50) | Y | - | 发票号码 | ✅ |  |
| `invoice_date` | date | Y | - | 开票日期 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 发票金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 发票未付金额 | ✅ |  |
| `state` | int | Y | - | 发票支付状态；0草稿 1未支付 2部分支付 3全部支付 100已作废 | ✅ |  |
| `file_url` | json | Y | - | 发票附件（界面:上传附件） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill_gh | ✅🔗 | →generator_settlement_bill_gh |

### generator_settlement_invoice_payment_allocation
**定义**：结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） ｜ **流角色**：付款分摊→发票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_invoice_detail_id` | bigint | Y | MUL | 结算发票明细；→generator_settlement_invoice_detail | ✅🔗 | →generator_settlement_invoice_detail |
| `settlement_payment_allocation_id` | bigint | Y | MUL | 结算付款分摊；→generator_settlement_payment_allocation | ✅🔗 | →generator_settlement_payment_allocation |

### generator_settlement_invoice_payment_allocation_gh
**定义**：广汇站点分表：结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） ｜ **流角色**：付款分摊→发票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_invoice_detail_id` | bigint | Y | MUL | 结算发票明细；→generator_settlement_invoice_detail_gh | ✅🔗 | →generator_settlement_invoice_detail_gh |
| `settlement_payment_allocation_id` | bigint | Y | MUL | 结算付款分摊；→generator_settlement_payment_allocation_gh | ✅🔗 | →generator_settlement_payment_allocation_gh |

### generator_settlement_invoice_payment_allocation_tf
**定义**：泰峰站点分表：结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） ｜ **流角色**：付款分摊→发票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_invoice_detail_id` | bigint | Y | MUL | 结算发票明细；→generator_settlement_invoice_detail_tf | ✅🔗 | →generator_settlement_invoice_detail_tf |
| `settlement_payment_allocation_id` | bigint | Y | MUL | 结算付款分摊；→generator_settlement_payment_allocation_tf | ✅🔗 | →generator_settlement_payment_allocation_tf |

### generator_settlement_invoice_payment_allocation_zt
**定义**：治通站点分表：结算付款分摊到发票行的二级分摊表，追踪每笔分摊对应的发票明细（未启用） ｜ **流角色**：付款分摊→发票明细（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_invoice_detail_id` | bigint | Y | MUL | 结算发票明细；→generator_settlement_invoice_detail_zt | ✅🔗 | →generator_settlement_invoice_detail_zt |
| `settlement_payment_allocation_id` | bigint | Y | MUL | 结算付款分摊；→generator_settlement_payment_allocation_zt | ✅🔗 | →generator_settlement_payment_allocation_zt |

### generator_settlement_invoice_tf
**定义**：泰峰站点分表：供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） ｜ **流角色**：发票登记：挂结算单（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_code` | varchar(50) | Y | - | 发票代码 | ✅ |  |
| `invoice_number` | varchar(50) | Y | - | 发票号码 | ✅ |  |
| `invoice_date` | date | Y | - | 开票日期 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 发票金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 发票未付金额 | ✅ |  |
| `state` | int | Y | - | 发票支付状态；0草稿 1未支付 2部分支付 3全部支付 100已作废 | ✅ |  |
| `file_url` | json | Y | - | 发票附件（界面:上传附件） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill_tf | ✅🔗 | →generator_settlement_bill_tf |

### generator_settlement_invoice_zt
**定义**：治通站点分表：供应商发票登记表，挂结算单，记录发票代码号码、金额与支付状态（未启用） ｜ **流角色**：发票登记：挂结算单（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `invoice_code` | varchar(50) | Y | - | 发票代码 | ✅ |  |
| `invoice_number` | varchar(50) | Y | - | 发票号码 | ✅ |  |
| `invoice_date` | date | Y | - | 开票日期 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 发票金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 发票未付金额 | ✅ |  |
| `state` | int | Y | - | 发票支付状态；0草稿 1未支付 2部分支付 3全部支付 100已作废 | ✅ |  |
| `file_url` | json | Y | - | 发票附件（界面:上传附件） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `settlement_bill_id` | bigint | Y | MUL | 结算单；→generator_settlement_bill_zt | ✅🔗 | →generator_settlement_bill_zt |

### generator_settlement_payment_allocation
**定义**：付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） ｜ **流角色**：付款→结算明细分摊（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `payment_record_id` | bigint | Y | MUL | 付款记录；→generator_payment_record | ✅🔗 | →generator_payment_record |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail | ✅🔗 | →generator_settlement_bill_detail |

### generator_settlement_payment_allocation_gh
**定义**：广汇站点分表：付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） ｜ **流角色**：付款→结算明细分摊（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `payment_record_id` | bigint | Y | MUL | 付款记录；→generator_payment_record_gh | ✅🔗 | →generator_payment_record_gh |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail_gh | ✅🔗 | →generator_settlement_bill_detail_gh |

### generator_settlement_payment_allocation_tf
**定义**：泰峰站点分表：付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） ｜ **流角色**：付款→结算明细分摊（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `payment_record_id` | bigint | Y | MUL | 付款记录；→generator_payment_record_tf | ✅🔗 | →generator_payment_record_tf |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail_tf | ✅🔗 | →generator_settlement_bill_detail_tf |

### generator_settlement_payment_allocation_zt
**定义**：治通站点分表：付款记录到结算单行的分摊表，实现一笔付款拆分到多条结算明细（未启用） ｜ **流角色**：付款→结算明细分摊（未启用） ｜ **代码**：`generator/settlement_bill/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 分摊金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `payment_record_id` | bigint | Y | MUL | 付款记录；→generator_payment_record_zt | ✅🔗 | →generator_payment_record_zt |
| `settlement_bill_detail_id` | bigint | Y | MUL | 结算单明细；→generator_settlement_bill_detail_zt | ✅🔗 | →generator_settlement_bill_detail_zt |
