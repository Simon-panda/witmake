---
created: 2026-06-02
source: Simon 分享的飞书卡片
tags: [claude-code, skills, 学习笔记]
---

# Claude Code 40项技能完整介绍

> 来源：飞书卡片整理 | 2026-06-02 | woker 🤖 搜索整理

---

## 第①组 — 核心开发（1-10）

### 1. Planning with Files
> 📄 基于文件的规划技能

让 Claude Code 在动手编码前，先以文件形式输出完整执行计划。适合复杂项目：先让 AI 在本地写 `.md` 规划文档，确认路线后再执行，避免"边想边写"导致的结构混乱。典型场景：大型重构、新功能架构设计、跨文件变更。

### 2. Superpowers
> ⚡ 开发能力增强套件（社区流行）

一套系统性技能库，核心理念：**测试驱动开发（TDD）优先、复杂度递减、自动化工作流**。提供 `/superpowers:test-driven` 等子命令，强制 Claude 先写测试再写实现、先做计划再编码。解决 Claude 容易"跳过步骤直接写代码"的问题。被多个社区评测评为最值得安装的技能之一。

### 3. Code Review
> 🔍 自动化代码审查（Anthropic 官方）

两种使用方式：
- **GitHub App 集成**：自动在 PR 上发布 inline review 评论，附带 **Claude Code Review** check run
- **本地 CLI**：在终端运行 `/code-review` 审查当前 diff

关注点：正确性 bug、代码复用性、简化空间、效率优化。读取仓库 `CLAUDE.md` 规则，新引入的违规标记为 nit-level 建议。

### 4. Webapp Testing
> 🌐 Web 应用 Playwright 自动化测试

封装 Playwright 测试框架的能力，让 Claude 自动为 Web 应用编写、运行端到端测试。支持：验证前端功能、调试 UI 行为、页面交互测试。开发者只需描述测试场景，Claude 自动生成测试脚本，无需手动写 Playwright 样板代码。

### 5. Code Simplifier
> 🧹 代码简化与质量审查

自动检测代码中的冗余、过度设计、复杂度超标等问题，给出简化建议。内置 `simplify` 子命令，聚焦：减少嵌套层级、消除重复代码、简化条件逻辑、降低圈复杂度。适合做代码重构前的"健康检查"。

### 6. UI UX Pro Max
> 🎨 前端界面与体验设计专家

将 Claude 转变为资深 UI/UX 设计师角色。能分析设计稿、生成风格一致的组件代码、优化布局和交互细节。内置响应式设计、可访问性（a11y）、色彩系统等最佳实践。适用于快速原型开发、设计系统落地。

### 7. MCP Builder
> 🔌 MCP（Model Context Protocol）服务构建器

辅助开发者快速构建 MCP Server。MCP 是 AI Agent 与外部工具/数据源之间的标准协议。该技能封装了 MCP 规范实现，让 Claude 自动生成 Server 骨架、工具定义、传输层（stdio/SSE）代码。适合需要让 AI 连接数据库、API、文件系统等外部资源的场景。

### 8. Ralph Loop
> 🔁 定时/循环任务执行器

在 Claude Code 中实现定时循环执行能力——设定间隔时间或触发条件，让 Claude 自动重复执行特定任务。典型用途：定期检查项目状态、持续监控日志、批量处理文件。底层基于 Claude Code 的 `/loop` 命令机制。

### 9. PPTX
> 📊 PPT 文档自动生成

让 Claude 直接生成 `.pptx` 文件（PowerPoint 格式），无需手动制作幻灯片。支持自定义模板、图表插入、排版布局。输入大纲或 Markdown 内容，自动转化为多页 PPT。适合技术方案汇报、项目进度演示、培训材料的快速产出。

### 10. Skill Creator
> 🛠️ 自定义技能生成器

让 Claude 通过对话引导你创建属于自己的 Skills。你只需描述想实现的功能，Skill Creator 自动生成 `SKILL.md` 文件（含 YAML frontmatter + 指令内容），并放置到正确的 `.claude/skills/` 目录。降低了技能开发门槛。

---

## 第②组 — 代码工程（11-20）

### 11. Context Pack
> 📦 上下文打包与注入

将项目相关的关键上下文（架构文档、API 规范、数据库 Schema、配置规则等）打包成一个结构化文件，在启动新会话时自动注入 Claude 的上下文窗口。解决"每次新会话都要重新解释项目背景"的问题。

### 12. Repo Cartographer
> 🗺️ 仓库地图绘制器

自动扫描整个代码仓库，生成项目结构地图——包括目录树、模块依赖关系、关键入口点、数据流向。帮助 Claude 快速理解陌生项目的全貌，类似于给 AI 一张"代码地图"再进行开发工作。

### 13. Test Pilot
> 🧪 自动化测试飞行员

为项目自动生成并维护测试套件。识别代码变更后自动补充单元测试、集成测试，覆盖边界条件和异常场景。支持主流测试框架（Jest、Vitest、pytest 等），确保新代码不会破坏已有测试。

### 14. Debug Radar
> 🐛 调试雷达

系统化排除 bug 的调试框架。分析报错栈、日志、运行时状态，给出可能的根因排序和验证步骤。集成了二分定位、日志注入、变量追踪等调试手法。遇到难复现的 bug 时引导 Claude 像资深工程师一样逐步缩小排查范围。

### 15. Refactor Lens
> 🔧 重构透镜

从全仓库视角分析代码质量，识别可重构的热点区域。重点检测：过长函数、过大类、重复代码、不合理耦合、违反 SOLID 原则等问题。对每个问题给出重构方案和预期收益评估。

### 16. API Stitcher
> 🔗 API 缝合器

连接和编排多个外部 API 的胶水代码生成器。自动处理：认证方式适配、数据格式转换、错误重试机制、接口调用顺序编排。输入 API 文档链接或 OpenAPI 规范，自动生成调用代码。

### 17. Migration Buddy
> 📦 迁移助手

处理代码/数据/框架迁移的向导工具。支持：语言迁移（JS→TS、Python 3.x 升级）、框架升级（React 16→18、Vue 2→3）、数据库迁移（Schema 变更、数据映射）。自动识别兼容性问题，生成迁移脚本和回滚方案。

### 18. Docs Whisperer
> 📝 文档低语者

从代码库自动生成高质量文档。扫描源码中的 JSDoc、类型定义、README 模式，生成：API 参考文档、内部 Wiki 页面、变更日志、使用示例。支持输出 Markdown 或直接写入飞书/Notion 等文档平台。

### 19. Prompt Harness
> 🎯 提示词工程工作台

为开发 AI 应用（特别是 LLM 调用）设计的提示词调试与测试框架。支持：Prompt 版本管理、多模型对比测试、边缘 case 覆盖、输出格式验证。可以批量跑 Prompt 测试用例并产出质量报告。

### 20. Ship Checklist
> ✅ 发布检查清单

代码发布前的自动化合规检查器。核对：代码审查是否完成、测试覆盖率和通过率、依赖安全扫描、文档是否更新、变更日志是否追加、版本号是否正确递增。输出可视化的"发版就绪度"报告。

---

## 第③组 — 自动化（21-30）

### 21. Agent Swarm
> 🐝 多 Agent 集群

在单次 Claude Code 会话中启动多个子 Agent（subagents）并行工作。将一个大型任务拆分为多个小任务，分派给不同 Agent 同时执行，最后汇总结果。适合：大规模代码重构、多模块并行开发、批量文档生成。

### 22. Playwright Scout
> 🕵️ 浏览器自动化侦察兵

基于 Playwright 的 Web 自动交互与数据采集工具。不同于 Webapp Testing 的"写测试"，Playwright Scout 擅长：页面交互、数据抓取、表单填写、截图对比。可以理解页面结构并自动生成选择器。

### 23. Terminal Sense
> 💻 终端感知

增强 Claude 对终端命令执行的感知能力。自动分析命令输出、检测错误模式、建议修复命令。支持：日志分析、进程管理、网络诊断。让 Claude 在终端操作中更"懂你在干什么"。

### 24. CI Fixer
> 🛠️ CI 流水线修复器

CI 构建失败时的自动诊断与修复专家。分析 CI 日志 → 定位失败步骤 → 判断问题类型 → 给出修复方案或直接提交修复。支持 GitHub Actions、GitLab CI、Jenkins 等主流 CI 平台。

### 25. Release Notes
> 📋 发布说明自动生成器

基于 Git 提交历史、PR 标题和标签、Issue 关联，自动生成结构化的 Release Notes。支持按版本聚合、分类展示（新功能/Bug 修复/性能优化/破坏性变更）。输出格式可定制：Markdown、HTML 邮件、飞书消息卡片。

### 26. Data Cleaner
> 🧹 数据清洗工

处理数据质量问题的自动化工具。支持：检测并处理缺失值/重复值/异常值、格式统一、敏感信息脱敏、数据格式转换。适合数据分析前的预处理、系统间数据迁移清洗、数据合规脱敏。

### 27. Screenshot QA
> 📸 截图质量检测

自动截取 Web 页面截图并与基准截图对比，检测 UI 差异。支持：视觉回归检测（像素级 diff）、响应式布局验证（多分辨率截图）、多浏览器渲染对比。生成差异标记图和高亮报告。

### 28. Changelog Miner
> ⛏️ 变更日志挖掘机

从 Git 历史中深入挖掘代码变更模式和趋势。分析：哪些模块变更最频繁、什么类型的提交最多、代码热区在哪里。输出可视化报告，帮助了解项目演进的健康状况。

### 29. Dependency Guard
> 🔒 依赖守卫

依赖包安全与健康度检查器。自动扫描依赖文件，检查：已知 CVE 漏洞、许可证合规性、版本过时情况、依赖树深度。发现风险依赖时给出升级建议或替代方案。

### 30. Nightly Runner
> 🌙 夜间自动化运行器

配置定时任务，让 Claude 在夜间自动执行重复性工作。典型用途：每日代码质量扫描、自动化测试跑批、数据报表生成、依赖更新检查。可配置失败告警通知（企业微信/飞书/邮件）。

---

## 第④组 — 协作与安全（31-40）

### 31. Spec Aligner
> 📐 规格对齐器

确保代码实现与需求规格/API 规范保持一致。对比：技术设计文档 vs 实际代码逻辑、OpenAPI 规范 vs 接口实现、数据库 Schema vs ORM 模型定义。发现偏差时标记差异并建议修正。

### 32. PR Narrator
> 📖 PR 叙述者

自动为 Pull Request 生成高质量的描述内容。分析 diff 变更 → 理解变更意图 → 生成结构化的 PR 描述（做什么/为什么做/影响范围/测试说明/需关注要点）。让 PR 过程更规范、Reviewer 理解更快。

### 33. Review Router
> 🚦 审查路由分配器

智能分配代码审查任务。根据 PR 变更涉及的模块、文件类型、修改复杂度，自动推荐最合适的 Reviewer。支持规则配置：按技术栈匹配、按负载均衡分派、按专家领域定向。

### 34. Decision Log
> 📜 决策日志

记录团队技术决策的全过程。每次关键决策自动生成结构化记录：背景→方案对比→决策依据→预期影响→参与人。类似 ADR（Architecture Decision Records）的自动化版。

### 35. Issue Gardener
> 🌱 Issue 花园园丁

自动化管理 Issue 生命周期：新 Issue 分类打标签 → 自动关联类似 Issue → 标记重复 → 追踪处理进度 → 关闭时验证解决方案。支持与飞书/企微/Jira 等工具联动。

### 36. Design Sync
> 🎨 设计同步器

确保前端实现与设计稿保持一致。分析 Figma 设计稿链接或导出的设计规范 → 对比已有组件库代码 → 标记 UI 差异。支持自动生成缺少的样式变量或组件代码。

