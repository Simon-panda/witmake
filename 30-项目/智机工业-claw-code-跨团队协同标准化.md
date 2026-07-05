# 智机工业 - claw-code 跨团队协同与标准化技术实现

## 1. 跨团队协同架构设计

### 1.1 统一数据模型与接口规范

#### 1.1.1 企业级数据字典
```python
# cross_team/enterprise_data_dictionary.py
import os
import json
import yaml
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union
from enum import Enum
from datetime import datetime
import hashlib

class Department(Enum):
    """部门枚举"""
    MECHANICAL_DESIGN = "mechanical_design"
    ELECTRICAL_ENGINEERING = "electrical_engineering"
    VISION_ALGORITHM = "vision_algorithm"
    IT_FULLSTACK = "it_fullstack"
    DATA_AI = "data_ai"
    FIELD_SERVICE = "field_service"
    QUALITY_ASSURANCE = "quality_assurance"
    PROJECT_MANAGEMENT = "project_management"

class DataCategory(Enum):
    """数据分类枚举"""
    DESIGN_DATA = "design_data"
    PRODUCTION_DATA = "production_data"
    QUALITY_DATA = "quality_data"
    MAINTENANCE_DATA = "maintenance_data"
    BUSINESS_DATA = "business_data"
    SYSTEM_DATA = "system_data"

@dataclass
class DataFieldDefinition:
    """数据字段定义"""
    field_id: str
    field_name: str
    field_description: str
    data_type: str
    unit: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    default_value: Optional[Any] = None
    allowed_values: List[Any] = field(default_factory=list)
    validation_rules: List[str] = field(default_factory=list)
    source_department: Department = None
    owner_department: Department = None
    sensitivity_level: str = "internal"  # public/internal/confidential/restricted
    retention_period_days: int = 3650
    version: str = "1.0.0"
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

@dataclass
class DataModel:
    """数据模型定义"""
    model_id: str
    model_name: str
    model_description: str
    category: DataCategory
    fields: List[DataFieldDefinition]
    relationships: List[Dict] = field(default_factory=list)
    constraints: List[Dict] = field(default_factory=list)
    indexes: List[Dict] = field(default_factory=list)
    version: str = "1.0.0"
    created_by: str = "system"
    created_at: datetime = field(default_factory=datetime.now)

class EnterpriseDataDictionary:
    """企业级数据字典管理"""
    
    def __init__(self, dictionary_path: str = "./enterprise_data_dictionary"):
        self.dictionary_path = dictionary_path
        os.makedirs(dictionary_path, exist_ok=True)
        
        # 加载现有数据字典
        self.models = self._load_existing_models()
        
        # 标准数据模型
        self.standard_models = self._initialize_standard_models()
    
    def _load_existing_models(self) -> Dict[str, DataModel]:
        """加载现有数据模型"""
        models = {}
        
        model_files = [f for f in os.listdir(self.dictionary_path) 
                      if f.endswith('.json')]
        
        for model_file in model_files:
            file_path = os.path.join(self.dictionary_path, model_file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    model_data = json.load(f)
                
                # 转换为DataModel对象
                model = self._dict_to_datamodel(model_data)
                models[model.model_id] = model
                
            except Exception as e:
                print(f"加载模型文件失败 {model_file}: {str(e)}")
        
        return models
    
    def _initialize_standard_models(self) -> Dict[str, DataModel]:
        """初始化标准数据模型"""
        standard_models = {}
        
        # 1. 设备基础信息模型
        device_model = DataModel(
            model_id="DEVICE_BASIC_INFO",
            model_name="设备基础信息",
            model_description="所有设备的基础信息模型",
            category=DataCategory.SYSTEM_DATA,
            fields=[
                DataFieldDefinition(
                    field_id="device_id",
                    field_name="设备ID",
                    field_description="设备唯一标识符",
                    data_type="string",
                    validation_rules=["required", "unique", "length:6-20"],
                    source_department=Department.ELECTRICAL_ENGINEERING,
                    owner_department=Department.IT_FULLSTACK
                ),
                DataFieldDefinition(
                    field_id="device_name",
                    field_name="设备名称",
                    field_description="设备显示名称",
                    data_type="string",
                    validation_rules=["required", "length:2-100"],
                    source_department=Department.MECHANICAL_DESIGN,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="device_type",
                    field_name="设备类型",
                    field_description="设备分类类型",
                    data_type="string",
                    allowed_values=["CNC", "ROBOT", "AGV", "VISION", "MEASUREMENT"],
                    validation_rules=["required"],
                    source_department=Department.MECHANICAL_DESIGN,
                    owner_department=Department.IT_FULLSTACK
                ),
                DataFieldDefinition(
                    field_id="model_number",
                    field_name="型号",
                    field_description="设备型号",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.MECHANICAL_DESIGN,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="manufacturer",
                    field_name="制造商",
                    field_description="设备制造商",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.MECHANICAL_DESIGN,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="serial_number",
                    field_name="序列号",
                    field_description="设备序列号",
                    data_type="string",
                    validation_rules=["required", "unique"],
                    source_department=Department.ELECTRICAL_ENGINEERING,
                    owner_department=Department.IT_FULLSTACK
                ),
                DataFieldDefinition(
                    field_id="installation_date",
                    field_name="安装日期",
                    field_description="设备安装日期",
                    data_type="date",
                    validation_rules=["required"],
                    source_department=Department.FIELD_SERVICE,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="status",
                    field_name="状态",
                    field_description="设备当前状态",
                    data_type="string",
                    allowed_values=["INSTALLING", "COMMISSIONING", "RUNNING", 
                                  "MAINTENANCE", "STOPPED", "DECOMMISSIONED"],
                    validation_rules=["required"],
                    source_department=Department.IT_FULLSTACK,
                    owner_department=Department.IT_FULLSTACK
                ),
                DataFieldDefinition(
                    field_id="location",
                    field_name="位置",
                    field_description="设备安装位置",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.FIELD_SERVICE,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="responsible_person",
                    field_name="负责人",
                    field_description="设备负责人",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.PROJECT_MANAGEMENT
                )
            ],
            relationships=[
                {
                    "type": "one_to_many",
                    "target_model": "DEVICE_PARAMETER",
                    "foreign_key": "device_id",
                    "description": "设备参数关系"
                },
                {
                    "type": "one_to_many",
                    "target_model": "MAINTENANCE_RECORD",
                    "foreign_key": "device_id",
                    "description": "维护记录关系"
                }
            ]
        )
        standard_models[device_model.model_id] = device_model
        
        # 2. 生产订单模型
        production_order_model = DataModel(
            model_id="PRODUCTION_ORDER",
            model_name="生产订单",
            model_description="生产订单信息模型",
            category=DataCategory.BUSINESS_DATA,
            fields=[
                DataFieldDefinition(
                    field_id="order_id",
                    field_name="订单ID",
                    field_description="生产订单唯一标识",
                    data_type="string",
                    validation_rules=["required", "unique", "pattern:^PO-\\d{8}-\\d{4}$"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="customer_id",
                    field_name="客户ID",
                    field_description="客户标识",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="part_number",
                    field_name="零件号",
                    field_description="生产零件编号",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.MECHANICAL_DESIGN,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="part_name",
                    field_name="零件名称",
                    field_description="零件名称",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.MECHANICAL_DESIGN,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="quantity",
                    field_name="数量",
                    field_description="生产数量",
                    data_type="integer",
                    min_value=1,
                    validation_rules=["required", "min:1"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="priority",
                    field_name="优先级",
                    field_description="生产优先级",
                    data_type="string",
                    allowed_values=["LOW", "MEDIUM", "HIGH", "URGENT"],
                    default_value="MEDIUM",
                    validation_rules=["required"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="due_date",
                    field_name="交付日期",
                    field_description="订单交付日期",
                    data_type="date",
                    validation_rules=["required"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="status",
                    field_name="状态",
                    field_description="订单状态",
                    data_type="string",
                    allowed_values=["PLANNED", "SCHEDULED", "IN_PROGRESS", 
                                  "COMPLETED", "CANCELLED", "ON_HOLD"],
                    default_value="PLANNED",
                    validation_rules=["required"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.PROJECT_MANAGEMENT
                ),
                DataFieldDefinition(
                    field_id="assigned_machine",
                    field_name="分配设备",
                    field_description="分配的生产设备",
                    data_type="string",
                    validation_rules=[],
                    source_department=Department.IT_FULLSTACK,
                    owner_department=Department.IT_FULLSTACK
                ),
                DataFieldDefinition(
                    field_id="quality_requirements",
                    field_name="质量要求",
                    field_description="质量检验标准",
                    data_type="json",
                    validation_rules=[],
                    source_department=Department.QUALITY_ASSURANCE,
                    owner_department=Department.QUALITY_ASSURANCE
                )
            ]
        )
        standard_models[production_order_model.model_id] = production_order_model
        
        # 3. 质量检测结果模型
        quality_inspection_model = DataModel(
            model_id="QUALITY_INSPECTION",
            model_name="质量检测结果",
            model_description="产品质量检测结果模型",
            category=DataCategory.QUALITY_DATA,
            fields=[
                DataFieldDefinition(
                    field_id="inspection_id",
                    field_name="检验ID",
                    field_description="检验记录唯一标识",
                    data_type="string",
                    validation_rules=["required", "unique", "pattern:^QI-\\d{8}-\\d{6}$"],
                    source_department=Department.QUALITY_ASSURANCE,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="order_id",
                    field_name="订单ID",
                    field_description="关联的生产订单",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.PROJECT_MANAGEMENT,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="part_number",
                    field_name="零件号",
                    field_description="检验零件编号",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.MECHANICAL_DESIGN,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="batch_number",
                    field_name="批次号",
                    field_description="生产批次号",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.IT_FULLSTACK,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="inspection_type",
                    field_name="检验类型",
                    field_description="检验方式",
                    data_type="string",
                    allowed_values=["FIRST_ARTICLE", "SAMPLING", "FULL", "AUDIT"],
                    validation_rules=["required"],
                    source_department=Department.QUALITY_ASSURANCE,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="inspector",
                    field_name="检验员",
                    field_description="执行检验的人员",
                    data_type="string",
                    validation_rules=["required"],
                    source_department=Department.QUALITY_ASSURANCE,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="inspection_date",
                    field_name="检验日期",
                    field_description="检验执行日期",
                    data_type="datetime",
                    validation_rules=["required"],
                    source_department=Department.QUALITY_ASSURANCE,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="measurement_data",
                    field_name="测量数据",
                    field_description="尺寸测量结果",
                    data_type="json",
                    validation_rules=["required"],
                    source_department=Department.VISION_ALGORITHM,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="defect_data",
                    field_name="缺陷数据",
                    field_description="表面缺陷检测结果",
                    data_type="json",
                    validation_rules=[],
                    source_department=Department.VISION_ALGORITHM,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="overall_result",
                    field_name="总体结果",
                    field_description="检验总体结论",
                    data_type="string",
                    allowed_values=["PASS", "FAIL", "CONDITIONAL_PASS"],
                    validation_rules=["required"],
                    source_department=Department.QUALITY_ASSURANCE,
                    owner_department=Department.QUALITY_ASSURANCE
                ),
                DataFieldDefinition(
                    field_id="remarks",
                    field_name="备注",
                    field_description="检验备注",
                    data_type="text",
                    validation_rules=[],
                    source_department=Department.QUALITY_ASSURANCE,
                    owner_department=Department.QUALITY_ASSURANCE
                )
            ]
        )
        standard_models[quality_inspection_model.model_id] = quality_inspection_model
        
        return standard_models
    
    def _dict_to_datamodel(self, data: Dict) -> DataModel:
        """字典转换为DataModel对象"""
        # 转换字段定义
        fields = []
        for field_data in data.get('fields', []):
            # 处理datetime字段
            for time_field in ['created_at', 'updated_at']:
                if time_field in field_data and isinstance(field_data[time_field], str):
                    field_data[time_field] = datetime.fromisoformat(field_data[time_field].replace('Z', '+00:00'))
            
            field = DataFieldDefinition(**field_data)
            fields.append(field)
        
        # 处理datetime字段
        for time_field in ['created_at', 'updated_at']:
            if time_field in data and isinstance(data[time_field], str):
                data[time_field] = datetime.fromisoformat(data[time_field].replace('Z', '+00:00'))
        
        # 创建DataModel对象
        model = DataModel(
            model_id=data['model_id'],
            model_name=data['model_name'],
            model_description=data['model_description'],
            category=DataCategory(data['category']),
            fields=fields,
            relationships=data.get('relationships', []),
            constraints=data.get('constraints', []),
            indexes=data.get('indexes', []),
            version=data.get('version', '1.0.0'),
            created_by=data.get('created_by', 'system'),
            created_at=data.get('created_at', datetime.now()),
            updated_at=data.get('updated_at', datetime.now())
        )
        
        return model
    
    def generate_model_code(self, model_id: str, target_technology: str) -> Dict:
        """
        为指定模型生成代码
        
        Args:
            model_id: 模型ID
            target_technology: 目标技术栈
            
