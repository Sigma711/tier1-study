# W44 · ZeRO、FSDP2、参数与优化器状态切分

## 本课目的

围绕 **ZeRO、FSDP2、参数与优化器状态切分** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- ZeRO
- FSDP2
- 参数与优化器状态切分

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：按 ZeRO-1/2/3 分别推导参数、梯度、optimizer state 在 N 个 rank 上的每卡显存，并计入 all-gather/reduce-scatter 临时峰值。
- **源码与产物**：定位 FSDP2 fully_shard、DTensor shard placement、unshard/reshard hook 与 distributed checkpoint state dict，区分参数驻留态和计算态。
- **性能与实验**：用峰值显存、all-gather/reduce-scatter 时间、tokens/s 对照 DDP、不同 reshard 策略与 wrap 粒度。
- **正确性与故障**：验证 shard metadata、参数顺序和 checkpoint world-size 重分片不变量；用 collective shape、state-dict key 与 OOM 时间点诊断错分片或预取峰值。
- **系统设计与评审**：在 ZeRO/FSDP2 的容量收益、通信放大、CPU offload 和 checkpoint 复杂度间选择，给出模型规模与互联条件。

## 与既有经验的连接

- **数据库内核**：参数 shard 像水平分区，unshard 像执行前 materialize；但参数分片由计算图需求驱动，不具备 SQL 分区裁剪语义。
- **存储引擎**：sharded state dict 类似分片快照；但 rank-local 文件不能脱离全局 metadata 独立恢复。
- **计算引擎**：all-gather/reduce-scatter 类似 repartition exchange；但其布局与张量维度强绑定，代价由层级执行顺序决定。
- **分布式系统**：FSDP process group 像固定分片成员集；但它不自动提供弹性重配置与复制容错。
- **可观测性**：峰值显存必须与 unshard/prefetch 时间线对齐；只看稳态 allocated memory 会漏掉临时峰值。

## 知识型学习产出

比较 DDP 与 FSDP 的显存、吞吐

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
