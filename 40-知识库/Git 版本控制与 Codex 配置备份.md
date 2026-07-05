---
tags: [Git, Codex, 工具, 版本控制]
created: 2026-06-21
---

# Git 版本控制与 Codex 配置备份

## Codex 配置仓库概况

| 项目 | 详情 |
|------|------|
| 仓库路径 | `C:\Users\ASUS\Documents\Codex\config-repo\` |
| 管理文件 | `config.toml`、`.gitignore`、`rules/`、`sync-config.ps1`、`daily-backup.ps1` |
| 分支策略 | 主干开发（`master` 直接提交） |
| 本地备份 | `D:\backup\codex-config.git`（裸仓库） |
| 同步脚本 | `sync-config.ps1 -Commit` → 拷贝 + 提交 + 推送 |

## Git 核心概念（制造管理者视角）

| 制造概念 | Git 等价物 | 说明 |
|----------|-----------|------|
| 工艺卡版本号 | **commit** | 每次修改的完整快照，带时间戳和责任人 |
| 换模记录 | **git log** | 谁、什么时候、改了什么、为什么改 |
| 回退到上一版工艺 | **git revert / reset** | 改坏了可以回到上一个确定好的版本 |
| 主产线 + 试验线 | **分支（branch）** | `master` 是主产线（稳定），`feat/xxx` 是试验线 |
| 异地备份 | **远程仓库（remote）** | 推送到外部存储，本机炸了也能恢复 |
| 工艺变更审批单 | **Pull Request** | 改完让别人看过再合入主分支 |

核心价值：**可追溯、可回滚、可备份。**

## 当前配置

### 远程仓库

```bash
# 查看
git remote -v

# 输出：
# backup  D:/backup/codex-config.git (fetch)
# backup  D:/backup/codex-config.git (push)
```

### sync-config.ps1 工作流

```
sync-config.ps1 -Commit
  ├─ 拷贝 ~/.codex/config.toml → 仓库
  ├─ 拷贝 ~/.codex/.gitignore → 仓库
  ├─ 拷贝 ~/.codex/rules/     → 仓库
  ├─ git diff → 有变化则 git commit
  ├─ git push backup master   → D:\backup
  └─ 完成
```

## 日常操作速查

| 场景 | 命令 | 说明 |
|------|------|------|
| 看看改了什么 | `git status` | 工作区状态 |
| 看具体差异 | `git diff` | 行级对比 |
| 保存修改 | `git add -A && git commit -m "..."` | 提交快照 |
| 推送到备份 | `git push backup` | 同步到 D 盘 |
| 看历史 | `git log --oneline -10` | 提交日志 |
| 回退一个提交 | `git revert HEAD` | 保留记录的撤回 |
| 丢弃未保存 | `git checkout -- <file>` | 回到上一版 |
| 紧急恢复 | `git reflog` | 30 天内操作日志 |

## 提交信息规范

格式：`<类型>: <简短描述>`

| 前缀 | 用途 |
|------|------|
| `feat:` | 新功能/新文件 |
| `fix:` | 修复问题 |
| `chore:` | 杂项/维护 |
| `docs:` | 文档 |
| `refactor:` | 重构 |

## 后续待办

- [ ] 添加真正的异地备份（GitHub 私有仓库）
- [ ] 考虑用分支工作流（改配置前开分支，验证后合入）
