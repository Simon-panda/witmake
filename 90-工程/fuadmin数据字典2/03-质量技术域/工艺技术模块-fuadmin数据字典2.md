---
title: 工艺技术模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 工艺技术]
---

# 工艺技术模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 2 | 字段: 28 | 代码锚定: 26(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/工艺技术模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_jgdm` | 激光打码工序产量与参数记录（动态表单字段） | 450 | 💻 |
| `generator_process_inventory` | 按站点聚合的产品在制工序库存汇总（未启用） | 0 | 💻 |

---

### generator_jgdm
**定义**：激光打码工序产量与参数记录（动态表单字段） ｜ **流角色**：工艺-激光打码 ｜ **代码**：`generator/jgdm/model.py` ｜ **行数(估)**：450

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `input_4` | varchar(255) | Y | - | 产量 | ✅ |  |
| `select_3` | varchar(255) | Y | - | 班次 | ✅ |  |
| `select_2` | varchar(255) | Y | - | 产线 | ✅ |  |
| `date_picker_1` | date | Y | - | 生产日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断]同步至V2系统的关联ID（技术列） | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | [推断]V2数据同步状态/批次标识（技术列） | 🔍 |  |

### generator_process_inventory
**定义**：按站点聚合的产品在制工序库存汇总（未启用） ｜ **流角色**：工艺-在制库存 ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `product_name` | varchar(100) | Y | - | 产品名称 | ✅ |  |
| `quantity` | int | N | - | 库存数量 | ✅ |  |
| `tracking_count` | int | N | - | 跟踪单数 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `product_id` | bigint | Y | MUL | 产品；→generator_product | ✅🔗 | →generator_product |
| `station_name` | varchar(100) | Y | - | 站点名称 | ✅ |  |
| `station_id` | bigint | Y | MUL | 跟踪站点；→track_station | ✅🔗 | →track_station |

---

## 同域兄弟模块
- [[03-质量技术域/设备装置模块-fuadmin数据字典2|设备装置模块]]
- [[03-质量技术域/设备模块-fuadmin数据字典2|设备模块]]
- [[03-质量技术域/工装夹具模块-fuadmin数据字典2|工装夹具模块]]
- [[03-质量技术域/质量检验模块-fuadmin数据字典2|质量检验模块]]
- [[03-质量技术域/刀具模块-fuadmin数据字典2|刀具模块]]
- [[03-质量技术域/维修保养模块-fuadmin数据字典2|维修保养模块]]
- [[03-质量技术域/测量计量模块-fuadmin数据字典2|测量计量模块]]
- [[03-质量技术域/产品模块-fuadmin数据字典2|产品模块]]
- [[03-质量技术域/工具工装模块-fuadmin数据字典2|工具工装模块]]
- [[03-质量技术域/03-质量技术域-业务流|03-质量技术域业务流(代码验证版)]]
