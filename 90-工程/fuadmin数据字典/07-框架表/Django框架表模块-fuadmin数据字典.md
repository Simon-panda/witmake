---
title: Django框架表模块-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引, python]
---

# auth框架模块 · fuadmin 数据字典
> 域: 07-框架表 | 表数: 16 | 用途: Agent基础文件 | 生成: 2026-07-23

# 07-框架表 · django-auth框架概述

本模块16张表全部为 Django 及 django-celery-beat/results 框架自带的标准表，不承载业务数据。auth_group/auth_permission 原生权限体系在本项目中基本闲置（实际权限走 05-人事系统域 system_role 自定义体系），django_admin_log 是唯一与业务用户表硬桥接的框架表（user_id FK→system_users.id），celery beat/results 七表支撑后台定时任务调度与结果存储（taskresult 约26.7万行为主要增长表），django_content_type/migrations/session 为框架运行底座。日常运维只需关注 celery 调度配置与 taskresult 清理策略，其余表交由框架自管理。

# 07-框架表 · django-auth框架上岗指南

16张表均为框架标准表，按职能分四组。业务排查一般只碰 django_admin_log 与 celery 两组。

## A. auth权限组（3表，原生RBAC，本项目基本闲置）

Django 自带"组-权限"模型；项目实际权限走 system_role 自定义体系，auth_group 两表 0 行，auth_permission 仅 132 行框架默认权限（如 add_logentry）。

| 表 | 说明 | 关键字段 |
|---|---|---|
| auth_group | 用户组定义（0行未用） | name 唯一 |
| auth_group_permissions | 组-权限桥（0行未用） | group_id→auth_group、permission_id→auth_permission 双FK |
| auth_permission | 权限点（132行框架默认） | content_type_id→django_content_type、codename（content_type+codename 唯一） |

## B. admin日志组（1表，与业务用户体系硬桥接）

Django admin 后台操作审计表，是本模块唯一与业务表硬绑定的表。

| 表 | 说明 | 关键字段 |
|---|---|---|
| django_admin_log | admin后台变更审计（0行，admin站点可能未启用或定期清理，待确认） | **user_id 硬FK→system_users.id**（索引名 django_admin_log_user_id_c564eba6_fk_system_users_id，证明项目用自定义 system_users 替代 auth_user）；content_type_id→django_content_type；action_flag 小枚举（1新增/2修改/3删除）；object_id/object_repr 被操作对象 |

## C. celery调度组（7表，beat调度+results存储）

django-celery-beat 的"调度定义四表+任务主表+变更戳"+ django-celery-results 的"结果三表"。业务定时任务（如"泰峰电量同步监控"）在 periodictask 注册，执行结果落 taskresult（约26.7万行，需定期清理策略，框架自带 celery.backend_cleanup 任务）。

| 表 | 说明 | 关键字段 |
|---|---|---|
| django_celery_beat_crontabschedule | crontab调度定义（13行） | minute/hour/day_of_week/day_of_month/month_of_year/timezone（样本：每天4点 Asia/Shanghai） |
| django_celery_beat_intervalschedule | 间隔调度定义（7行） | every+period（样本：10 seconds、1 hours） |
| django_celery_beat_clockedschedule | 一次性定时调度（0行） | clocked_time |
| django_celery_beat_solarschedule | 天文事件调度（0行） | event+latitude+longitude 唯一 |
| django_celery_beat_periodictask | 定时任务主表（17行） | name 唯一、task 任务路径（样本 system.tasks.test_task）、crontab_id/interval_id/solar_id/clocked_id 四选一FK、enabled、last_run_at、total_run_count、one_off |
| django_celery_beat_periodictasks | beat调度变更戳（1行） | ident+last_update，仅作beat重载信号 |
| django_celery_results_taskresult | 任务执行结果（~267232行，增长主力） | task_id 唯一、status（样本SUCCESS）、task_name、worker、date_done、traceback、periodic_task_name 冗余任务名 |
| django_celery_results_groupresult | 任务组结果（0行） | group_id 唯一 |
| django_celery_results_chordcounter | chord计数器（0行） | group_id 唯一、sub_tasks、count |

## D. contenttype与框架底座组（3表）

Django 运行时基础设施：模型注册表、迁移历史、会话存储。

| 表 | 说明 | 关键字段 |
|---|---|---|
| django_content_type | 模型注册表（33行） | app_label+model 唯一（样本 admin/logentry、auth/group）；被 auth_permission、django_admin_log FK引用 |
| django_migrations | 迁移历史（240行） | app+name+applied；首迁2024-01-29 |
| django_session | 会话存储（0行，疑似用缓存/签名校验替代，待确认） | session_key 主键、session_data、expire_date |

## 与 system_users 的桥接关系

