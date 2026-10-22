# W53 · Kubernetes GPU Operator、Device Plugin、MIG/MPS、NUMA 与资源隔离

## 本课目的

围绕 **Kubernetes GPU Operator、Device Plugin、MIG/MPS、NUMA 与资源隔离** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Kubernetes GPU Operator
- Device Plugin
- MIG/MPS
- NUMA 与资源隔离

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：由 GPU/MIG profile、CPU/内存和 NUMA 拓扑推导可调度容量与碎片率，并区分 MPS 时间共享和 MIG 空间隔离。
- **源码与产物**：定位 GPU Operator ClusterPolicy、NVIDIA device plugin ListAndWatch/Allocate、MIG strategy 与 kubelet topology hints。
- **性能与实验**：以 allocatable、pending time、GPU/CPU locality、PCIe throughput 和 interference 为指标，对照 MIG/MPS、NUMA 绑定与 workload mix。
- **正确性与故障**：守住 advertised resource 与实际 device/MIG identity 一致；用 pod allocation、plugin log、nvidia-smi topology 与 NUMA counter 诊断错配。
- **系统设计与评审**：在隔离强度、切分粒度、利用率与重配置成本间选择整卡、MIG 或 MPS，并定义 NUMA 放置策略。

## 与既有经验的连接

- **数据库内核**：GPU extended resource 像资源组配额；但 kube-scheduler 只做放置，不感知 Kernel 内部干扰。
- **存储引擎**：NUMA locality 类似数据与计算共置；但 GPU HBM/MIG 不是由通用页缓存管理的持久层。
- **计算引擎**：Device Plugin 暴露执行资源，topology hints 辅助放置；但不负责生成模型并行执行计划。
- **分布式系统**：Operator 管理驱动/插件生命周期；控制器 reconcile 成功不代表每个节点设备健康。
- **可观测性**：allocatable、MIG identity、PCIe/NUMA 与 workload 指标要关联；Pod Running 不证明资源隔离有效。

## 知识型学习产出

部署 GPU Workload 并分析资源拓扑

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P6：AI Data、GPU Cluster 与生产级基础设施](../README.md)
