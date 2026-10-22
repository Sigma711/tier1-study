# W41 · 简短 Quiz

1. 为 Mini Engine 推导权重、KV、每 token FLOPs/bytes、队列容量与 SLO 的统一容量预算。
2. 沿 API、Engine/Scheduler、KV allocator、Model Runner 和 kernel 描述请求状态与证据链。
3. 设计朴素基线和单变量消融，覆盖正确性、TTFT/TPOT、goodput、显存与 GPU counters。
4. 取消或失败请求后必须保持哪些状态、token、KV 所有权和资源回收不变量？
5. 给出调度、缓存、kernel、量化边界和可观测性的端到端技术评审结论。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
