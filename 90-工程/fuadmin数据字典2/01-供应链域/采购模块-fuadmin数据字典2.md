---
title: 采购模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 01-供应链域
tags: [工程, 数据字典2, 代码实证, 采购]
---

# 采购模块 · fuadmin 数据字典2（代码实证版）
> 域: 01-供应链域 | 表数: 43 | 字段: 1062 | 代码锚定: 985(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/01-供应链域/采购模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_historicalpurchaseorder` | 采购订单历史表：django-simple-history自动记录的变更快照，ope | 2465 | 📸 |
| `generator_historicalpurchaseorderdetail` | 采购订单明细历史表：django-simple-history自动记录的变更快照，o | 4039 | 📸 |
| `generator_historicalpurchaseorderdetailgh` | 采购订单明细历史表：django-simple-history自动记录的变更快照，o | 1161 | 📸 |
| `generator_historicalpurchaseorderdetailtf` | 采购订单明细历史表：django-simple-history自动记录的变更快照，o | 206 | 📸 |
| `generator_historicalpurchaseorderdetailzt` | 采购订单明细历史表：django-simple-history自动记录的变更快照，o | 0 | 📸 |
| `generator_historicalpurchaseordergh` | 采购订单历史表：django-simple-history自动记录的变更快照，ope | 919 | 📸 |
| `generator_historicalpurchaseordertf` | 采购订单历史表：django-simple-history自动记录的变更快照，ope | 250 | 📸 |
| `generator_historicalpurchaseorderzt` | 采购订单历史表：django-simple-history自动记录的变更快照，ope | 0 | 📸 |
| `generator_historicalpurchaserequisition` | 采购申请单历史表：django-simple-history自动记录的变更快照，op | 303 | 📸 |
| `generator_historicalpurchaserequisitiondetail` | 采购申请明细历史表：django-simple-history自动记录的变更快照，o | 1250 | 📸 |
| `generator_historicalpurchaserequisitiondetailgh` | 采购申请明细历史表：django-simple-history自动记录的变更快照，o | 0 | 📸 |
| `generator_historicalpurchaserequisitiondetailtf` | 采购申请明细历史表：django-simple-history自动记录的变更快照，o | 0 | 📸 |
| `generator_historicalpurchaserequisitiondetailzt` | 采购申请明细历史表：django-simple-history自动记录的变更快照，o | 0 | 📸 |
| `generator_historicalpurchaserequisitiongh` | 采购申请单历史表：django-simple-history自动记录的变更快照，op | 0 | 📸 |
| `generator_historicalpurchaserequisitiontf` | 采购申请单历史表：django-simple-history自动记录的变更快照，op | 0 | 📸 |
| `generator_historicalpurchaserequisitionzt` | 采购申请单历史表：django-simple-history自动记录的变更快照，op | 0 | 📸 |
| `generator_purchase_material` | 采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 | 723 | 💻 |
| `generator_purchase_material_gh` | 广汇站点分表：采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 | 176 | 💻 |
| `generator_purchase_material_tf` | 泰峰站点分表：采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 | 54 | 💻 |
| `generator_purchase_material_zt` | 治通站点分表：采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 | 19554 | 💻 |
| `generator_purchase_order` | 采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进度 | 1013 | 💻 |
| `generator_purchase_order_copy1` | 采购订单站点副本表(copy1)：数据库层复制的备份，代码无对应模型，不参与在线业务 | 678 | 🏭 |
| `generator_purchase_order_detail` | 采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 | 2630 | 💻 |
| `generator_purchase_order_detail_copy1` | 采购订单明细站点副本表(copy1)：数据库层复制的备份，代码无对应模型，不参与在线 | 1763 | 🏭 |
| `generator_purchase_order_detail_gh` | 广汇站点分表：采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 | 176 | 💻 |
| `generator_purchase_order_detail_tf` | 泰峰站点分表：采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 | 46 | 💻 |
| `generator_purchase_order_detail_zt` | 治通站点分表：采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 | 0 | 💻 |
| `generator_purchase_order_document` | 采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 | 1633 | 💻 |
| `generator_purchase_order_document_copy1` | 采购订单附件站点副本表(copy1)：数据库层复制的备份，代码无对应模型，不参与在线 | 1040 | 🏭 |
| `generator_purchase_order_document_gh` | 广汇站点分表：采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 | 70 | 💻 |
| `generator_purchase_order_document_tf` | 泰峰站点分表：采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 | 23 | 💻 |
| `generator_purchase_order_document_zt` | 治通站点分表：采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 | 0 | 💻 |
| `generator_purchase_order_gh` | 广汇站点分表：采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进 | 73 | 💻 |
| `generator_purchase_order_tf` | 泰峰站点分表：采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进 | 27 | 💻 |
| `generator_purchase_order_zt` | 治通站点分表：采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进 | 0 | 💻 |
| `generator_purchase_requisition` | 员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门创建 | 380 | 💻 |
| `generator_purchase_requisition_detail` | 采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 | 2810 | 💻 |
| `generator_purchase_requisition_detail_gh` | 广汇站点分表：采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 | 0 | 💻 |
| `generator_purchase_requisition_detail_tf` | 泰峰站点分表：采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 | 0 | 💻 |
| `generator_purchase_requisition_detail_zt` | 治通站点分表：采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 | 0 | 💻 |
| `generator_purchase_requisition_gh` | 广汇站点分表：员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门 | 0 | 💻 |
| `generator_purchase_requisition_tf` | 泰峰站点分表：员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门 | 0 | 💻 |
| `generator_purchase_requisition_zt` | 治通站点分表：员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门 | 0 | 💻 |

---

### generator_historicalpurchaseorder
**定义**：采购订单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：2465

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaseorderdetail
**定义**：采购订单明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：4039

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量（界面:单位） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping | ✅🔗 | →generator_supplier_material_mapping |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_historicalpurchaseorderdetailgh
**定义**：采购订单明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：1161

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量（界面:单位） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_gh（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_gh |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_gh（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_gh |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_gh | ✅🔗 | →generator_supplier_material_mapping_gh |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_historicalpurchaseorderdetailtf
**定义**：采购订单明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：206

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量（界面:单位） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_tf（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_tf |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_tf（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_tf |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_tf | ✅🔗 | →generator_supplier_material_mapping_tf |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_historicalpurchaseorderdetailzt
**定义**：采购订单明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量（界面:单位） | ✅🖥️ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_zt（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_zt |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_zt（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_zt |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_zt | ✅🔗 | →generator_supplier_material_mapping_zt |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_historicalpurchaseordergh
**定义**：采购订单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：919

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaseordertf
**定义**：采购订单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：250

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaseorderzt
**定义**：采购订单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisition
**定义**：采购申请单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：303

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号（界面:申请单号） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisitiondetail
**定义**：采购申请明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：1250

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请（界面:申请状态） | 💬⚖️🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisitiondetailgh
**定义**：采购申请明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请（界面:申请状态） | 💬⚖️🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_gh（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_gh |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisitiondetailtf
**定义**：采购申请明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请（界面:申请状态） | 💬⚖️🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_tf（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_tf |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisitiondetailzt
**定义**：采购申请明细历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请（界面:申请状态） | 💬⚖️🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_zt（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_zt |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisitiongh
**定义**：采购申请单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号（界面:申请单号） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisitiontf
**定义**：采购申请单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号（界面:申请单号） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_historicalpurchaserequisitionzt
**定义**：采购申请单历史表：django-simple-history自动记录的变更快照，operation_id归组同次操作 ｜ **流角色**：审计回溯：变更历史快照 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号（界面:申请单号） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `operation_id` | varchar(36) | Y | MUL | [推断]历史操作分组UUID，同一次操作跨表历史记录共享 | 🔍 |  |
| `operation_label` | varchar(100) | Y | - | [推断]历史操作标签（如新建/修改/取消申请） | 🔍 |  |

### generator_purchase_material
**定义**：采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 ｜ **流角色**：物料主数据：采购目录 ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：723

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:物料条码） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_unit` | varchar(10) | Y | - | 库存单位 | ✅ |  |
| `safety_stock` | decimal(13,2) | Y | - | 库存警戒线 | ✅ |  |
| `cost` | decimal(15,4) | Y | - | 成本 | ✅ |  |
| `standard_price` | decimal(15,4) | Y | - | 标价 | ✅ |  |
| `processing_product` | varchar(50) | Y | - | 加工产品 | ✅ |  |
| `product_type` | varchar(50) | Y | - | 产品类型 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `material_qrcode` | varchar(50) | Y | - | 物料条码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `internal_category` | varchar(50) | Y | - | 内部分类 | ✅ |  |
| `material_attachments` | json | Y | - | 物料附件 | ✅ |  |

### generator_purchase_material_gh
**定义**：广汇站点分表：采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 ｜ **流角色**：物料主数据：采购目录 ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：176

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_unit` | varchar(10) | Y | - | 库存单位 | ✅ |  |
| `safety_stock` | decimal(13,2) | Y | - | 库存警戒线 | ✅ |  |
| `cost` | decimal(15,4) | Y | - | 成本 | ✅ |  |
| `standard_price` | decimal(15,4) | Y | - | 标价 | ✅ |  |
| `internal_category` | varchar(50) | Y | - | 内部分类 | ✅ |  |
| `processing_product` | varchar(50) | Y | - | 加工产品 | ✅ |  |
| `product_type` | varchar(50) | Y | - | 产品类型 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `material_qrcode` | varchar(50) | Y | - | 物料条码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `material_attachments` | json | Y | - | 物料附件 | ✅ |  |

### generator_purchase_material_tf
**定义**：泰峰站点分表：采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 ｜ **流角色**：物料主数据：采购目录 ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：54

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_unit` | varchar(10) | Y | - | 库存单位 | ✅ |  |
| `safety_stock` | decimal(13,2) | Y | - | 库存警戒线 | ✅ |  |
| `cost` | decimal(15,4) | Y | - | 成本 | ✅ |  |
| `standard_price` | decimal(15,4) | Y | - | 标价 | ✅ |  |
| `internal_category` | varchar(50) | Y | - | 内部分类 | ✅ |  |
| `processing_product` | varchar(50) | Y | - | 加工产品 | ✅ |  |
| `product_type` | varchar(50) | Y | - | 产品类型 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `material_qrcode` | varchar(50) | Y | - | 物料条码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `material_attachments` | json | Y | - | 物料附件 | ✅ |  |

### generator_purchase_material_zt
**定义**：治通站点分表：采购物料主数据，记录物料名称、规格、品牌、安全库存、标准价与成本 ｜ **流角色**：物料主数据：采购目录 ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：19554

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `stock_unit` | varchar(10) | Y | - | 库存单位 | ✅ |  |
| `safety_stock` | decimal(13,2) | Y | - | 库存警戒线 | ✅ |  |
| `cost` | decimal(15,4) | Y | - | 成本 | ✅ |  |
| `standard_price` | decimal(15,4) | Y | - | 标价 | ✅ |  |
| `internal_category` | varchar(50) | Y | - | 内部分类 | ✅ |  |
| `processing_product` | varchar(50) | Y | - | 加工产品 | ✅ |  |
| `product_type` | varchar(50) | Y | - | 产品类型 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `material_qrcode` | varchar(50) | Y | - | 物料条码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `material_attachments` | json | Y | - | 物料附件 | ✅ |  |

### generator_purchase_order
**定义**：采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进度 ｜ **流角色**：采购链核心：订单头 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：1013

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:订单类型） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请（界面:到货状态） | 💬⚖️🖥️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总金额） | ✅🖥️ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |

### generator_purchase_order_copy1
**定义**：采购订单站点副本表(copy1)：数据库层复制的备份，代码无对应模型，不参与在线业务 ｜ **流角色**：备份副本：非在线业务表 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：678

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |

### generator_purchase_order_detail
**定义**：采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 ｜ **流角色**：订单行：执行与到货跟踪 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：2630

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:采购订单） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价（界面:含税单价(元)） | ✅🖥️ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称（界面:请选择或输入项目名称） | ✅🖥️ |  |
| `project_number` | varchar(50) | Y | - | 项目号（界面:请选择或输入项目号） | ✅🖥️ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间（界面:预计交付时间(天)） | ✅🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping | ✅🔗 | →generator_supplier_material_mapping |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量 | ✅ |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_purchase_order_detail_copy1
**定义**：采购订单明细站点副本表(copy1)：数据库层复制的备份，代码无对应模型，不参与在线业务 ｜ **流角色**：备份副本：非在线业务表 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：1763

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
| `belong` | varchar(50) | Y | - | [推断]待确认:归属（站点/部门归属） | 🔍 |  |
| `practical_date` | date | Y | - | [推断]实际到货日期，对照predict_date预计到货日期 | 🔍 |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(50) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(50) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping | ✅🔗 | →generator_supplier_material_mapping |

### generator_purchase_order_detail_gh
**定义**：广汇站点分表：采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 ｜ **流角色**：订单行：执行与到货跟踪 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：176

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_gh（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_gh |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_gh（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_gh |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_gh | ✅🔗 | →generator_supplier_material_mapping_gh |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量（界面:单位） | ✅🖥️ |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_purchase_order_detail_tf
**定义**：泰峰站点分表：采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 ｜ **流角色**：订单行：执行与到货跟踪 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：46

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_tf（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_tf |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_tf（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_tf |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_tf | ✅🔗 | →generator_supplier_material_mapping_tf |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量（界面:单位） | ✅🖥️ |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_purchase_order_detail_zt
**定义**：治通站点分表：采购订单行，回链申请行并按协议价映射定价，跟踪到货状态与累计入库数量 ｜ **流角色**：订单行：执行与到货跟踪 ｜ **代码**：`generator/purchase_order_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `state` | int | Y | - | 到货状态；1000退换货 1未到货 2全部到货 3部分到货 100取消申请 | 💬⚖️ |  |
| `predict_date` | date | Y | - | 预计到货日期 | ✅ |  |
| `predict_days` | smallint unsigned | Y | - | 预计交付时间 | ✅ |  |
| `amount` | decimal(13,2) | Y | - | 总价（界面:金额） | ✅🖥️ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点（界面:税点(%)） | ✅🖥️ |  |
| `unit_price` | decimal(15,4) | Y | - | 含税单价 | ✅ |  |
| `applicant` | varchar(20) | Y | - | 采购申请人（界面:请购人） | ✅🖥️ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `purchase_requisition_detail_id` | bigint | Y | - | 采购申请单明细ID（界面:采购申请明细ID） | ✅🖥️ | →generator_purchase_requisition_detail(推断) |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_zt（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_zt |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_zt（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_zt |
| `supplier_material_map_id` | bigint | Y | MUL | 关联供应商物料；指向供应商-物料报价记录；→generator_supplier_material_mapping_zt | ✅🔗 | →generator_supplier_material_mapping_zt |
| `stock_quantity` | decimal(13,2) | Y | - | 入库数量（界面:单位） | ✅🖥️ |  |
| `settlement_status` | int | Y | - | 结算状态；0未结算 1部分结算 2已全部结算 | ✅ |  |

### generator_purchase_order_document
**定义**：采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 ｜ **流角色**：订单凭证：合同/发票附件 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：1633

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:附件编号） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `doc_type` | varchar(20) | Y | - | 附件类型 | ✅ |  |
| `doc_number` | varchar(255) | Y | - | 附件编号；如发票号等 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 附件总金额（界面:税后附件总额） | ✅🖥️ |  |
| `file_url` | json | Y | - | 附件URL（界面:上传附件） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `signing_date` | date | Y | - | 签订日期 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 待付金额 | ✅ |  |
| `state` | int | Y | - | 支付状态；0草稿 1未支付 2部分支付 3全部支付 | 💬⚖️ |  |

### generator_purchase_order_document_copy1
**定义**：采购订单附件站点副本表(copy1)：数据库层复制的备份，代码无对应模型，不参与在线业务 ｜ **流角色**：备份副本：非在线业务表 ｜ **类型**：🏭站点复制 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：1040

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `doc_type` | varchar(20) | Y | - | 附件类型 | ✅ |  |
| `doc_number` | varchar(255) | Y | - | 附件编号；如发票号等 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 附件总金额 | ✅ |  |
| `file_url` | json | Y | - | 附件URL（界面:上传附件） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_purchase_order_document_gh
**定义**：广汇站点分表：采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 ｜ **流角色**：订单凭证：合同/发票附件 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：70

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `doc_type` | varchar(20) | Y | - | 附件类型 | ✅ |  |
| `doc_number` | varchar(255) | Y | - | 附件编号；如发票号等 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 附件总金额 | ✅ |  |
| `file_url` | json | Y | - | 附件URL（界面:上传附件） | ✅🖥️ |  |
| `signing_date` | date | Y | - | 签订日期 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 待付金额（界面:未付金额） | ✅🖥️ |  |
| `state` | int | Y | - | 支付状态；0草稿 1未支付 2部分支付 3全部支付 | 💬⚖️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_purchase_order_document_tf
**定义**：泰峰站点分表：采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 ｜ **流角色**：订单凭证：合同/发票附件 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：23

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `doc_type` | varchar(20) | Y | - | 附件类型 | ✅ |  |
| `doc_number` | varchar(255) | Y | - | 附件编号；如发票号等 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 附件总金额 | ✅ |  |
| `file_url` | json | Y | - | 附件URL（界面:上传附件） | ✅🖥️ |  |
| `signing_date` | date | Y | - | 签订日期 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 待付金额（界面:未付金额） | ✅🖥️ |  |
| `state` | int | Y | - | 支付状态；0草稿 1未支付 2部分支付 3全部支付 | 💬⚖️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_purchase_order_document_zt
**定义**：治通站点分表：采购订单附件（合同/发票等）凭证表，记录附件类型、编号、金额与支付状态 ｜ **流角色**：订单凭证：合同/发票附件 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `doc_type` | varchar(20) | Y | - | 附件类型 | ✅ |  |
| `doc_number` | varchar(255) | Y | - | 附件编号；如发票号等 | ✅ |  |
| `total_amount` | decimal(13,2) | Y | - | 附件总金额 | ✅ |  |
| `file_url` | json | Y | - | 附件URL（界面:上传附件） | ✅🖥️ |  |
| `signing_date` | date | Y | - | 签订日期 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 待付金额（界面:未付金额） | ✅🖥️ |  |
| `state` | int | Y | - | 支付状态；0草稿 1未支付 2部分支付 3全部支付 | 💬⚖️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |

### generator_purchase_order_gh
**定义**：广汇站点分表：采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进度 ｜ **流角色**：采购链核心：订单头 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：73

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |

### generator_purchase_order_tf
**定义**：泰峰站点分表：采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进度 ｜ **流角色**：采购链核心：订单头 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：27

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |

### generator_purchase_order_zt
**定义**：治通站点分表：采购员根据申请单下达的采购订单头，记录供应商、总价、结算方式与收付款进度 ｜ **流角色**：采购链核心：订单头 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `order_belong` | varchar(30) | Y | - | 订单归属 | ✅ |  |
| `total_price` | decimal(13,2) | Y | - | 总价（界面:总价(元)） | ✅🖥️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `order_number` | varchar(50) | Y | - | 采购订单编号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `paid_amount` | decimal(13,2) | Y | - | 已付金额 | ✅ |  |
| `due_amount` | decimal(13,2) | Y | - | 未付金额 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `order_type` | int | Y | - | 订单类型；0普通 1紧急 | 💬⚖️ |  |

### generator_purchase_requisition
**定义**：员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门创建 ｜ **流角色**：采购链起点：申请单头 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：380

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:物料名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间（界面:申请时间） | ✅📦🖥️ |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |

### generator_purchase_requisition_detail
**定义**：采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 ｜ **流角色**：申请行：物料需求明细 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：2810

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:采购申请编号） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称（界面:请选择或输入项目名称） | ✅🖥️ |  |
| `project_number` | varchar(50) | Y | - | 项目号（界面:请选择或输入项目号） | ✅🖥️ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请 | 💬⚖️ |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |

### generator_purchase_requisition_detail_gh
**定义**：广汇站点分表：采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 ｜ **流角色**：申请行：物料需求明细 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请（界面:申请状态） | 💬⚖️🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_gh（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_gh |

### generator_purchase_requisition_detail_tf
**定义**：泰峰站点分表：采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 ｜ **流角色**：申请行：物料需求明细 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请（界面:申请状态） | 💬⚖️🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_tf（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_tf |

### generator_purchase_requisition_detail_zt
**定义**：治通站点分表：采购申请行，记录物料名称/规格/数量/需求时间及项目归属，挂申请单 ｜ **流角色**：申请行：物料需求明细 ｜ **代码**：`generator/purchase_requisition_detail/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `operation_reason` | varchar(255) | Y | - | 操作原因 | ✅ |  |
| `requisition_state` | int | Y | - | 申请明细状态；0假删除 1正常采购 100取消申请（界面:申请状态） | 💬⚖️🖥️ |  |
| `delivery_address` | varchar(255) | Y | - | 送货地址 | ✅ |  |
| `required_time` | date | Y | - | 需求时间 | ✅ |  |
| `picture` | json | Y | - | 图片（界面:图片信息） | ✅🖥️ |  |
| `approval_comment` | varchar(255) | Y | - | 审核意见 | ✅ |  |
| `project_name` | varchar(50) | Y | - | 项目名称 | ✅ |  |
| `project_number` | varchar(50) | Y | - | 项目号 | ✅ |  |
| `material_subcategory` | varchar(50) | Y | - | 物料子类 | ✅ |  |
| `material_category` | varchar(20) | Y | - | 物料大类 | ✅ |  |
| `quantity` | decimal(13,2) | Y | - | 数量 | ✅ |  |
| `unit` | varchar(10) | Y | - | 单位 | ✅ |  |
| `brand` | varchar(20) | Y | - | 品牌 | ✅ |  |
| `config_requirement` | varchar(255) | Y | - | 配置要求 | ✅ |  |
| `specification` | varchar(255) | Y | - | 物料规格型号 | ✅ |  |
| `material_name` | varchar(255) | Y | - | 物料名称（界面:产品名称） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `purchase_requisition_id` | bigint | Y | MUL | 采购申请单；→generator_purchase_requisition_zt（界面:采购申请ID） | ✅🔗🖥️ | →generator_purchase_requisition_zt |

### generator_purchase_requisition_gh
**定义**：广汇站点分表：员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门创建 ｜ **流角色**：采购链起点：申请单头 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号（界面:申请单号） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |

### generator_purchase_requisition_tf
**定义**：泰峰站点分表：员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门创建 ｜ **流角色**：采购链起点：申请单头 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号（界面:申请单号） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |

### generator_purchase_requisition_zt
**定义**：治通站点分表：员工发起的采购申请单头，记录申请编号、原因、类型与审批状态，由需求部门创建 ｜ **流角色**：采购链起点：申请单头 ｜ **代码**：`generator/purchase_requisition/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `requisition_reason` | int | Y | - | 申请原因；0项目需求 1设计变更 2功能新增 3漏买 4办公用品 5备件耗材 6其他 | 💬⚖️ |  |
| `state` | int | Y | - | 审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请 | 💬⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `requisition_number` | varchar(50) | Y | - | 采购申请编号（界面:申请单号） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，外键关联system_users.id | 🔍 |  |
| `requisition_type` | int | Y | - | 申请单类型；0普通 1紧急 | 💬⚖️ |  |
