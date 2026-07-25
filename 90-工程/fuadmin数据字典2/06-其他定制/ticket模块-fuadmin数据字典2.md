---
title: ticket模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, ticket]
---

# ticket模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 25 | 代码锚定: 24(96%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/ticket模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_ticket` | 奖罚单 | 1578 | 💻 |

---

### generator_ticket
**定义**：奖罚单 ｜ **代码**：`generator/ticket/model.py` ｜ **行数(估)**：1578

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `signature` | json | Y | - | 签字；[{"key": "1", "name": "14018 李雪峰(生产部-经理)", "remark": "", "i_agree": "待确认", "is_send": true, "disabled": {"name": false, "remark": false, "i_agree": false, "operation": true}, "send_time": "2025-06-24 08:47:27", "agree_user": "", "signature_time": ""}]（界面:审批人） | ✅💬🖥️ |  |
| `handle_feedback` | longtext | Y | - | 处理意见 | ✅ |  |
| `measure` | longtext | Y | - | 改善措施 | ✅ |  |
| `info` | longtext | Y | - | 零件信息 | ✅ |  |
| `describe` | longtext | Y | - | 异常描述 | ✅ |  |
| `date_time` | datetime | Y | - | 生效日期 | ✅ |  |
| `work_order` | varchar(100) | Y | - | 关联工单；暂未使用该字段 | ✅💬 |  |
| `tracking_card` | varchar(100) | Y | - | 跟踪卡号；暂未使用该字段 | ✅💬 |  |
| `job_code` | varchar(100) | Y | - | 工作代号 | ✅ |  |
| `name` | varchar(100) | Y | - | 罚单名称（界面:单号名称） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `ticket_type` | int | Y | - | 状态；该字段未启用 | ✅💬 |  |
| `related_photos` | json | Y | - | 相关照片（界面:相关图片） | ✅🖥️ |  |
| `is_end` | tinyint(1) | Y | - | 是否结单（界面:已结单） | ✅🖥️ |  |
| `code` | varchar(100) | Y | - | 奖罚单号 | ✅ |  |
| `cc_send` | json | Y | - | 抄送人；["15029 林帅", "10000 刘超"] | ✅💬 |  |
| `is_audit` | int | Y | - | 是否审查；0是自己创建的奖罚单 关联不良品产生的奖罚单(未审查1 已审查2 不通过3) | ✅💬 |  |
| `audit_name` | varchar(30) | Y | - | 审查人；22323 卞士超 | ✅💬 |  |
