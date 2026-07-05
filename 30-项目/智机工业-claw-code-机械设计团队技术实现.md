# 智机工业 - claw-code 在机械设计团队的技术实现细节

## 1. 团队现状与痛点分析

### 1.1 团队构成
- 3名资深机械设计师
- 主要软件：SolidWorks 2024、AutoCAD Mechanical、Teamcenter PDM
- 设计范围：汽车发动机件（缸体、曲轴、凸轮轴）、底盘件（转向节、控制臂、轮毂）的工装夹具、自动化上下料机构

### 1.2 核心痛点
1. **BOM 管理低效**：手动从 SolidWorks 导出 BOM，再手工录入 ERP 系统，平均每个项目耗时 4-6 小时
2. **标准件库混乱**：各部门使用不同的标准件命名规范，导致采购错误率 3-5%
3. **图纸版本控制**：依赖 PDM 系统但缺乏自动化版本对比工具
4. **设计验证重复**：相似结构的有限元分析需要重复设置边界条件

## 2. claw-code 集成方案

### 2.1 技术架构
```
┌─────────────────────────────────────────────┐
│           机械设计工作流自动化平台           │
├─────────────────────────────────────────────┤
│  claw-code 代码生成引擎                      │
│  ├── SolidWorks API 封装层                  │
│  ├── AutoCAD .NET 接口层                    │
│  ├── PDM 系统集成模块                        │
│  └── ERP/MES 数据对接模块                   │
└─────────────────────────────────────────────┘
```

### 2.2 环境配置要求
```yaml
# 开发环境配置
development:
  os: Windows 10/11 专业版
  cad_software:
    - solidworks: 2022-2024
    - autocad_mechanical: 2023-2024
  programming:
    - python: 3.9+
    - .net_framework: 4.8
    - solidworks_api: Interop.SldWorks
  dependencies:
    - pywin32: 305+
    - comtypes: 1.2.0+
    - pandas: 1.5.0+
    - openpyxl: 3.1.0+
```

## 3. 核心功能模块实现

### 3.1 BOM 自动化导出系统

