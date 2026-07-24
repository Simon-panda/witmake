---
title: 订单模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 管理
tags: [工程, 数据管道, 索引, 管理]
---

# 订单模块 · fuadmin 数据字典
> 域: 04-订单项目域 | 表数: 5 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（待 enrich 补充）

## 2 Agent快速上岗指南

（待 enrich 补充）

## 3 数据字典

### generator_order_detail_document_mapping（约 4899 行）
业务定义: （待补充） ｜ 表注释: [脏注释-待清理] 'fuadmin.generator_machined_number_view' is not BASE TABLE

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| remark | varchar(255) | Y | - | - | 备注 | high |
| modifier | varchar(255) | Y | - | - | 最后修改人姓名 | high |
| belong_dept | int | Y | - | - | 所属部门ID | mid |
| update_datetime | datetime(6) | Y | - | - | 最后更新时间 | high |
| create_datetime | datetime(6) | Y | - | - | 创建时间 | high |
| sort | int | Y | - | - | 排序号 | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| document_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_document.id[推断] | mid |
| purchase_order_detail_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_detail.id[推断] | mid |
| actual_quantity | decimal(13,2) | Y | - | - | 数量[推断] | high |

### generator_order_detail_document_mapping_gh（约 133 行）
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
| actual_quantity | decimal(13,2) | Y | - | - | 数量[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| document_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_document.id[推断] | mid |
| purchase_order_detail_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_detail.id[推断] | mid |

### generator_order_detail_document_mapping_tf（约 26 行）
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
| actual_quantity | decimal(13,2) | Y | - | - | 数量[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| document_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_document.id[推断] | mid |
| purchase_order_detail_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_detail.id[推断] | mid |

### generator_order_detail_document_mapping_zt（约 0 行）
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
| actual_quantity | decimal(13,2) | Y | - | - | 数量[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| document_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_document.id[推断] | mid |
| purchase_order_detail_id | bigint | N | MUL | - | 关联ID → generator_purchase_order_detail.id[推断] | mid |

### generator_customer_order（约 2361 行）
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
| image | varchar(255) | Y | - | - | 图片路径[推断] | mid |
| count | int | Y | - | - | 数量[推断] | high |
| box_number | int | Y | - | - | 箱数[推断] | mid |
| number | int | Y | - | - | 编号/代码[推断] | mid |
| product_name | varchar(20) | Y | - | - | 名称[推断] | high |
| customer_name | varchar(30) | Y | - | - | 名称[推断] | high |
| site | varchar(30) | Y | - | - | 站点[推断] | mid |
| date | date | Y | - | - | 日期[推断] | high |
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| customer_order_number | varchar(30) | Y | - | - | 编号/代码[推断] | mid |
| order_state | tinyint(1) | Y | - | - | 状态（枚举值待确认）[推断] | mid |

## 4 模块ER图

（待 enrich 补充）

## 5 跨模块接口

（待 enrich 补充）

## 6 字段备注改进建议

（待 enrich 补充）

## 相关页面
- [[fuadmin数据字典总览]]
- [[客户模块-fuadmin数据字典]]
- [[生产计划模块-fuadmin数据字典]]
- [[财务模块-fuadmin数据字典]]
- [[项目模块-fuadmin数据字典]]
