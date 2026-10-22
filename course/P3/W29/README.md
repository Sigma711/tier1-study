# W29 · AOTAutograd、TorchInductor、Kernel Fusion、Code Generation、编译缓存

## 本课目的

围绕 **AOTAutograd、TorchInductor、Kernel Fusion、Code Generation、编译缓存** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- AOTAutograd
- TorchInductor
- Kernel Fusion
- Code Generation
- 编译缓存

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：从前向/反向图的保存张量推导内存下界，用 kernel launch 开销与中间流量模型判断 fusion 收益，并计算编译缓存摊销点。
- **源码与产物**：定位 AOTAutograd joint graph/partitioner、Inductor scheduler/IR、生成的 Triton/C++ kernel 与 code cache key。
- **性能与实验**：固定模型、shape 和精度，对照 eager、未融合/融合、冷/热缓存，记录 graph 数、kernel 数、编译时间、峰值内存和端到端延迟。
- **正确性与故障**：验证 forward/backward 数值与梯度、mutation/alias 语义、cache key 完整性；用 generated code、cache log、minifier 和误差对照定位错编译。
- **系统设计与评审**：评审 joint graph 分割、激进 fusion 和缓存粒度，在重计算、峰值内存、寄存器压力、冷启动与磁盘占用间取舍。

## 与既有经验的连接

- **数据库内核**：Inductor scheduler/fusion 像物理计划重排和表达式融合；autograd 的保存/重计算没有 SQL 优化器中的直接对应。
- **存储引擎**：code cache 类似物化结果缓存，key 必须包含语义环境；缓存对象可重建，不具备日志恢复与强一致读。
- **计算引擎**：generated kernels 对应 codegen operator pipeline；GPU fusion 还受寄存器、launch 与设备编译约束。
- **分布式系统**：缓存 key 的版本隔离类似制品兼容控制；本课不覆盖跨节点缓存一致性或分布式编译。
- **可观测性**：AOT graph、Inductor IR、生成源码、kernel trace 与 cache hit 串联因果；只看端到端加速无法判定来自 fusion 还是热缓存。

## 知识型学习产出

跟踪 `torch.compile` 的真实生成代码

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
