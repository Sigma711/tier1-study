# W46 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Pipeline Parallelism、Microbatch、GPipe、1F1B、Pipeline Bubble。

1. 推导 p stage、m microbatch 的 GPipe bubble fraction，并解释 m 增大为何不能无限增益。
2. 比较 GPipe 与 1F1B 的时序、激活驻留量和依赖。
3. PyTorch pipeline stage 的 split/merge 与 send/recv 必须满足哪些 shape/dtype 契约？
4. timeline 出现固定 stage 空槽时，如何区分 partition 不均、通信阻塞和 microbatch 太少？
5. 给出选择 stage 切点、microbatch 数与 schedule 的评审准则。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
