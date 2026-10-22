# W06 · 神经网络计算图、Autograd、计算与内存复杂度、Activation

## 本课目的

围绕 **神经网络计算图、Autograd、计算与内存复杂度、Activation** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 神经网络计算图
- Autograd
- 计算与内存复杂度
- Activation

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能为前向/反向 DAG 推导 FLOPs、参数/梯度/Activation 字节数和关键路径，解释 checkpointing 以重算换内存。
- **源码与产物**：能读 PyTorch autograd graph 的 `Function/Node`、saved tensors、version counter 与 FX graph，区分动态图记录和实际 Kernel。
- **性能与实验**：能按层比较 forward/backward 时间、saved Activation 峰值和重算开销，以固定模型/批量对照 checkpoint 前后。
- **正确性与故障**：能诊断 graph retention 泄漏、detach 断梯度、in-place 修改、错误 requires_grad 与 Activation OOM，并用图和内存快照举证。
- **系统设计与评审**：能在 eager 可调试性、图捕获优化、Activation checkpoint 粒度和峰值内存间作出可解释选择。

## 与既有经验的连接

- **数据库内核**：计算图像逻辑/物理执行计划，成立于依赖和代价分析；失效于 Autograd 还记录微分与生命周期语义。
- **存储引擎**：Activation 保存/重算像物化视图与重算，成立于空间—计算交换；失效于 Activation 是短生命周期易失状态。
- **计算引擎**：DAG 调度、关键路径和算子边界高度相似；失效于反向图由微分规则生成且数值语义特殊。
- **分布式系统**：依赖完成与异步调度可借鉴 happens-before；失效于本课图内同步不等于跨节点共识。
- **可观测性**：图节点耗时、内存快照和版本计数能构成诊断链；失效于汇总显存峰值无法单独定位哪个节点保留对象。

## 知识型学习产出

研究 PyTorch 自动微分执行图

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P1：AI 计算基础与现代模型架构](../README.md)
