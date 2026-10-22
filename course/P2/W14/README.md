# W14 · GEMM、Tiling、Tensor Core、MMA、CUTLASS

## 本课目的

围绕 **GEMM、Tiling、Tensor Core、MMA、CUTLASS** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- GEMM
- Tiling
- Tensor Core
- MMA
- CUTLASS

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能推导 GEMM 的 \(2MNK\) FLOPs、未分块与分块的数据搬运量和 arithmetic intensity，解释 threadblock/warp/MMA tile 的层次。
- **源码与产物**：能定位 CUTLASS collective/mainloop/epilogue、Tensor Core MMA 指令和 layout，核对 accumulator dtype 与 tile shape。
- **性能与实验**：能以 cuBLAS 为基线，固定 M/N/K、layout、dtype，对比 TFLOP/s、Tensor Core 利用率、DRAM bytes 与误差。
- **正确性与故障**：能诊断 leading dimension/layout 错误、tile 边界、对齐、累加精度、寄存器压力和 Tensor Core 未命中。
- **系统设计与评审**：能按 shape 分布、精度、融合 epilogue 与维护成本选择 cuBLAS、CUTLASS 或自定义 Kernel。

## 与既有经验的连接

- **数据库内核**：GEMM tiling 像 cache-aware blocking，成立于复用与工作集；失效于 MMA shape 和 Tensor Core 是 GPU 专用约束。
- **存储引擎**：矩阵 layout/leading dimension 像页内布局，成立于连续访问；失效于矩阵无记录/事务语义。
- **计算引擎**：tile 层次像分层执行计划，成立于局部计算与合并；失效于 CUTLASS 模板实例是 Kernel 生成机制。
- **分布式系统**：此处只含芯片内数据复用；不能把 tile 分工类比成跨节点分片后推导容错。
- **可观测性**：TFLOP/s、Tensor Core 指令、DRAM bytes 与误差需联合；失效于高峰值百分比不代表所有 shape 都优。

## 知识型学习产出

解释 GEMM 分块策略与性能

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
