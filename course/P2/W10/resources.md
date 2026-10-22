# W10 · 固定学习资料

> 资料状态核验：2026-10-22。

- [CUDA C++ Programming Guide: SIMT Architecture](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#simt-architecture) — **选入理由**：NVIDIA 在此定义 Warp 的 SIMT 执行、分支发散与 Independent Thread Scheduling，直接给出 CUDA 程序映射到线程调度硬件时必须遵守的行为边界；**支撑 Scope**：GPU 微架构、Warp、SIMT、线程调度；**阅读深度**：精读 warp execution、independent thread scheduling 与 divergence。
- [CUDA C++ Programming Guide: Hardware Implementation](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#hardware-implementation) — **选入理由**：官方文档定义 SM、thread block 与 warp 映射；**支撑 Scope**：SM、Warp、线程调度；**阅读深度**：读 multiprocessor、resident blocks/warps 和 resource partition。
- [CUDA Occupancy Calculator 11.0 archive](https://docs.nvidia.com/cuda/archive/11.0/cuda-occupancy-calculator/index.html) — **选入理由**：NVIDIA 官方归档文档将寄存器/shared/thread 限制具体化；**支撑 Scope**：Occupancy；**阅读深度**：手算 active blocks/warps，再用 calculator/编译资源报告交叉验证，并标明归档版本。
- [Nsight Compute Occupancy](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#occupancy) — **选入理由**：官方 profiler 定义 theoretical/achieved occupancy；**支撑 Scope**：Occupancy、线程调度；**阅读深度**：精读指标定义与限制，结合 warp stall 而非单指标优化。
- [Volta GPU Architecture Whitepaper](https://images.nvidia.com/content/volta-architecture/pdf/volta-architecture-whitepaper.pdf) — **选入理由**：官方微架构白皮书可核对 SM scheduler 与 execution resources；**支撑 Scope**：GPU 微架构、SM；**阅读深度**：精读 SM architecture 与 independent scheduling，同时标明架构版本边界。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
