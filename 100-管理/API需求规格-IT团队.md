# IT 团队 — API / MCP 接口需求规格

> **目标**：为 Hermes Agent（AI 管理助手）提供生产数据访问能力
> **优先级**：按 P0→P3 分批交付
> **交付物**：REST API 或 MCP Server（二选一即可，推荐 MCP）
> **认证**：API Key 或 Token，只读即可
> **联络人**：Simon

---

## 交付方式选择

| 方式 | 说明 | 推荐场景 |
|------|------|----------|
| **MCP Server** | 基于 Model Context Protocol，Hermes 原生支持 | ✅ 推荐：一次配置，直接对话查询 |
| **REST API** | 标准 HTTP API，返回 JSON | 备选：已有 API 时直接用 |

> MCP 优势：Hermes 通过 `hermes mcp add` 一键接入，无需额外适配层。

---

## P0 — 本周交付（早间简报必须）

### ① MES — OEE 数据接口

```
端点：GET /api/oee/daily?date=2026-06-14
返回：
{
  "date": "2026-06-14",
  "lines": [
    {
      "line_id": "L01",
      "line_name": "缸体线",
      "planned_hours": 24,
      "actual_hours": 22.5,
      "availability": 93.8,
      "performance": 87.2,
      "quality_rate": 98.5,
      "oee": 80.6,
      "total_parts": 1250,
      "good_parts": 1231
    }
  ]
}
```

### ② SCADA — 停机记录接口

```
端点：GET /api/downtime/daily?date=2026-06-14
返回：
{
  "date": "2026-06-14",
  "events": [
    {
      "machine_id": "MC-042",
      "start_time": "2026-06-14T10:23:00+08:00",
      "end_time": "2026-06-14T11:05:00+08:00",
      "duration_min": 42,
      "reason_code": "TOOL_CHANGE",
      "reason_desc": "换刀"
    }
  ]
}
```

**停机原因码建议标准化**：
| 码 | 含义 |
|----|------|
| TOOL_CHANGE | 换刀 |
| SETUP | 换模/调试 |
| MAINTENANCE | 计划维护 |
| BREAKDOWN | 设备故障 |
| QUALITY | 质量问题停机 |
| MATERIAL | 待料 |
| OTHER | 其他 |

### ③ QMS — 质量抽检接口

```
端点：GET /api/quality/daily?date=2026-06-14
返回：
{
  "date": "2026-06-14",
  "summary": {
    "total_inspected": 500,
    "total_defects": 12,
    "first_pass_yield": 97.6
  },
  "defects": [
    {
      "type": "尺寸超差",
      "count": 5,
      "product": "缸盖-A型",
      "line": "L02"
    }
  ]
}
```

---

## P1 — 两周内交付

### ④ ERP — 生产工单状态

```
端点：GET /api/orders/status
返回：今日到期工单列表、逾期工单、完成率
```

关键字段：工单号、产品、计划数量、已完成、交期、状态

### ⑤ 刀具管理 — 寿命计数

```
端点：GET /api/tools/warnings?threshold=50
返回：剩余寿命 < threshold 的刀具清单
```

关键字段：刀具编号、类型、已加工件数、寿命上限、预估更换时间

---

## P2 — 一个月内交付

### ⑥ ERP — 库存与采购

```
端点：GET /api/inventory/alerts     — 低于安全库存的物料
端点：GET /api/suppliers/performance — 供应商交付准时率
```

### ⑦ MES — 工艺参数回溯

```
端点：GET /api/process/params?machine=MC-042&time_range=...
返回：指定时间段内的进给量、转速、温度等参数曲线
```

---

## P3 — 未来规划

- 能耗数据接口（分设备/产线的电耗）
- 人员绩效数据接口（工时、产出、技能矩阵）
- 设备预测性维护数据（振动/温度传感器）

---

## MCP Server 开发参考

如选择 MCP 方案，推荐 Python 实现：

```python
# 示例骨架 — mcp_server.py
from mcp.server import Server
import requests

server = Server("mes-api")

@server.tool()
def get_oee_daily(date: str) -> dict:
    """获取指定日期的 OEE 数据"""
    resp = requests.get(f"http://mes.internal/api/oee/daily?date={date}")
    return resp.json()

@server.tool()
def get_downtime_daily(date: str) -> dict:
    """获取停机记录"""
    ...
```

Hermes 端接入命令：
```bash
hermes mcp add mes --command "python /path/to/mcp_server.py"
```

---

## 检查清单

- [ ] 确认 API 服务器内网地址和端口
- [ ] 确认防火墙规则（Hermes 主机 → API 服务器）
- [ ] 生成 API Key / Token
- [ ] 测试每个端点返回正确 JSON
- [ ] 通知 Simon 和 Hermes 端配置

---

*创建日期：2026-06-14 · 由 Hermes (analyst profile) 生成*
