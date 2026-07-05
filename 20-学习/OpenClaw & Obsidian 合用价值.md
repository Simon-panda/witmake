# OpenClaw & Obsidian 合用价值

> 整合编制：woker 🤖 | 2026-05-04
> 来源：Kimi 对话（https://www.kimi.com/share/19df31df-a962-83da-8000-0000ea44f737 + https://www.kimi.com/share/19df3210-dbe2-8413-8000-0000c2be9c26）

## 一、核心定位：各自负责什么

| 角色 | 职责 | 特点 |
|------|------|------|
| **OpenClaw** | AI智能体 — 对话交互、自动化任务、跨工具编排 | 连接数据层与知识层，驱动AI推理 |
| **Obsidian** | 知识库 — 存储人类可读的经验、报告、决策记录 | Markdown原生、双向链接、本地私有 |

> **核心原则：Obsidian不存原始机器数据，只存经过提炼的人类知识。**

## 二、制造业数据分层架构

```
┌─────────────────────────────────────────────┐
│  知识层（Obsidian / 知识图谱 / 向量数据库） │ ← 人类可读、AI可推理
│  故障案例、工艺诀窍、维修记录、改进方案        │
├─────────────────────────────────────────────┤
│  分析层（时序数据库 + OLAP / AI推理引擎）    │ ← 机器计算、实时分析
│  趋势预测、异常检测、根因分析、报表生成        │
├─────────────────────────────────────────────┤
│  数据层（时序数据库 / 数据湖）               │ ← 原始数据、长期归档
│  传感器时序数据、PLC日志、质检原始值           │
├─────────────────────────────────────────────┤
│  采集层（边缘网关 / SCADA / MQTT Broker）    │ ← 实时接入
│  设备PLC → 边缘计算 → 云端/本地              │
└─────────────────────────────────────────────┘
```

### 各层推荐工具

| 层级 | 推荐方案 | 说明 |
|------|----------|------|
| **采集层** | MQTT + EMQ X / OPC UA网关 / 自研采集器 | 开源免费，400台并发无压力 |
| **数据层** | TDengine（时序库）/ MinIO（对象存储） | 原始秒级数据保留30天，分钟级1年，小时级永久 |
| **分析层** | Gemma 3 27B / DeepSeek V3（本地部署） | 本地部署，禁止工艺数据出域 |
| **知识层** | Milvus（向量检索）+ Neo4j（知识图谱）+ Obsidian（笔记） | 混合方案，取各自所长 |

### 推荐最终架构

```
应用层：OpenClaw / 自研AI助手
    ↑
推理层：Gemma 3 27B / DeepSeek V3（本地部署）
    ↑
知识层：Milvus（向量）+ Neo4j（图谱）+ Obsidian（笔记）
    ↑  
数据层：TDengine（时序）+ MinIO（对象存储）
    ↑
采集层：MQTT Broker + 边缘网关 + OPC UA
```

## 三、Obsidian 的新定位（不要抛弃，重新定位）

| 旧定位 | 新定位 |
|--------|--------|
| 所有数据的存储中心 | → 人类经验的知识中枢 |
| 设备原始数据查询 | → 故障案例、改进方案的载体 |
| AI直接读取的数据源 | → AI生成内容的呈现层 |

**具体用法：**
- AI分析完时序数据 → 自动生成Markdown报告 → Obsidian归档，供管理层阅读
- 老师傅经验 → Obsidian记录并双向链接，沉淀企业Know-how
- 决策链路 → 完整笔记留痕（满足IATF16949追溯要求）

## 四、Obsidian 知识库结构设计（PARA + 原子笔记法）

```
我的知识库/
├── 00-收件箱/          # 快速录入，每日清空
├── 01-项目/            # 进行中的项目
│   ├── 项目A/
│   │   ├── 需求分析.md
│   │   └── 会议纪要.md
├── 02-领域/            # 持续关注的知识领域
│   ├── CNC工艺/
│   │   ├── 缸体加工参数.md
│   │   └── 五轴编程技巧.md
├── 03-资源/            # 参考资料、模板
│   └── 模板/
│       └── 8D报告模板.md
├── 04-归档/            # 已完成内容
└── 40-知识库/          # AI自动归档的核心知识（OpenClaw专用）
    └── 原子笔记/
```

**Frontmatter 元数据规范（供OpenClaw解析）：**
```yaml
---
title: "故障案例：MC-F-035主轴温升分析与处理"
date: 2026-05-04
tags: [设备故障, 主轴, FANUC]
category: 故障案例
source: 维修记录
status: permanent-note
related: [[主轴维保SOP]], [[MC-F系列温升历史]]
---
```

## 五、OpenClaw × Obsidian 核心工作流

### ① 智能信息捕获（自动入库）

```
文章/灵感 → OpenClaw自动提取 → 生成Markdown → 存入收件箱
```

