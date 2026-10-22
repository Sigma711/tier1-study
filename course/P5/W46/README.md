# W46 · Pipeline Parallelism、Microbatch、GPipe、1F1B、Pipeline Bubble

## 本课目的

围绕 **Pipeline Parallelism、Microbatch、GPipe、1F1B、Pipeline Bubble** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Pipeline Parallelism
- Microbatch
- GPipe
- 1F1B
- Pipeline Bubble

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：推导 p 个 stage、m 个 microbatch 时 GPipe 近似 bubble fraction (p-1)/(m+p-1)，并比较 1F1B 的激活驻留量。
- **源码与产物**：定位 PyTorch pipelining 的 stage、schedule、microbatch split/merge 与 send/recv，画出 GPipe 和 1F1B 的时序产物。
- **性能与实验**：以 bubble ratio、stage idle time、激活峰值和吞吐为指标，对照 microbatch 数、partition 与 stage balance。
- **正确性与故障**：验证跨 stage tensor shape/dtype、microbatch loss 缩放和 schedule 顺序；用 timeline 诊断 shape mismatch、stage skew 与通信阻塞。
- **系统设计与评审**：在 GPipe 的简单批调度与 1F1B 的低激活/复杂依赖间取舍，并给出分层切点和 microbatch 选择依据。

## 与既有经验的连接

- **数据库内核**：microbatch 流水类似向量批次穿过执行阶段；但反向依赖和权重版本约束使其不能任意乱序。
- **存储引擎**：激活驻留像中间结果缓存；但可重算激活没有持久恢复价值，容量模型取决于 schedule。
- **计算引擎**：stage partition 与 exchange 最接近分布式算子流水；但 GPipe/1F1B 还要调度正反向两类依赖。
- **分布式系统**：stage 间 send/recv 形成同步故障链；它不是容错消息队列，任一 stage 失联可阻塞全局。
- **可观测性**：timeline 中的空槽直接对应 bubble；平均 GPU busy 不能定位哪个 stage 造成不平衡。

## 知识型学习产出

模拟并测量流水线利用率

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
