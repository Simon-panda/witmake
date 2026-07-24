---
title: misc-zj2315模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# zj2315模块 · fuadmin 数据字典
> 域: 06-其他定制 | 表数: 3 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（待 enrich 补充）

## 2 Agent快速上岗指南

（待 enrich 补充）

## 3 数据字典

### zj2315_e38_data（约 46996 行）
业务定义: （待补充） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| ID | int | N | PRI | - | 数值字段[推断-待确认] | low |
| USER_NAME | varchar(100) | Y | - | - | 文本字段[推断-待确认] | low |
| PROJECT_NAME | varchar(100) | Y | - | - | 文本字段[推断-待确认] | low |
| QR_CODEE | varchar(100) | Y | - | - | 文本字段[推断-待确认] | low |
| TOTALT_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| CONCENTRATION | float | Y | - | - | 数值（小数）[推断-待确认] | low |
| POSITIVE_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| SIDE_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| UNDERSIDE_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| INNER_30_TOOL_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| INNER_18_TOOL_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| SMALL_45_OUTER_TOOL_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| LARGE_45_OUTER_TOOL_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| OUTER_116_TOOL_TIME | int | Y | - | - | 数值字段[推断-待确认] | low |
| SOURCE_ADDR | varchar(500) | Y | - | - | 文本字段[推断-待确认] | low |
| CREATE_DATE | timestamp | Y | - | - | 待确认 | low |
| THREADED_HOLE_COUNT | int | Y | - | - | 数值字段[推断-待确认] | low |
| PIN_HOLE_COUNT | int | Y | - | - | 数值字段[推断-待确认] | low |

### zj2315_e38_inspection_data（约 0 行）
业务定义: （待补充） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| ID | int | N | PRI | - | 数值字段[推断-待确认] | low |
| USER_NAME | varchar(100) | Y | - | - | 文本字段[推断-待确认] | low |
| CREATE_DATE | timestamp | Y | - | - | 待确认 | low |

### zj2315_e38_threaded_hole（约 0 行）
业务定义: （待补充） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| ID | int | N | PRI | - | 数值字段[推断-待确认] | low |
| TIME_STAMP | varchar(100) | Y | UNI | - | 文本字段[推断-待确认] | low |
| THREADED_HOLE_COUNT | int | Y | - | - | 数值字段[推断-待确认] | low |
| PIN_HOLE_COUNT | int | Y | - | - | 数值字段[推断-待确认] | low |
| CREATE_DATE | timestamp | Y | - | - | 待确认 | low |

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
- [[misc-triangle模块-fuadmin数据字典]]
- [[test-定制模块-fuadmin数据字典]]
- [[零散模块总览-fuadmin数据字典]]
