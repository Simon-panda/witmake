#!/usr/bin/env python3
"""
智能解析绩效统计Excel文件
专门处理"绩效统计-月度未完成事项统计-2026.xlsx"格式
"""

import zipfile
import re
import os
from collections import defaultdict

def extract_all_text(xlsx_path):
    """提取Excel中的所有文本"""
    all_text = []
    
    try:
        with zipfile.ZipFile(xlsx_path, 'r') as z:
            # 读取sharedStrings.xml
            if 'xl/sharedStrings.xml' in z.namelist():
                with z.open('xl/sharedStrings.xml') as f:
                    content = f.read().decode('utf-8')
                    # 提取所有文本项
                    texts = re.findall(r'<t[^>]*>([^<]+)</t>', content)
                    all_text = texts
                    
            # 读取所有sheet
            sheet_files = [f for f in z.namelist() if f.startswith('xl/worksheets/sheet')]
            
            sheet_texts = {}
            for sheet_file in sheet_files:
                sheet_num = int(sheet_file.replace('xl/worksheets/sheet', '').replace('.xml', ''))
                with z.open(sheet_file) as f:
                    sheet_content = f.read().decode('utf-8')
                    
                    # 提取单元格引用和值
                    cell_pattern = r'<c r="([A-Z]+)(\d+)"[^>]*>.*?<v>([^<]+)</v>'
                    cells = re.findall(cell_pattern, sheet_content, re.DOTALL)
                    
                    sheet_data = []
                    for col, row, val_idx in cells:
                        try:
                            val_idx = int(val_idx)
                            if val_idx < len(all_text):
                                value = all_text[val_idx]
                            else:
                                value = str(val_idx)
                        except:
                            value = val_idx
                        
                        sheet_data.append({
                            'row': int(row),
                            'col': col,
                            'value': value
                        })
                    
                    sheet_texts[sheet_num] = sheet_data
    
    except Exception as e:
        print(f"提取文本时出错: {e}")
    
    return all_text, sheet_texts

def analyze_sheet_structure(sheet_data):
    """分析sheet数据结构"""
    if not sheet_data:
        return None
    
    # 按行分组
    rows = defaultdict(list)
    for cell in sheet_data:
        rows[cell['row']].append(cell)
    
    # 按列排序
    for row_num in rows:
        rows[row_num].sort(key=lambda x: x['col'])
    
    # 转换为二维数组
    max_row = max(rows.keys()) if rows else 0
    table = []
    
    for row_num in range(1, max_row + 1):
        if row_num in rows:
            row_cells = rows[row_num]
            # 获取列值
            row_values = [cell['value'] for cell in row_cells]
            table.append(row_values)
        else:
            table.append([])
    
    return table

def find_data_section(table):
    """在表格中查找数据区域"""
    if not table:
        return None
    
    # 查找包含关键字段的行
    key_fields = ['责任部门', '责任人', '未完成事项', '会议时间', '备注']
    
    data_start = None
    headers = None
    
    for i, row in enumerate(table):
        if not row:
            continue
        
        # 检查是否包含表头
        row_text = ' '.join(str(cell) for cell in row)
        for field in key_fields:
            if field in row_text:
                if data_start is None:
                    data_start = i
                    headers = row
                break
    
    if data_start is None:
        # 如果没有找到标准表头，尝试其他模式
        for i, row in enumerate(table):
            if len(row) >= 3 and any('部' in str(cell) for cell in row[:3]):
                # 可能是数据行
                data_start = i
                # 猜测表头
                headers = ['会议时间', '责任部门', '责任人', '未完成事项', '备注']
                break
    
    return data_start, headers

def extract_records(table, data_start, headers):
    """从表格中提取记录"""
    records = []
    
    if data_start is None or not headers:
        return records
    
    # 从数据开始行提取
    for i in range(data_start, len(table)):
        row = table[i]
        if not row:
            continue
        
        # 跳过空行或表头行
        if i == data_start and any(h in str(cell) for cell in row for h in ['责任部门', '责任人']):
            continue
        
        # 尝试匹配数据模式
        # 模式1: 包含部门信息
        if len(row) >= 3:
            record = {}
            
            # 尝试识别字段
            for j, cell in enumerate(row):
                cell_str = str(cell).strip()
                if not cell_str:
                    continue
                
                # 根据内容猜测字段类型
                if j == 0 and ('.' in cell_str or '月' in cell_str or cell_str.replace('.', '').isdigit()):
                    record['日期'] = cell_str
                elif '部' in cell_str and len(cell_str) <= 10:
                    record['部门'] = cell_str
                elif len(cell_str) <= 5 and not any(c in cell_str for c in '0123456789.'):
                    record['人名'] = cell_str
                elif len(cell_str) > 20 or any(keyword in cell_str for keyword in ['未', '问题', '事件', '导致', '造成']):
                    if '未完成事项' not in record:
                        record['未完成事项'] = cell_str
                    else:
                        record['未完成事项'] += ' ' + cell_str
                elif '备注' in str(headers[j]) if j < len(headers) else False:
                    record['备注'] = cell_str
            
            # 如果找到了关键信息，添加到记录
            if '部门' in record and '人名' in record:
                # 确保有日期
                if '日期' not in record:
                    # 尝试从上一行获取日期
                    for prev_i in range(i-1, max(0, i-3), -1):
                        if prev_i < len(table) and table[prev_i]:
                            first_cell = str(table[prev_i][0]).strip()
                            if '.' in first_cell or first_cell.replace('.', '').isdigit():
                                record['日期'] = first_cell
                                break
                
                records.append(record)
    
    return records

