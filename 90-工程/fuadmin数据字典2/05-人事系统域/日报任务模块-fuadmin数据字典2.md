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
| `generator_dailyreport` | [推断] 员工日报表：每日工作详情+明日计划，支持抄送与评论（代码已移除，历史遗留） | 5904 | 🔍 |
| `generator_dailytask` | [推断] 每日任务表：任务日期+完成百分比，可挂项目（代码已移除，历史遗留） | 12784 | 🔍 |
| `generator_monthlytask` | [推断] 月度任务表：月度目标+完成百分比+审批人（代码已移除，历史遗留） | 754 | 🔍 |

---

### generator_dailyreport
**定义**：[推断] 员工日报表：每日工作详情+明日计划，支持抄送与评论（代码已移除，历史遗留） ｜ **流角色**：日报体系-日报填报 ｜ **行数(估)**：5904

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `remark` | varchar(255) | Y | - | [推断] 备注 | 🔍 |  |
| `modifier` | varchar(255) | Y | - | [推断] 修改人 | 🔍 |  |
| `belong_dept` | int | Y | - | [推断] 数据归属部门 | 🔍 |  |
| `update_datetime` | datetime(6) | Y | - | [推断] 修改时间 | 🔍 |  |
| `create_datetime` | datetime(6) | Y | - | [推断] 创建时间 | 🔍 |  |
| `sort` | int | Y | - | [推断] 显示排序 | 🔍 |  |
| `report_date` | date | N | - | [推断] 日报日期（与创建人联合唯一，每人每天一篇） | 🔍 |  |
| `details` | longtext | Y | - | [推断] 今日工作内容详情（富文本） | 🔍 |  |
| `tomorrow_plan` | longtext | Y | - | [推断] 明日工作计划（富文本） | 🔍 |  |
| `creator_id` | bigint | Y | MUL | [推断] 创建人/日报填报人（→system_users.id） | 🔍 | →system_users(推断) |
| `cc_users` | json | Y | - | [推断] 抄送人（用户ID列表，JSON） | 🔍 |  |
| `comments` | json | Y | - | [推断] 评论/批注列表（JSON） | 🔍 |  |

### generator_dailytask
**定义**：[推断] 每日任务表：任务日期+完成百分比，可挂项目（代码已移除，历史遗留） ｜ **流角色**：日报体系-日任务跟踪 ｜ **行数(估)**：12784

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `remark` | varchar(255) | Y | - | [推断] 备注 | 🔍 |  |
| `modifier` | varchar(255) | Y | - | [推断] 修改人 | 🔍 |  |
| `belong_dept` | int | Y | - | [推断] 数据归属部门 | 🔍 |  |
| `update_datetime` | datetime(6) | Y | - | [推断] 修改时间 | 🔍 |  |
| `create_datetime` | datetime(6) | Y | - | [推断] 创建时间 | 🔍 |  |
| `sort` | int | Y | - | [推断] 显示排序 | 🔍 |  |
| `task_date` | date | N | - | [推断] 任务日期 | 🔍 |  |
| `percentage` | int | N | - | [推断] 完成百分比（0-100） | 🔍 |  |
| `creator_id` | bigint | Y | MUL | [推断] 创建人（→system_users.id） | 🔍 | →system_users(推断) |
| `project_id` | bigint | Y | MUL | [推断] 关联项目（→generator_project.id） | 🔍 | →go_view_project(推断) |
| `is_systemTask` | tinyint(1) | N | - | [推断] 是否系统生成任务（1系统任务 0手动创建） | 🔍 |  |
| `name` | varchar(50) | Y | - | [推断] 任务名称 | 🔍 |  |

### generator_monthlytask
**定义**：[推断] 月度任务表：月度目标+完成百分比+审批人（代码已移除，历史遗留） ｜ **流角色**：日报体系-月度任务 ｜ **行数(估)**：754

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `remark` | varchar(255) | Y | - | [推断] 备注 | 🔍 |  |
| `modifier` | varchar(255) | Y | - | [推断] 修改人 | 🔍 |  |
| `belong_dept` | int | Y | - | [推断] 数据归属部门 | 🔍 |  |
| `update_datetime` | datetime(6) | Y | - | [推断] 修改时间 | 🔍 |  |
| `create_datetime` | datetime(6) | Y | - | [推断] 创建时间 | 🔍 |  |
| `sort` | int | Y | - | [推断] 显示排序 | 🔍 |  |
| `month_date` | varchar(10) | N | - | [推断] 所属月份（如2024-06） | 🔍 |  |
| `name` | varchar(50) | Y | - | [推断] 任务名称 | 🔍 |  |
| `percentage` | float(11,2) | N | - | [推断] 完成百分比（0-100） | 🔍 |  |
| `is_systemTask` | tinyint(1) | N | - | [推断] 是否系统生成任务（1系统任务 0手动创建） | 🔍 |  |
| `creator_id` | bigint | Y | MUL | [推断] 创建人（→system_users.id） | 🔍 | →system_users(推断) |
| `project_id` | bigint | Y | MUL | [推断] 关联项目（→generator_project.id） | 🔍 | →go_view_project(推断) |
| `approver` | varchar(15) | Y | - | [推断] 审批人 | 🔍 |  |
| `is_activate` | tinyint(1) | N | - | [推断] 是否激活/启用 | 🔍 |  |

---

## 同域兄弟模块
- [[05-人事系统域/考勤打卡模块-fuadmin数据字典2|考勤打卡模块]]
- [[05-人事系统域/人力能力模块-fuadmin数据字典2|人力能力模块]]
- [[05-人事系统域/用户权限模块-fuadmin数据字典2|用户权限模块]]
- [[05-人事系统域/05-人事系统域-业务流|05-人事系统域业务流(代码验证版)]]