`django_admin_log.user_id` 是全库框架表中唯一的硬外键（FK→system_users.id，索引名 ..._fk_system_users_id），证明本项目 Django 配置 `AUTH_USER_MODEL` 指向自定义 system_users。其余业务关联均为 creator_id 逻辑引用，无框架级硬FK。05-人事系统域的 system_users_groups / system_users_user_permissions 两表虽为 Django 原生多对多桥（FK→auth_group/auth_permission），但当前未启用。

## 3 数据字典

### auth_group（约 0 行）
业务定义: Django标准：用户组定义，本项目未启用 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| name | varchar(150) | N | UNI | - | 名称[推断] | high |

### auth_group_permissions（约 0 行）
业务定义: Django标准：用户组-权限多对多桥表，未启用 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| group_id | int | N | MUL | - | 关联ID → system_users_groups.id[推断] | mid |
| permission_id | int | N | MUL | - | 关联ID → system_role_permission.id[推断] | mid |

关联: permission_id → auth_permission.id; group_id → auth_group.id

### auth_permission（约 132 行）
业务定义: Django标准：权限点（模型级增删改查），仅框架默认132行 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| name | varchar(255) | N | - | - | 名称[推断] | high |
| content_type_id | int | N | MUL | - | 关联ID → django_content_type.id[推断] | mid |
| codename | varchar(100) | N | - | - | 名称[推断] | high |

关联: content_type_id → django_content_type.id

### django_admin_log（约 0 行）
业务定义: Django标准：admin后台变更审计，user_id硬FK→system_users ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| action_time | datetime(6) | N | - | - | 时间[推断] | high |
| object_id | longtext | Y | - | - | 关联ID（目标表待确认）[推断] | low |
| object_repr | varchar(200) | N | - | - | 文本字段[推断-待确认] | low |
| action_flag | smallint unsigned | N | - | - | 标志位（布尔）[推断] | mid |
| change_message | longtext | N | - | - | 年龄[推断] | high |
| content_type_id | int | Y | MUL | - | 关联ID → django_content_type.id[推断] | mid |
| user_id | bigint | N | MUL | - | 关联ID → system_users.id[推断] | mid |

关联: content_type_id → django_content_type.id; user_id → system_users.id

### django_celery_beat_clockedschedule（约 0 行）
业务定义: celery-beat标准：一次性定时调度定义 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| clocked_time | datetime(6) | N | - | - | 时间[推断] | high |

### django_celery_beat_crontabschedule（约 13 行）
业务定义: celery-beat标准：crontab调度定义（分时日月周） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| minute | varchar(240) | N | - | - | 文本字段[推断-待确认] | low |
| hour | varchar(96) | N | - | - | 文本字段[推断-待确认] | low |
| day_of_week | varchar(64) | N | - | - | 文本字段[推断-待确认] | low |
| day_of_month | varchar(124) | N | - | - | 文本字段[推断-待确认] | low |
| month_of_year | varchar(64) | N | - | - | 文本字段[推断-待确认] | low |
| timezone | varchar(63) | N | - | - | 文本字段[推断-待确认] | low |

### django_celery_beat_intervalschedule（约 7 行）
业务定义: celery-beat标准：固定间隔调度定义 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| every | int | N | - | - | 数值字段[推断-待确认] | low |
| period | varchar(24) | N | - | - | 文本字段[推断-待确认] | low |

### django_celery_beat_periodictask（约 17 行）
业务定义: celery-beat标准：定时任务主表，注册业务周期任务 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| name | varchar(200) | N | UNI | - | 名称[推断] | high |
| task | varchar(200) | N | - | - | 文本字段[推断-待确认] | low |
| args | longtext | N | - | - | 待确认 | low |
| kwargs | longtext | N | - | - | 待确认 | low |
| queue | varchar(200) | Y | - | - | 文本字段[推断-待确认] | low |
| exchange | varchar(200) | Y | - | - | 文本字段[推断-待确认] | low |
| routing_key | varchar(200) | Y | - | - | 文本字段[推断-待确认] | low |
| expires | datetime(6) | Y | - | - | 日期时间[推断] | mid |
| enabled | tinyint(1) | N | - | - | 数值字段[推断-待确认] | low |
| last_run_at | datetime(6) | Y | - | - | 时间[推断] | high |
| total_run_count | int unsigned | N | - | - | 数量[推断] | high |
| date_changed | datetime(6) | N | - | - | 日期时间[推断] | mid |
| description | longtext | N | - | - | 描述[推断] | mid |
| crontab_id | int | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| interval_id | int | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| solar_id | int | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| one_off | tinyint(1) | N | - | - | 数值字段[推断-待确认] | low |
| start_time | datetime(6) | Y | - | - | 时间[推断] | high |
| priority | int unsigned | Y | - | - | 数值字段[推断-待确认] | low |
| headers | longtext | N | - | - | 待确认 | low |
| clocked_id | int | Y | MUL | - | 关联ID（目标表待确认）[推断] | low |
| expire_seconds | int unsigned | Y | - | - | 数值字段[推断-待确认] | low |

