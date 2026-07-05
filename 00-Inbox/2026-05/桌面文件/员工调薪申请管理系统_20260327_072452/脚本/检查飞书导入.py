#!/usr/bin/env python3
"""
检查CSV文件格式，确保可以正确导入飞书多维表格
"""

import csv
import sys

def check_csv_file(filename):
    """检查CSV文件格式"""
    print(f"\n检查文件: {filename}")
    print("=" * 50)
    
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            # 读取前几行
            lines = f.readlines()
            
            if not lines:
                print("错误: 文件为空")
                return False
            
            # 检查编码
            print(f"文件编码: UTF-8 with BOM" if lines[0].startswith('\ufeff') else "文件编码: UTF-8")
            
            # 检查行数
            print(f"总行数: {len(lines)}")
            
            # 检查列数
            reader = csv.reader(lines)
            headers = next(reader)
            print(f"列数: {len(headers)}")
            print(f"列名: {headers}")
            
            # 检查数据行
            data_rows = list(reader)
            print(f"数据行数: {len(data_rows)}")
            
            if data_rows:
                print("\n第一行数据示例:")
                for i, (header, value) in enumerate(zip(headers, data_rows[0])):
                    print(f"  {header}: {value}")
            
            # 检查特殊字符
            special_chars = 0
            for line in lines:
                for char in line:
                    if ord(char) > 127 and char not in '，。！？；：""''':
                        special_chars += 1
            
            if special_chars > 0:
                print(f"\n警告: 发现 {special_chars} 个特殊字符")
            
            return True
            
    except Exception as e:
        print(f"错误: {e}")
        return False

def main():
    """主函数"""
    print("飞书多维表格CSV文件格式检查")
    print("=" * 60)
    
    files_to_check = [
        "数据文件/员工基本信息表.csv",
        "数据文件/调薪申请记录表.csv",
        "数据文件/部门统计表.csv"
    ]
    
    all_ok = True
    for file in files_to_check:
        if not check_csv_file(file):
            all_ok = False
    
    print("\n" + "=" * 60)
    if all_ok:
        print("✓ 所有文件格式检查通过，可以导入飞书多维表格")
        print("\n导入建议:")
        print("1. 在飞书多维表格中创建对应表")
        print("2. 点击'导入' → '从CSV文件导入'")
        print("3. 选择对应的CSV文件")
        print("4. 确认字段映射关系")
        print("5. 点击'导入'")
    else:
        print("✗ 部分文件存在问题，请检查后重新生成")
    
    print("\n常见问题解决:")
    print("1. 编码问题: 确保使用UTF-8 with BOM编码")
    print("2. 分隔符问题: 确保使用逗号分隔")
    print("3. 特殊字符: 避免使用飞书不支持的字符")
    print("4. 空行问题: 确保没有多余的空行")

if __name__ == "__main__":
    main()
