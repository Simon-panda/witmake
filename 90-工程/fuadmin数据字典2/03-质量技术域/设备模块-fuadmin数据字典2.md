---
title: 设备模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 设备]
---

# 设备模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 5 | 字段: 97 | 代码锚定: 96(99%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/设备模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_equipment_inspection` | 按点检标准对设备执行日常点检的记录（明细JSON） | 12993 | 💻 |
| `generator_equipment_maintenance_records` | 设备月/季/年周期保养执行记录与上次/下次保养日期 | 1377 | 💻 |
| `generator_equipment_repair` | 新版设备报修工单全流程：报修-接单-检修-评分-完成闭环 | 5896 | 💻 |
| `generator_equipment_repair_report` | 旧版设备报修单及处理情况说明（与新报修表并行使用） | 718 | 💻 |
| `generator_equipment_repair_report_cc_personnel` | M2M中间表: generator_equipment_repair_report↔ | 1934 | 🔗 |

---

### generator_equipment_inspection
**定义**：按点检标准对设备执行日常点检的记录（明细JSON） ｜ **流角色**：设备点检执行 ｜ **代码**：`generator/equipment_inspection/model.py` ｜ **行数(估)**：12993

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `inspection_details` | json | Y | - | 点检明细 | ✅ |  |
| `inspection_time` | datetime(6) | Y | - | 点检时间 | ✅ |  |
| `inspection_number` | varchar(50) | Y | - | 点检单号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `inspection_equipment_id` | bigint | Y | MUL | 点检设备；→generator_devices | ✅🔗 | →generator_devices |
| `inspection_personnel_id` | bigint | Y | MUL | 点检人；→system_users | ✅🔗 | →system_users |
| `inspection_standards_id` | bigint | Y | MUL | 点检标准；→generator_inspection_standards | ✅🔗 | →generator_inspection_standards |

### generator_equipment_maintenance_records
**定义**：设备月/季/年周期保养执行记录与上次/下次保养日期 ｜ **流角色**：设备保养执行 ｜ **代码**：`generator/equipment_maintenance_records/model.py` ｜ **行数(估)**：1377

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `related_photos` | varchar(255) | Y | - | 相关照片 | ✅ |  |
| `maintenance_details` | json | Y | - | 保养明细 | ✅ |  |
| `next_maintenance_date` | date | Y | - | 下次保养日期 | ✅ |  |
| `maintenance_date` | date | Y | - | 保养日期 | ✅ |  |
| `operator_id` | bigint | Y | MUL | 经办人；→system_users | ✅🔗 | →system_users |
| `equipment_id` | bigint | Y | MUL | 设备；→generator_devices | ✅🔗 | →generator_devices |
| `maintenance_order_number` | varchar(255) | Y | - | 保养单号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `last_maintenance_date` | date | Y | - | 上次保养日期 | ✅ |  |
| `maintenance_type` | varchar(255) | Y | - | 保养类型 | ✅ |  |
| `states` | int | Y | - | 状态：1待保养/2已保养 | ✅⚖️ |  |

### generator_equipment_repair
**定义**：新版设备报修工单全流程：报修-接单-检修-评分-完成闭环 ｜ **流角色**：设备报修工单主流程 ｜ **代码**：`generator/equipment_repair/model.py` ｜ **行数(估)**：5896

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `warranty_number` | varchar(40) | Y | - | 报修单号（示例BXDH+日期时间流水） | ✅⚖️ |  |
| `evaluate` | varchar(255) | Y | - | 维修评价 | ✅ |  |
| `problem_description` | varchar(255) | Y | - | 问题描述 | ✅ |  |
| `cc_personnel` | varchar(255) | Y | - | 抄送人员（存'工号 姓名'列表） | ✅⚖️ |  |
| `direct_time` | datetime(6) | Y | - | 接单日期；2025-03-12 08:22:00 | ✅💬 |  |
| `repair_time` | datetime(6) | Y | - | 报修日期；2025-03-12 07:59:00 | ✅💬 |  |
| `rate_time` | datetime(6) | Y | - | 评分时间；2025-03-12 09:00:00 | ✅💬 |  |
| `malfunction` | tinyint(1) | Y | - | 有无故障（True有/False无；有故障需填故障明细） | ✅⚖️ |  |
| `repetition` | tinyint(1) | Y | - | 需要配件（True需要/False不需要；需要时填配件清单） | ✅⚖️ |  |
| `stop_time` | varchar(20) | Y | - | 暂停时长 | ✅ |  |
| `maintain_time` | varchar(20) | Y | - | 维修时长；21:15:05 | ✅💬 |  |
| `order_time` | varchar(20) | Y | - | 接单时长；0:01:23 | ✅💬 |  |
| `inspection_states` | int | Y | - | 订单状态：1待接单/2待检修/3检修中/4已检修/5已评分/6已完成 | ✅⚖️ |  |
| `difficulty_level` | int | Y | - | 难度等级（1-10） | ✅⚖️ |  |
| `emergency_level` | int | Y | - | 紧急等级：1一级(最高)/2二级/3三级/4四级 | ✅⚖️ |  |
| `is_active` | int | Y | - | 状态：2启用/1暂停/0注销 | ✅⚖️ |  |
| `rate` | int | Y | - | 评分（0-5分） | ✅⚖️ |  |
| `mountings` | json | Y | - | 配件清单；[{"key": "1", "name": "履带主动轴", "user": "20011 任广建", "state": "已安装", "number": 1, "remark": "", "qr_code": "", "disabled": false, "use_time": "2025-03-12T00:23:30.499Z"}] | ✅💬 |  |
| `cooperate` | json | Y | - | 配合人；可能有多个人也有可能只有接单人一个人 [{"key": "1", "user": "20011 任广建", "remark": "杨帅通，任万传", "disabled": {"remark": false, "working_time": true, "working_scale": true}, "working_time": "2025-03-11 17:54:06", "working_scale": 100}, [{"key": "1", "user": "21967 严振东", "remark": "", "disabled": {"remark": true, "working_time": true, "working_scale": true}, "working_time": "2025-03-13 01:46:49", "working_scale": 100}]] | ✅💬 |  |
| `history` | json | Y | - | 操作历史 | ✅ |  |
| `fault_detail` | json | Y | - | 故障明细；[[{"img": ["https://zji5g.cn/static/20250429/20250429160843417104_b29413937d5258f2dc5e495222351165_compress.jpg"], "key": "1", "content": "更换定位套，定向轮，叶片", "disabled": false}],{"img": [], "key": "1", "content": "导轨过不去 上面加的油", "disabled": false}] | ✅💬 |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `device_id` | bigint | Y | MUL | 设备；→generator_devices | ✅🔗 | →generator_devices |
| `direct_writer_id` | bigint | Y | MUL | 接单人；→system_users | ✅🔗 | →system_users |
| `repair_applicant_id` | bigint | Y | MUL | 报修人；→system_users | ✅🔗 | →system_users |
| `img` | json | Y | - | 相关照片（图片URL列表） | ✅⚖️ |  |
| `message` | json | Y | - | 留言 | ✅ |  |
| `cnc_personnel` | varchar(40) | Y | - | 机床操作人（工号 姓名） | ✅⚖️ |  |
| `fault_class` | varchar(40) | Y | - | 故障分类 | ✅ |  |
| `zl_personnel` | varchar(255) | Y | - | 质量人员（'工号 姓名'列表） | ✅⚖️ |  |
| `after_img` | json | Y | - | 维修后照片（图片URL列表） | ✅⚖️ |  |

