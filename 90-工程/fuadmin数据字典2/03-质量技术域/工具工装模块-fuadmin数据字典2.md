---
title: 工具工装模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 工具工装]
---

# 工具工装模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 6 | 字段: 113 | 代码锚定: 104(92%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/工具工装模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_take_tool` | 领刀表 | 44384 | 💻 |
| `generator_tool_replacement` | 换刀片表 | 13446 | 💻 |
| `generator_tool_return_table` | 刀具返库 | 34790 | 💻 |
| `generator_tool_scrap` | 刀具报废 | 16936 | 💻 |
| `generator_tool_storage` | 刀具入库表 | 50440 | 💻 |
| `generator_tools` | 刀具表 | 1478 | 💻 |

---

### generator_take_tool
**定义**：领刀表 ｜ **代码**：`generator/take_tool/model.py` ｜ **行数(估)**：44384

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:入库时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | 🔍待补充 | 🔍 |  |

### generator_tool_replacement
**定义**：换刀片表 ｜ **代码**：`generator/tool_replacement/model.py` ｜ **行数(估)**：13446

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:入库时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_tool_return_table
**定义**：刀具返库 ｜ **代码**：`generator/tool_return_table/model.py` ｜ **行数(估)**：34790

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_tool_scrap
**定义**：刀具报废 ｜ **代码**：`generator/tool_scrap/model.py` ｜ **行数(估)**：16936

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `scrap_reason` | varchar(255) | Y | - | 报废原因 | ✅ |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_tool_storage
**定义**：刀具入库表 ｜ **代码**：`generator/tool_storage/model.py` ｜ **行数(估)**：50440

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:入库时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_tools
**定义**：刀具表 ｜ **代码**：`generator/tools/model.py` ｜ **行数(估)**：1478

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:条码） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_TO_V2` | varchar(255) | Y | - | _MASK_TO_V2 | ✅ |  |
