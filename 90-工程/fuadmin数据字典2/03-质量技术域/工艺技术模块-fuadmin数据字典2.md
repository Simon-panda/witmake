---
title: 工艺技术模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 工艺技术]
---

# 工艺技术模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 2 | 字段: 28 | 代码锚定: 24(86%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/工艺技术模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_jgdm` | 激光打码 | 450 | 💻 |
| `generator_process_inventory` | 工序库存 | 0 | 💻 |

---

### generator_jgdm
**定义**：激光打码 ｜ **代码**：`generator/jgdm/model.py` ｜ **行数(估)**：450

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Id（界面:生产日期） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `input_4` | varchar(255) | Y | - | 产量 | ✅ |  |
| `select_3` | varchar(255) | Y | - | 班次 | ✅ |  |
| `select_2` | varchar(255) | Y | - | 产线 | ✅ |  |
| `date_picker_1` | date | Y | - | 生产日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 | →system_users |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_process_inventory
**定义**：工序库存 ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `product_name` | varchar(100) | Y | - | 产品名称 | ✅ |  |
| `quantity` | int | N | - | 库存数量 | ✅ |  |
| `tracking_count` | int | N | - | 跟踪单数 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `product_id` | bigint | Y | MUL | 产品；→generator_product | ✅🔗 | →generator_product |
| `station_name` | varchar(100) | Y | - | 站点名称 | ✅ |  |
| `station_id` | bigint | Y | MUL | 跟踪站点；→track_station | ✅🔗 | →track_station |
