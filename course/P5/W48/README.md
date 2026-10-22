# W48 · NCCL、Ring/Tree Collectives、NVLink、RDMA、异步 Checkpoint

## 本课目的

围绕 **NCCL、Ring/Tree Collectives、NVLink、RDMA、异步 Checkpoint** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- NCCL
- Ring/Tree Collectives
- NVLink
- RDMA
- 异步 Checkpoint

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：分别用 alpha-beta 模型推导 ring/tree collective 延迟趋势，并以状态量 S、持久化带宽 B 推导异步 Checkpoint 的 staging 内存和重叠窗口。
- **源码与产物**：在 NCCL 拓扑/算法选择与 PyTorch Distributed Checkpoint async save 中分别定位 communicator/channel 与 staging/planner/future，明确两条独立控制路径。
- **性能与实验**：通信侧测 bus bandwidth、collective latency 并对照 Ring/Tree、NVLink/RDMA；持久化侧测 pause time、后台写带宽与 staging 峰值并对照同步/异步保存。
- **正确性与故障**：用 rank/collective 顺序、拓扑日志诊断 NCCL hang；用 checkpoint generation、原子完成标记和恢复校验诊断半成品或状态错配。
- **系统设计与评审**：独立选择节点内/节点间 collective 路径与 checkpoint 介质、频率和一致性边界，不能用“通信更快”替代恢复设计。

## 与既有经验的连接

- **数据库内核**：collective 顺序像并行算子协议，异步 checkpoint 像后台快照；但 NCCL 完成不代表模型状态已持久化。
- **存储引擎**：staging buffer 与异步落盘类似 snapshot writer；但必须另行定义跨 rank checkpoint 的完成标记，不能套用单机 fsync 结论。
- **计算引擎**：Ring/Tree 是通信物理计划；但算法最优性取决于拓扑与消息规模，不存在固定万能计划。
- **分布式系统**：RDMA/NVLink 提供数据路径，NCCL 提供 collective；它们都不替代 checkpoint generation 的一致性协议。
- **可观测性**：NCCL topology/debug 日志与 storage throughput/queue depth 是两组证据；不能把 checkpoint 卡顿一律归因于网络。

## 知识型学习产出

建立多 GPU 通信性能基线

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
