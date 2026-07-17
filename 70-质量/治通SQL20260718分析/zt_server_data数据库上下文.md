---
title: zt_server_data数据库上下文
created: 2026-07-17
updated: 2026-07-17
type: report
domain: 工程
tags: [数据管道, 报告]
---

# zt_server_data 数据库上下文（所有分析 Agent 必读）

## 连接方式

```bash
# git-bash 环境：
/f/mysql-8.0.29-winx64/bin/mysql.exe -u root zt_server_data -e "SQL语句"
# Windows 路径等价：F:\mysql-8.0.29-winx64\bin\mysql.exe -u root zt_server_data
```

- root 无密码，仅监听 127.0.0.1:3306
- 中文列名必须加反引号：`` SELECT `检测时间` FROM ... ``
- 输出默认 TAB 分隔；加 `-t` 参数可得表格格式

## 数据库本质

治通工厂终检/试漏工序检测数据仓库：缸体、缸盖、差壳、结构件四大产品族，35 张表，约 700 万条记录，6.3GB。数据跨度 2018 ~ 2026-07-17。

## 表清单（按业务分组）

### 密封（试漏）检测 — 7 张
| 表名 | 行数 | 时间列 | 结果列 | 检测通道列 |
|------|------|--------|--------|-----------|
| zt_cyl_block_seal | 113.7万 | `检测时间`(datetime) | `整体检测结果` | 箱体/水道/高压油道/螺纹孔 检测数据+结果, 断刀检测结果, 设备编号, 产品类型, 是否出货(bit) |
| zt_cyl_head_50t_seal | 77.3万 | `时间`(字符串!) | `气密综合结果` | 水道/油道/气道/PVC-BE/PVC-D/PVC-AC 数据+结果, 流量数据+结果 |
| zt_cyl_head_nf1_seal | 76.7万 | `测试时间`(字符串!) | `综合结果` | 气道/油道/水道/PCV孔 结果+数据 |
| zt_cyl_head_gb6_seal | 24.9万 | `日期`(datetime) | `结果` | 通道1~5 数据+结果 |
| zt_cyl_head_gl31_seal | 20.3万 | `测试时间`(字符串!) | (无单列综合结果，需从各通道汇总) | 气道/油道/水道/高压油道 结果+数据 |
| zt_cyl_head_evo_seal | 15.0万 | `时间`(字符串!) | `检测结果` | 水道/气道/低压油道1/低压油道2/高压油道 检测数据+结果, 设备编号 |
| zt_cyl_head_375t_seal | 11.3万 | `时间`(datetime) | `检测结果` | 水道/油道/气道/通道PVC1/通道PVC2 检测+结果, 设备编号 |

### 断芯检测（尺寸实测，57列）— 4 张
| 表名 | 行数 | 说明 |
|------|------|------|
| zt_cyl_block_brk_core_1 | 24.1万 | 时间(datetime), 测量结果; F301/F302/F305/F303 点1-3+XYZ, H301/H302/H305/H303 Y/Z/位置度, F100/F200 点位, 定位孔径, 孔中心距1/2, 尺寸结果, 光通/视觉/物理探针/流量检测, H333防错, 缸套1-3距离, 各检测状态 |
| zt_cyl_block_brk_core_2 | 26.3万 | 结构同 _1 |
| zt_cyl_block_brk_core_3 | 16.6万 | 结构不同：检测结果, 上面检测, 下面检测 等 |
| zt_cyl_head_evo_brk_core | 5.3万 | 时间, 综合结果, 密封性, K101 等 |

### 燃高检测 — 3 张
| 表名 | 行数 | 列 |
|------|------|-----|
| gb6_燃高 | 48.7万 | 日期(datetime), 检测结果, W1-W4, W平均值, W平均值到W1-W4, A/B/C, ABC平均值, E1-E6到W面值, 产线号, 人工 |
| zt_cyl_head_gl31_combustion_altitude | 1.7万 | 日期, 检测结果, W1-W3 等 |
| zt_cyl_head_gb6&nf1_combustion_altitude | 2.1万 | 表名含 & 必须加反引号 |

