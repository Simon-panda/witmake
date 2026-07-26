---
title: misc-external模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, misc-external]
---

# misc-external模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 3 | 字段: 134 | 代码锚定: 0(0%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/misc-external模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `external_data_d` | 外部设备直采数据表D（59通道，扫码绑定） | 901 | 🔍 |
| `external_data_jzt` | 外部设备直采数据表JZT（47通道） | 6429 | 🔍 |
| `external_data_ym` | 外部设备压力采集表（设定/实际压力） | 37205 | 🔍 |

---

### external_data_d
**定义**：外部设备直采数据表D（59通道，扫码绑定） ｜ **流角色**：设备数据直采落库 ｜ **行数(估)**：901

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `date_time` | datetime | Y | - | [推断] 采集时间 | 🔍 |  |
| `qr_code` | varchar(255) | Y | - | [推断] 二维码（扫码绑定产品/工单） | 🔍 |  |
| `result` | varchar(255) | Y | - | [推断] 采集结果（合格/不合格） | 🔍 |  |
| `data01` | varchar(50) | Y | - | [推断] 采集通道01数据 | 🔍 |  |
| `data02` | varchar(50) | Y | - | [推断] 采集通道02数据 | 🔍 |  |
| `data03` | varchar(50) | Y | - | [推断] 采集通道03数据 | 🔍 |  |
| `data04` | varchar(50) | Y | - | [推断] 采集通道04数据 | 🔍 |  |
| `data05` | varchar(50) | Y | - | [推断] 采集通道05数据 | 🔍 |  |
| `data06` | varchar(50) | Y | - | [推断] 采集通道06数据 | 🔍 |  |
| `data07` | varchar(50) | Y | - | [推断] 采集通道07数据 | 🔍 |  |
| `data08` | varchar(50) | Y | - | [推断] 采集通道08数据 | 🔍 |  |
| `data09` | varchar(50) | Y | - | [推断] 采集通道09数据 | 🔍 |  |
| `data10` | varchar(50) | Y | - | [推断] 采集通道10数据 | 🔍 |  |
| `data11` | varchar(50) | Y | - | [推断] 采集通道11数据 | 🔍 |  |
| `data12` | varchar(50) | Y | - | [推断] 采集通道12数据 | 🔍 |  |
| `data13` | varchar(50) | Y | - | [推断] 采集通道13数据 | 🔍 |  |
| `data14` | varchar(50) | Y | - | [推断] 采集通道14数据 | 🔍 |  |
| `data15` | varchar(50) | Y | - | [推断] 采集通道15数据 | 🔍 |  |
| `data16` | varchar(50) | Y | - | [推断] 采集通道16数据 | 🔍 |  |
| `data17` | varchar(50) | Y | - | [推断] 采集通道17数据 | 🔍 |  |
| `data18` | varchar(50) | Y | - | [推断] 采集通道18数据 | 🔍 |  |
| `data19` | varchar(50) | Y | - | [推断] 采集通道19数据 | 🔍 |  |
| `data20` | varchar(50) | Y | - | [推断] 采集通道20数据 | 🔍 |  |
| `data21` | varchar(50) | Y | - | [推断] 采集通道21数据 | 🔍 |  |
| `data22` | varchar(50) | Y | - | [推断] 采集通道22数据 | 🔍 |  |
| `data23` | varchar(50) | Y | - | [推断] 采集通道23数据 | 🔍 |  |
| `data24` | varchar(50) | Y | - | [推断] 采集通道24数据 | 🔍 |  |
| `data25` | varchar(50) | Y | - | [推断] 采集通道25数据 | 🔍 |  |
| `data26` | varchar(50) | Y | - | [推断] 采集通道26数据 | 🔍 |  |
| `data27` | varchar(50) | Y | - | [推断] 采集通道27数据 | 🔍 |  |
| `data28` | varchar(50) | Y | - | [推断] 采集通道28数据 | 🔍 |  |
| `data29` | varchar(50) | Y | - | [推断] 采集通道29数据 | 🔍 |  |
| `data30` | varchar(50) | Y | - | [推断] 采集通道30数据 | 🔍 |  |
| `data31` | varchar(50) | Y | - | [推断] 采集通道31数据 | 🔍 |  |
| `data32` | varchar(50) | Y | - | [推断] 采集通道32数据 | 🔍 |  |
| `data33` | varchar(50) | Y | - | [推断] 采集通道33数据 | 🔍 |  |
| `data34` | varchar(50) | Y | - | [推断] 采集通道34数据 | 🔍 |  |
| `data35` | varchar(50) | Y | - | [推断] 采集通道35数据 | 🔍 |  |
| `data36` | varchar(50) | Y | - | [推断] 采集通道36数据 | 🔍 |  |
| `data37` | varchar(50) | Y | - | [推断] 采集通道37数据 | 🔍 |  |
| `data38` | varchar(50) | Y | - | [推断] 采集通道38数据 | 🔍 |  |
| `data39` | varchar(50) | Y | - | [推断] 采集通道39数据 | 🔍 |  |
| `data40` | varchar(50) | Y | - | [推断] 采集通道40数据 | 🔍 |  |
| `data41` | varchar(50) | Y | - | [推断] 采集通道41数据 | 🔍 |  |
| `data42` | varchar(50) | Y | - | [推断] 采集通道42数据 | 🔍 |  |
| `data43` | varchar(50) | Y | - | [推断] 采集通道43数据 | 🔍 |  |
| `data44` | varchar(50) | Y | - | [推断] 采集通道44数据 | 🔍 |  |
| `data45` | varchar(50) | Y | - | [推断] 采集通道45数据 | 🔍 |  |
| `data46` | varchar(50) | Y | - | [推断] 采集通道46数据 | 🔍 |  |
| `data47` | varchar(50) | Y | - | [推断] 采集通道47数据 | 🔍 |  |
| `data48` | varchar(50) | Y | - | [推断] 采集通道48数据 | 🔍 |  |
| `data49` | varchar(50) | Y | - | [推断] 采集通道49数据 | 🔍 |  |
| `data50` | varchar(50) | Y | - | [推断] 采集通道50数据 | 🔍 |  |
| `data51` | varchar(50) | Y | - | [推断] 采集通道51数据 | 🔍 |  |
| `data52` | varchar(50) | Y | - | [推断] 采集通道52数据 | 🔍 |  |
| `data53` | varchar(50) | Y | - | [推断] 采集通道53数据 | 🔍 |  |
| `data54` | varchar(50) | Y | - | [推断] 采集通道54数据 | 🔍 |  |
| `data55` | varchar(50) | Y | - | [推断] 采集通道55数据 | 🔍 |  |
| `data56` | varchar(50) | Y | - | [推断] 采集通道56数据 | 🔍 |  |
| `data57` | varchar(50) | Y | - | [推断] 采集通道57数据 | 🔍 |  |
| `data58` | varchar(50) | Y | - | [推断] 采集通道58数据 | 🔍 |  |
| `data59` | varchar(50) | Y | - | [推断] 采集通道59数据 | 🔍 |  |
| `title1` | varchar(50) | Y | - | [推断] 标题/采集标题 | 🔍 |  |
| `create_datetime` | datetime | Y | - | [推断] 入库时间 | 🔍 |  |
| `ID` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断] 外部系统同步掩码（迁移痕迹） | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | [推断] 外部系统同步标识（迁移痕迹） | 🔍 |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断] 外部系统同步时间戳（迁移痕迹） | 🔍 |  |

