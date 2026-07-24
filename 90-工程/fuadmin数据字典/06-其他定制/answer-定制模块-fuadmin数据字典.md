---
title: answer-定制模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# 定制模块模块 · fuadmin 数据字典
> 域: 06-其他定制 | 表数: 2 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（待 enrich 补充）

## 2 Agent快速上岗指南

（待 enrich 补充）

## 3 数据字典

### generator_answer_list（约 20 行）
业务定义: （待补充） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| remark | varchar(255) | Y | - | - | 备注 | high |
| modifier | varchar(255) | Y | - | - | 最后修改人姓名 | high |
| belong_dept | int | Y | - | - | 所属部门ID | mid |
| update_datetime | datetime(6) | Y | - | - | 最后更新时间 | high |
| create_datetime | datetime(6) | Y | - | - | 创建时间 | high |
| sort | int | Y | - | - | 排序号 | high |
| link | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| dept_name | varchar(50) | Y | - | - | 名称[推断] | high |
| title | varchar(50) | Y | - | - | 标题[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| headline | varchar(50) | Y | - | - | 产线[推断] | mid |
| passing_score | int | Y | - | - | 评分[推断] | high |
| code | json | Y | - | - | 编号/代码[推断] | mid |
| choice_q | int | Y | - | - | 数值字段[推断-待确认] | low |
| content | longtext | Y | - | - | 内容[推断] | mid |
| estimate_q | int | Y | - | - | 数值字段[推断-待确认] | low |
| must_do | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| type | tinyint(1) | Y | - | - | 类型[推断] | mid |

### generator_answer_sheet（约 105 行）
业务定义: （待补充） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| remark | varchar(255) | Y | - | - | 备注 | high |
| modifier | varchar(255) | Y | - | - | 最后修改人姓名 | high |
| belong_dept | int | Y | - | - | 所属部门ID | mid |
| update_datetime | datetime(6) | Y | - | - | 最后更新时间 | high |
| create_datetime | datetime(6) | Y | - | - | 创建时间 | high |
| sort | int | Y | - | - | 排序号 | high |
| score | double | Y | - | - | 评分[推断] | high |
| dept_name | varchar(50) | Y | - | - | 名称[推断] | high |
| name | varchar(50) | Y | - | - | 名称[推断] | high |
| title | varchar(50) | Y | - | - | 标题[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| answer_type | int | Y | - | - | 类型[推断] | mid |
| code | varchar(50) | Y | - | - | 编号/代码[推断] | mid |
| headline | varchar(50) | Y | - | - | 产线[推断] | mid |
| info | longtext | Y | - | - | 待确认 | low |
| score_type | int | Y | - | - | 类型[推断] | mid |
| time | varchar(50) | Y | - | - | 时间[推断] | high |
| submit_time | datetime(6) | Y | - | - | 时间[推断] | high |

## 4 模块ER图

（待 enrich 补充）

## 5 跨模块接口

（待 enrich 补充）

## 6 字段备注改进建议

（待 enrich 补充）

## 相关页面
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
- [[misc-zj2315模块-fuadmin数据字典]]
- [[test-定制模块-fuadmin数据字典]]
- [[零散模块总览-fuadmin数据字典]]
