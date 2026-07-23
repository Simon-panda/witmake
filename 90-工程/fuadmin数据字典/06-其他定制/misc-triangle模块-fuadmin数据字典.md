---
title: misc-triangle模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# triangle模块 · fuadmin 数据字典
> 域: 06-其他定制 | 表数: 2 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 2 Agent快速上岗指南

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 3 数据字典

### generator_triangle_beam_count_data（约 246 行）
业务定义: 见同域总览或相关主模块 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| remark | varchar(255) | Y | - | - | 备注 | high |
| modifier | varchar(255) | Y | - | - | 最后修改人姓名 | high |
| belong_dept | int | Y | - | - | 所属部门ID | mid |
| update_datetime | datetime(6) | Y | - | - | 最后更新时间 | high |
| create_datetime | datetime(6) | Y | - | - | 创建时间 | high |
| sort | int | Y | - | - | 排序号 | high |
| check_count | int | Y | - | - | 数量[推断] | high |
| datetime | datetime(6) | Y | - | - | 时间[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| _MASK_TO_V2 | bigint | Y | MUL | - | 数值字段[推断-待确认] | low |

### generator_triangle_beam_monitoring_system（约 14210 行）
业务定义: 见同域总览或相关主模块 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| remark | varchar(255) | Y | - | - | 备注 | high |
| modifier | varchar(255) | Y | - | - | 最后修改人姓名 | high |
| belong_dept | int | Y | - | - | 所属部门ID | mid |
| update_datetime | datetime(6) | Y | - | - | 最后更新时间 | high |
| create_datetime | datetime(6) | Y | - | - | 创建时间 | high |
| sort | int | Y | - | - | 排序号 | high |
| user_name | varchar(100) | Y | - | - | 名称[推断] | high |
| project_name | varchar(100) | Y | - | - | 名称[推断] | high |
| qr_codee | varchar(100) | Y | - | - | 文本字段[推断-待确认] | low |
| total_time | double | Y | - | - | 时间[推断] | high |
| ztg_total_time | double | Y | - | - | 时间[推断] | high |
| pin_total_time | double | Y | - | - | 时间[推断] | high |
| location_pin_result_1 | varchar(50) | Y | - | - | 库位/位置[推断] | mid |
| location_pin_result_2 | varchar(50) | Y | - | - | 库位/位置[推断] | mid |
| area_result_1 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_1 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_2 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_2 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_3 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_3 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_4 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_4 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_5 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_5 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_6 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_6 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_7 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_7 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_8 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_8 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_9 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_9 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_10 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_10 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_11 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_11 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_12 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_12 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_13 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_13 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_14 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_14 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_15 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_15 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_16 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_16 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_17 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_17 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_18 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_18 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_19 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_19 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_20 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_20 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_21 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_21 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_22 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_22 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_23 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_23 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_24 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_24 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_25 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_25 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_26 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_26 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_27 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_27 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_28 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_28 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_29 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_29 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| area_result_30 | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| area_time_30 | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| result | varchar(50) | Y | - | - | 文本字段[推断-待确认] | low |
| concentration | double | Y | - | - | 数值（小数）[推断-待确认] | low |
| source_addr | varchar(500) | Y | - | - | 文本字段[推断-待确认] | low |
| start_datetime | datetime(6) | Y | - | - | 时间[推断] | high |
| end_datetime | datetime(6) | Y | - | - | 时间[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| _MASK_TO_V2 | bigint | Y | MUL | - | 数值字段[推断-待确认] | low |

## 4 模块ER图

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 5 跨模块接口

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 6 字段备注改进建议

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 相关页面
- [[answer-定制模块-fuadmin数据字典]]
- [[fuadmin数据字典总览]]
- [[liqiang-定制模块-fuadmin数据字典]]
- [[lizhu-定制模块-fuadmin数据字典]]
- [[misc-alarm模块-fuadmin数据字典]]
- [[misc-commentsmessage模块-fuadmin数据字典]]
- [[misc-cooperation模块-fuadmin数据字典]]
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
- [[misc-zj2315模块-fuadmin数据字典]]
- [[test-定制模块-fuadmin数据字典]]
- [[零散模块总览-fuadmin数据字典]]
