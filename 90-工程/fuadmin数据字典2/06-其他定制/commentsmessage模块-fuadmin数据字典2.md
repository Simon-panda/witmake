---
title: commentsmessage模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, commentsmessage]
---

# commentsmessage模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 16 | 代码锚定: 15(94%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/commentsmessage模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_commentsmessage` | 留言 | 188 | 💻 |

---

### generator_commentsmessage
**定义**：留言 ｜ **代码**：`generator/commentsmessage/model.py` ｜ **行数(估)**：188

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `odd_numbers` | varchar(255) | Y | - | 单号 | ✅ |  |
| `parentId` | int | Y | - | 父评论ID | ✅ |  |
| `postDate` | varchar(255) | Y | - | 发送时间 | ✅ |  |
| `receiverId` | int | Y | - | 接收者id | ✅ |  |
| `senderId` | int | Y | - | 发送者id | ✅ |  |
| `senderName` | varchar(255) | Y | - | 发送者姓名 | ✅ |  |
| `text` | varchar(255) | Y | - | 评论内容 | ✅ |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `receiverName` | varchar(255) | Y | - | 回复人姓名 | ✅ |  |
| `creator_id` | bigint | Y | - | 🔍待补充 | 🔍 |  |
