---
title: 考勤打卡模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 05-人事系统域
tags: [工程, 数据字典2, 代码实证, 考勤打卡]
---

# 考勤打卡模块 · fuadmin 数据字典2（代码实证版）
> 域: 05-人事系统域 | 表数: 1 | 字段: 18 | 代码锚定: 0(0%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/05-人事系统域/考勤打卡模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `att_transaction` |  | 189974 | 🔍 |

---

### att_transaction
**定义**：打卡记录表 ｜ **行数(估)**：189974

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `verify_type` | tinyint | Y | - | 🔍待补充 | 🔍 |  |
| `source` | tinyint | Y | - | （界面:来源） | 🔍🖥️ |  |
| `punch_time` | datetime | Y | MUL | 🔍待补充 | 🔍 |  |
| `temperature` | varchar(20) | Y | - | （界面:测量温度） | 🔍🖥️ |  |
| `terminal_sn` | varchar(50) | Y | - | 🔍待补充 | 🔍 |  |
| `terminal_alias` | varchar(100) | Y | - | 🔍待补充 | 🔍 |  |
| `att_photo_url` | varchar(500) | Y | - | 🔍待补充 | 🔍 |  |
| `mask_flag` | varchar(20) | Y | - | 🔍待补充 | 🔍 |  |
| `upload_time` | datetime | Y | - | 🔍待补充 | 🔍 |  |
| `timezone` | varchar(10) | Y | - | 🔍待补充 | 🔍 |  |
| `gps_location` | varchar(200) | Y | - | 🔍待补充 | 🔍 |  |
| `device_verify_type` | varchar(10) | Y | - | 🔍待补充 | 🔍 |  |
| `employee_code` | varchar(20) | Y | MUL | 🔍待补充 | 🔍 | →system_users(推断) |
| `first_name` | varchar(50) | Y | - | 🔍待补充 | 🔍 |  |
| `dept_name` | varchar(100) | Y | MUL | （界面:部门） | 🔍🖥️ | →system_dept(推断) |
| `status` | varchar(20) | Y | - | （界面:完成状态） | 🔍🖥️ |  |
| `created_at` | datetime | Y | - | 🔍待补充 | 🔍 |  |
