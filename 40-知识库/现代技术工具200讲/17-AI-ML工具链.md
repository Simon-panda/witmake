# 第17组：AI/ML 工具链

## 161. llama.cpp

**前世今生：** llama.cpp 由保加利亚开发者 Georgi Gerganov 于 2023 年 3 月创建。Meta 在 2023 年 2 月发布了 LLaMA 模型，但需要高端 GPU（A100）才能运行。Gerganov 用纯粹的 C/C++ 重写了推理引擎，核心创新是 GGML 张量库 + 整数量化——把 FP16 的模型权重压缩到 4-bit（INT4），精度损失极小（<1%），但内存需求降至 1/4。这意味着 70 亿参数的模型可以在普通笔记本上运行。llama.cpp 一夜之间引爆了整个本地 LLM 生态——Ollama、LM Studio、GPT4All、llamafile 全部基于它。2024 年获得 a16z 的 500 万美元投资，成立 ggml.ai 公司。

**使用方法与案例：**

安装：
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp && make -j4
```

**案例1：下载模型并推理**
```bash
# 下载 GGUF 格式的模型（以 Qwen2.5 7B 为例）
wget https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-GGUF/resolve/main/qwen2.5-7b-instruct-q4_k_m.gguf

# 交互式对话
./llama-cli -m qwen2.5-7b-instruct-q4_k_m.gguf \
  -p "你好，请解释什么是 OEE" \
  -n 512 -t 8
# -n 512: 最大输出 token；-t 8: 使用 8 个线程
```

**案例2：启动兼容 OpenAI API 的服务器**
```bash
./llama-server -m qwen2.5-7b-instruct-q4_k_m.gguf \
  --host 0.0.0.0 --port 8080
