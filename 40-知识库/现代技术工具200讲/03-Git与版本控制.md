# 第3组：Git 与版本控制

## 21. lazygit

**前世今生：** lazygit 由澳大利亚开发者 Jesse Duffield 于 2018 年创建。Duffield 在工作中发现，用 Git 命令行做交互式操作（如 `git add -p`、`git rebase -i`）效率极低，每次都要记复杂的参数组合。他想要一个"看一眼就知道 Git 状态的 TUI"。lazygit 用 Go 编写，界面分五个面板：状态（Status）、分支（Branches）、文件（Files）、提交（Commits）、暂存（Stash）。全部键盘快捷键操作，按 `?` 看帮助。截至 2024 年 GitHub 已超 60k stars，成为 Git TUI 分类中最受欢迎的工具。lazygit 的哲学是"不做 git 做不到的事，只让 git 更好用"。

**使用方法与案例：**

安装：
```bash
brew install lazygit                # macOS
winget install jesseduffield.lazygit  # Windows
# Linux: 下载 GitHub Releases 二进制
```

**案例1：交互式暂存部分修改**
```bash
lazygit   # 打开
# 按 1 切换到 Files 面板
# 按 空格 选中/取消文件
# 按 d 查看文件 diff
# 按 c 提交，输入 commit message
# 按 P 推送到远端
```
比 `git add -p` 直观 10×——你能看到每个文件的完整 diff。

**案例2：交互式 rebase**
```bash
# 在 lazygit 的 Commits 面板（按 3）
# 按 e 编辑当前 commit
# 按 s 压缩（squash）到上一个 commit
# 按 f 修复（fixup）到上一个 commit
# 按 r 改写 commit message
```
可视化拖拽重排 commit 顺序，比 `git rebase -i HEAD~5` 安全得多。

**案例3：解决合并冲突**
```bash
# 左侧显示当前分支，右侧显示合并分支，底部显示结果
# 按 空格 选择哪一侧的更改
# 按 b 选择两边都保留
# 解决完所有冲突后自动继续 merge
```

**进阶技巧：**
- `Ctrl+P` / `Ctrl+N` 在面板间快速切换
- 自定义快捷键：`~/.config/lazygit/config.yml`
- 集成 delta（Git diff 美化器）：`git.paging.externalDiffCommand: delta`
- `lazygit --git-dir=/path/to/repo` 指定仓库

---

## 22. gh (GitHub CLI)

**前世今生：** gh 由 GitHub 官方于 2019 年启动开发，2020 年发布 1.0。在 gh 之前，管理 GitHub 的 PR/Issue 要么用浏览器，要么用社区工具 hub（也被 GitHub 收购但后来停止维护）。gh 的设计理念是"一个命令解决整个 GitHub 工作流"——从 clone 到 PR 到 review 到 merge。gh 用 Go 编写，与 git CLI 无缝集成（`gh` 命令可完全替代浏览器操作 GitHub）。2021 年后 gh 持续快速迭代，成为 GitHub 用户的标准配置。

**使用方法与案例：**

安装：
```bash
brew install gh            # macOS
winget install GitHub.cli  # Windows
apt install gh             # Debian/Ubuntu
gh auth login              # 首次登录
```

**案例1：创建 PR 一条龙**
```bash
# 1. 克隆仓库
gh repo clone myorg/myproject
# 2. 创建分支 + 提交 + 推送 + 创建 PR
git checkout -b feat/oee-dashboard
# ... 改代码 ...
gh pr create --title "OEE Dashboard Enhancement" \
             --body "Added real-time OEE widget and alert thresholds" \
             --base main \
             --assignee simon \
             --label enhancement,frontend \
             --reviewer alice,bob
```
一条命令替代：push + 打开浏览器 + 填 PR 表单 + 设 reviewer + 加 label。

**案例2：代码审查不用离开终端**
```bash
gh pr list                            # 查看待审 PR
gh pr checkout 42                     # 切换到 PR #42 的分支
gh pr diff 42                         # 查看变更
gh pr review 42 --approve -b "LGTM!"  # 批准
gh pr merge 42 --squash               # 合并
```

**案例3：管理 Issue**
```bash
gh issue create --title "OEE calculation incorrect" \
                --body "Steps to reproduce: ..." \
                --label bug --assignee @me
gh issue list --label bug --state open
gh issue view 23             # 查看详情（含评论）
gh issue close 23 -c "Fixed in #45"  # 关闭并引用 PR
```

**进阶技巧：**
- `gh run watch` 实时查看 GitHub Actions 运行日志
- `gh auth token` 快速获取 Token 用于脚本
- `gh api /repos/{owner}/{repo}/releases` 直接调用 GitHub REST API
- 别名：`gh alias set co 'pr checkout'` → `gh co 42`

