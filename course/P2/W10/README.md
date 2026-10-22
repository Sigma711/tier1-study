# W10 · GPU 微架构：SM、Warp、SIMT、线程调度、Occupancy

## 本课目的

围绕 **GPU 微架构：SM、Warp、SIMT、线程调度、Occupancy** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- GPU 微架构
- SM
- Warp
- SIMT
- 线程调度
- Occupancy

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能由每 SM 的 warp/thread/register/shared-memory 上限推导 active blocks 与 occupancy，解释 SIMT 分支发散和 warp scheduler 隐藏延迟的条件。
- **源码与产物**：能从 CUDA Kernel launch 配置、PTX 控制流与编译器资源报告定位 block/warp 映射、寄存器数和静态 shared memory。
- **性能与实验**：能固定工作量对比 block size、寄存器压力和分支模式，以 achieved occupancy、eligible warps、IPC 与耗时共同解释结果。
- **正确性与故障**：能诊断非法 launch 配置、分支发散、低 occupancy、寄存器溢出和“occupancy 高但性能低”，用 counter 与 SASS/资源报告互证。
- **系统设计与评审**：能按延迟隐藏、并行度、寄存器与 shared memory 约束选择 launch 配置，不把最大 occupancy 当唯一目标。

## 与既有经验的连接

- **数据库内核**：warp/SIMT 可类比 SIMD 向量批，成立于同指令多数据；失效于 GPU warp 调度和掩码发散不同于 CPU worker。
- **存储引擎**：寄存器/shared memory 是受限工作集，类似局部缓冲预算；失效于片上资源无持久性与页语义。
- **计算引擎**：SM 调度像有限执行槽上的 task 调度；失效于 warp 是硬件执行组而非独立算子任务。
- **分布式系统**：occupancy 的资源配额思想可类比节点容量；失效于单 SM 调度不含网络和一致性。
- **可观测性**：occupancy、stall、IPC 需与时间联合解释；失效于单一 counter 不能给出因果。

## 知识型学习产出

分析 GPU 执行模型与 CPU 的本质差异

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