### generator_equipment_repair_report
**定义**：旧版设备报修单及处理情况说明（与新报修表并行使用） ｜ **流角色**：设备报修(旧版) ｜ **代码**：`generator/equipment_repair_report/model.py` ｜ **行数(估)**：718

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `explanation_of_handling_situation` | longtext | Y | - | 处理情况说明 | ✅ |  |
| `fault_details` | json | Y | - | 故障明细 | ✅ |  |
| `repair_completion_date` | datetime(6) | Y | - | 维修完成日期 | ✅ |  |
| `problem_confirmation` | varchar(255) | Y | - | 问题确认 | ✅ |  |
| `maintenance_personnel_id` | bigint | Y | MUL | 安排维修人员；→system_users | ✅🔗 | →system_users |
| `related_photos` | varchar(255) | Y | - | 相关照片 | ✅ |  |
| `problem_description` | longtext | Y | - | 问题描述 | ✅ |  |
| `equipment_id` | bigint | Y | MUL | 设备；→generator_devices | ✅🔗 | →generator_devices |
| `repair_time` | varchar(255) | Y | - | 报修时间 | ✅ |  |
| `repair_applicant_id` | bigint | Y | MUL | 报修人；→system_users | ✅🔗 | →system_users |
| `warranty_number` | varchar(255) | Y | - | 报修单号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `inspection_states` | varchar(255) | Y | - | 状态 | ✅ |  |
| `history` | varchar(1000) | Y | - | 记录 | ✅ |  |
| `quality_id` | bigint | Y | MUL | 质量部介入；→system_users | ✅🔗 | →system_users |
| `rate` | varchar(255) | Y | - | 评分 | ✅ |  |

### generator_equipment_repair_report_cc_personnel
**定义**：M2M中间表: generator_equipment_repair_report↔system_users（抄送人员） ｜ **流角色**：报修抄送关联 ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：1934

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键 | 🔗 |  |
| `equipmentrepairreport_id` | bigint | N | MUL | [推断]→generator_equipment_repair_report 主键 | 🔍 |  |
| `users_id` | bigint | N | MUL | →system_users 主键 | 🔗 | →system_users |

---

## 同域兄弟模块
- [[03-质量技术域/设备装置模块-fuadmin数据字典2|设备装置模块]]
- [[03-质量技术域/工装夹具模块-fuadmin数据字典2|工装夹具模块]]
- [[03-质量技术域/质量检验模块-fuadmin数据字典2|质量检验模块]]
- [[03-质量技术域/刀具模块-fuadmin数据字典2|刀具模块]]
- [[03-质量技术域/维修保养模块-fuadmin数据字典2|维修保养模块]]
- [[03-质量技术域/测量计量模块-fuadmin数据字典2|测量计量模块]]
- [[03-质量技术域/工艺技术模块-fuadmin数据字典2|工艺技术模块]]
- [[03-质量技术域/产品模块-fuadmin数据字典2|产品模块]]
- [[03-质量技术域/工具工装模块-fuadmin数据字典2|工具工装模块]]
- [[03-质量技术域/03-质量技术域-业务流|03-质量技术域业务流(代码验证版)]]