#### 3.1.1 SolidWorks BOM 解析模块
```python
# bom_automation/solidworks_bom_extractor.py
import win32com.client
import json
import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional

class SolidWorksBOMExtractor:
    """SolidWorks BOM 自动化提取器"""
    
    def __init__(self, sw_app=None):
        """初始化 SolidWorks 连接"""
        self.sw_app = sw_app or win32com.client.Dispatch("SldWorks.Application")
        self.sw_app.Visible = False  # 后台运行
        
    def extract_bom_from_assembly(self, assembly_path: str) -> Dict:
        """
        从装配体提取完整 BOM 信息
        
        Args:
            assembly_path: SolidWorks 装配体文件路径
            
        Returns:
            结构化 BOM 数据
        """
        try:
            # 打开装配体
            doc = self.sw_app.OpenDoc6(
                assembly_path,
                2,  # swDocASSEMBLY
                0,  # swOpenDocOptions_Silent
                "",
                errors=0,
                warnings=0
            )
            
            if not doc:
                raise Exception(f"无法打开文件: {assembly_path}")
            
            # 获取配置管理器
            config_mgr = doc.ConfigurationManager
            active_config = config_mgr.ActiveConfiguration
            
            # 获取 BOM 表
            bom_table = self._get_bom_table(doc, active_config)
            
            # 提取 BOM 数据
            bom_data = self._parse_bom_table(bom_table)
            
            # 关闭文档（不保存）
            self.sw_app.CloseDoc(assembly_path)
            
            return {
                "assembly_name": assembly_path.split("\\")[-1],
                "extraction_time": datetime.now().isoformat(),
                "total_components": len(bom_data),
                "bom_items": bom_data,
                "metadata": self._extract_metadata(doc)
            }
            
        except Exception as e:
            self.sw_app.CloseDoc(assembly_path)
            raise Exception(f"BOM 提取失败: {str(e)}")
    
    def _get_bom_table(self, doc, config):
        """获取 BOM 表对象"""
        # 创建 BOM 表注解
        annotation = doc.Annotation
        bom_feature = annotation.InsertBillOfMaterials2(
            0,  # swBOMConfigurationAnchor_TopLeft
            0, 0,  # X, Y 坐标
            0,  # swBOMType_TopLevelOnly
            config.Name,
            0,  # 不使用模板
            True  # 隐藏零部件
        )
        
        # 获取 BOM 表对象
        bom_table = bom_feature.GetTable
        return bom_table
    
    def _parse_bom_table(self, bom_table) -> List[Dict]:
        """解析 BOM 表数据"""
        bom_items = []
        
        # 获取行列数
        row_count = bom_table.RowCount
        col_count = bom_table.ColumnCount
        
        # 获取列标题（第一行）
        headers = []
        for col in range(col_count):
            cell_text = bom_table.Text(row=0, column=col)
            headers.append(cell_text.strip())
        
        # 提取数据行（从第二行开始）
        for row in range(1, row_count):
            item = {}
            for col in range(col_count):
                cell_text = bom_table.Text(row=row, column=col)
                header = headers[col] if col < len(headers) else f"Column_{col}"
                item[header] = cell_text.strip()
            
            # 标准化字段名
            standardized_item = self._standardize_bom_item(item)
            if standardized_item:
                bom_items.append(standardized_item)
        
        return bom_items
    
    def _standardize_bom_item(self, item: Dict) -> Dict:
        """标准化 BOM 项字段"""
        # 字段名映射表
        field_mapping = {
            "项目号": "item_number",
            "零件号": "part_number",
            "说明": "description",
            "数量": "quantity",
            "材料": "material",
            "重量": "weight",
            "备注": "remarks",
            "Item No.": "item_number",
            "Part No.": "part_number",
            "Description": "description",
            "QTY.": "quantity"
        }
        
        standardized = {}
        for raw_key, value in item.items():
            std_key = field_mapping.get(raw_key, raw_key.lower().replace(" ", "_"))
            standardized[std_key] = value
        
        # 数据类型转换
        try:
            standardized["quantity"] = int(float(standardized.get("quantity", 1)))
        except:
            standardized["quantity"] = 1
        
        return standardized
    
    def _extract_metadata(self, doc) -> Dict:
        """提取文档元数据"""
        try:
            custom_props = doc.Extension.CustomPropertyManager[""]
            prop_names = custom_props.GetNames()
            
            metadata = {}
            for prop_name in prop_names:
                value, resolved = custom_props.Get6(prop_name, False, "")
                metadata[prop_name] = value
            
            return {
                "author": metadata.get("Author", ""),
                "revision": metadata.get("Revision", ""),
                "project": metadata.get("Project", ""),
                "created_date": metadata.get("CreatedDate", ""),
                "custom_properties": metadata
            }
        except:
            return {}

# 使用示例
def generate_bom_export_script():
    """claw-code 生成的 BOM 导出脚本模板"""
    script_template = '''#!/usr/bin/env python3
"""
自动生成的 BOM 导出脚本
生成时间: {timestamp}
目标装配体: {assembly_pattern}
"""

import os
import sys
import json
import pandas as pd
from pathlib import Path

# 添加自定义模块路径
sys.path.append(r"{module_path}")

from bom_automation.solidworks_bom_extractor import SolidWorksBOMExtractor

def batch_export_bom(assemblies_folder, output_folder):
    """
    批量导出 BOM 数据
    
    Args:
        assemblies_folder: 装配体文件夹路径
        output_folder: 输出文件夹路径
    """
    # 创建输出目录
    os.makedirs(output_folder, exist_ok=True)
    
    # 初始化提取器
    extractor = SolidWorksBOMExtractor()
    
    # 查找所有装配体文件
    assembly_files = []
    for ext in [".sldasm", ".SLDASM"]:
        assembly_files.extend(Path(assemblies_folder).glob(f"**/*{ext}"))
    
    print(f"找到 {len(assembly_files)} 个装配体文件")
    
    all_bom_data = []
    
    for assembly_file in assembly_files:
        try:
            print(f"处理: {assembly_file.name}")
            
            # 提取 BOM
            bom_data = extractor.extract_bom_from_assembly(str(assembly_file))
            
            # 保存为 JSON
            json_path = Path(output_folder) / f"{assembly_file.stem}_bom.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(bom_data, f, ensure_ascii=False, indent=2)
            
            # 保存为 Excel
            excel_path = Path(output_folder) / f"{assembly_file.stem}_bom.xlsx"
            df = pd.DataFrame(bom_data['bom_items'])
            df.to_excel(excel_path, index=False)
            
            all_bom_data.append({
                "file": assembly_file.name,
                "bom": bom_data,
                "export_time": pd.Timestamp.now()
            })
            
            print(f"  ✓ 已导出: {json_path}")
            
        except Exception as e:
            print(f"  ✗ 处理失败: {str(e)}")
    
    # 生成汇总报告
    if all_bom_data:
        summary_path = Path(output_folder) / "bom_export_summary.xlsx"
        summary_data = []
        
        for item in all_bom_data:
            summary_data.append({
                "装配体": item["file"],
                "零件总数": item["bom"]["total_components"],
                "导出时间": item["export_time"],
                "状态": "成功"
            })
        
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(summary_path, index=False)
        print(f"\\n汇总报告已生成: {summary_path}")
    
    return all_bom_data

if __name__ == "__main__":
    # 配置路径
    ASSEMBLIES_FOLDER = r"{assemblies_path}"
    OUTPUT_FOLDER = r"{output_path}"
    
    # 执行批量导出
    results = batch_export_bom(ASSEMBLIES_FOLDER, OUTPUT_FOLDER)
    
    print(f"\\n处理完成！成功导出 {len(results)} 个装配体的 BOM 数据")
'''
    
    return script_template
```

