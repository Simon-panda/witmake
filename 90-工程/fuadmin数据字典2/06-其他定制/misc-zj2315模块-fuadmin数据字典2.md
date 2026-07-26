---
title: misc-zj2315模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, misc-zj2315]
---

# misc-zj2315模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 3 | 字段: 26 | 代码锚定: 0(0%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/misc-zj2315模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `zj2315_e38_data` | ZJ2315专机E38加工数据（工位刀时/孔数） | 46996 | 🔍 |
| `zj2315_e38_inspection_data` | ZJ2315专机E38检验数据 | 0 | 🔍 |
| `zj2315_e38_threaded_hole` | ZJ2315专机E38螺纹孔/销孔计数 | 0 | 🔍 |

---

### zj2315_e38_data
**定义**：ZJ2315专机E38加工数据（工位刀时/孔数） ｜ **流角色**：专机数据直采 ｜ **行数(估)**：46996

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `ID` | int | N | PRI | [推断] 主键ID | 🔍 |  |
| `USER_NAME` | varchar(100) | Y | - | [推断] 用户名（操作人） | 🔍 |  |
| `PROJECT_NAME` | varchar(100) | Y | - | [推断] 项目/产品名称 | 🔍 |  |
| `QR_CODEE` | varchar(100) | Y | - | [推断] 二维码（拼写沿用外部系统） | 🔍 |  |
| `TOTALT_TIME` | int | Y | - | [推断] 总加工时间 | 🔍 |  |
| `CONCENTRATION` | float | Y | - | [推断] 浓度 | 🔍 |  |
| `POSITIVE_TIME` | int | Y | - | [推断] 正面加工时间 | 🔍 |  |
| `SIDE_TIME` | int | Y | - | [推断] 侧面加工时间 | 🔍 |  |
| `UNDERSIDE_TIME` | int | Y | - | [推断] 底面加工时间 | 🔍 |  |
| `INNER_30_TOOL_TIME` | int | Y | - | [推断] 内30刀具加工时间 | 🔍 |  |
| `INNER_18_TOOL_TIME` | int | Y | - | [推断] 内18刀具加工时间 | 🔍 |  |
| `SMALL_45_OUTER_TOOL_TIME` | int | Y | - | [推断] 小45外刀加工时间 | 🔍 |  |
| `LARGE_45_OUTER_TOOL_TIME` | int | Y | - | [推断] 大45外刀加工时间 | 🔍 |  |
| `OUTER_116_TOOL_TIME` | int | Y | - | [推断] 外116刀具加工时间 | 🔍 |  |
| `SOURCE_ADDR` | varchar(500) | Y | - | [推断] 来源地址 | 🔍 |  |
| `CREATE_DATE` | timestamp | Y | - | [推断] 创建时间 | 🔍 |  |
| `THREADED_HOLE_COUNT` | int | Y | - | [推断] 螺纹孔数量 | 🔍 |  |
| `PIN_HOLE_COUNT` | int | Y | - | [推断] 销孔数量 | 🔍 |  |

### zj2315_e38_inspection_data
**定义**：ZJ2315专机E38检验数据 ｜ **流角色**：专机检验记录 ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `ID` | int | N | PRI | [推断] 主键ID | 🔍 |  |
| `USER_NAME` | varchar(100) | Y | - | [推断] 检验用户名 | 🔍 |  |
| `CREATE_DATE` | timestamp | Y | - | [推断] 创建时间 | 🔍 |  |

### zj2315_e38_threaded_hole
**定义**：ZJ2315专机E38螺纹孔/销孔计数 ｜ **流角色**：专机孔计数 ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `ID` | int | N | PRI | [推断] 主键ID | 🔍 |  |
| `TIME_STAMP` | varchar(100) | Y | UNI | [推断] 时间戳 | 🔍 |  |
| `THREADED_HOLE_COUNT` | int | Y | - | [推断] 螺纹孔数量 | 🔍 |  |
| `PIN_HOLE_COUNT` | int | Y | - | [推断] 销孔数量 | 🔍 |  |
| `CREATE_DATE` | timestamp | Y | - | [推断] 创建时间 | 🔍 |  |

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
- [[06-其他定制/test定制模块模块-fuadmin数据字典2|test定制模块模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
