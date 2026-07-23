---
title: misc-site模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# site模块 · fuadmin 数据字典
> 域: 06-其他定制 | 表数: 1 | 用途: Agent基础文件 | 生成: 2026-07-23

## 1 模块概述

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 2 Agent快速上岗指南

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 3 数据字典

### generator_site_management（约 323 行）
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
| creator_id | bigint | Y | MUL | - | 创建人ID → system_users.id | high |
| completion_date_rectification | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| deadline_rectification | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| description_countermeasures | varchar(255) | Y | - | - | 描述[推断] | mid |
| inspection_ticket_number | varchar(255) | Y | - | - | 编号/代码[推断] | mid |
| photo_rectification | varchar(255) | Y | - | - | 图片路径[推断] | mid |
| problem_description | varchar(255) | Y | - | - | 描述[推断] | mid |
| problem_discovery_date | varchar(255) | Y | - | - | 日期[推断] | high |
| problem_image | varchar(255) | Y | - | - | 图片路径[推断] | mid |
| region_id | bigint | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| region_map | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| responsible_person_id | bigint | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| inspection_states | varchar(255) | Y | - | - | 规格/型号[推断] | mid |
| inspector_id | bigint | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| history | varchar(1000) | Y | - | - | 文本字段[推断-待确认] | low |
| classification_5_s_id | bigint | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| inspection_standards | varchar(255) | Y | - | - | 规格/型号[推断] | mid |
| problem_items | varchar(255) | Y | - | - | 文本字段[推断-待确认] | low |
| responsible_department_id | bigint | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| rate | int | Y | - | - | 比率/百分比[推断] | high |
| collaborators | json | Y | - | - | 待确认 | low |
| problem_level | varchar(2) | Y | - | - | 等级[推断] | mid |

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
- [[misc-ticket模块-fuadmin数据字典]]
- [[misc-total模块-fuadmin数据字典]]
- [[misc-triangle模块-fuadmin数据字典]]
- [[misc-zj2315模块-fuadmin数据字典]]
- [[test-定制模块-fuadmin数据字典]]
- [[零散模块总览-fuadmin数据字典]]
