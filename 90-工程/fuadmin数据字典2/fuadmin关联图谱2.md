---
title: fuadmin关联图谱2
created: 2026-07-24
type: reference
tags: [工程, 数据字典2, 关联图谱]
---

# fuadmin 关联图谱2（代码实证版）
> 代码级关系 244 条 ｜ 推断补充 79 条

## 结构关系

- 📸 `generator_historicaljobcode` ← 快照自 `JobCode`
- 📸 `generator_historicaljobcode_devices` ← 快照自 `JobCode_Devices`
- 📸 `generator_historicalpurchaseorder` ← 快照自 `PurchaseOrder`
- 📸 `generator_historicalpurchaseorderdetail` ← 快照自 `PurchaseOrderDetail`
- 📸 `generator_historicalpurchaseorderdetailgh` ← 快照自 `PurchaseOrderDetailGH`
- 📸 `generator_historicalpurchaseorderdetailtf` ← 快照自 `PurchaseOrderDetailTF`
- 📸 `generator_historicalpurchaseorderdetailzt` ← 快照自 `PurchaseOrderDetailZT`
- 📸 `generator_historicalpurchaseordergh` ← 快照自 `PurchaseOrderGH`
- 📸 `generator_historicalpurchaseordertf` ← 快照自 `PurchaseOrderTF`
- 📸 `generator_historicalpurchaseorderzt` ← 快照自 `PurchaseOrderZT`
- 📸 `generator_historicalpurchaserequisition` ← 快照自 `PurchaseRequisition`
- 📸 `generator_historicalpurchaserequisitiondetail` ← 快照自 `PurchaseRequisitionDetail`
- 📸 `generator_historicalpurchaserequisitiondetailgh` ← 快照自 `PurchaseRequisitionDetailGH`
- 📸 `generator_historicalpurchaserequisitiondetailtf` ← 快照自 `PurchaseRequisitionDetailTF`
- 📸 `generator_historicalpurchaserequisitiondetailzt` ← 快照自 `PurchaseRequisitionDetailZT`
- 📸 `generator_historicalpurchaserequisitiongh` ← 快照自 `PurchaseRequisitionGH`
- 📸 `generator_historicalpurchaserequisitiontf` ← 快照自 `PurchaseRequisitionTF`
- 📸 `generator_historicalpurchaserequisitionzt` ← 快照自 `PurchaseRequisitionZT`
- 🏭 `generator_knife_life_standards_copy1` ← 复制自 `generator_knife_life_standards`
- 🏭 `generator_logistics_product_stock_copy1` ← 复制自 `generator_logistics_product_stock`
- 🏭 `generator_logistics_transaction_table_copy1` ← 复制自 `generator_logistics_transaction_table`
- 🏭 `generator_logistics_waybill_copy1` ← 复制自 `generator_logistics_waybill`
- 🏭 `generator_project_material_summary_detail_copy1` ← 复制自 `generator_project_material_summary_detail`
- 🏭 `generator_purchase_order_copy1` ← 复制自 `generator_purchase_order`
- 🏭 `generator_purchase_order_detail_copy1` ← 复制自 `generator_purchase_order_detail`
- 🏭 `generator_purchase_order_document_copy1` ← 复制自 `generator_purchase_order_document`
- 🏭 `generator_warehouse_transaction_detail_copy1` ← 复制自 `generator_warehouse_transaction_detail`

