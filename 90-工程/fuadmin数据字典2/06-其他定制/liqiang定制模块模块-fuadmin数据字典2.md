---
title: liqiang定制模块模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, liqiang定制模块]
---

# liqiang定制模块模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 3 | 字段: 39 | 代码锚定: 0(0%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/liqiang定制模块模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_liqiang_inventory` | 李强库存结存报表（产品日结存核对） | 40 | 🔍 |
| `generator_liqiang_logistics_cost` | 李强物流成本报表（月度路线成本） | 50 | 🔍 |
| `generator_liqiang_report_journals` | 李强日报汇报记录（今日/明日工作） | 10777 | 🔍 |

---

### generator_liqiang_inventory
**定义**：李强库存结存报表（产品日结存核对） ｜ **流角色**：李强报表-库存 ｜ **行数(估)**：40

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `product_name` | varchar(100) | N | - | [推断] 产品名称 | 🔍 |  |
| `date` | date | Y | - | [推断] 日期 | 🔍 |  |
| `summary_total` | int | Y | - | [推断] 汇总合计 | 🔍 |  |
| `logistics_balance` | int | Y | - | [推断] 物流结存 | 🔍 |  |
| `difference` | int | Y | - | [推断] 差异（汇总-物流结存） | 🔍 |  |
| `remark` | varchar(255) | Y | - | [推断] 备注 | 🔍 |  |
| `modifier` | varchar(255) | Y | - | [推断] 创建者 | 🔍 |  |
| `update_datetime` | datetime(6) | Y | - | [推断] 更新时间 | 🔍 |  |
| `create_datetime` | datetime(6) | Y | - | [推断] 创建时间 | 🔍 |  |

### generator_liqiang_logistics_cost
**定义**：李强物流成本报表（月度路线成本） ｜ **流角色**：李强报表-物流成本 ｜ **行数(估)**：50

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `project` | varchar(100) | N | - | [推断] 项目 | 🔍 |  |
| `date` | char(7) | N | - | [推断] 年月（格式YYYY-MM） | 🔍 |  |
| `product_category` | varchar(50) | Y | - | [推断] 产品分类 | 🔍 |  |
| `route_address` | varchar(200) | Y | - | [推断] 路线/地址 | 🔍 |  |
| `quantity` | int | Y | - | [推断] 数量 | 🔍 |  |
| `amount` | decimal(15,2) unsigned | Y | - | [推断] 金额（元） | 🔍 |  |
| `unit_cost` | decimal(10,2) unsigned | Y | - | [推断] 单位成本 | 🔍 |  |
| `target_unit_cost` | decimal(10,2) unsigned | Y | - | [推断] 目标单位成本 | 🔍 |  |
| `standard_cost` | decimal(10,2) unsigned | Y | - | [推断] 标准成本 | 🔍 |  |
| `completion_rate` | decimal(5,2) unsigned | Y | - | [推断] 完成率（%） | 🔍 |  |
| `remark` | varchar(255) | Y | - | [推断] 备注 | 🔍 |  |
| `modifier` | varchar(255) | Y | - | [推断] 创建者 | 🔍 |  |
| `update_datetime` | datetime(6) | Y | - | [推断] 更新时间 | 🔍 |  |
| `create_datetime` | datetime(6) | Y | - | [推断] 创建时间 | 🔍 |  |

### generator_liqiang_report_journals
**定义**：李强日报汇报记录（今日/明日工作） ｜ **流角色**：李强报表-日报 ｜ **行数(估)**：10777

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | [推断] 主键ID | 🔍 |  |
| `journal_uuid` | varchar(100) | N | - | [推断] 汇报记录唯一标识 | 🔍 |  |
| `template_name` | varchar(100) | Y | - | [推断] 汇报表单名称 | 🔍 |  |
| `report_time` | datetime | Y | - | [推断] 汇报时间 | 🔍 |  |
| `day_time` | datetime | Y | - | [推断] 日报日期 | 🔍 |  |
| `submitter_userid` | varchar(50) | Y | - | [推断] 提交者用户ID | 🔍 |  |
| `today_content` | varchar(2000) | Y | - | [推断] 今日工作内容 | 🔍 |  |
| `tomorrow_content` | varchar(2000) | Y | - | [推断] 明日工作计划 | 🔍 |  |
| `receivers_userids` | varchar(2000) | Y | - | [推断] 汇报接收对象用户ID列表 | 🔍 |  |
| `readed_receivers_userids` | varchar(2000) | Y | - | [推断] 已读接收人用户ID列表 | 🔍 |  |
| `remark` | varchar(255) | Y | - | [推断] 备注 | 🔍 |  |
| `modifier` | varchar(255) | Y | - | [推断] 创建者 | 🔍 |  |
| `update_datetime` | datetime(6) | Y | - | [推断] 更新时间 | 🔍 |  |
| `create_datetime` | datetime(6) | Y | - | [推断] 创建时间 | 🔍 |  |

---

## 同域兄弟模块
- [[06-其他定制/answer定制模块模块-fuadmin数据字典2|answer定制模块模块]]
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
- [[06-其他定制/test定制模块模块-fuadmin数据字典2|test定制模块模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
