---
title: 零散模块总览-fuadmin数据字典
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道, 索引]
---

# 零散模块总览 · fuadmin 数据字典
> 域: 06-其他定制 | 用途: 专机/外部/试验表导航 | 生成: 2026-07-23


# 06-其他定制 · 零散模块总览

本域共67张表，是"治通"主线五大域之外的定制开发集合，来源可分四类：一是专机项目数据落地（triangle_beam三角梁视觉检测、zj2315_e38英伟达边缘检验、lizhu缸盖专机计数、liqiang物流日报，多以项目/人名命名）；二是外部设备对接（external_data_d/jzt/ym，带 _MASK_TO_V2/_MUSID_SYNC_V2/_MASK_FROM_V2 同步标记列）；三是试验性与脚手架功能（demo、generator_test*、go_view*、track_*与tracking_*系列均为0行未启用）；四是未归入五域的零散实质业务（刀具全生命周期、质量检验、5S现场、安全点检、罚单协作、能耗与报警）。绝大多数表继承 generator_* 通用审计字段，creator_id 逻辑指向 system_users。处理建议：专机与外部大表按只读数据源治理、勿改结构；0行测试/跟踪框架表可归档；刀具、质检、现场安全等实质业务建议未来按归属域重组，本文件仅作过渡性总览。


# 06-其他定制 · 零散模块上岗指南

按语义分16组。每表一行：表名 | 推断业务语义 | 建议归属域 | 关键字段说明。行数为骨架统计。

## A. 专机项目数据（只读数据源，勿改结构）

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_triangle_beam_monitoring_system (~14210) | 三角梁专机视觉检测主记录：按二维码逐件记录总耗时+30个检测区域的结果/耗时 | 质量技术域 | qr_codee=工件二维码；area_result_N/area_time_N=第N区域结果与耗时；样本：user_name=黄明飞、project_name=三角梁、area_result=未检测；result/concentration 为汇总判定；source_addr=边缘设备原始图路径 |
| generator_triangle_beam_count_data (~246) | 三角梁检测计数台账 | 质量技术域 | check_count=当次检测数量；datetime=检测时间；与上表同时段生成（样本2025-08-28） |
| zj2315_e38_data (~46996) | ZJ2315-E38专机检验数据：加工/测量各刀位耗时与浓度 | 质量技术域 | USER_NAME/PROJECT_NAME/QR_CODEE（样本：朱海燕/E28A/No_001）；TOTALT_TIME总时长；POSITIVE/SIDE/UNDERSIDE/INNER_30/INNER_18/SMALL_45/LARGE_45/OUTER_116 各刀位时间；SOURCE_ADDR=/media/nvidia/... 表明来自英伟达边缘盒；THREADED_HOLE_COUNT/PIN_HOLE_COUNT 孔计数 |
| zj2315_e38_inspection_data (0) | E38检验记录表，未启用 | 可归档 | 仅 USER_NAME+CREATE_DATE |
| zj2315_e38_threaded_hole (0) | E38螺纹孔/销孔计数，未启用 | 可归档 | TIME_STAMP 唯一 |
| generator_lizhu_count_data (~457) | 缸盖GS61/GS62左右型号计数（lizhu专机） | 生产铸造域 | left/right_gs61(h)/gs62(h) 八列分型计数 |
| generator_lizhu_error_data (~251) | 换刀错误记录：应装刀型vs实装刀型 | 生产铸造域 | model_tool_type 应装、curr_tool_type 实装、direction 方位、image 照片 |
| generator_lizhu_robot_data (~171244) | 机器人刀型状态流水（17万行高频） | 生产铸造域 | tool_type/state/direction/create_date |
| generator_liqiang_inventory (~40) | 产品库存盘点（liqiang项目） | 供应链域 | summary_total/logistics_balance/difference 结存差异 |
| generator_liqiang_logistics_cost (~50) | 物流成本月度台账 | 供应链域 | date 格式YYYY-MM；unit_cost/target_unit_cost/standard_cost/completion_rate |
| generator_liqiang_report_journals (~10777) | 微信端日报汇报记录 | 人事系统域 | today_content/tomorrow_content；submitter_userid/receivers_userids/readed_receivers_userids 为微信用户ID串 |

