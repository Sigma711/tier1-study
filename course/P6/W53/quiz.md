# W53 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Kubernetes GPU Operator、Device Plugin、MIG/MPS、NUMA 与资源隔离。

1. 由整卡/MIG profile、CPU/内存和 NUMA 拓扑推导可调度容量与碎片。
2. GPU Operator ClusterPolicy、Device Plugin ListAndWatch/Allocate 与 kubelet 各自负责什么？
3. 比较 MIG 与 MPS 的隔离、利用率、重配置和干扰边界。
4. Pod Running 但 PCIe 吞吐异常时，如何用 allocation、topology 与 NUMA counter 定位？
5. 为混部负载选择整卡、MIG 或 MPS，并说明资源和安全边界。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
