# 智机工业 - claw-code 在电气工程团队的技术实现细节

## 1. 团队现状与痛点分析

### 1.1 团队构成
- 3名资深电气工程师
- 主要软件：EPLAN Electric P8、Siemens TIA Portal、Rockwell Studio 5000
- 工作范围：CNC 设备电气控制系统设计、PLC 编程、HMI 界面开发、现场调试

### 1.2 核心痛点
1. **IO 地址表管理混乱**：手动整理 Excel 表格，与图纸不同步，错误率 5-8%
2. **PLC 程序标准化不足**：不同工程师风格差异大，维护困难
3. **调试工具缺乏**：现场通讯测试依赖手动操作，效率低下
4. **文档生成耗时**：电气图纸、程序说明文档手动编制，占项目时间 20-30%

## 2. claw-code 集成方案

### 2.1 技术架构
```
┌─────────────────────────────────────────────┐
│           电气工程工作流自动化平台           │
├─────────────────────────────────────────────┤
│  claw-code 代码生成引擎                      │
│  ├── EPLAN API 集成层                       │
│  ├── TIA Portal 自动化接口                  │
│  ├── PLC 代码标准化模块                      │
│  ├── HMI 界面生成器                         │
│  └── 现场调试工具包                         │
└─────────────────────────────────────────────┘
```

### 2.2 环境配置要求
```yaml
# 开发环境配置
development:
  os: Windows 10/11 专业版
  electrical_software:
    - eplan_electric_p8: 2022-2024
    - siemens_tia_portal: V17-V18
    - rockwell_studio_5000: V33-V35
  programming:
    - python: 3.9+
    - .net_framework: 4.8
    - eplan_api: Eplan.EplApi.Base
  dependencies:
    - pywin32: 305+
    - pythonnet: 3.0.0+
    - pymodbus: 3.2.0+
    - snap7: 1.4.0+
    - pandas: 1.5.0+
    - openpyxl: 3.1.0+
```

## 3. 核心功能模块实现

### 3.1 EPLAN IO 地址表自动化生成

