# Needle — 26M参数工具调用模型

**来源：** Simon 推荐
**日期：** 2026-05-17
**GitHub：** [cactus-compute/needle](https://github.com/cactus-compute/needle)

---

## 核心定位

> 从 Gemini 3.1 蒸馏出的 26M 参数 **Simple Attention Network**，专注**单次工具调用**场景。

- 26M 参数量级，笔记本即可跑 **6000 tokens/s**（prefill）/ 1200 tokens/s（decode）
- 适合端侧设备（手机、手表、眼镜）快速对接 API
- 可在 Mac/PC 上本地微调

---

## 架构亮点

| 组件 | 说明 |
|------|------|
| Encoder | 12层，ZCRMSNorm + GQA + RoPE，无FFN |
| Decoder | 8层 Masked Self-Attn + Cross Attn + Gated Residual |
| Embedding | BPE 词表 8192，d=512, 8H/4KV |
| 输出头 | Linear(T) + Softmax → Tool Call |

![架构图](https://github.com/cactus-compute/needle/blob/main/assets/banner.png)

---

## 训练数据

- **预训练：** 16块 TPU v6e，200B tokens，27小时
- **后训练：** 2B tokens 单次函数调用数据集，45分钟
- **权重开源：** [HuggingFace - Cactus-Compute/needle](https://huggingface.co/Cactus-Compute/needle)

## 性能表现

在单次函数调用场景下，超越：
- FunctionGemma-270M
- Qwen-0.6B
- Granite-350M
- LFM2.5-350M

⚠️ 局限：仅专精单次工具调用，不适合多轮对话场景。

---

## 快速体验

```bash
git clone https://github.com/cactus-compute/needle.git
cd needle && source ./setup
needle playground
```

浏览器打开 `http://127.0.0.1:7860` 即可交互测试、微调。

## CLI 命令

| 命令 | 功能 |
|------|------|
| `needle playground` | Web UI 测试与微调 |
| `needle finetune data.jsonl` | 基于 JSONL 数据微调 |
| `needle run --query "..." --tools '[...]'` | 单次推理 |
| `needle train` | 完整训练 |
| `needle pretrain` | 预训练 |
| `needle eval --checkpoint <path>` | 评估检查点 |
| `needle generate-data` | 用 Gemini 合成训练数据 |

## Python API

```python
from needle import SimpleAttentionNetwork, load_checkpoint, generate, get_tokenizer

params, config = load_checkpoint("checkpoints/needle.pkl")
model = SimpleAttentionNetwork(config)
tokenizer = get_tokenizer()

result = generate(
    model, params, tokenizer,
    query="What's the weather in San Francisco?",
    tools='[{"name":"get_weather","description":"Get current weather for a city.","parameters":{"location":{"type":"string","description":"City name.","required":true}}}]',
    stream=False,
)
print(result)
# [{"name":"get_weather","arguments":{"location":"San Francisco"}}]
```

## 微调数据格式

JSONL，每行含三个字段：
- `query`: 用户提问
- `tools`: 工具定义（JSON字符串）
- `answers`: 期望的工具调用（JSON字符串）

**要求：** 每个工具至少 120 条示例（100 训练 / 10 验证 / 10 测试），否则容易过拟合。

---

## 与我们的相关性

| 维度 | 关联 |
|------|------|
| 端侧部署 | 26M 参数，适合车间数据采集点的本地推理，不需要联网 |
| 工具调用 | 单次工具调用精准，适合将MES/设备数据以API形式暴露给轻量化Agent |
| 可微调 | 可用企业自有工具集微调，适配工厂场景 |

潜在场景：设备看护Agent的轻量化工具调用引擎，或作为边缘节点上的API路由器。
