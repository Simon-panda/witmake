---
title: 财务模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 04-订单项目域
tags: [工程, 数据字典2, 代码实证, 财务]
---

# 财务模块 · fuadmin 数据字典2（代码实证版）
> 域: 04-订单项目域 | 表数: 2 | 字段: 28 | 代码锚定: 26(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/04-订单项目域/财务模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_finance_rule` | 财物规则 | 30 | 💻 |
| `generator_finance_subsidies` | 补贴 | 60 | 💻 |

---

### generator_finance_rule
**定义**：财物规则 ｜ **代码**：`generator/finance_rule/model.py` ｜ **行数(估)**：30

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:工作地点） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `value` | decimal(13,2) | Y | - | 值（界面:基础薪资） | ✅🖥️ |  |
| `rule_name` | varchar(20) | Y | - | 规则名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `compute_rule` | varchar(255) | Y | - | 计算规则 | ✅ |  |
| `site` | varchar(20) | Y | - | 工作地点 | ✅ |  |
| `attendance` | decimal(13,2) | Y | - | 出勤天数 | ✅ |  |
| `double` | decimal(13,2) | Y | - | 倍数 | ✅ |  |
| `money` | decimal(13,2) | Y | - | 薪资 | ✅ |  |
| `work_hours` | int | Y | - | 工作小时数 | ✅ |  |

### generator_finance_subsidies
**定义**：补贴 ｜ **代码**：`generator/finance_subsidies/model.py` ｜ **行数(估)**：60

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:姓名/工号） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `subsidies` | decimal(13,2) | Y | - | 补贴 | ✅ |  |
| `site` | varchar(20) | Y | - | 工作地点（界面:合同地点） | ✅🖥️ |  |
| `value` | decimal(13,2) | Y | - | 基础薪资 | ✅ |  |
| `name` | varchar(30) | Y | UNI | 姓名/工号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
