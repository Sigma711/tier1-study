# W49 · TorchTitan / Megatron 综合研究

## 本课目的

围绕 **TorchTitan / Megatron 综合研究** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- TorchTitan / Megatron 综合研究

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：从 TorchTitan 与 Megatron 的并行配置推导给定模型规模、序列长度和 mesh 下的每卡参数/激活显存、collective 量与理论 MFU 上界。
- **源码与产物**：对照 TorchTitan parallelisms/config/训练循环与 Megatron Core transformer/parallel_state/schedules，追踪同一训练 step 的配置到 Kernel 调用链。
- **性能与实验**：统一模型、精度、global batch 与硬件，对照 tokens/s、MFU、峰值显存和 checkpoint pause，避免拿不同口径排行榜作结论。
- **正确性与故障**：检查 parallel group、loss scaling、随机数与 checkpoint reshard 不变量；用 config dump、rank mapping、loss curve 和 trace 定位框架差异。
- **系统设计与评审**：基于扩展性、可插拔性、运维成熟度与源码可审查性选择 TorchTitan 或 Megatron，并明确迁移成本。

## 与既有经验的连接

- **数据库内核**：两框架的训练循环可像两个内核执行器做语义对照；但 API 同名不保证随机数、loss scaling 或状态布局相同。
- **存储引擎**：checkpoint 实现可按格式、分片和恢复契约比较；但文件数量少不等于恢复语义更强。
- **计算引擎**：并行配置像物理计划搜索空间；但训练拓扑受模型层与张量 shape 强约束，不能仅靠成本优化器自动决定。
- **分布式系统**：process group 与 rank mapping 可按故障域审查；但本课框架对比不引入新的弹性协议。
- **可观测性**：统一实验口径后比较 MFU、显存和 trace；框架自报吞吐若口径不同不能直接排序。

## 知识型学习产出

完成分布式训练实验与故障分析报告

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