#### 3.1.2 ERP 系统集成模块
```python
# bom_automation/erp_integration.py
import requests
import hashlib
import time
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ERPConfig:
    """ERP 系统配置"""
    base_url: str
    api_key: str
    company_code: str
    plant_code: str
    timeout: int = 30

class ERPIntegration:
    """ERP 系统集成接口"""
    
    def __init__(self, config: ERPConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json",
            "X-Company-Code": config.company_code,
            "X-Plant-Code": config.plant_code
        })
    
    def upload_bom_to_erp(self, bom_data: Dict, project_code: str) -> Dict:
        """
        上传 BOM 数据到 ERP 系统
        
        Args:
            bom_data: BOM 数据
            project_code: 项目编码
            
        Returns:
            上传结果
        """
        # 标准化 BOM 数据结构
        erp_payload = self._format_bom_for_erp(bom_data, project_code)
        
        # 调用 ERP API
        endpoint = f"{self.config.base_url}/api/v1/bom/upload"
        
        try:
            response = self.session.post(
                endpoint,
                json=erp_payload,
                timeout=self.config.timeout
            )
            
            response.raise_for_status()
            
            result = response.json()
            
            return {
                "success": True,
                "erp_reference": result.get("reference_number"),
                "upload_time": datetime.now().isoformat(),
                "message": "BOM 上传成功",
                "details": result
            }
            
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": str(e),
                "upload_time": datetime.now().isoformat(),
                "message": "BOM 上传失败"
            }
    
    def _format_bom_for_erp(self, bom_data: Dict, project_code: str) -> Dict:
        """格式化 BOM 数据为 ERP 系统要求的格式"""
        # 提取基本信息
        assembly_name = bom_data.get("assembly_name", "")
        extraction_time = bom_data.get("extraction_time", "")
        
        # 构建 ERP 物料清单
        bom_items = []
        
        for item in bom_data.get("bom_items", []):
            erp_item = {
                "itemNumber": item.get("item_number", ""),
                "materialCode": self._generate_material_code(item),
                "materialDescription": item.get("description", ""),
                "quantity": item.get("quantity", 1),
                "unitOfMeasure": "EA",  # 默认单位：个
                "materialGroup": self._determine_material_group(item),
                "procurementType": self._determine_procurement_type(item),
                "plant": self.config.plant_code,
                "storageLocation": "1000",  # 默认存储位置
                "batchManagement": False,
                "valuationType": "V",
                "priceControl": "S",
                "standardPrice": self._estimate_standard_price(item),
                "currency": "CNY",
                "costingLotSize": 1,
                "purchasingGroup": "001",
                "orderUnit": "EA",
                "minimumOrderQuantity": 1,
                "deliveryTime": 14,  # 默认交货期14天
                "safetyStock": 0,
                "reorderPoint": 0,
                "plannedDeliveryTime": 14,
                "goodsReceiptProcessingTime": 1,
                "inspectionSetupTime": 0.5,
                "inspectionProcessingTime": 0.5,
                "plannedOrderConversionFactor": 1,
                "roundingValue": 1,
                "toleranceOverDelivery": 10.0,  # 超交容差10%
                "toleranceUnderDelivery": 0.0,   # 欠交容差0%
                "unlimitedOverDelivery": False,
                "manufacturerPartNumber": item.get("part_number", ""),
                "manufacturer": self._identify_manufacturer(item),
                "technicalData": {
                    "material": item.get("material", ""),
                    "weight": item.get("weight", ""),
                    "dimensions": self._extract_dimensions(item),
                    "surfaceTreatment": "",
                    "heatTreatment": "",
                    "tolerance": "±0.1mm",
                    "drawingReference": item.get("part_number", "")
                },
                "qualityRequirements": {
                    "inspectionLevel": "II",
                    "aql": "1.0",
                    "samplingProcedure": "ISO 2859-1",
                    "inspectionCharacteristic": [
                        {
                            "characteristic": "Dimensions",
                            "method": "CMM",
                            "specification": "Per Drawing",
                            "tolerance": "±0.1mm"
                        },
                        {
                            "characteristic": "Surface Finish",
                            "method": "Surface Roughness Tester",
                            "specification": "Ra 1.6",
                            "tolerance": "+0/-0.4μm"
                        }
                    ]
                },
                "supplierInformation": {
                    "preferredSupplier": "",
                    "alternativeSupplier": "",
                    "supplierPartNumber": "",
                    "supplierLeadTime": 14,
                    "moq": 1,
                    "packagingInstructions": "Standard"
                },
                "sustainabilityData": {
                    "rohsCompliant": True,
                    "reachCompliant": True,
                    "materialRecyclability": ">90%",
                    "co2Footprint": 0,
                    "energyConsumption": 0
                },
                "customFields": {
                    "designer": bom_data.get("metadata", {}).get("author", ""),
                    "revision": bom_data.get("metadata", {}).get("revision", ""),
                    "extractionTimestamp": extraction_time,
                    "sourceFile": assembly_name,
                    "projectCode": project_code
                }
            }
            
            bom_items.append(erp_item)
        
        # 构建完整 ERP 请求
        erp_payload = {
            "header": {
                "documentType": "BOM",
                "documentNumber": self._generate_document_number(),
                "companyCode": self.config.company_code,
                "plant": self.config.plant_code,
                "projectCode": project_code,
                "materialDocument": assembly_name,
                "documentDate": datetime.now().strftime("%Y%m%d"),
                "postingDate": datetime.now().strftime("%Y%m%d"),
                "createdBy": "AUTO_BOM