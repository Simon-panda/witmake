#!/usr/bin/env python3
"""
员工调薪申请管理系统 - 简化版模拟器
无需外部依赖
"""

import datetime
import json
import csv
from typing import Dict, List, Any

class SimpleSalarySystem:
    """简化版薪资系统"""
    
    def __init__(self):
        self.employees = []
        self.salary_adjustments = []
        self.departments = ['质保部', '生产部', '技术部', '行政部', '财务部']
    
    def add_employee(self, employee_data: Dict[str, Any]) -> str:
        """添加员工"""
        employee_id = employee_data.get('员工ID')
        if not employee_id:
            # 自动生成员工ID
            name = employee_data['姓名']
            join_date = employee_data['入职日期'].replace('.', '')
            employee_id = f"{name[:2]}{join_date}"
            employee_data['员工ID'] = employee_id
        
        employee_data['创建时间'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        employee_data['更新时间'] = employee_data['创建时间']
        
        self.employees.append(employee_data)
        return employee_id
    
    def add_salary_adjustment(self, adjustment_data: Dict[str, Any]) -> str:
        """添加调薪申请"""
        # 自动生成申请ID
        today = datetime.datetime.now().strftime('%Y%m%d')
        seq_num = len(self.salary_adjustments) + 1
        application_id = f"SA{today}-{seq_num:03d}"
        adjustment_data['申请ID'] = application_id
        
        # 计算调薪金额和比例
        old_salary = float(adjustment_data.get('调整前薪资', 0))
        new_salary = float(adjustment_data.get('调整后薪资', 0))
        adjustment_amount = new_salary - old_salary
        adjustment_ratio = (adjustment_amount / old_salary * 100) if old_salary > 0 else 0
        
        adjustment_data['调薪金额'] = adjustment_amount
        adjustment_data['调薪比例'] = f"{adjustment_ratio:.2f}%"
        adjustment_data['创建时间'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        self.salary_adjustments.append(adjustment_data)
        return application_id
    
    def calculate_department_stats(self) -> List[Dict[str, Any]]:
        """计算部门统计信息"""
        stats = []
        
        for dept in self.departments:
            # 筛选部门员工
            dept_employees = [emp for emp in self.employees if emp.get('部门') == dept]
            
            if dept_employees:
                # 计算薪资统计
                total_salary = 0
                salaries = []
                
                for emp in dept_employees:
                    base_salary = float(emp.get('基本薪资', 0))
                    performance = float(emp.get('绩效基数', 0))
                    total = base_salary + performance
                    total_salary += total
                    salaries.append(total)
                
                avg_salary = total_salary / len(dept_employees)
                max_salary = max(salaries) if salaries else 0
                min_salary = min(salaries) if salaries else 0
                
                # 计算部门调薪统计
                dept_adjustments = []
                for adj in self.salary_adjustments:
                    emp_id = adj.get('员工ID')
                    # 查找员工所属部门
                    emp_dept = None
                    for emp in self.employees:
                        if emp.get('员工ID') == emp_id:
                            emp_dept = emp.get('部门')
                            break
                    
                    if emp_dept == dept:
                        dept_adjustments.append(adj)
                
                # 计算调薪总额和平均比例
                total_adjustment = sum([adj.get('调薪金额', 0) for adj in dept_adjustments])
                
                adjustment_ratios = []
                for adj in dept_adjustments:
                    ratio_str = adj.get('调薪比例', '0%')
                    ratio = float(ratio_str.replace('%', ''))
                    adjustment_ratios.append(ratio)
                
                avg_adjustment_ratio = sum(adjustment_ratios) / len(adjustment_ratios) if adjustment_ratios else 0
                
                stats.append({
                    '部门': dept,
                    '员工数量': len(dept_employees),
                    '平均薪资': round(avg_salary, 2),
                    '最高薪资': max_salary,
                    '最低薪资': min_salary,
                    '年度调薪总额': total_adjustment,
                    '平均调薪比例': f"{avg_adjustment_ratio:.2f}%"
                })
        
        return stats
    
    def export_to_csv(self):
        """导出为CSV文件"""
        # 导出员工信息
        if self.employees:
            with open('employee_info_simple.csv', 'w', newline='', encoding='utf-8-sig') as f:
                fieldnames = self.employees[0].keys() if self.employees else []
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.employees)
            print(f"员工信息已导出到: employee_info_simple.csv ({len(self.employees)}条记录)")
        
        # 导出调薪记录
        if self.salary_adjustments:
            with open('salary_adjustment_simple.csv', 'w', newline='', encoding='utf-8-sig') as f:
                fieldnames = self.salary_adjustments[0].keys() if self.salary_adjustments else []
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.salary_adjustments)
            print(f"调薪记录已导出到: salary_adjustment_simple.csv ({len(self.salary_adjustments)}条记录)")
        
        # 导出部门统计
        dept_stats = self.calculate_department_stats()
        if dept_stats:
            with open('department_stats_simple.csv', 'w', newline='', encoding='utf-8-sig') as f:
                fieldnames = dept_stats[0].keys() if dept_stats else []
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(dept_stats)
            print(f"部门统计已导出到: department_stats_simple.csv")