## 代码级外键/M2M（from → to）
| 从表.字段 | 到表 | 依据 |
|---|---|---|
| `extraneous_product_qrcode.creator_id` | `settings.AUTH_USER_MODEL` | code_fk |
| `extraneous_product_qrcode.rework_record_header_id` | `generator_rework_record_header` | code_fk |
| `generator_alarm_records.device_id` | `generator_devices` | code_fk |
| `generator_bad_product.ticket_id` | `generator_ticket` | code_fk |
| `generator_bad_product_record.bad_product_id` | `generator_bad_product` | code_fk |
| `generator_calibration_record.instrument_id` | `generator_measuring_instrument` | code_fk |
| `generator_device_cutting_fluid_check.inspector_id` | `system_users` | code_fk |
| `generator_device_eff.device_id` | `generator_devices` | code_fk |
| `generator_devices.type_id` | `generator_inspection_standards` | code_fk |
| `generator_devices.dept_id` | `system_dept` | code_fk |
| `generator_devices_log.device_id` | `generator_devices` | code_fk |
| `generator_equipment_inspection.inspection_equipment_id` | `generator_devices` | code_fk |
| `generator_equipment_inspection.inspection_personnel_id` | `system_users` | code_fk |
| `generator_equipment_inspection.inspection_standards_id` | `generator_inspection_standards` | code_fk |
| `generator_equipment_maintenance_records.operator_id` | `system_users` | code_fk |
| `generator_equipment_maintenance_records.equipment_id` | `generator_devices` | code_fk |
| `generator_equipment_repair.device_id` | `generator_devices` | code_fk |
| `generator_equipment_repair.direct_writer_id` | `system_users` | code_fk |
| `generator_equipment_repair.repair_applicant_id` | `system_users` | code_fk |
| `generator_equipment_repair_report.maintenance_personnel_id` | `system_users` | code_fk |
| `generator_equipment_repair_report.equipment_id` | `generator_devices` | code_fk |
| `generator_equipment_repair_report.repair_applicant_id` | `system_users` | code_fk |
| `generator_equipment_repair_report.quality_id` | `system_users` | code_fk |
| `generator_equipment_repair_report_cc_personnel.users_id` | `system_users` | code_m2m |
| `generator_fixture_maintenance_rc.fixture_id` | `generator_fixtures` | code_fk |
| `generator_fixture_usage_rc.fixture_id` | `generator_fixtures` | code_fk |
| `generator_fixtures.device_id` | `generator_devices` | code_fk |
| `generator_historicaljobcode.parent_id` | `generator_job_code` | code_fk |
| `generator_historicaljobcode_devices.devices_id` | `generator_devices` | code_fk |
| `generator_historicaljobcode_devices.job_code_id` | `generator_job_code` | code_fk |
| `generator_historicalpurchaseorderdetail.purchase_order_id` | `generator_purchase_order` | code_fk |
| `generator_historicalpurchaseorderdetail.purchase_requisition_id` | `generator_purchase_requisition` | code_fk |
| `generator_historicalpurchaseorderdetail.supplier_material_map_id` | `generator_supplier_material_mapping` | code_fk |
| `generator_historicalpurchaseorderdetailgh.purchase_order_id` | `generator_purchase_order_gh` | code_fk |
| `generator_historicalpurchaseorderdetailgh.purchase_requisition_id` | `generator_purchase_requisition_gh` | code_fk |
| `generator_historicalpurchaseorderdetailgh.supplier_material_map_id` | `generator_supplier_material_mapping_gh` | code_fk |
| `generator_historicalpurchaseorderdetailtf.purchase_order_id` | `generator_purchase_order_tf` | code_fk |
| `generator_historicalpurchaseorderdetailtf.purchase_requisition_id` | `generator_purchase_requisition_tf` | code_fk |
| `generator_historicalpurchaseorderdetailtf.supplier_material_map_id` | `generator_supplier_material_mapping_tf` | code_fk |
| `generator_historicalpurchaseorderdetailzt.purchase_order_id` | `generator_purchase_order_zt` | code_fk |
| `generator_historicalpurchaseorderdetailzt.purchase_requisition_id` | `generator_purchase_requisition_zt` | code_fk |
| `generator_historicalpurchaseorderdetailzt.supplier_material_map_id` | `generator_supplier_material_mapping_zt` | code_fk |
| `generator_historicalpurchaserequisitiondetail.purchase_requisition_id` | `generator_purchase_requisition` | code_fk |
| `generator_historicalpurchaserequisitiondetailgh.purchase_requisition_id` | `generator_purchase_requisition_gh` | code_fk |
| `generator_historicalpurchaserequisitiondetailtf.purchase_requisition_id` | `generator_purchase_requisition_tf` | code_fk |
| `generator_historicalpurchaserequisitiondetailzt.purchase_requisition_id` | `generator_purchase_requisition_zt` | code_fk |
| `generator_ingredients.parent_id` | `generator_ingredients` | code_fk |
| `generator_ingredients_split.ingredients_id` | `generator_ingredients` | code_fk |
| `generator_inspection_items.inspection_object_id` | `generator_objective` | code_fk |
| `generator_inspection_items.classification_5s_id` | `generator_definition_five_s` | code_fk |
| `generator_job_code.parent_id` | `generator_job_code` | code_fk |
| `generator_job_code_product.product_id` | `generator_product` | code_m2m |
| `generator_jobcode_devices.devices_id` | `generator_devices` | code_fk |
| `generator_jobcode_devices.job_code_id` | `generator_job_code` | code_fk |
| `generator_logistics_balance_mode.product_stock_id` | `generator_logistics_product_stock` | code_fk |
| `generator_logistics_detail_map.order_detail_id` | `generator_purchase_order_detail` | code_fk |
| `generator_logistics_detail_map.shipment_id` | `generator_logistics_shipment` | code_fk |
| `generator_logistics_product_stock.parent_id` | `generator_logistics_product_stock` | code_fk |
| `generator_logistics_product_stock_copy1.parent_id` | `generator_logistics_product_stock` | code_fk |
| `generator_logistics_push_log.shipment_id` | `generator_logistics_shipment` | code_fk |
| `generator_logistics_transaction_table.product_stock_id` | `generator_logistics_product_stock` | code_fk |
| `generator_logistics_transaction_table.logistics_waybill_id` | `generator_logistics_waybill` | code_fk |
| `generator_logistics_transaction_table.balance_mode_id` | `generator_logistics_balance_mode` | code_fk |
| `generator_logistics_transaction_table_copy1.product_stock_id` | `generator_logistics_product_stock` | code_fk |
| `generator_logistics_transaction_table_copy1.logistics_waybill_id` | `generator_logistics_waybill` | code_fk |
| `generator_logistics_transaction_table_copy1.balance_mode_id` | `generator_logistics_balance_mode` | code_fk |
| `generator_maintenance_records.device_id` | `generator_devices` | code_fk |
| `generator_maintenance_schedule.device_id` | `generator_devices` | code_fk |
| `generator_management_area_allocation.responsible_person_id` | `system_users` | code_fk |
| `generator_management_area_allocation.responsible_department_id` | `system_dept` | code_fk |
| `generator_order_detail_document_mapping.document_id` | `generator_purchase_order_document` | code_fk |
| `generator_order_detail_document_mapping.purchase_order_detail_id` | `generator_purchase_order_detail` | code_fk |
| `generator_order_detail_document_mapping_gh.document_id` | `generator_purchase_order_document_gh` | code_fk |
| `generator_order_detail_document_mapping_gh.purchase_order_detail_id` | `generator_purchase_order_detail_gh` | code_fk |
| `generator_order_detail_document_mapping_tf.document_id` | `generator_purchase_order_document_tf` | code_fk |
| `generator_order_detail_document_mapping_tf.purchase_order_detail_id` | `generator_purchase_order_detail_tf` | code_fk |
| `generator_order_detail_document_mapping_zt.document_id` | `generator_purchase_order_document_zt` | code_fk |
| `generator_order_detail_document_mapping_zt.purchase_order_detail_id` | `generator_purchase_order_detail_zt` | code_fk |
| `generator_payment_application.purchase_order_id` | `generator_purchase_order` | code_fk |
| `generator_payment_application.settlement_bill_id` | `generator_settlement_bill` | code_fk |
| `generator_payment_application_gh.purchase_order_id` | `generator_purchase_order_gh` | code_fk |
| `generator_payment_application_gh.settlement_bill_id` | `generator_settlement_bill_gh` | code_fk |
| `generator_payment_application_tf.purchase_order_id` | `generator_purchase_order_tf` | code_fk |
| `generator_payment_application_tf.settlement_bill_id` | `generator_settlement_bill_tf` | code_fk |
| `generator_payment_application_zt.purchase_order_id` | `generator_purchase_order_zt` | code_fk |
| `generator_payment_application_zt.settlement_bill_id` | `generator_settlement_bill_zt` | code_fk |
| `generator_payment_record.payment_application_id` | `generator_payment_application` | code_fk |
| `generator_payment_record_gh.payment_application_id` | `generator_payment_application_gh` | code_fk |
| `generator_payment_record_tf.payment_application_id` | `generator_payment_application_tf` | code_fk |
| `generator_payment_record_zt.payment_application_id` | `generator_payment_application_zt` | code_fk |
| `generator_plan_delivery_plan.customer_order_id` | `generator_customer_order` | code_fk |
| `generator_plan_delivery_plan.product_config_id` | `generator_plan_product_config` | code_fk |
| `generator_plan_delivery_plan_log.delivery_plan_id` | `generator_plan_delivery_plan` | code_fk |
| `generator_plan_inventory_snapshot.product_config_id` | `generator_plan_product_config` | code_fk |
| `generator_process_inventory.product_id` | `generator_product` | code_fk |
| `generator_process_inventory.station_id` | `track_station` | code_fk |
| `generator_product.parent_id` | `generator_product` | code_fk |
| `generator_product_plm_rufa.product_ready_id` | `generator_product_ready` | code_fk |
| `generator_product_plm_rufa.qrcode_in_id` | `generator_qrcode_in` | code_fk |
| `generator_product_plm_rufa.qrcode_out_id` | `generator_qrcode_out` | code_fk |
| `generator_product_szb.product_id_id` | `generator_product` | code_fk |
| `generator_production_line.parent_id` | `generator_production_line` | code_fk |
| `generator_production_tracking.product_id` | `generator_product` | code_fk |
| `generator_production_tracking.current_route_step_id` | `track_route_step` | code_fk |
| `generator_production_tracking.current_station_id` | `track_station` | code_fk |
| `generator_production_tracking.route_id` | `track_route` | code_fk |
| `generator_project_attendance.user_id` | `system_users` | code_fk |
| `generator_project_info.parent_id` | `generator_project_info` | code_fk |
| `generator_project_material_summary_detail.project_material_summary_id` | `generator_project_material_summary` | code_fk |
| `generator_project_material_summary_detail.purchase_order_detail_id` | `generator_purchase_order_detail` | code_fk |
| `generator_project_material_summary_detail_copy1.project_material_summary_id` | `generator_project_material_summary` | code_fk |
| `generator_project_material_summary_detail_gh.project_material_summary_id` | `generator_project_material_summary_gh` | code_fk |
| `generator_project_material_summary_detail_gh.purchase_order_detail_id` | `generator_purchase_order_detail_gh` | code_fk |
| `generator_project_material_summary_detail_tf.project_material_summary_id` | `generator_project_material_summary_tf` | code_fk |
| `generator_project_material_summary_detail_tf.purchase_order_detail_id` | `generator_purchase_order_detail_tf` | code_fk |
| `generator_project_material_summary_detail_zt.project_material_summary_id` | `generator_project_material_summary_zt` | code_fk |
| `generator_project_material_summary_detail_zt.purchase_order_detail_id` | `generator_purchase_order_detail_zt` | code_fk |
| `generator_project_schedule.parent_id` | `generator_project_schedule` | code_fk |
| `generator_project_schedule.project_info_id` | `generator_project_info` | code_fk |
| `generator_purchase_order_detail.purchase_order_id` | `generator_purchase_order` | code_fk |
| `generator_purchase_order_detail.purchase_requisition_id` | `generator_purchase_requisition` | code_fk |
| `generator_purchase_order_detail.supplier_material_map_id` | `generator_supplier_material_mapping` | code_fk |
| `generator_purchase_order_detail_copy1.purchase_order_id` | `generator_purchase_order` | code_fk |
| `generator_purchase_order_detail_copy1.purchase_requisition_id` | `generator_purchase_requisition` | code_fk |
| `generator_purchase_order_detail_copy1.supplier_material_map_id` | `generator_supplier_material_mapping` | code_fk |
| `generator_purchase_order_detail_gh.purchase_order_id` | `generator_purchase_order_gh` | code_fk |
| `generator_purchase_order_detail_gh.purchase_requisition_id` | `generator_purchase_requisition_gh` | code_fk |
| `generator_purchase_order_detail_gh.supplier_material_map_id` | `generator_supplier_material_mapping_gh` | code_fk |
| `generator_purchase_order_detail_tf.purchase_order_id` | `generator_purchase_order_tf` | code_fk |
| `generator_purchase_order_detail_tf.purchase_requisition_id` | `generator_purchase_requisition_tf` | code_fk |
| `generator_purchase_order_detail_tf.supplier_material_map_id` | `generator_supplier_material_mapping_tf` | code_fk |
| `generator_purchase_order_detail_zt.purchase_order_id` | `generator_purchase_order_zt` | code_fk |
| `generator_purchase_order_detail_zt.purchase_requisition_id` | `generator_purchase_requisition_zt` | code_fk |
| `generator_purchase_order_detail_zt.supplier_material_map_id` | `generator_supplier_material_mapping_zt` | code_fk |
| `generator_purchase_requisition_detail.purchase_requisition_id` | `generator_purchase_requisition` | code_fk |
| `generator_purchase_requisition_detail_gh.purchase_requisition_id` | `generator_purchase_requisition_gh` | code_fk |
| `generator_purchase_requisition_detail_tf.purchase_requisition_id` | `generator_purchase_requisition_tf` | code_fk |
| `generator_purchase_requisition_detail_zt.purchase_requisition_id` | `generator_purchase_requisition_zt` | code_fk |
| `generator_qrcode_sendout.customer_order_id` | `generator_customer_order` | code_fk |
| `generator_return_order_detail.return_order_header_id` | `generator_return_order` | code_fk |
| `generator_salary.newscheduling_id` | `generator_newscheduling` | code_fk |
| `generator_scheduling.code_id` | `system_users` | code_fk |
| `generator_scheduling.production_line_id` | `generator_production_line` | code_fk |
| `generator_scheduling.train_user_code_id` | `system_users` | code_fk |
| `generator_settlement_bill_detail.purchase_order_detail_id` | `generator_purchase_order_detail` | code_fk |
| `generator_settlement_bill_detail.settlement_bill_id` | `generator_settlement_bill` | code_fk |
| `generator_settlement_bill_detail_gh.purchase_order_detail_id` | `generator_purchase_order_detail_gh` | code_fk |
| `generator_settlement_bill_detail_gh.settlement_bill_id` | `generator_settlement_bill_gh` | code_fk |
| `generator_settlement_bill_detail_tf.purchase_order_detail_id` | `generator_purchase_order_detail_tf` | code_fk |
| `generator_settlement_bill_detail_tf.settlement_bill_id` | `generator_settlement_bill_tf` | code_fk |
| `generator_settlement_bill_detail_zt.purchase_order_detail_id` | `generator_purchase_order_detail_zt` | code_fk |
| `generator_settlement_bill_detail_zt.settlement_bill_id` | `generator_settlement_bill_zt` | code_fk |
| `generator_settlement_invoice.settlement_bill_id` | `generator_settlement_bill` | code_fk |
| `generator_settlement_invoice_detail.settlement_bill_detail_id` | `generator_settlement_bill_detail` | code_fk |
| `generator_settlement_invoice_detail.settlement_invoice_id` | `generator_settlement_invoice` | code_fk |
| `generator_settlement_invoice_detail_gh.settlement_bill_detail_id` | `generator_settlement_bill_detail_gh` | code_fk |
| `generator_settlement_invoice_detail_gh.settlement_invoice_id` | `generator_settlement_invoice_gh` | code_fk |
| `generator_settlement_invoice_detail_tf.settlement_bill_detail_id` | `generator_settlement_bill_detail_tf` | code_fk |
| `generator_settlement_invoice_detail_tf.settlement_invoice_id` | `generator_settlement_invoice_tf` | code_fk |
| `generator_settlement_invoice_detail_zt.settlement_bill_detail_id` | `generator_settlement_bill_detail_zt` | code_fk |
| `generator_settlement_invoice_detail_zt.settlement_invoice_id` | `generator_settlement_invoice_zt` | code_fk |
| `generator_settlement_invoice_gh.settlement_bill_id` | `generator_settlement_bill_gh` | code_fk |
| `generator_settlement_invoice_payment_allocation.settlement_invoice_detail_id` | `generator_settlement_invoice_detail` | code_fk |
| `generator_settlement_invoice_payment_allocation.settlement_payment_allocation_id` | `generator_settlement_payment_allocation` | code_fk |
| `generator_settlement_invoice_payment_allocation_gh.settlement_invoice_detail_id` | `generator_settlement_invoice_detail_gh` | code_fk |
| `generator_settlement_invoice_payment_allocation_gh.settlement_payment_allocation_id` | `generator_settlement_payment_allocation_gh` | code_fk |
| `generator_settlement_invoice_payment_allocation_tf.settlement_invoice_detail_id` | `generator_settlement_invoice_detail_tf` | code_fk |
| `generator_settlement_invoice_payment_allocation_tf.settlement_payment_allocation_id` | `generator_settlement_payment_allocation_tf` | code_fk |
| `generator_settlement_invoice_payment_allocation_zt.settlement_invoice_detail_id` | `generator_settlement_invoice_detail_zt` | code_fk |
| `generator_settlement_invoice_payment_allocation_zt.settlement_payment_allocation_id` | `generator_settlement_payment_allocation_zt` | code_fk |
| `generator_settlement_invoice_tf.settlement_bill_id` | `generator_settlement_bill_tf` | code_fk |
| `generator_settlement_invoice_zt.settlement_bill_id` | `generator_settlement_bill_zt` | code_fk |
| `generator_settlement_payment_allocation.payment_record_id` | `generator_payment_record` | code_fk |
| `generator_settlement_payment_allocation.settlement_bill_detail_id` | `generator_settlement_bill_detail` | code_fk |
| `generator_settlement_payment_allocation_gh.payment_record_id` | `generator_payment_record_gh` | code_fk |
| `generator_settlement_payment_allocation_gh.settlement_bill_detail_id` | `generator_settlement_bill_detail_gh` | code_fk |
| `generator_settlement_payment_allocation_tf.payment_record_id` | `generator_payment_record_tf` | code_fk |
| `generator_settlement_payment_allocation_tf.settlement_bill_detail_id` | `generator_settlement_bill_detail_tf` | code_fk |
| `generator_settlement_payment_allocation_zt.payment_record_id` | `generator_payment_record_zt` | code_fk |
| `generator_settlement_payment_allocation_zt.settlement_bill_detail_id` | `generator_settlement_bill_detail_zt` | code_fk |
| `generator_shift_template_member.template_id` | `generator_shift_template` | code_fk |
| `generator_site_management.region_id` | `generator_management_area_allocation` | code_fk |
| `generator_site_management.responsible_person_id` | `system_users` | code_fk |
| `generator_site_management.inspector_id` | `system_users` | code_fk |
| `generator_site_management.classification_5_s_id` | `generator_definition_five_s` | code_fk |
| `generator_site_management.responsible_department_id` | `system_dept` | code_fk |
| `generator_supplier_material_mapping.purchase_material_id` | `generator_purchase_material` | code_fk |
| `generator_supplier_material_mapping.supplier_id` | `generator_supplier` | code_fk |
| `generator_supplier_material_mapping_gh.purchase_material_id` | `generator_purchase_material_gh` | code_fk |
| `generator_supplier_material_mapping_gh.supplier_id` | `generator_supplier_gh` | code_fk |
| `generator_supplier_material_mapping_tf.purchase_material_id` | `generator_purchase_material_tf` | code_fk |
| `generator_supplier_material_mapping_tf.supplier_id` | `generator_supplier_tf` | code_fk |
| `generator_supplier_material_mapping_zt.purchase_material_id` | `generator_purchase_material_zt` | code_fk |
| `generator_supplier_material_mapping_zt.supplier_id` | `generator_supplier_zt` | code_fk |
| `generator_tf_coremaking.sand_count_id` | `generator_ingredients` | code_fk |
| `generator_tf_coremaking.mould_id` | `generator_tf_mould` | code_fk |
| `generator_tf_coremaking_batch_relation.coremaking_id` | `generator_tf_coremaking` | code_fk |
| `generator_tf_mould_operate.mould_id` | `generator_tf_mould` | code_fk |
| `generator_tf_mould_scanreport.code_id` | `generator_tf_mould` | code_fk |
| `generator_tracking_transfer.device_id` | `generator_devices` | code_fk |
| `generator_tracking_transfer.tracking_id` | `generator_production_tracking` | code_fk |
| `generator_tracking_transfer.from_station_id` | `track_station` | code_fk |
| `generator_tracking_transfer.to_station_id` | `track_station` | code_fk |
| `generator_tracking_waste_record.tracking_id` | `generator_production_tracking` | code_fk |
| `generator_tracking_waste_record.transfer_id` | `generator_tracking_transfer` | code_fk |
| `generator_users_ticket.ticket_id` | `generator_ticket` | code_fk |
| `generator_users_ticket.users_id` | `system_users` | code_fk |
| `generator_warehouse_inventory.supplier_material_map_id` | `generator_supplier_material_mapping` | code_fk |
| `generator_warehouse_inventory_gh.supplier_material_map_id` | `generator_supplier_material_mapping_gh` | code_fk |
| `generator_warehouse_inventory_tf.supplier_material_map_id` | `generator_supplier_material_mapping_tf` | code_fk |
| `generator_warehouse_inventory_zt.supplier_material_map_id` | `generator_supplier_material_mapping_zt` | code_fk |
| `generator_warehouse_transaction_detail.warehouse_transaction_id` | `generator_warehouse_transaction` | code_fk |
| `generator_warehouse_transaction_detail.purchase_order_detail_id` | `generator_purchase_order_detail` | code_fk |
| `generator_warehouse_transaction_detail_copy1.warehouse_transaction_id` | `generator_warehouse_transaction` | code_fk |
| `generator_warehouse_transaction_detail_gh.warehouse_transaction_id` | `generator_warehouse_transaction_gh` | code_fk |
| `generator_warehouse_transaction_detail_gh.purchase_order_detail_id` | `generator_purchase_order_detail_gh` | code_fk |
| `generator_warehouse_transaction_detail_tf.warehouse_transaction_id` | `generator_warehouse_transaction_tf` | code_fk |
| `generator_warehouse_transaction_detail_tf.purchase_order_detail_id` | `generator_purchase_order_detail_tf` | code_fk |
| `generator_warehouse_transaction_detail_zt.warehouse_transaction_id` | `generator_warehouse_transaction_zt` | code_fk |
| `generator_warehouse_transaction_detail_zt.purchase_order_detail_id` | `generator_purchase_order_detail_zt` | code_fk |
| `knife_jobcode.job_code_id` | `generator_job_code` | code_fk |
| `system_area.pcode_id` | `self` | code_fk |
| `system_category_dict.parent_id` | `system_category_dict` | code_fk |
| `system_config.parent_id` | `self` | code_fk |
| `system_dept.parent_id` | `system_dept` | code_fk |
| `system_dict_item.dict_id` | `system_dict` | code_fk |
| `system_menu.parent_id` | `system_menu` | code_fk |
| `system_menu_button.menu_id` | `system_menu` | code_fk |
| `system_menu_column_field.menu_id` | `system_menu` | code_fk |
| `system_role_column.role_id` | `system_role` | code_m2m |
| `system_role_dept.role_id` | `system_role` | code_m2m |
| `system_role_dept.dept_id` | `system_dept` | code_m2m |
| `system_role_menu.role_id` | `system_role` | code_m2m |
| `system_role_menu.menu_id` | `system_menu` | code_m2m |
| `system_role_permission.role_id` | `system_role` | code_m2m |
| `system_users.dept_id` | `system_dept` | code_fk |
| `system_users_post.users_id` | `system_users` | code_m2m |
| `system_users_post.post_id` | `system_post` | code_m2m |
| `system_users_role.users_id` | `system_users` | code_m2m |
| `system_users_role.role_id` | `system_role` | code_m2m |
| `track_route_step.route_id` | `track_route` | code_fk |
| `track_route_step.station_id` | `track_station` | code_fk |
| `track_station_job_code_map.job_code_id` | `generator_job_code` | code_fk |
| `track_station_job_code_map.station_id` | `track_station` | code_fk |