def process_sheet(sheet_num, sheet_data):
    """处理单个sheet"""
    print(f"\n处理Sheet {sheet_num}:")
    
    # 分析表格结构
    table = analyze_sheet_structure(sheet_data)
    if not table:
        print("  无数据")
        return []
    
    print(f"  表格大小: {len(table)} 行")
    
    # 查找数据区域
    data_start, headers = find_data_section(table)
    
    if data_start is None:
        print("  未找到数据区域")
        # 显示前几行帮助调试
        print("  前5行内容:")
        for i, row in enumerate(table[:5]):
            print(f"    行{i+1}: {row}")
        return []
    
    print(f"  数据起始行: {data_start + 1}")
    print(f"  表头: {headers}")
    
    # 提取记录
    records = extract_records(table, data_start, headers)
    print(f"  提取到 {len(records)} 条记录")
    
    # 显示前几条记录
    if records:
        print("  前3条记录示例:")
        for i, record in enumerate(records[:3]):
            print(f"    记录{i+1}: {record}")
    
    return records

def create_markdown(records_by_sheet):
    """创建markdown格式的输出"""
    if not records_by_sheet:
        return "# 月度未完成事项统计\n\n暂无数据\n"
    
    markdown = "# 月度未完成事项统计\n\n"
    
    for sheet_name, records in records_by_sheet.items():
        if not records:
            continue
        
        markdown += f"## {sheet_name}\n\n"
        
        # 创建表格
        markdown += "| 部门 | 人名 | 日期 | 未完成事项 |\n"
        markdown += "|------|------|------|------------|\n"
        
        for record in records:
            department = record.get('部门', '')
            person = record.get('人名', '')
            date = record.get('日期', '')
            task = record.get('未完成事项', '')
            
            # 清理文本
            task = task.replace('\n', ' ').replace('\r', ' ').strip()
            
            markdown += f"| {department} | {person} | {date} | {task} |\n"
        
        markdown += "\n"
    
    return markdown

def main():
    xlsx_path = '绩效统计-月度未完成事项统计-2026.xlsx'
    
    if not os.path.exists(xlsx_path):
        print(f"文件不存在: {xlsx_path}")
        return
    
    print("正在智能解析Excel文件...")
    print("=" * 60)
    
    # 提取所有文本
    all_text, sheet_texts = extract_all_text(xlsx_path)
    print(f"总共找到 {len(all_text)} 个文本项")
    
    # 处理每个sheet
    all_records = {}
    sheet_names = {
        1: "2026年2月",
        2: "2026年3月",
        3: "其他"
    }
    
    for sheet_num in sorted(sheet_texts.keys()):
        sheet_name = sheet_names.get(sheet_num, f"Sheet{sheet_num}")
        records = process_sheet(sheet_num, sheet_texts[sheet_num])
        if records:
            all_records[sheet_name] = records
    
    print("\n" + "=" * 60)
    print(f"总共从 {len(all_records)} 个sheet中提取到数据")
    
    # 统计总记录数
    total_records = sum(len(records) for records in all_records.values())
    print(f"总记录数: {total_records}")
    
    if total_records > 0:
        # 创建markdown
        markdown_content = create_markdown(all_records)
        
        # 保存文件
        output_file = '绩效统计-月度未完成事项统计-整理版.md'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"\nMarkdown文件已保存: {output_file}")
        
        # 显示部分内容
        print("\n生成的内容预览:")
        print("=" * 60)
        lines = markdown_content.split('\n')[:30]
        for line in lines:
            print(line)
        
        if len(markdown_content.split('\n')) > 30:
            print("... (更多内容请查看完整文件)")
    
    else:
        print("未提取到有效数据")
        print("\n尝试手动查看Excel文件结构...")
        
        # 显示一些原始文本帮助调试
        print("\n前50个文本项:")
        for i, text in enumerate(all_text[:50]):
            print(f"{i+1:3d}: {text}")

if __name__ == "__main__":
    main()