---

## 23. glab

**前世今生：** glab 由 Clément Sam (profclems) 于 2019 年创建，对标 GitHub CLI 用于 GitLab。GitLab 虽然在自托管领域占据主导地位，但命令行工具长期空缺。glab 提供了与 gh 几乎一致的体验——`glab mr create`、`glab ci status`、`glab issue list`。2021 年 glab 被 GitLab 官方认可并推荐为社区 CLI。对于大量使用 GitLab 私有部署的企业，glab 是日常开发不可或缺的工具。

**使用方法与案例：**

安装：
```bash
brew install glab           # macOS
winget install GitLab.Glab  # Windows
# Linux: 下载 .deb/.rpm 包
glab auth login             # 登录 GitLab 实例
```

**案例1：创建 MR（Merge Request）**
```bash
glab mr create \
  --title "Fix OEE calculation" \
  --description "Corrected the OEE formula from (A*P*Q)/100 to (A*P*Q)" \
  --target-branch main \
  --assignee @simon \
  --reviewer @alice \
  --label "bug,production" \
  --remove-source-branch
```

**案例2：CI/CD 管理**
```bash
glab ci status              # 查看最近 pipeline
glab ci trace               # 实时查看 CI 日志
glab ci retry               # 重跑失败的 job
glab ci run                 # 触发新 pipeline
```

**案例3：管理 Issues 和 Snippets**
```bash
glab issue create --title "Database connection timeout" --label bug
glab issue list --assignee @me
glab snippet create report.md --title "Weekly OEE Report" --visibility internal
```

**进阶技巧：**
- `glab config set --host gitlab.internal.com` 连接私有实例
- `glab api /projects/:id/variables` 调用 GitLab API
- `glab variable set` 管理 CI/CD 环境变量

---

## 24. forgit

**前世今生：** forgit 由 Wook (wfxr) 于 2018 年创建，名字来自 "fzf" + "git"。它的设计极简——一套 Shell 函数，用 fzf 给 Git 命令加上交互式界面。`ga`（替代 `git add`）弹出 fzf 让你选文件，`glo`（替代 `git log`）让你搜索 commit 历史，`gcb`（替代 `git checkout -b`）让你搜索分支。没有新概念，就是让现有的 Git 命令更好用。

**使用方法与案例：**

安装：
```bash
# 先安装 fzf: brew install fzf / apt install fzf
git clone https://github.com/wfxr/forgit ~/.forgit
# 在 .bashrc 或 .zshrc 中:
source ~/.forgit/forgit.plugin.zsh
```

**案例1：交互式 git add**
```bash
ga
# fzf 弹出文件列表
# Tab 多选，Enter 确认，Ctrl+C 取消
# 等价于 git add -p 但更快
```

**案例2：搜索并切换分支**
```bash
gcb
# fzf 列出所有分支，输入关键字过滤
# 输入 "oee" → 匹配 "feat/oee-enhancement" "bugfix/oee-reset"
```

**案例3：交互式查看 log 和 diff**
```bash
glo   # fzf 搜索 commit message
gd    # fzf 选择文件看 diff
grh   # 交互式 reset HEAD（撤销暂存）
```

**进阶技巧：**
- 所有 forgit 命令本质上是 `git xxx | fzf` 的包装，可以组合自定义
- `FORGIT_LOG_FORMAT` 自定义 `glo` 的输出格式
- `gcf`（git checkout file）从其他分支或 commit 检出一个特定文件

---

## 25. gitui

**前世今生：** gitui 由德国开发者 Stephan Dilly (extrawurst) 于 2020 年创建。他喜欢 lazygit 的概念，但想要一个用 Rust 重写的、更快的、更面向键盘的替代品。gitui 确实做到了"快"——启动几乎瞬时，即使在大仓库（Linux kernel 级别）也能流畅滚动。gitui 的界面设计与 lazygit 不同：选项卡式（tab-based）而非面板式（panel-based），顶部分别是 Status/Log/Stashing/Stashes。Rust 的异步渲染确保 UI 从不会卡顿。

**使用方法与案例：**

安装：
```bash
brew install gitui             # macOS
winget install extrawurst.gitui  # Windows
cargo install gitui            # 从源码
```

**案例1：快速提交**
```bash
gitui
# Tab 1 (Status): 选中文件，按 Enter 查看 diff
# 按 s 暂存选中文件
# 按 c 打开 commit 编辑框，写 message
# Ctrl+D 提交
# 按 p 推送
```

**案例2：搜索 Log**
```bash
# 按 2 切换到 Log 选项卡
# 输入 / 搜索 commit message
# 按 Enter 看选中 commit 的详细 diff
```

