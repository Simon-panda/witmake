---
title: total模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, total]
---

# total模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 15 | 代码锚定: 12(80%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/total模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_total_power` | 泰峰总电量 | 738910 | 💻 |

---

### generator_total_power
**定义**：泰峰总电量 ｜ **代码**：`generator/total_power/model.py` ｜ **行数(估)**：738910

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `accumulated_electricity_consumption` | varchar(255) | Y | - | 累计用电量 | ✅ |  |
| `active_power` | varchar(255) | Y | - | 有功功率 | ✅ |  |
| `time` | datetime(6) | Y | - | 时间（界面:用时） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `minute_electricity_consumption` | int | Y | - | 分钟用电量 | ✅ |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |
