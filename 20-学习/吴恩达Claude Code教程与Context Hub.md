# 吴恩达 Claude Code 最新教程与开源项目

**来源：** Simon 要求查找
**日期：** 2026-05-17 整理

---

吴恩达（Andrew Ng）2026年在 Claude Code / Coding Agent 方向有两个重要产出：**一门免费课程** 和 **一个开源项目**。

---

## 一、Claude Code 课程（免费）

### Claude Code: A Highly Agentic Coding Assistant

- **平台：** [DeepLearning.AI](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)
- **合作方：** Anthropic
- **讲师：** Elie Schoppik（Anthropic 技术教育主管）
- **时长：** ~2小时短课
- **费用：** 免费
- **先修：** 熟悉 Python + Git

#### 课程内容（10节）

| 章节 | 内容 |
|------|------|
| 1 | Claude Code 架构：工具链、代码库导航方式、跨会话记忆机制 |
| 2 | 探索 RAG 聊天机器人代码库，理解前端/后端数据流 |
| 3 | 创建 `CLAUDE.md` 文件 — 跨会话记忆指南 |
| 4 | 给 Claude Code 提供上下文：引用文件、截图/图片、escape/clear/compact 命令 |
| 5 | 新增功能：先规划再执行、思考模式（thinking mode）处理复杂任务、Subagents |
| 6 | 编写测试、重构 RAG 聊天机器人 |
| 7 | Git Worktrees — 同时运行多个 Claude 会话并行开发 |
| 8 | GitHub Issues → PR 创建/审查/合并的集成 |
| 9 | Claude Code Hooks — 工具执行前后自动执行脚本 |
| 10 | **三大实战项目：**
  - 重构电商 Jupyter Notebook → 仪表盘
  - Figma MCP Server 接入 → 从设计稿生成 Web 界面
  - Playwright MCP Server 自动浏览器截图 → 改善 UI 设计 |

#### 核心技能点

- 用 `CLAUDE.md` 持久化项目上下文（跨会话记忆）
- MCP Server 扩展（Figma、Playwright 等）
- Git Worktrees 并行开发
- Hooks 自动化（pre/post tool events）
- Subagents 协同

---

### Agent Skills with Anthropic（补充课程 — 资料已下载 ✅）

