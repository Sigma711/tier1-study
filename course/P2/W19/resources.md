# W19 · 固定学习资料

> 资料状态核验：2026-10-22。GitHub 条目描述本日核验到的官方仓库；综合考核只复用 W10–W18 已固定边界。

- [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/) — **选入理由**：官方指南整合正确性验证、计时、带宽、访存与执行配置；**支撑 Scope**：GPU Kernel 专题综合学习与考核；**阅读深度**：按 Verification、Performance Metrics、Memory Optimizations 建立评审清单。
- [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) — **选入理由**：官方诊断工具提供 memory/race/init/sync 原始证据；**支撑 Scope**：综合考核的正确性与失效分析；**阅读深度**：能解释各 tool 的检测范围、报告位置与“无报告不等于无 bug”边界。
- [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) — **选入理由**：Profiling Guide 解释 Roofline、Memory Workload、Occupancy 和 Warp State 各指标怎样采集及何时失真，是把 Counter 组合成因果证据链而非凭单项指标猜瓶颈的依据；**支撑 Scope**：综合考核的性能模型与证据；**阅读深度**：以 Roofline、memory、occupancy、warp state 构造相互验证的归因链。
- [Triton repository](https://github.com/triton-lang/triton/tree/c1641abbb17a80b8c9cad1fa05b4c70d6ac260ab) — **选入理由**：固定 commit 的 Triton 源码允许沿 Python AST、Triton Dialect、LLVM 到 PTX 追踪同一 Kernel，并把文档中的编程抽象与实际 IR、Pass 和测试一一对应；**支撑 Scope**：综合考核的 Triton 源码、IR 与生成产物；**阅读深度**：固定 commit，追一个 Kernel 从 Python AST 到 dialect/LLVM/PTX。
- [CUTLASS repository](https://github.com/NVIDIA/cutlass/tree/91843b71d90737e0a9b86f7d9df213cff5a3526f) — **选入理由**：本日核验到的 NVIDIA 官方高性能 Kernel 模板仓库；**支撑 Scope**：综合考核的 GEMM/tile/layout 与库基线；**阅读深度**：固定 commit，审查一个 example 的 collective/mainloop/epilogue 和 profiler 结果。
- [FlashAttention repository @ 767386d](https://github.com/Dao-AILab/flash-attention/tree/767386d814051d1d853c45ac952d8259b5bc7235) — **选入理由**：2026-10-22 核验到的 IO-aware attention 官方实现固定 revision；**支撑 Scope**：综合考核的算法—Kernel—Benchmark 证据链；**阅读深度**：对照论文算法、支持矩阵、测试与 benchmark，禁止把 README 数字直接当本机结论。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
