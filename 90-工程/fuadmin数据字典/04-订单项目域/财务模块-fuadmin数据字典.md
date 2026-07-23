---
title: 财务模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 财务
tags: [工程, 数据管道, 索引, 财务]
---

# 财务模块 · fuadmin 数据字典
> 域: 04-订单项目域 | 表数: 2 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 2 Agent快速上岗指南

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 3 数据字典

### generator_finance_rule（约 30 行）
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
| value | decimal(13,2) | Y | - | - | 数值（小数）[推断-待确认] | low |
| rule_name | varchar(20) | Y | - | - | 名称[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| compute_rule | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| site | varchar(20) | Y | - | - | 站点[推断] | mid |
| attendance | decimal(13,2) | Y | - | - | 数值（小数）[推断-待确认] | low |
| double | decimal(13,2) | Y | - | - | 数值（小数）[推断-待确认] | low |
| money | decimal(13,2) | Y | - | - | 金额[推断] | high |
| work_hours | int | Y | - | - | 数值字段[推断-待确认] | low |

### generator_finance_subsidies（约 60 行）
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
| subsidies | decimal(13,2) | Y | - | - | 数值（小数）[推断-待确认] | low |
| site | varchar(20) | Y | - | - | 站点[推断] | mid |
| value | decimal(13,2) | Y | - | - | 数值（小数）[推断-待确认] | low |
| name | varchar(30) | Y | UNI | - | 名称[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |

## 4 模块ER图

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 5 跨模块接口

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 6 字段备注改进建议

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 相关页面
- [[fuadmin数据字典总览]]
- [[客户模块-fuadmin数据字典]]
- [[订单模块-fuadmin数据字典]]
- [[项目模块-fuadmin数据字典]]
