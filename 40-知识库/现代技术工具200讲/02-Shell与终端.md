# 第2组: Shell 与终端

> Shell 是开发者与操作系统对话的语言，终端是这对话发生的窗口。本组的 10 个工具覆盖了从 Shell 本身、提示符美化、终端模拟器、会话管理到历史增强的完整链条。它们共同定义了一个高效、美观、功能丰富的命令行工作环境。

---

### 11. zsh

**前世今生**

Z shell (zsh) 由 Paul Falstad 于 1990 年在普林斯顿大学求学期间创建，名字取自当时耶鲁大学助教钟绍京（Zhong Shao）的登录名 "zsh"。zsh 最初的定位是 Bourne shell (sh) 的超集，同时融入 csh 和 ksh 的优秀特性。但真正让 zsh 走向大众的是 2015 年发布的 Oh My Zsh——由 Robby Russell 创建的社区驱动配置框架，它将复杂的 zsh 配置浓缩为一个命令，并提供了 300+ 主题和 1000+ 插件的生态系统。2019 年，Apple 宣布 macOS Catalina 将 zsh 设为默认 Shell，替代已停留在 GPLv2 老版本的 bash 3.2（受限于许可证问题），这一决定让 zsh 的用户基数暴增。zsh 的核心优势包括：超强的自动补全（菜单式选择、模糊匹配）、拼写纠正、路径扩展、右侧提示符（RPROMPT）、共享命令历史等。虽然近年 fish 和 nushell 异军突起，zsh 凭借其 bash 兼容性和成熟的插件生态，仍是开发者最广泛使用的交互式 Shell。

**使用方法与案例**

```bash
# macOS（已预装，设为默认）
chsh -s /bin/zsh

# Ubuntu/Debian
sudo apt install zsh
chsh -s $(which zsh)

# 安装 Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

**核心配置（~/.zshrc）：**

```bash
# 推荐的 Oh My Zsh 插件
plugins=(
  git                    # Git 别名和函数
  docker                 # Docker 自动补全
  kubectl                # Kubernetes 自动补全
  zsh-autosuggestions    # 历史命令建议（灰色提示）
  zsh-syntax-highlighting # 命令语法高亮
  fzf                    # fzf 集成
  extract                # 智能解压（x 任意压缩包）
  z                      # 目录跳转记录
)

# 实用别名
alias ll='ls -lah'
alias gs='git status'
alias gc='git commit'
alias gp='git push'
alias dps='docker ps'

# 历史记录配置
HISTSIZE=50000
SAVEHIST=50000
setopt SHARE_HISTORY        # 多终端共享历史
setopt HIST_IGNORE_DUPS     # 忽略连续重复命令
setopt HIST_IGNORE_SPACE    # 以空格开头的命令不记录
```

**实战案例 1：智能自动补全配置**

```bash
# zsh 的补全系统是工业级最强
# 按 Tab 键触发菜单式补全
# 按 Ctrl+F/N/P/B 在候选中导航

# 启用高级补全
autoload -Uz compinit && compinit
zstyle ':completion:*' menu select       # 菜单式补全
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' # 大小写不敏感
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}      # 彩色补全

# 补全时展开缩写
zstyle ':completion:*' completer _expand _complete _ignored

# kill 命令补全进程名
zstyle ':completion:*:*:kill:*' menu yes select
```

**实战案例 2：自动跳转系统**

```bash
# 安装 z 插件（Oh My Zsh 内置）
# z 会记录访问过的目录，按"frecency"算法排序

# 跳转到包含 "proj" 的常用目录
z proj
# 跳转到最匹配 "down" 的目录
z down
# 列出匹配的目录选项
z -l proj

# 使用 autojump（第三方更强大的版本）
brew install autojump
# 安装后在 .zshrc 中添加
[[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && \
  . $(brew --prefix)/etc/profile.d/autojump.sh

# 现在可以用 j 代替 z
j proj
```

**实战案例 3：自定义功能函数**

```bash
# 在 ~/.zshrc 中添加以下函数

# mkcd - 创建目录并进入
mkcd() { mkdir -p "$1" && cd "$1"; }

# extract - 根据扩展名智能解压
extract() {
  if [ -f "$1" ]; then
    case "$1" in
      *.tar.bz2) tar xjf "$1"   ;;
      *.tar.gz)  tar xzf "$1"   ;;
      *.bz2)     bunzip2 "$1"   ;;
      *.rar)     unrar x "$1"   ;;
      *.gz)      gunzip "$1"    ;;
      *.tar)     tar xf "$1"    ;;
      *.tbz2)    tar xjf "$1"   ;;
      *.tgz)     tar xzf "$1"   ;;
      *.zip)     unzip "$1"     ;;
      *.7z)      7z x "$1"      ;;
      *)         echo "'$1' cannot be extracted" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# take - git clone + 自动进入目录
take() {
  git clone "$1" && cd "$(basename "$1" .git)"
}
```

**进阶技巧：**

- `vared` 命令可以交互式编辑变量：`vared PATH`
- `zmv` 批量重命名：`autoload -Uz zmv && zmv '(*).jpeg' '$1.jpg'`
- 使用 `setopt CORRECT` 启用拼写纠正（会有确认提示）
- `zsh` 的 `print -P` 支持提示符转义序列，写出彩色输出

---

### 12. fish

**前世今生**

fish（Friendly Interactive SHell）由 Axel Liljencrantz 于 2005 年创建，设计哲学与 zsh/bash 截然不同——fish 认为一个现代化的 Shell 应该"开箱即用"，无需繁杂配置。Axel 当时是瑞典皇家理工学院的学生，他对 bash/zsh 那些晦涩的配置语法感到沮丧：`if [ "$x" = "y" ]` 和 `$(ps aux | grep ...)` 对新手极不友好。fish 重新设计了语法：`if test "$x" = "y"`、`(ps aux | grep ...)` 括号式命令替换、`$status` 代替 `$?`。更关键的是，fish 首创了"基于历史输入的自动建议"（autosuggestion）——用户输入时，灰色文本会自动提示历史匹配，按右箭头即可接受。fish 还内置了语法高亮、Web 配置界面（`fish_config`）、24 位真彩色支持。虽然 fish 不是 POSIX 兼容的（因此不能直接运行 bash 脚本），但它可以用 `bash -c '...'` 包裹执行。fish 的哲学影响了后来的 nushell 和 zsh 的 autosuggestion 插件。

**使用方法与案例**

```bash
# macOS
brew install fish
# 添加到可用 Shell 列表
echo /opt/homebrew/bin/fish | sudo tee -a /etc/shells
chsh -s /opt/homebrew/bin/fish

