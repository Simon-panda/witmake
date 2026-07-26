---
title: test定制模块模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, test定制模块]
---

# test定制模块模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 2 | 字段: 23 | 代码锚定: 23(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/test定制模块模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_test` | 模板测试（开发测试用） | 0 | 💻 |
| `generator_test_demo` | 测试案例（开发测试用） | 0 | 💻 |

---

### generator_test
**定义**：模板测试（开发测试用） ｜ **流角色**：开发测试 ｜ **代码**：`generator/test/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `icon` | varchar(255) | Y | - | 图标 | ✅ |  |
| `sequence` | decimal(13,4) | Y | - | 排序 | ✅ |  |
| `code` | varchar(255) | Y | - | 代码 | ✅ |  |
| `name` | varchar(255) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_test_demo
**定义**：测试案例（开发测试用） ｜ **流角色**：开发测试 ｜ **代码**：`generator/test_demo/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `des` | longtext | Y | - | 描述 | ✅ |  |
| `code` | decimal(13,4) | Y | - | 编码 | ✅ |  |
| `name` | varchar(255) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

---

## 同域兄弟模块
- [[06-其他定制/answer定制模块模块-fuadmin数据字典2|answer定制模块模块]]
- [[06-其他定制/liqiang定制模块模块-fuadmin数据字典2|liqiang定制模块模块]]
- [[06-其他定制/lizhu定制模块模块-fuadmin数据字典2|lizhu定制模块模块]]
- [[06-其他定制/misc-alarm模块-fuadmin数据字典2|misc-alarm模块]]
- [[06-其他定制/misc-commentsmessage模块-fuadmin数据字典2|misc-commentsmessage模块]]
- [[06-其他定制/misc-cooperation模块-fuadmin数据字典2|misc-cooperation模块]]
- [[06-其他定制/misc-definition模块-fuadmin数据字典2|misc-definition模块]]
- [[06-其他定制/misc-demo模块-fuadmin数据字典2|misc-demo模块]]
- [[06-其他定制/misc-external模块-fuadmin数据字典2|misc-external模块]]
- [[06-其他定制/misc-go模块-fuadmin数据字典2|misc-go模块]]
- [[06-其他定制/misc-management模块-fuadmin数据字典2|misc-management模块]]
- [[06-其他定制/misc-objective模块-fuadmin数据字典2|misc-objective模块]]
- [[06-其他定制/misc-public模块-fuadmin数据字典2|misc-public模块]]
- [[06-其他定制/misc-safety模块-fuadmin数据字典2|misc-safety模块]]
- [[06-其他定制/misc-site模块-fuadmin数据字典2|misc-site模块]]
- [[06-其他定制/misc-ticket模块-fuadmin数据字典2|misc-ticket模块]]
- [[06-其他定制/misc-total模块-fuadmin数据字典2|misc-total模块]]
- [[06-其他定制/misc-triangle模块-fuadmin数据字典2|misc-triangle模块]]
- [[06-其他定制/misc-zj2315模块-fuadmin数据字典2|misc-zj2315模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