- **平台：** [DeepLearning.AI](https://www.deeplearning.ai/courses/agent-skills-with-anthropic)
- **讲师：** Anthropic 团队
- **定位：** 学习如何构建、配置和分享 Claude Code 的 **Skills**（可复用的 Markdown 指令集）
- **核心概念：** SKILL.md → 渐进式上下文暴露（progressive disclosure）
- **关联工具：** 与我们 OpenClaw Skills 机制异曲同工
- **本地路径：** `~/Documents/Obsidian-Vault/20-学习/sc-agent-skills-files/`

#### 课程大纲（L1-L7）

| 章节 | 核心内容 |
|------|----------|
| L1 Part I | 入门：分析营销活动数据，用 Skill 替代原生 Prompt（对比效果）|
| L1 Part II | 什么是Agent Skills — 模块化可复用的技能包 |
| L2 | Why Use Skills — Skills 的意义，从 Agent 角度思考 Skills |
| L3 | 构建高级 Skill：品牌设计规范 Skill（含 Logo/参考文件打包）|
| L4 | 自定义 Skill 捆绑脚本（Python代码） → 时序分析 + 自动出题 |
| L5 | Skills 可组合使用（Composable）→ 数据 + 脚本 + 引用文件 → 报告生成 |
| L6 | Subagents + Skills 集成：Claude Code 中配置 Subagent 专用 Skills |
| L7 | Skills 在 Claude API 和 Claude Agent SDK 中的使用 |

#### 课程资料结构

| 目录 | 内容 |
|------|------|
| `L1-partI/` | 营销报告 Skill 示例 + Prompt 对比（有Skill vs 无Skill）+ CSV 数据 |
| `L1-partII/` | 概念阅读材料 |
| `L2/` | Skills 意义讲解 |
| `L3/` | 品牌设计规范 Skill（含 Logo PNG + 品牌指南引用）|  
| `L4/` | 自定义 Skill：时序分析（含 Python 脚本）+ 自动出题（含 LaTeX 模板）|
| `L5/` | Skills 组合使用：数据+脚本+模版 → 完整报告输出（IPython Notebook）|
| `L6/` | 完整 Python CLI 项目 + Subagents（code-reviewer/test-generator）+ 3个 Skills |
| `L7/` | 基于 Claude API 的 Multi-Agent 系统（main_agent + 3个子Agent Prompt）|
| `L7_notes/` | 学习 MinerU 工具的学习路径 + 代码示例 |

> Agent Skills 的核心思想与我们 OpenClaw 的 Skills 机制（SKILL.md）非常相似，可以交叉借鉴最佳实践。

---

## 二、Context Hub（chub）— 开源项目

- **GitHub：** [andrewyng/context-hub](https://github.com/andrewyng/context-hub)
- **发布时间：** 2026年3月
- **定位：** 给 Coding Agent 补一层"长期缺失的上下文基础设施"

### 痛点

1. **API 幻觉** — Agent 调用的 API 版本/参数已过时
2. **会话遗忘** — 上次踩的坑，新会话又重来一次

### 核心设计

```
npm install -g @aisuite/chub
```

| 命令 | 功能 |
|------|------|
| `chub search <query>` | 搜索文档/Skills |
| `chub get <id> --lang py\|js` | 按 ID 获取指定语言版本的文档 |
| `chub annotate <id> <note>` | 为文档添加本地注解（跨会话持久化） |
| `chub annotate --clear` | 清除注解 |
| `chub annotate --list` | 列出所有注解 |
| `chub feedback <id> up\|down` | 为文档打分（反馈给维护者） |

### 架构亮点

| 特性 | 说明 |
|------|------|
| 文档即 Markdown + YAML Frontmatter | 任何人可通过 PR 贡献内容和 Skills |
| 增量获取 | `--file` 指定引用文件，省 token |
| 本地注解 → 跨会话记忆 | Agent 踩过的坑，下回自动知道 |
| 公共反馈 → 文档持续改善 | 反馈流回维护者 |
| 版本化 + 语言区分 | `--lang py\|js` 等 |

### 使用方式

**推荐集成到 Claude Code：**
```bash
# 创建 Skill 目录
mkdir -p ~/.claude/skills/get-api-docs
# 放入 SKILL.md 让 Claude 学会用 chub
```

或者在 prompt 中直接指示：
> "Use the CLI command **chub** to get the latest API documentation. Run 'chub help' to understand how it works."

---

## 三、与我们的潜在关联

| 项目 | 关联场景 |
|------|----------|
| **Claude Code 课程** | Simon 的自动化系统集成公司有 AI 大模型应用小组，Claude Code 的 MCP/Subagents/Skills 体系可直接落地为内部开发工具链 |
| **Context Hub** | 企业内部的 API/工具文档可以用 chub 格式组织，让 AI Agent 直接引用，解决"文档版本滞后"和"经验无法复用"两个老问题 |
| **Agent Skills 课程** | Skills 机制与 OpenClaw Skills（SKILL.md）理念一致，可交叉参考最佳实践 |
| **NPM 安装 @aisuite/chub** | 可在本地直接体验 `chub search/get/annotate` |

---

## 四、课程资料本地下载（已拉取 ✅）

课程官方 GitHub 仓库已 clone 到本地：

**路径：** `~/Documents/Obsidian-Vault/20-学习/sc-claude-code-files/`

### 目录结构

| 路径 | 内容 |
|------|------|
| `reading_notes/L0-L8_notes.md` | 每节课详细笔记（含Prompt原文） |
| `updated_reading_notes/` | 更新后的笔记 + Prompt汇总 |
| `lesson7_files/` | 电商数据分析完整案例（原始+重构Notebook、Python模块、数据集） |
| `additional_files/` | L1可视化HTML、L8 Figma设计稿二进制文件 |
| `links_to_course_repos.md` | 实战项目GitHub链接（RAG Chatbot / FRED Dashboard） |

### 讲义核心内容概览

| 章节 | 核心知识点 |
|------|-----------|
| L1 | 安装、环境配置、VS Code集成 |
| L2 | RAG系统架构概览 + `CLAUDE.md` + `#`记忆 + `/init`命令 |
| L3 | 新增功能：先规划后执行 + `@`引用文件 + thinking mode + subagents |
| L4 | 测试编写、错误调试、代码重构 |
| L5 | Git Worktrees 多会话并行开发 |
| L6 | GitHub Issues → PR创建/审查/合并 + Hooks |
| L7 | Jupyter Notebook重构 → 仪表盘 |
| L8 | Figma MCP → Playwright MCP → Web应用UI迭代 |

### 课程三大实战项目代码仓库

1. **RAG Chatbot**（L2-6）：[starting-ragchatbot-codebase](https://github.com/https-deeplearning-ai/starting-ragchatbot-codebase.git) → [final](https://github.com/https-deeplearning-ai/ragchatbot-codebase.git)
2. **电商数据分析Dashboard**（L7）：课程文件内 `lesson7_files/`
3. **FRED Dashboard + Figma**（L8）：[FRED-dashboard](https://github.com/https-deeplearning-ai/FRED-dashboard.git)

## 五、快速入口

- **Claude Code 课程：** https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant
- **Agent Skills 课程：** https://www.deeplearning.ai/courses/agent-skills-with-anthropic
- **Context Hub 项目：** https://github.com/andrewyng/context-hub
- **Context Hub NPM包：** `npm install -g @aisuite/chub`
