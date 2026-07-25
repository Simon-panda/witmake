---
title: 维修保养模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 维修保养]
---

# 维修保养模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 2 | 字段: 34 | 代码锚定: 32(94%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/维修保养模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_maintenance_records` | 设备维修记录 | 3 | 💻 |
| `generator_maintenance_schedule` | 设备维修计划表 | 9 | 💻 |

---

### generator_maintenance_records
**定义**：设备维修记录 ｜ **代码**：`generator/maintenance_records/model.py` ｜ **行数(估)**：3

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:设备名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | longtext | Y | - | 备注 | ✅ |  |
| `duration` | longtext | Y | - | 处理/用途内容 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 登记时间 | ✅ |  |
| `after_img` | varchar(255) | Y | - | 维修后图片 | ✅ |  |
| `before_img` | varchar(255) | Y | - | 维修前图片 | ✅ |  |
| `spare_part_number` | int | Y | - | 使用数量 | ✅ |  |
| `spare_part_model` | varchar(255) | Y | - | 备件型号 | ✅ |  |
| `spare_part_name` | varchar(255) | Y | - | 备件名称 | ✅ |  |
| `operation_duration` | decimal(13,1) | Y | - | 操作时长 | ✅ |  |
| `technician` | varchar(255) | Y | - | 维修人员 | ✅ |  |
| `type` | varchar(255) | Y | - | 事件类型 | ✅ |  |
| `name` | varchar(255) | Y | - | 事件名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 | →system_users |
| `device_id` | bigint | Y | MUL | 设备名称；→generator_devices | ✅🔗 | →generator_devices |

### generator_maintenance_schedule
**定义**：设备维修计划表 ｜ **代码**：`generator/maintenance_schedule/model.py` ｜ **行数(估)**：9

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:设备名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `status` | varchar(255) | Y | - | 状态 | ✅ |  |
| `description` | longtext | Y | - | 描述 | ✅ |  |
| `type` | varchar(255) | Y | - | 事件类型 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 预定日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `device_id` | bigint | Y | MUL | 设备名称；→generator_devices | ✅🔗 | →generator_devices |