### 37. Security Scout
> 🛡️ 安全侦察兵

代码安全漏洞主动扫描器。从源码层面检测：注入攻击风险、认证绕过漏洞、敏感信息硬编码、不安全的第三方依赖。与 Dependency Guard 互补——Guard 管外部依赖，Scout 管内部代码安全。

### 38. Hot Reload
> 🔄 热重载

开发过程中的实时反馈引擎。当代码变更时自动：重新编译/打包 → 运行相关测试 → 刷新预览 → 报告变更影响范围。减少"改代码→切终端→等编译→手动刷新"的摩擦。

### 39. Codebase Onboard
> 🚀 代码库入职向导

新成员接入项目时的自动导航器。分析仓库结构 → 生成项目入门文档（架构概览/开发环境搭建/核心流程/常见问题）。新开发者输入 `/onboard` 即可获得定制化项目漫游指南。

### 40. Security Compliance
> 📋 安全合规检查器

安全规范与行业标准的自动合规审计。支持对照：OWASP Top 10、ISO 27001、等保 2.0、CIS Benchmarks 等标准，逐项检查代码库和配置的合规情况。输出合规差距分析报告和修复优先级排序。

---

## 四组速览

| 组别 | 编号 | 名称 | 一句话定位 |
|------|:----:|------|-----------|
| **①核心开发** | 1 | Planning with Files | 文件级规划先行 |
| | 2 | Superpowers | TDD+系统化开发增强 |
| | 3 | Code Review | 自动化PR审查 |
| | 4 | Webapp Testing | Playwright端到端测试 |
| | 5 | Code Simplifier | 代码质量审查与简化 |
| | 6 | UI UX Pro Max | 资深UI/UX设计专家 |
| | 7 | MCP Builder | MCP服务快速构建 |
| | 8 | Ralph Loop | 定时循环任务 |
| | 9 | PPTX | PPT自动生成 |
| | 10 | Skill Creator | 自定义技能生成 |
| **②代码工程** | 11 | Context Pack | 项目上下文打包 |
| | 12 | Repo Cartographer | 仓库结构地图 |
| | 13 | Test Pilot | 自动化测试生成与维护 |
| | 14 | Debug Radar | 系统化调试框架 |
| | 15 | Refactor Lens | 代码重构热点分析 |
| | 16 | API Stitcher | 多API编排代码生成 |
| | 17 | Migration Buddy | 代码/框架迁移助手 |
| | 18 | Docs Whisperer | 自动文档生成 |
| | 19 | Prompt Harness | Prompt测试工作台 |
| | 20 | Ship Checklist | 发布合规检查 |
| **③自动化** | 21 | Agent Swarm | 多Agent并行执行 |
| | 22 | Playwright Scout | 浏览器自动化侦察 |
| | 23 | Terminal Sense | 终端输出智能分析 |
| | 24 | CI Fixer | CI故障自动修复 |
| | 25 | Release Notes | 发布说明自动生成 |
| | 26 | Data Cleaner | 数据清洗与脱敏 |
| | 27 | Screenshot QA | UI视觉回归检测 |
| | 28 | Changelog Miner | Git变更趋势分析 |
| | 29 | Dependency Guard | 依赖安全扫描 |
| | 30 | Nightly Runner | 夜间批量任务执行 |
| **④协作与安全** | 31 | Spec Aligner | 代码vs规格一致性检查 |
| | 32 | PR Narrator | PR自动描述生成 |
| | 33 | Review Router | Reviewer智能分配 |
| | 34 | Decision Log | 技术决策记录 |
| | 35 | Issue Gardener | Issue生命周期管理 |
| | 36 | Design Sync | 设计稿vs代码同步 |
| | 37 | Security Scout | 源码安全漏洞扫描 |
| | 38 | Hot Reload | 变更实时反馈 |
| | 39 | Codebase Onboard | 新成员项目导航 |
| | 40 | Security Compliance | 安全合规审计 |
