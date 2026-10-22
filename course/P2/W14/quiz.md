# W14 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：GEMM、Tiling、Tensor Core、MMA、CUTLASS。

1. 推导 M×K 乘 K×N 的 FLOPs 和读取输入一次的最低字节数，计算 arithmetic intensity。
2. 为什么 tiling 能减少 global-memory 访问？threadblock、warp、MMA tile 各负责哪层复用？
3. 区分 Tensor Core、MMA 指令和 CUTLASS：硬件、指令、模板库分别是什么。
4. leading dimension 或 row/column-major 解释错误会产生什么结果？如何用非方阵 Shape 暴露？
5. 评审自定义 GEMM 时，为什么必须以 cuBLAS 为基线并覆盖多 Shape/dtype？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
