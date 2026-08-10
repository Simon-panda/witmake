---
title: 质量检验模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 质量检验]
---

# 质量检验模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 5 | 字段: 81 | 代码锚定: 80(99%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/质量检验模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_inspection_items` | 5S/对象类检查项目及其检查标准定义 | 7 | 💻 |
| `generator_inspection_points` | 现场巡检点位档案（区域、点位、二维码） | 21 | 💻 |
| `generator_inspection_standards` | 设备点检内容明细及月/季/年度保养标准库 | 74 | 💻 |
| `generator_quality_inspection` | 质量巡检执行记录（巡检人、类型、二维码；多数字段代码注明闲置） | 158130 | 💻 |
| `generator_qualityrapid_response` | 质量异常QRQC快反单：问题分类、原因分析、临时/永久措施与标准化闭环 | 189 | 💻 |

---

### generator_inspection_items
**定义**：5S/对象类检查项目及其检查标准定义 ｜ **流角色**：检查标准定义 ｜ **代码**：`generator/inspection_items/model.py` ｜ **行数(估)**：7

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `inspection_standards` | longtext | Y | - | 检查标准 | ✅ |  |
| `inspection_item` | longtext | Y | - | 检查项目 | ✅ |  |
| `inspection_object_id` | bigint | Y | MUL | 检查对象；→generator_objective | ✅🔗 | →generator_objective |
| `classification_5s_id` | bigint | Y | MUL | 5S分类；→generator_definition_five_s | ✅🔗 | →generator_definition_five_s |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_inspection_points
**定义**：现场巡检点位档案（区域、点位、二维码） ｜ **流角色**：巡检点位主数据 ｜ **代码**：`generator/inspection_points/model.py` ｜ **行数(估)**：21

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `code` | varchar(255) | Y | - | 二维码 | ✅ |  |
| `dot` | varchar(20) | Y | - | 点位 | ✅ |  |
| `area` | varchar(20) | Y | - | 区域 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_inspection_standards
**定义**：设备点检内容明细及月/季/年度保养标准库 ｜ **流角色**：点检保养标准库 ｜ **代码**：`generator/inspection_standards/model.py` ｜ **行数(估)**：74

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `inspection_details` | json | Y | - | 点检内容明细 | ✅ |  |
| `device_type` | varchar(50) | Y | - | 设备类型 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `device_name_id` | bigint | Y | MUL | [推断]设备名称（→generator_devices） | 🔍 |  |
| `annual_maintenance_details` | json | Y | - | 年度保养明细 | ✅⚖️ |  |
| `monthly_maintenance_details` | json | Y | - | 月度保养明细 | ✅⚖️ |  |
| `quarterly_maintenance_details` | json | Y | - | 季度保养明细 | ✅⚖️ |  |

### generator_quality_inspection
**定义**：质量巡检执行记录（巡检人、类型、二维码；多数字段代码注明闲置） ｜ **流角色**：质量巡检执行 ｜ **代码**：`generator/quality_inspection/model.py` ｜ **行数(估)**：158130

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `cc` | varchar(255) | Y | - | 抄送人（代码标注基本未用） | ✅⚖️ |  |
| `img` | json | Y | - | 图片（代码标注基本未用） | ✅⚖️ |  |
| `code` | varchar(255) | Y | - | 二维码（代码标注基本未用） | ✅⚖️ |  |
| `type` | varchar(50) | Y | - | 类型（代码标注基本未用） | ✅⚖️ |  |
| `inspector` | varchar(20) | Y | - | 巡检人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `associated_infor` | varchar(100) | Y | - | 关联信息（代码标注基本未用） | ✅⚖️ |  |

