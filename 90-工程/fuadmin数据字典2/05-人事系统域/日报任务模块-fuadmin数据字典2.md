---
title: 日报任务模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 05-人事系统域
tags: [工程, 数据字典2, 代码实证, 日报任务]
---

# 日报任务模块 · fuadmin 数据字典2（代码实证版）
> 域: 05-人事系统域 | 表数: 3 | 字段: 41 | 代码锚定: 0(0%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/05-人事系统域/日报任务模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_dailyreport` |  | 5904 | 🔍 |
| `generator_dailytask` |  | 12784 | 🔍 |
| `generator_monthlytask` |  | 754 | 🔍 |

---

### generator_dailyreport
**定义**：（待补充） ｜ **行数(估)**：5904

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `remark` | varchar(255) | Y | - | （界面:备注） | 🔍🖥️ |  |
| `modifier` | varchar(255) | Y | - | （界面:修改人） | 🔍🖥️ |  |
| `belong_dept` | int | Y | - | （界面:所属部门） | 🔍🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | （界面:未结单） | 🔍🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | （界面:时间） | 🔍🖥️ |  |
| `sort` | int | Y | - | （界面:排序） | 🔍🖥️ |  |
| `report_date` | date | N | - | 🔍待补充 | 🔍 |  |
| `details` | longtext | Y | - | （界面:产线产量趋势） | 🔍🖥️ |  |
| `tomorrow_plan` | longtext | Y | - | 🔍待补充 | 🔍 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 | →system_users(推断) |
| `cc_users` | json | Y | - | 🔍待补充 | 🔍 |  |
| `comments` | json | Y | - | 🔍待补充 | 🔍 |  |

### generator_dailytask
**定义**：（待补充） ｜ **行数(估)**：12784

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `remark` | varchar(255) | Y | - | （界面:备注） | 🔍🖥️ |  |
| `modifier` | varchar(255) | Y | - | （界面:修改人） | 🔍🖥️ |  |
| `belong_dept` | int | Y | - | （界面:所属部门） | 🔍🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | （界面:未结单） | 🔍🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | （界面:时间） | 🔍🖥️ |  |
| `sort` | int | Y | - | （界面:排序） | 🔍🖥️ |  |
| `task_date` | date | N | - | 🔍待补充 | 🔍 |  |
| `percentage` | int | N | - | （界面:余量百分比） | 🔍🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 | →system_users(推断) |
| `project_id` | bigint | Y | MUL | 🔍待补充 | 🔍 | →go_view_project(推断) |
| `is_systemTask` | tinyint(1) | N | - | 🔍待补充 | 🔍 |  |
| `name` | varchar(50) | Y | - | （界面:原辅料名称） | 🔍🖥️ |  |

### generator_monthlytask
**定义**：（待补充） ｜ **行数(估)**：754

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `remark` | varchar(255) | Y | - | （界面:备注） | 🔍🖥️ |  |
| `modifier` | varchar(255) | Y | - | （界面:修改人） | 🔍🖥️ |  |
| `belong_dept` | int | Y | - | （界面:所属部门） | 🔍🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | （界面:未结单） | 🔍🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | （界面:时间） | 🔍🖥️ |  |
| `sort` | int | Y | - | （界面:排序） | 🔍🖥️ |  |
| `month_date` | varchar(10) | N | - | 🔍待补充 | 🔍 |  |
| `name` | varchar(50) | Y | - | （界面:原辅料名称） | 🔍🖥️ |  |
| `percentage` | float(11,2) | N | - | （界面:余量百分比） | 🔍🖥️ |  |
| `is_systemTask` | tinyint(1) | N | - | 🔍待补充 | 🔍 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 | →system_users(推断) |
| `project_id` | bigint | Y | MUL | 🔍待补充 | 🔍 | →go_view_project(推断) |
| `approver` | varchar(15) | Y | - | （界面:审批人） | 🔍🖥️ |  |
| `is_activate` | tinyint(1) | N | - | 🔍待补充 | 🔍 |  |
