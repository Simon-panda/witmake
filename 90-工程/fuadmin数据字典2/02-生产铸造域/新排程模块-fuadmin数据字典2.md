---
title: 新排程模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 02-生产铸造域
tags: [工程, 数据字典2, 代码实证, 新排程]
---

# 新排程模块 · fuadmin 数据字典2（代码实证版）
> 域: 02-生产铸造域 | 表数: 2 | 字段: 55 | 代码锚定: 55(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/02-生产铸造域/新排程模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_newscheduling` | 工作信息表 | 246180 | 💻 |
| `generator_newscheduling_temp` | 工作日报临时表 | 42987 | 💻 |

---

### generator_newscheduling
**定义**：工作信息表 ｜ **代码**：`generator/newscheduling/model.py` ｜ **行数(估)**：246180

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 | →generator_salary |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `status` | varchar(10) | Y | - | 状态：冻结/启用，决定该数据能否被修改 | 💬⚖️ |  |
| `leader` | varchar(20) | Y | - | 班长签字 | ✅ |  |
| `scrap_waste` | int | Y | - | 料废：生产部生产时发现的料废数 | ✅⚖️ |  |
| `industrial_waste` | int | Y | - | 工废：生产部生产时发现的工废数 | ✅⚖️ |  |
| `device_code` | varchar(30) | Y | - | 设备编号（已废弃暂未使用） | ✅⚖️ | →generator_devices(推断) |
| `train_user` | varchar(30) | Y | - | 培训人(师傅) | ✅ |  |
| `right` | int | Y | - | R：右部零件数量（已废弃暂未使用） | ✅⚖️ |  |
| `left` | int | Y | - | L：左部零件数量（已废弃暂未使用） | ✅⚖️ |  |
| `actual_output` | int | Y | - | 实际生产数：实际的生产数量 | ✅⚖️ |  |
| `plan_output` | int | Y | - | 计划生产数 | ✅ |  |
| `work_hours` | decimal(13,2) | Y | - | 工时(小时)：当天该条记录用时，可分开填写后叠加 | ✅⚖️ |  |
| `work_state` | varchar(20) | Y | - | 工作状态（该字段用得很少） | ✅⚖️ |  |
| `job_code_name` | varchar(80) | Y | - | 工作代号 | ✅ |  |
| `day_night` | varchar(20) | Y | - | 班次：白班/夜班/休息 | 💬⚖️ |  |
| `working_system` | varchar(20) | Y | - | 工作制：0(5天8H-W) 1(6天8H-W) 2(5天8H-I) 3(6天8H-I) | 💬⚖️ |  |
| `user` | varchar(20) | Y | - | 姓名/工号，格式'工号 姓名' | ✅⚖️ |  |
| `dept` | varchar(20) | Y | - | 部门：生产/物流/质量/工程 | 💬⚖️ |  |
| `site` | varchar(20) | Y | - | 工作地点：治通/广汇/娄塘/泰峰，站点内部门或有缺失 | 💬⚖️ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `date` | date | Y | - | 日期：具体工作日期 | ✅⚖️ |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `downtime` | decimal(6,1) | Y | - | 宕机时间(小时)，精度0.5小时 | ✅⚖️ |  |
| `finance_hours` | decimal(13,2) | Y | - | 工时(财务)（已废弃暂未使用） | ✅⚖️ |  |

### generator_newscheduling_temp
**定义**：工作日报临时表 ｜ **代码**：`generator/newscheduling/model.py` ｜ **行数(估)**：42987

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `date` | date | Y | - | 日期 | ✅ |  |
| `site` | varchar(20) | Y | - | 工作地点 | ✅ |  |
| `dept` | varchar(20) | Y | - | 部门 | ✅ |  |
| `user` | varchar(50) | Y | - | 姓名/工号 | ✅ |  |
| `day_night` | varchar(20) | Y | - | 班次 | ✅ |  |
| `job_code_name` | varchar(80) | Y | - | 工作代号 | ✅ |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `actual_output` | int | Y | - | 实际生产数 | ✅ |  |
| `work_hours` | decimal(13,2) | Y | - | 工时(小时) | ✅ |  |
| `industrial_waste` | int | Y | - | 工废 | ✅ |  |
| `scrap_waste` | int | Y | - | 料废 | ✅ |  |
| `user_remark` | varchar(255) | Y | - | 操作工描述 | ✅ |  |
| `status` | int | Y | - | 状态：0待审核 1已审核 2注销(假删除) | ✅⚖️ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `approve_time` | datetime(6) | Y | - | 审批时间；最近一次审批操作时间 | ✅ |  |
| `approver` | varchar(50) | Y | - | 审批人：班长签字，姓名/工号 | ✅⚖️ |  |
| `history_snapshot` | json | Y | - | 变更历史；每次修改追加一条，包含修改人、时间、变更字段前后值 | ✅ |  |
| `downtime` | decimal(6,1) | Y | - | 宕机时间；宕机时间（小时），精度0.5小时 | ✅ |  |

---

## 同域兄弟模块
- [[02-生产铸造域/不良品模块-fuadmin数据字典2|不良品模块]]
- [[02-生产铸造域/生产计划模块-fuadmin数据字典2|生产计划模块]]
- [[02-生产铸造域/生产模块-fuadmin数据字典2|生产模块]]
- [[02-生产铸造域/二维码追溯模块-fuadmin数据字典2|二维码追溯模块]]
- [[02-生产铸造域/班次模块-fuadmin数据字典2|班次模块]]
- [[02-生产铸造域/TF铸造模块-fuadmin数据字典2|TF铸造模块]]
- [[02-生产铸造域/02-生产铸造域-业务流|02-生产铸造域业务流(代码验证版)]]