关联: clocked_id → django_celery_beat_clockedschedule.id; crontab_id → django_celery_beat_crontabschedule.id; interval_id → django_celery_beat_intervalschedule.id; solar_id → django_celery_beat_solarschedule.id

### django_celery_beat_periodictasks（约 0 行）
业务定义: celery-beat标准：调度变更戳，触发beat重载 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| ident | smallint | N | PRI | - | 待确认 | low |
| last_update | datetime(6) | N | - | - | 日期[推断] | high |

### django_celery_beat_solarschedule（约 0 行）
业务定义: celery-beat标准：天文事件（日出日落）调度定义 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| event | varchar(24) | N | MUL | - | 文本字段[推断-待确认] | low |
| latitude | decimal(9,6) | N | - | - | 数值（小数）[推断-待确认] | low |
| longitude | decimal(9,6) | N | - | - | 数值（小数）[推断-待确认] | low |

### django_celery_results_chordcounter（约 0 行）
业务定义: celery-results标准：chord并行组计数器 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| group_id | varchar(255) | N | UNI | - | 关联ID → system_users_groups.id[推断] | mid |
| sub_tasks | longtext | N | - | - | 待确认 | low |
| count | int unsigned | N | - | - | 数量[推断] | high |

### django_celery_results_groupresult（约 0 行）
业务定义: celery-results标准：任务组执行结果 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| group_id | varchar(255) | N | UNI | - | 关联ID → system_users_groups.id[推断] | mid |
| date_created | datetime(6) | N | MUL | - | 日期时间[推断] | mid |
| date_done | datetime(6) | N | MUL | - | 日期时间[推断] | mid |
| content_type | varchar(128) | N | - | - | 类型[推断] | mid |
| content_encoding | varchar(64) | N | - | - | 文本字段[推断-待确认] | low |
| result | longtext | Y | - | - | 待确认 | low |

### django_celery_results_taskresult（约 267232 行）
业务定义: celery-results标准：任务执行结果明细（26.7万行） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| task_id | varchar(255) | N | UNI | - | 关联ID（目标表待确认）[推断] | low |
| status | varchar(50) | N | MUL | - | 状态（枚举值待确认）[推断] | mid |
| content_type | varchar(128) | N | - | - | 类型[推断] | mid |
| content_encoding | varchar(64) | N | - | - | 文本字段[推断-待确认] | low |
| result | longtext | Y | - | - | 待确认 | low |
| date_done | datetime(6) | N | MUL | - | 日期时间[推断] | mid |
| traceback | longtext | Y | - | - | 待确认 | low |
| meta | longtext | Y | - | - | 待确认 | low |
| task_args | longtext | Y | - | - | 待确认 | low |
| task_kwargs | longtext | Y | - | - | 待确认 | low |
| task_name | varchar(255) | Y | MUL | - | 名称[推断] | high |
| worker | varchar(100) | Y | MUL | - | 文本字段[推断-待确认] | low |
| date_created | datetime(6) | N | MUL | - | 日期时间[推断] | mid |
| periodic_task_name | varchar(255) | Y | - | - | 名称[推断] | high |

### django_content_type（约 33 行）
业务定义: Django标准：模型注册表（app_label+model） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | int | N | PRI | - | 主键ID | high |
| app_label | varchar(100) | N | MUL | - | 文本字段[推断-待确认] | low |
| model | varchar(100) | N | - | - | 规格/型号[推断] | mid |

### django_migrations（约 240 行）
业务定义: Django标准：数据库迁移历史记录 ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| id | bigint | N | PRI | - | 主键ID | high |
| app | varchar(255) | N | - | - | 文本字段[推断-待确认] | low |
| name | varchar(255) | N | - | - | 名称[推断] | high |
| applied | datetime(6) | N | - | - | 日期时间[推断] | mid |

### django_session（约 0 行）
业务定义: Django标准：服务端会话存储（当前0行） ｜ 表注释: -

| 字段 | 类型 | 可空 | 键 | 原始注释 | 推断语义 | 置信度 |
|---|---|---|---|---|---|---|
| session_key | varchar(40) | N | PRI | - | 文本字段[推断-待确认] | low |
| session_data | longtext | N | - | - | 待确认 | low |
| expire_date | datetime(6) | N | MUL | - | 日期[推断] | high |

## 4 模块ER图

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 5 跨模块接口

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 6 字段备注改进建议

（本模块为小型/过渡性模块，业务语义与归属建议见同域《零散模块总览》或域内相关主模块文档）

## 相关页面
- [[fuadmin数据字典总览]]
