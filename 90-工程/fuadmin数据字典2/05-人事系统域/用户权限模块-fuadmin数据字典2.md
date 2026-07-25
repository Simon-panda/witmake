---
title: 用户权限模块-fuadmin数据字典2
created: 2026-07-24
updated: 2026-07-24
type: reference
domain: 05-人事系统域
tags: [工程, 数据字典2, 代码实证, 用户权限]
---

# 用户权限模块 · fuadmin 数据字典2（代码实证版）
> 域: 05-人事系统域 | 表数: 29 | 字段: 335 | 代码锚定: 297(89%) | 生成: 2026-07-24 | 上游: [[fuadmin数据字典2总览]] | 旧版: [[90-工程/fuadmin数据字典/05-人事系统域/用户权限模块-fuadmin数据字典]]

> [!info] 证据图例
> ✅代码verbose/help实证 ｜ 💬行内注释 ｜ 🔢枚举解码 ｜ 🔗代码级关联 ｜ 🖥️前端界面label ｜ ⚖️冲突仲裁 ｜ 🔍推断(无代码锚点) ｜ 📦框架/基类字段

## 表清单
| 表 | 定义 | 行数(估) | 锚点 |
|---|---|---|---|
| `generator_authorization` | 授权表 | 78 | 💻 |
| `generator_inform` | 通知功能 | 8 | 💻 |
| `generator_users_ticket` |  | 3071 | 💻 |
| `system_api_white_list` | 接口白名单 | 0 | 💻 |
| `system_area` | 地区表 | 3440 | 💻 |
| `system_button` | 权限标识表 | 0 | 💻 |
| `system_category_dict` | 分类字典表 | 0 | 💻 |
| `system_config` | 系统配置表 | 0 | 💻 |
| `system_dept` | 部门表 | 27 | 💻 |
| `system_dict` | 字典表 | 9 | 💻 |
| `system_dict_item` | 字典表详情表 | 36 | 💻 |
| `system_file` | 文件管理 | 57721 | 💻 |
| `system_generator_template` | 代码生成器模板 | 54 | 💻 |
| `system_login_log` | 登录日志 | 0 | 💻 |
| `system_menu` | 菜单表 | 259 | 💻 |
| `system_menu_button` | 菜单权限表 | 1015 | 💻 |
| `system_menu_column_field` | 菜单数据列表 | 1203 | 💻 |
| `system_post` | 岗位表 | 40 | 💻 |
| `system_product_szb` |  | 0 | 🔍 |
| `system_role` | 角色表 | 54 | 💻 |
| `system_role_column` | M2M中间表: system_role ↔ system_menu_column_f | 15058 | 🔗 |
| `system_role_dept` | M2M中间表: system_role ↔ system_dept（数据权限-关联部 | 34 | 🔗 |
| `system_role_menu` | M2M中间表: system_role ↔ system_menu（关联菜单） | 2607 | 🔗 |
| `system_role_permission` | M2M中间表: system_role ↔ system_menu_button（关 | 10070 | 🔗 |
| `system_users` | 用户表 | 1625 | 💻 |
| `system_users_groups` |  | 0 | 🔍 |
| `system_users_post` | M2M中间表: system_users ↔ system_post（关联岗位） | 178 | 🔗 |
| `system_users_role` | M2M中间表: system_users ↔ system_role（关联角色） | 367 | 🔗 |
| `system_users_user_permissions` |  | 0 | 🔍 |

---

### generator_authorization
**定义**：授权表 ｜ **代码**：`generator/authorization/model.py` ｜ **行数(估)**：78

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:用户信息） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `code` | varchar(100) | Y | - | 授权码 | ✅ |  |
| `userinfo` | varchar(100) | Y | - | 用户信息 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `is_active` | int | Y | - | 状态 | ✅ |  |
| `work_dept` | json | Y | - | 工作站点；0治通 1智机 2广汇 3泰峰 4娄塘 | ✅💬 |  |

