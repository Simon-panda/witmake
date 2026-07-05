#!/bin/bash
# 安全磁盘修复脚本
# 尝试非破坏性方法修复My Passport只读问题

set -e  # 遇到错误退出

echo "🔧 My Passport磁盘安全修复工具"
echo "================================="
echo "此脚本尝试非破坏性方法修复只读问题"
echo "不会删除或修改磁盘上的现有文件"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查磁盘是否挂载
check_disk_mounted() {
    echo "📋 步骤1: 检查磁盘挂载状态..."
    if [ -d "/Volumes/My Passport" ]; then
        echo -e "${GREEN}✓ My Passport已挂载${NC}"
        return 0
    else
        echo -e "${RED}✗ My Passport未挂载${NC}"
        return 1
    fi
}

# 检查磁盘空间
check_disk_space() {
    echo ""
    echo "📋 步骤2: 检查磁盘空间..."
    if df -h "/Volumes/My Passport" &>/dev/null; then
        df -h "/Volumes/My Passport"
    else
        echo -e "${YELLOW}⚠ 无法获取磁盘空间信息${NC}"
    fi
}

# 创建备份提醒
create_backup_reminder() {
    echo ""
    echo "📋 步骤3: 备份提醒..."
    echo -e "${YELLOW}⚠ 重要：在继续之前，请备份重要数据${NC}"
    echo "建议备份位置："
    echo "  1. ~/Desktop/MyPassport_Backup/"
    echo "  2. 另一个外部硬盘"
    echo "  3. 云存储"
    echo ""
    read -p "是否已备份重要数据？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}⚠ 建议先备份数据再继续${NC}"
        echo "创建备份目录示例："
        echo "  mkdir -p ~/Desktop/MyPassport_Backup"
        echo "  cp -r \"/Volumes/My Passport/重要文件夹\" ~/Desktop/MyPassport_Backup/"
    else
        echo -e "${GREEN}✓ 已确认备份${NC}"
    fi
}

# 尝试修复方法1：检查文件系统
try_fix_method1() {
    echo ""
    echo "🔧 方法1: 检查文件系统..."
    echo "尝试以只读模式检查文件系统（不修改）..."
    
    # 查找磁盘设备
    DISK_DEVICE=$(df "/Volumes/My Passport" 2>/dev/null | tail -1 | awk '{print $1}')
    
    if [ -n "$DISK_DEVICE" ]; then
        echo "找到磁盘设备: $DISK_DEVICE"
        echo "运行文件系统检查（只读模式）..."
        # 这里本应运行fsck，但需要sudo权限
        echo -e "${YELLOW}⚠ 需要sudo权限运行fsck，跳过此步骤${NC}"
    else
        echo -e "${YELLOW}⚠ 无法确定磁盘设备${NC}"
    fi
}

# 尝试修复方法2：重新挂载
try_fix_method2() {
    echo ""
    echo "🔧 方法2: 重新挂载尝试..."
    echo "注意：需要sudo权限"
    echo ""
    echo "建议手动操作："
    echo "  1. 在Finder中弹出'My Passport'"
    echo "  2. 等待10秒"
    echo "  3. 重新插入硬盘"
    echo "  4. 检查是否可写"
}

# 尝试修复方法3：权限修复
try_fix_method3() {
    echo ""
    echo "🔧 方法3: 权限检查..."
    echo "当前权限："
    ls -ld "/Volumes/My Passport"
    
    echo ""
    echo "测试写入权限："
    TEST_FILE="/Volumes/My Passport/.write_test_$(date +%s)"
    if touch "$TEST_FILE" 2>/dev/null; then
        echo -e "${GREEN}✓ 磁盘可写！删除测试文件...${NC}"
        rm "$TEST_FILE"
    else
        echo -e "${RED}✗ 磁盘只读${NC}"
    fi
}

# 提供解决方案建议
provide_solutions() {
    echo ""
    echo "💡 解决方案建议："
    echo "================================="
    
    echo "1. ${GREEN}安装NTFS驱动（最推荐）${NC}"
    echo "   如果磁盘是NTFS格式："
    echo "   - brew install --cask mounty"
    echo "   - 或购买Tuxera/Paragon NTFS"
    
    echo ""
    echo "2. ${YELLOW}使用磁盘工具${NC}"
    echo "   - 打开'磁盘工具'应用"
    echo "   - 选择My Passport"
    echo "   - 点击'急救' → '验证磁盘'"
    echo "   - 如有问题，点击'修复磁盘'"
    
    echo ""
    echo "3. ${RED}重新格式化（最后手段）${NC}"
    echo "   - 必须先备份所有数据！"
    echo "   - 格式选择exFAT（兼容macOS/Windows）"
    echo "   - 在磁盘工具中点击'抹掉'"
}

# 创建临时工作区
create_temp_workspace() {
    echo ""
    echo "🔄 创建临时工作区..."
    TEMP_DIR="$HOME/Desktop/ai2026_temp"
    if [ ! -d "$TEMP_DIR" ]; then
        mkdir -p "$TEMP_DIR"
        echo -e "${GREEN}✓ 创建临时工作区: $TEMP_DIR${NC}"
        echo "您可以在此文件夹中工作，等磁盘修复后复制到My Passport"
    else
        echo -e "${YELLOW}⚠ 临时工作区已存在: $TEMP_DIR${NC}"
    fi
}

# 主函数
main() {
    echo "开始修复流程..."
    echo ""
    
    # 检查磁盘
    if ! check_disk_mounted; then
        echo "请先插入My Passport硬盘"
        exit 1
    fi
    
    # 执行检查
    check_disk_space
    create_backup_reminder
    
    # 尝试修复方法
    try_fix_method1
    try_fix_method2
    try_fix_method3
    
    # 提供解决方案
    provide_solutions
    
    # 创建临时工作区
    create_temp_workspace
    
    echo ""
    echo "================================="
    echo "🔧 修复流程完成"
    echo ""
    echo "📁 创建的文件："
    echo "  - ~/Desktop/fix_disk_readonly.sh (诊断脚本)"
    echo "  - ~/Desktop/MyPassport修复指南.md (详细指南)"
    echo "  - ~/Desktop/safe_disk_repair.sh (本脚本)"
    echo "  - ~/Desktop/ai2026_temp/ (临时工作区)"
    echo ""
    echo "⚠ 如果问题仍然存在，建议："
    echo "  1. 在Windows电脑上测试磁盘"
    echo "  2. 联系Western Digital技术支持"
    echo "  3. 考虑使用其他硬盘暂时替代"
    echo ""
    echo "祝您修复顺利！"
}

# 运行主函数
main