**案例3：管理 Stash**
```bash
# 按 3 打开 Stashing
# 按 s 保存当前工作区到 stash
# 按 a 应用 stash
# 按 d 删除 stash
```

**进阶技巧：**
- `theme.ron` 自定义主题（文件路径在 `gitui --help` 中查看）
- 支持 Git Hooks（pre-commit 等）的完整反馈
- 内置文件 blame 视图
- 异步 Git 操作——push 时不阻塞 UI

---

## 26. git-absorb

**前世今生：** git-absorb 由 Facebook 的 Tudor Brindus 于 2018 年在实习期间创建，灵感来自 Mercurial 的 `hg absorb` 功能。问题场景：你写了一个修复，但忘了用 `git commit --fixup`，直接做了新 commit。git-absorb 自动分析工作区的 diff，判断每个改动应该"吸收"到历史的哪个 commit 中（通过 `git blame` 看每行代码最初来自哪个 commit），然后自动执行 fixup。Facebook 的 Monorepo 有数千开发者，这个功能每天节省大量时间。

**使用方法与案例：**

安装：
```bash
brew install git-absorb             # macOS
cargo install git-absorb            # Rust
# Windows: 下载 GitHub Releases 二进制
```

**案例1：自动吸收修复到正确的 commit**
```bash
# 你的历史：
# a1b2c3d feat: add OEE calculator
# e4f5g6h feat: add production report
# i7j8k9l fix: typo
# 当前工作区修改：OEE 公式修正 + 报告日期修正

git absorb
# 自动分析：
# - OEE 公式修改 → fixup 到 a1b2c3d
# - 报告日期修改 → fixup 到 e4f5g6h
# 然后 git rebase --autosquash 就完成了
```

**案例2：指定基准 commit**
```bash
git absorb --base main
# 只考虑 main 之后的 commit
```

**进阶技巧：**
- `git absorb --dry-run` 预览而不执行
- `git absorb --and-rebase` 吸收 + 自动 rebase
- 和 `git commit --fixup` 搭配使用：先自动吸收，再微调

---

## 27. bfg

**前世今生：** bfg（BFG Repo-Cleaner）由 Roberto Tyley 于 2013 年创建，名字来自《毁灭战士》中的 BFG 9000 武器。Tyley 在 Guardian 报社工作时需要清理 Git 仓库中的大文件，发现 `git filter-branch` 极其缓慢。bfg 用 Scala 编写（跑在 JVM 上），核心优化是打包文件层面的处理而非 commit 层面，速度比 `git filter-branch` 快 10-720 倍。GitHub 官方推荐 bfg 作为清理仓库的首选工具。注意：bfg 不处理最新 commit，这是设计特性——让你手动处理最新的，然后 bfg 扫历史。

**使用方法与案例：**

安装：
```bash
brew install bfg             # macOS
# 下载 JAR: bfg-1.14.0.jar
java -jar bfg-1.14.0.jar     # 需要 Java 运行环境
```

**案例1：从历史中删除大文件**
```bash
# 1. 镜像克隆
git clone --mirror https://github.com/myorg/myrepo.git
# 2. 删除 >100M 的大文件
java -jar bfg.jar --strip-blobs-bigger-than 100M myrepo.git
# 3. 清理并推送
cd myrepo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

**案例2：删除敏感文件（密码文件）**
```bash
java -jar bfg.jar --delete-files passwords.txt myrepo.git
java -jar bfg.jar --delete-files "*.pem" myrepo.git    # 删除所有私钥
```

**案例3：替换敏感字符串**
```bash
# 将历史中所有 "sk-abc123" 替换为 "***REMOVED***"
java -jar bfg.jar --replace-text replacements.txt myrepo.git
# replacements.txt 内容：
# sk-abc123==>***REMOVED***
```

**进阶技巧：**
- 先 `git clone --mirror` 做备份，错了能恢复
- 通知所有协作者 force push 后重新 clone（不要 pull）
- `git-filter-repo` 是比 bfg 更新的替代品（Python 编写，更灵活）
- 处理完后用 `git count-objects -vH` 看仓库瘦身了多少

---

## 28. pre-commit

**前世今生：** pre-commit 由 Yelp 的 Anthony Sottile 于 2014 年创建。Sottile 在 Yelp 做代码质量时发现，虽然团队配置了各种 lint 工具（flake8, eslint, prettier），但总会有人忘记在提交前运行。pre-commit 的解决方案是将 lint 工具注册为 Git hooks，在 `git commit` 时自动触发。它的独特设计是"多语言框架"——Hook 可以用 Python、Node.js、Ruby、Go 等不同语言写，pre-commit 自动管理运行时环境（缓存、隔离）。2023 年 pre-commit 成为 Python 生态中最常用的代码质量工具之一。

**使用方法与案例：**

安装：
```bash
pip install pre-commit
brew install pre-commit  # macOS
```

**案例1：Python 项目配置**
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.4.0
    hooks:
      - id: black                 # 自动格式化
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff                  # Lint（替代 flake8）
      - id: ruff-format           # 格式化（替代 isort）
```
```bash
pre-commit install          # 安装 Git hook
pre-commit run --all-files  # 手动运行所有检查
```
现在每次 `git commit` 自动：
1. ruff 检查代码规范
2. black 统一格式
3. 如果失败 → 拒绝提交 + 显示问题列表

