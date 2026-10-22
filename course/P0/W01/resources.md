# W01 · 固定学习资料

> 资料状态核验：2026-10-22。链接状态只表示本日可访问；论文结论与当前源码实现须分别核对。

- [MLSys Conference](https://mlsys.org/) — **选入理由**：MLSys 顶会官方入口，用于建立 AI Infra 的研究版图；**支撑 Scope**：AI Infra 全景；**阅读深度**：浏览近两届 accepted papers 的 compiler、runtime、serving、training、data/cluster 分类，能说明各层接口，不把会议信息页当技术结论。
- [PyTorch Dispatcher](https://docs.pytorch.org/tutorials/advanced/dispatcher.html) — **选入理由**：官方教程直接解释算子从 Python/API 到 backend kernel 的分派；**支撑 Scope**：从模型计算到 GPU 执行；**阅读深度**：读清 operator schema、dispatch key、kernel registration，并能把一次调用追到 ATen/CUDA 实现。
- [OpenXLA StableHLO specification](https://openxla.org/stablehlo/spec) — **选入理由**：StableHLO 规范钉死算子、张量类型、动态 Shape 与数值行为，是判断模型 IR 在 Lowering 前后是否仍保持语义的权威合同；**支撑 Scope**：从模型计算到 GPU 执行；**阅读深度**：精读 operation、tensor type、shape 与 numerical semantics，区分 IR 语义和设备 Kernel。
- [NVIDIA Deep Learning Performance Guide](https://docs.nvidia.com/deeplearning/performance/) — **选入理由**：官方文档给出吞吐、延迟、算术强度与 GPU 利用的测量边界；**支撑 Scope**：性能指标；**阅读深度**：精读 Performance Guidelines 与 Matrix Multiplication Background，能列出对照变量和指标局限。
- [MLPerf Training Rules](https://github.com/mlcommons/training_policies/tree/14bc89fe00691a5181f401bd67dc242dc928b205) — **选入理由**：公开基准规则能约束“能力测评/性能测评”中的可比性；**支撑 Scope**：性能指标、现有能力测评；**阅读深度**：读 submission、measurement、compliance 规则，解释为何硬件、软件、精度与统计口径必须公开。
- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics.html) — **选入理由**：vLLM 在真实 Serving Runtime 中定义 TTFT、inter-token latency、端到端延迟与吞吐的采集位置和标签，可避免把不同时间窗口或处理阶段的指标混为一谈；**支撑 Scope**：性能指标、现有能力测评；**阅读深度**：精读 TTFT、inter-token latency、end-to-end latency 与 token throughput 的定义和标签，不用单一平均值概括体验。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
