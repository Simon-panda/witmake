#!/usr/bin/env python3
"""
从Excel文件中提取数据并转换为markdown格式
"""

import zipfile
import xml.etree.ElementTree as ET
import re
import os
from datetime import datetime

def parse_sheet_data(xlsx_path, sheet_num=1):
    """解析指定sheet的数据"""
    try:
        with zipfile.ZipFile(xlsx_path, 'r') as z:
            # 读取sharedStrings.xml获取所有文本
            shared_strings = []
            if 'xl/sharedStrings.xml' in z.namelist():
                with z.open('xl/sharedStrings.xml') as f:
                    content = f.read().decode('utf-8')
                    # 提取所有文本
                    shared_strings = re.findall(r'<t[^>]*>([^<]+)</t>', content)
            
            # 读取指定sheet的XML
            sheet_file = f'xl/worksheets/sheet{sheet_num}.xml'
            if sheet_file not in z.namelist():
                return []
            
            with z.open(sheet_file) as f:
                sheet_content = f.read().decode('utf-8')
            
            # 解析sheet数据
            rows = []
            
            # 简单解析 - 查找所有单元格
            cell_pattern = r'<c r="([A-Z]+)(\d+)"[^>]*>.*?<v>([^<]+)</v>'
            matches = re.findall(cell_pattern, sheet_content, re.DOTALL)
            
            # 组织数据
            max_row = 0
            max_col = 0
            cells = {}
            
            for col_letter, row_num, value_idx in matches:
                row = int(row_num)
                col = col_letter_to_index(col_letter)
                
                # 更新最大行列
                max_row = max(max_row, row)
                max_col = max(max_col, col)
                
                # 获取实际文本值
                try:
                    value_idx = int(value_idx)
                    if value_idx < len(shared_strings):
                        value = shared_strings[value_idx]
                    else:
                        value = str(value_idx)
                except:
                    value = value_idx
                
                cells[(row, col)] = value
            
            # 将数据组织成表格
            for row in range(1, max_row + 1):
                row_data = []
                for col in range(1, max_col + 1):
                    row_data.append(cells.get((row, col), ''))
                if any(row_data):  # 只添加非空行
                    rows.append(row_data)
            
            return rows
            
    except Exception as e:
        print(f"解析sheet {sheet_num}时出错: {e}")
        return []

def col_letter_to_index(letter):
    """将列字母转换为数字索引（A=1, B=2, ...）"""
    index = 0
    for char in letter:
        index = index * 26 + (ord(char.upper()) - ord('A') + 1)
    return index

def extract_all_data(xlsx_path):
    """从所有sheet中提取数据"""
    all_data = []
    
    try:
        with zipfile.ZipFile(xlsx_path, 'r') as z:
            # 获取所有sheet
            sheet_files = [f for f in z.namelist() if f.startswith('xl/worksheets/sheet')]
            
            for sheet_file in sheet_files:
                sheet_num = int(sheet_file.replace('xl/worksheets/sheet', '').replace('.xml', ''))
                print(f"正在处理sheet {sheet_num}...")
                
                # 读取sheet名称
                sheet_name = get_sheet_name(xlsx_path, sheet_num)
                print(f"  Sheet名称: {sheet_name}")
                
                # 解析数据
                rows = parse_sheet_data(xlsx_path, sheet_num)
                
                if rows:
                    print(f"  找到 {len(rows)} 行数据")
                    
                    # 假设第一行是表头
                    if len(rows) > 0:
                        headers = rows[0]
                        print(f"  表头: {headers}")
                        
                        # 提取数据行
                        for i, row in enumerate(rows[1:], 1):
                            if len(row) >= 4:  # 至少需要4列数据
                                # 尝试匹配字段
                                record = {
                                    'sheet': sheet_name,
                                    'row': i
                                }
                                
                                # 根据表头映射字段
                                for j, header in enumerate(headers):
                                    if j < len(row):
                                        record[header] = row[j]
                                
                                all_data.append(record)
                
                print()
                
    except Exception as e:
        print(f"提取数据时出错: {e}")
    
    return all_data

def get_sheet_name(xlsx_path, sheet_num):
    """获取sheet名称"""
    try:
        with zipfile.ZipFile(xlsx_path, 'r') as z:
            with z.open('xl/workbook.xml') as f:
                content = f.read().decode('utf-8')
                root = ET.fromstring(content)
                
                ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                
                sheets = root.findall('.//ns:sheet', ns)
                for sheet in sheets:
                    if sheet.get('sheetId') == str(sheet_num):
                        return sheet.get('name')
    except:
        pass
    
    return f"Sheet{sheet_num}"

def convert_to_markdown(data):
    """将数据转换为markdown格式"""
    if not data:
        return "# 月度未完成事项统计\n\n暂无数据\n"
    
    # 提取所有可能的字段
    all_fields = set()
    for record in data:
        all_fields.update(record.keys())
    
    # 确定需要的字段
    required_fields = ['责任部门', '责任人', '会议时间', '未完成事项']
    available_fields = [f for f in required_fields if any(f in record for record in data)]
    
    # 如果没有找到标准字段，使用找到的字段
    if not available_fields:
        available_fields = [f for f in all_fields if f not in ['sheet', 'row']]
    
    markdown = "# 月度未完成事项统计\n\n"
    
    # 按sheet分组
    sheets = {}
    for record in data:
        sheet_name = record.get('sheet', '未知')
        if sheet_name not in sheets:
            sheets[sheet_name] = []
        sheets[sheet_name].append(record)
    
    for sheet_name, sheet_data in sheets.items():
        markdown += f"## {sheet_name}\n\n"
        
        # 创建表格
        if available_fields:
            # 表头
            markdown += "| " + " | ".join(available_fields) + " |\n"
            markdown += "|" + "|".join(["---"] * len(available_fields)) + "|\n"
            
            # 数据行
            for record in sheet_data:
                row = []
                for field in available_fields:
                    value = record.get(field, '')
                    # 清理值
                    if value is None:
                        value = ''
                    else:
                        value = str(value).strip()
                    row.append(value)
                markdown += "| " + " | ".join(row) + " |\n"
        
        markdown += "\n"
    
    return markdown

def main():
    xlsx_path = '绩效统计-月度未完成事项统计-2026.xlsx'
    
    if not os.path.exists(xlsx_path):
        print(f"文件不存在: {xlsx_path}")
        return
    
    print("正在提取Excel文件数据...")
    print("=" * 60)
    
    # 提取数据
    data = extract_all_data(xlsx_path)
    
    print(f"总共提取到 {len(data)} 条记录")
    print("=" * 60)
    
    if data:
        # 显示前几条记录
        print("\n前5条记录示例:")
        for i, record in enumerate(data[:5]):
            print(f"\n记录 {i+1}:")
            for key, value in record.items():
                print(f"  {key}: {value}")
        
        # 转换为markdown
        markdown_content = convert_to_markdown(data)
        
        # 保存markdown文件
        output_file = '月度未完成事项统计_整理后.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\nMarkdown文件已保存: {output_file}")
        
        # 显示部分内容
        print("\n生成的Markdown文件前部分内容:")
        print("=" * 60)
        lines = markdown_content.split('\n')[:30]
        for line in lines:
            print(line)
        
        if len(markdown_content.split('\n')) > 30:
            print("... (更多内容请查看完整文件)")
    
    else:
        print("未提取到数据")

if __name__ == "__main__":
    main()