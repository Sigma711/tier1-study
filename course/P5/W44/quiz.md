# W44 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：ZeRO、FSDP2、参数与优化器状态切分。

1. 推导 ZeRO-1/2/3 在 N 个 rank 上参数、梯度与 Adam 状态的每卡驻留量。
2. 解释 FSDP2 fully_shard 的 unshard/reshard 与 DTensor placement 如何配合。
3. 如何对照 DDP 与不同 reshard/wrap 粒度的峰值显存、collective 时间和 tokens/s？
4. world size 改变后恢复 checkpoint，必须验证哪些 shard metadata 与 state-dict 不变量？
5. 在 CPU offload、通信带宽与 checkpoint 复杂度约束下选择 ZeRO/FSDP2 策略。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
