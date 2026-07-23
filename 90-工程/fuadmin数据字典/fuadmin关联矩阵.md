---
title: fuadmin关联矩阵
created: 2026-07-23
updated: 2026-07-23
type: reference
domain: 工程
tags: [工程, 数据管道]
---

# fuadmin 全局关联矩阵

- 关联总数（去重后）: 288
- 跨模块关联: 146
- 跨模块边: 63

| 源模块.表.字段 | → | 目标模块.表.字段 | 依据 | 置信度 | 说明 |
|---|---|---|---|---|---|
| att-考勤打卡.att_transaction.employee_code | → | system-用户权限.system_users.username | fk | mid | att-考勤打卡接口 |
| att-考勤打卡.att_transaction.employee_code | → | hr-人力能力.generator_roster.employee_id | naming | mid | att-考勤打卡接口 |
| att-考勤打卡.att_transaction.dept_name | → | system-用户权限.system_dept.name | fk | mid | att-考勤打卡接口 |
| bad-不良品.generator_rework_record_header.id | → | qrcode-二维码追溯.extraneous_product_qrcode.rework_record_header_id | fk | high | bad-不良品接口 |
| bad-不良品.generator_bad_product.ticket_id | → | system-用户权限.generator_users_ticket.id | naming | mid | 字段名惯例推断 |
| dailyreport-日报任务.generator_dailytask.project_id | → | misc-go.go_view_project.id | naming | mid | 字段名惯例推断 |
| dailyreport-日报任务.generator_monthlytask.project_id | → | misc-go.go_view_project.id | naming | mid | 字段名惯例推断 |
| dailyreport-日报任务.generator_dailyreport.creator_id | → | system-用户权限.system_users.id | naming | mid | dailyreport-日报任务接口 |
| dailyreport-日报任务.generator_dailytask.creator_id | → | system-用户权限.system_users.id | naming | mid | dailyreport-日报任务接口 |
| dailyreport-日报任务.generator_monthlytask.creator_id | → | system-用户权限.system_users.id | naming | mid | dailyreport-日报任务接口 |
| device-设备装置.generator_devices.type_id | → | inspection-质量检验.generator_inspection_standards.id | fk | high | InnoDB硬外键 |
| device-设备装置.generator_devices.id | → | equipment-设备.generator_equipment_repair.device_id | naming | high | device-设备装置接口 |
| device-设备装置.generator_devices.id | → | equipment-设备.generator_equipment_inspection.inspection_equipment_id | naming | high | device-设备装置接口 |
| device-设备装置.generator_devices.id | → | equipment-设备.generator_equipment_maintenance_records.equipment_id | naming | high | device-设备装置接口 |
| device-设备装置.generator_devices.type_id | → | django-auth框架.django_content_type.id | naming | mid | 字段名惯例推断 |
| device-设备装置.generator_devices.dept_id | → | system-用户权限.system_dept.id | naming | mid | 字段名惯例推断 |
| device-设备装置.generator_devices.internal_code | → | newscheduling-新排程.generator_newscheduling.device_code | naming | mid | device-设备装置接口 |
| django-auth框架.django_admin_log.user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| django-auth框架.auth_group_permissions.group_id | → | system-用户权限.system_users_groups.id | naming | mid | 字段名惯例推断 |
| django-auth框架.auth_group_permissions.permission_id | → | system-用户权限.system_role_permission.id | naming | mid | 字段名惯例推断 |
| django-auth框架.django_celery_results_chordcounter.group_id | → | system-用户权限.system_users_groups.id | naming | mid | 字段名惯例推断 |
| django-auth框架.django_celery_results_groupresult.group_id | → | system-用户权限.system_users_groups.id | naming | mid | 字段名惯例推断 |
| equipment-设备.generator_equipment_inspection.inspection_standards_id | → | inspection-质量检验.generator_inspection_standards.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_repair.device_id | → | device-设备装置.generator_devices.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_repair_report_cc_personnel.users_id | → | system-用户权限.system_users.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_inspection.inspection_equipment_id | → | device-设备装置.generator_devices.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_inspection.inspection_personnel_id | → | system-用户权限.system_users.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_maintenance_records.equipment_id | → | device-设备装置.generator_devices.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_maintenance_records.operator_id | → | system-用户权限.system_users.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_repair.repair_applicant_id | → | system-用户权限.system_users.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_repair.direct_writer_id | → | system-用户权限.system_users.id | naming | high | equipment-设备接口 |
| equipment-设备.generator_equipment_repair_report.equipment_id | → | device-设备装置.generator_devices.id | naming | high | equipment-设备接口 |
| fixture-工装夹具.generator_fixtures.device_id | → | device-设备装置.generator_devices.id | naming | mid | 字段名惯例推断 |
| hr-人力能力.generator_historicaljobcode.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| hr-人力能力.generator_historicaljobcode_devices.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| hr-人力能力.generator_salary.newscheduling_id | → | newscheduling-新排程.generator_newscheduling.id | sample | high | hr-人力能力接口 |
| hr-人力能力.generator_jobcode_devices.devices_id | → | device-设备装置.generator_devices.id | fk | high | InnoDB硬外键 |
| hr-人力能力.generator_historicaljobcode_devices.devices_id | → | device-设备装置.generator_devices.id | naming | mid | 字段名惯例推断 |
| hr-人力能力.generator_job_code_product.jobcode_id | → | knife-刀具.knife_jobcode.id | naming | mid | 字段名惯例推断 |
| hr-人力能力.generator_job_code_product.product_id | → | bad-不良品.generator_bad_product.id | naming | mid | 字段名惯例推断 |
| hr-人力能力.generator_capability_score.user_code | → | system-用户权限.system_users.username | fk | mid | hr-人力能力接口 |
| hr-人力能力.generator_roster.employee_id | → | system-用户权限.system_users.username | fk | mid | hr-人力能力接口 |
| knife-刀具.generator_knife_life_standards.production_line_id | → | production-生产.generator_production_line.id | naming | mid | 字段名惯例推断 |
| knife-刀具.generator_knife_life_standards_copy1.production_line_id | → | production-生产.generator_production_line.id | naming | mid | 字段名惯例推断 |
| knife-刀具.knife_jobcode.job_code_id | → | hr-人力能力.generator_job_code.id | naming | mid | 字段名惯例推断 |
| knife-刀具.generator_machine_tool_change.production_line_id | → | production-生产.generator_production_line.id | naming | mid | 字段名惯例推断 |
| logistics-物流.generator_logistics_detail_map.order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| maintenance-维修保养.generator_maintenance_records.device_id | → | device-设备装置.generator_devices.id | naming | high | maintenance-维修保养接口 |
| maintenance-维修保养.generator_maintenance_schedule.device_id | → | device-设备装置.generator_devices.id | naming | high | maintenance-维修保养接口 |
| maintenance-维修保养.generator_maintenance_records.creator_id | → | system-用户权限.system_users.id | naming | high | maintenance-维修保养接口 |
| misc-alarm.generator_alarm_records.device_id | → | device-设备装置.generator_devices.id | fk | mid | 零散模块总览接口 |
| misc-site.generator_site_management.region_id | → | misc-management.generator_management_area_allocation.id | fk | mid | 零散模块总览接口 |
| misc-site.generator_site_management.classification_5_s_id | → | misc-definition.generator_definition_five_s.id | fk | mid | 零散模块总览接口 |
| newscheduling-新排程.generator_newscheduling.id | → | hr-人力能力.generator_salary.newscheduling_id | sample | high | newscheduling-新排程接口 |
| newscheduling-新排程.generator_newscheduling.creator_id | → | system-用户权限.system_users.id | naming | high | newscheduling-新排程接口 |
| newscheduling-新排程.generator_newscheduling.device_code | → | device-设备装置.generator_devices.internal_code | naming | mid | newscheduling-新排程接口 |
| order-订单.generator_order_detail_document_mapping.document_id | → | purchase-采购.generator_purchase_order_document.id | naming | mid | 字段名惯例推断 |
| order-订单.generator_order_detail_document_mapping.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| order-订单.generator_order_detail_document_mapping_gh.document_id | → | purchase-采购.generator_purchase_order_document.id | naming | mid | 字段名惯例推断 |
| order-订单.generator_order_detail_document_mapping_gh.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| order-订单.generator_order_detail_document_mapping_tf.document_id | → | purchase-采购.generator_purchase_order_document.id | naming | mid | 字段名惯例推断 |
| order-订单.generator_order_detail_document_mapping_tf.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| order-订单.generator_order_detail_document_mapping_zt.document_id | → | purchase-采购.generator_purchase_order_document.id | naming | mid | 字段名惯例推断 |
| order-订单.generator_order_detail_document_mapping_zt.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application.purchase_order_id | → | purchase-采购.generator_purchase_order.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application.settlement_bill_id | → | settlement-结算.generator_settlement_bill.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application_gh.purchase_order_id | → | purchase-采购.generator_purchase_order.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application_gh.settlement_bill_id | → | settlement-结算.generator_settlement_bill.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application_tf.purchase_order_id | → | purchase-采购.generator_purchase_order.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application_tf.settlement_bill_id | → | settlement-结算.generator_settlement_bill.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application_zt.purchase_order_id | → | purchase-采购.generator_purchase_order.id | naming | mid | 字段名惯例推断 |
| payment-付款.generator_payment_application_zt.settlement_bill_id | → | settlement-结算.generator_settlement_bill.id | naming | mid | 字段名惯例推断 |
| plan-生产计划.generator_plan_delivery_plan.customer_order_id | → | order-订单.generator_customer_order.id | naming | mid | 字段名惯例推断 |
| plan-生产计划.generator_scheduling.code_id | → | hr-人力能力.generator_job_code.id | naming | mid | 字段名惯例推断 |
| plan-生产计划.generator_scheduling.production_line_id | → | production-生产.generator_production_line.id | naming | mid | 字段名惯例推断 |
| process-工艺技术.generator_jgdm.creator_id | → | system-用户权限.system_users.id | naming | high | process-工艺技术接口 |
| process-工艺技术.generator_process_inventory.product_id | → | bad-不良品.generator_bad_product.id | naming | mid | 字段名惯例推断 |
| process-工艺技术.generator_process_inventory.station_id | → | qrcode-二维码追溯.track_station.id | naming | mid | 字段名惯例推断 |
| process-工艺技术.generator_process_inventory.product_id | → | product-产品.generator_product.id | naming | mid | process-工艺技术接口 |
| product-产品.generator_product_plm_rufa.qrcode_in_id | → | qrcode-二维码追溯.generator_qrcode_in.id | naming | mid | 字段名惯例推断 |
| product-产品.generator_product_plm_rufa.qrcode_out_id | → | qrcode-二维码追溯.generator_qrcode_out.id | naming | mid | 字段名惯例推断 |
| production-生产.generator_production_tracking.product_id | → | bad-不良品.generator_bad_product.id | naming | mid | 字段名惯例推断 |
| production-生产.generator_production_tracking.route_id | → | qrcode-二维码追溯.track_route.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_attendance.user_id | → | system-用户权限.system_users.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_copy1.purchase_order_id | → | purchase-采购.generator_purchase_order.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_copy1.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_gh.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_gh.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_tf.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_tf.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_zt.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| project-项目.generator_project_material_summary_detail_zt.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| purchase-采购.generator_historicalpurchaseorder.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaseorderdetail.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaseorderdetailgh.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaseorderdetailtf.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaseorderdetailzt.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaseordergh.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaseordertf.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaseorderzt.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisition.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisitiondetail.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisitiondetailgh.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisitiondetailtf.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisitiondetailzt.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisitiongh.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisitiontf.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| purchase-采购.generator_historicalpurchaserequisitionzt.history_user_id | → | system-用户权限.system_users.id | fk | high | InnoDB硬外键 |
| qrcode-二维码追溯.generator_qrcode_sendout.customer_order_id | → | order-订单.generator_customer_order.id | fk | high | qrcode-二维码追溯接口 |
| qrcode-二维码追溯.extraneous_product_qrcode.rework_record_header_id | → | bad-不良品.generator_rework_record_header.id | fk | high | qrcode-二维码追溯接口 |
| qrcode-二维码追溯.generator_tracking_transfer.device_id | → | device-设备装置.generator_devices.id | fk | high | InnoDB硬外键 |
| qrcode-二维码追溯.generator_tracking_transfer.tracking_id | → | production-生产.generator_production_tracking.id | fk | high | InnoDB硬外键 |
| qrcode-二维码追溯.generator_tracking_waste_record.tracking_id | → | production-生产.generator_production_tracking.id | fk | high | InnoDB硬外键 |
| qrcode-二维码追溯.track_station_job_code_map.job_code_id | → | hr-人力能力.generator_job_code.id | fk | mid | qrcode-二维码追溯接口 |
| settlement-结算.generator_settlement_bill_detail.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| settlement-结算.generator_settlement_bill_detail_gh.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| settlement-结算.generator_settlement_bill_detail_tf.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| settlement-结算.generator_settlement_bill_detail_zt.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| settlement-结算.generator_settlement_payment_allocation.payment_record_id | → | payment-付款.generator_payment_record.id | naming | mid | 字段名惯例推断 |
| settlement-结算.generator_settlement_payment_allocation_gh.payment_record_id | → | payment-付款.generator_payment_record.id | naming | mid | 字段名惯例推断 |
| settlement-结算.generator_settlement_payment_allocation_tf.payment_record_id | → | payment-付款.generator_payment_record.id | naming | mid | 字段名惯例推断 |
| settlement-结算.generator_settlement_payment_allocation_zt.payment_record_id | → | payment-付款.generator_payment_record.id | naming | mid | 字段名惯例推断 |
| shift-班次.generator_shift_schedule.creator_id | → | system-用户权限.system_users.id | naming | high | shift-班次接口 |
| supplier-供应商.generator_supplier_material_mapping.purchase_material_id | → | purchase-采购.generator_purchase_material.id | naming | mid | 字段名惯例推断 |
| supplier-供应商.generator_supplier_material_mapping_gh.purchase_material_id | → | purchase-采购.generator_purchase_material.id | naming | mid | 字段名惯例推断 |
| supplier-供应商.generator_supplier_material_mapping_tf.purchase_material_id | → | purchase-采购.generator_purchase_material.id | naming | mid | 字段名惯例推断 |
| supplier-供应商.generator_supplier_material_mapping_zt.purchase_material_id | → | purchase-采购.generator_purchase_material.id | naming | mid | 字段名惯例推断 |
| system-用户权限.system_users_groups.group_id | → | django-auth框架.auth_group.id | fk | high | InnoDB硬外键 |
| system-用户权限.system_users_user_permissions.permission_id | → | django-auth框架.auth_permission.id | fk | high | InnoDB硬外键 |
| system-用户权限.system_product_szb.product_id | → | bad-不良品.generator_bad_product.id | naming | mid | 字段名惯例推断 |
| system-用户权限.system_users.id | → | django-auth框架.django_admin_log.user_id | naming | mid | system-用户权限接口 |
| system-用户权限.generator_users_ticket.ticket_id | → | misc-ticket.generator_ticket.id | naming | mid | system-用户权限接口 |
| tf-TF铸造.generator_tf_mould_scanreport.code_id | → | hr-人力能力.generator_job_code.id | naming | mid | 字段名惯例推断 |
| tool-工具工装.generator_tool_replacement.production_line_id | → | production-生产.generator_production_line.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_copy1.purchase_order_id | → | purchase-采购.generator_purchase_order.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_copy1.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_gh.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_gh.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_tf.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_tf.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_zt.purchase_requisition_detail_id | → | purchase-采购.generator_purchase_requisition_detail.id | naming | mid | 字段名惯例推断 |
| warehouse-仓储.generator_warehouse_transaction_detail_zt.purchase_order_detail_id | → | purchase-采购.generator_purchase_order_detail.id | naming | mid | 字段名惯例推断 |

## 相关页面
- [[fuadmin数据字典总览]]
