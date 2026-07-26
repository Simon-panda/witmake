---
title: 供应商模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 01-供应链域
tags: [工程, 数据字典2, 代码实证, 供应商]
---

# 供应商模块 · fuadmin 数据字典2（代码实证版）
> 域: 01-供应链域 | 表数: 8 | 字段: 164 | 代码锚定: 164(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/01-供应链域/供应商模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_supplier` | 供应商主档：采购员维护的供应商资质、联系方式、银行账户、结算方式与代理品牌，供采购订 | 210 | 💻 |
| `generator_supplier_gh` | 供应商（广汇站点分表）：同主表，站点隔离的供应商主数据 | 43 | 💻 |
| `generator_supplier_material_mapping` | 供应商-物料价格中间表：维护供应商对采购物料的税后单价、税点、最少采购量与有效期，供 | 806 | 💻 |
| `generator_supplier_material_mapping_gh` | 供应商-物料价格中间表（广汇站点分表）：同主表，站点隔离的报价记录 | 183 | 💻 |
| `generator_supplier_material_mapping_tf` | 供应商-物料价格中间表（泰峰站点分表）：同主表，站点隔离的报价记录 | 54 | 💻 |
| `generator_supplier_material_mapping_zt` | 供应商-物料价格中间表（治通站点分表）：同主表，站点隔离的报价记录 | 23060 | 💻 |
| `generator_supplier_tf` | 供应商（泰峰站点分表）：同主表，站点隔离的供应商主数据 | 42 | 💻 |
| `generator_supplier_zt` | 供应商（治通站点分表）：同主表，站点隔离的供应商主数据 | 1467 | 💻 |

---

### generator_supplier
**定义**：供应商主档：采购员维护的供应商资质、联系方式、银行账户、结算方式与代理品牌，供采购订单与付款引用；无独立评价表 ｜ **流角色**：供应商主数据 ｜ **代码**：`generator/supplier/model.py` ｜ **行数(估)**：210

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | Y | - | 状态 | ✅ |  |
| `company_documents` | json | Y | - | 公司资料 | ✅ |  |
| `represented_brands` | varchar(255) | Y | - | 代理品牌 | ✅ |  |
| `has_signed_agreement` | tinyint(1) | Y | - | 是否签订协议 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `category` | varchar(50) | Y | - | 类别 | ✅ |  |
| `business_scope` | varchar(255) | Y | - | 经营范围 | ✅ |  |
| `contact_phone` | varchar(50) | Y | - | 联系电话 | ✅ |  |
| `contact_person` | varchar(20) | Y | - | 联系人 | ✅ |  |
| `address` | varchar(255) | Y | - | 地址 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `use_dept` | varchar(30) | Y | - | 使用范围 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `supplier_code` | varchar(50) | Y | - | 供应商代码 | ✅ |  |
| `email` | varchar(50) | Y | - | 电子邮箱 | ✅ |  |

### generator_supplier_gh
**定义**：供应商（广汇站点分表）：同主表，站点隔离的供应商主数据 ｜ **流角色**：供应商主数据(广汇) ｜ **代码**：`generator/supplier/model.py` ｜ **行数(估)**：43

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | Y | - | 状态 | ✅ |  |
| `company_documents` | json | Y | - | 公司资料 | ✅ |  |
| `represented_brands` | varchar(255) | Y | - | 代理品牌 | ✅ |  |
| `has_signed_agreement` | tinyint(1) | Y | - | 是否签订协议 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `category` | varchar(50) | Y | - | 类别 | ✅ |  |
| `business_scope` | varchar(255) | Y | - | 经营范围 | ✅ |  |
| `email` | varchar(50) | Y | - | 电子邮箱 | ✅ |  |
| `contact_phone` | varchar(50) | Y | - | 联系电话 | ✅ |  |
| `contact_person` | varchar(20) | Y | - | 联系人 | ✅ |  |
| `address` | varchar(255) | Y | - | 地址 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `supplier_code` | varchar(50) | Y | - | 供应商代码 | ✅ |  |
| `use_dept` | varchar(30) | Y | - | 使用范围 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_supplier_material_mapping
**定义**：供应商-物料价格中间表：维护供应商对采购物料的税后单价、税点、最少采购量与有效期，供采购询价与订单取价 ｜ **流角色**：供应商报价维护 ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：806

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `unit_price` | decimal(15,4) | Y | - | 税后单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `period_type` | varchar(50) | Y | - | 类型 | ✅ |  |
| `unit` | varchar(10) | Y | - | 采购单位 | ✅ |  |
| `start_date` | date | Y | - | 开始时间 | ✅ |  |
| `end_date` | date | Y | - | 结束时间 | ✅ |  |
| `min_order_quantity` | decimal(13,2) | Y | - | 最少采购数量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `purchase_material_id` | bigint | N | MUL | 采购物料；→generator_purchase_material | ✅🔗 | →generator_purchase_material |
| `supplier_id` | bigint | N | MUL | 供应商；→generator_supplier | ✅🔗 | →generator_supplier |

### generator_supplier_material_mapping_gh
**定义**：供应商-物料价格中间表（广汇站点分表）：同主表，站点隔离的报价记录 ｜ **流角色**：供应商报价维护(广汇) ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：183

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `unit_price` | decimal(15,4) | Y | - | 税后单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `period_type` | varchar(50) | Y | - | 类型 | ✅ |  |
| `unit` | varchar(10) | Y | - | 采购单位 | ✅ |  |
| `start_date` | date | Y | - | 开始时间 | ✅ |  |
| `end_date` | date | Y | - | 结束时间 | ✅ |  |
| `min_order_quantity` | decimal(13,2) | Y | - | 最少采购数量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `purchase_material_id` | bigint | N | MUL | 采购物料；→generator_purchase_material_gh | ✅🔗 | →generator_purchase_material_gh |
| `supplier_id` | bigint | N | MUL | 供应商；→generator_supplier_gh | ✅🔗 | →generator_supplier_gh |

### generator_supplier_material_mapping_tf
**定义**：供应商-物料价格中间表（泰峰站点分表）：同主表，站点隔离的报价记录 ｜ **流角色**：供应商报价维护(泰峰) ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：54

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `unit_price` | decimal(15,4) | Y | - | 税后单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `period_type` | varchar(50) | Y | - | 类型 | ✅ |  |
| `unit` | varchar(10) | Y | - | 采购单位 | ✅ |  |
| `start_date` | date | Y | - | 开始时间 | ✅ |  |
| `end_date` | date | Y | - | 结束时间 | ✅ |  |
| `min_order_quantity` | decimal(13,2) | Y | - | 最少采购数量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `purchase_material_id` | bigint | N | MUL | 采购物料；→generator_purchase_material_tf | ✅🔗 | →generator_purchase_material_tf |
| `supplier_id` | bigint | N | MUL | 供应商；→generator_supplier_tf | ✅🔗 | →generator_supplier_tf |

### generator_supplier_material_mapping_zt
**定义**：供应商-物料价格中间表（治通站点分表）：同主表，站点隔离的报价记录 ｜ **流角色**：供应商报价维护(治通) ｜ **代码**：`generator/purchase_material/model.py` ｜ **行数(估)**：23060

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `unit_price` | decimal(15,4) | Y | - | 税后单价 | ✅ |  |
| `tax_rate` | decimal(6,2) | Y | - | 税点 | ✅ |  |
| `period_type` | varchar(50) | Y | - | 类型 | ✅ |  |
| `unit` | varchar(10) | Y | - | 采购单位 | ✅ |  |
| `start_date` | date | Y | - | 开始时间 | ✅ |  |
| `end_date` | date | Y | - | 结束时间 | ✅ |  |
| `min_order_quantity` | decimal(13,2) | Y | - | 最少采购数量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `purchase_material_id` | bigint | N | MUL | 采购物料；→generator_purchase_material_zt | ✅🔗 | →generator_purchase_material_zt |
| `supplier_id` | bigint | N | MUL | 供应商；→generator_supplier_zt | ✅🔗 | →generator_supplier_zt |

### generator_supplier_tf
**定义**：供应商（泰峰站点分表）：同主表，站点隔离的供应商主数据 ｜ **流角色**：供应商主数据(泰峰) ｜ **代码**：`generator/supplier/model.py` ｜ **行数(估)**：42

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | Y | - | 状态 | ✅ |  |
| `company_documents` | json | Y | - | 公司资料 | ✅ |  |
| `represented_brands` | varchar(255) | Y | - | 代理品牌 | ✅ |  |
| `has_signed_agreement` | tinyint(1) | Y | - | 是否签订协议 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `category` | varchar(50) | Y | - | 类别 | ✅ |  |
| `business_scope` | varchar(255) | Y | - | 经营范围 | ✅ |  |
| `email` | varchar(50) | Y | - | 电子邮箱 | ✅ |  |
| `contact_phone` | varchar(50) | Y | - | 联系电话 | ✅ |  |
| `contact_person` | varchar(20) | Y | - | 联系人 | ✅ |  |
| `address` | varchar(255) | Y | - | 地址 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `supplier_code` | varchar(50) | Y | - | 供应商代码 | ✅ |  |
| `use_dept` | varchar(30) | Y | - | 使用范围 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_supplier_zt
**定义**：供应商（治通站点分表）：同主表，站点隔离的供应商主数据 ｜ **流角色**：供应商主数据(治通) ｜ **代码**：`generator/supplier/model.py` ｜ **行数(估)**：1467

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | Y | - | 状态 | ✅ |  |
| `company_documents` | json | Y | - | 公司资料 | ✅ |  |
| `represented_brands` | varchar(255) | Y | - | 代理品牌 | ✅ |  |
| `has_signed_agreement` | tinyint(1) | Y | - | 是否签订协议 | ✅ |  |
| `payment_term` | varchar(50) | Y | - | 结算方式 | ✅ |  |
| `category` | varchar(50) | Y | - | 类别 | ✅ |  |
| `business_scope` | varchar(255) | Y | - | 经营范围 | ✅ |  |
| `email` | varchar(50) | Y | - | 电子邮箱 | ✅ |  |
| `contact_phone` | varchar(50) | Y | - | 联系电话 | ✅ |  |
| `contact_person` | varchar(20) | Y | - | 联系人 | ✅ |  |
| `address` | varchar(255) | Y | - | 地址 | ✅ |  |
| `deposit_bank` | varchar(50) | Y | - | 开户行 | ✅ |  |
| `bank_account` | varchar(50) | Y | - | 银行账号 | ✅ |  |
| `supplier_name` | varchar(50) | Y | - | 供应商名称 | ✅ |  |
| `supplier_code` | varchar(50) | Y | - | 供应商代码 | ✅ |  |
| `use_dept` | varchar(30) | Y | - | 使用范围 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

---

## 同域兄弟模块
- [[01-供应链域/物流模块-fuadmin数据字典2|物流模块]]
- [[01-供应链域/付款模块-fuadmin数据字典2|付款模块]]
- [[01-供应链域/采购模块-fuadmin数据字典2|采购模块]]
- [[01-供应链域/退货模块-fuadmin数据字典2|退货模块]]
- [[01-供应链域/结算模块-fuadmin数据字典2|结算模块]]
- [[01-供应链域/仓储模块-fuadmin数据字典2|仓储模块]]
- [[01-供应链域/01-供应链域-业务流|01-供应链域业务流(代码验证版)]]
