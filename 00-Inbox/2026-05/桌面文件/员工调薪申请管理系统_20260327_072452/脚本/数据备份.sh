#!/bin/bash
# 数据备份脚本

BACKUP_DIR="../备份/备份_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "开始备份数据..."
cp -r "数据文件" "$BACKUP_DIR/"
cp "系统配置.json" "$BACKUP_DIR/"
cp "使用说明.txt" "$BACKUP_DIR/"

echo "备份完成: $BACKUP_DIR"
echo "备份文件:"
find "$BACKUP_DIR" -type f -name "*.csv" -o -name "*.json" -o -name "*.txt" | sort
