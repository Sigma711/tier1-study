# W16 · 固定学习资料

> 资料状态核验：2026-10-22。

- [Triton Fused Softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html) — **选入理由**：官方教程逐项计算 unfused/fused 内存访问；**支撑 Scope**：Operator Fusion、Softmax、内存流量优化；**阅读深度**：精读稳定 softmax、字节量模型、BLOCK_SIZE/num_warps 与 benchmark shape。
- [PyTorch softmax](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.softmax.html) — **选入理由**：官方 API 给出轴、dtype 与数值语义基线；**支撑 Scope**：Softmax；**阅读深度**：核对 dim/dtype 与 reference output，用于验证 fused 实现。
- [Layer Normalization](https://arxiv.org/abs/1607.06450) — **选入理由**：LayerNorm 原论文定义均值/方差和 affine 参数；**支撑 Scope**：LayerNorm；**阅读深度**：精读方法公式、与 batch normalization 对比及适用边界。
- [Root Mean Square Layer Normalization](https://papers.neurips.cc/paper/9403-root-mean-square-layer-normalization) — **选入理由**：RMSNorm 原文给出可直接转写为 Kernel 的归一化公式，并通过去掉均值计算说明少一次 Reduction 的来源及其质量边界；**支撑 Scope**：RMSNorm；**阅读深度**：精读公式、re-centering invariance 差异、速度与质量实验。
- [PyTorch Inductor CPU backend: fusion overview](https://docs.pytorch.org/tutorials/intermediate/inductor_debug_cpu.html) — **选入理由**：这个官方调试教程同时展示 Fusion 前后的 Graph 与生成代码，使“算子被融合”能由编译产物核验，其 CPU 后端也恰好用于辨认哪些方法可迁移、哪些性能结论不能外推到 GPU；**支撑 Scope**：Operator Fusion；**阅读深度**：只提取 graph/kernel fusion 和生成代码验证方法，明确 CPU 示例不能直接证明 GPU 收益。
- [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) — **选入理由**：官方工具用于验证 DRAM bytes、register 与 occupancy；**支撑 Scope**：内存流量优化；**阅读深度**：选 Memory Workload/Occupancy 指标对照独立与融合 Kernel。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