### generator_inform
**定义**：通知功能 ｜ **代码**：`generator/inform/model.py` ｜ **行数(估)**：8

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:状态） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `remind_record` | json | Y | - | 历史记录 | ✅ |  |
| `state` | int | Y | - | 状态；0待启动 1进行中 2已完成 | ✅💬 |  |
| `remind_state` | json | Y | - | 提醒状态；已通知过的内容存入,存入后就不需要再通知 ["当天", "三天前"] | ✅💬 |  |
| `remind_method` | json | Y | - | 提醒方式；需要通知的方式一共有4种通过复选框的形势存在["当天", "三天前", "一个月前", "半年前"] | ✅💬 |  |
| `remind_user` | json | Y | - | 提醒人；[169, 1] | ✅💬 |  |
| `remind_group` | varchar(100) | Y | - | 提醒群 | ✅ |  |
| `department` | varchar(50) | Y | - | 责任部门 | ✅ |  |
| `end_time` | date | Y | - | 结束时间 | ✅ |  |
| `start_time` | date | Y | - | 生效时间 | ✅ |  |
| `content` | longtext | Y | - | 提醒内容 | ✅ |  |
| `type` | varchar(20) | Y | - | 类型；合同或协议 公司资质 个人证书 特种设备 系统模块 | ✅💬 |  |
| `name` | varchar(100) | Y | - | 名称 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `avatar` | varchar(255) | Y | - | 照片 | ✅ |  |

### generator_users_ticket
**定义**：（待补充） ｜ **代码**：`generator/ticket/model.py` ｜ **行数(估)**：3071

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `punishment_method` | varchar(100) | Y | - | 处罚方式；处罚金额 培训和教育 奖励金额 | ✅💬 |  |
| `sum` | decimal(10,2) | Y | - | 金额 | ✅ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅ |  |
| `i_agree` | varchar(20) | Y | - | 是否确认；拒绝 同意 待确认（界面:确认状态） | ✅💬🖥️ |  |
| `is_active` | tinyint(1) | N | - | 是否启用（界面:状态） | ✅🖥️ |  |
| `remark` | varchar(255) | Y | - | 备注 | ✅ |  |
| `ticket_id` | bigint | N | MUL | →generator_ticket | 🔗 | →generator_ticket |
| `users_id` | bigint | N | MUL | →system_users | 🔗 | →system_users |
| `name` | varchar(50) | Y | - | 姓名工号；被处罚的员工工号和姓名可能包含职位 14003 潘利飞(生产部-班长)（界面:原辅料名称） | ✅💬🖥️ |  |
| `agree_user` | varchar(30) | Y | - | 签字人；是谁帮他签字的人 有可能是领导或者创建单子的人 | ✅💬 |  |

