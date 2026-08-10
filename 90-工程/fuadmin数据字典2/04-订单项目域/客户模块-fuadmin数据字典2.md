---
title: 客户模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 04-订单项目域
tags: [工程, 数据字典2, 代码实证, 客户]
---

# 客户模块 · fuadmin 数据字典2（代码实证版）
> 域: 04-订单项目域 | 表数: 1 | 字段: 18 | 代码锚定: 18(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/04-订单项目域/客户模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_company` | 客商与公司档案: 按关系类型区分本公司/客户/供应商 | 116 | 💻 |

---

### generator_company
**定义**：客商与公司档案: 按关系类型区分本公司/客户/供应商 ｜ **流角色**：主数据-客商档案 ｜ **代码**：`generator/company/model.py` ｜ **行数(估)**：116

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 状态 | ✅ |  |
| `business_scope` | longtext | Y | - | 经营范围 | ✅ |  |
| `phone_number` | varchar(30) | Y | - | 联系电话 | ✅ |  |
| `address` | varchar(255) | Y | - | 地址 | ✅ |  |
| `type` | varchar(100) | Y | - | 公司类型 | ✅ |  |
| `legal_representative` | varchar(80) | Y | - | 法人代表 | ✅ |  |
| `registration_number` | varchar(100) | Y | - | 注册号 | ✅ |  |
| `name` | varchar(255) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `use_dept` | varchar(30) | Y | - | 使用范围 | ✅ |  |
| `relationship` | int | Y | - | 关系类型: 0本公司/1客户/2供应商 | ✅⚖️ |  |

---

## 同域兄弟模块
- [[04-订单项目域/财务模块-fuadmin数据字典2|财务模块]]
- [[04-订单项目域/订单模块-fuadmin数据字典2|订单模块]]
- [[04-订单项目域/项目模块-fuadmin数据字典2|项目模块]]
- [[04-订单项目域/04-订单项目域-业务流|04-订单项目域业务流(代码验证版)]]