def main():
    """主函数"""
    print("=" * 60)
    print("员工调薪申请管理系统 - 简化版模拟器")
    print("=" * 60)
    
    # 创建模拟器实例
    system = SimpleSalarySystem()
    
    # 添加陈永灯示例数据
    print("\n1. 添加示例员工数据...")
    chen_data = {
        '姓名': '陈永灯',
        '部门': '质保部',
        '职位': '外检（来料检）',
        '入职日期': '2023.4.2',
        '基本薪资': '2740',
        '绩效基数': '500',
        '加班费标准': '按公司规定',
        '在职状态': '在职'
    }
    chen_id = system.add_employee(chen_data)
    print(f"   员工添加成功: {chen_data['姓名']} (ID: {chen_id})")
    
    # 添加调薪申请
    print("\n2. 添加调薪申请记录...")
    adjustment_data = {
        '员工ID': chen_id,
        '申请日期': '2026.3.6',
        '生效日期': '2026.1.1',
        '调薪类型': '绩效调整',
        '调整前职位': '外检',
        '调整后职位': '外检（来料检）',
        '调整前薪资': '2740',
        '调整后薪资': '3240',
        '申请理由': '陈永灯负责缸体检验，严格执行标准，无重大质量问题',
        '员工表现': '工作期间态度认真，服从安排，积极学习新岗位技能，并能主动帮助同事',
        '审批状态': '已批准',
        '审批人': '郑华钦',
        '审批日期': '2026.3.7',
        '审批意见': '同意，勉励其在新的任务中继续努力，有所作为'
    }
    app_id = system.add_salary_adjustment(adjustment_data)
    print(f"   调薪申请添加成功: {app_id}")
    
    old_salary = float(adjustment_data['调整前薪资'])
    new_salary = float(adjustment_data['调整后薪资'])
    adjustment_amount = new_salary - old_salary
    adjustment_ratio = (adjustment_amount / old_salary * 100) if old_salary > 0 else 0
    
    print(f"   调薪金额: {adjustment_amount}元")
    print(f"   调薪比例: {adjustment_ratio:.2f}%")
    
    # 显示系统状态
    print("\n3. 系统状态报告...")
    print(f"   员工总数: {len(system.employees)}")
    print(f"   调薪申请总数: {len(system.salary_adjustments)}")
    print(f"   部门数量: {len(system.departments)}")
    
    # 显示部门统计
    print("\n4. 部门统计信息...")
    dept_stats = system.calculate_department_stats()
    for stat in dept_stats:
        if stat['员工数量'] > 0:
            print(f"\n  部门: {stat['部门']}")
            print(f"    员工数量: {stat['员工数量']}")
            print(f"    平均薪资: {stat['平均薪资']}元")
            print(f"    最高薪资: {stat['最高薪资']}元")
            print(f"    最低薪资: {stat['最低薪资']}元")
            print(f"    年度调薪总额: {stat['年度调薪总额']}元")
            print(f"    平均调薪比例: {stat['平均调薪比例']}")
    
    # 导出数据
    print("\n5. 导出数据文件...")
    system.export_to_csv()
    
    # 生成详细报告
    report = {
        '生成时间': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        '系统状态': '运行正常',
        '数据统计': {
            '员工总数': len(system.employees),
            '调薪申请总数': len(system.salary_adjustments),
            '部门数量': len(system.departments)
        },
        '员工列表': system.employees,
        '调薪记录': system.salary_adjustments,
        '部门统计': dept_stats
    }
    
    with open('system_simple_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"测试报告已保存到: system_simple_report.json")
    
    print("\n" + "=" * 60)
    print("模拟完成！")
    print("=" * 60)
    print("\n生成的文件:")
    print("  1. employee_info_simple.csv - 员工信息表")
    print("  2. salary_adjustment_simple.csv - 调薪申请记录表")
    print("  3. department_stats_simple.csv - 部门统计表")
    print("  4. system_simple_report.json - 系统测试报告")
    print("\n这些文件可以直接导入到飞书多维表格中。")
    
    # 显示导入说明
    print("\n" + "=" * 60)
    print("飞书多维表格导入说明:")
    print("=" * 60)
    print("""
1. 登录飞书，进入"工作台"
2. 创建"多维表格"应用，名称: "员工调薪申请管理系统"
3. 创建"员工基本信息表"，然后点击"导入" → "从CSV文件导入"
4. 选择 employee_info_simple.csv 文件
5. 创建"调薪申请记录表"，导入 salary_adjustment_simple.csv
6. 配置字段类型和公式（参考详细指南）
    """)

if __name__ == "__main__":
    main()