## B. 外部设备对接（同步落库，只读）

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| external_data_d (~901) | 外部测量机D数据：56列测量值+判定 | 质量技术域 | data01-56 浮点字符串；result=合格/不合格；title1=预（预检？待确认）；qr_code 工件码；_MASK_TO_V2/_MUSID_SYNC_V2/_MASK_FROM_V2 为V2系统双向同步标记 |
| external_data_jzt (~6429) | 精测台（JZT）测量数据：44列 | 质量技术域 | data01-44；result=合格；title1=精；样本 qr_code=240225BPS10559 |
| external_data_ym (~37205) | 压铆/压装机数据 | 生产铸造域 | set_pressure 设定压力、pressure_val 实测压力、variety/type 型号分类；样本 set_pressure=160 |

## C. 刀具全生命周期（实质业务，数据量大）

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_eng_tool_knives (~15947) | 刀具档案：刀柜/层位/型号/供应商/条码 | 生产铸造域 | bar_code 唯一条码（样本DA0561008）；cabinet_number+number_of_layers 定位；knife_leader 刀具班长；model 完整型号（如D20 PCD面铣刀） |
| generator_machine_tool_change (~26984) | 机台换刀记录：旧刀→新刀 | 生产铸造域 | machine_tool 机台号（Z-J-059）、production_line_id 产线（DCTeco-OP30-2）、old/new 供应商与条码、change_reason=磨损、working_shift 班次、status=已完成 |
| generator_take_tool (~44384) | 领刀记录 | 生产铸造域 | tool_borrower 领用人、cabinet_id 刀柜、bar_code |
| generator_old_knife_recycle (~9362) | 旧刀回收登记 | 生产铸造域 | admin 回收经手人、layer_number/cabinet_number |
| knife_jobcode (~389) | 刀具与工序关联 | 生产铸造域 | job_code_id→generator_job_code；is_auto 是否自动换刀；internal_code |
| generator_abnormal_tool_filtering_data (~18484) | 异常刀具筛选推送记录 | 生产铸造域 | barcode、pushed_exception_item 异常项、is_resolved 是否处理、push_datetime |
| generator_daily_tool_summary (0) | 刀具日汇总，未启用 | 可归档 | model/bar_code/date_time |

## D. 质量检验（实质业务）

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_quality_inspection (~158130) | 质量巡检/扫码检验主记录（15.8万行，全域最大） | 质量技术域 | code=工件/批次码（样本Z-C-016）、inspector 检验员（工号+姓名）、type、img JSON照片、associated_infor |
| generator_cmm_inspection_log (~37743) | 三坐标测量日志 | 质量技术域 | is_first_article 是否首件、first_article_reason；mold_no/production_line_no/qr_code；temperature 环境温度；result/status |
| generator_qualityrapid_response (~189) | 质量快速响应单（QRQC） | 质量技术域 | exception_issue 异常描述、CauseAnalysisTable 原因分析、Temporary/PermanentMeasuresTable 临时/永久措施JSON、is_end 关闭标记 |
| generator_defective_product (~2069) | 不良品登记 | 质量技术域 | product/quantity/reason/discoverer/discovery_method/responsible_person/type |
| generator_rework_record_header (~1641) | 返工单头（编号YC+日期+流水） | 质量技术域 | rework_number（样本YC202505220002）、line_name、unqualified_content、approval_process/coordinator JSON审批流、phase 阶段、repair_deadline |
| extraneous_product_qrcode (~35082) | 返工/异常产品二维码明细 | 质量技术域 | old_product_code→new_product_code 换码；rework_record_header_id→返工单；rework_defects JSON；operate_state/phase |
| generator_objective (~6) | 检验对象定义（5S/质量共用字典？待确认） | 质量技术域 | inspection_object longtext |

