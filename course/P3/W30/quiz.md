# W30 · 简短 Quiz

1. 比较 TTIR、TTGIR、PTX、StableHLO、XLA HLO、IREE Flow/HAL、TVM TensorIR 各自抽象层。
2. 给定矩阵乘 tile，计算每 program 的 FLOPs、读写字节与算术强度，判断 roofline 瓶颈。
3. 为什么同一 StableHLO op 经不同 Backend 不能保证相同数值细节与性能？
4. 如何用逐级 IR dump、PTX 和 GPU counters 定位 layout lowering 退化？
5. 何时选 Triton kernel DSL，何时选 XLA/IREE/TVM 端到端栈？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
