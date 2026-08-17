---
title: AI开源课程评估与内训路径
created: 2026-08-16
updated: 2026-08-16
type: reference
domain: 学习
tags: [学习, AI, agent, llm, 调研]
---

# AI开源课程评估与内训路径

> 缘起：Simon 发 microsoft/AI-For-Beginners 问"适不适合我们学"。结论扩展为三层——微软入门三仓逐仓评估 + 12 个更 senior 的开源课程/库分派到副业五个小组 + 量化内训路径。全部经 GitHub API 源码级实证（2026-08-16），两仓已镜像到本机。

## 一、三档结论（微软入门三仓）

| 仓 | ★ / 协议 / 新鲜度 | 结论 | 一句话 |
|---|---|---|---|
| microsoft/AI-For-Beginners | 65.0k / MIT / 2021建，仍维护 | **借鉴吸收（按小组裁剪）** | 24课通识课，仅 CV 7 课（6-12）对视觉组是高价值教材；LLM 停在 BERT 入门，大模型组不要投时间 |
| microsoft/generative-ai-for-beginners | 117.8k / MIT / v3 活跃 | **借鉴吸收** | 21课 Python+TS 双语言，精华在后半程：11 Function Calling、15 RAG、16 开源模型、18 微调、19 SLM |
| microsoft/ai-agents-for-beginners | 72.2k / MIT / 2024-11 建 | **三仓中最对口** | 18课，MAF+MCP 为主；10 生产观测/12 上下文工程/18 签名回执三课已蒸馏进 [[QM企业级Agent框架整合架构]] 第八节 |

三仓共性短板：无 RAG/Agent 深度工程、无 MLOps/产线部署（ONNX/TensorRT）、无时间序列预测性维护——入门定位使然，senior 内容靠下表补。

## 二、Senior 仓库清单（按小组分派）

| 小组 | 仓库 | ★ / 协议 | 定位 |
|---|---|---|---|
| AI 大模型组 | mlabonne/llm-course | 81.7k / Apache-2.0 | 首选进阶：基础/科学家/工程师三轨，量化、微调、模型合并含 Colab |
| | rasbt/LLMs-from-scratch | 102.7k / 配套书 | PyTorch 从零手搓 GPT，练内功 |
| | Shubhamsaboo/awesome-llm-apps | 132.8k / Apache-2.0 | 100+ 可跑 Agent/RAG 案例，客户项目模式库 |
| | huggingface/smol-course | 6.7k / Apache-2.0 | 小模型对齐（SFT/DPO/GRPO），对口私有部署 SLM 路线 |
| AI 视觉组 | open-edge-platform/anomalib | 6k / Apache-2.0 | **工业异常检测 SOTA 库**：v2.6 收录 CVPR2026 工业赛道冠军模型 SuperADD，自带汽车零部件视觉检测基准 AutoVI，可导出 OpenVINO 部署 |
| | ultralytics/ultralytics | 60.6k / ⚠️ AGPL-3.0 | YOLO 标杆，但 AGPL 商用需购企业授权——副业项目启用前必须过 Simon |
| IT 软件组 | DataTalksClub/mlops-zoomcamp | 15.1k | MLOps 全流程：实验追踪/编排/部署/监控 |
| | GokuMohandas/Made-With-ML | 49k / MIT | 生产级 ML 工程课 |
| | DataTalksClub/llm-zoomcamp | 7k | LLM 应用工程（RAG/评估/监控）10 周 |
| 边缘/现场 | microsoft/edgeai-for-beginners | 1.65k / MIT | 唯一讲边缘 SLM 落地的课：llama.cpp、蒸馏、Qwen/Phi/BitNET、MCP |
| 全员参考 | dair-ai/Prompt-Engineering-Guide | 77.5k / MIT | 提示工程案头参考 |
| | microsoft/mcp-for-beginners | （微软系）/ MIT | MCP 协议入门，配合 QM 数据平面 |

## 三、内训路径（量化）

| 对象 | 路径 | 周期 | 结营产出 |
|---|---|---|---|
| AI 视觉组 | AI-For-Beginners 课 3-5 + 6-12（10课）→ anomalib notebooks + AutoVI 复现 | 5+2 周 | 产线可试跑的缺陷检测 baseline |
| AI 大模型组 | agents 仓 10/11/12/13/16/18 六课精读 → llm-course 工程师轨（每周 1 Colab） | 2+6 周 | 一份 QM 生产化改造清单（已有雏形=架构文档第八节） |
| IT 软件组 | mlops-zoomcamp 每周 1 模块 | 8 周 | QM/模型服务的部署运维手册 |
| 40 骨干通识 | AI-For-Beginners 课 1-3 + 7（4课） | 1 周 | Agent 投放认知对齐（配合 [[人员组织架构与Agent投放规划]]） |

## 四、本地镜像

| 仓 | 路径 | 状态 |
|---|---|---|
| generative-ai-for-beginners | `C:\Users\ASUS\repos\generative-ai-for-beginners` | 21 课全量（剔除 50+ 语言翻译包，sparse checkout） |
| ai-agents-for-beginners | `C:\Users\ASUS\repos\ai-agents-for-beginners` | 18 课 README 全量（经 API 精准拉取；含代码样本的完整包 436MB 需后台慢拉） |

> 本机网络教训：GitHub blob 按需拉取与 436MB zip 直连均被重置（early EOF / 断流）；API 单文件 raw 端点稳定可用。git clone 目标路径在 Windows git.exe 下 `/c/...` 会被解析成 `C:\c\...`，须先 `cd` 再用相对目录名克隆。

## 参考来源

- [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) · [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) · [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [mlabonne/llm-course](https://github.com/mlabonne/llm-course) · [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) · [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) · [smol-course](https://github.com/huggingface/smol-course)
- [anomalib](https://github.com/open-edge-platform/anomalib) · [ultralytics](https://github.com/ultralytics/ultralytics)
- [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) · [Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) · [llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)
- [edgeai-for-beginners](https://github.com/microsoft/edgeai-for-beginners) · [Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) · [mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)

## 相关页面

- [[QM企业级Agent框架整合架构]] — agents 仓 10/12/18 三课的设计借鉴已蒸馏为第八节（生产观测/上下文工程/签名回执）
- [[人员组织架构与Agent投放规划]] — 内训路径的人员基础（40 骨干 T1-T4 梯队）
- [[深入理解AI-Agent-总索引]] — 已在库的中文 Agent 教材（李博杰），与本页外部课程互为补充