## E. 现场5S与安全

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_safety_inspection (~9098) | 安全点检记录 | 人事系统域(行政/EHS) | dot 点位（配电房）、area 区域（上海治通门卫室）、error 异常类型、code 点位码、img/cc JSON；样本 inspector=22538 韩莹星 |
| generator_site_management (~323) | 5S现场问题整改单（编号5SXJ+流水） | 人事系统域(行政/5S) | inspection_ticket_number（样本5SXJ202407110023）、problem_image/photo_rectification 整改前后照片、inspection_states=待整改/已确认、region_id→区域、classification_5_s_id→5S分类、responsible_person_id/inspector_id→system_users |
| generator_definition_five_s (~9) | 5S项目定义（整理整顿清扫清洁素养） | 人事系统域(行政/5S) | project_5s/objective/implementation_benefits/activity_object |
| generator_management_area_allocation (~28) | 现场区域责任划分 | 人事系统域(行政/5S) | region 区域描述、regional_plan 区域图、responsible_person_id/responsible_department_id |

## F. 报警与能耗

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_alarm_records (~3) | 设备报警记录 | 生产铸造域 | type=温度异常/设备故障、priority=中/高、push_status=未发送/已发送、device_id→generator_devices、date_time 报警时刻；样本：设备温度过高、主轴过载 |
| generator_total_power (~738910) | 总电表分钟级能耗采集（73.9万行，全库最大时序表） | 生产铸造域(能管) | active_power 有功功率、accumulated_electricity_consumption 累计电量、minute_electricity_consumption 分钟电量、time 分钟级时间戳 |

## G. 工单·协作·奖惩

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_ticket (~1578) | 奖惩/问题工单（编号JFDH+流水） | 人事系统域 | ticket_type、name/describe/info/measure/handle_feedback 五段叙述、signature 签名JSON、is_audit/is_end、work_order/tracking_card/job_code 关联生产 |
| generator_users_ticket (~3071) | 人员罚单关联（一罚单罚多人） | 人事系统域 | ticket_id→generator_ticket、users_id→system_users、punishment_method=处罚金额、sum 金额、i_agree 本人确认；样本：各罚50元 |
| generator_cooperation (~256) | 跨部门协作单 | 人事系统域 | type/priority/target、support_staff/cc_send/purchase/message JSON、state |
| generator_commentsmessage (~188) | 站内评论消息 | 人事系统域 | senderId/senderName→receiverId/receiverName、parentId 楼层、odd_numbers 关联单号 |
| generator_inform (~8) | 通知提醒（证书到期等），已迁出至05人事域，此处仅登记 | 人事系统域 | remind_user/remind_method/remind_state JSON、start/end_time |

## H. 生产基础数据（工序/路线）

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_job_code (~1379) | 工序代码树（计件工资基准） | 生产铸造域 | name 唯一（机加-差壳-DCT300）、parent_id 自关联、piecework_price 计件单价、settlement_method 结算方式、contribution_ratio、is_production |
| generator_job_code_product (~1715) | 工序-产品多对多桥 | 生产铸造域 | jobcode_id+product_id 唯一联合 |
| generator_jobcode_devices (~68) | 工序-设备桥 | 生产铸造域 | devices_id→generator_devices、job_code_id→generator_job_code |
| generator_public_data (~30) | 公共参数数据 | 人事系统域 | name/value/date 简单键值 |
| generator_process_inventory (0) | 工序在制品，未启用 | 可归档 | product_id+station_id 唯一 |
| track_route (0) | 跟踪路线定义，新框架未启用 | 可归档 | route_name/product_category |
| track_route_step (0) | 路线步骤，未启用 | 可归档 | route_id→track_route、station_id→track_station、step_no |
| track_station (0) | 跟踪工位，未启用 | 可归档 | station_name/station_type |
| track_station_job_code_map (0) | 工位-工序映射，未启用 | 可归档 | station_id+job_code_id 唯一 |
| generator_tracking_transfer (0) | 工序转移记录，未启用 | 可归档 | tracking_id→generator_production_tracking、from/to_station_id、input/output/三类废料 |
| generator_tracking_waste_record (0) | 转移废料记录，未启用 | 可归档 | tracking_id/transfer_id 双FK |

