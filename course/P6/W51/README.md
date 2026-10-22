# W51 · 模型权重、Checkpoint、分布式存储、一致性与恢复语义

## 本课目的

围绕 **模型权重、Checkpoint、分布式存储、一致性与恢复语义** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 模型权重
- Checkpoint
- 分布式存储
- 一致性与恢复语义

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：由权重/optimizer state 总量 S、rank 数 N、带宽 B 和 checkpoint 间隔 I 推导每 rank 写量、理论保存时长与故障浪费上界。
- **源码与产物**：定位 PyTorch Distributed Checkpoint planner、StorageWriter/Reader、metadata 与 state_dict mapping，解释 model weights 与训练状态的不同恢复契约。
- **性能与实验**：以 checkpoint pause、aggregate bandwidth、文件/请求数和 restore time 为指标，对照分片粒度、并发度与存储后端。
- **正确性与故障**：守住一次 generation 的全局 metadata、所有 shard 与完成标记一致；用缺 shard、校验和、step/revision metadata 诊断 torn checkpoint 和错误恢复点。
- **系统设计与评审**：在全量/增量、同步/异步、可移植权重/可续训状态与存储成本之间明确选择。

## 与既有经验的连接

- **数据库内核**：checkpoint step 像一致性恢复点；但模型参数快照通常没有并发事务读写的隔离级别。
- **存储引擎**：分片 checkpoint 像 SST/分片快照，metadata 像 manifest；但缺任一必要 shard 可能使全局状态不可恢复。
- **计算引擎**：world-size 重分片像改变执行分区；但 tensor layout 与 optimizer state shape 必须数学一致，不是普通 repartition。
- **分布式系统**：完成标记把多 writer 输出绑定成 generation；对象可见不等于全局 checkpoint 已提交。
- **可观测性**：pause、写带宽、失败 shard 和 restore 校验构成证据链；只记录“上传成功”不足以证明可恢复。

## 知识型学习产出

实现并测试可恢复的 Checkpoint 流程

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P6：AI Data、GPU Cluster 与生产级基础设施](../README.md)
