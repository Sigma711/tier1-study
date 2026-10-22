# W15 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Triton 编程模型、Block、Layout、Warp 映射。

1. 给定 N 个元素和 BLOCK_SIZE，推导 Triton 一维 grid；最后一个 program 为什么需要 mask？
2. 区分 Triton program instance、block、num_warps 与 CUDA thread block/warp 的对应和非对应。
3. TTIR、TTGIR、LLVM IR、PTX 各位于哪一层？layout 信息在哪些 lowering 中被具体化？
4. 相同 Triton 源码仅改变 num_warps，为何可能同时改变 occupancy、访存和耗时？
5. 什么情况下 Triton 的生产力优势胜过手写 CUDA，什么情况下应使用库或 CUDA？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
