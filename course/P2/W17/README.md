# W17 · FlashAttention、Online Softmax、IO Complexity、Warp 分工

## 本课目的

围绕 **FlashAttention、Online Softmax、IO Complexity、Warp 分工** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- FlashAttention
- Online Softmax
- IO Complexity
- Warp 分工

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能推导 online softmax 的 running max/sum 合并式，说明 FlashAttention 保持精确 attention 而降低 HBM I/O，并分析序列块与 warp 分工。
- **源码与产物**：能在 FlashAttention 官方实现中定位 forward tile loop、softmax state、Q/K/V staging 与 warp partition，区分论文伪码和当前 Kernel。
- **性能与实验**：能固定 batch、heads、L、head_dim、dtype，对比标准 attention 的 latency、HBM bytes、workspace 与误差，覆盖多种长度。
- **正确性与故障**：能诊断 causal mask、边界 tile、online rescale、低精度累加和 head_dim 限制，用参考 attention 与 profiler 证据定位。
- **系统设计与评审**：能根据长度、head_dim、硬件、精度和维护成本决定使用框架 SDPA、FlashAttention 或普通实现。

## 与既有经验的连接

- **数据库内核**：online softmax 像可合并流式聚合，成立于维护充分统计量；失效于 attention 还需重标定输出向量。
- **存储引擎**：IO-aware tiling 像 cache-aware 算法，成立于减少慢层访问；失效于 HBM/SRAM 无持久层语义。
- **计算引擎**：warp 分工与 tile pipeline 是细粒度执行计划；失效于其正确性依赖数值恒等式和 GPU 同步。
- **分布式系统**：块间状态合并可类比局部聚合；失效于没有网络故障、一致性或重试。
- **可观测性**：长度分层的 HBM bytes、latency 和误差验证 IO 收益；失效于单一短序列结果不能外推长序列。

## 知识型学习产出

复现核心算法并分析 I/O 收益

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