```
```python
import openai
client = openai.OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed")
response = client.chat.completions.create(
    model="local-model",
    messages=[{"role": "user", "content": "总结今天产线A的生产情况"}]
)
```

**案例3：量化自定义模型**
```bash
# 将 HuggingFace 模型转为 GGUF + 量化
python convert_hf_to_gguf.py /path/to/model --outtype q4_k_m
```

**进阶技巧：**
- Q4_K_M vs Q8_0：质量和速度的权衡；Q4 足够日常使用
- `--n-gpu-layers 35` GPU 加速：前 35 层跑 GPU，其余 CPU
- 多 GPU 支持：自动跨 GPU 分片（无需 NVLink）

---

## 162. ollama

**前世今生：** Ollama 由 Jeffrey Morgan（前 GitHub 和 Docker 工程师）于 2023 年 7 月创建。Morgan 受到 Docker"一行命令运行应用"理念的启发，想让 LLM 也变成"一行命令运行"。Ollama 基于 llama.cpp，但封装了模型下载、量化自动选择、OpenAI 兼容 API、多模型并发、GPU 加速。`ollama run llama3.2` 不需要理解 GGUF、量化、推理参数——全自动。2024 年 Ollama 成为最流行的本地 LLM 运行器，GitHub 已超 100k stars。

**使用方法与案例：**

安装：
```bash
brew install ollama        # macOS
curl -fsSL https://ollama.com/install.sh | sh  # Linux
# Windows: 下载 ollama.com 安装包
```

**案例1：一行跑模型**
```bash
ollama pull qwen2.5:7b       # 下载模型
ollama run qwen2.5:7b        # 交互式对话
# 或直接提问
ollama run qwen2.5:7b "生产日报模板应该包含哪些关键指标？"
```

**案例2：模型定制（Modelfile）**
```dockerfile
# Modelfile — 类似 Dockerfile
FROM qwen2.5:7b
SYSTEM """
你是 MES 系统的 AI 助手 Woker。
回答风格：简洁、数据驱动、优先用表格。
"""
PARAMETER temperature 0.3
PARAMETER num_ctx 8192
```
```bash
ollama create woker-mes-assistant -f Modelfile
ollama run woker-mes-assistant
```

**案例3：API 集成到 Python 应用**
```python
import ollama
response = ollama.chat(model='qwen2.5:7b', messages=[
    {'role': 'user', 'content': '产线A今日产量450件，计划500件，良品率96%，分析生产效率'}
])
print(response['message']['content'])
```

**进阶技巧：**
- `ollama serve` 暴露 REST API，支持多客户端并发
- `OLLAMA_NUM_PARALLEL=4` 允许 4 个请求同时推理
- `ollama list` 查看已下载模型及磁盘占用
- 社区模型库：ollama.com/library 有 1000+ 现成模型

---

## 163. Hugging Face

**前世今生：** Hugging Face 由法国创业者 Clément Delangue、Julien Chaumond 和 Thomas Wolf 于 2016 年创立，最初是一个青少年聊天机器人 App。2018 年开源了 PyTorch 版 BERT 实现后意外爆红，转型为 ML 模型的"GitHub"。Hugging Face Hub 托管了 80 万+ 模型、20 万+ 数据集、30 万+ 应用（Spaces）。`transformers` 库用 3 行代码加载任何模型。2023 年 D 轮融资 2.35 亿美元，估值 45 亿美元。Hugging Face 被称为"AI 领域的 GitHub"。

**使用方法与案例：**

```python
# 3 行代码做情感分析
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("今天生产效率非常好!")
# [{'label': 'POSITIVE', 'score': 0.998}]
```

```python
# 加载模型做文本生成
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-7B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")
```

**进阶技巧：**
- `datasets` 库高效加载 TB 级数据
- `peft` 做 LoRA 微调（只训练 1% 参数）
- Model Card 系统：模型的"README"，包含用途、限制、偏见评估

---

## 164. PyTorch

**前世今生：** PyTorch 由 Facebook AI Research (FAIR) 于 2016 年发布，由 Soumith Chintala 主导开发。当时 TensorFlow 是霸主（Google 2015 年发布），但开发者抱怨其静态计算图难调试。PyTorch 的杀手创新是"动态计算图"——定义即执行（define-by-run），可以用 Python 的 print/if/for 调试，就像写普通 Python 代码。这一设计哲学使 PyTorch 在学术界迅速击败 TensorFlow。2019 年 PyTorch 在 NeurIPS 论文使用率超过 TensorFlow。今天 PyTorch 是深度学习框架的事实标准，OpenAI、Meta、Stability AI 都用它训练模型。

**案例：训练一个简单的 OEE 预测模型**
```python
import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(5, 64),   # 5 个输入特征（产量、废品率、速度...）
    nn.ReLU(),
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 1)    # 输出：预测 OEE
)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(100):
    pred = model(X_train)
    loss = criterion(pred, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

---

## 165. LangChain ### 166. DSPy

**LangChain** 由 Harrison Chase 于 2022 年创建，是最早的 LLM 应用框架。它提供 Chain、Agent、RAG、Memory 等抽象，让开发者用组合方式构建复杂 LLM 应用。2023 年估值 10 亿美元。但也因"过度抽象"而受批评——简单任务被包装成复杂链。

**DSPy** 由斯坦福 NLP 组的 Omar Khattab 等人于 2023 年创建，理念与 LangChain 相反——不手动设计 prompt，用程序逻辑描述需求，DSPy 自动优化 prompt。类比：LangChain 是手写汇编，DSPy 是编译器。

```python
import dspy
lm = dspy.LM('openai/gpt-4o-mini')
dspy.configure(lm=lm)

# 声明式定义：输入 → 输出
class OEEAnalyst(dspy.Signature):
    """分析生产数据给出改进建议"""
    production_data = dspy.InputField()
    analysis = dspy.OutputField(desc="生产效率分析，200字以内")

analyst = dspy.Predict(OEEAnalyst)
result = analyst(production_data="产线A产量450件，良品率96%，宕机30分钟")
```

---

## 167. Whisper ### 168. Stable Diffusion ### 169. ComfyUI ### 170. Aider

**Whisper** 由 OpenAI 于 2022 年开源，是语音识别的 GPT 时刻——68 万小时多语言数据训练，96 种语言。whisper.cpp（基于 llama.cpp 同款框架）让它在手机和树莓派上实时运行。`whisper audio.mp3 --model small --language zh` 秒级转写中文。

**Stable Diffusion** 由 Stability AI 于 2022 年开源，由慕尼黑大学 CompVis 组开发。SD 是首个能在消费级 GPU（8GB VRAM）上运行的高质量文生图模型，引爆了 AI 图像生成民主化。2024 年 SD3 发布，引入 Diffusion Transformer 架构。`from diffusers import StableDiffusionPipeline` 三行代码生成图像。

**ComfyUI** 由 comfyanonymous 于 2023 年创建，是节点式 AI 图像生成工作流。不像 WebUI（线性流程），ComfyUI 用节点和连线构建复杂的图像处理管线：文生图 → ControlNet 姿势控制 → 放大 → 面部修复，全在可视化画布上完成。已成为 AI 图像生成的专业标准。

**Aider** 由 Paul Gauthier 于 2023 年创建，是终端 AI 编程助手。与 Copilot 不同，Aider 一次可以修改多个文件，自动生成 Git commit。`aider --model deepseek` 进入对话式编码。已集成到 Hermes 作为可选的编码后端。

```bash
aider --model openai/gpt-4o --dark-mode
# > 给 MES 报表系统添加 OEE 趋势图功能
# Aider: 分析代码 → 修改 3 个文件 → 自动 git commit
```

---

*第17组完成 · 200 讲全部完成！*
