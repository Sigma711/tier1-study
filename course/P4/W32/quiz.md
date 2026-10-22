# W32 · 简短 Quiz

1. 推导 Transformer 单层 Prefill 与单 token Decode 的主要 FLOPs/KV 读字节，解释两者为何可能分别算力/带宽受限。
2. 写出 TTFT 与 TPOT 的时间分解；queue time 应计入哪个指标，为什么？
3. 固定模型和 GPU 时，batch、输入长度、输出长度如何改变 arithmetic intensity 与显存？
4. 异步 CUDA 未同步或预热不足会怎样歪曲测量？给出交叉证据。
5. 为交互式与离线工作负载分别确定容量目标和取舍。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
