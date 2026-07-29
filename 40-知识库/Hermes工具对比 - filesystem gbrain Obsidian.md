---
created: 2026-06-12
tags: [Hermes, AI工具, 基础设施]
---

# Hermes 工具对比：filesystem × gbrain × Obsidian

## 一句话概括

| 工具 | 本质 | 一句话 |
|------|------|--------|
| **filesystem (MCP)** | 本地文件系统接口 | 操作一切文件——Excel、PDF、代码、数据 |
| **gbrain** | AI 向量知识库 | 让 AI 用自然语言搜索和问答企业知识 |
| **Obsidian** | Markdown 笔记系统 | 人类阅读的知识库——日报、制度、项目笔记 |

---

## 详细对比

| 维度 | filesystem (MCP) | gbrain | Obsidian |
|------|:---:|:---:|:---:|
| **存储** | 原始文件（任意格式） | PGLite 数据库 + 向量索引 | `~/Documents/Obsidian-Vault` 下的 `.md` 文件 |
| **检索方式** | 文件名匹配 / 内容正则 | **语义搜索** + 关键词混合检索 (RRF) | 文件名/内容正则 + 标签 |
| **写入** | 任意文件读写 | 页面粒度 CRUD (`put`/`get`) | Markdown + `[[双向链接]]` |
| **适用场景** | 操作任何文件：代码、Excel、PDF | **知识问答**——"公司刀具寿命标准是多少？" | **人类阅读的知识库**——制度文档、日报归档、项目笔记 |

---

## 在企业运营体系中的角色

```
filesystem  →  底层管道。所有文件操作的基础层（Excel 报工表、生产数据）
                ↑ Hermes 通过它读写一切文件

gbrain      →  AI 大脑。把知识向量化，支持自然语言问答
                适合：制度文档、技术规范、经验库的智能检索

Obsidian    →  你的笔记本。日报归档、制度文档、项目管理
                优势：双向链接、本地可控、人类可读
```

---

## 三层协作模式

Obsidian 里已有日报、制度、项目笔记。

1. **gbrain 导入 Obsidian** → 对 vault 做语义索引
2. **语义召回** → 问"上周三哪个产线良率最低？"→ gbrain 找到相关日报
3. **数据核实** → filesystem 读原始 Excel 验证

三层协作，从问答到数据到文件，全链路打通。

---

## 当前配置状态

| 组件 | 状态 | 路径/信息 |
|------|:--:|------|
| filesystem (MCP) | ✅ 已启用 | `npx @modelcontextprotocol/server-filesystem` |
| gbrain | ✅ 已启用 | v0.8.0, `/Users/kongfu/.bun/bin/gbrain` |
| Obsidian | ✅ 可用 | `~/Documents/Obsidian-Vault` |
