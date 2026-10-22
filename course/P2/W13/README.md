# W13 · 并行算法：Reduction、Scan、Atomic、Synchronization

## 本课目的

围绕 **并行算法：Reduction、Scan、Atomic、Synchronization** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 并行算法
- Reduction
- Scan
- Atomic
- Synchronization

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能推导树形 reduction 的 \(O(n)\) work/\(O(\log n)\) span、Blelloch scan 的上下扫过程，并分析 atomic contention 与同步次数。
- **源码与产物**：能读 CUDA cooperative groups/CUB 的 reduction、scan，定位 `__syncthreads`、warp shuffle 与 atomic 指令的作用域。
- **性能与实验**：能固定输入与 dtype，对比 naïve、shared、shuffle、atomic 实现，以 GB/s、items/s、同步/atomic stall 和误差衡量。
- **正确性与故障**：能诊断 barrier divergence、race、错误 identity、非结合浮点重排和 atomic 热点，用 Compute Sanitizer 与参考结果举证。
- **系统设计与评审**：能根据输入规模、结合性、确定性要求和 contention 选择分层 reduction/scan 或 atomic。

## 与既有经验的连接

- **数据库内核**：reduction 像并行聚合，成立于结合律与局部聚合；失效于浮点重排导致非确定误差。
- **存储引擎**：scan 可类比前缀索引构造，成立于前缀状态；失效于 GPU 临时存储没有持久索引语义。
- **计算引擎**：work/span 和分层合并可直接用于并行算子设计；失效于 barrier/warp shuffle 是硬件作用域机制。
- **分布式系统**：atomic 像共享状态串行化热点；失效于设备原子不提供跨节点容错。
- **可观测性**：racecheck、stall 与结果误差共同定位并发问题；失效于结果偶尔正确不能证明无 race。

## 知识型学习产出

比较不同并行规约算法

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
