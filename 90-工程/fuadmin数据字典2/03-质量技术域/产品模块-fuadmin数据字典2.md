---
title: 产品模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 产品]
---

# 产品模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 6 | 字段: 81 | 代码锚定: 72(89%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/产品模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_product` | 产品表 | 69 | 💻 |
| `generator_product_plm_rufa` | 产品(入库-发货) | 0 | 💻 |
| `generator_product_ready` | 产品待发仓 | 0 | 💻 |
| `generator_product_szb` | 产品三坐标报告 | 151966 | 💻 |
| `generator_product_urgent_mark` | 产品赋红 | 3886 | 💻 |
| `generator_product_urgent_record` | 产品赋红记录 | 2055 | 💻 |

---

### generator_product
**定义**：产品表 ｜ **代码**：`generator/product/model.py` ｜ **行数(估)**：69

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:上级产品） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `product_name` | varchar(255) | Y | - | 产品名 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 上级产品；→generator_product | ✅🔗 | →generator_product |
| `code` | varchar(60) | Y | - | 产品编号 | ✅ |  |
| `is_active` | varchar(20) | Y | - | 状态；启用 / 停用 | ✅💬 |  |
| `material_number` | varchar(80) | Y | - | 物料号 | ✅ |  |
| `production_value` | double | Y | - | 产值 | ✅ |  |
| `name` | varchar(255) | Y | - | 简称 | ✅ |  |
| `history` | longtext | Y | - | 操作记录（界面:操作历史） | ✅🖥️ |  |
| `weight` | double | Y | - | 重量（界面:成品重量） | ✅🖥️ |  |
| `is_delete` | tinyint(1) | Y | - | 是否删除；是否删除(软删除标记)（界面:封存） | ✅📦🖥️ |  |

### generator_product_plm_rufa
**定义**：产品(入库-发货) ｜ **代码**：`generator/product_plm_rufa/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:入库） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `qrcode` | varchar(255) | Y | - | 二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `product_ready_id` | bigint | Y | MUL | 产品名称；→generator_product_ready | ✅🔗 | →generator_product_ready |
| `qrcode_in_id` | bigint | Y | MUL | 入库；→generator_qrcode_in | ✅🔗 | →generator_qrcode_in |
| `qrcode_out_id` | bigint | Y | MUL | 发货；→generator_qrcode_out | ✅🔗 | →generator_qrcode_out |

### generator_product_ready
**定义**：产品待发仓 ｜ **代码**：`generator/product_ready/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:公司） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `number` | int | Y | - | 库存数量 | ✅ |  |
| `name` | varchar(30) | Y | - | 零部件名称 | ✅ |  |
| `product` | varchar(30) | Y | - | 产品名称 | ✅ |  |
| `company` | varchar(20) | Y | - | 公司 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_product_szb
**定义**：产品三坐标报告 ｜ **代码**：`generator/szb/model.py` ｜ **行数(估)**：151966

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:上级产品） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `report_time` | datetime(6) | Y | - | 报告时间 | ✅ |  |
| `workpiece_number` | varchar(255) | Y | - | 工件号 | ✅ |  |
| `product_name` | varchar(255) | Y | - | 程序名（界面:产品名） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `product_id_id` | bigint | Y | MUL | 所属产品；关联产品；→generator_product | ✅🔗 | →generator_product |
| `report` | mediumblob | Y | - | 🔍待补充 |  |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 |  |  |
| `static_file_path` | varchar(50) | Y | - | 静态文件路径；存储相关静态文件的路径 | ✅ |  |

### generator_product_urgent_mark
**定义**：产品赋红 ｜ **代码**：`generator/product_urgent_mark/model.py` ｜ **行数(估)**：3886

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:不验证） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 赋红原因 | ✅ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `urgent_level` | int | Y | - | 等级；1~4，1最紧急 1红色(致命) 2橙色(严重) 3黄色(一般) 4蓝色(提示)（界面:赋红等级） | ✅💬🖥️ |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `product_qrcode` | varchar(255) | Y | - | 产品二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `active_state` | int | Y | - | 激活状态；1激活 0注销（界面:是否激活） | ✅💬🖥️ |  |
| `state` | int | Y | - | 验证规则状态；1已验证 0未验证 | ✅💬 |  |
| `_MASK_FROM_V2` | timestamp | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_product_urgent_record
**定义**：产品赋红记录 ｜ **代码**：`generator/product_urgent_mark/model.py` ｜ **行数(估)**：2055

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:上级产品） | ✅🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅🖥️ |  |
| `user_name` | varchar(55) | Y | - | 操作人（界面:姓名） | ✅🖥️ |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅🖥️ |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅ |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `product_qrcode` | varchar(255) | Y | - | 产品二维码 | ✅ |  |
| `message` | text | Y | - | 报警内容（界面:留言） | ✅🖥️ |  |
| `level` | tinyint | Y | - | 报警等级 | ✅ |  |
