---
title: Hermes ↔ Codex 双引擎通讯协议 v5
date: 2026-06-08
tags: [AI基础设施, 通讯协议, Hermes, Codex, 技术架构]
---

# Hermes ↔ Codex 双引擎通讯协议 v5

## 背景

Simon 的 AI 体系包含两个核心引擎：

| 系统 | 名称 | 定位 | 核心能力 |
|------|------|------|---------|
| **Hermes** | Woker | 数字合伙人 | 生产运营分析、多通道通讯（企微/飞书/Telegram）、Obsidian 知识库、日报/周报/简报自动生成、ERP/MES 数据管道、跨平台自动化、经营决策辅助 |
| **Codex Desktop** | Codex | 编程工作站 | 代码编写/重构/审查、脚本开发、技术调研、文档/PPT/图表生成、副业系统集成项目编码 |

## 通道演进史

| 版本 | 日期 | 方案 | 结果 |
|------|------|------|------|
| v1 | 06-08 | 初始文件 Handoff（无消费端） | ❌ Hermes 端无人读文件 |
| v2 | 06-08 | watcher + tracker 状态文件 | ❌ tracker 提前打勾，agent 失败后永不重试 |
| v3 | 06-08 | LLM agent cron 管道 | ❌ `[SILENT]` 静默退出 |
| v4 | 06-08 | no_agent 纯脚本管道 | ⚠️ Codex 沙箱阻止写入 `~/workspace/` |
| **v5** | **06-08** | **软链接透明桥** | **✅ 当前生效** |

## v5 架构

```
Codex 写入物理路径:     ~/Documents/Codex/shared-handoff/
         ↕ 软链接
Hermes 读取逻辑路径:      ~/workspace/handoff/
```

**核心原理：** Codex Desktop 沙箱允许写入 `~/Documents/Codex/`，但阻止写入 `~/workspace/`。将物理文件放在 Codex 可写区，Hermes 通过软链接透明读取，双方互不感知。

### 目录结构

```
~/Documents/Codex/shared-handoff/
├── CHANNEL_STATUS.md          # 通道状态文件（双方可读，Hermes 维护）
├── to-hermes/                 # Codex → Hermes 请求
│   └── archive/               # 已处理归档
└── from-hermes/               # Hermes → Codex 回复/通知

~/workspace/handoff/
├── to-hermes  → (软链接到 ↑)
└── from-hermes → (软链接到 ↑)
```

### 自动管道

- **Cron Job ID**: `2e9dbdc47b86`
- **周期**: 每 5 分钟
- **脚本**: `~/.hermes/scripts/handoff_responder.py`
- **模式**: `no_agent=true`（纯 Python 脚本，零 LLM 调用）

## Codex → Hermes 通讯

### 请求格式

Codex 写 `.md` 到 `~/Documents/Codex/shared-handoff/to-hermes/`：

```markdown
# 请求：<描述>
From: Codex
Created: YYYY-MM-DD HH:MM Asia/Shanghai

<正文>
```

### 响应

Cron 每 5 分钟处理一次，回复出现在 `~/Documents/Codex/shared-handoff/from-hermes/`，文件名 `request-` → `response-`。

### 等待策略

- 等待最多 5 分钟
- 超过 10 分钟无响应：读 `CHANNEL_STATUS.md` 诊断

## Hermes → Codex 通讯

### 通知格式

Hermes 写 `notice-from-hermes-YYYYMMDD-HHMM.md` 到 `~/Documents/Codex/shared-handoff/from-hermes/`：

```markdown
# Hermes → Codex 通知：<主题>
From: Hermes
To: Codex
Created: YYYY-MM-DD HH:MM Asia/Shanghai
Priority: normal

<通知内容>

Requested action:
- <希望 Codex 执行的操作>
```

### 触发方式

Hermes 不在 Codex 后台常驻 watcher。需要 Simon 对 Codex 说"检查 Hermes 通知"来触发读取。

## 共享资源

### 技能桥
`~/.codex/skills/hermes-inherited/` — 13 个 Hermes 技能，Codex 只读访问：
- `manufacturing/` — CNC 工艺、IATF 审核、排程、质量、刀具管理
- `enterprise-ops-analysis` — 经营数据 Excel 分析
- `daily-report-analysis` — 员工日报 NLP 分析
- `evalagent` — AI Agent 评估
- `obsidian/` — Obsidian 知识库读写
- 工程、测试、调试等相关技能

### 上下文文件
- `~/.codex/AGENTS.md` — Codex 启动时读取，包含完整协作协议
- `~/.codex/company-context.md` — 公司业务背景

## 故障排查

| 症状 | 检查 |
|------|------|
| Codex 写入失败 | 确认路径用的是 `~/Documents/Codex/shared-handoff/`，不是 `~/workspace/handoff/` |
| 无响应超过 10 分钟 | `cronjob list` 检查 `2e9dbdc47b86` |
| 软链接断开 | `ls -la ~/workspace/handoff/` 确认软链接指向正确 |
| 通道状态不明 | 读 `CHANNEL_STATUS.md` |

## 自修正机制

1. 通道状态变更 → Hermes 更新 `CHANNEL_STATUS.md` 和 `AGENTS.md`
2. Codex 发现通道问题 → 写诊断到 `to-hermes/` → cron 自动响应
3. Hermes 活跃会话中评估修复方案 → 直接修改配置文件和脚本

## 相关文件

- `~/Documents/Codex/shared-handoff/CHANNEL_STATUS.md` — 通道状态
- `~/.codex/AGENTS.md` — Codex 全局指南（含 Handoff 协议章节）
- `~/.hermes/scripts/handoff_responder.py` — 自动响应脚本
- `~/.hermes/skills/autonomous-ai-agents/codex-handoff/SKILL.md` — Hermes 端协作 skill
