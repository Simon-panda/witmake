---
title: lizhu定制模块模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, lizhu定制模块]
---

# lizhu定制模块模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 3 | 字段: 45 | 代码锚定: 40(89%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/lizhu定制模块模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_lizhu_count_data` | 立柱累计数据（GS61/GS62左右侧计数） | 457 | 💻 |
| `generator_lizhu_error_data` | 立柱错误数据（刀具/方向异常影像） | 251 | 💻 |
| `generator_lizhu_robot_data` | 立柱机器人数据（加工状态采集） | 171244 | 💻 |

---

### generator_lizhu_count_data
**定义**：立柱累计数据（GS61/GS62左右侧计数） ｜ **流角色**：立柱专机-产量累计 ｜ **代码**：`generator/lizhu_count_data/model.py` ｜ **行数(估)**：457

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `create_date` | datetime(6) | Y | - | CREATE_DATE | ✅ |  |
| `RIGHT_GS62H` | int | Y | - | [推断] 右侧GS62H机型累计计数 | 🔍 |  |
| `RIGHT_GS62` | int | Y | - | [推断] 右侧GS62机型累计计数 | 🔍 |  |
| `right_gs61h` | int | Y | - | RIGHT_GS61H | ✅ |  |
| `right_gs61` | int | Y | - | RIGHT_GS61 | ✅ |  |
| `left_gs62h` | int | Y | - | LEFT_GS62H | ✅ |  |
| `left_gs62` | int | Y | - | LEFT_GS62 | ✅ |  |
| `left_gs61h` | int | Y | - | LEFT_GS61H | ✅ |  |
| `left_gs61` | int | Y | - | LEFT_GS61 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断] 外部系统同步掩码（迁移痕迹） | 🔍 |  |

### generator_lizhu_error_data
**定义**：立柱错误数据（刀具/方向异常影像） ｜ **流角色**：立柱专机-异常记录 ｜ **代码**：`generator/lizhu_error_data/model.py` ｜ **行数(估)**：251

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `image` | varchar(255) | Y | - | IMAGE | ✅ |  |
| `create_date` | datetime(6) | Y | - | CREATE_DATE | ✅ |  |
| `model_tool_type` | varchar(255) | Y | - | MODEL_TOOL_TYPE | ✅ |  |
| `curr_tool_type` | varchar(255) | Y | - | CURR_TOOL_TYPE | ✅ |  |
| `direction` | varchar(255) | Y | - | DIRECTION | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断] 外部系统同步掩码（迁移痕迹） | 🔍 |  |

### generator_lizhu_robot_data
**定义**：立柱机器人数据（加工状态采集） ｜ **流角色**：立柱专机-状态采集 ｜ **代码**：`generator/lizhu_robot_data/model.py` ｜ **行数(估)**：171244

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `direction` | varchar(255) | Y | - | DIRECTION | ✅ |  |
| `create_date` | datetime(6) | Y | - | CREATE_DATE | ✅ |  |
| `state` | varchar(255) | Y | - | STATE | ✅ |  |
| `tool_type` | varchar(255) | Y | - | TOOL_TYPE | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断] 外部系统同步掩码（迁移痕迹） | 🔍 |  |

---

## 同域兄弟模块
- [[06-其他定制/answer定制模块模块-fuadmin数据字典2|answer定制模块模块]]
- [[06-其他定制/liqiang定制模块模块-fuadmin数据字典2|liqiang定制模块模块]]
- [[06-其他定制/misc-alarm模块-fuadmin数据字典2|misc-alarm模块]]
- [[06-其他定制/misc-commentsmessage模块-fuadmin数据字典2|misc-commentsmessage模块]]
- [[06-其他定制/misc-cooperation模块-fuadmin数据字典2|misc-cooperation模块]]
- [[06-其他定制/misc-definition模块-fuadmin数据字典2|misc-definition模块]]
- [[06-其他定制/misc-demo模块-fuadmin数据字典2|misc-demo模块]]
- [[06-其他定制/misc-external模块-fuadmin数据字典2|misc-external模块]]
- [[06-其他定制/misc-go模块-fuadmin数据字典2|misc-go模块]]
- [[06-其他定制/misc-management模块-fuadmin数据字典2|misc-management模块]]
- [[06-其他定制/misc-objective模块-fuadmin数据字典2|misc-objective模块]]
- [[06-其他定制/misc-public模块-fuadmin数据字典2|misc-public模块]]
- [[06-其他定制/misc-safety模块-fuadmin数据字典2|misc-safety模块]]
- [[06-其他定制/misc-site模块-fuadmin数据字典2|misc-site模块]]
- [[06-其他定制/misc-ticket模块-fuadmin数据字典2|misc-ticket模块]]
- [[06-其他定制/misc-total模块-fuadmin数据字典2|misc-total模块]]
- [[06-其他定制/misc-triangle模块-fuadmin数据字典2|misc-triangle模块]]
- [[06-其他定制/misc-zj2315模块-fuadmin数据字典2|misc-zj2315模块]]
- [[06-其他定制/test定制模块模块-fuadmin数据字典2|test定制模块模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
