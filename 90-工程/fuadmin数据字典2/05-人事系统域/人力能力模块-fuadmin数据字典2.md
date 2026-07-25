---
title: 人力能力模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 05-人事系统域
tags: [工程, 数据字典2, 代码实证, 人力能力]
---

# 人力能力模块 · fuadmin 数据字典2（代码实证版）
> 域: 05-人事系统域 | 表数: 11 | 字段: 263 | 代码锚定: 225(86%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/05-人事系统域/人力能力模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_capability_score` | 人力能力评分表 | 5085 | 💻 |
| `generator_employment_registration` | 应聘登记表 | 249 | 💻 |
| `generator_historicaljobcode` | 工作代号表 | 2144 | 📸 |
| `generator_historicaljobcode_devices` |  | 0 | 📸 |
| `generator_holiday_date` | 法定假期 | 65 | 💻 |
| `generator_job_code` | 工作代号表 | 1379 | 💻 |
| `generator_job_code_product` | M2M中间表: generator_job_code ↔ generator_pro | 1715 | 🔗 |
| `generator_jobcode_devices` |  | 68 | 💻 |
| `generator_roster` | 花名册 | 686 | 💻 |
| `generator_salary` | 工资表 | 253374 | 💻 |
| `generator_user_product_matrix` |  | 6627 | 🔍 |

---

### generator_capability_score
**定义**：人力能力评分表 ｜ **代码**：`generator/newscheduling/model.py` ｜ **行数(估)**：5085

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `site` | varchar(20) | Y | MUL | 工作地点 | ✅ |  |
| `dept` | varchar(30) | Y | - | 所属部门 | ✅ |  |
| `job_code` | varchar(255) | Y | - | 线级工作代号 | ✅ |  |
| `product_name` | varchar(500) | Y | MUL | 产品名称 | ✅ |  |
| `line_type` | varchar(20) | Y | - | 工作类型 | ✅ |  |
| `category` | varchar(20) | Y | - | 类别 | ✅ |  |
| `plan_output` | int | Y | - | 计划产量(每班)（界面:计划数量） | ✅🖥️ |  |
| `user_code` | varchar(20) | Y | MUL | 工号 | ✅ | →system_users(推断) |
| `user_name` | varchar(30) | Y | - | 姓名 | ✅ |  |
| `work_days` | int | Y | - | 工作天数 | ✅ |  |
| `unit_hours` | decimal(13,4) | Y | - | 单件工时 | ✅ |  |
| `oph` | decimal(10,2) | Y | - | （界面:时产量(件/时)） | 🔍🖥️ |  |
| `attain_rate` | decimal(8,4) | Y | - | 产量达成率 | ✅ |  |
| `quality_rate` | decimal(8,4) | Y | - | 良率 | ✅ |  |
| `downtime_rate` | decimal(8,4) | Y | - | 宕机率 | ✅ |  |
| `eff_score` | decimal(6,4) | Y | - | 效率子分 | ✅ |  |
| `attain_score` | decimal(6,4) | Y | - | 达成子分 | ✅ |  |
| `stability_score` | decimal(6,4) | Y | - | （界面:稳定性） | 🔍🖥️ |  |
| `exp_score` | decimal(6,4) | Y | - | 经验子分 | ✅ |  |
| `recency_days` | int | Y | - | 距最近一次作业天数 | ✅ |  |
| `recency_score` | decimal(6,4) | Y | - | 近期性子分 | ✅ |  |
| `score` | decimal(6,4) | Y | - | 综合评分（界面:综合分） | ✅🖥️ |  |
| `rank_in_line` | int | Y | - | 该线内排名 | ✅ |  |
| `day_cap` | tinyint(1) | N | - | 白班做过 | ✅ |  |
| `night_cap` | tinyint(1) | N | - | 夜班做过 | ✅ |  |
| `calc_time` | datetime | Y | - | 本次计算时间 | ✅ |  |

### generator_employment_registration
**定义**：应聘登记表 ｜ **代码**：`generator/employment_registration/model.py` ｜ **行数(估)**：249

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:状态） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间（界面:填表时间） | ✅📦🖥️ |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `state` | int | Y | - | 状态；0淘汰 1录用 2面试中 | ✅💬 |  |
| `company` | varchar(20) | Y | - | 所在公司；挂靠的公司 治通/广汇/泰峰/智机/中蓝/挂中蓝 等等 | ✅💬 |  |

### generator_historicaljobcode
**定义**：工作代号表 ｜ **类型**：📸历史快照 ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：2144

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 是否启用（界面:状态） | ✅🖥️ |  |
| `is_delete` | tinyint(1) | N | - | 是否删除（界面:封存） | ✅🖥️ |  |
| `incentive_system` | json | Y | - | 奖励 | ✅ |  |
| `is_production` | varchar(20) | Y | - | 计入产值；是 否 判断产品是否是最后一个工序避免重复计算数量 | ✅💬 |  |
| `range_price` | json | Y | - | 区间价格 | ✅ |  |
| `piecework_price` | decimal(10,2) | Y | - | 计件单价 | ✅ |  |
| `settlement_method` | varchar(20) | Y | - | 计薪方式 | ✅ |  |
| `type` | varchar(20) | Y | - | 工作类型；手动线 #自动线（界面:问题分类） | ✅💬🖥️ |  |
| `name` | varchar(255) | Y | MUL | 全称（界面:原辅料名称） | ✅🖥️ |  |
| `dept` | varchar(30) | Y | - | 代码所属部门；生产,质量,工程,物流 字符串拼接也可以单个 | ✅💬 |  |
| `contribution_ratio` | decimal(8,2) | Y | - | 贡献值占例 | ✅ |  |
| `is_sign` | tinyint(1) | N | - | 标记 | ✅ |  |
| `is_floor` | tinyint(1) | N | - | 最底层；True表示最底层(可以被人选择) False表示不是最底层(不能被人选择)（界面:是否底层） | ✅💬🖥️ |  |
| `plan_output` | int | Y | - | 计划生产数；name以机加开头的产线定义的每班的计划生产数量 每一条线可能不一样（界面:计划数量） | ✅💬🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `parent_id` | bigint | Y | MUL | 上级代码；→generator_job_code（界面:上级归属） | ✅🔗🖥️ | →generator_job_code |
| `station_group` | varchar(100) | Y | - | 岗位组；同一物理岗位的不同产品产线填写相同组名，排班时互斥 | ✅ |  |

### generator_historicaljobcode_devices
**定义**：（待补充） ｜ **类型**：📸历史快照 ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | MUL | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 是否启用（界面:状态） | ✅🖥️ |  |
| `history_id` | int | N | PRI | 历史记录ID | ✅📦 |  |
| `history_date` | datetime(6) | N | MUL | 历史记录时间 | ✅📦 |  |
| `history_change_reason` | varchar(100) | Y | - | 变更原因 | ✅📦 |  |
| `history_type` | varchar(1) | N | - | 变更类型；+新增 / ~修改 / -删除 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `devices_id` | bigint | Y | MUL | →generator_devices | 🔗 | →generator_devices |
| `history_user_id` | bigint | Y | MUL | 操作人 | ✅📦 | →system_users |
| `job_code_id` | bigint | Y | MUL | →generator_job_code | 🔗 | →generator_job_code |

### generator_holiday_date
**定义**：法定假期 ｜ **代码**：`generator/holiday_date/model.py` ｜ **行数(估)**：65

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `holiday_name` | varchar(20) | Y | - | 假日名称 | ✅ |  |
| `date_time` | date | Y | UNI | 时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `settle_rule` | varchar(20) | Y | - | 结算规则 | ✅ |  |

### generator_job_code
**定义**：工作代号表 ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：1379

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:所属部门） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `is_delete` | tinyint(1) | N | - | 是否删除（界面:封存） | ✅🖥️ |  |
| `incentive_system` | json | Y | - | 奖励 | ✅ |  |
| `is_production` | varchar(20) | Y | - | 计入产值；是 否 判断产品是否是最后一个工序避免重复计算数量 | ✅💬 |  |
| `piecework_price` | decimal(10,2) | Y | - | 计件单价 | ✅ |  |
| `settlement_method` | varchar(20) | Y | - | 计薪方式 | ✅ |  |
| `type` | varchar(20) | Y | - | 工作类型；手动线 #自动线 | ✅💬 |  |
| `name` | varchar(255) | Y | UNI | 全称 | ✅ |  |
| `dept` | varchar(30) | Y | - | 代码所属部门；生产,质量,工程,物流 字符串拼接也可以单个 | ✅💬 |  |
| `history` | longtext | Y | - | 操作记录（界面:操作历史） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 上级代码；→generator_job_code | ✅🔗 | →generator_job_code |
| `contribution_ratio` | decimal(8,2) | Y | - | 贡献值占例 | ✅ |  |
| `is_sign` | tinyint(1) | N | - | 标记 | ✅ |  |
| `range_price` | json | Y | - | 区间价格 | ✅ |  |
| `is_floor` | tinyint(1) | N | - | 最底层；True表示最底层(可以被人选择) False表示不是最底层(不能被人选择)（界面:是否底层） | ✅💬🖥️ |  |
| `plan_output` | int | Y | - | 计划生产数；name以机加开头的产线定义的每班的计划生产数量 每一条线可能不一样（界面:计划数量） | ✅💬🖥️ |  |
| `station_group` | varchar(100) | Y | - | 岗位组；同一物理岗位的不同产品产线填写相同组名，排班时互斥 | ✅ |  |

### generator_job_code_product
**定义**：M2M中间表: generator_job_code ↔ generator_product（所属产品-关联产品） ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：1715

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键（界面:列表权限） | 🔗🖥️ |  |
| `jobcode_id` | bigint | N | MUL | 🔍待补充 | 🔍 | →knife_jobcode(推断) |
| `product_id` | bigint | N | MUL | →generator_product 主键（界面:产品） | 🔗🖥️ | →generator_product |

### generator_jobcode_devices
**定义**：（待补充） ｜ **代码**：`generator/job_code/model.py` ｜ **行数(估)**：68

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `devices_id` | bigint | N | MUL | →generator_devices | 🔗 | →generator_devices |
| `job_code_id` | bigint | N | MUL | →generator_job_code | 🔗 | →generator_job_code |
| `is_active` | tinyint(1) | N | - | 是否启用（界面:状态） | ✅🖥️ |  |

### generator_roster
**定义**：花名册 ｜ **代码**：`generator/roster/model.py` ｜ **行数(估)**：686

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
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
| `company` | varchar(20) | Y | - | 所在公司；挂靠的公司 治通/广汇/泰峰/智机 | ✅💬 |  |
| `provident_fund` | tinyint(1) | Y | - | 公积金；1正常缴纳 0未缴纳 | ✅💬 |  |
| `social_security` | tinyint(1) | Y | - | 社保；1正常缴纳 0未缴纳 | ✅💬 |  |
| `health_report` | varchar(10) | Y | - | 体检报告；枚举[有=有,无=无,异常=异常] | ✅🔢 |  |
| `employer_insurance` | tinyint(1) | Y | - | 雇主险；1已购买 0未购买 | ✅💬 |  |
| `residence_permit` | tinyint(1) | Y | - | 居住证；1有 0无 | ✅💬 |  |
| `veteran_status` | tinyint(1) | Y | - | 退役军人；1是 0否 | ✅💬 |  |
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
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `type_work` | varchar(10) | Y | - | 工种 | ✅ |  |
| `site` | varchar(10) | Y | - | 工作站点；治通 广汇 泰峰 智机 娄塘 | ✅💬 |  |

### generator_salary
**定义**：工资表 ｜ **代码**：`generator/salary/model.py` ｜ **行数(估)**：253374

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:工作地点） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `output_value` | decimal(13,2) | Y | - | 产值；产品的产值 | ✅💬 |  |
| `contribution_value` | decimal(13,2) | Y | - | 贡献值 | ✅ |  |
| `gross_wage` | decimal(13,2) | Y | - | 合计工资；最后结算的总工资 | ✅💬 |  |
| `piece_rate_wage` | decimal(13,2) | Y | - | 计件工资；计件的工资 | ✅💬 |  |
| `hourly_wage` | decimal(13,2) | Y | - | 计时工资；计时的工资 | ✅💬 |  |
| `holiday_overtime` | decimal(13,2) | Y | - | 假日加班；假日加班的工资 | ✅💬 |  |
| `regular_overtime` | decimal(13,2) | Y | - | 平时加班；平时加班的工资 | ✅💬 |  |
| `normal_salary` | decimal(13,2) | Y | - | 正常工资；每天正常的工资 | ✅💬 |  |
| `night_shift_allowance` | decimal(13,2) | Y | - | 夜班补贴 | ✅ |  |
| `other_subsidies` | decimal(13,2) | Y | - | 其他补贴 | ✅ |  |
| `reward` | decimal(13,2) | Y | - | 奖励 | ✅ |  |
| `quality` | decimal(13,2) | Y | - | 质量奖 | ✅ |  |
| `overproduction` | decimal(13,2) | Y | - | 超产奖励 | ✅ |  |
| `production_target` | decimal(13,2) | Y | - | 达产奖励 | ✅ |  |
| `settlement_method` | varchar(255) | Y | - | 结算方式；计件 计时 | ✅💬 |  |
| `contribution_ratio` | decimal(13,2) | Y | - | 贡献值占例 | ✅ |  |
| `production_value` | decimal(13,2) | Y | - | 产值单价 | ✅ |  |
| `time_price` | decimal(13,2) | Y | - | 计时单价 | ✅ |  |
| `piecework_price` | decimal(13,2) | Y | - | 计件单价 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `newscheduling_id` | bigint | Y | UNI | 工作代号；→generator_newscheduling | ✅🔗 | →generator_newscheduling |
| `pattern` | varchar(20) | Y | - | 模式；1倍 2倍 3倍 (记录该条工资的工资倍率) | ✅💬 |  |
| `is_change` | tinyint(1) | Y | - | 手动更改 | ✅ |  |
| `ticket_sum` | decimal(13,2) | Y | - | 奖罚单；奖罚单的工资可能为负值 也有可能为正值 | ✅💬 |  |

### generator_user_product_matrix
**定义**：人力矩阵统计表 ｜ **行数(估)**：6627

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `user` | varchar(50) | N | MUL | （界面:员工） | 🔍🖥️ |  |
| `product_name` | varchar(50) | N | MUL | （界面:产品名称） | 🔍🖥️ |  |
| `process` | varchar(30) | Y | MUL | 🔍待补充 | 🔍 |  |
| `stat_month` | varchar(7) | N | MUL | 🔍待补充 | 🔍 |  |
| `dept` | varchar(20) | Y | - | （界面:部门） | 🔍🖥️ |  |
| `site` | varchar(20) | Y | - | （界面:地点） | 🔍🖥️ |  |
| `total_work_hours` | decimal(13,2) | Y | - | 🔍待补充 | 🔍 |  |
| `total_output` | int | N | - | （界面:关联总产数） | 🔍🖥️ |  |
| `avg_output_per_hour` | decimal(10,4) | Y | - | 🔍待补充 | 🔍 |  |
| `output_per_hour_std` | decimal(10,4) | Y | - | 🔍待补充 | 🔍 |  |
| `total_industrial_waste` | int | N | - | （界面:工废） | 🔍🖥️ |  |
| `total_scrap_waste` | int | N | - | （界面:料废） | 🔍🖥️ |  |
| `quality_rate` | decimal(6,4) | Y | - | （界面:良率） | 🔍🖥️ |  |
| `record_count` | int | N | - | （界面:记录数） | 🔍🖥️ |  |
| `work_day_count` | int | N | - | 🔍待补充 | 🔍 |  |
| `efficiency_score` | decimal(6,4) | Y | - | 🔍待补充 | 🔍 |  |
| `quality_score` | decimal(6,4) | Y | - | 🔍待补充 | 🔍 |  |
| `experience_score` | decimal(6,4) | Y | - | 🔍待补充 | 🔍 |  |
| `stability_score` | decimal(6,4) | Y | - | （界面:稳定性） | 🔍🖥️ |  |
| `composite_score` | decimal(6,4) | Y | - | 🔍待补充 | 🔍 |  |
| `last_stat_date` | date | Y | - | 🔍待补充 | 🔍 |  |
| `update_datetime` | datetime | Y | - | （界面:未结单） | 🔍🖥️ |  |
| `create_datetime` | datetime | Y | - | （界面:时间） | 🔍🖥️ |  |
| `remark` | varchar(255) | Y | - | （界面:备注） | 🔍🖥️ |  |
| `is_qualified` | tinyint(1) | Y | - | 🔍待补充 | 🔍 |  |
