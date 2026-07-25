---
title: 测量计量模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 03-质量技术域
tags: [工程, 数据字典2, 代码实证, 测量计量]
---

# 测量计量模块 · fuadmin 数据字典2（代码实证版）
> 域: 03-质量技术域 | 表数: 3 | 字段: 59 | 代码锚定: 54(92%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/03-质量技术域/测量计量模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_calibration_record` | 检定记录 | 138 | 💻 |
| `generator_cmm_inspection_log` | 三坐标送检记录 | 37743 | 💻 |
| `generator_measuring_instrument` | 计量器具档案 | 138 | 💻 |

---

### generator_calibration_record
**定义**：检定记录 ｜ **代码**：`generator/calibration_record/model.py` ｜ **行数(估)**：138

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:计量器具） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `images` | json | Y | - | 检定图片 | ✅ |  |
| `number` | varchar(100) | Y | - | 检定证书编号 | ✅ |  |
| `result` | varchar(10) | Y | MUL | 检定结果 | ✅ |  |
| `cycle_days` | int unsigned | Y | - | 本次检定数（界面:检定周期(天)） | ✅🖥️ |  |
| `next_date` | date | Y | MUL | 下次检定日期 | ✅ |  |
| `date` | date | Y | - | 检定日期 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `instrument_id` | bigint | Y | MUL | 计量器具；→generator_measuring_instrument | ✅🔗 | →generator_measuring_instrument |

### generator_cmm_inspection_log
**定义**：三坐标送检记录 ｜ **代码**：`generator/cmm_inspection_log/model.py` ｜ **行数(估)**：37743

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:送检时间） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remarks` | varchar(255) | Y | - | 备注 | ✅ |  |
| `person` | varchar(255) | Y | - | 测量人员 | ✅ |  |
| `status` | varchar(255) | Y | - | 测量状态 | ✅ |  |
| `result` | varchar(255) | Y | - | 测量结果 | ✅ |  |
| `temperature` | varchar(255) | Y | - | 测量温度 | ✅ |  |
| `time` | datetime(6) | Y | - | 测量时间 | ✅ |  |
| `inspection_person` | varchar(255) | Y | - | 送检人员 | ✅ |  |
| `first_article_reason` | varchar(255) | Y | - | 首件原因 | ✅ |  |
| `is_first_article` | varchar(255) | Y | - | 是否首件 | ✅ |  |
| `inspection_status` | varchar(255) | Y | - | 送检状态 | ✅ |  |
| `mold_no` | varchar(255) | Y | - | 模号 | ✅ |  |
| `production_line_no` | varchar(255) | Y | - | 线号 | ✅ |  |
| `qr_code` | varchar(255) | Y | - | 二维码 | ✅ |  |
| `product_name` | varchar(255) | Y | - | 产品名称 | ✅ |  |
| `inspection_time` | datetime(6) | Y | - | 送检时间 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MASK_TO_V2` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `_MUSID_SYNC_V2` | int unsigned | Y | MUL | 🔍待补充 | 🔍 |  |

### generator_measuring_instrument
**定义**：计量器具档案 ｜ **代码**：`generator/measuring_instrument/model.py` ｜ **行数(估)**：138

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:注销） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `is_active` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `images` | json | Y | - | 器具图片 | ✅ |  |
| `calibration_cycle_days` | int unsigned | N | - | 检定周期(天)；182 | ✅💬 |  |
| `specification` | varchar(160) | Y | - | 规格；"例：CHKΦ10.84±0.16" | ✅💬 |  |
| `storage_location` | varchar(50) | N | - | 存放地点 | ✅ |  |
| `products` | json | Y | - | 测量产品；例：["GS61", "GS61HEV", "GS62"]' | ✅💬 |  |
| `type` | varchar(30) | Y | MUL | 器具类型；"例：塞规 / 螺纹塞规 / 底孔规/ 游标卡尺" | ✅💬 |  |
| `number` | varchar(30) | Y | MUL | 器具编号；"例：GN52720A0600" | ✅💬 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `company` | varchar(50) | Y | - | 制造厂家；"例：海克斯康 无锡格康特" | ✅💬 |  |
| `name` | varchar(30) | Y | - | 器具名称；"例：带深度通止塞规 光通尺寸检测设备 粗糙度比对样块" | ✅💬 |  |
| `site` | varchar(30) | Y | MUL | 站点；"例：治通/广汇/娄塘/泰峰/智机" | ✅💬 |  |