# Ubuntu/Debian
sudo apt install fish
chsh -s $(which fish)

# Windows (WSL 中推荐)
sudo apt install fish
```

**常用命令：**

```fish
# 变量操作
set name "value"               # 设置变量
set -x PATH $PATH /new/path   # 导出环境变量
set -e name                    # 删除变量

# 函数定义
function greet
    echo "Hello, $argv[1]!"
end
funcsave greet                 # 保存函数（持久化）

# 条件语句
if test -f "config.yaml"
    echo "Config found"
else
    echo "No config"
end

# 循环
for file in *.txt
    echo "Processing $file"
end

# 命令替换（用括号代替反引号）
set count (wc -l < data.txt)
echo "Lines: $count"
```

**实战案例 1：零配置的生产力环境**

```fish
# fish 不需要 Oh My Fish 已经很好用了
# 但如果你想要插件管理：

# 安装 Oh My Fish（可选）
curl -L https://get.oh-my.fish | fish

# 安装实用插件
omf install z                  # 目录跳转
omf install foreign-env        # 兼容 bash 环境变量
omf install fzf                # fzf 集成

# 配置缩写（abbr — fish 独有的扩展功能）
abbr -a gco git checkout
abbr -a gst git status
abbr -a gcm git commit -m
abbr -a dc docker-compose
# 输入 gco<空格> 自动展开为 git checkout
```

**实战案例 2：自定义提示符**

```fish
# 直接在命令行定义函数（无需编辑配置文件）
# fish_prompt 是 fish 的特殊函数

function fish_prompt
    set -l last_status $status
    # 当前目录（蓝色）
    set_color blue
    echo -n (prompt_pwd)
    # Git 分支
    set -l git_branch (git branch --show-current 2>/dev/null)
    if test -n "$git_branch"
        set_color yellow
        echo -n " [$git_branch]"
    end
    # 退出状态码
    if test $last_status -ne 0
        set_color red
        echo -n " ✗"
    end
    set_color normal
    echo -n ' ➜ '
end

# 保存函数
funcsave fish_prompt
```

**实战案例 3：Web 配置界面**

```bash
# fish 提供基于浏览器的配置工具
fish_config
# 这会打开浏览器，可视化配置：
# - 颜色主题（选择预置或自定义）
# - 提示符（选择多种布局样式）
# - 函数和别名管理
# - 环境变量查看
# - 历史记录浏览

# 也可以直接在终端中：
fish_config prompt choose informative
fish_config prompt choose classic
```

**进阶技巧：**

- `fish_update_completions` 重建命令补全数据库
- `Alt+E` 或 `Alt+V` 用编辑器编辑当前命令行
- `Ctrl+Space` 在 pager 模式下展开完整列表
- `commandline -f repaint` 手动刷新语法高亮
- fish 不支持 `!!`（上一条命令），用 `Alt+Up` 代替

---

### 13. starship

**前世今生**

starship 由 Matan Kushner 于 2019 年发布，是一个用 Rust 编写的跨 Shell、跨平台的极简提示符。在 starship 出现之前，定制 Shell 提示符是一场噩梦：bash 需要复杂的 `PS1` 转义序列、zsh 有 `powerlevel10k` 但配置极其复杂、fish 的内置方案切换不便。更麻烦的是，在 zsh、bash、fish 之间切换时，每个 Shell 都需要单独配置提示符。Matan Kushner 的解决方案是用 Rust 写一个独立的二进制程序，通过环境变量和配置文件读取状态，为所有主流 Shell 输出统一风格的提示符。starship 的配置文件是一个直观的 TOML 文件，支持显示 Git 状态、Node.js/Python/Rust 版本、命令执行时间、电池电量、AWS 配置等数十种模块。starship 的"非侵入式"设计也意味着它不影响 Shell 启动速度——实测比 powerlevel10k 快 2-3 倍。截至 2025 年，starship 拥有超过 45,000 颗星，是 GitHub 上最受欢迎的提示符工具。

**使用方法与案例**

```bash
# macOS / Linux
curl -sS https://starship.rs/install.sh | sh

# Windows
scoop install starship

# 在 Shell 配置文件中添加（选择你使用的 Shell）：
# ~/.bashrc
eval "$(starship init bash)"

# ~/.zshrc
eval "$(starship init zsh)"

# ~/.config/fish/config.fish
starship init fish | source
```

**配置文件（~/.config/starship.toml）：**

```toml
# 基础格式
format = """
[](color_bg)[ $os ](bg:color_bg fg:white)[](bg:color_bg fg:color_fg)$directory\
[](fg:color_fg bg:color_bg)$git_branch$git_status\
[](fg:color_bg)"""

# 添加新行
add_newline = true

# 命令执行时间（超过 3 秒才显示）
[cmd_duration]
min_time = 3000
format = " took [$duration]($style) "

# Git 分支
[git_branch]
format = " [$branch]($style) "
style = "bold purple"

# Git 状态
[git_status]
conflicted = "🏳"
ahead = "⇡${count}"
behind = "⇣${count}"
diverged = "⇕⇡${ahead_count}⇣${behind_count}"
untracked = "?${count}"
stashed = "\\$"
modified = "!${count}"
staged = "+${count}"
renamed = "»${count}"
deleted = "✘${count}"

# 语言版本显示
[nodejs]
format = " via [⬢ $version](bold green) "

[python]
format = " via [🐍 $version](bold blue) "

[rust]
format = " via [🦀 $version](bold red) "

# 目录截断
[directory]
truncation_length = 3
truncate_to_repo = true

# 自定义模块
[custom.error]
command = "echo $?"
when = """ test $? -ne 0 """
format = " [$output](bold red) "
```

**实战案例 1：Nerd Font 定制主题**

```bash
# 先安装 Nerd Font（推荐 FiraCode Nerd Font）
brew tap homebrew/cask-fonts
brew install --cask font-fira-code-nerd-font

# 在终端模拟器中设置字体为 "FiraCode Nerd Font"

# 预设主题（直接使用社区主题）
starship preset nerd-font-symbols -o ~/.config/starship.toml

# 或浏览主题库
starship preset --list
```

**实战案例 2：工作目录智能提示**

```toml
# 在 ~/.config/starship.toml 中配置

