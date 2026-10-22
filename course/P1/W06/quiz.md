# W06 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：神经网络计算图、Autograd、计算与内存复杂度、Activation。

1. 为两层 MLP 列出前向图和反向依赖，哪些 tensor 必须保存，哪些可重算？
2. 若每层保存 B×L×H 个 FP16 Activation，N 层的容量如何估算？checkpointing 改变了什么量？
3. 区分 autograd graph、FX graph 与实际 GPU Kernel；各自适合回答什么问题？
4. 解释 detach、retain_graph 和 in-place version counter 各会造成哪类错误或泄漏。
5. 如何选择 Activation checkpoint 的分段粒度，使峰值内存下降且重算成本可接受？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