#### 3.1.1 EPLAN 项目解析模块
```python
# electrical_automation/eplan_io_extractor.py
import clr
import sys
import json
import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

# 添加 EPLAN API 引用
sys.path.append(r"C:\Program Files\EPLAN\Platform\2.9\API\EplApi.NET")
clr.AddReference("Eplan.EplApi.Base")
clr.AddReference("Eplan.EplApi.DataModel")
clr.AddReference("Eplan.EplApi.HEServices")

from Eplan.EplApi.Base import *
from Eplan.EplApi.DataModel import *
from Eplan.EplApi.HEServices import *

@dataclass
class IOAddress:
    """IO 地址数据结构"""
    device_tag: str          # 设备标识符
    io_type: str            # IO 类型: DI/DO/AI/AO
    address: str            # 物理地址: I0.0, Q0.1, AIW0, AQW2
    signal_name: str        # 信号名称
    description: str        # 功能描述
    cable_number: str       # 电缆编号
    terminal_number: str    # 端子号
    wire_number: str        # 线号
    page_reference: str     # 图纸页参考
    plc_module: str         # PLC 模块型号
    rack_slot: str          # 机架/插槽位置
    comment: str            # 备注
    data_type: str          # 数据类型: BOOL/INT/REAL
    scaling_factor: float   # 缩放系数
    engineering_unit: str   # 工程单位
    alarm_config: Dict      # 报警配置

class EplanIOExtractor:
    """EPLAN IO 地址表提取器"""
    
    def __init__(self, project_path: str = None):
        """初始化 EPLAN 连接"""
        self.project_path = project_path
        self.init_success = False
        
        try:
            # 初始化 EPLAN API
            self.settings = Settings()
            self.settings.SetStringSetting("USER.ProjectFilter.ProjectDirectory", project_path or "", 0)
            
            self.project = Project()
            if project_path:
                self.project.Open(project_path)
            
            self.init_success = True
            print(f"EPLAN API 初始化成功，项目: {project_path}")
            
        except Exception as e:
            print(f"EPLAN API 初始化失败: {str(e)}")
            self.init_success = False
    
    def extract_io_addresses(self, filter_criteria: Dict = None) -> List[IOAddress]:
        """
        从 EPLAN 项目提取所有 IO 地址
        
        Args:
            filter_criteria: 过滤条件
            
        Returns:
            IO 地址列表
        """
        if not self.init_success:
            raise Exception("EPLAN API 未正确初始化")
        
        io_addresses = []
        
        try:
            # 获取所有设备
            device_filter = DeviceFilter()
            devices = self.project.GetDevices(device_filter)
            
            for device in devices:
                # 检查是否为 IO 设备
                if self._is_io_device(device):
                    io_address = self._extract_device_io(device)
                    if io_address:
                        io_addresses.append(io_address)
            
            # 应用过滤条件
            if filter_criteria:
                io_addresses = self._filter_io_addresses(io_addresses, filter_criteria)
            
            return io_addresses
            
        except Exception as e:
            raise Exception(f"IO 地址提取失败: {str(e)}")
    
    def _is_io_device(self, device) -> bool:
        """判断是否为 IO 设备"""
        device_type = device.GetProperty("DT").GetValue() if device.GetProperty("DT") else ""
        
        io_device_types = [
            "DI", "DO", "AI", "AO",           # 数字/模拟 IO
            "PLC_DI", "PLC_DO", "PLC_AI", "PLC_AO",  # PLC IO
            "TERMINAL", "TERMINAL_STRIP",     # 端子
            "SENSOR", "ACTUATOR",             # 传感器/执行器
            "VALVE", "MOTOR", "DRIVE"         # 阀门/电机/驱动器
        ]
        
        return any(io_type in device_type.upper() for io_type in io_device_types)
    
    def _extract_device_io(self, device) -> Optional[IOAddress]:
        """从单个设备提取 IO 信息"""
        try:
            # 获取设备属性
            device_tag = device.GetProperty("DT").GetValue() if device.GetProperty("DT") else ""
            device_name = device.GetProperty("DP").GetValue() if device.GetProperty("DP") else ""
            
            # 确定 IO 类型
            io_type = self._determine_io_type(device)
            if not io_type:
                return None
            
            # 提取地址信息
            address = self._extract_address(device)
            if not address:
                return None
            
            # 构建 IO 地址对象
            io_address = IOAddress(
                device_tag=device_tag,
                io_type=io_type,
                address=address,
                signal_name=device_name,
                description=self._extract_description(device),
                cable_number=self._extract_cable_number(device),
                terminal_number=self._extract_terminal_number(device),
                wire_number=self._extract_wire_number(device),
                page_reference=self._extract_page_reference(device),
                plc_module=self._extract_plc_module(device),
                rack_slot=self._extract_rack_slot(device),
                comment=self._extract_comment(device),
                data_type=self._determine_data_type(io_type),
                scaling_factor=self._extract_scaling_factor(device),
                engineering_unit=self._extract_engineering_unit(device),
                alarm_config=self._extract_alarm_config(device)
            )
            
            return io_address
            
        except Exception as e:
            print(f"设备 {device.GetProperty('DT').GetValue()} IO 提取失败: {str(e)}")
            return None
    
    def _determine_io_type(self, device) -> str:
        """确定 IO 类型"""
        device_type = device.GetProperty("DT").GetValue() if device.GetProperty("DT") else ""
        
        if any(x in device_type.upper() for x in ["DI", "DIGITAL_IN"]):
            return "DI"
        elif any(x in device_type.upper() for x in ["DO", "DIGITAL_OUT"]):
            return "DO"
        elif any(x in device_type.upper() for x in ["AI", "ANALOG_IN"]):
            return "AI"
        elif any(x in device_type.upper() for x in ["AO", "ANALOG_OUT"]):
            return "AO"
        elif "PLC" in device_type.upper():
            # 从 PLC 属性推断
            plc_io_type = device.GetProperty("20001").GetValue() if device.GetProperty("20001") else ""
            if plc_io_type:
                return plc_io_type
        
        return ""
    
    def _extract_address(self, device) -> str:
        """提取物理地址"""
        # 尝试从不同属性获取地址
        address_properties = ["20002", "20003", "20004", "ADDRESS", "PLC_ADDRESS"]
        
        for prop_name in address_properties:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        # 从设备名称推断
        device_name = device.GetProperty("DP").GetValue() if device.GetProperty("DP") else ""
        if any(x in device_name.upper() for x in ["I", "Q", "M", "AI", "AQ"]):
            # 简单正则匹配地址模式
            import re
            match = re.search(r'[IQMA][0-9]+\.[0-9]+|[AIQ]W[0-9]+', device_name.upper())
            if match:
                return match.group()
        
        return ""
    
    def _extract_description(self, device) -> str:
        """提取功能描述"""
        desc_properties = ["20005", "20006", "FUNCTION_TEXT", "DESCRIPTION"]
        
        for prop_name in desc_properties:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        return device.GetProperty("DP").GetValue() if device.GetProperty("DP") else ""
    
    def _extract_cable_number(self, device) -> str:
        """提取电缆编号"""
        cable_props = ["20007", "CABLE_NUMBER", "WIRE_CABLE"]
        
        for prop_name in cable_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        return ""
    
    def _extract_terminal_number(self, device) -> str:
        """提取端子号"""
        terminal_props = ["20008", "TERMINAL_NUMBER", "TERMINAL"]
        
        for prop_name in terminal_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        return ""
    
    def _extract_wire_number(self, device) -> str:
        """提取线号"""
        wire_props = ["20009", "WIRE_NUMBER", "WIRE"]
        
        for prop_name in wire_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        return ""
    
    def _extract_page_reference(self, device) -> str:
        """提取图纸页参考"""
        page_props = ["20010", "PAGE_REFERENCE", "PAGE"]
        
        for prop_name in page_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        # 从设备位置获取
        location = device.GetLocation()
        if location:
            return f"Page {location.Page}"
        
        return ""
    
    def _extract_plc_module(self, device) -> str:
        """提取 PLC 模块型号"""
        module_props = ["20011", "PLC_MODULE", "MODULE_TYPE"]
        
        for prop_name in module_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        return ""
    
    def _extract_rack_slot(self, device) -> str:
        """提取机架/插槽位置"""
        rack_props = ["20012", "RACK_SLOT", "SLOT"]
        
        for prop_name in rack_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        return ""
    
    def _extract_comment(self, device) -> str:
        """提取备注"""
        comment_props = ["20013", "COMMENT", "REMARK"]
        
        for prop_name in comment_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        return ""
    
    def _determine_data_type(self, io_type: str) -> str:
        """确定数据类型"""
        data_type_map = {
            "DI": "BOOL",
            "DO": "BOOL",
            "AI": "REAL",
            "AO": "REAL"
        }
        return data_type_map.get(io_type, "UNKNOWN")
    
    def _extract_scaling_factor(self, device) -> float:
        """提取缩放系数"""
        scaling_props = ["20014", "SCALING_FACTOR", "SCALE"]
        
        for prop_name in scaling_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                try:
                    return float(prop.GetValue())
                except:
                    pass
        
        # 默认值
        io_type = self._determine_io_type(device)
        if io_type in ["AI", "AO"]:
            return 1.0  # 模拟量默认缩放系数
        return 1.0
    
    def _extract_engineering_unit(self, device) -> str:
        """提取工程单位"""
        unit_props = ["20015", "ENGINEERING_UNIT", "UNIT"]
        
        for prop_name in unit_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                return prop.GetValue()
        
        # 根据信号类型推断
        signal_name = device.GetProperty("DP").GetValue() if device.GetProperty("DP") else ""
        
        unit_map = {
            "TEMP": "°C",
            "PRESSURE": "Bar",
            "FLOW": "L/min",
            "LEVEL": "mm",
            "SPEED": "RPM",
            "CURRENT": "A",
            "VOLTAGE": "V",
            "POWER": "kW",
            "FORCE": "N",
            "TORQUE": "Nm"
        }
        
        for key, unit in unit_map.items():
            if key in signal_name.upper():
                return unit
        
        return ""
    
    def _extract_alarm_config(self, device) -> Dict:
        """提取报警配置"""
        alarm_config = {
            "enabled": False,
            "high_alarm": 0.0,
            "high_warning": 0.0,
            "low_warning": 0.0,
            "low_alarm": 0.0,
            "deadband": 0.0,
            "delay": 0,
            "priority": "LOW"
        }
        
        # 尝试从属性获取报警配置
        alarm_props = ["20016", "ALARM_CONFIG", "ALARM"]
        
        for prop_name in alarm_props:
            prop = device.GetProperty(prop_name)
            if prop and prop.GetValue():
                try:
                    config_data = json.loads(prop.GetValue())
                    alarm_config.update(config_data)
                    alarm_config["enabled"] = True
                except:
                    pass
        
        return alarm_config
    
    def _filter_io_addresses(self, io_addresses: List[IOAddress], criteria: Dict) -> List[IOAddress]:
        """过滤 IO 地址"""
        filtered = []
        
        for io in io_addresses:
            include = True
            
            # IO 类型过滤
            if "io_type" in criteria and criteria["io_type"]:
                if io.io_type not in criteria["io_type"]:
                    include = False
            
            # PLC 模块过滤
            if "plc_module" in criteria and criteria["plc_module"]:
                if io.plc_module not in criteria["plc_module"]:
                    include = False
            
            # 页面过滤
            if "page_reference" in criteria and criteria["page_reference"]:
                if criteria["page_reference"] not in io.page_reference:
                    include = False
            
            if include:
                filtered.append(io)
        
        return filtered

# 使用示例
def generate_io_mapping_report():
    """claw-code 生成的 IO 映射报告脚本"""
    script_template = '''#!/usr/bin/env python3
"""
自动生成的 IO 地址映射报告脚本
生成时间: {timestamp}
EPLAN 项目: {project_name}
"""

import os
import sys
import json
import pandas as pd
from pathlib import Path
from datetime import datetime

# 添加自定义模块路径
sys.path.append(r"{module_path}")

from electrical_automation.eplan_io_extractor import EplanIOExt