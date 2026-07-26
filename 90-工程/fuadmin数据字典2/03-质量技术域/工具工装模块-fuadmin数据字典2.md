---
title: 工具工装模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 工具工装]
---

# 工具工装模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 6 | 字段: 113 | 代码锚定: 110(97%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/工具工装模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_take_tool` | 生产现场从智能刀具柜领刀登记 | 44384 | 💻 |
| `generator_tool_replacement` | 刀片更换记录（机台、刀序、新旧刀供应商与条码） | 13446 | 💻 |
| `generator_tool_return_table` | 刀具使用后退返刀具柜登记（返库原因、管理员） | 34790 | 💻 |
| `generator_tool_scrap` | 刀具报废登记（报废人、报废原因） | 16936 | 💻 |
| `generator_tool_storage` | 新刀入智能刀具柜登记（管理员、柜号） | 50440 | 💻 |
| `generator_tools` | 刀具主档：条码、型号、大小分类、供应商、所属刀柜 | 1478 | 💻 |

---

### generator_take_tool
**定义**：生产现场从智能刀具柜领刀登记 ｜ **流角色**：刀具生命周期-领刀 ｜ **代码**：`generator/take_tool/model.py` ｜ **行数(估)**：44384

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | _MASK_TO_V2 | ✅ |  |
| `remarks` | longtext | Y | - | 备注 | ✅ |  |
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `cabinet_id` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `tool_borrower` | varchar(255) | Y | - | 领刀人 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier_name` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `bar_code` | varchar(255) | Y | - | 条码 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 入库时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断]从V2系统同步的时间戳（技术列） | 🔍 |  |

### generator_tool_replacement
**定义**：刀片更换记录（机台、刀序、新旧刀供应商与条码） ｜ **流角色**：刀具生命周期-换刀片 ｜ **代码**：`generator/tool_replacement/model.py` ｜ **行数(估)**：13446

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | _MASK_TO_V2 | ✅ |  |
| `remarks` | longtext | Y | - | 备注 | ✅ |  |
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `cabinet_id` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `tool_changer` | varchar(255) | Y | - | 换刀人 | ✅ |  |
| `tool_order` | varchar(255) | Y | - | 刀序 | ✅ |  |
| `machine_tool` | varchar(255) | Y | - | 机床 | ✅ |  |
| `production_line_id` | varchar(255) | Y | - | 产线 | ✅ | →generator_production_line(推断) |
| `old_tool_supplier` | varchar(255) | Y | - | 旧刀供应商 | ✅ |  |
| `old_bar_code` | varchar(255) | Y | - | 旧刀条码 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `new_tool_supplier` | varchar(255) | Y | - | 新刀供应商 | ✅ |  |
| `bar_code` | varchar(255) | Y | - | 新刀条码 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 入库时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_tool_return_table
**定义**：刀具使用后退返刀具柜登记（返库原因、管理员） ｜ **流角色**：刀具生命周期-返库 ｜ **代码**：`generator/tool_return_table/model.py` ｜ **行数(估)**：34790

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `factory_name` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `cabinet_number` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `admin` | varchar(255) | Y | - | 管理员 | ✅ |  |
| `return_reason` | varchar(255) | Y | - | 返库原因 | ✅ |  |
| `model_type` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier_name` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `barcode` | varchar(255) | Y | - | 条码 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]同步至V2系统的关联ID（技术列） | 🔍 |  |

### generator_tool_scrap
**定义**：刀具报废登记（报废人、报废原因） ｜ **流角色**：刀具生命周期-报废 ｜ **代码**：`generator/tool_scrap/model.py` ｜ **行数(估)**：16936

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `cabinet_number` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `scrapper_name` | varchar(255) | Y | - | 报废人 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `barcode` | varchar(255) | Y | - | 条码 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `scrap_reason` | varchar(255) | Y | - | 报废原因 | ✅ |  |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]同步至V2系统的关联ID（技术列） | 🔍 |  |

### generator_tool_storage
**定义**：新刀入智能刀具柜登记（管理员、柜号） ｜ **流角色**：刀具生命周期-入库 ｜ **代码**：`generator/tool_storage/model.py` ｜ **行数(估)**：50440

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | _MASK_TO_V2 | ✅ |  |
| `remarks` | longtext | Y | - | 备注 | ✅ |  |
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `cabinet_id` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `admin` | varchar(255) | Y | - | 管理员 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier_name` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `bar_code` | varchar(255) | Y | - | 条码 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 入库时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_tools
**定义**：刀具主档：条码、型号、大小分类、供应商、所属刀柜 ｜ **流角色**：刀具主数据 ｜ **代码**：`generator/tools/model.py` ｜ **行数(估)**：1478

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `factory` | varchar(255) | Y | - | 工厂 | ✅ |  |
| `cabinet_id` | varchar(255) | Y | - | 柜号 | ✅ |  |
| `code` | varchar(255) | Y | - | 编号 | ✅ |  |
| `manager` | varchar(255) | Y | - | 管理员 | ✅ |  |
| `model` | varchar(255) | Y | - | 型号 | ✅ |  |
| `supplier_name` | varchar(255) | Y | - | 供应商 | ✅ |  |
| `subcategory` | varchar(255) | Y | - | 小类 | ✅ |  |
| `main_category` | varchar(255) | Y | - | 大类 | ✅ |  |
| `product` | varchar(255) | Y | - | 产品 | ✅ |  |
| `bar_code` | varchar(255) | Y | - | 条码 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | varchar(255) | Y | - | _MASK_TO_V2 | ✅ |  |

---

## 同域兄弟模块
- [[03-质量技术域/设备装置模块-fuadmin数据字典2|设备装置模块]]
- [[03-质量技术域/设备模块-fuadmin数据字典2|设备模块]]
- [[03-质量技术域/工装夹具模块-fuadmin数据字典2|工装夹具模块]]
- [[03-质量技术域/质量检验模块-fuadmin数据字典2|质量检验模块]]
- [[03-质量技术域/刀具模块-fuadmin数据字典2|刀具模块]]
- [[03-质量技术域/维修保养模块-fuadmin数据字典2|维修保养模块]]
- [[03-质量技术域/测量计量模块-fuadmin数据字典2|测量计量模块]]
- [[03-质量技术域/工艺技术模块-fuadmin数据字典2|工艺技术模块]]
- [[03-质量技术域/产品模块-fuadmin数据字典2|产品模块]]
- [[03-质量技术域/03-质量技术域-业务流|03-质量技术域业务流(代码验证版)]]