**案例2：前端项目配置**
```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.2.0
    hooks:
      - id: prettier             # JS/TS/CSS/HTML/YAML 格式化
  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v9.0.0
    hooks:
      - id: eslint
```

**案例3：综合质量门**
```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks             # 密钥泄露检测
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace  # 删除行尾空格
      - id: end-of-file-fixer    # 文件以换行结尾
      - id: check-yaml           # YAML 语法检查
      - id: check-added-large-files  # 禁止 >500KB 文件
```

**进阶技巧：**
- `pre-commit autoupdate` 自动更新 hook 版本到最新
- `--hook-stage manual` 只在手动触发时运行（如耗时检查）
- CI 中也能跑：`pre-commit run --all-files --show-diff-on-failure`
- 本地 hook：指向本机脚本（如 `entry: ./scripts/validate_config.sh`）

---

## 29. git-filter-repo

**前世今生：** git-filter-repo 由 Elijah Newren（Git 核心贡献者）于 2019 年创建。Newren 在维护 Git 的 `git filter-branch` 时发现其性能和安全问题（容易产生损坏的仓库），于是决定从零重写一个更好的替代品。git-filter-repo 用 Python 编写，比 bfg 更灵活（支持任意 Python 回调过滤），比 filter-branch 快得多。Git 官方于 2022 年正式推荐 git-filter-repo 作为 filter-branch 的替代。它只操作一个仓库的本地拷贝，设计上防止了大多数误用。

**使用方法与案例：**

安装：
```bash
pip install git-filter-repo
# 或下载单个脚本: git-filter-repo (standalone Python file)
```

**案例1：按文件路径切分子仓库（monorepo 拆分）**
```bash
git clone https://github.com/myorg/monorepo.git
cd monorepo
git filter-repo --path services/mes-api/ --path-rename services/mes-api/:
# 原来 services/mes-api/main.py → main.py
# 历史只保留 mes-api 相关的 commit
```

**案例2：修改历史中的作者信息**
```bash
cat > mailmap.txt << 'EOF'
Old Name <old@email.com> <new@email.com>
EOF
git filter-repo --mailmap mailmap.txt
```

**案例3：删除整个文件夹的历史**
```bash
git filter-repo --path secrets/ --invert-paths
# --invert-paths: 删除 secrets/，保留其余所有
# --path-glob "*.exe" --invert-paths: 删除所有 EXE 文件
```

**进阶技巧：**
- `--analyze` 先生成分析报告（不修改仓库）：文件大小、目录结构、活跃分支
- `--refs` 只处理特定分支或标签
- `--force` 强制覆盖（默认拒绝在没有 --force 时操作非全新克隆）
- 比 bfg 快 2-3×，且能处理 bfg 无法处理的复杂场景

---

## 30. gitleaks

**前世今生：** （详见第 109 项安全组 gitleaks，此处做补充视角）

在 Git 工作流中，gitleaks 最核心的价值是 **pre-commit 集成**和 **CI/CD 阻断**。虽然同在第 109 项详细介绍，但这里强调 Git 场景下的最佳实践：

**使用方法与案例（Git 场景特化）：**

**案例1：GitHub Actions CI 自动扫描**
```yaml
# .github/workflows/gitleaks.yml
name: Gitleaks Scan
on: [push, pull_request]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # 获取完整历史
      - uses: gitleaks/gitleaks-action@v2
```
任何 push/PR 自动扫描，发现密钥 → CI 标红。

**案例2：保护特定文件模式**
```toml
# .gitleaks.toml
[[rules]]
id = "mes-api-key"
description = "MES API Key Pattern"
regex = '''MES_API_KEY["']?\s*[:=]\s*["'][A-Za-z0-9+/]{32,}["']'''
tags = ["api-key", "mes"]
```

**进阶技巧（Git 场景）：**
- `gitleaks protect` 替代 pre-commit hook，实时监控暂存区
- 加 `--staged` 只扫描即将提交的内容（更快）
- baseline 机制：`gitleaks detect --baseline-path .gitleaks-report.json` 记录已知告警，下次只看新增

---

*第3组完成 · 下一组: 文件与磁盘管理*
