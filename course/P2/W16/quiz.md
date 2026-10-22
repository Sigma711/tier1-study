# W16 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Operator Fusion、Softmax、LayerNorm、RMSNorm、内存流量优化。

1. 写出数值稳定 softmax 的公式，为什么先减 max 不改变概率却避免溢出？
2. 比较 LayerNorm 与 RMSNorm 的统计量；二者能否仅靠删除均值步骤互换？
3. 若未融合链路把 N 个元素往返 HBM 三次，融合后一次，理论字节量减少多少？实际为何未必 3 倍加速？
4. hidden size 增大后 fused Kernel 变慢，如何从寄存器、occupancy、reduction 与 DRAM 证据诊断？
5. 选择框架算子、现成 fused Kernel 或自定义实现时，应怎样设置正确性与维护门槛？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
