#!/bin/bash
# 安全修复My Passport磁盘只读问题脚本
# 不会破坏任何文件

echo "=== My Passport磁盘只读问题修复脚本 ==="
echo "开始时间: $(date)"
echo ""

# 检查磁盘是否挂载
if [ ! -d "/Volumes/My Passport" ]; then
    echo "错误: My Passport磁盘未挂载"
    exit 1
fi

echo "1. 检查磁盘状态..."
DISK_INFO=$(df -h "/Volumes/My Passport" 2>/dev/null)
if [ $? -eq 0 ]; then
    echo "磁盘信息:"
    echo "$DISK_INFO"
else
    echo "无法获取磁盘信息"
fi

echo ""
echo "2. 检查文件权限..."
ls -ld "/Volumes/My Passport"
echo ""

echo "3. 尝试创建测试文件（预期会失败）..."
touch "/Volumes/My Passport/.test_write" 2>&1
if [ $? -eq 0 ]; then
    echo "✓ 磁盘可写，删除测试文件..."
    rm "/Volumes/My Passport/.test_write"
else
    echo "✗ 磁盘只读（预期中）"
fi

echo ""
echo "4. 可能的原因和解决方案:"
echo "   a) NTFS格式: macOS默认只读NTFS，需要安装NTFS驱动"
echo "   b) 文件系统错误: 需要修复文件系统"
echo "   c) 物理写保护: 检查硬盘上的物理开关"
echo "   d) 权限问题: 磁盘挂载为只读模式"
echo ""

echo "5. 安全建议:"
echo "   - 先备份重要数据到其他位置"
echo "   - 使用磁盘工具进行修复"
echo "   - 考虑重新格式化为exFAT（兼容macOS和Windows）"
echo "   - 安装NTFS for Mac驱动（如果是NTFS格式）"
echo ""

echo "6. 临时解决方案:"
echo "   - 使用桌面上的临时文件夹: ~/Desktop/temp_ai2026"
echo "   - 等解决只读问题后再移动到My Passport"
echo ""

echo "脚本完成于: $(date)"
echo "=== 结束 ==="