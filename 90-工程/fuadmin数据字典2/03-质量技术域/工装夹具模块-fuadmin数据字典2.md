---
title: 工装夹具模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 工装夹具]
---

# 工装夹具模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 3 | 字段: 46 | 代码锚定: 43(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/工装夹具模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_fixture_maintenance_rc` | 夹具维护记录表 | 4 | 💻 |
| `generator_fixture_usage_rc` | 夹具使用记录表 | 2 | 💻 |
| `generator_fixtures` | 夹具表 | 5 | 💻 |

---

### generator_fixture_maintenance_rc
**定义**：夹具维护记录表 ｜ **代码**：`generator/fixture_maintenance_rc/model.py` ｜ **行数(估)**：4

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:夹具） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `content` | longtext | Y | - | 维护内容 | ✅ |  |
| `after_img` | varchar(255) | Y | - | 维修后图片 | ✅ |  |
| `before_img` | varchar(255) | Y | - | 维修前图片 | ✅ |  |
| `user` | varchar(255) | Y | - | 维护人员 | ✅ |  |
| `type` | varchar(255) | Y | - | 维护类型 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 日期时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `fixture_id` | bigint | Y | MUL | 夹具名称；→generator_fixtures | ✅🔗 | →generator_fixtures |

### generator_fixture_usage_rc
**定义**：夹具使用记录表 ｜ **代码**：`generator/fixture_usage_rc/model.py` ｜ **行数(估)**：2

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:夹具名称） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `status` | varchar(255) | Y | - | 使用状态 | ✅ |  |
| `user` | varchar(255) | Y | - | 使用人员 | ✅ |  |
| `purpose_use` | longtext | Y | - | 使用目的 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 日期时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `fixture_id` | bigint | Y | MUL | 夹具名称；→generator_fixtures | ✅🔗 | →generator_fixtures |

### generator_fixtures
**定义**：夹具表 ｜ **代码**：`generator/fixtures/model.py` ｜ **行数(估)**：5

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:设备绑定） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `status` | varchar(255) | Y | - | 状态 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 日期时间 | ✅ |  |
| `manufacturer` | varchar(255) | Y | - | 制造商 | ✅ |  |
| `material` | varchar(255) | Y | - | 材质 | ✅ |  |
| `url` | varchar(255) | Y | - | 图片路径 | ✅ |  |
| `size` | varchar(255) | Y | - | 尺寸 | ✅ |  |
| `type` | varchar(255) | Y | - | 类型 | ✅ |  |
| `name` | varchar(255) | Y | - | 名称 | ✅ |  |
| `code` | varchar(255) | Y | - | 编号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `device_id` | bigint | Y | MUL | 设备名称；→generator_devices | ✅🔗 | →generator_devices |