# AWS 环境提示（只在 AWS 目录下显示）
[aws]
format = 'on [$symbol($region)]($style) '
disabled = false

# Kubernetes 上下文（只在有 kubeconfig 时显示）
[kubernetes]
format = '☸ [$context](bold cyan) '
disabled = false

# Terraform 工作区
[terraform]
format = '[🏗 $workspace]($style) '

# 自定义：检测是否在 Git 仓库中
[custom.is_git_repo]
command = 'git rev-parse --is-inside-work-tree 2>/dev/null'
when = 'true'
format = ''

# 这样在配置中可以用 $custom.is_git_repo 状态来条件显示
```

**实战案例 3：多机器统一配置**

```bash
# 创建 Git 管理的 dots 仓库
mkdir -p ~/dots && cd ~/dots
git init

# 添加 starship 配置
cp ~/.config/starship.toml starship.toml

# 使用条件模块区分机器
# 在 starship.toml 中：
# 可以设置 STARSHIP_CONFIG 环境变量指向不同配置

# 在家目录创建符号链接
ln -sf ~/dots/starship.toml ~/.config/starship.toml

# 通过 Git 在多台机器间同步
git remote add origin git@github.com:user/dots.git
git push -u origin main
```

**进阶技巧：**

- `starship timings` 检查各模块耗时，优化启动速度
- `starship explain` 解释当前提示符的每个部分含义
- `starship module <name>` 单独测试某个模块的输出
- 设置 `STARSHIP_LOG=error` 调试配置问题
- 使用 `[env_var]` 模块显示任意环境变量

---

### 14. tmux

**前世今生**

tmux（Terminal MUltipleXer）由 Nicholas Marriott 于 2007 年创建，是 GNU Screen 的现代替代品。终端复用器的概念源于 1987 年 Oliver Laumann 为 BSD 开发的 `window` 命令，后来被 GNU Screen（1987 年）发扬光大。但 GNU Screen 的代码库极其老旧（核心代码近 20 年未变）、不支持垂直分屏、配置语法反直觉。Nicholas Marriott 当时在剑桥大学攻读计算机科学，受到 GNU Screen 的启发和困扰，决定用 OpenBSD 风格编写一个全新的终端复用器。tmux 的核心价值在于：允许你在一个终端窗口中管理多个会话、窗口和面板，断开后会话继续运行（即使 SSH 断开），并支持多人实时共享终端（结对编程）。tmux 采用客户端-服务器架构，服务端管理持久会话，客户端负责显示。2015 年发布的 tmux 2.0 引入了 256 色支持和新的配置格式。tmux 是服务器运维、远程开发和本地工作流管理的必备工具。

**使用方法与案例**

```bash
# macOS
brew install tmux

# Ubuntu/Debian
sudo apt install tmux

# Windows (WSL 中)
sudo apt install tmux
```

**常用命令：**

```bash
# 会话管理
tmux new -s dev              # 创建命名会话
tmux ls                      # 列出会话
tmux attach -t dev           # 附加到会话
tmux kill-session -t dev     # 终止会话
tmux detach                  # 分离（Ctrl+B d）

# 窗口管理（在 tmux 内）
Ctrl+B c                     # 创建新窗口
Ctrl+B ,                     # 重命名窗口
Ctrl+B n / p                 # 切换下一个/上一个窗口
Ctrl+B 0-9                   # 跳转到指定窗口
Ctrl+B &                     # 关闭窗口

# 面板管理
Ctrl+B %                     # 垂直分割
Ctrl+B "                     # 水平分割
Ctrl+B 方向键                # 在面板间移动
Ctrl+B Ctrl+方向键           # 调整面板大小
Ctrl+B z                     # 全屏/恢复面板
Ctrl+B x                     # 关闭面板
Ctrl+B Space                 # 切换面板布局

# 滚动与复制
Ctrl+B [                     # 进入复制/滚动模式
# 在滚动模式中：
#   Space 开始选择
#   Enter 复制选择
#   q 退出
Ctrl+B ]                     # 粘贴

# 同步输入（多面板同时输入）
Ctrl+B :setw synchronize-panes on/off
```

**实战案例 1：开发环境一键启动**

```bash
# 创建启动脚本 ~/dev-session.sh
#!/bin/bash
SESSION="myproject"

# 如果会话已存在则附加，否则创建
tmux has-session -t $SESSION 2>/dev/null
if [ $? -eq 0 ]; then
    tmux attach -t $SESSION
    exit 0
fi

# 创建新会话（不附加）
tmux new-session -d -s $SESSION -n editor

# 窗口 0: 编辑器
tmux send-keys -t $SESSION:0 'cd ~/projects/myapp && nvim .' C-m

# 窗口 1: 开发服务器
tmux new-window -t $SESSION -n server
tmux send-keys -t $SESSION:1 \
  'cd ~/projects/myapp && npm run dev' C-m

# 窗口 2: Git 操作
tmux new-window -t $SESSION -n git
tmux send-keys -t $SESSION:1 \
  'cd ~/projects/myapp && git status' C-m

# 窗口 3: 系统监控
tmux new-window -t $SESSION -n monitor
tmux send-keys -t $SESSION:3 'htop' C-m
# 分割窗口
tmux split-window -h -t $SESSION:3
tmux send-keys -t $SESSION:3.1 \
  'watch -n 1 "docker ps --format \"table {{.Names}}\t{{.Status}}\""' C-m

# 选择主窗口并附加
tmux select-window -t $SESSION:0
tmux attach -t $SESSION
```

**实战案例 2：远程服务器持久会话**

```bash
# SSH 到服务器后
ssh user@server

# 创建或附加 tmux
tmux new -As main

# 在 tmux 内运行长时间任务
python train_model.py --epochs 100

# 安全断开（Ctrl+B d）
# SSH 连接可以安全断开，任务继续运行

# 稍后重新连接
ssh user@server
tmux attach -t main
# 任务仍在运行，可以查看进度

# 分享会话给同事（结对调试）
# 同事通过 SSH 登录同一台机器
tmux attach -t main
# 双方看到同一屏幕，可以同时操作
```

**实战案例 3：tmux 配置文件**

```bash
# ~/.tmux.conf
# 修改前缀键（从 Ctrl+B 改为 Ctrl+A，更像 Screen）
set -g prefix C-a
unbind C-b
bind C-a send-prefix

# 用 Alt+方向键 切换面板（无需前缀键）
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D

