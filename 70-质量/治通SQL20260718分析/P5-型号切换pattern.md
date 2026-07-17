---
title: P5-型号切换pattern
created: 2026-07-17
updated: 2026-07-17
type: report
domain: 生产
tags: [生产, 报告, OEE]
---

# P5 — 缸体产线型号切换 Pattern 分析

> 基于 `zt_cyl_block_las_mark`（激光打标记录），按 device_name + timestamp 排序识别切换模式。
> 数据范围：2022-11-10 ~ 2026-07-17，9 条产线，645,865 条记录，6 种产品型号。

---

## 一、分析目的

识别缸体产线型号切换的频次、耗时和批次规模，量化切换对产能的冲击，为排产优化和 SMED 改进提供数据基础。

---

## 二、使用的 SQL

### 2.1 切换点识别（窗口函数 LAG）

```sql
-- 每条线的相邻记录 product_type 不同 → 一次切换
WITH ordered AS (
  SELECT device_name, DATE(timestamp) AS dt, product_type,
         LAG(product_type) OVER (PARTITION BY device_name ORDER BY timestamp) AS prev_pt
  FROM zt_cyl_block_las_mark WHERE product_type IS NOT NULL
)
SELECT device_name, COUNT(*) AS total_switches,
       COUNT(DISTINCT dt) AS active_days,
       ROUND(COUNT(*)/COUNT(DISTINCT dt),1) AS avg_switches_per_day
FROM ordered
WHERE prev_pt IS NOT NULL AND product_type != prev_pt
GROUP BY device_name ORDER BY total_switches DESC;
```

### 2.2 换型时间间隔分布

```sql
WITH ordered AS (
  SELECT device_name, timestamp, product_type,
         LAG(product_type) OVER w AS prev_pt,
         LAG(timestamp) OVER w AS prev_ts
  FROM zt_cyl_block_las_mark WHERE product_type IS NOT NULL
  WINDOW w AS (PARTITION BY device_name ORDER BY timestamp)
),
switch_gaps AS (
  SELECT TIMESTAMPDIFF(MINUTE, prev_ts, timestamp) AS gap_minutes
  FROM ordered
  WHERE prev_pt IS NOT NULL AND product_type != prev_pt
)
SELECT CASE 
    WHEN gap_minutes < 10 THEN '0-10min'
    WHEN gap_minutes < 30 THEN '10-30min'
    WHEN gap_minutes < 60 THEN '30-60min'
    WHEN gap_minutes < 120 THEN '1-2h'
    WHEN gap_minutes < 240 THEN '2-4h'
    WHEN gap_minutes < 480 THEN '4-8h'
    WHEN gap_minutes < 1440 THEN '8-24h'
    ELSE '>24h' END AS gap_range,
  COUNT(*) AS switch_cnt,
  ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(), 1) AS pct
FROM switch_gaps GROUP BY gap_range ORDER BY MIN(gap_minutes);
```

### 2.3 批次大小（连续同型号打码件数）

```sql
WITH ordered AS (
  SELECT device_name, timestamp, product_type,
         LAG(product_type) OVER (PARTITION BY device_name ORDER BY timestamp) AS prev_pt
  FROM zt_cyl_block_las_mark WHERE product_type IS NOT NULL
),
grp AS (
  SELECT device_name, product_type,
         SUM(CASE WHEN prev_pt IS NULL OR product_type != prev_pt THEN 1 ELSE 0 END) 
           OVER (PARTITION BY device_name ORDER BY timestamp) AS batch_id
  FROM ordered
),
batch_sizes AS (
  SELECT COUNT(*) AS batch_size FROM grp
  GROUP BY device_name, product_type, batch_id
)
-- 用 ROW_NUMBER 近似的四分位数
SELECT ... FROM batch_sizes;
```

### 2.4 各线各型号打码量

```sql
SELECT device_name, product_type, COUNT(*) AS pieces
FROM zt_cyl_block_las_mark WHERE product_type IS NOT NULL
GROUP BY device_name, product_type
ORDER BY device_name, pieces DESC;
```

---

## 三、数据结果

### 3.1 各产线切换频次总览

