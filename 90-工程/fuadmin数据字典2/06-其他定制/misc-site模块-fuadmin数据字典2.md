---
title: misc-site模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, misc-site]
---

# misc-site模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 1 | 字段: 29 | 代码锚定: 29(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/misc-site模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_site_management` | 现场管理（5S问题整改单） | 323 | 💻 |

---

### generator_site_management
**定义**：现场管理（5S问题整改单） ｜ **流角色**：5S问题整改闭环 ｜ **代码**：`generator/site_management/model.py` ｜ **行数(估)**：323

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
| `history` | varchar(1000) | Y | - | 记录 | ✅ |  |
| `classification_5_s_id` | bigint | Y | MUL | 5S分类；→generator_definition_five_s | ✅🔗 | →generator_definition_five_s |
| `inspection_standards` | varchar(255) | Y | - | 检查标准 | ✅ |  |
| `problem_items` | varchar(255) | Y | - | 问题项目 | ✅ |  |
| `responsible_department_id` | bigint | Y | MUL | 责任部门；→system_dept | ✅🔗 | →system_dept |
| `rate` | int | Y | - | 评分（0-5分） | ✅⚖️ |  |
| `collaborators` | json | Y | - | 协作人；协作人，默认JSON数组格式，如：[{"id":1,"name":"张三"},{"id":2,"name":"李四"}] | ✅ |  |
| `problem_level` | varchar(2) | Y | - | 问题等级；问题等级，可选：一级、二级、三级、四级；枚举[1=一级,2=二级,3=三级,4=四级] | ✅🔢 |  |

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
- [[06-其他定制/misc-ticket模块-fuadmin数据字典2|misc-ticket模块]]
- [[06-其他定制/misc-total模块-fuadmin数据字典2|misc-total模块]]
- [[06-其他定制/misc-triangle模块-fuadmin数据字典2|misc-triangle模块]]
- [[06-其他定制/misc-zj2315模块-fuadmin数据字典2|misc-zj2315模块]]
- [[06-其他定制/test定制模块模块-fuadmin数据字典2|test定制模块模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
