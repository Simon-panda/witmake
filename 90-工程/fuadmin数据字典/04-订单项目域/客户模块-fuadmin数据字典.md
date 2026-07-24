---
title: 客户模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 管理
tags: [工程, 数据管道, 索引, 管理]
---

# 客户模块 · fuadmin 数据字典
> 域: 04-订单项目域 | 表数: 1 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（待 enrich 补充）

## 2 Agent快速上岗指南

（待 enrich 补充）

## 3 数据字典

### generator_company（约 116 行）
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
| is_active | tinyint(1) | N | - | - | 标志位（布尔）[推断] | mid |
| business_scope | longtext | Y | - | - | 待确认 | low |
| phone_number | varchar(30) | Y | - | - | 编号/代码[推断] | mid |
| address | varchar(255) | Y | - | - | 地址[推断] | high |
| type | varchar(100) | Y | - | - | 类型[推断] | mid |
| legal_representative | varchar(80) | Y | - | - | 文本字段[推断-待确认] | low |
| registration_number | varchar(100) | Y | - | - | 编号/代码[推断] | mid |
| name | varchar(255) | Y | - | - | 名称[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| use_dept | varchar(30) | Y | - | - | 部门[推断] | high |
| relationship | int | Y | - | - | IP地址[推断] | high |

## 4 模块ER图

（待 enrich 补充）

## 5 跨模块接口

（待 enrich 补充）

## 6 字段备注改进建议

（待 enrich 补充）

## 相关页面
- [[fuadmin数据字典总览]]
- [[订单模块-fuadmin数据字典]]
- [[财务模块-fuadmin数据字典]]
- [[项目模块-fuadmin数据字典]]
