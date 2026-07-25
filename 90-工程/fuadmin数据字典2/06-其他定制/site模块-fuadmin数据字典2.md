---
title: site模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, site]
---

# site模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 29 | 代码锚定: 28(97%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/site模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_site_management` | 现场管理 | 323 | 💻 |

---

### generator_site_management
**定义**：现场管理 ｜ **代码**：`generator/site_management/model.py` ｜ **行数(估)**：323

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:巡检单号） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `completion_date_rectification` | varchar(255) | Y | - | 整改完成日期 | ✅ |  |
| `deadline_rectification` | varchar(255) | Y | - | 整改截止日期 | ✅ |  |
| `description_countermeasures` | varchar(255) | Y | - | 对策描述 | ✅ |  |
| `inspection_ticket_number` | varchar(255) | Y | - | 巡检单号 | ✅ |  |
| `photo_rectification` | varchar(255) | Y | - | 整改后图片 | ✅ |  |
| `problem_description` | varchar(255) | Y | - | 问题描述 | ✅ |  |
| `problem_discovery_date` | varchar(255) | Y | - | 问题发生日期 | ✅ |  |
| `problem_image` | varchar(255) | Y | - | 问题图片 | ✅ |  |
| `region_id` | bigint | Y | MUL | 所在区域；→generator_management_area_allocation | ✅🔗 | →generator_management_area_allocation |
| `region_map` | varchar(255) | Y | - | 区域图 | ✅ |  |
| `responsible_person_id` | bigint | Y | MUL | 负责人；→system_users | ✅🔗 | →system_users |
| `inspection_states` | varchar(255) | Y | - | 状态 | ✅ |  |
| `inspector_id` | bigint | Y | MUL | 检查人；→system_users | ✅🔗 | →system_users |
| `history` | varchar(1000) | Y | - | 记录（界面:操作历史） | ✅🖥️ |  |
| `classification_5_s_id` | bigint | Y | MUL | 5S分类；→generator_definition_five_s | ✅🔗 | →generator_definition_five_s |
| `inspection_standards` | varchar(255) | Y | - | 检查标准 | ✅ |  |
| `problem_items` | varchar(255) | Y | - | 问题项目 | ✅ |  |
| `responsible_department_id` | bigint | Y | MUL | 责任部门；→system_dept | ✅🔗 | →system_dept |
| `rate` | int | Y | - | 评分；0-5分 | ✅💬 |  |
| `collaborators` | json | Y | - | 协作人；协作人，默认JSON数组格式，如：[{"id":1,"name":"张三"},{"id":2,"name":"李四"}]（界面:协作抄送人） | ✅🖥️ |  |
| `problem_level` | varchar(2) | Y | - | 问题等级；问题等级，可选：一级、二级、三级、四级；枚举[1=一级,2=二级,3=三级,4=四级] | ✅🔢 |  |
