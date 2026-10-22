# W17 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：FlashAttention、Online Softmax、IO Complexity、Warp 分工。

1. 推导 online softmax 合并旧块与新块时 running max、running sum 的更新式。
2. FlashAttention 为什么仍是精确 attention？它降低的是算术复杂度还是 HBM I/O 复杂度？
3. Q/K/V tile 与 warp 分工怎样影响 SRAM 容量、并行度和同步？
4. causal mask 或边界 tile 错误如何用短序列参考 attention 最小化复现？
5. 比较普通 attention、框架 SDPA 与 FlashAttention 时必须控制哪些 Shape、dtype 和误差变量？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
