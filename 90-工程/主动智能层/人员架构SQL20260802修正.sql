-- ============================================================================
-- 人员架构数据同步 SQL v2（全量版）  2026-08-02
-- 依据: Simon 修订版《人员组织架构与Agent投放规划》组织架构图（唯一事实源）
-- 目标库: fuadmin（生产库，治通服务器）
-- ⚠️ 取代 v1（4 处修正版），v1 内容已全部并入本脚本
-- 2026-08-02 增补: B9 孙明 lv8→lv5（公司级MPC）
-- 2026-08-02 定级修正(Simon): 郑敏维持 lv2 不变(取消升lv1)、谭昌发 lv1→lv3(新增"子公司一把手"层级)
-- ⚠️ dept_level / dept_id 影响 fuadmin 后台数据权限与可见范围，
--    被修改人需重新登录生效；建议非工作时间执行
-- ⚠️ 先在 E 盘本地快照库演练，再到生产库执行
-- 执行方式: 事务内逐区执行，每区先 SELECT 核对再 UPDATE；
--           全部复核后取消末尾 COMMIT 注释提交
-- 编制: Woker | 审核: Simon
-- ============================================================================

START TRANSACTION;

-- ============================================================================
-- A. 集团/公司级（2 人层级调整）
-- ============================================================================
-- A1 郑敏：维持 lv2 不变（大股东；曾拟升 lv1，Simon 2026-08-02 定回 lv2）
--      生产库原本即为 lv2，无需改动，故无 UPDATE 语句
--
-- A2 谭昌发 lv1 → lv3（泰峰一把手；lv3=新增"子公司一把手"层级，Simon 2026-08-02 定）
UPDATE system_users SET dept_level = 3, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 291 AND dept_level = 1;

-- ============================================================================
-- B. 上海治通（升 5 / 降 4）
-- ============================================================================
-- B1 潘利飞 lv6 → lv5（生产主管，对齐 7-30 考核名单 C 类主管）
UPDATE system_users SET dept_level = 5, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 24 AND dept_level = 6;

-- B2 孟永超 lv8 → lv6（质量班长）
UPDATE system_users SET dept_level = 6, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 478 AND dept_level = 8;

-- B3 邱桂昊 lv8 → lv5（数据主管；同时修正 belong_dept 10→17 与 dept_id 对齐）
UPDATE system_users SET dept_level = 5, belong_dept = 17, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 97 AND dept_level = 8;

-- B4 石垒 lv8 → lv4（项目经理，dept_id=11 项目部已在库）
UPDATE system_users SET dept_level = 4, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 19 AND dept_level = 8;

-- B5 倪新磊 lv5 → lv8（架构图已不含，降级为普通员工）
UPDATE system_users SET dept_level = 8, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 1152 AND dept_level = 5;

-- B6 温天祯 lv5 → lv8
UPDATE system_users SET dept_level = 8, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 730 AND dept_level = 5;

-- B7 赵配配 lv5 → lv8
UPDATE system_users SET dept_level = 8, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 21 AND dept_level = 5;

-- B8 陶新芋 lv5 → lv8
UPDATE system_users SET dept_level = 8, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 1389 AND dept_level = 5;

-- B9 孙明 lv8 → lv5（公司级MPC，治通生产部）
UPDATE system_users SET dept_level = 5, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 1401 AND dept_level = 8;

-- ============================================================================
-- C. 安徽广汇（调动 5 / 升 3 / 降 1）
-- ============================================================================
-- C1 李雪峰 dept 10 → 4（广汇厂长兼工程部负责人，挂公司级；lv4 不变）
UPDATE system_users SET dept_id = 4, belong_dept = 4, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 13 AND dept_id = 10;

-- C2 曾华 dept 3 → 4（外联行政经理，广汇公司级；lv4 不变）
UPDATE system_users SET dept_id = 4, belong_dept = 4, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 195 AND dept_id = 3;

-- C3 王付毫 dept 10 → 20（广汇生产班长；lv6 不变）
UPDATE system_users SET dept_id = 20, belong_dept = 20, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 184 AND dept_id = 10;