### external_data_jzt
**定义**：外部设备直采数据表JZT（47通道） ｜ **流角色**：设备数据直采落库 ｜ **行数(估)**：6429

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `date_time` | datetime | Y | - | [推断] 采集时间 | 🔍 |  |
| `qr_code` | varchar(255) | Y | - | [推断] 二维码（扫码绑定产品/工单） | 🔍 |  |
| `result` | varchar(20) | Y | - | [推断] 采集结果（合格/不合格） | 🔍 |  |
| `data01` | varchar(50) | Y | - | [推断] 采集通道01数据 | 🔍 |  |
| `data02` | varchar(50) | Y | - | [推断] 采集通道02数据 | 🔍 |  |
| `data03` | varchar(50) | Y | - | [推断] 采集通道03数据 | 🔍 |  |
| `data04` | varchar(50) | Y | - | [推断] 采集通道04数据 | 🔍 |  |
| `data05` | varchar(50) | Y | - | [推断] 采集通道05数据 | 🔍 |  |
| `data06` | varchar(50) | Y | - | [推断] 采集通道06数据 | 🔍 |  |
| `data07` | varchar(50) | Y | - | [推断] 采集通道07数据 | 🔍 |  |
| `data08` | varchar(50) | Y | - | [推断] 采集通道08数据 | 🔍 |  |
| `data09` | varchar(50) | Y | - | [推断] 采集通道09数据 | 🔍 |  |
| `data10` | varchar(50) | Y | - | [推断] 采集通道10数据 | 🔍 |  |
| `data11` | varchar(50) | Y | - | [推断] 采集通道11数据 | 🔍 |  |
| `data12` | varchar(50) | Y | - | [推断] 采集通道12数据 | 🔍 |  |
| `data13` | varchar(50) | Y | - | [推断] 采集通道13数据 | 🔍 |  |
| `data14` | varchar(50) | Y | - | [推断] 采集通道14数据 | 🔍 |  |
| `data15` | varchar(50) | Y | - | [推断] 采集通道15数据 | 🔍 |  |
| `data16` | varchar(50) | Y | - | [推断] 采集通道16数据 | 🔍 |  |
| `data17` | varchar(50) | Y | - | [推断] 采集通道17数据 | 🔍 |  |
| `data18` | varchar(50) | Y | - | [推断] 采集通道18数据 | 🔍 |  |
| `data19` | varchar(50) | Y | - | [推断] 采集通道19数据 | 🔍 |  |
| `data20` | varchar(50) | Y | - | [推断] 采集通道20数据 | 🔍 |  |
| `data21` | varchar(50) | Y | - | [推断] 采集通道21数据 | 🔍 |  |
| `data22` | varchar(50) | Y | - | [推断] 采集通道22数据 | 🔍 |  |
| `data23` | varchar(50) | Y | - | [推断] 采集通道23数据 | 🔍 |  |
| `data24` | varchar(50) | Y | - | [推断] 采集通道24数据 | 🔍 |  |
| `data25` | varchar(50) | Y | - | [推断] 采集通道25数据 | 🔍 |  |
| `data26` | varchar(50) | Y | - | [推断] 采集通道26数据 | 🔍 |  |
| `data27` | varchar(50) | Y | - | [推断] 采集通道27数据 | 🔍 |  |
| `data28` | varchar(50) | Y | - | [推断] 采集通道28数据 | 🔍 |  |
| `data29` | varchar(50) | Y | - | [推断] 采集通道29数据 | 🔍 |  |
| `data30` | varchar(50) | Y | - | [推断] 采集通道30数据 | 🔍 |  |
| `data31` | varchar(50) | Y | - | [推断] 采集通道31数据 | 🔍 |  |
| `data32` | varchar(50) | Y | - | [推断] 采集通道32数据 | 🔍 |  |
| `data33` | varchar(50) | Y | - | [推断] 采集通道33数据 | 🔍 |  |
| `data34` | varchar(50) | Y | - | [推断] 采集通道34数据 | 🔍 |  |
| `data35` | varchar(50) | Y | - | [推断] 采集通道35数据 | 🔍 |  |
| `data36` | varchar(50) | Y | - | [推断] 采集通道36数据 | 🔍 |  |
| `data37` | varchar(50) | Y | - | [推断] 采集通道37数据 | 🔍 |  |
| `data38` | varchar(50) | Y | - | [推断] 采集通道38数据 | 🔍 |  |
| `data39` | varchar(50) | Y | - | [推断] 采集通道39数据 | 🔍 |  |
| `data40` | varchar(50) | Y | - | [推断] 采集通道40数据 | 🔍 |  |
| `data41` | varchar(50) | Y | - | [推断] 采集通道41数据 | 🔍 |  |
| `data42` | varchar(50) | Y | - | [推断] 采集通道42数据 | 🔍 |  |
| `data43` | varchar(50) | Y | - | [推断] 采集通道43数据 | 🔍 |  |
| `data44` | varchar(50) | Y | - | [推断] 采集通道44数据 | 🔍 |  |
| `data45` | varchar(50) | Y | - | [推断] 采集通道45数据 | 🔍 |  |
| `data46` | varchar(50) | Y | - | [推断] 采集通道46数据 | 🔍 |  |
| `data47` | varchar(50) | Y | - | [推断] 采集通道47数据 | 🔍 |  |
| `title1` | varchar(20) | Y | - | [推断] 标题/采集标题 | 🔍 |  |
| `create_datetime` | datetime | Y | - | [推断] 入库时间 | 🔍 |  |
| `ID` | int | N | PRI | [推断] 主键ID | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断] 外部系统同步掩码（迁移痕迹） | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | [推断] 外部系统同步标识（迁移痕迹） | 🔍 |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断] 外部系统同步时间戳（迁移痕迹） | 🔍 |  |

### external_data_ym
**定义**：外部设备压力采集表（设定/实际压力） ｜ **流角色**：设备数据直采落库 ｜ **行数(估)**：37205

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `date_time` | datetime | Y | - | [推断] 采集时间 | 🔍 |  |
| `qr_code` | varchar(255) | Y | - | [推断] 二维码（扫码绑定产品/工单） | 🔍 |  |
| `variety` | varchar(10) | Y | - | [推断] 品种 | 🔍 |  |
| `type` | varchar(10) | Y | - | [推断] 类型 | 🔍 |  |
| `set_pressure` | decimal(10,0) | Y | - | [推断] 设定压力 | 🔍 |  |
| `pressure_val` | decimal(10,0) | Y | - | [推断] 实际压力值 | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | [推断] 外部系统同步掩码（迁移痕迹） | 🔍 |  |
| `ID` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | [推断] 外部系统同步标识（迁移痕迹） | 🔍 |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断] 外部系统同步时间戳（迁移痕迹） | 🔍 |  |

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
- [[06-其他定制/test定制模块模块-fuadmin数据字典2|test定制模块模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
