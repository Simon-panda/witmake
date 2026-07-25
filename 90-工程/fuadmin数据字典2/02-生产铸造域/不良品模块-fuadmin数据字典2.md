---
title: 不良品模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 02-生产铸造域
tags: [工程, 数据字典2, 代码实证, 不良品]
---

# 不良品模块 · fuadmin 数据字典2（代码实证版）
> 域: 02-生产铸造域 | 表数: 4 | 字段: 86 | 代码锚定: 80(93%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/02-生产铸造域/不良品模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_bad_product` | 不良产品单 | 16317 | 💻 |
| `generator_bad_product_record` | 不良产品登记 | 10010 | 💻 |
| `generator_defective_product` | 不良品登记 | 2069 | 💻 |
| `generator_rework_record_header` | 异常产品处理 | 1641 | 💻 |

---

### generator_bad_product
**定义**：不良产品单 ｜ **代码**：`generator/bad_product/model.py` ｜ **行数(估)**：16317

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `method` | longtext | Y | - | 处理措施 | ✅ |  |
| `reason` | longtext | Y | - | 原因分析 | ✅ |  |
| `responser` | varchar(255) | Y | - | 责任人列表；工废>4时取奖罚单Users_Ticket人员 | ✅⚖️ |  |
| `find_method` | varchar(20) | Y | - | 发现方式：操作工/巡检员/外检员/三坐标发现 | 💬⚖️ |  |
| `finder` | varchar(20) | Y | - | 发现人（界面:确认人） | ✅🖥️ |  |
| `debug_work` | int | Y | - | 工废数量；>4时自动创建奖罚单号 | ✅⚖️ |  |
| `debug_data` | int | Y | - | 调试废 | ✅ |  |
| `details` | longtext | Y | - | 问题描述 | ✅ |  |
| `picture` | json | Y | - | 不良图片 | ✅ |  |
| `type` | varchar(20) | Y | - | 问题分类：孔大/孔小/形位公差/位置公差/表面粗糙度/外观缺陷/其他 | 💬⚖️ |  |
| `code` | varchar(255) | Y | - | 机加二维码（界面:产品二维码） | ✅🖥️ |  |
| `date` | datetime(6) | Y | - | 日期 | ✅ |  |
| `job_code` | varchar(255) | Y | - | 工作代号 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `scrap_waste` | int | Y | - | 料废 | ✅ |  |
| `ticket_id` | bigint | Y | UNI | 奖罚单号；→generator_ticket | ✅🔗 | →generator_ticket |
| `responsible_dept` | varchar(255) | Y | - | 归责方：供应商/生产部/工程部/质量部 | 💬⚖️ |  |

### generator_bad_product_record
**定义**：不良产品登记 ｜ **代码**：`generator/bad_product_record/model.py` ｜ **行数(估)**：10010

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:孔偏） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `box_code` | varchar(255) | Y | - | 箱码 | ✅ |  |
| `state` | int | Y | - | 系统状态：0隐藏 1使用 | 💬⚖️ |  |
| `type` | varchar(20) | Y | - | 问题分类，如密封不良 | ✅⚖️ |  |
| `job_code` | varchar(255) | Y | - | 工作代号 | ✅ |  |
| `product_name` | varchar(20) | Y | - | 产品名称 | ✅ |  |
| `product_qrcode` | varchar(50) | Y | - | 产品二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `scan_time` | datetime | Y | - | 扫码时间：操作人扫码录入时间 | ✅⚖️ |  |
| `p_state` | int | Y | - | 产品状态：0工废 1良品 2料废 3退货 4可返修 | 💬⚖️ |  |
| `bad_product_id` | bigint | Y | MUL | 不良产品单；关联的不良产品单；→generator_bad_product | ✅🔗 | →generator_bad_product |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断]掩码同步标记列(V2来源侧)，无代码锚点，非业务字段 | 🔍 |  |

### generator_defective_product
**定义**：不良品登记 ｜ **代码**：`generator/defective_product/model.py` ｜ **行数(估)**：2069

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:日期） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `quantity` | int | Y | - | 数量 | ✅ |  |
| `reason` | varchar(30) | Y | - | 原因：孔大/磕碰伤/夹具故障/机器故障/漏加工/倒角大等 | 💬⚖️ |  |
| `discoverer` | varchar(30) | Y | - | 发现人，格式'工号 姓名' | ✅⚖️ |  |
| `discovery_method` | varchar(30) | Y | - | 发现方式：操作工/巡检员/外检员/三坐标发现 | 💬⚖️ |  |
| `responsible_person` | varchar(30) | Y | - | 责任人，格式'工号 姓名' | ✅⚖️ |  |
| `type` | varchar(30) | Y | - | 类型：工废/料废 | 💬⚖️ |  |
| `product` | varchar(30) | Y | - | 产品 | ✅ |  |
| `date` | date | Y | - | 日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |

### generator_rework_record_header
**定义**：异常产品处理 ｜ **代码**：`generator/rework_record_header/model.py` ｜ **行数(估)**：1641

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:黄单类型） | ✅📦🖥️ | →extraneous_product_qrcode |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `approval_process` | json | Y | - | 审批流程 | ✅ |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `phase` | int | Y | - | 阶段：0不通过 1待处理 2已处理 3已核验 | 💬⚖️ |  |
| `exception_record_datetime` | datetime | Y | - | 异常发现时间 | ✅ |  |
| `line_name` | varchar(40) | Y | - | 产线/工序 | ✅ |  |
| `product_name` | varchar(50) | Y | - | 异常产品名称 | ✅ |  |
| `rework_number` | varchar(50) | Y | - | 异常产品处理编号（界面:黄单编号） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | [推断]创建人（CoreModel审计字段，存用户标识） | 🔍 |  |
| `responsible_worker` | varchar(20) | Y | - | 作业员（界面:责任人） | ✅🖥️ |  |
| `coordinator` | json | Y | - | 介入人员（界面:介入记录） | ✅🖥️ |  |
| `message` | json | Y | - | 留言 | ✅ |  |
| `finished_picture` | json | Y | - | 返修完成图片 | ✅ |  |
| `category` | int | Y | - | 黄单类别：0空白黄单(内容有值) 1普通黄单 2红单返修（界面:黄单类型） | 💬⚖️🖥️ |  |
| `unqualified_content` | varchar(255) | Y | - | 不合格内容（界面:不良内容） | ✅🖥️ |  |
| `repair_deadline` | datetime | Y | - | 返修截止时间；红单返修截止时间 | ✅ |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断]掩码同步标记列(V2来源侧)，无代码锚点，非业务字段 | 🔍 |  |
| `belong` | int | Y | - | 归属工作站点：0治通 1智机 2广汇 3泰峰 4娄塘 | 💬⚖️ |  |
| `quantity_limit` | int | Y | - | 数量限制 | ✅ |  |
| `finish_time` | datetime(6) | Y | - | 收尾时间 | ✅ |  |
| `finisher` | varchar(20) | Y | - | 收尾人员 | ✅ |  |
