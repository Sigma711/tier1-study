# W18 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Nsight Compute、Nsight Systems、Roofline、PTX/SASS、自动调优。

1. 给定峰值 100 TFLOP/s、带宽 2 TB/s、AI=20 FLOP/byte，Roofline 上界是多少，属于哪类瓶颈？
2. 区分 PTX 与 SASS；为什么看到 PTX 向量指令不能证明最终机器指令相同？
3. Nsight Systems 与 Nsight Compute 分别回答什么问题？为什么 profiling 顺序应先全局后局部？
4. counter replay 与 profiler perturbation 如何使测量失真？如何建立无 profiler 基线？
5. 自动调优如何划分搜索集与留出 Shape，并用正确性门避免过拟合最快候选？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
