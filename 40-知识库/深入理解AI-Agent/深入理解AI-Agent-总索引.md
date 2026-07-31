---
title: 深入理解AI-Agent 总索引
created: 2026-07-27
updated: 2026-07-27
type: reference
domain: 学习
tags: [AI, agent, llm, mcp, 学习, 索引]
sources: [raw/assets/深入理解AI-Agent-李博杰-2026-07.pdf]
---

# 深入理解 AI Agent：设计原理与工程实践

> **作者**：李博杰 | **协议**：Apache-2.0 | **Star**：22.2k
> **来源**：[github.com/bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)
> **入库日期**：2026-07-27（镜像 main 分支正文 + 133 张配图）
> **蒸馏日期**：2026-07-31（cangjie 流水线 → 13 个可执行 skills，见 [[蒸馏产物/蒸馏总览]]）

## 核心公式

**Agent = LLM（大脑）+ 上下文（眼睛）+ 工具（手脚）**

全书 10 章围绕此公式层层递进，从原理讲到工程实战，含 **92 个配套实验**（70+ 可独立运行）。实验代码在 [原仓库 chapter1~chapter10 目录](https://github.com/bojieli/ai-agent-book)，未入库（依赖外部仓库与运行环境）。

## 章节导航

| 章 | 主题 | 一句话核心 |
|---|---|---|
| — | [[引言]] | 为什么写这本书、如何读 |
| 1 | [[第01章 Agent基础知识]] | Agent = LLM + 上下文 + 工具；Harness 工程才是竞争力 |
| 2 | [[第02章 上下文工程]] | KV Cache、提示工程、Agent Skills、上下文压缩 |
| 3 | [[第03章 用户记忆和知识库]] | 用户记忆、RAG、结构化索引、知识图谱 |
| 4 | [[第04章 工具]] | MCP 协议、感知/执行/协作三类工具、事件驱动异步 Agent |
| 5 | [[第05章 Coding Agent与代码生成]] | 代码是「能创造新工具的工具」，生产级 Coding Agent 全景 |
| 6 | [[第06章 Agent的评估]] | 评估环境、指标、统计显著性、评估驱动选型 |
| 7 | [[第07章 模型后训练]] | 预训练/SFT/RL 三阶段，工具调用内化、样本效率 |
| 8 | [[第08章 Agent的持续进化]] | 从运行轨迹获得学习信号，更新知识、指令、程序与参数 |
| 9 | [[第09章 多模态与实时交互]] | 语音三范式、Computer Use、机器人 |
| 10 | [[第10章 多Agent协作]] | 协作框架、上下文共享/隔离、涌现的「Agent 社会」 |
| — | [[后记]] | 作者总结 |
| — | [[思考题参考答案]] | 全书思考题解答 |

## 蒸馏产物（2026-07-31，cangjie 流水线）

- [[蒸馏产物/蒸馏总览]] — 13 个可执行 skills 的路线图与组合用法
- [[蒸馏产物/精华长文-DIGEST]] — 6 千字读薄 316 页（含全书批判）
- [[蒸馏产物/学习笔记-大白话]] — 管理者版：一个类比+十条结论+三张清单
- [[蒸馏产物/话术库-TALKING_POINTS]] — 16 条场景话术
- [[蒸馏产物/术语词典-GLOSSARY]] — 71 条术语

## 配套资源

- **PDF 离线版**：`raw/assets/深入理解AI-Agent-李博杰-2026-07.pdf`（11MB，适合手机阅读）
- **在线阅读**：[bojieli.github.io/ai-agent-book](https://bojieli.github.io/ai-agent-book/)（全文搜索、章节折叠）
- **图片**：本目录 `images/`（133 张 SVG/PNG，正文中以相对路径引用）

## 与本公司业务的关联

- 第 4 章 **MCP 协议** ↔ 我们的 [[工作分配与API建设深度拆解|MCP Server 架构]]（fuadmin 数据字典 334 表已就绪）
- 第 3 章 **RAG/知识库** ↔ [[企业级数据Agent落地方案v2]] 的数据 Agent 落地路径
- 第 10 章 **多 Agent 协作** ↔ Kanban 多 Agent 系统（factory-ops 8 profiles）
- 第 6 章 **Agent 评估** ↔ [[主动智能层_优化版实施方案]] 的效果度量需求

## 相关页面

- [[现代技术工具100讲]] — 工具视角的技术全景
- [[Hermes精装攻略七步法]] — 本厂 Agent 运行环境配置
- [[AI-Agent-Skills-Matt-Pocock]] — 同级 Agent Skills 工程实践集
