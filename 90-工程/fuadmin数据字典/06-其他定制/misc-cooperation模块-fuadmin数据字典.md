---
title: misc-cooperation模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# cooperation模块 · fuadmin 数据字典
> 域: 06-其他定制 | 表数: 1 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（待 enrich 补充）

## 2 Agent快速上岗指南

（待 enrich 补充）

## 3 数据字典

### generator_cooperation（约 256 行）
业务定义: （待补充） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| modifier | varchar(255) | Y | - | - | 最后修改人姓名 | high |
| belong_dept | int | Y | - | - | 所属部门ID | mid |
| update_datetime | datetime(6) | Y | - | - | 最后更新时间 | high |
| create_datetime | datetime(6) | Y | - | - | 创建时间 | high |
| sort | int | Y | - | - | 排序号 | high |
| support_staff | json | Y | - | - | 待确认 | low |
| end_datetime | datetime(6) | Y | - | - | 时间[推断] | high |
| cc_send | json | Y | - | - | 待确认 | low |
| remark | longtext | Y | - | - | 备注 | high |
| priority | varchar(20) | Y | - | - | 文本字段[推断-待确认] | low |
| product_name | varchar(50) | Y | - | - | 名称[推断] | high |
| job_code_name | varchar(80) | Y | - | - | 名称[推断] | high |
| date_time | datetime(6) | Y | - | - | 时间[推断] | high |
| type | varchar(20) | Y | - | - | 类型[推断] | mid |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| devices | varchar(80) | Y | - | - | 设备[推断] | mid |
| purchase | json | Y | - | - | 待确认 | low |
| target | varchar(40) | Y | - | - | 文本字段[推断-待确认] | low |
| picture | json | Y | - | - | 图片路径[推断] | mid |
| message | json | Y | - | - | 年龄[推断] | high |
| tangential_process | json | Y | - | - | 工序[推断] | mid |
| state | int | Y | - | - | 状态（枚举值待确认）[推断] | mid |

## 4 模块ER图

（待 enrich 补充）

## 5 跨模块接口

（待 enrich 补充）

## 6 字段备注改进建议

（待 enrich 补充）

## 相关页面
- [[answer-定制模块-fuadmin数据字典]]
- [[fuadmin数据字典总览]]
- [[liqiang-定制模块-fuadmin数据字典]]
- [[lizhu-定制模块-fuadmin数据字典]]
- [[misc-alarm模块-fuadmin数据字典]]
- [[misc-commentsmessage模块-fuadmin数据字典]]
- [[misc-definition模块-fuadmin数据字典]]
- [[misc-demo模块-fuadmin数据字典]]
- [[misc-external模块-fuadmin数据字典]]
- [[misc-go模块-fuadmin数据字典]]
- [[misc-management模块-fuadmin数据字典]]
- [[misc-objective模块-fuadmin数据字典]]
- [[misc-public模块-fuadmin数据字典]]
- [[misc-safety模块-fuadmin数据字典]]
- [[misc-site模块-fuadmin数据字典]]
- [[misc-ticket模块-fuadmin数据字典]]
- [[misc-total模块-fuadmin数据字典]]
- [[misc-triangle模块-fuadmin数据字典]]
- [[misc-zj2315模块-fuadmin数据字典]]
- [[test-定制模块-fuadmin数据字典]]
- [[零散模块总览-fuadmin数据字典]]
