# W34 · 简短 Quiz

1. 用 Little 定律解释到达率、在制请求与响应时间的关系，为什么接近容量时排队会失控？
2. 给定长 Prefill 长度与 chunk size，计算调度轮数，并分析对 TTFT/TPOT 的相反影响。
3. Continuous Batching 与静态 batching 的组批时机有何本质差异？
4. 如何从 per-request timeline 识别饥饿、preemption 抖动和不公平？
5. 设计 admission control 与公平策略，说明拒绝率和 goodput 取舍。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
