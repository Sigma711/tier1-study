# W14 · 固定学习资料

> 资料状态核验：2026-10-22。GitHub 条目描述本日核验到的官方仓库。

- [Anatomy of High-Performance Matrix Multiplication](https://www.cs.utexas.edu/~flame/pubs/GotoTOMS_revision.pdf) — **选入理由**：Goto 论文把 GEMM 拆成 packing、macro-kernel 与 micro-kernel，并从内存层次推导 Block 尺寸，是理解 Tiling 为何有效而非只记循环模板的经典来源；**支撑 Scope**：GEMM、Tiling；**阅读深度**：精读 memory-layer model、packing 与 macro/micro-kernel，迁移时标明 CPU/GPU 差异。
- [CUDA Programming Guide: WMMA](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#warp-matrix-functions) — **选入理由**：官方指南给出 warp-level matrix fragment 契约；**支撑 Scope**：Tensor Core、MMA；**阅读深度**：读 fragment shape/layout、load/mma/store 与架构限制。
- [PTX ISA: Matrix Multiply-Accumulate](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#warp-level-matrix-instructions-mma) — **选入理由**：官方 ISA 精确定义 mma 指令操作数、shape 与 dtype；**支撑 Scope**：MMA、Tensor Core；**阅读深度**：选定一个架构/数据类型读 operand layout、accumulator 与 saturation。
- [CUTLASS](https://github.com/NVIDIA/cutlass/tree/91843b71d90737e0a9b86f7d9df213cff5a3526f) — **选入理由**：本日核验到的 NVIDIA 官方仓库实现 GEMM tile hierarchy；**支撑 Scope**：GEMM、Tiling、Tensor Core、MMA、CUTLASS；**阅读深度**：精读 docs/ 和 include/cutlass/gemm 的 collective/mainloop/epilogue，不以仓库首页代替源码。
- [CUTLASS GEMM API](https://docs.nvidia.com/cutlass/latest/media/docs/cpp/gemm_api.html) — **选入理由**：官方文档解释 threadblock/warp/instruction tile 分层；**支撑 Scope**：Tiling、CUTLASS；**阅读深度**：读 tiled MMA、collective builder、epilogue 与 layout/alignment 参数。
- [cuBLAS GEMM](https://docs.nvidia.com/cuda/cublas/index.html#cublas-t-gemm) — **选入理由**：cuBLAS 的 GEMM 契约明确矩阵布局、leading dimension、compute type、算法选择与可复现性限制，可把纸面矩阵乘法落实为生产库调用时的正确性条件；**支撑 Scope**：GEMM；**阅读深度**：读 trans/layout/leading dimension、compute type、algorithm 与 reproducibility。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
