# W39 · 简短 Quiz

1. 分别写出 TP collective、PP bubble、EP all-to-all 与 P/D KV transfer 的主要通信量/等待来源。
2. 给定计算时间与通信带宽，建立每 token 关键路径并判断增加 GPU 为何可能变慢。
3. rank/world-size、collective 次序、stage shape 或 KV 请求身份错配各产生什么故障证据？
4. 对照共置与 P/D 分离实验必须固定哪些请求和拓扑变量？
5. 为目标 SLO 组合 TP/PP/EP 与路由策略，明确故障域取舍。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
