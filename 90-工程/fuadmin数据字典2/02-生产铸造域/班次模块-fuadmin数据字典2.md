---
title: 班次模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 02-生产铸造域
tags: [工程, 数据字典2, 代码实证, 班次]
---

# 班次模块 · fuadmin 数据字典2（代码实证版）
> 域: 02-生产铸造域 | 表数: 3 | 字段: 42 | 代码锚定: 39(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/02-生产铸造域/班次模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_shift_schedule` | 预排班 | 20980 | 💻 |
| `generator_shift_template` | 排班模板 | 13 | 💻 |
| `generator_shift_template_member` | 模板成员 | 140 | 💻 |

---

### generator_shift_schedule
**定义**：预排班 ｜ **代码**：`generator/shift_schedule/model.py` ｜ **行数(估)**：20980

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `site` | varchar(20) | N | MUL | 工作地点 | ✅ |  |
| `dept` | varchar(20) | Y | - | 部门 | ✅ |  |
| `user` | varchar(50) | N | - | 姓名/工号 | ✅ |  |
| `date` | date | N | - | 排班日期 | ✅ |  |
| `shift` | varchar(10) | N | - | 班次；枚举[白班=白班,夜班=夜班,休息=休息] | ✅🔢 |  |
| `job_codes` | json | Y | - | 预排工作代号；JSON 数组，如 ["机加-A线-1号机"]，空表示未指定任务 | ✅ |  |
| `is_override` | tinyint(1) | N | - | 是否手动调整 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 | →system_users |

### generator_shift_template
**定义**：排班模板 ｜ **代码**：`generator/shift_schedule/model.py` ｜ **行数(估)**：13

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `site` | varchar(20) | N | - | 工作地点 | ✅ |  |
| `name` | varchar(30) | N | - | 模板名称（界面:原辅料名称） | ✅🖥️ |  |
| `pattern_type` | varchar(20) | N | - | 模式类型；枚举[fixed_day=固定白班,fixed_night=固定夜班,rotate_2w=双周轮班,custom=自定义] | ✅🔢 |  |
| `custom_pattern` | json | Y | - | 自定义模式 | ✅ |  |
| `anchor_date` | date | Y | - | 周期锚点日 | ✅ |  |
| `rest_on_weekend` | tinyint(1) | N | - | 周末强制休息 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `dept` | varchar(20) | Y | - | 部门 | ✅ |  |

### generator_shift_template_member
**定义**：模板成员 ｜ **代码**：`generator/shift_schedule/model.py` ｜ **行数(估)**：140

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `user` | varchar(50) | N | - | 姓名/工号（界面:员工） | ✅🖥️ |  |
| `site` | varchar(20) | N | - | 站点（界面:地点） | ✅🖥️ |  |
| `dept` | varchar(20) | Y | - | 部门 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `template_id` | bigint | N | MUL | 模板；→generator_shift_template | ✅🔗 | →generator_shift_template |
