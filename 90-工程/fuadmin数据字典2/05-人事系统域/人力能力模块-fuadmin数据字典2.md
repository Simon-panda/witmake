---
title: 人力能力模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 05-人事系统域
tags: [工程, 数据字典2, 代码实证, 人力能力]
---

# 人力能力模块 · fuadmin 数据字典2（代码实证版）
> 域: 05-人事系统域 | 表数: 11 | 字段: 263 | 代码锚定: 233(89%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/05-人事系统域/人力能力模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_capability_score` | 人力能力评分表：按站点/产品/线级工作代号统计员工效率达成质量子分与综合评分S及线内 | 5085 | 💻 |
| `generator_employment_registration` | 应聘登记表：应聘者全量信息+面试录用状态流转（0淘汰/1录用/2面试中） | 249 | 💻 |
| `generator_historicaljobcode` | 工作代号历史表（simple_history）：计件单价/结算方式/激励制度等历史快 | 2144 | 📸 |
| `generator_historicaljobcode_devices` | 工作代号-设备关联历史快照表（simple_history，当前0行） | 0 | 📸 |
| `generator_holiday_date` | 法定假期表：假日名称+日期+结算规则，节假日加班工资倍率依据 | 65 | 💻 |
| `generator_job_code` | 工作代号表：产线/工序级工作代号树，含计件单价、结算方式、计划产量 | 1379 | 💻 |
| `generator_job_code_product` | M2M中间表: generator_job_code↔generator_produ | 1715 | 🔗 |
| `generator_jobcode_devices` | 工作代号-设备关联表：工作代号可使用的设备绑定 | 68 | 💻 |
| `generator_roster` | 花名册：员工档案主数据（合同/社保/公积金/雇主险/紧急联系/入离职） | 686 | 💻 |
| `generator_salary` | 工资表：员工逐日报工工资明细（计件/计时/加班/津贴/奖罚），gross_wage需 | 253374 | 💻 |
| `generator_user_product_matrix` | [推断] 人力矩阵统计表：按人×产品×工序×月份汇总工时产量质量及五维评分 | 6627 | 🔍 |

---

### generator_capability_score
**定义**：人力能力评分表：按站点/产品/线级工作代号统计员工效率达成质量子分与综合评分S及线内排名 ｜ **流角色**：人力能力评估→排产调度依据 ｜ **代码**：`generator/newscheduling/model.py` ｜ **行数(估)**：5085

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `site` | varchar(20) | Y | MUL | 工作地点 | ✅ |  |
| `dept` | varchar(30) | Y | - | 所属部门 | ✅ |  |
| `job_code` | varchar(255) | Y | - | 线级工作代号 | ✅ |  |
| `product_name` | varchar(500) | Y | MUL | 产品名称 | ✅ |  |
| `line_type` | varchar(20) | Y | - | 工作类型 | ✅ |  |
| `category` | varchar(20) | Y | - | 类别 | ✅ |  |
| `plan_output` | int | Y | - | 计划产量(每班) | ✅ |  |
| `user_code` | varchar(20) | Y | MUL | 工号 | ✅ | →system_users(推断) |
| `user_name` | varchar(30) | Y | - | 姓名 | ✅ |  |
| `work_days` | int | Y | - | 工作天数 | ✅ |  |
| `unit_hours` | decimal(13,4) | Y | - | 单件工时 | ✅ |  |
| `oph` | decimal(10,2) | Y | - | [推断] 时均产量OPH（每人每小时产出件数） | 🔍 |  |
| `attain_rate` | decimal(8,4) | Y | - | 产量达成率 | ✅ |  |
| `quality_rate` | decimal(8,4) | Y | - | 良率 | ✅ |  |
| `downtime_rate` | decimal(8,4) | Y | - | 宕机率 | ✅ |  |
| `eff_score` | decimal(6,4) | Y | - | 效率子分 | ✅ |  |
| `attain_score` | decimal(6,4) | Y | - | 达成子分 | ✅ |  |
| `stability_score` | decimal(6,4) | Y | - | [推断] 稳定性子分（产量波动稳定性评分） | 🔍 |  |
| `exp_score` | decimal(6,4) | Y | - | 经验子分 | ✅ |  |
| `recency_days` | int | Y | - | 距最近一次作业天数 | ✅ |  |
| `recency_score` | decimal(6,4) | Y | - | 近期性子分 | ✅ |  |
| `score` | decimal(6,4) | Y | - | 综合评分 | ✅ |  |
| `rank_in_line` | int | Y | - | 该线内排名 | ✅ |  |
| `day_cap` | tinyint(1) | N | - | 白班做过 | ✅ |  |
| `night_cap` | tinyint(1) | N | - | 夜班做过 | ✅ |  |
| `calc_time` | datetime | Y | - | 本次计算时间 | ✅ |  |

### generator_employment_registration
**定义**：应聘登记表：应聘者全量信息+面试录用状态流转（0淘汰/1录用/2面试中） ｜ **流角色**：人事流-招聘入职入口 ｜ **代码**：`generator/employment_registration/model.py` ｜ **行数(估)**：249

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `veteran_status` | tinyint(1) | Y | - | 是否是退役军人 | ✅ |  |
| `residence_permit` | tinyint(1) | Y | - | 是否有居住证 | ✅ |  |
| `work_certificate` | varchar(100) | Y | - | 作业证书 | ✅ |  |
| `political_status` | varchar(10) | Y | - | 政治面貌 | ✅ |  |
| `self_introduction` | longtext | Y | - | 个人自我介绍 | ✅ |  |
| `family_information` | json | Y | - | 家庭情况 | ✅ |  |
| `work_experience` | json | Y | - | 主要工作经历 | ✅ |  |
| `major` | varchar(30) | Y | - | 所学专业 | ✅ |  |
| `graduation_school` | varchar(255) | Y | - | 毕业院校 | ✅ |  |
| `graduation_date` | date | Y | - | 毕业时间 | ✅ |  |
| `education` | varchar(20) | Y | - | 最高学历 | ✅ |  |
| `id_number` | varchar(18) | Y | - | 身份证号码 | ✅ |  |
| `household_registration_type` | varchar(50) | Y | - | 户口性质 | ✅ |  |
| `emergency_contact_phone` | varchar(30) | Y | - | 紧急联系人电话 | ✅ |  |
| `emergency_contact_name` | varchar(30) | Y | - | 紧急联系人姓名 | ✅ |  |
| `phone` | varchar(20) | Y | - | 联系电话 | ✅ |  |
| `home_address` | varchar(255) | Y | - | 家庭住址 | ✅ |  |
| `postal_code` | varchar(20) | Y | - | 邮编 | ✅ |  |
| `registered_address` | varchar(255) | Y | - | 身份证地址 | ✅ |  |
| `marital_status` | varchar(20) | Y | - | 婚姻情况 | ✅ |  |
| `weight_kg` | decimal(5,2) | Y | - | 体重(kg) | ✅ |  |
| `height_cm` | decimal(5,2) | Y | - | 身高(cm) | ✅ |  |
| `vision` | varchar(50) | Y | - | 视力 | ✅ |  |
| `birth_date` | date | Y | - | 出生年月日 | ✅ |  |
| `health_status` | varchar(100) | Y | - | 健康状况 | ✅ |  |
| `ethnicity` | varchar(50) | Y | - | 民族 | ✅ |  |
| `native_place` | varchar(255) | Y | - | 籍贯 | ✅ |  |
| `is_male` | tinyint(1) | Y | - | 性别 | ✅ |  |
| `name` | varchar(30) | Y | - | 姓名 | ✅ |  |
| `position` | varchar(30) | Y | - | 应聘职位 | ✅ |  |
| `site` | varchar(10) | Y | - | 应聘公司 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `state` | int | Y | - | 状态：0淘汰 1录用 2面试中 | ✅⚖️ |  |
| `company` | varchar(20) | Y | - | 所在公司（挂靠）：治通/广汇/泰峰/智机/中蓝/挂中蓝等 | ✅⚖️ |  |

### generator_historicaljobcode
**定义**：工作代号历史表（simple_history）：计件单价/结算方式/激励制度等历史快照 ｜ **流角色**：薪酬-工作代号变更追溯 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：2144

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `is_delete` | tinyint(1) | N | - | 是否删除 | ✅ |  |
| `incentive_system` | json | Y | - | 奖励 | ✅ |  |
| `is_production` | varchar(20) | Y | - | 计入产值（是/否）：判断是否最后工序，避免重复计算数量 | ✅⚖️ |  |
| `range_price` | json | Y | - | 区间价格 | ✅ |  |
| `piecework_price` | decimal(10,2) | Y | - | 计件单价 | ✅ |  |
| `settlement_method` | varchar(20) | Y | - | 计薪方式 | ✅ |  |
| `type` | varchar(20) | Y | - | 工作类型：手动线/自动线 | ✅⚖️ |  |
| `name` | varchar(255) | Y | MUL | 全称 | ✅ |  |
| `dept` | varchar(30) | Y | - | 代码所属部门：生产/质量/工程/物流，字符串拼接或单个 | ✅⚖️ |  |
| `contribution_ratio` | decimal(8,2) | Y | - | 贡献值占例 | ✅ |  |
| `is_sign` | tinyint(1) | N | - | 标记 | ✅ |  |
| `is_floor` | tinyint(1) | N | - | 最底层；True表示最底层(可以被人选择) False表示不是最底层(不能被人选择) | ✅💬 |  |
| `plan_output` | int | Y | - | 计划生产数：机加开头产线每班计划生产数量，各线可不同 | ✅⚖️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `parent_id` | bigint | Y | MUL | 上级代码；→generator_job_code | ✅🔗 | →generator_job_code |
| `station_group` | varchar(100) | Y | - | 岗位组；同一物理岗位的不同产品产线填写相同组名，排班时互斥 | ✅ |  |

### generator_historicaljobcode_devices
**定义**：工作代号-设备关联历史快照表（simple_history，当前0行） ｜ **流角色**：薪酬-关联变更追溯 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `devices_id` | bigint | Y | MUL | →generator_devices | 🔗 | →generator_devices |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `job_code_id` | bigint | Y | MUL | →generator_job_code | 🔗 | →generator_job_code |

### generator_holiday_date
**定义**：法定假期表：假日名称+日期+结算规则，节假日加班工资倍率依据 ｜ **流角色**：薪酬-节假日工资依据 ｜ **代码**：`generator/holiday_date/model.py` ｜ **行数(估)**：65

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `holiday_name` | varchar(20) | Y | - | 假日名称 | ✅ |  |
| `date_time` | date | Y | UNI | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `settle_rule` | varchar(20) | Y | - | 结算规则 | ✅ |  |

### generator_job_code
**定义**：工作代号表：产线/工序级工作代号树，含计件单价、结算方式、计划产量 ｜ **流角色**：薪酬-计件计时定价基准 ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：1379

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `is_delete` | tinyint(1) | N | - | 是否删除 | ✅ |  |
| `incentive_system` | json | Y | - | 奖励 | ✅ |  |
| `is_production` | varchar(20) | Y | - | 计入产值（是/否）：判断是否最后工序，避免重复计算数量 | ✅⚖️ |  |
| `piecework_price` | decimal(10,2) | Y | - | 计件单价 | ✅ |  |
| `settlement_method` | varchar(20) | Y | - | 计薪方式 | ✅ |  |
| `type` | varchar(20) | Y | - | 工作类型：手动线/自动线 | ✅⚖️ |  |
| `name` | varchar(255) | Y | UNI | 全称 | ✅ |  |
| `dept` | varchar(30) | Y | - | 代码所属部门：生产/质量/工程/物流，字符串拼接或单个 | ✅⚖️ |  |
| `history` | longtext | Y | - | 操作记录 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `parent_id` | bigint | Y | MUL | 上级代码；→generator_job_code | ✅🔗 | →generator_job_code |
| `contribution_ratio` | decimal(8,2) | Y | - | 贡献值占例 | ✅ |  |
| `is_sign` | tinyint(1) | N | - | 标记 | ✅ |  |
| `range_price` | json | Y | - | 区间价格 | ✅ |  |
| `is_floor` | tinyint(1) | N | - | 最底层；True表示最底层(可以被人选择) False表示不是最底层(不能被人选择) | ✅💬 |  |
| `plan_output` | int | Y | - | 计划生产数：机加开头产线每班计划生产数量，各线可不同 | ✅⚖️ |  |
| `station_group` | varchar(100) | Y | - | 岗位组；同一物理岗位的不同产品产线填写相同组名，排班时互斥 | ✅ |  |

### generator_job_code_product
**定义**：M2M中间表: generator_job_code↔generator_product（所属产品-关联产品） ｜ **流角色**：薪酬-代号产品映射 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：1715

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `jobcode_id` | bigint | N | MUL | [推断] →generator_job_code 主键 | 🔍 | →knife_jobcode(推断) |
| `product_id` | bigint | N | MUL | →generator_product 主键 | 🔗 | →generator_product |

### generator_jobcode_devices
**定义**：工作代号-设备关联表：工作代号可使用的设备绑定 ｜ **流角色**：排产-代号设备映射 ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：68

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `devices_id` | bigint | N | MUL | →generator_devices | 🔗 | →generator_devices |
| `job_code_id` | bigint | N | MUL | →generator_job_code | 🔗 | →generator_job_code |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |

### generator_roster
**定义**：花名册：员工档案主数据（合同/社保/公积金/雇主险/紧急联系/入离职） ｜ **流角色**：人事流-员工主数据 ｜ **代码**：`generator/roster/model.py` ｜ **行数(估)**：686

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `avatar` | varchar(255) | Y | - | 照片 | ✅ |  |
| `wechat_id` | varchar(20) | Y | - | 企业微信ID | ✅ |  |
| `contract_count` | int | Y | - | 签合同次数 | ✅ |  |
| `emergency_contact_phone` | varchar(30) | Y | - | 紧急联系人电话 | ✅ |  |
| `emergency_contact_name` | varchar(30) | Y | - | 紧急联系人姓名 | ✅ |  |
| `home_address` | varchar(255) | Y | - | 家庭住址 | ✅ |  |
| `registered_address` | varchar(255) | Y | - | 户籍地址 | ✅ |  |
| `phone` | varchar(20) | Y | - | 联系电话 | ✅ |  |
| `resignation_reason` | varchar(255) | Y | - | 离职原因 | ✅ |  |
| `resignation_date` | date | Y | - | 离职日期 | ✅ |  |
| `contract_end_date` | date | Y | - | 合同截止日期 | ✅ |  |
| `contract_start_date` | date | Y | - | 合同开始日期 | ✅ |  |
| `confirmation_date` | date | Y | - | 转正日期 | ✅ |  |
| `entry_date` | date | Y | - | 入职日期 | ✅ |  |
| `srcb_card_number` | varchar(30) | Y | - | 上海农商银行卡号 | ✅ |  |
| `abc_card_number` | varchar(30) | Y | - | 农业银行卡号 | ✅ |  |
| `company` | varchar(20) | Y | - | 所在公司（挂靠）：治通/广汇/泰峰/智机 | ✅⚖️ |  |
| `provident_fund` | tinyint(1) | Y | - | 公积金：1正常缴纳 0未缴纳 | ✅⚖️ |  |
| `social_security` | tinyint(1) | Y | - | 社保：1正常缴纳 0未缴纳 | ✅⚖️ |  |
| `health_report` | varchar(10) | Y | - | 体检报告；枚举[有=有,无=无,异常=异常] | ✅🔢 |  |
| `employer_insurance` | tinyint(1) | Y | - | 雇主险：1已购买 0未购买 | ✅⚖️ |  |
| `residence_permit` | tinyint(1) | Y | - | 居住证：1有 0无 | ✅⚖️ |  |
| `veteran_status` | tinyint(1) | Y | - | 退役军人：1是 0否 | ✅⚖️ |  |
| `political_status` | varchar(10) | Y | - | 政治面貌 | ✅ |  |
| `work_certificate` | varchar(100) | Y | - | 作业证书 | ✅ |  |
| `major` | varchar(30) | Y | - | 专业 | ✅ |  |
| `education` | varchar(20) | Y | - | 学历 | ✅ |  |
| `location` | varchar(30) | Y | - | 所在地 | ✅ |  |
| `position` | varchar(30) | Y | - | 岗位 | ✅ |  |
| `department` | varchar(30) | Y | - | 部门 | ✅ |  |
| `employee_id` | varchar(20) | Y | UNI | 工号 | ✅ | →system_users(推断) |
| `id_number` | varchar(18) | Y | - | 身份证号码 | ✅ |  |
| `name` | varchar(30) | Y | - | 姓名 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `type_work` | varchar(10) | Y | - | 工种 | ✅ |  |
| `site` | varchar(10) | Y | - | 工作站点：治通/广汇/泰峰/智机/娄塘 | ✅⚖️ |  |

### generator_salary
**定义**：工资表：员工逐日报工工资明细（计件/计时/加班/津贴/奖罚），gross_wage需多条叠加 ｜ **流角色**：薪酬-日工资核算 ｜ **代码**：`generator/salary/model.py` ｜ **行数(估)**：253374

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `output_value` | decimal(13,2) | Y | - | 产值：产品的产值 | ✅⚖️ |  |
| `contribution_value` | decimal(13,2) | Y | - | 贡献值 | ✅ |  |
| `gross_wage` | decimal(13,2) | Y | - | 合计工资：最后结算的总工资 | ✅⚖️ |  |
| `piece_rate_wage` | decimal(13,2) | Y | - | 计件工资：按计件结算的工资 | ✅⚖️ |  |
| `hourly_wage` | decimal(13,2) | Y | - | 计时工资：按计时结算的工资 | ✅⚖️ |  |
| `holiday_overtime` | decimal(13,2) | Y | - | 假日加班：假日加班的工资 | ✅⚖️ |  |
| `regular_overtime` | decimal(13,2) | Y | - | 平时加班：平时加班的工资 | ✅⚖️ |  |
| `normal_salary` | decimal(13,2) | Y | - | 正常工资：每天正常的工资 | ✅⚖️ |  |
| `night_shift_allowance` | decimal(13,2) | Y | - | 夜班补贴 | ✅ |  |
| `other_subsidies` | decimal(13,2) | Y | - | 其他补贴 | ✅ |  |
| `reward` | decimal(13,2) | Y | - | 奖励 | ✅ |  |
| `quality` | decimal(13,2) | Y | - | 质量奖 | ✅ |  |
| `overproduction` | decimal(13,2) | Y | - | 超产奖励 | ✅ |  |
| `production_target` | decimal(13,2) | Y | - | 达产奖励 | ✅ |  |
| `settlement_method` | varchar(255) | Y | - | 结算方式：计件/计时 | ✅⚖️ |  |
| `contribution_ratio` | decimal(13,2) | Y | - | 贡献值占例 | ✅ |  |
| `production_value` | decimal(13,2) | Y | - | 产值单价 | ✅ |  |
| `time_price` | decimal(13,2) | Y | - | 计时单价 | ✅ |  |
| `piecework_price` | decimal(13,2) | Y | - | 计件单价 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `newscheduling_id` | bigint | Y | UNI | 工作代号；→generator_newscheduling | ✅🔗 | →generator_newscheduling |
| `pattern` | varchar(20) | Y | - | 模式：1倍/2倍/3倍（该条工资的工资倍率） | ✅⚖️ |  |
| `is_change` | tinyint(1) | Y | - | 手动更改 | ✅ |  |
| `ticket_sum` | decimal(13,2) | Y | - | 奖罚单：奖罚单工资金额，可为正值或负值 | ✅⚖️ |  |

### generator_user_product_matrix
**定义**：[推断] 人力矩阵统计表：按人×产品×工序×月份汇总工时产量质量及五维评分 ｜ **流角色**：人力能力评估-排产适配 ｜ **行数(估)**：6627

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `user` | varchar(50) | N | MUL | [推断] 员工（姓名/工号） | 🔍 |  |
| `product_name` | varchar(50) | N | MUL | [推断] 产品名称 | 🔍 |  |
| `process` | varchar(30) | Y | MUL | [推断] 工序（工作代号首段，如密封/机加/清整） | 🔍 |  |
| `stat_month` | varchar(7) | N | MUL | [推断] 统计月份YYYY-MM，全量用ALL | 🔍 |  |
| `dept` | varchar(20) | Y | - | [推断] 部门 | 🔍 |  |
| `site` | varchar(20) | Y | - | [推断] 工作地点 | 🔍 |  |
| `total_work_hours` | decimal(13,2) | Y | - | [推断] 累计工时 | 🔍 |  |
| `total_output` | int | N | - | [推断] 累计产量 | 🔍 |  |
| `avg_output_per_hour` | decimal(10,4) | Y | - | [推断] 单位工时产量（时均产量） | 🔍 |  |
| `output_per_hour_std` | decimal(10,4) | Y | - | [推断] 时均产量标准差（效率稳定性度量） | 🔍 |  |
| `total_industrial_waste` | int | N | - | [推断] 累计工废数量 | 🔍 |  |
| `total_scrap_waste` | int | N | - | [推断] 累计料废数量（仅参考） | 🔍 |  |
| `quality_rate` | decimal(6,4) | Y | - | [推断] 良品率 | 🔍 |  |
| `record_count` | int | N | - | [推断] 报工记录条数 | 🔍 |  |
| `work_day_count` | int | N | - | [推断] 累计工作天数 | 🔍 |  |
| `efficiency_score` | decimal(6,4) | Y | - | [推断] 效率得分 | 🔍 |  |
| `quality_score` | decimal(6,4) | Y | - | [推断] 质量得分 | 🔍 |  |
| `experience_score` | decimal(6,4) | Y | - | [推断] 经验得分 | 🔍 |  |
| `stability_score` | decimal(6,4) | Y | - | [推断] 稳定性得分 | 🔍 |  |
| `composite_score` | decimal(6,4) | Y | - | [推断] 综合适配度评分 | 🔍 |  |
| `last_stat_date` | date | Y | - | [推断] 最近统计日期 | 🔍 |  |
| `update_datetime` | datetime | Y | - | [推断] 修改时间 | 🔍 |  |
| `create_datetime` | datetime | Y | - | [推断] 创建时间 | 🔍 |  |
| `remark` | varchar(255) | Y | - | [推断] 备注 | 🔍 |  |
| `is_qualified` | tinyint(1) | Y | - | [推断] 是否达到样本门槛（达标才参与评奖） | 🔍 |  |

---

## 同域兄弟模块
- [[05-人事系统域/考勤打卡模块-fuadmin数据字典2|考勤打卡模块]]
- [[05-人事系统域/日报任务模块-fuadmin数据字典2|日报任务模块]]
- [[05-人事系统域/用户权限模块-fuadmin数据字典2|用户权限模块]]
- [[05-人事系统域/05-人事系统域-业务流|05-人事系统域业务流(代码验证版)]]