### 激光打码/打标 — 9 张
- zt_cyl_block_las_mark (64.3万): id, device_ip, device_name(缸体1线~8线), timestamp(datetime), mark_code, product_type, error_info, notification_status
- zt_cyl_block_las_mark_copy1 (58.5万): 历史快照，结构与主表类似
- zt_dct_las_mark (42.3万): DCT差壳打标
- zt_cyl_head_50t/375/evo/sge/gl31/gs6_las_mark: 各型号缸盖打标

### 出货与视觉 — 5 张
- zt_diff_hous_shipment (71.8万): 时间(datetime), 差壳类型(DCT300/DCTeco/E38H/E28A...), 二维码, 操作人员, 工位, 结果(合格/不合格/重码/二维码错误/直径38尺寸超差), 检测数量, 容量, 箱码, 视觉时间, 视觉结果, 重码, 备注
- left/right_front_wheel_housing_detection_system (0.6/0.5万): QR_CODEE, TOTAL_TIME, AREA_RESULT_1~34, AREA_TIME_1~34, RESULT, RESULT_TYPE, START_DATETIME(datetime)
- left/right_front_wheel_housing_detection_check_count_data (各70): DATETIME, CHECK_COUNT, QUALIFIED_COUNT

### 结构件 — 4 张
- zt_struc_part_557q_las_mark (1.5万): 时间, 产品类型, 二维码, 结果, 工位, 加工数量, 操作者
- zt_struc_part_557q_blind_rivet (10): 时间, 拉力, 位移, 结果, 基准拉力, 基准位移
- zt_struc_part_ndev_las_mark (0.3万), zt_struc_part_ndev_seal (空表)

### 元数据
- db_table_mapping (52行): 表名→地点/产品/工艺映射
- v_query_options: 视图

## ⚠️ 数据陷阱（必须处理）

1. **时间格式混乱**：`zt_cyl_head_50t_seal`/`nf1`/`gl31`/`evo` 的时间列是**字符串**（格式 `2018/12/17 11:49:15`），不是 datetime！时间分析必须 `STR_TO_DATE(`时间`, '%Y/%m/%d %H:%i:%s')`。其余表为原生 datetime。
2. **检测数据列是文本**：格式如 `02>:  2.04 bar:(OK):  6.55 cm3/`，提取数值需 SUBSTRING_INDEX/REGEXP 解析，例如：
   `CAST(REGEXP_SUBSTR(`箱体检测数据`, '[0-9]+\\.?[0-9]*(?= *cm3)') AS DECIMAL(10,3))`
3. **结果值集合**：合格/不合格/可修复/未检测/测试中/测试完成/空字符串。空字符串需单独统计，不可忽略。
4. **_copy1 表**是历史快照，与主表可能重叠，分析时用主表，copy1 仅作历史补充。
5. **_MASK_TO_V2 / _MUSID_SYNC_V2** 是同步元数据列，无业务含义，忽略。
6. **产品型号写法不统一**：LPNA / LP_NA / MP/LP_NA 混用，统计时需归一化。
7. **表名含特殊字符**：`zt_cyl_head_gb6&nf1_combustion_altitude`、`gb6_燃高` 必须加反引号。

## 输出要求（所有 Agent 统一）

1. 报告写入 `F:\zt_analysis\` 目录，文件名按卡片指定（如 `Q1-密封合格率基线.md`）
2. 报告结构：**分析目的 → 使用的SQL（完整可复现）→ 数据结果（表格）→ 结论（管理价值导向）→ 数据局限性**
3. **铁律：所有数字必须来自真实 SQL 查询结果，禁止编造/估算/凑数。算不出来的指标就明说"数据不足，无法计算"并说明缺什么。**
4. 结论必须指向管理行动（谁、什么时候、该关注什么），不要正确的废话。

---

## 相关页面
- [[治通试漏数据分析-总报告]]
- [[A1-数据质量审计]]
