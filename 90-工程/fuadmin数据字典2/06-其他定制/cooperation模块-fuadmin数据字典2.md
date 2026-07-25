---
title: cooperation模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, cooperation]
---

# cooperation模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 23 | 代码锚定: 22(96%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/cooperation模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_cooperation` | 合作管理 | 256 | 💻 |

---

### generator_cooperation
**定义**：合作管理 ｜ **代码**：`generator/cooperation/model.py` ｜ **行数(估)**：256

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `support_staff` | json | Y | - | 配合人员 | ✅ |  |
| `end_datetime` | datetime(6) | Y | - | 截止时间 | ✅ |  |
| `cc_send` | json | Y | - | 抄送人 | ✅ |  |
| `remark` | longtext | Y | - | 问题描述 | ✅ |  |
| `priority` | varchar(20) | Y | - | 优先级 | ✅ |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `job_code_name` | varchar(80) | Y | - | 工作代号 | ✅ |  |
| `date_time` | datetime(6) | Y | - | 发起时间 | ✅ |  |
| `type` | varchar(20) | Y | - | 分类（界面:问题分类） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `devices` | varchar(80) | Y | - | 设备 | ✅ |  |
| `purchase` | json | Y | - | 采购清单 | ✅ |  |
| `target` | varchar(40) | Y | - | 备选信息 | ✅ |  |
| `picture` | json | Y | - | 相关照片 | ✅ |  |
| `message` | json | Y | - | 留言 | ✅ |  |
| `tangential_process` | json | Y | - | 切线流程 | ✅ |  |
| `state` | int | Y | - | 本单状态；0已取消 1处理中 2已完成 | ✅💬 |  |
