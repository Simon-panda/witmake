---
title: 定制模块模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, 定制模块]
---

# 定制模块模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 2 | 字段: 23 | 代码锚定: 21(91%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/定制模块模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_test` | 模板测试 | 0 | 💻 |
| `generator_test_demo` | 测试案例 | 0 | 💻 |

---

### generator_test
**定义**：模板测试 ｜ **代码**：`generator/test/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `icon` | varchar(255) | Y | - | 图标 | ✅ |  |
| `sequence` | decimal(13,4) | Y | - | 排序 | ✅ |  |
| `code` | varchar(255) | Y | - | 代码 | ✅ |  |
| `name` | varchar(255) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_test_demo
**定义**：测试案例 ｜ **代码**：`generator/test_demo/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `des` | longtext | Y | - | 描述 | ✅ |  |
| `code` | decimal(13,4) | Y | - | 编码 | ✅ |  |
| `name` | varchar(255) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
