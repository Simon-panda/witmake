---
name: tdd
description: Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
---

# 测试驱动开发

## 核心理念

**核心原则**：测试应通过公共接口验证行为，而非验证实现细节。代码可以完全改变，但测试不应该变。

**好的测试**是集成风格的：它们通过公共 API 运行真实的代码路径。它们描述系统_做什么_，而非_怎么做_。一个好的测试读起来像一份规格说明——"用户可以使用有效购物车结账"明确告诉你存在什么能力。这些测试能在重构中存活下来，因为它们不关心内部结构。

**坏的测试**与实现耦合。它们 mock 内部协作者、测试私有方法，或通过外部手段验证（例如直接查询数据库而非使用接口）。警示信号：当你重构时测试失败，但行为并未改变。如果你重命名一个内部函数而测试失败了，那些测试是在验证实现，而非行为。

示例参见 [tests.md](tests.md)，mock 准则参见 [mocking.md](mocking.md)。

## 反模式：水平切片

**不要先写所有测试，再写所有实现。** 这是"水平切片"——将 RED 阶段视为"写所有测试"，将 GREEN 阶段视为"写所有代码"。

这会产生**糟糕的测试**：

- 批量编写的测试验证的是_想象中的_行为，而非_实际的_行为
- 最终你测试的是事物的_形态_（数据结构、函数签名），而非面向用户的行为
- 测试对真实变化变得不敏感——行为出错时测试通过，行为正常时测试反而失败
- 你跑得比自己的车灯还快，在理解实现之前就锁定了测试结构

**正确做法**：通过曳光弹进行垂直切片。一个测试 → 一个实现 → 重复。每个测试都响应你从上一轮中学到的内容。因为你刚写完代码，你确切知道什么行为重要以及如何验证它。

```
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

## 工作流

### 1. 规划

在探索代码库时，阅读 `CONTEXT.md`（如果存在），以便测试名称和接口词汇与项目的领域语言匹配，并尊重你所涉及的领域中的 ADR。

在编写任何代码之前：

- [ ] 与用户确认需要哪些接口变更
- [ ] 与用户确认要测试哪些行为（确定优先级）
- [ ] 识别深度模块的机会（小接口，深实现）——运行 `/codebase-design` 技能以获取相关词汇和可测试性检查
- [ ] 列出要测试的行为（而非实现步骤）
- [ ] 获得用户对计划的批准

提问："公共接口应该是什么样的？哪些行为最重要需要测试？"

**你无法测试一切。** 与用户确认哪些行为最为重要。将测试精力集中在关键路径和复杂逻辑上，而非每一个可能的边缘情况。

### 2. 曳光弹

写一个测试来验证系统的一件事情：

```
RED:   Write test for first behavior → test fails
GREEN: Write minimal code to pass → test passes
```

这就是你的曳光弹——证明整条路径端到端能够工作。

### 3. 增量循环

对于每个剩余的行为：

```
RED:   Write next test → fails
GREEN: Minimal code to pass → passes
```

规则：

- 一次一个测试
- 只写足够通过当前测试的代码
- 不要预判未来的测试
- 保持测试聚焦于可观察的行为

### 4. 重构

所有测试通过后，寻找[重构候选](refactoring.md)：

- [ ] 提取重复代码
- [ ] 深化模块（将复杂性移到简单接口背后）
- [ ] 在合适的地方应用 SOLID 原则
- [ ] 思考新代码对现有代码的启示
- [ ] 每次重构步骤后运行测试

**绝不在 RED 阶段重构。** 先到达 GREEN。

## 每轮检查清单

```
[ ] Test describes behavior, not implementation
[ ] Test uses public interface only
[ ] Test would survive internal refactor
[ ] Code is minimal for this test
[ ] No speculative features added
```
