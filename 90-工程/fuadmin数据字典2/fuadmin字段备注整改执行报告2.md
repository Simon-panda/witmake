---
title: fuadmin字段备注整改执行报告2
created: 2026-07-28
updated: 2026-07-28
type: report
domain: 工程
tags: [工程, 数据字典2, 报告, 已完成]
sources: [90-工程/fuadmin数据字典2/附件/fuadmin-remediation2.sql]
---

# fuadmin 字段备注整改执行报告（第2轮 · 字典2源码实证版）

> 执行日期：2026-07-28 ｜ 目标库：fuadmin@E:/mysql-data（MySQL 8.0.29）
> SQL 文件：`90-工程/fuadmin数据字典2/附件/fuadmin-remediation2.sql`

## 结果总览

| 指标 | 数值 |
|---|---|
| 表级备注 | **355/355（100%）** |
| 列级备注 | **6,325/6,369（99.3%）** |
| 未覆盖列 | 44 列，全部为**视图**（generator_bad_product_view 25、v_打卡记录 6 等），字典2 仅覆盖 Django models 基表，视图无语义来源 |
| 执行耗时 | 44 秒（MySQL 8.0 INSTANT 元数据变更） |
| 失败 | 1 条（generator_ingredients_split.stock 备注超 1024 字符，已截断语义核心后修复成功） |

## 备注内容质量

- **枚举完整解码**：如 `state` → `审批状态；0不通过 1已申请 2已复核 3已批准 100取消申请`
- **关联标注**：如 `creator_id` → `创建人；→system_users(软)`
- **站点分表继承主表语义**：`_gh/_zt/_tf` 分表备注与主表一致（字典2 同源）
- 空转跳过：22 列现有备注与字典2 一致，未重复写入

## 与第1轮对比

| 轮次 | 来源 | 列覆盖 | 特点 |
|---|---|---|---|
| 第1轮（未执行） | 字典1（库侧推断） | 5,615 条建议 | 推断置信度不一，仅出整改计划 |
| **第2轮（已执行）** | **字典2（源码实证，90.5%锚定）** | **5,855 条列级 + 334 条表级** | verbose_name/help_text/choices/行内注释四重证据 |

## 配套变更：MySQL 迁移 F→E

同日完成 MySQL 物理迁移：`F:/mysql-8.0.29-winx64 + F:/mysql-data` → `E:` 对应路径（15.49GB，robocopy 5分15秒）。三库完整（fuadmin 355 / zt_server_data 35 / zt_produce 43），zt_cyl_block_seal 等大表行数抽查一致。

⚠️ **遗留**：Windows 服务 MySQLZT 注册仍指向 F 盘旧路径（STOPPED 状态），当前 E 盘库以 console 模式运行。需管理员权限执行修正（见 [[MySQL迁移E盘-服务注册修正]] 或下条命令）：

```bat
:: 以管理员身份运行
sc delete MySQLZT
E:\mysql-8.0.29-winx64\bin\mysqld.exe --install MySQLZT --defaults-file="E:\mysql-8.0.29-winx64\my.ini"
sc start MySQLZT
```

修正前注意：**不要** `sc start MySQLZT`（会从 F 盘起旧库，端口冲突）。F 盘原目录保留未删。

## 相关页面

- [[fuadmin数据字典2总览]] — 备注语义来源
- [[字典2与旧版差异报告]] — 字典2 相对字典1 的修正
- [[fuadmin整改建议复核报告]] — 第1轮整改计划（已被本轮取代）
