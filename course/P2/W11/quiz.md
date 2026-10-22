# W11 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：GPU 内存层次、Register、Shared Memory、L1/L2、HBM、Coalescing。

1. 连续 warp 访问、stride-2 访问和未对齐访问对 memory transaction 数有何影响？
2. 区分 register、shared memory、L1/L2、HBM 的作用域、生命周期与典型用途。
3. shared-memory bank conflict 与 global-memory coalescing 是同一问题吗？分别如何举证？
4. 为何寄存器溢出可能表现为 local memory 流量？资源报告和 profiler 中看什么？
5. 何时值得先搬到 shared memory，何时直接依赖 cache/HBM 更好？给出复用率与同步成本判断。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
