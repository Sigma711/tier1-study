# W11 · GPU 内存层次：Register、Shared Memory、L1/L2、HBM、Coalescing

## 本课目的

围绕 **GPU 内存层次：Register、Shared Memory、L1/L2、HBM、Coalescing** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- GPU 内存层次
- Register
- Shared Memory
- L1/L2
- HBM
- Coalescing

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能由 warp 地址模式推导 memory transactions 与有效带宽，量化 register/shared/L1/L2/HBM 的容量、作用域和延迟层级。
- **源码与产物**：能从 CUDA C++、PTX load/store 和资源报告识别 global/shared/local 访问、cache hint 与寄存器溢出。
- **性能与实验**：能固定算术工作量对比 stride、alignment、AoS/SoA 和 shared-memory staging，以 transactions/request、cache hit、DRAM bytes 与 GB/s 评估。
- **正确性与故障**：能诊断未对齐/非合并访问、shared bank conflict、local memory spill、越界和陈旧数据，用 sanitizer 与内存 counter 举证。
- **系统设计与评审**：能在复用率、同步成本、占用资源和布局改造复杂度间决定使用 shared/cache 或直接访问 HBM。

## 与既有经验的连接

- **数据库内核**：coalescing 类似向量化连续列访问，成立于批量搬运；失效于 warp transaction 由 GPU 硬件规则决定。
- **存储引擎**：HBM/cache/shared 层次可类比 buffer hierarchy，成立于局部性；失效于片上内存无持久、替换与事务保证。
- **计算引擎**：shared staging 像算子内物化以复用数据；失效于同步和 bank 结构是 GPU 特有约束。
- **分布式系统**：带宽与背压思路可用于理解供给不足；失效于芯片内 transaction 不是网络消息。
- **可观测性**：cache hit、DRAM bytes、transactions 结合代码地址模式才有解释力；失效于命中率高不保证耗时低。

## 知识型学习产出

设计并测量不同访存模式

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
