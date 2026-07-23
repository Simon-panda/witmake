---
title: liqiang-定制模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# 定制模块模块 · fuadmin 数据字典
> 域: 06-其他定制 | 表数: 3 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 2 Agent快速上岗指南

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 3 数据字典

### generator_liqiang_inventory（约 40 行）
业务定义: 见同域总览或相关主模块 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | id | id（原注释） | high |
| product_name | varchar(100) | N | - | 产品名称 | 产品名称（原注释） | high |
| date | date | Y | - | 时间 | 时间（原注释） | high |
| summary_total | int | Y | - | 汇总合计 | 汇总合计（原注释） | high |
| logistics_balance | int | Y | - | 物流结存 | 物流结存（原注释） | high |
| difference | int | Y | - | 差异 | 差异（原注释） | high |
| remark | varchar(255) | Y | - | 备注 | 备注（原注释） | high |
| modifier | varchar(255) | Y | - | 创建者 | 创建者（原注释） | high |
| update_datetime | datetime(6) | Y | - | 更新时间 | 更新时间（原注释） | high |
| create_datetime | datetime(6) | Y | - | 创建时间 | 创建时间（原注释） | high |

### generator_liqiang_logistics_cost（约 50 行）
业务定义: 见同域总览或相关主模块 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | id | id（原注释） | high |
| project | varchar(100) | N | - | 项目 | 项目（原注释） | high |
| date | char(7) | N | - | 年月信息(格式:YYYY-MM) | 年月信息(格式:YYYY-MM)（原注释） | high |
| product_category | varchar(50) | Y | - | 产品分类 | 产品分类（原注释） | high |
| route_address | varchar(200) | Y | - | 路线/地址 | 路线/地址（原注释） | high |
| quantity | int | Y | - | 数量 | 数量（原注释） | high |
| amount | decimal(15,2) unsigned | Y | - | 金额 | 金额（原注释） | high |
| unit_cost | decimal(10,2) unsigned | Y | - | 单位成本 | 单位成本（原注释） | high |
| target_unit_cost | decimal(10,2) unsigned | Y | - | 目标单位成本 | 目标单位成本（原注释） | high |
| standard_cost | decimal(10,2) unsigned | Y | - | 标准成本 | 标准成本（原注释） | high |
| completion_rate | decimal(5,2) unsigned | Y | - | 完成率 | 完成率（原注释） | high |
| remark | varchar(255) | Y | - | 备注 | 备注（原注释） | high |
| modifier | varchar(255) | Y | - | 创建者 | 创建者（原注释） | high |
| update_datetime | datetime(6) | Y | - | 更新时间 | 更新时间（原注释） | high |
| create_datetime | datetime(6) | Y | - | 创建时间 | 创建时间（原注释） | high |

### generator_liqiang_report_journals（约 10777 行）
业务定义: 见同域总览或相关主模块 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | id | id（原注释） | high |
| journal_uuid | varchar(100) | N | - | 汇报记录唯一标识 | 汇报记录唯一标识（原注释） | high |
| template_name | varchar(100) | Y | - | 汇报表单名称 | 汇报表单名称（原注释） | high |
| report_time | datetime | Y | - | 汇报时间 | 汇报时间（原注释） | high |
| day_time | datetime | Y | - | 日报时间 | 日报时间（原注释） | high |
| submitter_userid | varchar(50) | Y | - | 提交者用户ID | 提交者用户ID（原注释） | high |
| today_content | varchar(2000) | Y | - | 今日内容 | 今日内容（原注释） | high |
| tomorrow_content | varchar(2000) | Y | - | 明日内容 | 明日内容（原注释） | high |
| receivers_userids | varchar(2000) | Y | - | 汇报接收对象 | 汇报接收对象（原注释） | high |
| readed_receivers_userids | varchar(2000) | Y | - | 汇报已读用户 | 汇报已读用户（原注释） | high |
| remark | varchar(255) | Y | - | 备注 | 备注（原注释） | high |
| modifier | varchar(255) | Y | - | 创建者 | 创建者（原注释） | high |
| update_datetime | datetime(6) | Y | - | 更新时间 | 更新时间（原注释） | high |
| create_datetime | datetime(6) | Y | - | 创建时间 | 创建时间（原注释） | high |

## 4 模块ER图

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 5 跨模块接口

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 6 字段备注改进建议

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 相关页面
- [[answer-定制模块-fuadmin数据字典]]
- [[fuadmin数据字典总览]]
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
