-- 班长产量达成率核算（预排班×每班计划产量基准）V1.0
-- 基准来源：generator_job_code.plan_output（正常节拍×当班制度工时的每班计划生产数）
-- 班组归属：generator_newscheduling_temp.approver（班长签字，已审核 status=1）
-- 去重规则：OP子码沿 parent_id 归并到线级码（父级 plan_output 相同则上挂），同线同班次只计一次基准
-- 宕机修正：可比达成率 = 实际 / (基准 × (1 - 宕机h/8h))，制度工时 8h/班
-- 计分：达成率≥95% → 50分；75–95% 线性 0→50；<75% → 0分
-- 参数：:date_start, :date_end, 站点（默认全站点，可按需加 AND t.site='治通'）

WITH ls AS (
  SELECT t.approver, t.date, t.day_night,
    COALESCE(
      CASE WHEN p3.plan_output=j.plan_output AND j.plan_output>0 THEN p3.name END,
      CASE WHEN p2.plan_output=j.plan_output AND j.plan_output>0 THEN p2.name END,
      CASE WHEN p1.plan_output=j.plan_output AND j.plan_output>0 THEN p1.name END,
      t.job_code_name) AS line_root,
    MAX(j.plan_output) AS base,
    SUM(t.actual_output) AS act,
    SUM(COALESCE(t.downtime,0)) AS dt
  FROM generator_newscheduling_temp t
  LEFT JOIN generator_job_code j  ON j.name=t.job_code_name
  LEFT JOIN generator_job_code p1 ON p1.id=j.parent_id
  LEFT JOIN generator_job_code p2 ON p2.id=p1.parent_id
  LEFT JOIN generator_job_code p3 ON p3.id=p2.parent_id
  WHERE t.date BETWEEN '2026-07-01' AND '2026-07-29'   -- ★ 考核周期
    AND t.status=1
    AND t.job_code_name LIKE '机加%'
    AND t.approver IS NOT NULL AND t.approver<>''
  GROUP BY t.approver, t.date, t.day_night, line_root
)
SELECT approver AS 班长,
       COUNT(*) AS 覆盖班次,
       SUM(base) AS 基准产量,
       SUM(act)  AS 实际产量,
       ROUND(100*SUM(act)/SUM(base),1) AS 达成率pct,
       ROUND(100*SUM(act)/SUM(base*(1-LEAST(dt,8)/8)),1) AS 可比达成率pct,
       ROUND(50*LEAST(1,GREATEST(0,(SUM(act)/SUM(base*(1-LEAST(dt,8)/8))-0.75)/0.20)),1) AS B2得分
FROM ls
GROUP BY approver
HAVING 覆盖班次>=20
ORDER BY 基准产量 DESC;