## 命名推断关系（补充，置信中）
| 从表.字段 | 到表 | 说明 |
|---|---|---|
| `att_transaction.employee_code` | `system_users` | att-考勤打卡接口 |
| `att_transaction.dept_name` | `system_dept` | att-考勤打卡接口 |
| `auth_group_permissions.group_id` | `system_users_groups` | 字段名惯例推断 |
| `auth_group_permissions.permission_id` | `system_role_permission` | 字段名惯例推断 |
| `auth_permission.content_type_id` | `django_content_type` | 字段名惯例推断 |
| `django_admin_log.content_type_id` | `django_content_type` | 字段名惯例推断 |
| `django_admin_log.user_id` | `system_users` | 字段名惯例推断 |
| `django_celery_beat_periodictask.clocked_id` | `django_celery_beat_clockedschedule` | InnoDB硬外键 |
| `django_celery_beat_periodictask.crontab_id` | `django_celery_beat_crontabschedule` | InnoDB硬外键 |
| `django_celery_beat_periodictask.interval_id` | `django_celery_beat_intervalschedule` | InnoDB硬外键 |
| `django_celery_beat_periodictask.solar_id` | `django_celery_beat_solarschedule` | InnoDB硬外键 |
| `django_celery_results_chordcounter.group_id` | `system_users_groups` | 字段名惯例推断 |
| `django_celery_results_groupresult.group_id` | `system_users_groups` | 字段名惯例推断 |
| `generator_capability_score.user_code` | `system_users` | hr-人力能力接口 |
| `generator_dailyreport.creator_id` | `system_users` | dailyreport-日报任务接口 |
| `generator_dailytask.project_id` | `go_view_project` | 字段名惯例推断 |
| `generator_dailytask.creator_id` | `system_users` | dailyreport-日报任务接口 |
| `generator_devices.id` | `generator_equipment_repair` | device-设备装置接口 |
| `generator_devices.internal_code` | `generator_newscheduling` | device-设备装置接口 |
| `generator_historicaljobcode.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicaljobcode_devices.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseorder.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseorderdetail.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_historicalpurchaseorderdetail.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseorderdetailgh.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_historicalpurchaseorderdetailgh.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseorderdetailtf.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_historicalpurchaseorderdetailtf.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseorderdetailzt.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_historicalpurchaseorderdetailzt.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseordergh.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseordertf.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaseorderzt.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisition.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisitiondetail.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisitiondetailgh.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisitiondetailtf.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisitiondetailzt.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisitiongh.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisitiontf.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_historicalpurchaserequisitionzt.history_user_id` | `system_users` | InnoDB硬外键 |
| `generator_jgdm.creator_id` | `system_users` | process-工艺技术接口 |
| `generator_job_code_product.jobcode_id` | `knife_jobcode` | 字段名惯例推断 |
| `generator_knife_life_standards.production_line_id` | `generator_production_line` | 字段名惯例推断 |
| `generator_knife_life_standards_copy1.production_line_id` | `generator_production_line` | 字段名惯例推断 |
| `generator_machine_tool_change.production_line_id` | `generator_production_line` | 字段名惯例推断 |
| `generator_maintenance_records.creator_id` | `system_users` | maintenance-维修保养接口 |
| `generator_monthlytask.project_id` | `go_view_project` | 字段名惯例推断 |
| `generator_monthlytask.creator_id` | `system_users` | dailyreport-日报任务接口 |
| `generator_newscheduling.device_code` | `generator_devices` | newscheduling-新排程接口 |
| `generator_newscheduling.creator_id` | `system_users` | newscheduling-新排程接口 |
| `generator_newscheduling.id` | `generator_salary` | newscheduling-新排程接口 |
| `generator_project_material_summary_detail.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_project_material_summary_detail_copy1.purchase_order_id` | `generator_purchase_order` | 字段名惯例推断 |
| `generator_project_material_summary_detail_copy1.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_project_material_summary_detail_gh.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_project_material_summary_detail_tf.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_project_material_summary_detail_zt.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_purchase_order_detail.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_purchase_order_detail_copy1.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_purchase_order_detail_gh.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_purchase_order_detail_tf.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_purchase_order_detail_zt.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_rework_record_header.id` | `extraneous_product_qrcode` | bad-不良品接口 |
| `generator_roster.employee_id` | `system_users` | hr-人力能力接口 |
| `generator_shift_schedule.creator_id` | `system_users` | shift-班次接口 |
| `generator_tool_replacement.production_line_id` | `generator_production_line` | 字段名惯例推断 |
| `generator_warehouse_transaction_detail.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_warehouse_transaction_detail_copy1.purchase_order_id` | `generator_purchase_order` | 字段名惯例推断 |
| `generator_warehouse_transaction_detail_copy1.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_warehouse_transaction_detail_gh.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_warehouse_transaction_detail_tf.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `generator_warehouse_transaction_detail_zt.purchase_requisition_detail_id` | `generator_purchase_requisition_detail` | 字段名惯例推断 |
| `system_product_szb.product_id` | `generator_bad_product` | 字段名惯例推断 |
| `system_users.id` | `django_admin_log` | system-用户权限接口 |
| `system_users_groups.users_id` | `system_users` | 字段名惯例推断 |
| `system_users_groups.group_id` | `system_users_groups` | 字段名惯例推断 |
| `system_users_user_permissions.users_id` | `system_users` | 字段名惯例推断 |
| `system_users_user_permissions.permission_id` | `system_role_permission` | 字段名惯例推断 |