# 用 Shift+方向键 切换窗口
bind -n S-Left previous-window
bind -n S-Right next-window

# 用 | 垂直分割，- 水平分割（更直观）
bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"

# 鼠标支持
set -g mouse on

# Vi 风格复制模式
setw -g mode-keys vi
bind-key -T copy-mode-vi 'v' send -X begin-selection
bind-key -T copy-mode-vi 'y' send -X copy-selection

# 256 色支持
set -g default-terminal "screen-256color"
set -ga terminal-overrides ",*256col*:Tc"

# 自动重命名窗口
set -g automatic-rename on
set -g renumber-windows on

# 状态栏美化
set -g status-bg colour235
set -g status-fg white
set -g status-left '#[fg=green]#S '
set -g status-right '#[fg=yellow]%Y-%m-%d %H:%M'
```

**进阶技巧：**

- `tmux source-file ~/.tmux.conf` 重新加载配置
- `tmux list-keys` 查看所有快捷键绑定
- `tmux info` 查看当前服务器信息
- `tmuxinator` 或 `tmuxp` 用 YAML 配置会话布局
- `Ctrl+B :` 进入命令模式的完整命令列表

---

### 15. alacritty

**前世今生**

Alacritty 由 Joe Wilm 于 2016 年创建，是一个用 Rust 编写的 GPU 加速的终端模拟器。"Alacritty"这个名字来自"Alacrity"（意为敏捷、迅速），体现了其核心设计目标：极致性能。传统终端模拟器（如 macOS Terminal、GNOME Terminal）使用 CPU 渲染文本，在大量输出（如 `find /` 或编译日志）时会明显卡顿。Joe Wilm 选择直接用 OpenGL 在 GPU 上渲染终端内容，将渲染流水线的每一帧延迟降到最低。Alacritty 是"简单"哲学的坚定实践者：它刻意不支持分页（tab）和窗口分割——这些功能留给 tmux 或窗口管理器。这让 Alacritty 的代码库极为精简，bug 更少，性能更优。Alacritty 也是最早全面支持 24 位真彩色和连字（ligatures）的终端之一。虽然 Alacritty 本身不支持标签页，但在 macOS 上配合系统标签页、Linux 上配合平铺窗口管理器（如 i3/sway），体验极为流畅。

**使用方法与案例**

```bash
# macOS
brew install --cask alacritty

# Ubuntu/Debian
sudo add-apt-repository ppa:aslatter/ppa
sudo apt install alacritty

# Windows
scoop install alacritty
# 或下载 Windows 安装包
```

**配置文件（~/.config/alacritty/alacritty.toml）：**

```toml
# 通用配置
[window]
opacity = 0.95
decorations = "none"  # 无边框模式（配合平铺窗口管理器）
dynamic_title = true

[font]
size = 14
# 推荐使用带连字的 Nerd Font
[font.normal]
family = "FiraCode Nerd Font"
style = "Regular"

[font.bold]
family = "FiraCode Nerd Font"
style = "Bold"

[font.italic]
family = "FiraCode Nerd Font"
style = "Italic"

# 颜色主题（Dracula 风格示例）
[colors]
[colors.primary]
background = "#282a36"
foreground = "#f8f8f2"

[colors.normal]
black = "#21222c"
red = "#ff5555"
green = "#50fa7b"
yellow = "#f1fa8c"
blue = "#bd93f9"
magenta = "#ff79c6"
cyan = "#8be9fd"
white = "#f8f8f2"

[colors.bright]
black = "#6272a4"
red = "#ff6e6e"
green = "#69ff94"
yellow = "#ffffa5"
blue = "#d6acff"
magenta = "#ff92df"
cyan = "#a4ffff"
white = "#ffffff"

# 键盘绑定
[keyboard]
bindings = [
  # 复制粘贴（macOS 风格）
  { key = "C", mods = "Command|Shift", action = "Copy" },
  { key = "V", mods = "Command|Shift", action = "Paste" },
  # Vi 模式滚动
  { key = "K", mods = "Command", action = "ScrollPageUp" },
  { key = "J", mods = "Command", action = "ScrollPageDown" },
]

# 光标
[cursor]
style = { shape = "Beam", blinking = "On" }
vi_mode_style = { shape = "Block", blinking = "Off" }

# 选择
[selection]
semantic_escape_chars = ",│`|:\"' ()[]{}<>"
save_to_clipboard = true
```

**实战案例 1：性能基准对比**

```bash
# 测试终端性能的经典方法：输出大量文本
# 在 alacritty 中运行：
time find / -name "*" 2>/dev/null | head -100000
# 对比 macOS Terminal / iTerm2 / GNOME Terminal 的时间差异

# 测试颜色渲染
# 24 位真彩色测试
awk 'BEGIN{
  s="/\\/\\/\\/\\/\\"; s=s s s s s s s s;
  for (colnum=0; colnum<77; colnum++) {
    r=255-(colnum*255/76);
    g=(colnum*510/76);
    b=(colnum*255/76);
    if (g>255) g=510-g;
    printf "\033[48;2;%d;%d;%dm", r,g,b;
    printf "\033[38;2;%d;%d;%dm", 255-r,255-g,255-b;
    printf "%s\033[0m", substr(s, colnum+1, 1);
  }
  printf "\n";
}'
```

**实战案例 2：主题切换工作流**

```bash
# 管理多个主题配置文件
ls ~/.config/alacritty/themes/

# 创建主题切换脚本
cat > ~/.local/bin/alacritty-theme << 'EOF'
#!/bin/bash
THEME="${1:-dark}"
case $THEME in
  dark)
    cp ~/.config/alacritty/themes/dracula.toml \
       ~/.config/alacritty/colors.toml
    ;;
  light)
    cp ~/.config/alacritty/themes/solarized-light.toml \
       ~/.config/alacritty/colors.toml
    ;;
  *)
    echo "Unknown theme: $THEME"
    exit 1
    ;;
esac
touch ~/.config/alacritty/alacritty.toml  # 触发配置重载
echo "Switched to ${THEME} theme"
EOF
chmod +x ~/.local/bin/alacritty-theme