### generator_qualityrapid_response
**定义**：质量异常QRQC快反单：问题分类、原因分析、临时/永久措施与标准化闭环 ｜ **流角色**：质量异常闭环(QRQC) ｜ **代码**：`generator/qualityrapid_response/model.py` ｜ **行数(估)**：189

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `quality_notes` | longtext | Y | - | 品质状况说明 | ✅ |  |
| `StandardizationTable` | longtext | Y | - | 标准化 | ✅ |  |
| `PermanentMeasuresTable` | json | Y | - | 永久措施；[{"key": "1", "person": "13080 牛周义(生产部-主管)", "remark": "", "status": "已完成", "is_send": true, "disabled": true, "ls_method": ["定期对刀库进行保养和清理"], "send_time": "2024-09-14 16:56:18", "status_time": {"finished": "2024-09-14 17:02:44", "progress": ""}, "ls_method_active": ["定期对刀库进行保养和清理"]}, {"key": "2", "person": "15026 夏玉强(质量部-班长)", "remark": "", "status": "已完成", "is_send": false, "disabled": true, "ls_method": ["要求检验员对14.117孔检具百检"], "send_time": "", "status_time": {"finished": "2024-09-14 17:04:15", "progress": ""}, "ls_method_active": ["要求检验员对14.117孔检具百检"]}] | ✅💬 |  |
| `CauseAnalysisTable` | longtext | Y | - | 原因分析 | ✅ |  |
| `TemporaryMeasuresTable` | json | Y | - | 临时措施；[{"key": "1", "person": "21680 张仲华", "remark": "可能是刀柄上粘铝屑了，清理刀库刀套", "status": "已完成", "is_send": false, "disabled": true, "ls_method": ["现场排查刀具情况和机床有无异常"], "send_time": "", "status_time": {"finished": "2024-09-12 14:13:57", "progress": ""}, "ls_method_active": ["现场排查刀具情况和机床有无异常"]}] | ✅💬 |  |
| `priority` | varchar(20) | Y | - | 优先级：紧急/高级/中级/低级 | ✅⚖️ |  |
| `response_name` | varchar(20) | Y | - | 相关负责人（代码标注未使用） | ✅⚖️ |  |
| `picture` | json | Y | - | 相关照片 | ✅ |  |
| `issue_number` | int | Y | - | 问题件数 | ✅ |  |
| `issue_type` | varchar(20) | Y | - | 问题分类：外协加工/进料检验/生产制造/终检/售后(驻厂)/客诉/其他 | ✅⚖️ |  |
| `exception_issue` | longtext | Y | - | 异常问题描述 | ✅ |  |
| `find_time` | date | Y | - | 发现时间 | ✅ |  |
| `finder` | varchar(20) | Y | - | 发现人（工号 姓名） | ✅⚖️ |  |
| `product_name` | varchar(50) | Y | - | 产品名称（可多选，存JSON数组样式字符串） | ✅⚖️ |  |
| `quality_exception` | varchar(50) | Y | - | 异常单号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `job_code` | varchar(255) | Y | - | 工作代号 | ✅ |  |
| `is_end` | tinyint(1) | Y | - | 是否结单（False未结/True已结） | ✅⚖️ |  |
| `cc_send` | json | Y | - | 抄送人 | ✅ |  |
| `PermanentTime` | varchar(50) | Y | - | 永久措施时间；['2025-05-25 21:00', '2025-05-25 21:00'] | ✅💬 |  |
| `TemporaryTime` | varchar(50) | Y | - | 临时措施时间；['2025-05-25 20:06', '2025-05-25 20:06'] | ✅💬 |  |
| `attachment` | json | Y | - | 相关附件 | ✅ |  |
| `mqs` | varchar(255) | Y | - | MQS分类 | ✅ |  |

---

## 同域兄弟模块
- [[03-质量技术域/设备装置模块-fuadmin数据字典2|设备装置模块]]
- [[03-质量技术域/设备模块-fuadmin数据字典2|设备模块]]
- [[03-质量技术域/工装夹具模块-fuadmin数据字典2|工装夹具模块]]
- [[03-质量技术域/刀具模块-fuadmin数据字典2|刀具模块]]
- [[03-质量技术域/维修保养模块-fuadmin数据字典2|维修保养模块]]
- [[03-质量技术域/测量计量模块-fuadmin数据字典2|测量计量模块]]
- [[03-质量技术域/工艺技术模块-fuadmin数据字典2|工艺技术模块]]
- [[03-质量技术域/产品模块-fuadmin数据字典2|产品模块]]
- [[03-质量技术域/工具工装模块-fuadmin数据字典2|工具工装模块]]
- [[03-质量技术域/03-质量技术域-业务流|03-质量技术域业务流(代码验证版)]]
