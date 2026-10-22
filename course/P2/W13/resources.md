# W13 · 固定学习资料

> 资料状态核验：2026-10-22。

- [GPU Gems 3: Parallel Prefix Sum](https://developer.nvidia.com/gpugems/gpugems3/part-vi-gpu-computing/chapter-39-parallel-prefix-sum-scan-cuda) — **选入理由**：NVIDIA 官方经典章节完整推导 work-efficient scan；**支撑 Scope**：Scan、并行算法；**阅读深度**：精读 naïve 与 Blelloch work/span、bank conflict 与分块。
- [CUB DeviceReduce](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceReduce.html) — **选入理由**：NVIDIA CCCL 官方 API 显示生产级 reduction 契约；**支撑 Scope**：Reduction；**阅读深度**：读 temporary storage、iterator、determinism 与 numeric behavior；unstable 表示文档版本会演进，需按本日内容核对。
- [CUB API index: DeviceScan](https://nvidia.github.io/cccl/unstable/cub/api/index.html) — **选入理由**：NVIDIA CCCL 官方索引提供 DeviceScan 的当前入口；**支撑 Scope**：Scan；**阅读深度**：进入 DeviceScan 后核对 inclusive/exclusive、identity、in-place、operator associativity 与并行结果。
- [CUDA Programming Guide: Atomic Functions](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#atomic-functions) — **选入理由**：CUDA 官方文档列出各 Atomic 支持的数据类型、Compute Capability、作用域与内存序保证，能准确划清“单次原子更新”和事务一致性之间的边界；**支撑 Scope**：Atomic；**阅读深度**：精读 device/system scope、ordering 与 contention，不把原子性等同事务。
- [CUDA Programming Guide: Synchronization Functions](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#synchronization-functions) — **选入理由**：官方章节定义 barrier、warp vote 与 fence；**支撑 Scope**：Synchronization；**阅读深度**：读收敛要求、可见性与作用域，识别 barrier divergence。
- [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) — **选入理由**：官方诊断工具覆盖 racecheck/synccheck；**支撑 Scope**：Atomic、Synchronization；**阅读深度**：读 memcheck、racecheck、synccheck 报告语义与误报边界。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