# 使用
alacritty-theme dark
alacritty-theme light
```

**实战案例 3：自定义快捷键工作流**

```toml
# ~/.config/alacritty/alacritty.toml 中的键盘定制
[keyboard]
bindings = [
  # Ctrl+Shift+N 打开新窗口
  { key = "N", mods = "Control|Shift",
    action = "SpawnNewInstance" },
  
  # Alt+Enter 全屏切换
  { key = "Return", mods = "Alt",
    action = "ToggleFullscreen" },
  
  # 字体缩放
  { key = "Plus", mods = "Control",
    action = "IncreaseFontSize" },
  { key = "Minus", mods = "Control",
    action = "DecreaseFontSize" },
  { key = "Key0", mods = "Control",
    action = "ResetFontSize" },
  
  # Vi 模式快捷键
  { key = "Space", mods = "Control|Shift",
    action = "ToggleViMode" },
]
```

**进阶技巧：**

- Alacritty 使用 `alacritty msg` 子命令控制运行中的实例
- `alacritty --working-directory ~/projects` 指定启动目录
- 多显示器配置不同字体大小，使用 `[font]` 的 `size` 字段配合条件配置
- macOS 上配合 `yabai` 平铺窗口管理器体验最佳

---

### 16. kitty

**前世今生**

kitty 由 Kovid Goyal（也是电子书管理工具 Calibre 的创建者）于 2017 年发布，是一个用 C 和 Python 混合编写的 GPU 加速终端模拟器。kitty 的全名叫 "kitty terminal"，Kovid Goyal 的猫就叫 Kitty。与 Alacritty 的"极简不做窗口管理"不同，kitty 野心更大：它内置了标签页和面板分割系统、支持显示图片（通过自定义的终端图形协议）、提供远程控制功能（允许脚本操控终端）、内置滚动回看缓冲和搜索。kitty 的渲染引擎完全使用 GPU（OpenGL on Linux, Metal on macOS），在大量输出下的滚动性能极为流畅。kitty 的图形协议（Kitty Graphics Protocol）是终端显示图片的最先进方案，已被 ranger、neofetch 等工具支持。kitty 的"kittens"子系统（Python 编写的插件）提供了 SSH 集成、剪贴板管理、Unicode 输入等高级功能。

**使用方法与案例**

```bash
# macOS
brew install --cask kitty

# Ubuntu/Debian
curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin

# Windows (WSL 中)
# 同上 Linux 安装方法
```

**常用命令：**

```bash
# 标签页和窗口管理
Ctrl+Shift+T              # 新建标签页
Ctrl+Shift+Q              # 关闭标签页
Ctrl+Shift+Right/Left     # 切换标签页
Ctrl+Shift+Enter          # 新建窗口（垂直分割）
Ctrl+Shift+] / [          # 切换窗口
Ctrl+Shift+R              # 调整窗口大小

# 滚动和搜索
Ctrl+Shift+Up/Down        # 滚动
Ctrl+Shift+H              # 浏览滚动缓冲区
Ctrl+Shift+G              # 搜索

# kitty 独有功能
Ctrl+Shift+F2             # 编辑滚动缓冲区内容（用 $EDITOR）
Ctrl+Shift+U              # Unicode 字符输入
Ctrl+Shift+P               # 使用 fzf 搜索历史
```

**配置文件（~/.config/kitty/kitty.conf）：**

```conf
# 字体
font_family      FiraCode Nerd Font Mono
bold_font        auto
italic_font      auto
bold_italic_font auto
font_size        13.0

# 窗口样式
window_padding_width 8
hide_window_decorations yes
confirm_os_window_close 0

# 颜色主题
include themes/dracula.conf

# 光标
cursor_shape beam
cursor_beam_thickness 1.5
cursor_blink_interval 0.5

# 滚动
scrollback_lines 10000
scrollback_pager_history_size 0  # 不限制 pager 历史

# 鼠标
mouse_hide_wait 2.0
url_color #61afef
url_style curly

# 性能
repaint_delay 6
input_delay 3
sync_to_monitor yes

# 标签栏
tab_bar_style powerline
tab_powerline_style angled
active_tab_font_style bold

# 键盘快捷键
map ctrl+shift+c copy_to_clipboard
map ctrl+shift+v paste_from_clipboard
map ctrl+shift+n new_tab
map ctrl+w close_tab
```

**实战案例 1：终端内显示图片**

```bash
# kitty 的图形协议可以在终端内直接显示图片
# 使用 icat kitten 显示图片
kitty +kitten icat ~/Pictures/photo.jpg

# 显示网络图片
kitty +kitten icat https://example.com/image.png

# 显示图片的缩略图
kitty +kitten icat --place 80x80@0x0 photo.jpg

# 配合命令行工具使用
# 在 ranger 中预览图片（需在 ranger 配置中启用 kitty 预览）
# 设置 ~/.config/ranger/rc.conf：
# set preview_images true
# set preview_images_method kitty
```

**实战案例 2：远程控制与自动化**

```bash
# kitty 提供了强大的远程控制协议
# 打开新窗口并运行命令
kitty @ new-window --title "htop" htop

# 在当前窗口运行命令
kitty @ send-text "git status\n"

# 设置窗口标题
kitty @ set-window-title "Production Server"

# 获取终端信息
kitty @ ls  # 列出所有窗口（JSON 格式）

# 在脚本中控制布局
kitty @ launch --type=window --title "Editor" nvim
sleep 1
kitty @ launch --type=window --title "Terminal" \
  --location=hsplit fish
```

**实战案例 3：SSH 集成（ssh kitten）**

```bash
# kitty 的 ssh kitten 可以自动：
# 1. 复制 terminfo 到远程服务器
# 2. 启用 kitty 图形协议
# 3. 自动处理断开重连

# 使用 kitten 连接
kitty +kitten ssh user@server

# 创建别名
alias kssh='kitty +kitten ssh'

# 解决常见问题：远程主机不支持 terminfo
kitty +kitten ssh user@server
# kitten 会自动复制和安装 terminfo，无需手动配置

# 配合 tmux 在远程使用
kssh user@server tmux new -As main
```

**进阶技巧：**

- `kitty +kitten clipboard` 管理剪贴板历史
- `kitty +kitten unicode` 交互式 Unicode 字符搜索
- `kitty +kitten hints` 用快捷键选择屏幕上的 URL/路径
- 自定义 kitten（Python 插件）扩展 kitty 功能
- 使用 `kitty @ set-background-opacity 0.8` 动态调整透明度

---

### 17. zellij

**前世今生**

zellij 由 Aram Drevekenin 于 2021 年在 GitHub 上开源，是一个用 Rust 编写的现代终端工作区管理器。"Zellij"这个名字来自波斯语，意为波斯传统建筑中的彩色玻璃窗，恰如其功能——将终端变成一幅由多个面板组成的美丽"花窗"。zellij 的定位介于 tmux 和桌面窗口管理器之间：它像 tmux 一样管理终端会话，但提供了可视化界面、浮动面板、状态栏插件系统、WebAssembly 插件等现代特性。Aram Drevekenin 认为 tmux 的门槛太高（所有操作靠记快捷键），zellij 的解决方案是提供一个始终可见的状态栏和快捷键提示、支持鼠标点击操作、默认配置即开即用。zellij 最独特的创新是"锁定模式"——输入 `Ctrl+G` 后，zellij 拦截所有键盘输入，让你可以像操作 Vim 一样操作终端布局。2023 年加入的 Wasm 插件系统允许用任意编译为 Wasm 的语言编写状态栏组件。

**使用方法与案例**

```bash
# macOS / Linux
cargo install zellij
# 或从 GitHub Release 下载

# 简单启动
zellij                    # 启动新会话
zellij attach             # 附加到已有会话
zellij ls                 # 列出会话
```

**核心概念：**

```bash
# 锁屏模式（Ctrl+G）- 所有操作的基础
# 进入锁屏模式后，所有按键变为 zellij 快捷键：
#   无需按修饰键

# 面板操作（在锁屏模式下）
n                         # 新建面板（默认方向）
h / j / k / l             # 移动焦点（Vim 风格）
HJKL                      # 调整面板大小
p + h/j/k/l               # 切换面板位置
x                         # 关闭面板
f                         # 全屏当前面板
z                         # 缩放面板

# 标签页操作（在锁屏模式下）
t                         # 新建标签页
[ / ]                     # 切换标签页
1-9                       # 跳转标签页
, 或 .                    # 移动标签页位置

# 滚动（在锁屏模式下）
s                         # 进入滚动模式
# 在滚动模式中：
#   j/k 滚动
#   Ctrl+u/d 翻页
#   y 复制选择
#   / 搜索
#   Esc 退出
```

**实战案例 1：开发布局模板**

```bash
# zellij 支持 YAML 配置文件定义布局
# ~/.config/zellij/layouts/dev.kdl

layout {
    default_tab_template {
        pane size=1 borderless=true {
            plugin location="zellij:tab-bar"
        }
        children
        pane size=2 borderless=true {
            plugin location="zellij:status-bar"
        }
    }

    tab name="editor" focus=true {
        pane split_direction="vertical" {
            pane command="nvim" size="70%"
            pane {
                command="fish"
                size="30%"
            }
        }
    }

    tab name="server" {
        command="npm"
        args="run" "dev"
        cwd="/home/user/projects/myapp"
    }

    tab name="git" {
        command="lazygit"
        cwd="/home/user/projects/myapp"
    }
}

# 使用自定义布局启动
zellij --layout dev
```

**实战案例 2：浮动终端面板**

```bash
# zellij 支持浮动面板（tmux 不支持）
# 在锁屏模式下：
Ctrl+p + w                # 打开浮动面板
# 或：
Ctrl+p + e                # 在浮动面板中打开编辑器

# 浮动面板可以拖动、调整大小
# 适合运行一次性命令而不破坏布局

# 通过命令行创建浮动面板
zellij action new-pane --floating --command "htop"
zellij action new-pane --floating \
  --x 20 --y 10 --width 60 --height 40
```

**实战案例 3：会话协作**

```bash
# 多人同时连接到同一个 zellij 会话
# 用户 A 创建会话
zellij --session pair-programming

# 用户 B 附加到同一会话
zellij attach pair-programming
# 现在两人看到相同内容，可以同时操作
# 不同用户的光标颜色不同

# 会话持久化（断开后自动保存）
# zellij 默认启用会话持久化
# 退出时按 Ctrl+Q 而非关闭终端
zellij attach pair-programming  # 恢复会话

# 列出所有可恢复的会话
zellij list-sessions
```

**进阶技巧：**

- `zellij action` 命令可以脚本化所有操作
- Wasm 插件编写：https://zellij.dev/documentation/plugins
- `zellij setup --dump-config` 查看完整默认配置
- `Ctrl+o` 在锁屏模式下切换至"会话管理器"
- `zellij pipe` 向运行中的插件发送数据

---

### 18. atuin

**前世今生**

atuin 由 Ellie Huxtable 于 2021 年创建，是一个用 Rust 编写的 Shell 历史记录增强工具——它用一个 SQLite 数据库替换了传统的 `.bash_history` 纯文本文件。"Atuin"在古苏格兰语中意为"我们自己的"，Ellie 是英国开发者，她将 atuin 设计为对传统 Shell 历史的彻底革命。传统 Shell 历史的问题包括：只记录命令（无上下文）、无法搜索工作目录或退出码、多终端历史各自独立、无法在多台机器间同步。atuin 的解决方案是：记录每条命令的时间戳、工作目录、退出码、主机名、会话 ID 和持续时长；使用 SQLite 全文搜索提供亚秒级历史检索；支持端到端加密的跨设备历史同步。更妙的是，atuin 提供了类似 fzf 的交互式搜索界面（`Ctrl+R` 被重新绑定），支持按目录、主机、退出码等多种维度筛选。截至 2025 年，atuin 拥有超过 20,000 颗 GitHub 星标。

**使用方法与案例**

```bash
# macOS / Linux
curl --proto '=https' --tlsv1.2 -sSf \
  https://setup.atuin.sh | bash

# 安装后在 Shell 配置文件中添加
# ~/.zshrc 或 ~/.bashrc
eval "$(atuin init zsh)"  # 或 bash/fish

# 重启 Shell 或 source ~/.zshrc
```

**核心功能操作：**

```bash
# 搜索历史（替代 Ctrl+R）
# 按 Ctrl+R，输入关键词搜索

# 在 atuin 搜索界面中：
#   Enter — 执行选中命令
#   Tab — 将命令填入当前行（可编辑）
#   Ctrl+E — 同上
#   Ctrl+C / Esc — 取消
#   Ctrl+O — 交互式目录筛选

# 命令行查询（不用交互界面）
atuin search "git commit"           # 搜索历史
atuin search --cwd . --exit 0       # 当前目录成功执行的命令
atuin search --after "2024-01-01"   # 特定日期后
atuin search --limit 20             # 限制结果数

# 历史统计
atuin stats                         # 个人统计仪表板
atuin stats --count 20              # Top 20 命令
atuin history list                  # 列出历史
atuin history list --cwd .          # 当前目录的历史
atuin history start "long task" -- "$SHELL"  # 记录任务起止
atuin history end "completed"
```

**实战案例 1：找回遗忘的命令**

```bash
# 场景：三天前在 ~/projects/backend 目录执行过
# 一个复杂的 docker-compose 命令，现在想找回

# 按 Ctrl+R 打开 atuin 搜索
# 输入 "docker-compose" 并按 Tab 进入过滤模式
# 按 Ctrl+O 选择目录筛选，输入 "backend"
# 就能找到三天前的那条命令

# 或者直接命令行：
atuin search "docker-compose" \
  --cwd ~/projects/backend \
  --after "3 days ago" \
  --limit 5
```

**实战案例 2：命令使用分析**

```bash
# 分析自己的 Shell 使用习惯
atuin stats
# 输出：最常用命令、常用目录、错误率、每日命令数等

# 查看特定命令的所有变体
atuin search "kubectl" --limit 100 | \
  awk '{print $NF}' | sort | uniq -c | sort -rn

# 检查哪些命令经常失败（退出码非0）
atuin search --exit 1 --limit 50
# 帮助识别需要重新学习的命令
```

**实战案例 3：多设备同步**

```bash
# 注册 atuin 账号（可选，用于同步）
atuin register
# 输入用户名、邮箱、密码

# 登录
atuin login
# 输入用户名和密码，使用默认密钥加密

# 同步历史
atuin sync
# 自动同步所有设备的历史记录
# 数据端到端加密，atuin 服务器无法解密

# 查看同步状态
atuin status
# 输出：用户名、同步状态、历史条目数

# 如果不想用云同步，可以自建服务器
# 或仅使用本地功能（不注册即可）
```

**进阶技巧：**

- `atuin search --reverse` 反向排序（最新的在前）
- `atuin search --delete` 交互式删除历史条目
- `atuin history import bash` 从 bash 导入历史
- 设置 `ATUIN_SYNC_FREQUENCY="5m"` 调整同步频率
- `atuin dotfiles` 管理 dotfiles 版本

---

### 19. navi

**前世今生**

navi 由 Denis Isidoro 于 2019 年创建，是一个用 Rust 编写的交互式命令备忘录（cheatsheet）工具。Denis 是一位巴西开发者，他发现自己在日常工作中频繁查找相同的命令片段——awk 高级用法、docker 清理命令、git 变基流程等——每次都要搜索 Stack Overflow 或翻阅笔记。navi 的解决方案是将这些"命令配方"组织成可搜索的 `.cheat` 文件，用 fzf 风格的交互界面模糊查找并按需填充参数。navi 的创新在于"动态占位符"系统：cheatsheet 中可以定义 `<placeholder>`，navi 会在选择时提示你填入实际值。navi 内置了来自社区的大型 cheatsheet 仓库（覆盖 docker、git、kubectl、tmux 等数百个工具），也可以自定义私有 cheatsheet。它与 fzf 和 atuin 配合使用，构成了"命令发现 → 历史搜索 → 配方执行"的完整工作流。

**使用方法与案例**

```bash
# macOS
brew install navi

# Ubuntu/Debian
# 从 GitHub Release 下载二进制
# 或通过 cargo
cargo install navi

# Windows
scoop install navi
```

**快速入门：**

```bash
# 启动交互式界面
navi

# 搜索特定主题
navi --query "docker clean"

# 直接执行（跳过选择）
navi --print "git undo last commit"

# 导入社区 cheatsheets
navi repo add denisidoro/cheats
navi repo add denisidoro/tools

# 列出已安装的 cheatsheet 仓库
navi repo list
```

**实战案例 1：编写自定义 Cheatsheet**

```bash
# 创建私有 cheatsheet 目录
mkdir -p ~/.local/share/navi/cheats

# 示例：Git 操作备忘录
cat > ~/.local/share/navi/cheats/git.cheat << 'EOF'
% git

# 撤销最后一次提交（保留修改）
git reset --soft HEAD~1

# 修改最后一次提交信息
git commit --amend -m "<message>"

# 交互式暂存
git add -p

# 将分支变基到 main
git fetch origin
git rebase origin/main

# 删除已合并的本地分支
git branch --merged | grep -v "main\|master" | xargs git branch -d

# 查找引入 bug 的提交
git bisect start
git bisect bad
git bisect good <commit_hash>

# 恢复被删除的文件
git checkout $(git rev-list -n 1 HEAD -- "<file>")^ -- "<file>"
EOF

# Docker 操作备忘录
cat > ~/.local/share/navi/cheats/docker.cheat << 'EOF'
% docker

# 清理所有未使用的资源
docker system prune -af

# 进入运行中的容器
docker exec -it <container> /bin/sh

# 查看容器日志（跟随）
docker logs -f <container>

# 列出所有容器（包括停止的）
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 删除所有停止的容器
docker container prune -f

# 导出/导入镜像
docker save <image>:<tag> -o <file>.tar
docker load -i <file>.tar
EOF
```

**实战案例 2：使用动态占位符**

```bash
# 创建带占位符的 cheatsheet
cat > ~/.local/share/navi/cheats/k8s.cheat << 'EOF'
% kubernetes, k8s

# 查看 Pod 日志
kubectl logs -f <pod> -n <namespace>

# 端口转发
kubectl port-forward <pod> <local_port>:<remote_port> -n <namespace>

# 获取 Pod 详细信息
kubectl describe pod <pod> -n <namespace>

# 在 Pod 中执行命令
kubectl exec -it <pod> -n <namespace> -- <command>

# 按标签筛选资源
kubectl get <resource> -l <label_key>=<label_value> -n <namespace>

# 扩缩容
kubectl scale deployment/<name> --replicas=<count> -n <namespace>
EOF

# 使用 navi 搜索并填充参数
navi --query "port forward"
# 交互式提示：
#   pod: my-app-7d4f8c9b6-xk2lm
#   local_port: 8080
#   remote_port: 80
#   namespace: default
```

**实战案例 3：Shell 集成**

```bash
# 在 ~/.zshrc 中添加 Ctrl+G 快捷键绑定
# 让 navi 的输出直接填入命令行

# zsh 绑定
eval "$(navi widget zsh)"

# bash 绑定
eval "$(navi widget bash)"

# fish 绑定
navi widget fish | source

# 现在按 Ctrl+G 就可以在任何地方调用 navi
# 选择命令后直接填入当前命令行，支持继续编辑

# 高级：创建动态 cheatsheet
# 使用 shell 输出作为占位符建议值
cat > ~/.local/share/navi/cheats/process.cheat << 'EOF'
% process, kill

# 查找并终止进程（按名称）
ps aux | grep -i <process_name> | awk '{print $2}' | xargs kill -9

# 按端口查找进程
lsof -i :<port>

# 获取进程的子进程树
pstree -p <pid>
EOF

# 使用变量占位符
# 在 cheatsheet 中，$变量名 会被展开为 shell 变量
cat > ~/.local/share/navi/cheats/env.cheat << 'EOF'
% env

# 查看当前 Shell
echo $SHELL

# 当前用户
echo $USER

# PATH 中的所有目录
echo $PATH | tr ':' '\n'
EOF
```

**进阶技巧：**

- `navi --tldr <command>` 使用 tldr 作为 cheatsheet 源
- 变量占位符语法：`$NAME`（环境变量）、`$NAME: default`（默认值）
- 多选占位符：`<option1|option2|option3>`
- 自定义 cheatsheet 路径：`export NAVI_PATH="$HOME/cheats:$HOME/work/cheats"`

---

### 20. nushell

**前世今生**

nushell（简称 nu）由 Yehuda Katz（Ruby on Rails 核心成员、Ember.js 创建者）和 Sophia Turner 等人于 2019 年共同创建。nushell 的核心理念是：Shell 不应该只是处理字节流，而应该是处理**结构化数据**。传统 Unix Shell（bash/zsh/fish）将命令输出视为纯文本，需要 `awk`、`sed`、`grep` 等工具来解析。nushell 将一切视为结构化数据——命令输出是表格，管道传递的是类型化的数据流，每条管道都可以用 `describe` 查看数据类型。nushell 的实验灵感来自 PowerShell（微软的结构化 Shell），但设计上更加简洁现代，且原生支持 Linux/macOS/Windows 跨平台。nushell 的内置命令涵盖文件操作、网络请求、JSON/YAML/CSV 解析，甚至内建了 SQL 查询支持。虽然 nushell 目前还不适合作为登录 Shell（生态较新），但作为数据处理 Shell 和脚本语言，它提供了前所未有的命令行数据处理体验。

**使用方法与案例**

```bash
# macOS
brew install nushell

# Ubuntu/Debian
# 从 GitHub Release 下载
# 或通过 cargo
cargo install nu

# 启动
nu
```

**核心理念：**

```nu
# 传统 Shell：纯文本管道
# ls | grep ".md" | wc -l

# nushell：结构化数据管道
ls | where name =~ "\.md" | length

# 查看数据类型
ls | describe
# → table<name: string, type: string, size: filesize, modified: date>

# 查看详细帮助
help ls
help commands | where category == "filters"
```

**常用命令：**

```nu
# 文件操作（结构化输出）
ls                                  # 列表，返回表格
ls | sort-by size                   # 按大小排序
ls | where size > 1mb               # 筛选大于 1MB 的文件
ls | where modified > (date now) - 7day  # 最近 7 天修改的
ls | select name size               # 选择列
ls | first 5                        # 前 5 个

# 字符串处理
"hello world" | str upcase           # 大写
"hello world" | str contains "hello" # 包含判断
"a,b,c" | split row ","             # 分割为列表

# 表格操作
[[name, age]; [Alice, 30] [Bob, 25]] | 
  where age > 28 |
  select name

# 网络请求
http get https://api.github.com/repos/nushell/nushell |
  select full_name stargazers_count

# 数据格式转换
open data.json                      # 自动解析 JSON
open data.yaml                      # 自动解析 YAML
open data.csv                       # 自动解析 CSV
[1 2 3] | to json                   # 转换为 JSON
```

**实战案例 1：数据处理管道**

```nu
# 传统 Shell 需要 awk/sed/jq 组合
# nushell 一行完成

# CSV 分析
open sales.csv |
  where amount > 1000 |
  group-by region |
  transpose region records |
  update records {|r| $r.records | length} |
  rename region count |
  sort-by count --reverse

# JSON API 处理
http get "https://api.github.com/repos/BurntSushi/ripgrep/issues" |
  select title state created_at user.login |
  where state == "open" |
  sort-by created_at |
  first 10
```

**实战案例 2：系统管理**

```nu
# 查找最大的 5 个文件
ls **/* |
  where type == file |
  sort-by size --reverse |
  first 5 |
  select name size

# 进程管理（结构化 ps）
ps | where mem > 500mb | select name pid mem
ps | where name =~ "node" | length

# 磁盘使用分析
ls / | 
  where type == dir |
  each {|d| {name: $d.name, 
             count: (ls $d.name | length), 
             size: (ls $d.name | each {|f| $f.size} | math sum)}}
```

**实战案例 3：自定义命令和脚本**

```nu
# 创建自定义命令
def greet [name: string] {
  echo $"Hello, ($name)!"
}

# 定义参数类型和默认值
def "git push-force" [
  branch?: string  # 可选参数
  --remote: string = "origin"  # 命名参数带默认值
] {
  let b = if ($branch == null) { 
    git branch --show-current | str trim 
  } else { $branch }
  git push -f $remote $b
}

# 脚本文件（script.nu）
# 支持创建完整的自动化脚本
#!/usr/bin/env nu

def main [path: string] {
  let files = ls $path | where type == file
  print $"Found ($files | length) files"
  
  let total_size = $files | get size | math sum
  print $"Total size: ($total_size | into string)"

  $files | sort-by size --reverse | first 5
}
```

**进阶技巧：**

- `config nu` 打开配置文件进行编辑
- `$env.config.show_banner = false` 关闭启动横幅
- `source ~/myscripts.nu` 加载自定义函数
- `nu -c 'ls | first 3'` 从 bash 调用 nushell 命令
- nushell 脚本扩展名 `.nu`，可以用 `chmod +x` 后直接执行
- `open file | query db "SELECT ..."` 内建 SQL 支持

---

> **本组小结：** 从 zsh/fish 的 Shell 革命，到 starship 的一站式提示符美化，到 tmux/zellij 的会话持久化，再到 alacritty/kitty 的 GPU 渲染终端——这一组的工具重新定义了"命令行"的体验边界。加上 atuin 的历史增强、navi 的备忘配方、nushell 的结构化数据哲学，它们共同构建了一个比传统 Unix 环境更智能、更现代、更具生产力的工作空间。
