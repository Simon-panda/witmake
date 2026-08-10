---
title: 工装夹具模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 工装夹具]
---

# 工装夹具模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 3 | 字段: 46 | 代码锚定: 46(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/工装夹具模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_fixture_maintenance_rc` | 工装夹具维护/维修记录（含维护前后照片） | 4 | 💻 |
| `generator_fixture_usage_rc` | 夹具领用/使用登记（使用人、用途、状态） | 2 | 💻 |
| `generator_fixtures` | 工装夹具台账：编码、名称、规格、材质、所属设备 | 5 | 💻 |

---

### generator_fixture_maintenance_rc
**定义**：工装夹具维护/维修记录（含维护前后照片） ｜ **流角色**：夹具维保 ｜ **代码**：`generator/fixture_maintenance_rc/model.py` ｜ **行数(估)**：4

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `content` | longtext | Y | - | 维护内容 | ✅ |  |
| `after_img` | varchar(255) | Y | - | 维修后图片 | ✅ |  |
| `before_img` | varchar(255) | Y | - | 维修前图片 | ✅ |  |
| `user` | varchar(255) | Y | - | 维护人员 | ✅ |  |
| `type` | varchar(255) | Y | - | 维护类型 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 日期时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `fixture_id` | bigint | Y | MUL | 夹具名称；→generator_fixtures | ✅🔗 | →generator_fixtures |

### generator_fixture_usage_rc
**定义**：夹具领用/使用登记（使用人、用途、状态） ｜ **流角色**：夹具使用登记 ｜ **代码**：`generator/fixture_usage_rc/model.py` ｜ **行数(估)**：2

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `status` | varchar(255) | Y | - | 使用状态 | ✅ |  |
| `user` | varchar(255) | Y | - | 使用人员 | ✅ |  |
| `purpose_use` | longtext | Y | - | 使用目的 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 日期时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `fixture_id` | bigint | Y | MUL | 夹具名称；→generator_fixtures | ✅🔗 | →generator_fixtures |

### generator_fixtures
**定义**：工装夹具台账：编码、名称、规格、材质、所属设备 ｜ **流角色**：夹具主数据 ｜ **代码**：`generator/fixtures/model.py` ｜ **行数(估)**：5

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
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
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `device_id` | bigint | Y | MUL | 设备名称；→generator_devices | ✅🔗 | →generator_devices |

---

## 同域兄弟模块
- [[03-质量技术域/设备装置模块-fuadmin数据字典2|设备装置模块]]
- [[03-质量技术域/设备模块-fuadmin数据字典2|设备模块]]
- [[03-质量技术域/质量检验模块-fuadmin数据字典2|质量检验模块]]
- [[03-质量技术域/刀具模块-fuadmin数据字典2|刀具模块]]
- [[03-质量技术域/维修保养模块-fuadmin数据字典2|维修保养模块]]
- [[03-质量技术域/测量计量模块-fuadmin数据字典2|测量计量模块]]
- [[03-质量技术域/工艺技术模块-fuadmin数据字典2|工艺技术模块]]
- [[03-质量技术域/产品模块-fuadmin数据字典2|产品模块]]
- [[03-质量技术域/工具工装模块-fuadmin数据字典2|工具工装模块]]
- [[03-质量技术域/03-质量技术域-业务流|03-质量技术域业务流(代码验证版)]]