| 产线 | 切换总次数 | 有切换天数 | 日均切换(活跃日) | 总运营天数 | 切换密度 |
|------|-----------|-----------|-----------------|-----------|---------|
| 缸体1线 | 118 | 67 | 1.8 | 841 | **最高** |
| 缸体3线 | 96 | 56 | 1.7 | 275 | 高 |
| 缸体5线 | 81 | 51 | 1.6 | 764 | 高 |
| 缸体6线 | 75 | 45 | 1.7 | 652 | 中高 |
| 缸体7线 | 51 | 30 | 1.7 | 362 | 中 |
| 缸体4线 | 44 | 29 | 1.5 | 950 | **最低** |
| 缸体8线 | 28 | 15 | 1.9 | 138 | 中 |
| 缸体9线 | 12 | 10 | 1.2 | 25 | 低 |
| 缸体2线 | 9 | 7 | 1.3 | 216 | 低 |
| **合计** | **514** | — | — | — | — |

> 解读：切换**不频繁**。绝大多数天数（80-95%）产线全天只跑一个型号。即使在有切换的日子里，日均切换 1.2–1.9 次（即每天最多换 1 次型，极少 2 次以上）。

### 3.2 换型时间间隔分布

| 间隔区间 | 切换次数 | 占比 | 累计占比 |
|---------|---------|------|---------|
| 0–10 分钟 | 114 | 22.2% | 22.2% |
| 10–30 分钟 | 120 | 23.3% | 45.5% |
| 30–60 分钟 | 57 | 11.1% | 56.6% |
| 1–2 小时 | 49 | 9.5% | 66.1% |
| 2–4 小时 | 35 | 6.8% | 73.0% |
| 4–8 小时 | 26 | 5.1% | 78.0% |
| 8–24 小时 | 49 | 9.5% | 87.5% |
| >24 小时 | 64 | 12.5% | 100% |

> 关键解读：
> - **45.5% 的切换在 30 分钟内完成**（打码机记录层面的首末件间隔），这是真实的换型窗口。
> - 8 小时以上（22%）大概率包含班次交接、夜班停机、周末休息，非纯换型耗时。
> - 将间隔 ≤2 小时视为"当班换型"，则 66% 的切换属于此类，中位间隔约 **20–30 分钟**。

### 3.3 批次大小分布 — 全局

| 统计量 | 数值 |
|-------|------|
| 总批次数 | 523 |
| 最小批次 | 1 件 |
| P25 | 6 件 |
| **中位数 (P50)** | **31 件** |
| P75 | 960 件 |
| 平均值 | 1,234 件 |
| 最大批次 | 39,948 件 |

| 批次范围 | 批次数 | 占比 |
|---------|-------|------|
| 1–9 件 | 159 | 30.4% |
| 10–49 件 | 126 | 24.1% |
| 50–99 件 | 25 | 4.8% |
| 100–499 件 | 49 | 9.4% |
| 500–999 件 | 38 | 7.3% |
| 1000–1999 件 | 45 | 8.6% |
| 2000–4999 件 | 51 | 9.8% |
| 5000+ 件 | 30 | 5.7% |

> **极度双峰分布**：54.5% 的批次 ≤49 件（微批次，大概率是调试/首件确认/试切），另一端则是 2,000–40,000 件的连续大批量。

### 3.4 各产线批次规模对比

| 产线 | 批次数 | 最小 | 最大 | 平均 | 特征 |
|------|-------|------|------|------|------|
| 缸体4线 | 45 | 1 | 39,948 | 3,617 | 超级大批次，极稳 |
| 缸体2线 | 10 | 1 | 15,923 | 2,918 | 数据量小但批次大 |
| 缸体5线 | 82 | 1 | 18,133 | 1,488 | 切换多+批次大 |
| 缸体6线 | 76 | 1 | 25,793 | 1,387 | 类似5线 |
| 缸体1线 | 119 | 1 | 25,634 | 1,131 | 切换最多，批次中等 |
| 缸体7线 | 52 | 1 | 4,112 | 711 | 中小批次为主 |
| 缸体8线 | 29 | 1 | 5,027 | 593 | 中小批次 |
| 缸体3线 | 97 | 1 | 12,844 | 375 | 切换多，批次小 |
| 缸体9线 | 13 | 12 | 201 | 71 | 极小批次 |

### 3.5 各型号批次规模

| 型号 | 批次数 | 平均批次 | 总件数 |
|------|-------|---------|--------|
| MP缸体 | 90 | 1,659 | 149,332 |
| PFI缸体 | 86 | 1,461 | 125,629 |
| LPNA缸体 | 133 | 1,297 | 172,459 |
| TDC缸体 | 18 | 1,080 | 19,441 |
| LP缸体 | 153 | 1,043 | 159,573 |
| MPNA缸体 | 43 | 441 | 18,967 |

