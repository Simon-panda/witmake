# Wiki Log — 智机工业知识库

> **操作日志**。追加模式，记录所有知识库操作。
> 格式：`## [YYYY-MM-DD] action | subject`
> 操作类型：ingest, create, update, query, lint, archive, delete
> 超过 500 条后轮转：重命名为 `log-YYYY.md`，新建此文件。
> Agent 维护——每次操作后追加。

---

## [2026-07-05] create | LLM Wiki 模式初始化

### 基于 Karpathy LLM Wiki 模式建立知识库基础设施

**创建的文件：**
- `SCHEMA.md` — 结构约定、标签分类、页面类型、操作规范
- `index.md` — 内容目录，按域分节，涵盖现有主要页面
- `log.md` — 本文件，操作日志
- `raw/` 目录 — 不可变源材料层（articles/, papers/, transcripts/, assets/）

**背景：**
分析了 Karpathy 的 [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)（最后更新 2026-07-05），对比已有 `llm-wiki` skill (v2.1.0)，确认 skill 已包含全部原文内容并扩展了工程化细节（来源溯源标记、置信度标注、sha256漂移检测、12点Lint等）。

**现有 Vault 诊断：**
- ✅ 内容丰富，覆盖 10+ 域
- ✅ 已使用数字前缀分层目录（PARA-like）
- ❌ 缺少 SCHEMA.md（无统一约定）
- ❌ 缺少 index.md（无内容目录）
- ❌ 缺少 log.md（无操作记录）
- ❌ 缺少 raw/ 层（源材料与合成页面混放）
- ❌ 根目录有 `未命名.md`、`未命名.canvas` 等孤立文件
- ❌ macOS 资源分支文件（`._` 前缀）散落各处

**下一步：全部完成 ✅**
- ✅ 创建 raw/ 目录结构
- ✅ 将 Karpathy LLM Wiki 原文收入 raw/articles/
- ✅ 清理根目录：删除 6 个未命名文件 + 242 个 macOS 资源分支文件
- 为关键页面逐步补充 frontmatter（持续）

---

## [2026-07-05] cleanup | 清理孤立文件与资源分支

**删除的文件：**
- `未命名.md`（空文件，0字节）
- `未命名.canvas`, `未命名 1.canvas`, `未命名 2.canvas`, `未命名 3.canvas`, `未命名 4.canvas`（空画布，各2字节）
- `未命名/` 和 `未命名 1/` 空目录
- 242 个 macOS 资源分支文件（`._` 前缀），分布在 `00-Inbox/`, `10-工作/`, `20-学习/`, `30-项目/`, `40-知识库/` 各子目录

---

## [2026-07-05] update | 批量补充 frontmatter + 源材料入库

**补充 frontmatter 的页面（5个）：**
- `30-项目/企业级数据Agent落地方案.md` — type:project, domain:工程, tags:[AI, agent, text-to-sql, 数据管道, 方案, 语义模型, Skill]
- `30-项目/企业级数据Agent落地方案v2.md` — type:project, domain:工程, tags:[AI, agent, text-to-sql, 主动智能层, MCP, 方案, 语义模型, Skill, 风险目录]; supersedes v1.0
- `90-工程/主动智能层/主动智能层_首批风险清单与架构方案.md` — type:project, domain:工程, tags:[AI, agent, 主动智能层, 风险目录, 预测, 根因分析, CNC, 方案]
- `90-工程/主动智能层/主动智能层_优化版实施方案.md` — type:project, domain:工程, tags:[AI, agent, 主动智能层, 方案, 路线图, 成本模型, 降级方案, 组织变革]
- `90-工程/主动智能层/工作分配与API建设深度拆解.md` — type:project, domain:工程, tags:[AI, agent, MCP, API, 刀具磨损, RACI, 主动智能层, 方案]

**收入 raw/articles/ 的源材料（5个）：**
- `raw/articles/karpathy-llm-wiki-2026-07.md` — Karpathy LLM Wiki gist 原文
- `raw/articles/infoq-data-agent-2026-07.md` — InfoQ 企业数据Agent文章（从v1.0方案中提取）
- `raw/articles/主动智能层_首批风险清单与架构方案.md` — 复制自 90-工程/主动智能层/
- `raw/articles/主动智能层_优化版实施方案.md` — 复制自 90-工程/主动智能层/
- `raw/articles/工作分配与API建设深度拆解.md` — 复制自 90-工程/主动智能层/

**更新 index.md**：新增 `源材料 (raw/articles/)` 节，添加 5 个条目。
