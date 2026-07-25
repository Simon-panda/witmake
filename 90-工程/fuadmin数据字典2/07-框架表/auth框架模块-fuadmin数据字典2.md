---
title: auth框架模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 07-框架表
tags: [工程, 数据字典2, 代码实证, auth框架]
---

# auth框架模块 · fuadmin 数据字典2（代码实证版）
> 域: 07-框架表 | 表数: 16 | 字段: 94 | 代码锚定: 94(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/07-框架表/auth框架模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `auth_group` |  | 0 | 🔍 |
| `auth_group_permissions` |  | 0 | 🔍 |
| `auth_permission` |  | 132 | 🔍 |
| `django_admin_log` |  | 0 | 🔍 |
| `django_celery_beat_clockedschedule` |  | 0 | 🔍 |
| `django_celery_beat_crontabschedule` |  | 13 | 🔍 |
| `django_celery_beat_intervalschedule` |  | 7 | 🔍 |
| `django_celery_beat_periodictask` |  | 17 | 🔍 |
| `django_celery_beat_periodictasks` |  | 0 | 🔍 |
| `django_celery_beat_solarschedule` |  | 0 | 🔍 |
| `django_celery_results_chordcounter` |  | 0 | 🔍 |
| `django_celery_results_groupresult` |  | 0 | 🔍 |
| `django_celery_results_taskresult` |  | 267232 | 🔍 |
| `django_content_type` |  | 33 | 🔍 |
| `django_migrations` |  | 240 | 🔍 |
| `django_session` |  | 0 | 🔍 |

---

### auth_group
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `name` | varchar(150) | N | UNI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:原辅料名称） | 📦🖥️ |  |

### auth_group_permissions
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `group_id` | int | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →system_users_groups(推断) |
| `permission_id` | int | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →system_role_permission(推断) |

### auth_permission
**定义**：（待补充） ｜ **行数(估)**：132

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `name` | varchar(255) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:原辅料名称） | 📦🖥️ |  |
| `content_type_id` | int | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →django_content_type(推断) |
| `codename` | varchar(100) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_admin_log
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `action_time` | datetime(6) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `object_id` | longtext | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `object_repr` | varchar(200) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `action_flag` | smallint unsigned | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `change_message` | longtext | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `content_type_id` | int | Y | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →django_content_type(推断) |
| `user_id` | bigint | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →system_users(推断) |

### django_celery_beat_clockedschedule
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `clocked_time` | datetime(6) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_celery_beat_crontabschedule
**定义**：（待补充） ｜ **行数(估)**：13

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `minute` | varchar(240) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `hour` | varchar(96) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `day_of_week` | varchar(64) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `day_of_month` | varchar(124) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `month_of_year` | varchar(64) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `timezone` | varchar(63) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_celery_beat_intervalschedule
**定义**：（待补充） ｜ **行数(估)**：7

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `every` | int | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `period` | varchar(24) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_celery_beat_periodictask
**定义**：（待补充） ｜ **行数(估)**：17

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `name` | varchar(200) | N | UNI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:原辅料名称） | 📦🖥️ |  |
| `task` | varchar(200) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `args` | longtext | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `kwargs` | longtext | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `queue` | varchar(200) | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `exchange` | varchar(200) | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `routing_key` | varchar(200) | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `expires` | datetime(6) | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `enabled` | tinyint(1) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `last_run_at` | datetime(6) | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `total_run_count` | int unsigned | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `date_changed` | datetime(6) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `description` | longtext | N | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:描述） | 📦🖥️ |  |
| `crontab_id` | int | Y | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →django_celery_beat_crontabschedule |
| `interval_id` | int | Y | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →django_celery_beat_intervalschedule |
| `solar_id` | int | Y | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →django_celery_beat_solarschedule |
| `one_off` | tinyint(1) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `start_time` | datetime(6) | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:生效时间） | 📦🖥️ |  |
| `priority` | int unsigned | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:优先级） | 📦🖥️ |  |
| `headers` | longtext | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `clocked_id` | int | Y | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →django_celery_beat_clockedschedule |
| `expire_seconds` | int unsigned | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_celery_beat_periodictasks
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `ident` | smallint | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `last_update` | datetime(6) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_celery_beat_solarschedule
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `event` | varchar(24) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `latitude` | decimal(9,6) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `longitude` | decimal(9,6) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_celery_results_chordcounter
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `group_id` | varchar(255) | N | UNI | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →system_users_groups(推断) |
| `sub_tasks` | longtext | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `count` | int unsigned | N | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:单数） | 📦🖥️ |  |

### django_celery_results_groupresult
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `group_id` | varchar(255) | N | UNI | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 | →system_users_groups(推断) |
| `date_created` | datetime(6) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `date_done` | datetime(6) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `content_type` | varchar(128) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `content_encoding` | varchar(64) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `result` | longtext | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:检定结果） | 📦🖥️ |  |

### django_celery_results_taskresult
**定义**：（待补充） ｜ **行数(估)**：267232

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `task_id` | varchar(255) | N | UNI | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `status` | varchar(50) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:完成状态） | 📦🖥️ |  |
| `content_type` | varchar(128) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `content_encoding` | varchar(64) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `result` | longtext | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:检定结果） | 📦🖥️ |  |
| `date_done` | datetime(6) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `traceback` | longtext | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `meta` | longtext | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `task_args` | longtext | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `task_kwargs` | longtext | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `task_name` | varchar(255) | Y | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `worker` | varchar(100) | Y | MUL | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:作业员） | 📦🖥️ |  |
| `date_created` | datetime(6) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `periodic_task_name` | varchar(255) | Y | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_content_type
**定义**：（待补充） ｜ **行数(估)**：33

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | int | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `app_label` | varchar(100) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `model` | varchar(100) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:型号） | 📦🖥️ |  |

### django_migrations
**定义**：（待补充） ｜ **行数(估)**：240

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:列表权限） | 📦🖥️ |  |
| `app` | varchar(255) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `name` | varchar(255) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档）（界面:原辅料名称） | 📦🖥️ |  |
| `applied` | datetime(6) | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |

### django_session
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `session_key` | varchar(40) | N | PRI | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `session_data` | longtext | N | - | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
| `expire_date` | datetime(6) | N | MUL | Django/Celery 框架表（结构由框架定义，见官方文档） | 📦 |  |