### system_api_white_list
**定义**：接口白名单 ｜ **代码**：`system/models.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `url` | varchar(200) | N | - | url；url地址（界面:图片） | ✅🖥️ |  |
| `method` | int | Y | - | 接口请求方法（界面:措施内容） | ✅🖥️ |  |
| `enable_datasource` | tinyint(1) | N | - | 激活数据权限 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### system_area
**定义**：地区表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：3440

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(100) | N | - | 名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(20) | N | UNI | 地区编码（界面:奖罚单号） | ✅🖥️ |  |
| `level` | bigint | N | - | 地区层级(1省份 2城市 3区县 4乡级) | ✅ |  |
| `pinyin` | varchar(255) | N | - | 拼音 | ✅ |  |
| `initials` | varchar(20) | N | - | 首字母 | ✅ |  |
| `enable` | tinyint(1) | N | - | 是否启用 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `pcode_id` | varchar(20) | Y | MUL | 父地区编码；→self | ✅🔗 | →self |

### system_button
**定义**：权限标识表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(64) | N | UNI | 权限名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(64) | N | UNI | 权限值（界面:奖罚单号） | ✅🖥️ |  |
| `status` | tinyint(1) | Y | - | 按钮状态（界面:完成状态） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### system_category_dict
**定义**：分类字典表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `label` | varchar(100) | Y | - | 显示名称（界面:标签） | ✅🖥️ |  |
| `value` | varchar(100) | Y | - | 实际值（界面:基础薪资） | ✅🖥️ |  |
| `code` | varchar(100) | Y | UNI | 编码（界面:奖罚单号） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 上级；→system_category_dict（界面:上级归属） | ✅🔗🖥️ | →system_category_dict |

### system_config
**定义**：系统配置表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `title` | varchar(50) | N | - | 标题（界面:任务名称） | ✅🖥️ |  |
| `key` | varchar(20) | N | - | 键（界面:序号） | ✅🖥️ |  |
| `value` | json | Y | - | 值（界面:基础薪资） | ✅🖥️ |  |
| `status` | tinyint(1) | N | - | 启用状态（界面:完成状态） | ✅🖥️ |  |
| `data_options` | json | Y | - | 数据options | ✅ |  |
| `form_item_type` | int | N | - | 表单类型；枚举[0=text,1=textarea,2=number,3=select,4=radio,5=checkbox,6=date,7=datetime,8=time,9=imgs,10=files,11=array,12=foreignkey,13=manytomany] | ✅🔢 |  |
| `rule` | json | Y | - | 校验规则 | ✅ |  |
| `placeholder` | varchar(50) | Y | - | 提示信息（界面:占位符） | ✅🖥️ |  |
| `setting` | json | Y | - | 配置 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 父级；→self（界面:上级归属） | ✅🔗🖥️ | →self |

### system_dept
**定义**：部门表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：27

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(64) | N | - | 部门名称（界面:原辅料名称） | ✅🖥️ |  |
| `owner` | varchar(32) | Y | - | 负责人 | ✅ |  |
| `phone` | varchar(32) | Y | - | 联系电话 | ✅ |  |
| `email` | varchar(32) | Y | - | 邮箱（界面:电子邮箱） | ✅🖥️ |  |
| `status` | tinyint(1) | Y | - | 部门状态（界面:完成状态） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 上级部门；→system_dept（界面:上级归属） | ✅🔗🖥️ | →system_dept |

### system_dict
**定义**：字典表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：9

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 备注 | ✅ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(100) | Y | - | 字典名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(100) | Y | - | 编码（界面:奖罚单号） | ✅🖥️ |  |
| `status` | tinyint(1) | N | - | 状态（界面:完成状态） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### system_dict_item
**定义**：字典表详情表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：36

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `icon` | varchar(100) | Y | - | ICON（界面:图标） | ✅🖥️ |  |
| `label` | varchar(100) | Y | - | 显示名称（界面:标签） | ✅🖥️ |  |
| `value` | varchar(100) | Y | - | 实际值（界面:基础薪资） | ✅🖥️ |  |
| `status` | tinyint(1) | N | - | 状态（界面:完成状态） | ✅🖥️ |  |
| `remark` | varchar(2000) | Y | - | 备注 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `dict_id` | bigint | N | MUL | 字典；→system_dict | ✅🔗 | →system_dict |

### system_file
**定义**：文件管理 ｜ **代码**：`system/models.py` ｜ **行数(估)**：57721

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(255) | Y | - | 实际名称（界面:原辅料名称） | ✅🖥️ |  |
| `save_name` | varchar(255) | Y | - | 存储名称 | ✅ |  |
| `url` | varchar(100) | N | - | （界面:图片） | 🖥️ |  |
| `size` | bigint | Y | - | 大小（界面:尺寸） | ✅🖥️ |  |
| `md5sum` | varchar(36) | N | - | 文件md5 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### system_generator_template
**定义**：代码生成器模板 ｜ **代码**：`system/models.py` ｜ **行数(估)**：54

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(64) | N | - | 模板名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(32) | N | - | 模板编码（界面:奖罚单号） | ✅🖥️ |  |
| `form_info` | longtext | N | - | 表单信息 | ✅ |  |
| `table_info` | longtext | N | - | 表格信息 | ✅ |  |
| `has_menu` | tinyint(1) | N | - | 是否已经生成菜单 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### system_login_log
**定义**：登录日志 ｜ **代码**：`system/models.py` ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `username` | varchar(150) | Y | - | 登录用户名（界面:工号） | ✅🖥️ |  |
| `ip` | varchar(50) | Y | - | 登录ip | ✅ |  |
| `agent` | varchar(255) | Y | - | agent信息 | ✅ |  |
| `browser` | varchar(100) | Y | - | 浏览器名 | ✅ |  |
| `os` | varchar(100) | Y | - | 操作系统 | ✅ |  |
| `continent` | varchar(50) | Y | - | 州 | ✅ |  |
| `country` | varchar(50) | Y | - | 国家 | ✅ |  |
| `country_code` | varchar(20) | Y | - | 简称 | ✅ |  |
| `country_english` | varchar(100) | Y | - | 英文全称 | ✅ |  |
| `province` | varchar(50) | Y | - | 省份 | ✅ |  |
| `city` | varchar(50) | Y | - | 城市 | ✅ |  |
| `district` | varchar(50) | Y | - | 县区 | ✅ |  |
| `isp` | varchar(100) | Y | - | 运营商 | ✅ |  |
| `area_code` | varchar(20) | Y | - | 区域代码 | ✅ |  |
| `belong_dept` | varchar(100) | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `login_type` | varchar(20) | Y | - | 登录类型；枚举[1=普通登录] | ✅🔢 |  |
| `latitude` | double | Y | - | 纬度 | ✅ |  |
| `longitude` | double | Y | - | 经度 | ✅ |  |
| `creator_id` | bigint | Y | - | 🔍待补充 | 🔍 |  |
| `modifier` | varchar(100) | Y | - | 修改人 | ✅📦 |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `create_datetime` | datetime | Y | - | 创建时间 | ✅📦 |  |
| `update_datetime` | datetime | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |

### system_menu
**定义**：菜单表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：259

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `icon` | varchar(64) | N | - | 菜单图标 | ✅ |  |
| `title` | varchar(64) | N | - | 菜单名称（界面:任务名称） | ✅🖥️ |  |
| `permission` | varchar(64) | Y | - | 权限标识 | ✅ |  |
| `is_ext` | tinyint(1) | N | - | 是否外链 | ✅ |  |
| `type` | int | N | - | 是否目录；枚举[0=目录,1=菜单]（界面:问题分类） | ✅🔢🖥️ |  |
| `path` | varchar(128) | Y | - | 路由地址 | ✅ |  |
| `redirect` | varchar(128) | Y | - | 重定向地址 | ✅ |  |
| `component` | varchar(128) | Y | - | 组件地址（界面:控件-FormItem） | ✅🖥️ |  |
| `name` | varchar(50) | Y | - | 组件名称（界面:原辅料名称） | ✅🖥️ |  |
| `status` | tinyint(1) | N | - | 菜单状态（界面:完成状态） | ✅🖥️ |  |
| `keepalive` | tinyint(1) | N | - | 是否页面缓存 | ✅ |  |
| `hide_menu` | tinyint(1) | N | - | 侧边栏中是否隐藏 | ✅ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `parent_id` | bigint | Y | MUL | 上级菜单；→system_menu（界面:上级归属） | ✅🔗🖥️ | →system_menu |

### system_menu_button
**定义**：菜单权限表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：1015

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(64) | N | - | 名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(64) | N | - | 权限值（界面:奖罚单号） | ✅🖥️ |  |
| `api` | varchar(200) | N | - | 接口地址（界面:按钮状态） | ✅🖥️ |  |
| `method` | int | Y | - | 接口请求方法（界面:措施内容） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `menu_id` | bigint | N | MUL | 关联菜单；→system_menu | ✅🔗 | →system_menu |

### system_menu_column_field
**定义**：菜单数据列表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：1203

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(64) | N | - | 名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(64) | N | - | 权限值（界面:奖罚单号） | ✅🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |
| `menu_id` | bigint | N | MUL | 关联菜单；→system_menu | ✅🔗 | →system_menu |

### system_post
**定义**：岗位表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：40

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(64) | N | - | 岗位名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(32) | N | - | 岗位编码（界面:奖罚单号） | ✅🖥️ |  |
| `status` | int | N | - | 岗位状态；枚举[0=离职,1=在职]（界面:完成状态） | ✅🔢🖥️ |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### system_product_szb
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:上级产品） | 🔍🖥️ |  |
| `product_name` | varchar(255) | Y | - | （界面:产品名） | 🔍🖥️ |  |
| `workpiece_number` | varchar(255) | Y | - | （界面:工件号） | 🔍🖥️ |  |
| `report_time` | datetime | Y | - | （界面:报告时间） | 🔍🖥️ |  |
| `product_id` | int | Y | - | （界面:产品） | 🔍🖥️ | →generator_bad_product(推断) |
| `report` | mediumblob | Y | - | 🔍待补充 | 🔍 |  |

### system_role
**定义**：角色表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：54

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ |  |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `name` | varchar(64) | N | - | 角色名称（界面:原辅料名称） | ✅🖥️ |  |
| `code` | varchar(64) | N | UNI | 角色编码（界面:奖罚单号） | ✅🖥️ |  |
| `status` | tinyint(1) | N | - | 角色状态（界面:完成状态） | ✅🖥️ |  |
| `admin` | tinyint(1) | N | - | 是否为admin（界面:管理员） | ✅🖥️ |  |
| `data_range` | int | N | - | 数据权限范围；枚举[0=仅本人数据权限,1=本部门数据权限,2=本部门及以下数据权限,3=全部数据权限,4=自定数据权限] | ✅🔢 |  |
| `creator_id` | bigint | Y | MUL | 🔍待补充 | 🔍 |  |

### system_role_column
**定义**：M2M中间表: system_role ↔ system_menu_column_field（列表权限） ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：15058

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键（界面:列表权限） | 🔗🖥️ |  |
| `role_id` | bigint | N | MUL | →system_role 主键 | 🔗 | →system_role |
| `menucolumnfield_id` | bigint | N | MUL | 🔍待补充 | 🔍 |  |

### system_role_dept
**定义**：M2M中间表: system_role ↔ system_dept（数据权限-关联部门） ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：34

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键（界面:列表权限） | 🔗🖥️ |  |
| `role_id` | bigint | N | MUL | →system_role 主键 | 🔗 | →system_role |
| `dept_id` | bigint | N | MUL | →system_dept 主键（界面:所属部门） | 🔗🖥️ | →system_dept |

### system_role_menu
**定义**：M2M中间表: system_role ↔ system_menu（关联菜单） ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：2607

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键（界面:列表权限） | 🔗🖥️ |  |
| `role_id` | bigint | N | MUL | →system_role 主键 | 🔗 | →system_role |
| `menu_id` | bigint | N | MUL | →system_menu 主键 | 🔗 | →system_menu |

### system_role_permission
**定义**：M2M中间表: system_role ↔ system_menu_button（关联菜单的接口按钮） ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：10070

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键（界面:列表权限） | 🔗🖥️ |  |
| `role_id` | bigint | N | MUL | →system_role 主键 | 🔗 | →system_role |
| `menubutton_id` | bigint | N | MUL | 🔍待补充 | 🔍 |  |

### system_users
**定义**：用户表 ｜ **代码**：`system/models.py` ｜ **行数(估)**：1625

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `password` | varchar(128) | N | - | 密码（界面:当前密码） | 📦🖥️ |  |
| `last_login` | datetime(6) | Y | - | 最后登录时间 | 📦 |  |
| `is_superuser` | tinyint(1) | N | - | 超级管理员标志 | 📦 |  |
| `is_staff` | tinyint(1) | N | - | 后台员工标志 | 📦 |  |
| `is_active` | tinyint(1) | N | - | 账号启用标志（界面:状态） | 📦🖥️ |  |
| `date_joined` | datetime(6) | N | - | 注册时间 | 📦 |  |
| `id` | bigint | N | PRI | Id（界面:列表权限） | ✅📦🖥️ | →django_admin_log(推断) |
| `remark` | varchar(255) | Y | - | 描述（界面:备注） | ✅📦🖥️ |  |
| `modifier` | varchar(255) | Y | - | 修改人 | ✅📦 |  |
| `belong_dept` | int | Y | - | 数据归属部门（界面:所属部门） | ✅📦🖥️ |  |
| `update_datetime` | datetime(6) | Y | - | 修改时间（界面:未结单） | ✅📦🖥️ |  |
| `create_datetime` | datetime(6) | Y | - | 创建时间 | ✅📦 |  |
| `sort` | int | Y | - | 显示排序 | ✅📦 |  |
| `username` | varchar(150) | N | UNI | 用户账号（界面:工号） | ✅🖥️ |  |
| `email` | varchar(255) | Y | - | 邮箱（界面:电子邮箱） | ✅🖥️ |  |
| `mobile` | varchar(255) | Y | - | 电话 | ✅ |  |
| `avatar` | longtext | Y | - | 头像（界面:照片） | ✅🖥️ |  |
| `name` | varchar(40) | N | - | 姓名（界面:原辅料名称） | ✅🖥️ |  |
| `status` | tinyint(1) | N | - | 状态；True 激活 False 禁用（界面:完成状态） | ✅💬🖥️ |  |
| `gender` | int | Y | - | 性别；枚举[0=女,1=男] | ✅🔢 |  |
| `user_type` | int | Y | - | 用户类型；枚举[0=后台用户,1=前台用户] | ✅🔢 |  |
| `first_name` | varchar(150) | Y | - | 🔍待补充 |  |  |
| `last_name` | varchar(150) | Y | - | 🔍待补充 |  |  |
| `home_path` | varchar(150) | Y | - | 🔍待补充 |  |  |
| `creator_id` | bigint | Y | MUL | 创建人 | 📦 |  |
| `dept_id` | bigint | Y | MUL | 所属部门；关联部门；→system_dept | ✅🔗 | →system_dept |
| `is_delete` | tinyint(1) | N | - | 是否删除；是否删除(软删除标记)（界面:封存） | ✅📦🖥️ |  |
| `wechat_id` | varchar(150) | Y | - | （界面:企业微信ID） | 🖥️ |  |
| `working_type` | int | Y | - | working_system（界面:工作类型） | ✅🖥️ |  |
| `resignation_time` | datetime(6) | Y | - | 离职时间 | ✅ |  |
| `dept_level` | int | Y | - | 部门等级（界面:审批等级） | ✅🖥️ |  |
| `regulatory_dept` | json | Y | - | 监管部门 | ✅ |  |
| `work_dept` | json | Y | - | 工作站点；0治通 1智机 2广汇 3泰峰 4娄塘 | ✅💬 |  |
| `entry_time` | datetime(6) | Y | - | 入职时间 | ✅ |  |
| `wechat_openid` | varchar(150) | Y | UNI | 微信小程序openid | ✅ |  |

### system_users_groups
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `users_id` | bigint | N | MUL | 🔍待补充 | 🔍 | →system_users(推断) |
| `group_id` | int | N | MUL | 🔍待补充 | 🔍 | →system_users_groups(推断) |

### system_users_post
**定义**：M2M中间表: system_users ↔ system_post（关联岗位） ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：178

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键（界面:列表权限） | 🔗🖥️ |  |
| `users_id` | bigint | N | MUL | →system_users 主键 | 🔗 | →system_users |
| `post_id` | bigint | N | MUL | →system_post 主键 | 🔗 | →system_post |

### system_users_role
**定义**：M2M中间表: system_users ↔ system_role（关联角色） ｜ **类型**：🔗M2M中间表 ｜ **行数(估)**：367

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | 中间表主键（界面:列表权限） | 🔗🖥️ |  |
| `users_id` | bigint | N | MUL | →system_users 主键 | 🔗 | →system_users |
| `role_id` | bigint | N | MUL | →system_role 主键 | 🔗 | →system_role |

### system_users_user_permissions
**定义**：（待补充） ｜ **行数(估)**：0

| 字段 | 类型 | 可空 | 键 | 语义 | 证据 | 关联 |
|---|---|---|---|---|---|---|
| `id` | bigint | N | PRI | （界面:列表权限） | 🔍🖥️ |  |
| `users_id` | bigint | N | MUL | 🔍待补充 | 🔍 | →system_users(推断) |
| `permission_id` | int | N | MUL | 🔍待补充 | 🔍 | →system_role_permission(推断) |
