# W15 · 固定学习资料

> 资料状态核验：2026-10-22。GitHub 条目描述本日核验到的官方仓库。

- [Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations](https://dl.acm.org/doi/10.1145/3315508.3329973) — **选入理由**：MAPL 原论文定义 block/tile 编程动机；**支撑 Scope**：Triton 编程模型、Block；**阅读深度**：精读 programming model、tile-level optimization 与 evaluation，区分论文版本和当前实现。
- [Triton Programming Guide: Introduction](https://triton-lang.org/main/programming-guide/chapter-1/introduction.html) — **选入理由**：官方文档定义 blocked program 与 scalar thread 的执行模型；**支撑 Scope**：Triton 编程模型、Block；**阅读深度**：精读 blocked algorithm、program instance 与 compiler scheduling。
- [Triton language API](https://triton-lang.org/main/python-api/triton.language.html) — **选入理由**：官方 API 索引集中给出 program_id、arange、load/store 与 block/tensor descriptor；**支撑 Scope**：Block、Layout；**阅读深度**：沿具体 API 核对 shape/stride/offset、mask 和边界语义。
- [Triton MLIR Dialects and Ops](https://triton-lang.org/main/dialects/dialects.html) — **选入理由**：官方生成文档同时暴露 Triton/TritonGPU 的 layout encoding 与操作语义，能把 Python tile 程序连接到 TTIR/TTGIR；**支撑 Scope**：Layout、Warp 映射；**阅读深度**：读 blocked/dot operand encoding、convert_layout、load/dot/reduce，并选一个 tutorial Kernel 对照两层 IR。
- [Triton Vector Addition Tutorial](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html) — **选入理由**：官方最小示例明确 program_id/block/mask；**支撑 Scope**：Triton 编程模型、Block；**阅读深度**：逐行推导 grid、offset、mask 与 num_warps，不只运行代码。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
