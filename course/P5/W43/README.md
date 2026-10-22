# W43 · DDP、Gradient Synchronization、AllReduce、通信与计算重叠

## 本课目的

围绕 **DDP、Gradient Synchronization、AllReduce、通信与计算重叠** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- DDP
- Gradient Synchronization
- AllReduce
- 通信与计算重叠

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：推导 p 个 rank、梯度总量 M 时 ring AllReduce 每 rank 约 2(p-1)M/p 字节通信量，并用 alpha-beta 模型解释 bucket 大小与重叠上界。
- **源码与产物**：定位 PyTorch DDP Reducer、gradient bucket、autograd hook 与 process group AllReduce，说明梯度何时 ready、何时除以 world size。
- **性能与实验**：以 exposed communication time、bucket ready time、step time 和 scaling efficiency 为指标，对照 bucket cap、模型层序与网卡带宽。
- **正确性与故障**：守住所有 rank 参数初值、collective 顺序和 unused-parameter 判定一致；用 NCCL trace、rank stack 与 bucket 日志诊断 hang、慢 rank 和错误重叠。
- **系统设计与评审**：在小 bucket 的启动开销与大 bucket 的晚就绪之间取舍，并判断何时 DDP 的复制显存与同步屏障已不适合目标规模。

## 与既有经验的连接

- **数据库内核**：DDP bucket 像批量交换缓冲，ready hook 像流水执行触发；但梯度平均只保证副本更新一致，不提供事务隔离。
- **存储引擎**：梯度 bucket 的聚合类似批写合并；但它每步可重建且不具有 WAL 的持久恢复语义。
- **计算引擎**：计算/通信重叠类似 exchange 与上游算子流水；但 collective 要求所有 rank 顺序一致，不能任意异步重排。
- **分布式系统**：AllReduce 是固定成员 collective；它不负责成员变更或故障共识，某 rank 缺席通常会整体阻塞。
- **可观测性**：bucket ready、NCCL duration 与 rank skew 能解释 exposed communication；平均 step time 会掩盖尾部慢 rank。

## 知识型学习产出

实现多 GPU 数据并行实验

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
