# W10 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：GPU 微架构、SM、Warp、SIMT、线程调度、Occupancy。

1. 给定每 SM 最多 2048 threads、64 warps，block=256 threads，仅按线程上限可驻留多少 block、理论 occupancy 多少？
2. SIMT 与 SIMD 有何共同点和根本区别？分支发散为何按路径串行化有效工作？
3. 寄存器数和 shared memory 如何进一步限制 active blocks？写出取各资源上限最小值的推导。
4. 为什么 achieved occupancy 很高但 Kernel 仍可能很慢？给出两类 counter 证据。
5. 为一个 latency-bound Kernel 选择 block size 时，如何权衡 warp 数、寄存器压力和调度开销？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
