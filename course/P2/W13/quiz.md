# W13 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：并行算法、Reduction、Scan、Atomic、Synchronization。

1. 推导树形 reduction 的 work 与 span，并说明与串行累加的差别。
2. 写出 Blelloch exclusive scan 的 up-sweep/down-sweep 不变量；identity 选错会怎样？
3. 为什么部分线程跳过 __syncthreads 可能死锁或产生未定义行为？
4. 比较 warp shuffle、shared-memory reduction 和 global atomic 的适用规模与 contention。
5. 浮点 reduction 多次运行结果末位不同是否一定是 bug？如何设定正确性判据并排除 race？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
