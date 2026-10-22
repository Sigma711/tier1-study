# W09 · 固定学习资料

> 资料状态核验：2026-10-22。

- [PyTorch Optimizing Model Parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) — **选入理由**：官方教程明确训练 loop 的 zero_grad/backward/step；**支撑 Scope**：模型训练过程；**阅读深度**：追踪每阶段状态变更和生命周期，不停留在 API 抄写。
- [Transformers Generation](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation) — **选入理由**：官方文档定义 autoregressive generation、stopping 与 sampling 参数；**支撑 Scope**：模型生成过程；**阅读深度**：精读 GenerationConfig、max_new_tokens、EOS、sampling 与 cache 相关返回。
- [Transformers KV cache strategies](https://huggingface.co/docs/transformers/main/en/kv_cache) — **选入理由**：Transformers 对 Dynamic、Static 等 KV Cache 策略给出容量增长、编译兼容性和 Offload 取舍，可把逐 Token 生成状态直接换算为显存占用；**支撑 Scope**：生成过程、显存占用模型；**阅读深度**：读 Dynamic/Static cache 的容量和编译权衡，仅用于单模型生成状态，不提前扩展服务调度。
- [PyTorch CUDA memory](https://docs.pytorch.org/docs/stable/notes/cuda.html#cuda-memory-management) — **选入理由**：官方文档给出 allocator、snapshot 与峰值口径；**支撑 Scope**：显存占用模型；**阅读深度**：区分 allocated/reserved、memory snapshot、fragmentation 与 OOM 证据。
- [LLM Inference Unveiled](https://arxiv.org/abs/2402.16363) — **选入理由**：系统化测量 prefill/decode 工作负载的研究论文；**支撑 Scope**：推理工作负载；**阅读深度**：读阶段划分、算术/带宽特征和测量设置，论文结论需与本地硬件证据分开。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
