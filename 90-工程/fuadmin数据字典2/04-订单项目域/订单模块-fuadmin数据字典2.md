---
title: 订单模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 04-订单项目域
tags: [工程, 数据字典2, 代码实证, 订单]
---

# 订单模块 · fuadmin 数据字典2（代码实证版）
> 域: 04-订单项目域 | 表数: 5 | 字段: 62 | 代码锚定: 62(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/04-订单项目域/订单模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_customer_order` | 客户发货订单主表: 产品/总数量/总箱数/送货日期地点,判定发货完成 | 2361 | 💻 |
| `generator_order_detail_document_mapping` | 采购订单明细↔附件单据关联表(到货凭证) | 4899 | 💻 |
| `generator_order_detail_document_mapping_gh` | 采购订单明细↔附件关联表(广汇分表) | 133 | 💻 |
| `generator_order_detail_document_mapping_tf` | 采购订单明细↔附件关联表(泰峰分表) | 26 | 💻 |
| `generator_order_detail_document_mapping_zt` | 采购订单明细↔附件关联表(治通分表)(未启用) | 0 | 💻 |

---

### generator_customer_order
**定义**：客户发货订单主表: 产品/总数量/总箱数/送货日期地点,判定发货完成 ｜ **流角色**：订单交付链起点 ｜ **代码**：`generator/customer_order/model.py` ｜ **行数(估)**：2361

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `image` | varchar(255) | Y | - | 图片 | ✅ |  |
| `count` | int | Y | - | 总数量 | ✅ |  |
| `box_number` | int | Y | - | 总箱数 | ✅ |  |
| `number` | int | Y | - | 装箱量 | ✅ |  |
| `product_name` | varchar(20) | Y | - | 产品名称 | ✅ |  |
| `customer_name` | varchar(30) | Y | - | 客户名称 | ✅ |  |
| `site` | varchar(30) | Y | - | 送货地点 | ✅ |  |
| `date` | date | Y | - | 送货日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `customer_order_number` | varchar(30) | Y | - | 客户订单号 | ✅ |  |
| `order_state` | tinyint(1) | Y | - | 订单状态；True表示已完成，False表示未完成 | ✅💬 |  |

### generator_order_detail_document_mapping
**定义**：采购订单明细↔附件单据关联表(到货凭证) ｜ **流角色**：采购链-到货凭证关联 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：4899

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `document_id` | bigint | N | MUL | 附件；→generator_purchase_order_document | ✅🔗 | →generator_purchase_order_document |
| `purchase_order_detail_id` | bigint | N | MUL | 采购订单明细；→generator_purchase_order_detail | ✅🔗 | →generator_purchase_order_detail |
| `actual_quantity` | decimal(13,2) | Y | - | 实际到货数量 | ✅ |  |

### generator_order_detail_document_mapping_gh
**定义**：采购订单明细↔附件关联表(广汇分表) ｜ **流角色**：采购链-到货凭证关联 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：133

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `actual_quantity` | decimal(13,2) | Y | - | 实际到货数量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `document_id` | bigint | N | MUL | 附件；→generator_purchase_order_document_gh | ✅🔗 | →generator_purchase_order_document_gh |
| `purchase_order_detail_id` | bigint | N | MUL | 采购订单明细；→generator_purchase_order_detail_gh | ✅🔗 | →generator_purchase_order_detail_gh |

### generator_order_detail_document_mapping_tf
**定义**：采购订单明细↔附件关联表(泰峰分表) ｜ **流角色**：采购链-到货凭证关联 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：26

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `actual_quantity` | decimal(13,2) | Y | - | 实际到货数量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `document_id` | bigint | N | MUL | 附件；→generator_purchase_order_document_tf | ✅🔗 | →generator_purchase_order_document_tf |
| `purchase_order_detail_id` | bigint | N | MUL | 采购订单明细；→generator_purchase_order_detail_tf | ✅🔗 | →generator_purchase_order_detail_tf |

### generator_order_detail_document_mapping_zt
**定义**：采购订单明细↔附件关联表(治通分表)(未启用) ｜ **流角色**：采购链-到货凭证关联 ｜ **代码**：`generator/purchase_order_document/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `actual_quantity` | decimal(13,2) | Y | - | 实际到货数量 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `document_id` | bigint | N | MUL | 附件；→generator_purchase_order_document_zt | ✅🔗 | →generator_purchase_order_document_zt |
| `purchase_order_detail_id` | bigint | N | MUL | 采购订单明细；→generator_purchase_order_detail_zt | ✅🔗 | →generator_purchase_order_detail_zt |

---

## 同域兄弟模块
- [[04-订单项目域/客户模块-fuadmin数据字典2|客户模块]]
- [[04-订单项目域/财务模块-fuadmin数据字典2|财务模块]]
- [[04-订单项目域/项目模块-fuadmin数据字典2|项目模块]]
- [[04-订单项目域/04-订单项目域-业务流|04-订单项目域业务流(代码验证版)]]
