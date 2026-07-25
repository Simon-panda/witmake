---
title: 退货模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 01-供应链域
tags: [工程, 数据字典2, 代码实证, 退货]
---

# 退货模块 · fuadmin 数据字典2（代码实证版）
> 域: 01-供应链域 | 表数: 2 | 字段: 33 | 代码锚定: 31(94%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/01-供应链域/退货模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_return_order` | 退货单：外检创建的不合格品退货主单（编号TH开头、退货理由/数量、物流单号、阶段）， | 23 | 💻 |
| `generator_return_order_detail` | 退货单明细：按二维码逐件记录退货品的检查记录与处置状态（合格/隔离/报废/返厂），可 | 1087 | 💻 |

---

### generator_return_order
**定义**：退货单：外检创建的不合格品退货主单（编号TH开头、退货理由/数量、物流单号、阶段），驱动物流退货流程 ｜ **流角色**：退货主单 ｜ **代码**：`generator/return_order/model.py` ｜ **行数(估)**：23

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:退货单编号） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `return_process` | json | Y | - | 退货单流程 | ✅ |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `phase` | int | Y | - | 阶段：0外检已创建 1物流已收 2物流已退货 | ✅⚖️ |  |
| `return_quantity` | int | Y | - | 退货总数 | ✅ |  |
| `return_reason` | varchar(50) | Y | - | 退货理由 | ✅ |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `belong` | int | Y | - | 归属工作站点：0治通 1智机 2广汇 3泰峰 4娄塘 | ✅⚖️ |  |
| `tracking_number` | varchar(100) | Y | - | 物流单号 | ✅ |  |
| `return_number` | varchar(20) | Y | - | 退货单编号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |

### generator_return_order_detail
**定义**：退货单明细：按二维码逐件记录退货品的检查记录与处置状态（合格/隔离/报废/返厂），可触发黄单（返工记录） ｜ **流角色**：退货逐件处置 ｜ **代码**：`generator/return_order_detail/model.py` ｜ **行数(估)**：1087

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:二维码） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `inspection_record` | json | Y | - | 检查记录 | ✅ |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `state` | int | Y | - | 状态；0不合格 1合格 2隔离 3报废 4未检查（返厂后默认） | ✅💬 |  |
| `is_returned_to_factory` | tinyint(1) | Y | - | 是否返厂 | ✅ |  |
| `quantity` | int | Y | - | 数量 | ✅ |  |
| `qrcode` | varchar(255) | Y | - | 二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人ID，关联系统用户表（与modifier修改人对应） | 🔍 |  |
| `return_order_header_id` | bigint | Y | MUL | 退货单；→generator_return_order | ✅🔗 | →generator_return_order |
| `is_rework_record_generated` | tinyint(1) | Y | - | 是否生成黄单 | ✅ |  |
