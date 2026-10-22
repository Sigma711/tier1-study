# W47 · MoE、Expert Parallelism、All-to-All、负载均衡

## 本课目的

围绕 **MoE、Expert Parallelism、All-to-All、负载均衡** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- MoE
- Expert Parallelism
- All-to-All
- 负载均衡

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：由 tokens T、专家数 E、top-k 与 capacity factor 推导每专家期望负载、丢弃上界和 All-to-All 发送量。
- **源码与产物**：定位 Megatron Core router logits、top-k dispatch、token permutation、expert group 与 All-to-All，解释 auxiliary load-balancing loss 的作用位置。
- **性能与实验**：以 expert load CV、dropped tokens、All-to-All 时间和 tokens/s 为指标，对照 capacity factor、top-k 与 expert-parallel degree。
- **正确性与故障**：守住 token→expert→token 的索引可逆性和容量语义；用每专家 token 直方图、router entropy 与 collective trace 诊断热点、丢 token 或 hang。
- **系统设计与评审**：权衡专家容量、模型质量、通信局部性和热点风险，决定专家布局与负载均衡策略。

## 与既有经验的连接

- **数据库内核**：router 像按 key 分区，专家像分区执行单元；但路由由学习出的概率决定，负载与语义可共同漂移。
- **存储引擎**：expert 权重分布像分片数据布局；但 token dispatch 是每层瞬时交换，不是持久数据迁移。
- **计算引擎**：All-to-All 像 shuffle，capacity factor 像背压缓冲；但丢弃 token 会直接改变模型函数而不只是降低吞吐。
- **分布式系统**：专家热点类似倾斜分区；但不能仅靠一致性哈希修复，因为 router quality 是训练目标的一部分。
- **可观测性**：每专家 token 数、router entropy 与 All-to-All 尾延迟需联合观察；平均负载会隐藏单专家溢出。

## 知识型学习产出

分析专家分配与通信代价

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
