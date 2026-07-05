macOS 终端开发命令速查手册（超全详细版）

本手册整合 macOS 日常操作、文件管理、网络调试、进程排查、权限配置、Brew/NPM 开发工具全套命令，**全覆盖、无废话、可直接复制使用**，适合开发常驻备忘录。

## 一、基础路径与目录命令

### 1. pwd（查看当前路径）

**作用**：打印当前所在的绝对路径

```bash
pwd
```

### 2. ls（列出目录文件）

**作用**：查看当前目录下文件/文件夹

**常用参数**：

- `-a`：显示所有文件（包含隐藏文件 `.` 开头）
    
- `-l`：展示详细信息（权限、大小、时间、所有者）
    
- `-h`：人性化单位展示文件大小
    

```bash
ls          # 基础展示
ls -la      # 最常用：详细+隐藏文件
ls -alh     # 详细、隐藏、单位友好
```

### 3. cd（切换目录）

**作用**：跳转工作目录

```bash
cd ~        # 回到用户根目录
cd /        # 回到系统根目录
cd ..       # 返回上一级目录
cd ../..    # 返回上两级目录
cd -        # 回到上一次访问的目录
cd Desktop  # 进入桌面
```

## 二、文件与文件夹操作命令

### 4. mkdir（新建文件夹）

```bash
mkdir test              # 新建单层文件夹
mkdir -p a/b/c/d        # 递归创建多层文件夹（重点：-p 不存在则创建，存在不报错）
```

### 5. touch（新建空文件）

**作用**：创建空白文件，也可更新文件修改时间

```bash
touch index.js
touch .env              # 创建隐藏配置文件
```

### 6. cat（读取文件内容）

**作用**：查看小型文本文件全部内容

```bash
cat README.md
cat /etc/hosts
```

### 7. cp（复制文件/文件夹）

```bash
cp file1.txt file2.txt          # 复制文件
cp -r folder1 folder2           # 复制整个文件夹（文件夹必须加 -r）
```

### 8. mv（移动/重命名）

```bash
mv old.txt new.txt              # 文件重命名
mv file.txt ~/Desktop           # 移动文件到桌面
mv folder ~/Downloads           # 移动文件夹
```

### 9. rm（删除文件/文件夹）

**高危警告**：终端删除**不可恢复**，禁止随意执行`rm -rf /`

```bash
rm file.txt                     # 删除单个文件
rm -r folder                    # 删除文件夹
rm -rf folder                   # 强制彻底删除，无弹窗提示
```

## 三、文件查找与筛选命令

### 10. find（全局查找文件）

```bash
find ~ -name "*.json"           # 用户目录查找所有json文件
find . -name "*.log"            # 当前目录查找所有日志文件
find . -name "*.log" -delete    # 批量删除当前目录所有log文件
```

### 11. grep（文本关键词筛选）

```bash
ls -la | grep D                 # 筛选目录文件夹
cat app.log | grep error        # 过滤日志错误信息
grep -rn "token" .              # 全局搜索包含token的文件内容
```

## 四、权限与管理员命令

### 12. sudo（临时管理员权限）

**作用**：临时获取系统最高权限，输入开机密码生效

```bash
sudo cat /etc/hosts
sudo rm -rf /opt/test
```

### 13. chmod（修改文件权限）

```bash
chmod +x run.sh                 # 给脚本添加执行权限
sudo chmod -R 755 folder        # 递归赋予文件夹读写执行权限
```

## 五、进程与端口排查（开发高频）

### 14. ps（查看系统进程）

```bash
ps aux                          # 查看全部进程
ps aux | grep node              # 筛选node进程
ps aux | grep python            # 筛选python进程
```

### 15. kill（结束进程）

```bash
kill 进程ID                     # 正常结束进程
kill -9 进程ID                  # 强制杀死进程（强制终止）
```

### 16. lsof（端口占用查询）

```bash
lsof -i :3000                   # 查询3000端口占用程序
lsof -i :8080
kill -9 $(lsof -t -i:3000)      # 一键杀死3000端口进程
```

### 17. netstat（网络端口统计）

```bash
netstat -an | grep LISTEN       # 查看所有正在监听的端口
```

## 六、网络调试命令

### 18. ping（测试网络连通性）

```bash
ping www.baidu.com              # 持续ping测试
ping -c 4 www.baidu.com         # 只ping4次，自动停止
```

### 19. curl（接口/网络请求）

```bash
curl https://www.baidu.com              # 基础GET请求
curl -I https://api.xxx.com             # 仅获取接口响应头（查状态码）
curl -H "Token: 123456" https://api.xxx.com # 自定义请求头
```

## 七、系统工具命令

### 20. which（查询软件安装路径）

**作用**：区分系统自带软件 & Brew安装软件

```bash
which curl
which brew
which node
which npm
```

### 21. du（查看文件/文件夹大小）

```bash
du -sh                          # 查看当前目录总大小
du -sh ~/Desktop                # 查看桌面文件夹大小
```

### 22. man（命令官方手册）

**作用**：查询任意命令官方详细文档

```bash
man curl
man ls
man brew
```

### 23. clear（清空终端）

```bash
clear
```

### 24. uname（查看系统信息）

```bash
uname -a                        # 查看系统内核、版本信息
```

## 八、压缩解压命令

```bash
unzip file.zip                  # 解压zip压缩包
tar -zxvf file.tar.gz           # 解压tar.gz压缩包
tar -czvf file.tar.gz folder    # 压缩文件夹为tar.gz
```

## 九、Homebrew 专属命令（Mac 必备）

```bash
brew install 软件名             # 安装软件
brew uninstall 软件名           # 卸载软件
brew update                     # 更新brew软件源
brew upgrade                    # 升级所有已安装软件
brew list                       # 查看已安装全部软件
brew cleanup                    # 清理缓存、冗余安装包
brew doctor                     # 检测brew环境问题
```

## 十、NPM 前端开发专属命令

```bash
npm init                        # 初始化项目
npm install                     # 安装项目全部依赖
npm install 包名                # 安装第三方依赖
npm run 脚本名                  # 执行package.json脚本
npm uninstall 包名             # 卸载依赖
npm cache clean --force        # 强制清空npm缓存
npm root -g                    # 查看全局依赖安装路径
```

## 十一、核心目录概念复盘（配套记忆）

- `/`：系统根目录，最高层级
    
- `~`：用户个人家目录（/Users/用户名）
    
- `/opt`：第三方大型独立软件目录
    
- `/usr/local`：Brew 默认安装目录
    
- `/etc`：系统所有配置文件目录
    
- `/var`：日志、缓存、动态数据目录
    
- `/tmp`：系统临时文件目录（重启清空）
    

## 十二、新手避坑重点

1. **绝对不要执行**：`rm -rf /`、`sudo rm -rf /`，会销毁系统文件
    
2. `绝对路径`：以 `/` 开头，全局通用
    
3. `相对路径`：不以 `/` 开头，依赖当前目录
    
4. 所有带 `-r` 参数的命令，均针对文件夹操作
    
5. `sudo` 权限谨慎使用，仅用于修改系统资源