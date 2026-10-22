# W49 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：TorchTitan / Megatron 综合研究。

1. 从模型规模、序列长度和 mesh 推导 TorchTitan/Megatron 的每卡显存与 collective 量。
2. 对照两者的 parallelisms/parallel_state、训练循环和 schedule 源码路径。
3. 比较两框架时必须固定哪些模型、精度、batch、硬件和统计口径？
4. 如何用 rank mapping、loss curve、config dump 与 checkpoint reshard 证据诊断语义差异？
5. 在扩展性、可插拔性、运维成熟度与迁移成本间作框架选择。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
