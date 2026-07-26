---
title: 二维码追溯模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 02-生产铸造域
tags: [工程, 数据字典2, 代码实证, 二维码追溯]
---

# 二维码追溯模块 · fuadmin 数据字典2（代码实证版）
> 域: 02-生产铸造域 | 表数: 13 | 字段: 215 | 代码锚定: 213(99%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/02-生产铸造域/二维码追溯模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `extraneous_product_qrcode` | 产品二维码 | 35082 | 💻 |
| `generator_box_code_verify` | 箱码验证 | 9071 | 💻 |
| `generator_exception_qrcode` | 异常二维码 | 15 | 💻 |
| `generator_qrcode_in` | 扫码入库（0行） | 0 | 💻 |
| `generator_qrcode_out` | 扫码出库（0行） | 0 | 💻 |
| `generator_qrcode_sendout` | 扫码发货 | 39588 | 💻 |
| `generator_registration_qrcode` | 登记二维码 | 7 | 💻 |
| `generator_tracking_transfer` | 跟踪单流转记录（0行） | 0 | 💻 |
| `generator_tracking_waste_record` | 不良品记录（0行） | 0 | 💻 |
| `track_route` | 工艺路线（0行） | 0 | 💻 |
| `track_route_step` | 工艺路线步骤（0行） | 0 | 💻 |
| `track_station` | 跟踪站点（0行） | 0 | 💻 |
| `track_station_job_code_map` | 站点-计价代码映射（0行） | 0 | 💻 |

---

### extraneous_product_qrcode
**定义**：产品二维码 ｜ **代码**：`extraneous/models.py` ｜ **行数(估)**：35082

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅ |  |
| `state` | int | Y | - | 状态：0不合格 1合格 2隔离 3报废 | 💬⚖️ |  |
| `unqualified_content` | varchar(255) | Y | - | 不合格内容，如[孔径大,形位公差] | ✅⚖️ |  |
| `processed_content` | varchar(255) | Y | - | 已处理内容，如[孔径大] | ✅⚖️ |  |
| `remark` | varchar(255) | Y | - | 备注 | ✅ |  |
| `new_product_code` | varchar(255) | Y | - | 产品二维码：返修换码后的新码存储 | ✅⚖️ |  |
| `old_product_code` | varchar(255) | Y | - | 旧产品二维码：返修前原有二维码存储 | ✅⚖️ |  |
| `product_name` | varchar(50) | Y | - | 产品名称 | ✅ |  |
| `userinfo` | varchar(50) | Y | - | 用户信息 | ✅ |  |
| `is_active` | tinyint(1) | Y | - | 是否激活 | ✅ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅ |  |
| `system_user` | tinyint(1) | Y | - | 是否系统用户：True内部用户 False外部用户 | 💬⚖️ |  |
| `box_code` | varchar(100) | Y | - | 箱体二维码（该字段未启用） | ✅⚖️ |  |
| `img` | json | Y | - | [推断]现场图片（异常/换码佐证图） | 🔍 |  |
| `operate_state` | varchar(50) | Y | - | 操作名称：人工确认/隔离/退箱/人工修复/物流发货 | 💬⚖️ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users | ✅🔗 | →system_users |
| `line_name` | varchar(40) | Y | - | 产线/工序 | ✅ |  |
| `phase` | int | Y | - | 阶段：0创建 1待处理 2已处理 3已核验 | 💬⚖️ |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅ |  |
| `picture` | json | Y | - | 图片 | ✅ |  |
| `exception_record_datetime` | datetime | Y | - | 异常记录时间：发现问题或检测时的时间 | ✅⚖️ |  |
| `cc_user` | json | Y | - | 抄送人 | ✅ |  |
| `production_manager` | varchar(30) | Y | - | 生产部负责人，格式'工号 姓名' | ✅⚖️ |  |
| `quality_directer` | varchar(30) | Y | - | 质量部负责人，格式'工号 姓名' | ✅⚖️ |  |
| `rework_record_header_id` | bigint | Y | MUL | 异常产品处理；→generator_rework_record_header | ✅🔗 | →generator_rework_record_header |
| `temporary_state` | int | Y | - | 临时状态：0不合格 1合格 2隔离 3报废 | 💬⚖️ |  |
| `rework_defects` | json | Y | - | 返修记录；[[{"id": "1", "result": "", "worker": "", "content": "漏加工", "process_time": ""}, {"id": "2", "result": "", "worker": "", "content": "断刀", "process_time": ""}]] | ✅💬 |  |
| `rework_datetime` | datetime | Y | - | 返修时间：二维码返修有值，关联返工单时为空 | ✅⚖️ |  |
| `worker` | varchar(20) | Y | - | 作业员：二维码返修有值，关联返工单时为空 | ✅⚖️ |  |
| `_MASK_FROM_V2` | timestamp | N | MUL | [推断]掩码同步标记列(V2来源侧)，无代码锚点，非业务字段 | 🔍 |  |
| `belong` | int | Y | - | 归属工作站点：0治通 1智机 2广汇 3泰峰 4娄塘 | 💬⚖️ |  |

### generator_box_code_verify
**定义**：箱码验证 ｜ **代码**：`generator/box_code_verify/model.py` ｜ **行数(估)**：9071

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `image` | json | Y | - | 图片：现场图片（JSON列表） | ✅⚖️ |  |
| `cc` | json | Y | - | 抄送 | ✅ |  |
| `product_qr` | varchar(50) | Y | - | 产品二维码：单件码，需flag=True才验证 | ✅⚖️ |  |
| `product_qr_verified` | int | Y | - | 验证状态：综合结果 0未通过/1通过 | 💬⚖️ |  |
| `p_state` | int | Y | - | 人工审核：0未通过/1通过/3隐藏 | 💬⚖️ |  |
| `ai_state` | int | Y | - | AI审核：0待验证/1通过/2验证不一致/3未识别出 | 💬⚖️ |  |
| `number` | int | Y | - | 装箱量 | ✅ |  |
| `product_name` | varchar(20) | Y | - | 产品名称 | ✅ |  |
| `box_code` | varchar(50) | Y | - | 箱码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `flag` | tinyint(1) | Y | - | 是否验证：是否需要验证产品二维码 | ✅⚖️ |  |
| `image_md5` | json | Y | - | MD5：图片md5（JSON列表） | ✅⚖️ |  |
| `customer_box_code` | varchar(500) | Y | - | 客户箱码；客户箱码原始内容 | ✅ |  |
| `customer_box_code_bind_time` | datetime(6) | Y | - | 客户箱码绑定时间 | ✅ |  |
| `customer_box_code_binder` | varchar(100) | Y | - | 客户箱码绑定人 | ✅ |  |

### generator_exception_qrcode
**定义**：异常二维码 ｜ **代码**：`generator/exception_qrcode/model.py` ｜ **行数(估)**：15

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `type` | varchar(20) | Y | - | 类型 | ✅ |  |
| `qrcode` | varchar(255) | Y | - | 二维码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_qrcode_in
**定义**：扫码入库（0行） ｜ **代码**：`generator/qrcode_in/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `Inspection_data` | json | Y | - | 检测数据 | ✅ |  |
| `certigier` | varchar(100) | Y | - | 质量授权人 | ✅ |  |
| `state` | int | Y | - | 检测状态：0未检测 1已检测 2授权 | 💬⚖️ |  |
| `boxstate` | varchar(10) | Y | - | 箱码状态：合格/警告/不合格 | 💬⚖️ |  |
| `number` | int | Y | - | 整箱数量 | ✅ |  |
| `box_code` | varchar(255) | Y | - | 箱码 | ✅ |  |
| `user` | varchar(20) | Y | - | 入库人 | ✅ |  |
| `entry_time` | datetime(6) | Y | - | 入库时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_qrcode_out
**定义**：扫码出库（0行） ｜ **代码**：`generator/qrcode_out/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `certigier` | varchar(100) | Y | - | 物流授权人 | ✅ |  |
| `consignor` | varchar(100) | Y | - | 送货方 | ✅ |  |
| `consignee` | varchar(100) | Y | - | 收货方 | ✅ |  |
| `car_number` | varchar(20) | Y | - | 车号 | ✅ |  |
| `number` | int | Y | - | 整箱数量 | ✅ |  |
| `box_code` | varchar(255) | Y | - | 箱码 | ✅ |  |
| `user` | varchar(20) | Y | - | 出库人 | ✅ |  |
| `out_time` | datetime(6) | Y | - | 出库时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_qrcode_sendout
**定义**：扫码发货 ｜ **代码**：`generator/customer_order/model.py` ｜ **行数(估)**：39588

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `user` | varchar(20) | N | - | 扫码人；执行出库操作的人员 | ✅ |  |
| `box_code` | varchar(255) | N | - | 箱码；产品箱码 | ✅ |  |
| `product_name` | varchar(20) | N | - | 产品名称 | ✅ |  |
| `bar_code` | varchar(30) | N | - | 物料条形码：产品物料编码（非件码） | ✅⚖️ |  |
| `number` | int | N | - | 实发数量：每箱实发数，交付件数=SUM(number) | ✅⚖️ |  |
| `type` | int | N | - | 扫码状态：0错误 1正常 2退货 3隐藏；默认查0/1/2 | 💬⚖️ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `customer_order_id` | bigint | Y | MUL | 客户订单；关联的客户订单；→generator_customer_order | ✅🔗 | →generator_customer_order |
| `error_message` | longtext | Y | - | 错误信息；记录操作中的错误信息 | ✅ |  |
| `check_number` | int | Y | - | 整箱数量：每箱的外检合格数量 | ✅⚖️ |  |
| `part_qr_codes` | json | Y | - | 零件二维码列表；该箱内包含的零件二维码 | ✅ |  |
| `part_qr_verified` | tinyint(1) | Y | - | 零件二维码验证状态；True表示所有零件二维码均通过验证，False表示存在未通过验证的零件,或者没有数据 | ✅ |  |

### generator_registration_qrcode
**定义**：登记二维码 ｜ **代码**：`generator/registration_qrcode/model.py` ｜ **行数(估)**：7

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `state` | tinyint(1) | Y | - | 状态：True正常 False异常 | 💬⚖️ |  |
| `type` | varchar(20) | Y | - | 类型 | ✅ |  |
| `qrcode` | varchar(255) | Y | - | 二维码 | ✅ |  |
| `box_code` | varchar(255) | Y | - | 箱码 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### generator_tracking_transfer
**定义**：跟踪单流转记录（0行） ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | longtext | Y | - | 备注 | ✅ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `from_sequence` | int | Y | - | 来源工序顺序 | ✅ |  |
| `to_sequence` | int | Y | - | 目标工序顺序 | ✅ |  |
| `input_quantity` | int | N | - | 投入数量 | ✅ |  |
| `output_quantity` | int | N | - | 产出数量 | ✅ |  |
| `industrial_waste` | int | N | - | 工废 | ✅ |  |
| `scrap_waste` | int | N | - | 料废 | ✅ |  |
| `debug_waste` | int | N | - | 调试废 | ✅ |  |
| `operator` | varchar(50) | Y | - | 操作人 | ✅ |  |
| `operator_id` | int | Y | - | 操作人ID | ✅ |  |
| `transfer_time` | datetime(6) | N | - | 交接时间 | ✅ |  |
| `shift` | varchar(10) | Y | - | 班次 | ✅ |  |
| `site` | varchar(20) | Y | - | 工作地点 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `device_id` | bigint | Y | MUL | 设备；→generator_devices | ✅🔗 | →generator_devices |
| `tracking_id` | bigint | N | MUL | 跟踪单；→generator_production_tracking | ✅🔗 | →generator_production_tracking |
| `from_station_id` | bigint | Y | MUL | 来源站点；→track_station | ✅🔗 | →track_station |
| `to_station_id` | bigint | Y | MUL | 目标站点；→track_station | ✅🔗 | →track_station |

### generator_tracking_waste_record
**定义**：不良品记录（0行） ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `waste_type` | varchar(20) | N | - | 不良类型；工废/料废/调试废 | ✅ |  |
| `quantity` | int | N | - | 数量 | ✅ |  |
| `handle_status` | varchar(20) | N | - | 处理状态；pending/handled | ✅ |  |
| `handle_time` | datetime(6) | Y | - | 处理时间 | ✅ |  |
| `handler` | varchar(50) | Y | - | 处理人 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `tracking_id` | bigint | N | MUL | 跟踪单；→generator_production_tracking | ✅🔗 | →generator_production_tracking |
| `transfer_id` | bigint | N | MUL | 流转记录；→generator_tracking_transfer | ✅🔗 | →generator_tracking_transfer |

### track_route
**定义**：工艺路线（0行） ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `route_name` | varchar(100) | N | - | 路线名称 | ✅ |  |
| `product_category` | varchar(30) | Y | - | 产品类别；缸体/缸盖/差壳/结构件/转向节 | ✅ |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### track_route_step
**定义**：工艺路线步骤（0行） ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `step_no` | int | N | - | 步骤序号；1, 2, 3... | ✅ |  |
| `is_first` | tinyint(1) | N | - | 是否首工序 | ✅ |  |
| `is_last` | tinyint(1) | N | - | 是否末工序 | ✅ |  |
| `plan_hours` | decimal(6,2) | Y | - | 计划工时；小时 | ✅ |  |
| `site` | varchar(20) | Y | - | 工作地点；治通/广汇/泰峰 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `route_id` | bigint | N | MUL | 工艺路线；→track_route | ✅🔗 | →track_route |
| `station_id` | bigint | N | MUL | 跟踪站点；→track_station | ✅🔗 | →track_station |

### track_station
**定义**：跟踪站点（0行） ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `station_name` | varchar(100) | N | - | 站点名称 | ✅ |  |
| `product_category` | varchar(30) | Y | - | 产品类别；缸体/缸盖/差壳/结构件/转向节 | ✅ |  |
| `station_type` | varchar(30) | Y | - | 站点类型；机加/去毛刺/清洗/密封/断芯/穿扎带/GP12 | ✅ |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |

### track_station_job_code_map
**定义**：站点-计价代码映射（0行） ｜ **代码**：`generator/production_tracking/model.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `job_code_id` | bigint | N | MUL | 计价代码；→generator_job_code | ✅🔗 | →generator_job_code |
| `station_id` | bigint | N | MUL | 跟踪站点；→track_station | ✅🔗 | →track_station |

---

## 同域兄弟模块
- [[02-生产铸造域/不良品模块-fuadmin数据字典2|不良品模块]]
- [[02-生产铸造域/新排程模块-fuadmin数据字典2|新排程模块]]
- [[02-生产铸造域/生产计划模块-fuadmin数据字典2|生产计划模块]]
- [[02-生产铸造域/生产模块-fuadmin数据字典2|生产模块]]
- [[02-生产铸造域/班次模块-fuadmin数据字典2|班次模块]]
- [[02-生产铸造域/TF铸造模块-fuadmin数据字典2|TF铸造模块]]
- [[02-生产铸造域/02-生产铸造域-业务流|02-生产铸造域业务流(代码验证版)]]