-- C4 祝新斌 dept 10 → 20 且 lv8 → 6（广汇生产班长）
UPDATE system_users SET dept_id = 20, belong_dept = 20, dept_level = 6, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 36 AND dept_id = 10;

-- C5 夏玉强 dept 12 → 21 且 lv6 → 5（广汇质量主管；belong_dept 已是 21）
UPDATE system_users SET dept_id = 21, dept_level = 5, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 118 AND dept_id = 12;

-- C6 李丹洋 dept 14 → 23（广汇物流班长；lv6 不变；Simon 版用字"李丹阳"，同人）
UPDATE system_users SET dept_id = 23, belong_dept = 23, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 119 AND dept_id = 14;

-- C7 胡旭宾 dept 18 → 4 且 lv8 → 6（广汇人事专员；广汇无人事部节点，暂挂公司级）
UPDATE system_users SET dept_id = 4, dept_level = 6, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 1051 AND dept_id = 18;

-- C8 贾世伟 lv6 → lv8（架构图已不含）
UPDATE system_users SET dept_level = 8, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 286 AND dept_level = 6;

-- ============================================================================
-- D. 江苏泰峰（调动 1 / 升 2 / 调级 1）
-- ============================================================================
-- D1 吴春鹏 lv5 → lv6（泰峰生产班长；dept 已是 25）
UPDATE system_users SET dept_level = 6, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 297 AND dept_level = 5;

-- D2 邹杰 dept 28 → 26 且 lv8 → 5（技术工程师兼质量负责人，挂质量部）
UPDATE system_users SET dept_id = 26, belong_dept = 26, dept_level = 5, modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 295 AND dept_id = 28;

-- 赵建星(293)、邓嘉君(299)、高荣幸(298)：部门与层级已与架构图一致，无需改动

-- ============================================================================
-- E. 上海智机（6 人全部 lv8 → lv5，子部门节点见 F2 可选项）
-- ============================================================================
UPDATE system_users SET dept_level = 5, modifier = 'Woker', update_datetime = NOW(6) WHERE id = 423  AND dept_level = 8;  -- 付磊建-机械主管
UPDATE system_users SET dept_level = 5, modifier = 'Woker', update_datetime = NOW(6) WHERE id = 421  AND dept_level = 8;  -- 赵伟伟-电气主管
UPDATE system_users SET dept_level = 5, belong_dept = 2, modifier = 'Woker', update_datetime = NOW(6) WHERE id = 169 AND dept_level = 8;  -- 苏杨-IT主管（belong_dept 15→2 修正）
UPDATE system_users SET dept_level = 5, modifier = 'Woker', update_datetime = NOW(6) WHERE id = 182  AND dept_level = 8;  -- 李强-AI主管
UPDATE system_users SET dept_level = 5, modifier = 'Woker', update_datetime = NOW(6) WHERE id = 1686 AND dept_level = 8;  -- 杨艳娇-人事行政专员
UPDATE system_users SET dept_level = 5, belong_dept = 2, modifier = 'Woker', update_datetime = NOW(6) WHERE id = 121 AND dept_level = 8;  -- 唐玉-财务主管（belong_dept 22→2 修正）

-- ============================================================================
-- F. 可选项处置（Simon 2026-08-02 已拍板）
-- ============================================================================
-- F1 ✅ 已批准：李雪峰兼管广汇工程部（dept 32），监管权限补充
UPDATE system_users SET regulatory_dept = JSON_ARRAY(4, 32), modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 13;

-- F4 ✅ 已批准：孙兴（id=576）regulatory_dept 脏数据清理 [null,4,20]→[4,20]
UPDATE system_users SET regulatory_dept = JSON_ARRAY(4, 20), modifier = 'Woker', update_datetime = NOW(6)
WHERE id = 576;

-- F2/F3 ⏸ 按建议不走 SQL，由 IT 在 fuadmin 后台建节点：
--   F2 智机子部门（机械/电气/IT/AI/总经办，挂 dept 2 下）→ 建成后 6 位主管再 UPDATE dept_id
--   F3 广汇人事部节点 → 建成后 UPDATE id=1051 的 dept_id
-- 注：Simon 版架构图不含孙兴管理岗 → 不升级，v1 的 4b/4c 作废