## I. 仓储物流

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_box_code_verify (~9071) | 箱码校验与客户箱码绑定 | 供应链域 | box_code/product_qr、ai_state/p_state AI与人工校验态、customer_box_code_bind_time/binder |
| generator_customer_order (~2361) | 客户订单登记 | 订单项目域 | customer_order_number/customer_name/product_name/count/box_number/order_state |
| generator_ingredients_split (~1849) | 辅料拆分出入库 | 供应链域 | ingredients_id、stock JSON、in_warehouse/stock/send 三段人时记录、bar_code |
| generator_registration_qrcode (~7) | 注册二维码 | 供应链域 | qrcode/box_code/type/state |
| generator_exception_qrcode (~15) | 异常二维码登记 | 质量技术域 | qrcode/type |

## J. 人事辅助

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| generator_employment_registration (~249) | 入职登记（含身份证/学历/家庭/工作经历） | 人事系统域 | id_number 身份证18位、family_information/work_experience JSON、state 审批态；敏感个人信息注意脱敏 |
| generator_holiday_date (~65) | 节假日定义 | 人事系统域 | date_time 唯一、holiday_name、settle_rule 结算规则 |
| generator_authorization (~78) | 授权码（扫码/外部授权凭证） | 人事系统域 | code+userinfo（工号 姓名）、work_dept JSON、is_active；亦见05域 |

## K. 试验/脚手架（可归档）

| 表名 | 推断业务语义 | 建议归属域 | 关键字段说明 |
|---|---|---|---|
| demo (0) | 代码生成器演示表 | 可归档 | name/code/status 三示例列 |
| generator_test (0) | 测试表 | 可归档 | sequence decimal(13,4) 排序试验 |
| generator_test_demo (0) | 测试演示表 | 可归档 | des/code/name |
| go_view_data (0) | 数据大屏内容试验 | 可归档 | content longtext |
| go_view_project (0) | 大屏项目试验 | 可归档 | project_name/index_image/content |

> 说明：generator_inform / generator_users_ticket / generator_authorization 三表同时出现在05-人事系统域 skeleton 与本域，归属以05域为准，此处仅保留交叉登记。

## 相关页面
- [[answer-定制模块-fuadmin数据字典]]
- [[fuadmin数据字典总览]]
- [[liqiang-定制模块-fuadmin数据字典]]
- [[lizhu-定制模块-fuadmin数据字典]]
- [[misc-alarm模块-fuadmin数据字典]]
- [[misc-commentsmessage模块-fuadmin数据字典]]
- [[misc-cooperation模块-fuadmin数据字典]]
- [[misc-definition模块-fuadmin数据字典]]
- [[misc-demo模块-fuadmin数据字典]]
- [[misc-external模块-fuadmin数据字典]]
- [[misc-go模块-fuadmin数据字典]]
- [[misc-management模块-fuadmin数据字典]]
- [[misc-objective模块-fuadmin数据字典]]
- [[misc-public模块-fuadmin数据字典]]
- [[misc-safety模块-fuadmin数据字典]]
- [[misc-site模块-fuadmin数据字典]]
- [[misc-ticket模块-fuadmin数据字典]]
- [[misc-total模块-fuadmin数据字典]]
- [[misc-triangle模块-fuadmin数据字典]]
- [[misc-zj2315模块-fuadmin数据字典]]
- [[test-定制模块-fuadmin数据字典]]
