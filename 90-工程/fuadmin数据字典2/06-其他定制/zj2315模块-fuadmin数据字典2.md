---
title: zj2315模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, zj2315]
---

# zj2315模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 3 | 字段: 26 | 代码锚定: 0(0%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/zj2315模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `zj2315_e38_data` |  | 46996 | 🔍 |
| `zj2315_e38_inspection_data` |  | 0 | 🔍 |
| `zj2315_e38_threaded_hole` |  | 0 | 🔍 |

---

### zj2315_e38_data
**定义**：（待补充） ｜ **行数(估)**：46996

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `ID` | int | N | PRI | 🔍待补充 | 🔍 |  |
| `USER_NAME` | varchar(100) | Y | - | 🔍待补充 | 🔍 |  |
| `PROJECT_NAME` | varchar(100) | Y | - | 🔍待补充 | 🔍 |  |
| `QR_CODEE` | varchar(100) | Y | - | 🔍待补充 | 🔍 |  |
| `TOTALT_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `CONCENTRATION` | float | Y | - | 🔍待补充 | 🔍 |  |
| `POSITIVE_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `SIDE_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `UNDERSIDE_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `INNER_30_TOOL_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `INNER_18_TOOL_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `SMALL_45_OUTER_TOOL_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `LARGE_45_OUTER_TOOL_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `OUTER_116_TOOL_TIME` | int | Y | - | 🔍待补充 | 🔍 |  |
| `SOURCE_ADDR` | varchar(500) | Y | - | 🔍待补充 | 🔍 |  |
| `CREATE_DATE` | timestamp | Y | - | （界面:创建时间） | 🔍🖥️ |  |
| `THREADED_HOLE_COUNT` | int | Y | - | 🔍待补充 | 🔍 |  |
| `PIN_HOLE_COUNT` | int | Y | - | 🔍待补充 | 🔍 |  |

### zj2315_e38_inspection_data
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `ID` | int | N | PRI | 🔍待补充 | 🔍 |  |
| `USER_NAME` | varchar(100) | Y | - | 🔍待补充 | 🔍 |  |
| `CREATE_DATE` | timestamp | Y | - | （界面:创建时间） | 🔍🖥️ |  |

### zj2315_e38_threaded_hole
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `ID` | int | N | PRI | 🔍待补充 | 🔍 |  |
| `TIME_STAMP` | varchar(100) | Y | UNI | 🔍待补充 | 🔍 |  |
| `THREADED_HOLE_COUNT` | int | Y | - | 🔍待补充 | 🔍 |  |
| `PIN_HOLE_COUNT` | int | Y | - | 🔍待补充 | 🔍 |  |
| `CREATE_DATE` | timestamp | Y | - | （界面:创建时间） | 🔍🖥️ |  |
