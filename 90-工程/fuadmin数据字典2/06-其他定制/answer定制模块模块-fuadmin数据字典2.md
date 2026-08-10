---
title: answer定制模块模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 06-其他定制
tags: [工程, 数据字典2, 代码实证, answer定制模块]
---

# answer定制模块模块 · fuadmin 数据字典2（代码实证版）
> 域: 06-其他定制 | 表数: 2 | 字段: 38 | 代码锚定: 38(100%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/06-其他定制/answer定制模块模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_answer_list` | 答卷列表（考题/问卷定义） | 20 | 💻 |
| `generator_answer_sheet` | 答卷（员工答题成绩记录） | 105 | 💻 |

---

### generator_answer_list
**定义**：答卷列表（考题/问卷定义） ｜ **流角色**：考试管理-出题 ｜ **代码**：`generator/answer_list/model.py` ｜ **行数(估)**：20

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `link` | varchar(255) | Y | - | 链接 | ✅ |  |
| `dept_name` | varchar(50) | Y | - | 部门 | ✅ |  |
| `title` | varchar(50) | Y | - | 试卷标题 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `headline` | varchar(50) | Y | - | 大类表题 | ✅ |  |
| `passing_score` | int | Y | - | 合格分数 | ✅ |  |
| `code` | json | Y | - | 考题内容JSON（暂未启用） | ✅⚖️ |  |
| `choice_q` | int | Y | - | 选择题 | ✅ |  |
| `content` | longtext | Y | - | 考题汇总：题号列表，1-100判断题/101-200选择题 | ✅⚖️ |  |
| `estimate_q` | int | Y | - | 判断题 | ✅ |  |
| `must_do` | varchar(255) | Y | - | 必做题目（题号逗号分隔） | ✅⚖️ |  |
| `type` | tinyint(1) | Y | - | 状态；用于开启随机抽取题型的开关 | ✅💬 |  |

### generator_answer_sheet
**定义**：答卷（员工答题成绩记录） ｜ **流角色**：考试管理-作答 ｜ **代码**：`generator/answer_sheet/model.py` ｜ **行数(估)**：105

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述 | ✅📦 |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门 | ✅📦 |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间 | ✅📦 |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `score` | double | Y | - | 分数 | ✅ |  |
| `dept_name` | varchar(50) | Y | - | 部门名称 | ✅ |  |
| `name` | varchar(50) | Y | - | 员工姓名 | ✅ |  |
| `title` | varchar(50) | Y | - | 标题 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 创建人；→system_users(软) | ✅🔗📦 | →system_users(软) |
| `answer_type` | int | Y | - | 答卷状态：0未答卷/1已答卷 | ✅⚖️ |  |
| `code` | varchar(50) | Y | - | 员工工号 | ✅ |  |
| `headline` | varchar(50) | Y | - | 大类表题 | ✅ |  |
| `info` | longtext | Y | - | 答卷内容 | ✅ |  |
| `score_type` | int | Y | - | 合格状态：0不及格/1合格 | ✅⚖️ |  |
| `time` | varchar(50) | Y | - | 用时；4.8 | ✅💬 |  |
| `submit_time` | datetime(6) | Y | - | 提交时间 | ✅ |  |

---

## 同域兄弟模块
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
- [[06-其他定制/misc-site模块-fuadmin数据字典2|misc-site模块]]
- [[06-其他定制/misc-ticket模块-fuadmin数据字典2|misc-ticket模块]]
- [[06-其他定制/misc-total模块-fuadmin数据字典2|misc-total模块]]
- [[06-其他定制/misc-triangle模块-fuadmin数据字典2|misc-triangle模块]]
- [[06-其他定制/misc-zj2315模块-fuadmin数据字典2|misc-zj2315模块]]
- [[06-其他定制/test定制模块模块-fuadmin数据字典2|test定制模块模块]]
- [[06-其他定制/06-其他定制-业务流|06-其他定制业务流(代码验证版)]]
