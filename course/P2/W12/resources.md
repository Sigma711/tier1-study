# W12 · 固定学习资料

> 资料状态核验：2026-10-22。

- [CUDA Programming Model](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model) — **选入理由**：官方指南定义 host/device、grid/block/thread；**支撑 Scope**：CUDA 编程模型、Kernel Launch；**阅读深度**：精读 kernel、thread hierarchy、launch configuration 与异步错误。
- [CUDA Runtime API: Execution Control](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EXECUTION.html) — **选入理由**：官方 API 给出 launch 与配置的精确契约；**支撑 Scope**：Kernel Launch；**阅读深度**：读 launch、device synchronize、error return 与资源限制。
- [CUDA Programming Guide: Asynchronous Concurrent Execution](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#asynchronous-concurrent-execution) — **选入理由**：该章节精确定义 Stream 内顺序、跨 Stream 并发、默认 Stream 与隐式同步条件，是判断拷贝和 Kernel 能否真实重叠的权威依据；**支撑 Scope**：Stream、异步执行；**阅读深度**：精读 concurrent execution、overlap、default stream 与 implicit synchronization。
- [CUDA Runtime API: Stream Management](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__STREAM.html) — **选入理由**：官方 API 明确 stream ordering、wait 和 capture；**支撑 Scope**：Stream；**阅读深度**：读 create/wait/synchronize/query 与生命周期。
- [CUDA Runtime API: Event Management](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html) — **选入理由**：官方 API 定义 event record/wait/timing；**支撑 Scope**：Event、异步执行；**阅读深度**：精读 record、elapsed time、跨 stream 依赖与 timing 限制。
- [Nsight Systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html) — **选入理由**：官方时间线工具用于验证 CPU enqueue 与 GPU overlap；**支撑 Scope**：Stream、Event、异步执行；**阅读深度**：读 CUDA trace、timeline、NVTX，能识别空洞与隐式同步。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
