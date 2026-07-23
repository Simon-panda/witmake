---
title: misc-total模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# total模块 · fuadmin 数据字典
> 域: 06-其他定制 | 表数: 1 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 2 Agent快速上岗指南

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 3 数据字典

### generator_total_power（约 738910 行）
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
| remarks | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| accumulated_electricity_consumption | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| active_power | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| time | datetime(6) | Y | - | - | 时间[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| minute_electricity_consumption | int | Y | - | - | 数值字段[推断-待确认] | low |
| _MASK_TO_V2 | bigint | Y | MUL | - | 数值字段[推断-待确认] | low |
| _MUSID_SYNC_V2 | int unsigned | Y | MUL | - | 数值字段[推断-待确认] | low |

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
- [[misc-triangle模块-fuadmin数据字典]]
- [[misc-zj2315模块-fuadmin数据字典]]
- [[test-定制模块-fuadmin数据字典]]
- [[零散模块总览-fuadmin数据字典]]
