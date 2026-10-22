# W59 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Kernel、分析性能瓶颈并实现优化。

1. 计算一个 Kernel 的 FLOPs、HBM/shared-memory bytes、算术强度和 Roofline 上界。
2. 从 Triton/CUDA tile、load/store、reduction 追到 PTX/SASS，解释访存合并。
3. tile/warps/stages 对 latency、occupancy、寄存器与 DRAM/L2 throughput 有何影响？
4. 如何用边界 mask、差分测试和 sanitizer 发现任意 shape 下的竞态/越界？
5. 何时应保留通用回退 Kernel，而不接受只对单一 shape 的峰值优化？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
