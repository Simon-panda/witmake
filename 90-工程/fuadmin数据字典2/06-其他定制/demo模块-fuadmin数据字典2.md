---
title: demo模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, demo]
---

# demo模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 11 | 代码锚定: 0(0%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/demo模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `demo` |  | 0 | 🔍 |

---

### demo
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `remark` | varchar(255) | Y | - | （界面:备注） | 🔍🖥️ |  |
| `modifier` | varchar(255) | Y | - | （界面:修改人） | 🔍🖥️ |  |
| `belong_dept` | int | Y | - | （界面:所属部门） | 🔍🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | （界面:未结单） | 🔍🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | （界面:时间） | 🔍🖥️ |  |
| `sort` | int | Y | - | （界面:排序） | 🔍🖥️ |  |
| `name` | varchar(64) | N | - | （界面:原辅料名称） | 🔍🖥️ |  |
| `code` | varchar(32) | N | - | （界面:奖罚单号） | 🔍🖥️ |  |
| `status` | varchar(64) | N | - | （界面:完成状态） | 🔍🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