-- ============================================================================
-- G. 复核（提交前必跑）
-- ============================================================================
-- 预期: lv≤6 合计 40 人（lv1=1, lv2=1, lv3=1, lv4=7, lv5=15, lv6=15）
-- SELECT dept_level, COUNT(*) FROM system_users
-- WHERE is_delete=0 AND status=1 AND resignation_time IS NULL AND dept_level <= 6
-- GROUP BY dept_level ORDER BY dept_level;
--
-- 预期全名单 40 人：
-- lv1 郑希钦 (1) | lv2 郑敏 (1) | lv3 谭昌发 (1)
-- lv4 徐红雷/杨云祥/韩莹星/蔡汉东/石垒/李雪峰/曾华 (7)
-- lv5 孙明/潘利飞/赵菡/邱桂昊/牛周义/夏玉强/邹杰/邓嘉君/高荣幸/付磊建/赵伟伟/苏杨/李强/杨艳娇/唐玉 (15)
-- lv6 张迪/袁延志/赵飞/张双喜/林帅/孟永超/张仲华/张治民/陈建/王付毫/祝新斌/李丹洋/胡旭宾/吴春鹏/赵建星 (15)
-- SELECT u.dept_level, d.name AS dept, u.name FROM system_users u
-- LEFT JOIN system_dept d ON d.id = u.dept_id
-- WHERE u.is_delete=0 AND u.status=1 AND u.resignation_time IS NULL AND u.dept_level <= 6
-- ORDER BY u.dept_level, u.dept_id;

-- ============================================================================
-- 全部复核无误后，取消下行注释提交；有问题直接 ROLLBACK
-- ============================================================================
-- COMMIT;

-- ============================================================================
-- 回滚段（提交后如需撤销，按区执行）:
-- UPDATE system_users SET dept_level = 1 WHERE id = 291;
-- UPDATE system_users SET dept_level = 6 WHERE id = 24;
-- UPDATE system_users SET dept_level = 8 WHERE id = 478;
-- UPDATE system_users SET dept_level = 8, belong_dept = 10 WHERE id = 97;
-- UPDATE system_users SET dept_level = 8 WHERE id = 19;
-- UPDATE system_users SET dept_level = 5 WHERE id = 1152;
-- UPDATE system_users SET dept_level = 5 WHERE id = 730;
-- UPDATE system_users SET dept_level = 5 WHERE id = 21;
-- UPDATE system_users SET dept_level = 5 WHERE id = 1389;
-- UPDATE system_users SET dept_level = 8 WHERE id = 1401;
-- UPDATE system_users SET dept_id = 10, belong_dept = 10 WHERE id = 13;
-- UPDATE system_users SET dept_id = 3, belong_dept = 3 WHERE id = 195;
-- UPDATE system_users SET dept_id = 10, belong_dept = 10 WHERE id = 184;
-- UPDATE system_users SET dept_id = 10, belong_dept = 10, dept_level = 8 WHERE id = 36;
-- UPDATE system_users SET dept_id = 12, dept_level = 6 WHERE id = 118;
-- UPDATE system_users SET dept_id = 14, belong_dept = 22 WHERE id = 119;
-- UPDATE system_users SET dept_id = 18, dept_level = 8 WHERE id = 1051;
-- UPDATE system_users SET dept_level = 6 WHERE id = 286;
-- UPDATE system_users SET dept_level = 5 WHERE id = 297;
-- UPDATE system_users SET dept_id = 28, belong_dept = 28, dept_level = 8 WHERE id = 295;
-- UPDATE system_users SET dept_level = 8 WHERE id IN (423, 421, 182, 1686);
-- UPDATE system_users SET dept_level = 8, belong_dept = 15 WHERE id = 169;
-- UPDATE system_users SET dept_level = 8, belong_dept = 22 WHERE id = 121;
-- UPDATE system_users SET regulatory_dept = NULL WHERE id = 13;
-- UPDATE system_users SET regulatory_dept = JSON_ARRAY(NULL, 4, 20) WHERE id = 576;
-- ============================================================================
