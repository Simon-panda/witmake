#!/usr/bin/env python3
"""
简单读取Excel文件的脚本
"""

import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def read_excel_sheet_names(xlsx_path):
    """读取Excel文件的sheet名称"""
    try:
        with zipfile.ZipFile(xlsx_path, 'r') as z:
            # 读取workbook.xml获取sheet信息
            with z.open('xl/workbook.xml') as f:
                content = f.read().decode('utf-8')
                root = ET.fromstring(content)
                
                # 获取命名空间
                ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                
                sheets = []
                for sheet in root.findall('.//ns:sheet', ns):
                    name = sheet.get('name')
                    sheet_id = sheet.get('sheetId')
                    sheets.append({'name': name, 'id': sheet_id})
                
                return sheets
    except Exception as e:
        print(f"读取sheet名称时出错: {e}")
        return []

def read_excel_as_text(xlsx_path):
    """尝试以文本方式读取Excel文件"""
    try:
        # 首先尝试用zipfile查看内容
        with zipfile.ZipFile(xlsx_path, 'r') as z:
            file_list = z.namelist()
            print("Excel文件包含的文件:")
            for f in file_list[:20]:  # 只显示前20个文件
                print(f"  {f}")
            
            # 尝试读取sharedStrings.xml（包含文本内容）
            if 'xl/sharedStrings.xml' in file_list:
                print("\n尝试读取文本内容...")
                with z.open('xl/sharedStrings.xml') as f:
                    content = f.read().decode('utf-8')
                    # 简单提取文本
                    import re
                    texts = re.findall(r'<t[^>]*>([^<]+)</t>', content)
                    print(f"找到 {len(texts)} 个文本项")
                    print("前20个文本项:")
                    for i, text in enumerate(texts[:20]):
                        print(f"  {i+1}: {text}")
            
            return True
    except Exception as e:
        print(f"读取Excel文件时出错: {e}")
        return False

def main():
    xlsx_path = '绩效统计-月度未完成事项统计-2026.xlsx'
    
    if not os.path.exists(xlsx_path):
        print(f"文件不存在: {xlsx_path}")
        return
    
    print(f"正在分析文件: {xlsx_path}")
    print("=" * 60)
    
    # 读取sheet名称
    sheets = read_excel_sheet_names(xlsx_path)
    if sheets:
        print(f"找到 {len(sheets)} 个sheet:")
        for sheet in sheets:
            print(f"  Sheet {sheet['id']}: {sheet['name']}")
    else:
        print("无法读取sheet信息")
    
    print("\n" + "=" * 60)
    
    # 尝试读取文本内容
    read_excel_as_text(xlsx_path)
    
    print("\n" + "=" * 60)
    print("建议: 如果可能，请将Excel文件另存为CSV格式，以便更好地处理。")

if __name__ == "__main__":
    main()