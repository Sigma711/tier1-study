# W27 · Tensor Layout、Shape Inference、动态形状、符号维度、内存规划

## 本课目的

围绕 **Tensor Layout、Shape Inference、动态形状、符号维度、内存规划** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Tensor Layout
- Shape Inference
- 动态形状
- 符号维度
- 内存规划

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：用 shape 符号与 stride 公式推导 tensor 地址，计算静态/动态 buffer 生命周期重叠时的峰值内存，并说明 shape constraint 求解的保守性。
- **源码与产物**：定位 MLIR Shape dialect、tensor/memref layout maps、shape inference interfaces 与 buffer deallocation/planning 相关 IR，辨认动态维和符号约束。
- **性能与实验**：固定算子图，对照 contiguous/strided layout、静态/动态 shape 与复用策略，测量 guard/shape 开销、峰值内存和访存带宽。
- **正确性与故障**：验证 rank/dimension/stride 一致、符号约束可满足、复用 buffer 生命周期不重叠；用 shape assertion、IR verifier 和越界/峰值 trace 诊断。
- **系统设计与评审**：评审为动态 shape 保留通用实现、按符号范围特化或回退的代码膨胀、缓存命中、内存利用率与正确性取舍。

## 与既有经验的连接

- **数据库内核**：Shape inference 类似 schema/基数属性传播；tensor 维度约束通常精确，查询基数估计则是统计近似。
- **存储引擎**：layout/stride 与行列布局、页内偏移相似；tensor buffer 是运行态内存，不含持久编码、校验和恢复。
- **计算引擎**：动态 shape 与运行时 schema/批大小传播相似；符号维会驱动代码特化，而一般算子调度未必生成新代码。
- **分布式系统**：符号约束像部署前置条件，guard 失败触发其他路径；它不是共识协议，也不处理节点间状态分歧。
- **可观测性**：shape、stride、allocation timeline 与峰值水位可解释内存；仅记录 OOM 不能定位是约束失真还是生命周期重叠。

## 知识型学习产出

实现布局与 Shape 相关优化

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
