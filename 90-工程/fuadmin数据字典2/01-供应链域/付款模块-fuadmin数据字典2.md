---
title: 付款模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 01-供应链域
tags: [工程, 数据字典2, 代码实证, 付款]
---

# 付款模块 · fuadmin 数据字典2（代码实证版）
> 域: 01-供应链域 | 表数: 8 | 字段: 120 | 代码锚定: 112(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/01-供应链域/付款模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_payment_application` | 付款申请：采购员按采购订单/结算单发起付款申请（金额、账单类型、付款方式），走多级审 | 928 | 💻 |
| `generator_payment_application_gh` | 付款申请（广汇站点分表）：同主表，按站点隔离的付款申请与审批 | 13 | 💻 |
| `generator_payment_application_tf` | 付款申请（泰峰站点分表）：同主表，按站点隔离的付款申请与审批（0行，未启用） | 0 | 💻 |
| `generator_payment_application_zt` | 付款申请（治通站点分表）：同主表，按站点隔离的付款申请与审批（0行，未启用） | 0 | 💻 |
| `generator_payment_record` | 付款记录：财务对已批准付款申请录入的实际付款流水，累计不超申请金额，回写采购订单已付 | 262 | 💻 |
| `generator_payment_record_gh` | 付款记录（广汇站点分表）：同主表，站点隔离的实际付款流水 | 12 | 💻 |
| `generator_payment_record_tf` | 付款记录（泰峰站点分表）：同主表，站点隔离的实际付款流水（0行，未启用） | 0 | 💻 |
| `generator_payment_record_zt` | 付款记录（治通站点分表）：同主表，站点隔离的实际付款流水（0行，未启用） | 0 | 💻 |

---

### generator_payment_application
**定义**：付款申请：采购员按采购订单/结算单发起付款申请（金额、账单类型、付款方式），走多级审批流后供财务付款 ｜ **流角色**：付款审批入口 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：928

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `application_number` | varchar(50) | Y | UNI | 付款申请编号 | ✅ |  |
| `application_amount` | decimal(13,2) | Y | - | 申请金额 | ✅ |  |
| `state` | int | Y | - | 审批状态：0未申请/不通过 1已申请(已提交) 2审批中 3已批准 100取消申请 | ✅⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `pay_time` | date | Y | - | 付款日期 | ✅ |  |
| `bill_type` | varchar(30) | Y | - | 账单类型 | ✅ |  |
| `settlement_bill_id` | bigint | Y | - | 结算单；→generator_settlement_bill | ✅🔗 | →generator_settlement_bill |

### generator_payment_application_gh
**定义**：付款申请（广汇站点分表）：同主表，按站点隔离的付款申请与审批 ｜ **流角色**：付款审批入口(广汇) ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：13

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `application_number` | varchar(50) | Y | UNI | 付款申请编号 | ✅ |  |
| `application_amount` | decimal(13,2) | Y | - | 申请金额 | ✅ |  |
| `state` | int | Y | - | 审批状态：0未申请/不通过 1已申请(已提交) 2审批中 3已批准 100取消申请 | ✅⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `pay_time` | date | Y | - | 付款日期 | ✅ |  |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_gh（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_gh |
| `bill_type` | varchar(30) | Y | - | 账单类型 | ✅ |  |
| `settlement_bill_id` | bigint | Y | - | 结算单；→generator_settlement_bill_gh | ✅🔗 | →generator_settlement_bill_gh |

### generator_payment_application_tf
**定义**：付款申请（泰峰站点分表）：同主表，按站点隔离的付款申请与审批（0行，未启用） ｜ **流角色**：付款审批入口(泰峰) ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `application_number` | varchar(50) | Y | UNI | 付款申请编号 | ✅ |  |
| `application_amount` | decimal(13,2) | Y | - | 申请金额 | ✅ |  |
| `state` | int | Y | - | 审批状态：0未申请/不通过 1已申请(已提交) 2审批中 3已批准 100取消申请 | ✅⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `pay_time` | date | Y | - | 付款日期 | ✅ |  |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_tf（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_tf |
| `bill_type` | varchar(30) | Y | - | 账单类型 | ✅ |  |
| `settlement_bill_id` | bigint | Y | - | 结算单；→generator_settlement_bill_tf | ✅🔗 | →generator_settlement_bill_tf |

### generator_payment_application_zt
**定义**：付款申请（治通站点分表）：同主表，按站点隔离的付款申请与审批（0行，未启用） ｜ **流角色**：付款审批入口(治通) ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `application_number` | varchar(50) | Y | UNI | 付款申请编号 | ✅ |  |
| `application_amount` | decimal(13,2) | Y | - | 申请金额 | ✅ |  |
| `state` | int | Y | - | 审批状态：0未申请/不通过 1已申请(已提交) 2审批中 3已批准 100取消申请 | ✅⚖️ |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `pay_time` | date | Y | - | 付款日期 | ✅ |  |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `purchase_order_id` | bigint | Y | MUL | 采购订单；→generator_purchase_order_zt（界面:采购订单ID） | ✅🔗🖥️ | →generator_purchase_order_zt |
| `bill_type` | varchar(30) | Y | - | 账单类型 | ✅ |  |
| `settlement_bill_id` | bigint | Y | - | 结算单；→generator_settlement_bill_zt | ✅🔗 | →generator_settlement_bill_zt |

### generator_payment_record
**定义**：付款记录：财务对已批准付款申请录入的实际付款流水，累计不超申请金额，回写采购订单已付/未付金额并通知申请人 ｜ **流角色**：实际付款执行 ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：262

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 付款金额 | ✅ |  |
| `pay_time` | datetime(6) | Y | - | 付款时间 | ✅ |  |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `pay_user` | varchar(50) | Y | - | 付款人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `payment_application_id` | bigint | Y | MUL | 付款申请；→generator_payment_application | ✅🔗 | →generator_payment_application |

### generator_payment_record_gh
**定义**：付款记录（广汇站点分表）：同主表，站点隔离的实际付款流水 ｜ **流角色**：实际付款执行(广汇) ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：12

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 付款金额 | ✅ |  |
| `pay_time` | datetime(6) | Y | - | 付款时间 | ✅ |  |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `pay_user` | varchar(50) | Y | - | 付款人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `payment_application_id` | bigint | Y | MUL | 付款申请；→generator_payment_application_gh | ✅🔗 | →generator_payment_application_gh |

### generator_payment_record_tf
**定义**：付款记录（泰峰站点分表）：同主表，站点隔离的实际付款流水（0行，未启用） ｜ **流角色**：实际付款执行(泰峰) ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 付款金额 | ✅ |  |
| `pay_time` | datetime(6) | Y | - | 付款时间 | ✅ |  |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `pay_user` | varchar(50) | Y | - | 付款人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `payment_application_id` | bigint | Y | MUL | 付款申请；→generator_payment_application_tf | ✅🔗 | →generator_payment_application_tf |

### generator_payment_record_zt
**定义**：付款记录（治通站点分表）：同主表，站点隔离的实际付款流水（0行，未启用） ｜ **流角色**：实际付款执行(治通) ｜ **代码**：`generator/purchase_order/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `amount` | decimal(13,2) | Y | - | 付款金额 | ✅ |  |
| `pay_time` | datetime(6) | Y | - | 付款时间 | ✅ |  |
| `pay_method` | varchar(50) | Y | - | 付款方式 | ✅ |  |
| `pay_user` | varchar(50) | Y | - | 付款人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `payment_application_id` | bigint | Y | MUL | 付款申请；→generator_payment_application_zt | ✅🔗 | →generator_payment_application_zt |
