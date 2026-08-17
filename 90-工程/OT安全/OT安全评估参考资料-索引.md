---
title: OT安全评估参考资料-索引
created: 2026-08-15
updated: 2026-08-15
type: reference
domain: 工程
tags: [工程, 调研]
sources: [https://github.com/zhaoxuya520/reverse-skill]
---

# OT安全评估参考资料（reverse-skill 单拆）

> 用途：未来对工厂 OT 网络（200 台加工中心、FANUC/西门子/三菱、SCADA 规划）做**授权安全自检**时的方法论存档。
> 来源：GitHub `zhaoxuya520/reverse-skill`（25.4k stars，MIT），2026-08-15 仅提取 `skills/ot-ics/` 与 `skills/field-journal/` 的机制文件，未安装整包。

## 使用纪律（先于一切技术内容）

1. **仅限对自有资产的授权自检**；任何对外扫描/测试禁止
2. **被动优先（passive-first）**：流量镜像 > 端口扫描；未明确授权**禁止对 PLC 写线圈/寄存器**
3. 工控误操作可致物理危害——评估前书面写清：站点、网段、是否允许主动探测、维护窗口、回滚方案
4. 发现高危立即停止扩大并通报

## 文件清单

| 现文件名 | 原仓库路径 | 内容 |
|---------|-----------|------|
| `OT工控安全评估-SKILL.md` | `skills/ot-ics/SKILL.md` | OT/ICS 评估主流程：Purdue L0–L5 分区 → 资产清单 → 被动只读 → 受限主动 → 固件CVE映射；含安全铁律与工具链表 |
| `OT工控安全评估-安全评估参考.md` | `skills/ot-ics/references/ot-safe-assessment.md` | 6 条安全清单 + 工控协议端口速查（Modbus 502 / S7comm 102 / EtherNet-IP 44818 / DNP3 20000） |
| `field-journal-模板.md` | `skills/field-journal/_template.md` | 经验日志模板：完整执行链路（含弯路）、踩坑四列表、Evidence 链契约、进化动作 checklist |
| `field-journal-脱敏规范.md` | `skills/field-journal/anonymization.md` | 脱敏占位符总表（`{target_ip}`/`{token}` 等），对外分享材料前必查 |
| `field-journal-授权先例.md` | `skills/field-journal/precedent-auth.md` | 授权确认先例（读序第一） |
| `field-journal-渗透先例.md` | `skills/field-journal/precedent-pentest.md` | 授权渗透常规操作清单（25KB，OT 评估 SKILL 指定必读） |
| `field-journal-逆向先例.md` | `skills/field-journal/precedent-reverse.md` | 逆向操作先例（固件分析时参考） |

注：文件内容保持原样（byte-identical），文内相对链接指向原仓库路径，按上表对照即可。field-journal 目录下另有 36 个具体攻击案例日志（Web/APK/AD 等），与 OT 自检无关，未收录进本目录。2026-08-15 起完整仓库克隆保留在 `E:\reverse-skill`（13MB，仅供查阅，不接入任何 Agent 客户端）。

## 启用时机

- SCADA 项目上线后首轮网络安全自检
- 设备联网（机床数据采集）范围扩大前的暴露面评估
- 参考 `MES-ERP-SCADA架构图` 目录规划 IT/OT 边界时

## 相关页面

- [[Skill路由治理三机制-reverse-skill架构借鉴]] — 同一仓库的架构借鉴方案（A 任务），本目录是 B 任务产物
- [[QM企业级Agent框架整合架构]] — Agent 平台总体规划，OT 安全自检未来可纳入 Agent 巡检能力
- [[主动智能层_首批风险清单与架构方案]] — 主动智能层风险视角，OT 暴露面属同一治理框架

## 参考来源

- [zhaoxuya520/reverse-skill · GitHub](https://github.com/zhaoxuya520/reverse-skill)（MIT License；CTF 子模块为 GPLv3，未提取）
