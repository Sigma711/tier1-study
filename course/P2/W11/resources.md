# W11 · 固定学习资料

> 资料状态核验：2026-10-22。

- [CUDA Programming Guide: Memory Hierarchy](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#memory-hierarchy) — **选入理由**：官方规范定义 thread/block/device 可见的存储层次；**支撑 Scope**：Register、Shared Memory、L1/L2、Global/HBM；**阅读深度**：读作用域、生命周期、cache 与一致性边界。
- [CUDA Best Practices: Coalesced Access](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#coalesced-access-to-global-memory) — **选入理由**：官方指南具体给出 warp transaction 规则；**支撑 Scope**：HBM、Coalescing；**阅读深度**：精读 alignment、stride、wasted transactions 与 effective bandwidth。
- [CUDA Best Practices: Shared Memory](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#shared-memory) — **选入理由**：官方文档覆盖 staging、bank 与 conflict；**支撑 Scope**：Shared Memory；**阅读深度**：读 bank conflict、padding、matrix transpose 案例和同步成本。
- [PTX ISA: State Spaces](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#state-spaces) — **选入理由**：官方 ISA 规范将寄存器、shared、local、global 地址空间落实到指令层；**支撑 Scope**：Register、Shared Memory、HBM；**阅读深度**：精读 .reg/.shared/.local/.global 及 load/store，不混淆 local 与片上。
- [Nsight Compute Memory Workload Analysis](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#memory-workload-analysis) — **选入理由**：官方指标说明用于验证 cache/DRAM 归因；**支撑 Scope**：L1/L2、HBM、Coalescing；**阅读深度**：把 requests、sectors、hit rate、bytes 与地址模式对应。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
