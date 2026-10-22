# W32 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [NVIDIA TensorRT-LLM Performance Analysis](https://nvidia.github.io/TensorRT-LLM/performance/performance-tuning-guide/index.html) — **选入理由**：它把 prefill 的矩阵计算、decode 的逐 token 访存和 in-flight batching 放进同一调优框架，适合建立阶段化瓶颈模型；**支撑 Scope**：Prefill、Decode、算力/带宽约束；**阅读深度**：精读 in-flight batching、KV、compute/memory bottleneck 与测量条件。
- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics.html) — **选入理由**：它明确 TTFT、TPOT、排队时间等指标在请求生命周期中的计时边界，可防止把互不相同的延迟数字放在一起比较；**支撑 Scope**：TTFT、TPOT；**阅读深度**：精读指标时间边界、直方图与请求状态。
- [FlashAttention](https://arxiv.org/abs/2205.14135) — **选入理由**：它从 HBM—SRAM 数据搬运量而非 FLOPs 解释 attention 性能，提供判断推理 Kernel 何时受带宽约束的经典下界；**支撑 Scope**：推理计算模型中的 attention IO 模型；**阅读深度**：精读 IO complexity 与 roofline 动机；不把训练实验直接当 serving 结论。
