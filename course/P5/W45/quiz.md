# W45 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Tensor、Sequence、Context Parallelism、DTensor、DeviceMesh。

1. 为 Y=XW 推导 row/column tensor parallel 的局部 GEMM shape 与 collective。
2. 比较 Sequence 与 Context Parallelism 对 attention 激活、通信和长序列容量的影响。
3. 解释 DeviceMesh 和 DTensor Shard/Replicate/Partial 如何表达全局张量布局。
4. layout 不一致导致 silent wrong result 时，应检查哪些 shape、placement 和 collective 证据？
5. 给定节点内 NVLink、节点间 RDMA，如何选择 mesh shape 与 TP/sequence/context degree？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
