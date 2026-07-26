---
title: misc-ticket模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, misc-ticket]
---

# misc-ticket模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 25 | 代码锚定: 25(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/misc-ticket模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_ticket` | 奖罚单（质量/行为奖惩与审查） | 1578 | 💻 |

---

### generator_ticket
**定义**：奖罚单（质量/行为奖惩与审查） ｜ **流角色**：奖惩管理 ｜ **代码**：`generator/ticket/model.py` ｜ **行数(估)**：1578

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `signature` | json | Y | - | 签字；[{"key": "1", "name": "14018 李雪峰(生产部-经理)", "remark": "", "i_agree": "待确认", "is_send": true, "disabled": {"name": false, "remark": false, "i_agree": false, "operation": true}, "send_time": "2025-06-24 08:47:27", "agree_user": "", "signature_time": ""}] | ✅💬 |  |
| `handle_feedback` | longtext | Y | - | 处理意见 | ✅ |  |
| `measure` | longtext | Y | - | 改善措施 | ✅ |  |
| `info` | longtext | Y | - | 零件信息 | ✅ |  |
| `describe` | longtext | Y | - | 异常描述 | ✅ |  |
| `date_time` | datetime | Y | - | 生效日期 | ✅ |  |
| `work_order` | varchar(100) | Y | - | 关联工单（暂未启用） | ✅⚖️ |  |
| `tracking_card` | varchar(100) | Y | - | 跟踪卡号（暂未启用） | ✅⚖️ |  |
| `job_code` | varchar(100) | Y | - | 工作代号 | ✅ |  |
| `name` | varchar(100) | Y | - | 罚单名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `ticket_type` | int | Y | - | 奖罚单类型（Ticket_TYPE枚举，未启用） | 💬⚖️ |  |
| `related_photos` | json | Y | - | 相关照片 | ✅ |  |
| `is_end` | tinyint(1) | Y | - | 是否结单 | ✅ |  |
| `code` | varchar(100) | Y | - | 奖罚单号 | ✅ |  |
| `cc_send` | json | Y | - | 抄送人JSON列表（工号+姓名） | ✅⚖️ |  |
| `is_audit` | int | Y | - | 是否审查：0自建奖罚单；不良品关联单1未审/2已审/3不通过 | 💬⚖️ |  |
| `audit_name` | varchar(30) | Y | - | 审查人（工号+姓名，如 工号 某某） | ✅⚖️ |  |

---

## 同域兄弟模块
- [[06-其他定制/answer定制模块模块-fuadmin数据字典2|answer定制模块模块]]
- [[06-其他定制/liqiang定制模块模块-fuadmin数据字典2|liqiang定制模块模块]]
- [[06-其他定制/lizhu定制模块模块-fuadmin数据字典2|lizhu定制模块模块]]
- [[06-其他定制/misc-alarm模块-fuadmin数据字典2|misc-alarm模块]]
- [[06-其他定制/misc-commentsmessage模块-fuadmin数据字典2|misc-commentsmessage模块]]
- [[06-其他定制/misc-cooperation模块-fuadmin数据字典2|misc-cooperation模块]]
- [[06-其他定制/misc-definition模块-fuadmin数据字典2|misc-definition模块]]
- [[06-其他定制/misc-demo模块-fuadmin数据字典2|misc-demo模块]]
- [[06-其他定制/misc-external模块-fuadmin数据字典2|misc-external模块]]
- [[06-其他定制/misc-go模块-fuadmin数据字典2|misc-go模块]]
- [[06-其他定制/misc-management模块-fuadmin数据字典2|misc-management模块]]
- [[06-其他定制/misc-objective模块-fuadmin数据字典2|misc-objective模块]]
- [[06-其他定制/misc-public模块-fuadmin数据字典2|misc-public模块]]
- [[06-其他定制/misc-safety模块-fuadmin数据字典2|misc-safety模块]]
- [[06-其他定制/misc-site模块-fuadmin数据字典2|misc-site模块]]
- [[06-其他定制/misc-total模块-fuadmin数据字典2|misc-total模块]]
- [[06-其他定制/misc-triangle模块-fuadmin数据字典2|misc-triangle模块]]
- [[06-其他定制/misc-zj2315模块-fuadmin数据字典2|misc-zj2315模块]]
- [[06-其他定制/test定制模块模块-fuadmin数据字典2|test定制模块模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
