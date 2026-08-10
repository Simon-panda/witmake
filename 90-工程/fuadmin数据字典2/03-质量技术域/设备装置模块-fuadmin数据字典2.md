---
title: 设备装置模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 设备装置]
---

# 设备装置模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 4 | 字段: 66 | 代码锚定: 66(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/设备装置模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_device_cutting_fluid_check` | 设备切削液浓度定期巡检记录（浓度对照设备允许范围） | 344 | 💻 |
| `generator_device_eff` | 按日统计单台设备运行/停机时长、产量与效率并给出改进建议 | 2 | 💻 |
| `generator_devices` | 设备台账主档：厂内编号、型号、产线、状态、归属及切削液浓度范围 | 543 | 💻 |
| `generator_devices_log` | 设备运行/停机/报警状态变更流水日志 | 11 | 💻 |

---

### generator_device_cutting_fluid_check
**定义**：设备切削液浓度定期巡检记录（浓度对照设备允许范围） ｜ **流角色**：设备点检-切削液 ｜ **代码**：`generator/device_cutting_fluid_check/model.py` ｜ **行数(估)**：344

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `inspection_content` | json | Y | - | 巡检内容 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `inspector_id` | bigint | Y | MUL | 巡检人；→system_users | ✅🔗 | →system_users |

### generator_device_eff
**定义**：按日统计单台设备运行/停机时长、产量与效率并给出改进建议 ｜ **流角色**：设备效率(OEE)分析 ｜ **代码**：`generator/device_eff/model.py` ｜ **行数(估)**：2

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `recommendations` | longtext | Y | - | 建议 | ✅ |  |
| `date_time` | date | Y | - | 分析日期 | ✅ |  |
| `production_count` | int | Y | - | 执行数量 | ✅ |  |
| `efficiency` | decimal(13,2) | Y | - | 效率 | ✅ |  |
| `downtime` | decimal(13,1) | Y | - | 停机时间 | ✅ |  |
| `runtime` | decimal(13,1) | Y | - | 运行时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `device_id` | bigint | Y | MUL | 设备名称；→generator_devices | ✅🔗 | →generator_devices |

### generator_devices
**定义**：设备台账主档：厂内编号、型号、产线、状态、归属及切削液浓度范围 ｜ **流角色**：设备主数据 ｜ **代码**：`generator/devices/model.py` ｜ **行数(估)**：543

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 | →generator_equipment_repair |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `status` | varchar(255) | Y | - | 设备状态（运行/停机/报警） | ✅⚖️ |  |
| `last_maintenance` | date | Y | - | 最后维护日期 | ✅ |  |
| `ownership` | varchar(255) | Y | - | 设备归属 | ✅ |  |
| `manager` | varchar(255) | Y | - | 设备负责人 | ✅ |  |
| `production_line` | varchar(255) | Y | - | 产线（关联工作代号表name，一台设备可挂多条产线） | ✅⚖️ |  |
| `four_axis_config` | varchar(255) | Y | - | 四轴转塔配置 | ✅ |  |
| `tool_config` | varchar(255) | Y | - | 刀库配置 | ✅ |  |
| `power_parameters` | varchar(255) | Y | - | 功率参数 | ✅ |  |
| `manufacturer` | varchar(255) | Y | - | 生产厂家 | ✅ |  |
| `manufacturing_date` | date | Y | - | 出厂日期 | ✅ |  |
| `arrival_date` | date | Y | - | 进厂日期 | ✅ |  |
| `type_id` | bigint | Y | MUL | 设备类型；→generator_inspection_standards | ✅🔗 | →generator_inspection_standards |
| `internal_code` | varchar(255) | Y | MUL | 厂内编号（设备唯一ID） | ✅⚖️ | →generator_newscheduling(推断) |
| `serial_code` | varchar(255) | Y | - | 出厂编号 | ✅ |  |
| `model` | varchar(255) | Y | - | 设备型号 | ✅ |  |
| `name` | varchar(255) | Y | - | 设备名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `dept_id` | bigint | Y | MUL | 所属部门；关联部门；→system_dept | ✅🔗 | →system_dept |
| `is_delete` | tinyint(1) | N | - | 是否删除；是否删除(软删除标记) | ✅📦 |  |
| `history` | json | Y | - | 操作历史 | ✅ |  |
| `tool_list` | json | Y | - | 刀具清单 | ✅ |  |
| `concentration_range` | json | Y | - | 设备浓度范围；设备浓度范围，格式示例：{"min": 10, "max": 50}，取值范围 0-100 | ✅ |  |

### generator_devices_log
**定义**：设备运行/停机/报警状态变更流水日志 ｜ **流角色**：设备状态流水 ｜ **代码**：`generator/devices_log/model.py` ｜ **行数(估)**：11

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `description` | longtext | Y | - | 描述 | ✅ |  |
| `status` | varchar(255) | Y | - | 运行状态 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 日期时间 | ✅ |  |
| `device_id` | bigint | Y | MUL | 设备名称；→generator_devices | ✅🔗 | →generator_devices |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

---

## 同域兄弟模块
- [[03-质量技术域/设备模块-fuadmin数据字典2|设备模块]]
- [[03-质量技术域/工装夹具模块-fuadmin数据字典2|工装夹具模块]]
- [[03-质量技术域/质量检验模块-fuadmin数据字典2|质量检验模块]]
- [[03-质量技术域/刀具模块-fuadmin数据字典2|刀具模块]]
- [[03-质量技术域/维修保养模块-fuadmin数据字典2|维修保养模块]]
- [[03-质量技术域/测量计量模块-fuadmin数据字典2|测量计量模块]]
- [[03-质量技术域/工艺技术模块-fuadmin数据字典2|工艺技术模块]]
- [[03-质量技术域/产品模块-fuadmin数据字典2|产品模块]]
- [[03-质量技术域/工具工装模块-fuadmin数据字典2|工具工装模块]]
- [[03-质量技术域/03-质量技术域-业务流|03-质量技术域业务流(代码验证版)]]
