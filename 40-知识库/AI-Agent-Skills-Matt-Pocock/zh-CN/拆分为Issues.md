---
name: to-issues
description: Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices.
disable-model-invocation: true
---

# 拆分为 Issues

使用垂直切片（曳光弹）将计划拆分为可独立领取的 issues。

issue tracker 和分类标签词汇应当已经提供给你——如果没有，运行 `/setup-matt-pocock-skills`。

## 流程

### 1. 收集上下文

基于对话上下文中已有的内容工作。如果用户将 issue 引用（issue 编号、URL 或路径）作为参数传入，从 issue tracker 中获取它并阅读其完整正文和评论。

### 2. 探索代码库（可选）

如果你尚未探索代码库，请先了解代码的当前状态。issue 的标题和描述应使用项目的领域词汇表术语，并尊重涉及区域中的 ADR。

寻找对代码进行预重构的机会，以使实现更简单。"让变化变得容易，然后做出容易的变化。"

### 3. 草拟垂直切片

将计划拆分为**曳光弹** issues。每个 issue 是一个贯穿所有集成层的薄垂直切片，而不是单一层的水平切片。

<vertical-slice-rules>

- 每个切片在每一层（schema、API、UI、测试）中交付一条窄但完整的路径
- 完成的切片可独立演示或验证
- 任何预重构应先进行

</vertical-slice-rules>

### 4. 询问用户

以编号列表的形式呈现建议的拆分方案。对每个切片，展示：

- **标题**：简短的描述性名称
- **被阻塞于**：哪些其他切片（如果有）必须先完成
- **覆盖的用户故事**：该切片处理了哪些用户故事（如果源材料中有的话）

询问用户：

- 粒度是否合适？（太粗 / 太细）
- 依赖关系是否正确？
- 是否有切片需要合并或进一步拆分？

反复迭代直到用户批准拆分方案。

### 5. 发布 issues 到 issue tracker

对每个批准的切片，在 issue tracker 中发布一个新 issue。使用下方的 issue 正文模板。这些 issues 被视为可供 AFK 代理使用，因此除非另有指示，请使用正确的分类标签发布。

按依赖顺序发布 issues（先发阻塞项），以便你可以在"被阻塞于"字段中引用真实的 issue 标识符。

<issue-template>
## 父 issue

对 issue tracker 中父 issue 的引用（如果来源是已有的 issue，否则省略此节）。

## 要构建的内容

对此垂直切片的简洁描述。描述端到端的行为，而非逐层实现。

避免具体的文件路径或代码片段——它们会很快过时。例外：如果原型产生的代码片段能比文字更精确地编码某个决策（如状态机、reducer、schema、类型结构），则将其内联到这里，并简要注明它来自原型。精简到决策关键部分——不是可运行的演示，只是重要的部分。

## 验收标准

- [ ] 标准 1
- [ ] 标准 2
- [ ] 标准 3

## 被阻塞于

- 对阻塞 ticket 的引用（如果有）

如果没有阻塞项，写"无——可立即开始"。

</issue-template>

不要关闭或修改任何父 issue。
