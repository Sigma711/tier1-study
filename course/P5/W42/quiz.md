# W42 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：训练完整生命周期、Forward、Backward、Optimizer State、Activation Memory、预训练、SFT、LoRA、RLHF、DPO、GRPO、评估、模型与训练版本管理。

1. 推导 Adam 全参训练中参数、梯度、一二阶矩的最低显存，并说明 Activation Memory 为何还随 batch、序列长度和层数增长。
2. 沿 grad_fn→Node→AccumulateGrad→AdamW.step 解释一次 Forward、Backward 与更新的因果顺序。
3. 比较预训练、SFT、LoRA、RLHF、DPO、GRPO 分别改变的参数、数据/反馈和优化目标；哪些状态必须进入版本管理？
4. loss 突然变 NaN 时，如何用 grad norm、saved tensor、optimizer state 与 model revision 证据区分数值爆炸和状态错配？
5. 设计一次只改变 activation checkpointing 的对照，说明如何用 step time、峰值显存、tokens/s 与 MFU 作结论。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
