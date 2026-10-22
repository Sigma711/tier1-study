# W25 · Affine、SCF、Linalg、Tiling、Fusion、Bufferization

## 本课目的

围绕 **Affine、SCF、Linalg、Tiling、Fusion、Bufferization** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Affine
- SCF
- Linalg
- Tiling
- Fusion
- Bufferization

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：以二维 Linalg 迭代域推导 tile 后工作量不变而数据搬运由复用决定，并估算 tile 尺寸受 cache/shared-memory 容量的上界。
- **源码与产物**：定位 MLIR Affine/SCF/Linalg dialect 的 op definitions、tiling/fusion interfaces 与 One-Shot Bufferize，读出 tensor 到 memref 的 alias/equivalence 决策。
- **性能与实验**：固定算子 shape 与后端，对照 tile size、fusion 开关和 bufferization 策略，观测内存流量、峰值内存、编译时间与运行时间。
- **正确性与故障**：验证 affine bound 合法、迭代域覆盖、fusion 不改变依赖顺序、bufferization 不破坏读写冲突；用 verifier、IR diff 与 copy 统计定位失败。
- **系统设计与评审**：评审结构化 Linalg 路线与提前降为 loops 的取舍，以及 destination-passing style、in-place bufferization 对可优化性和内存峰值的影响。

## 与既有经验的连接

- **数据库内核**：Affine/Linalg 迭代域像规则化的逻辑算子语义；循环依赖与内存副作用不能简化为关系代数等价。
- **存储引擎**：Tiling 和 Bufferization 可类比页/块粒度与缓冲区复用；编译期 memref 不提供持久性、WAL 或并发隔离。
- **计算引擎**：Fusion 对应 operator fusion，减少中间物化；过度融合同样会扩大工作集，但 GPU 寄存器/shared-memory 约束更硬。
- **分布式系统**：tile 划分像分片，但本课 tile 仍在单程序地址空间内，没有跨节点通信和故障恢复。
- **可观测性**：IR 中的 tile/fusion/copy、峰值内存和硬件计数器构成证据链；只见算子数下降不能证明性能提升。

## 知识型学习产出

将高层 Tensor Operation 逐级 Lowering

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
