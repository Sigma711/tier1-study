# W45 · Tensor、Sequence、Context Parallelism、DTensor、DeviceMesh

## 本课目的

围绕 **Tensor、Sequence、Context Parallelism、DTensor、DeviceMesh** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Tensor
- Sequence
- Context Parallelism
- DTensor
- DeviceMesh

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：为 Y=XW 推导 column/row tensor parallel 的局部 GEMM shape 与 collective 字节数，并比较 sequence/context 切分下 attention 激活和通信随序列长度的增长。
- **源码与产物**：定位 PyTorch DeviceMesh、DTensor Shard/Replicate/Partial placement 和 TorchTitan parallelize plan，解释布局传播与 redistribution。
- **性能与实验**：用 GEMM 利用率、collective 时间、每卡激活显存和端到端 tokens/s，对照 mesh shape、TP/sequence/context degree。
- **正确性与故障**：守住 global tensor shape、placement 与 mesh 维度一致；用 DTensor layout、collective shape 和数值对齐证据诊断 silent wrong result 或死锁。
- **系统设计与评审**：按算子 shape、序列长度与节点内外带宽，选择 Tensor、Sequence、Context Parallelism 组合及 DeviceMesh 映射。

## 与既有经验的连接

- **数据库内核**：DTensor placement 类似分区元数据；但 Partial 表示待归约的数学状态，不是未提交事务。
- **存储引擎**：tensor layout 像数据布局；但 Replicate/Shard 的选择服务于算子通信，不等同于持久化副本策略。
- **计算引擎**：redistribute 是显式 exchange，mesh 是执行拓扑；但 attention 的序列依赖使关系算子式局部性类比在 context parallel 处失效。
- **分布式系统**：mesh 维度提供通信域；它不处理故障成员替换，布局一致也不代表高可用。
- **可观测性**：应把 GEMM shape、collective 与 mesh 维度关联；总通信量相同也可能因跨节点映射产生不同尾延迟。

## 知识型学习产出

进行多维并行实验

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