### 3.6 切换方向 TOP 15

| 产线 | 切换方向 | 次数 |
|------|---------|------|
| 缸体1线 | LP → LPNA | 33 |
| 缸体1线 | LPNA → LP | 28 |
| 缸体5线 | LP → LPNA | 15 |
| 缸体6线 | LP → LPNA | 15 |
| 缸体5线 | LPNA → LP | 14 |
| 缸体6线 | LPNA → LP | 13 |
| 缸体1线 | MP → LP | 12 |
| 缸体5线 | LPNA → PFI | 12 |
| 缸体5线 | PFI → LPNA | 11 |
| 缸体6线 | LPNA → PFI | 10 |
| 缸体6线 | PFI → LPNA | 10 |
| 缸体1线 | LP → MP | 9 |
| 缸体4线 | LPNA → LP | 9 |
| 缸体7线 | MP → PFI | 8 |
| 缸体4线 | LP → LPNA | 8 |

> 切换集中在 **LP ↔ LPNA** 和 **LPNA ↔ PFI** 两对组合，合计占总切换的 60% 以上。

### 3.7 近 30 天状况（2026-06-17 ~ 2026-07-17）

近 30 天**几乎无切换**：各线每天只跑 1 个型号。仅 缸体3线 在 7/3 和 7/14 出现 2 型号同日打码。

---

## 四、结论与管理建议

### 结论 1：切换频率低，但成本不低

- 514 次切换覆盖约 4 年，日均全厂仅 0.35 次切换。这不是"切换太频繁"的问题，而是"每次切换代价大 → 不敢频繁切换 → 被迫长批次"。
- 即使每天只换 1 次，按中位间隔 20-30 分钟 + 首件确认时间，单次切换保守损耗 **30–60 分钟产能**。

### 结论 2：换型间隔显示优化空间

- 45% 的切换在 30 分钟内完成（真实换型窗口），但仍有 22% 超过 8 小时。
- **行动建议：对 缸体1线、缸体5线 推行 SMED 快速换模试点**，目标将换型窗口压缩到 ≤15 分钟。从 LP↔LPNA 这个最高频切换方向开始。

### 结论 3：微批次（≤49 件）占 54.5%，存在调试浪费

- 30.4% 的批次 ≤9 件，24.1% 的批次 10–49 件。这些大概率是首件调试、试切验证或异常中断后的重新起跑。
- **行动建议：在生产日报/报工系统中新增"微批次原因"字段（首件调试 / 异常中断 / 补单），追因后再治。**

### 结论 4：产线分工建议

| 产线 | 定位建议 | 理由 |
|------|---------|------|
| 缸体4线 | **专线专品**（LP/MP 大批量） | 4年仅44次切换，平均批次3,617件 |
| 缸体1线 | **弹性线**（多品种快速切换） | 切换最多(118次)，已习惯多品种 |
| 缸体3线 | **需关注**（切换多但批次小） | 97次切换，平均批次仅375件 — 效率低 |
| 缸体9线 | **备线/试制线** | 仅946件，批次极小(平均71件) |

### 结论 5：LP ↔ LPNA 是最大切换痛点

- 这两个型号的互切占全部切换的 30%+。如果两者工装兼容性高，应评估**合并工装或快速定位方案**，把 LP↔LPNA 的切换成本降到接近 0。

---

## 五、数据局限性

| 局限 | 说明 |
|------|------|
| 间隔 ≠ 换型时间 | `timestamp` 间隔是打码机记录的"上一型号末件 → 下一型号首件"时间差，包含了可能的停机、班次切换、人员休息，**不等于**实际工装更换+调试时间。需配合产线日报人工对照验证。 |
| 微批次原因未知 | ≤49 件的批次占比高但无法从打码记录中区分"调试废件"还是"小批量急单"。需业务系统补充上下文。 |
| 产线9数据量极少 | 缸体9线仅 946 条记录，统计意义有限。 |
| 仅覆盖打码工序 | 切换影响是全流程的（上下料、加工、检测），本分析仅反映激光打码环节的时间线。 |
| 2022-2023 年数据稀疏 | 早期仅有 1-4 条线运行，切换模式与当前 9 线满产不可比。 |

---

*报告生成时间：2026-07-17*
*数据源：`zt_cyl_block_las_mark`（645,865 行），MySQL zt_server_data*

---

## 相关页面
- [[治通试漏数据分析-总报告]]
- [[zt_server_data数据库上下文]]
