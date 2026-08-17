---
title: Skill路由治理三机制-reverse-skill架构借鉴
created: 2026-08-15
updated: 2026-08-15
type: project
domain: 工程
tags: [工程, agent, 方案]
sources: [https://github.com/zhaoxuya520/reverse-skill]
---

# Skill 路由治理三机制（reverse-skill 架构借鉴）

> 2026-08-15 Simon 决策：对 reverse-skill（25.4k stars，MIT）采用 **A+B 组合**——不安装整包，只借鉴架构（本页）+ 单拆 OT 安全参考资料（见 [[OT安全评估参考资料-索引]]）。
> 目标：解决我们 Hermes 200+ skills / QM 40 骨干 Agent 体系的路由失准、门禁靠自觉、经验不回流三个隐患。

## 一、机制拆解与我们的差距

### 机制 1：路由单一事实源 + 回归基线

| 维度 | reverse-skill 做法 | 我们现状 |
|------|------------------|---------|
| 事实源 | `routing.json` 唯一事实源（41 条规则 R0–R40），改路由只改它 | skill 描述散落在各 SKILL.md，57 字符截断窗口 |
| 消歧 | 关键词正则 + `mustAll`/`exclude`（如"越狱"排除 LLM 语境归 iOS） | 纯模型语义匹配，无消歧层 |
| 回归 | 163 条 benchmark 用例，`test-routing.ps1` 比对期望 PRIMARY，exit 1 报警 | **无回归基线**——改一条 skill 描述，不知道会不会带歪别的路由 |
| 一致性 | `verify-routing-coherence.ps1` 校验 markdown 表 ↔ JSON 漂移 | 无校验 |
| CI | Windows + Ubuntu 双平台跑同一套检查 | 无 |

**差距量化**：skills 数量已到 200+ 量级，每次新增/修订 skill 都有路由串扰风险，且无法观测。QM 框架 40 骨干人手一个 Agent 后，误路由 = 错误动作放大 40 倍。

### 机制 2：Scope 授权闸门（机器可执行，非口头纪律）

| 维度 | reverse-skill 做法 | 我们现状 |
|------|------------------|---------|
| 闸门 | ACT 前必须落地 `scope.md`（auth.status / in_scope / network_profile / ready_for_act 四段） | production-sql-fix-protocol、db-change-review 是文档约定 |
| 机器拦截 | `case-guard.ps1` 检查未就绪 exit 2；auth≠granted 只允许读文档 | **无机器拦截，靠 Agent 自觉** |
| 职责分离 | "能不能打"（scope）与"用什么打"（tool-index）正交 | 混在一起 |

### 机制 3：field-journal 自进化经验库

| 维度 | reverse-skill 做法 | 我们现状 |
|------|------------------|---------|
| 结构 | 每个 case 按模板写日志：完整链路（含弯路）、踩坑表 `[问题\|原因\|方案\|耗时]`、进化动作 checklist | skills 有 Pitfalls 区但格式随意，无耗时列 |
| 回流 | 写完强制更新 `_index.md` 三维索引（场景/高频模式/实体倒排）+ 累计统计 | 踩坑靠事后 patch skill，无强制回流点 |
| 脱敏 | 占位符总表（`{target_ip}`/`{token}`…），提交前正则自检 | 无脱敏规范，对外分享材料靠人工把关 |

### 附：tool-index 自举

行动前查自动生成的 `tool-index.md`，缺工具按 manifest bootstrap，**不猜命令**。我们 E 盘便携工具日益增多（MySQL 绿色版、OBS、netcat…），无统一可查索引，Agent 偶尔瞎猜命令名。

## 二、落地方案（最小闭环，不照搬体系）

| # | 方案 | 具体动作 | 成本 | 验收指标 |
|---|------|---------|------|---------|
| **A1** | skill 路由回归基线 | ① 从 session DB 抽 100 条真实历史任务，人工标注期望 skill → `routing-benchmark.json`；② Python 重放脚本：每条任务对当前 skill 描述做匹配，输出首选命中率；③ cron 每周跑，命中率下降 >5pp 报警 | 0.5 天 | 建立基线 → 首选命中率 ≥90%；skill 改动后回归不降级 |
| **A2** | 生产变更机器门禁 | ① 约定：生产库 DDL/批量 DML 执行前，任务目录必须有 `approval.md`（approver / scope / 回滚 SQL 路径 / 有效期 4 字段）；② 约 100 行 guard 脚本包在 mcp execute 前，无 approval 拒绝执行；③ 嵌入现有 production-sql-fix-protocol，不另起流程 | 2 小时 | 生产变更 100% 过闸；未授权执行 = 0 |
| **A3** | 踩坑表 + 脱敏约定 | ① skill Pitfalls 区统一改 `[问题\|原因\|方案\|耗时]` 四列表（新增/修订时执行，不回填存量）；② 对外分享 prompt/案例前按脱敏占位符表自检（表现存 [[OT安全评估参考资料-索引]]） | 1 小时 | 新规 skill 100% 执行 |
| **A4**（可选） | tool-index 自举 | 脚本扫描 E 盘便携工具 + 常用脚本，生成 `tool-index.md`；工具增删时重跑 | 1 小时 | "命令不存在"类瞎猜 = 0 |

**实施序**：A2（安全相关，先行）→ A1（路由基线，QM 放量前必须）→ A3 → A4。

## 三、明确不做

- ❌ 不安装 reverse-skill 整包（42 个模块中 39 个与业务无关，且含 EDR 绕过/漏洞利用等进攻性内容，不进公司环境）
- ❌ 不引入其 PowerShell 脚本体系（我们栈是 Python，guard/测试脚本全部重写）
- ❌ 不建独立 journal 系统（经验回流走现有 skills / memory / session DB，只吸收格式）
- ❌ 不做 CTF / 渗透能力建设（OT 安全仅限自有资产授权自检，见 [[OT安全评估参考资料-索引]]）

## 四、决策请求

请 Simon 裁定：
1. A1–A4 哪些立项？（建议至少 A1+A2）
2. A2 门禁范围：只生产库 DDL/DML，还是连"对外发送消息/邮件"也纳入？
3. A1 基准标注 100 条由谁复核（建议：我初标 + Simon 抽 20% 复核）？

## 相关页面

- [[OT安全评估参考资料-索引]] — 同一仓库的 B 任务产物（ot-ics + field-journal 参考资料）
- [[QM企业级Agent框架整合架构]] — A1 路由基线是 QM 40 骨干 Agent 放量（T1–T4 梯队）的前置保障
- [[人员组织架构与Agent投放规划]] — Agent 投放节奏决定 A1 的完成时限
- [[主动智能层_优化版实施方案]] — 6 阶段路线图，本方案三机制可并入对应阶段

## 参考来源

- [zhaoxuya520/reverse-skill · GitHub](https://github.com/zhaoxuya520/reverse-skill)（MIT License，2026-08-15 评估，commit `dd7c50d`）
- 机制细节依据仓库内 `skills/config/routing.json`、`skills/ops/scope-contract.md`、`skills/ops/evidence-finding-path.md`、`skills/field-journal/_template.md`、`skills/scripts/test-routing.ps1` 实读
