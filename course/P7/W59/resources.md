# W59 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/) — **选入理由**：NVIDIA 将 Coalescing、Shared Memory、Occupancy、Async Copy 与 Profiling 建议放在同一硬件约束体系中，可逐项验证 Kernel 优化究竟减少了哪类瓶颈；**支撑 Scope**：Kernel、性能瓶颈；**阅读深度**：读 coalescing、shared memory、occupancy、async copy 与 profiling guidance。
- [Triton Tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) — **选入理由**：官方从 vector add 到 fused softmax/matmul 的 Kernel 产物；**支撑 Scope**：实现优化；**阅读深度**：逐个对照 program id、tile、mask、autotune 与生成代码。
- [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/) — **选入理由**：Kernel counter、replay 与 Roofline 的官方解释；**支撑 Scope**：分析性能瓶颈；**阅读深度**：读 SpeedOfLight、MemoryWorkloadAnalysis、Occupancy 和 Roofline，核对采集扰动。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