关键命令：
```bash
openclaw obsidian capture-wechat --url "文章链接" --title "标题" --target "02-领域/CNC工艺"
openclaw obsidian batch-parse --input "~/Downloads/技术文档" --output "40-知识库" --format "markdown"
openclaw obsidian deduplicate --path "00-收件箱" --field "title"
```

### ② 自然语言语义检索

```bash
# 构建向量索引（首次运行）
openclaw skill run vector-search --build-index

# 自然语言查询
"查找我之前写的关于FANUC主轴温升的笔记"
"总结2026年Q1的设备故障案例核心内容"
"对比缸体加工和曲轴加工的工艺差异"
```

### ③ AI辅助笔记整理（自动化维护）

| 周期 | 操作 | 效果 |
|------|------|------|
| **每日（5分钟）** | 收件箱清理 | 按标签自动分类到对应文件夹 |
| **每周（30分钟）** | 合并重复内容 | 推荐知识关联，建立双向链接 |
| **每月（1小时）** | 检测孤岛笔记 | 找出无关联的笔记，提示补充链接 |

### ④ Obsidian内嵌AI对话（ObsidianClaw插件）

安装ObsidianClaw官方插件后，侧边栏直接对话：

- "基于当前这篇故障案例，补充5个类似案例"
- "将这篇会议记录整理成行动清单，创建待办笔记"
- "在我的知识库中，有哪些笔记与'刀具寿命'相关？"

### ⑤ 跨设备同步方案

| 方案 | 适用场景 | 优点 |
|------|----------|------|
| **Obsidian Sync（官方付费）** | 已有订阅 | 实时同步、端到端加密 |
| **Obsidian Git（免费）** | 技术用户 | 版本控制、免费可靠 |
| **Remotely Save（免费）** | 有S3/Dropbox | 支持多种云存储 |
| **Local REST API + Tunnel** | 需实时访问 | 无同步延迟 |

> 推荐：**个人用Git，团队用Headless Sync**

## 六、部署方案

### 方案A：本地部署（隐私优先，个人使用）

```bash
npm install -g openclaw@latest
npm install -g obsidian-mcp-server
```

配置 `~/.openclaw/openclaw.json`：
```json
{
  "mcp": {
    "servers": {
      "obsidian": {
        "command": "obsidian-mcp-server",
        "args": ["--vault", "/Users/用户名/Documents/知识库"]
      }
    }
  }
}
```

推荐Obsidian插件：ObsidianClaw、Smart Connections、Templater、Dataview

### 方案B：阿里云部署（团队协作，7×24在线）

```bash
docker pull openclaw/openclaw:2026-latest
docker run -d \
  --name openclaw-obsidian \
  --restart always \
  -p 18789:18789 \
  -v /opt/openclaw/config:/app/config \
  -v /opt/obsidian-vault:/app/obsidian-vault \
  -e MODEL_PROVIDER=aliyun_bailian \
  openclaw/openclaw:2026-latest
```

## 七、模型配置建议

| 场景 | 推荐模型 | 理由 |
|------|----------|------|
| 日常检索、快速问答 | 阿里云千问 Qwen3-Mini | 免费额度充足、低延迟 |
| 复杂推理、长文档分析 | 阿里云千问 Qwen3-Max | 超长上下文、强推理能力 |
| 代码生成、技术文档 | DeepSeek V3 | 编程能力突出 |
| 隐私敏感场景 | 本地 Ollama（如Gemma 3 27B） | 数据完全不出域 |

配置命令：
```bash
openclaw config set agents.defaults.model.primary "bailian/qwen3-mini"
openclaw gateway restart
```

## 八、实施路径 & 成本估算（适用400台设备工厂）

| 阶段 | 时间 | 投入 | 核心任务 |
|------|------|------|----------|
| **① 数据层打通** | 1-2个月 | 5-10万 | MQTT + TDengine搭建，2-3条产线试点 |
| **② AI层搭建** | 2-4个月 | 10-15万 | Milvus部署 + 文档向量化 + 本地大模型 |
| **③ 知识层融合** | 4-6个月 | 5-10万 | OpenClaw对接Milvus/TDengine，Obsidian作为报告层 |

> **首年总投入20-35万**，远低于外采MES+BI系统的100-200万。
> **核心原则：工艺数据本地部署，禁止出域。**

## 九、最佳实践清单

1. **结构先行** — PARA法组织文件夹，统一Frontmatter元数据
2. **自动捕获** — OpenClaw自动抓取文章、灵感，先丢收件箱
3. **定期整理** — 设置定时任务自动分类、去重、补链接
4. **语义检索** — 用自然语言提问，而非记忆文件名
5. **双向链接** — 多用 `[[]]` 建立关联，让知识图谱自然生长
6. **上下文工程** — 写好 CLAUDE.md / OPENCLAW.md，让AI理解规则
7. **多端同步** — 选择适合的同步方案，确保数据一致
8. **数据不出域** — 核心工艺数据本地，非敏感报表可上云

---

> **核心价值：** Obsidian负责结构化存储，OpenClaw负责智能处理，两者协同让知识从"零散囤积"变为"有序流动、可复用"。
