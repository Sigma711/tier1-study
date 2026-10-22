# W59 · Kernel：分析性能瓶颈并实现优化

## 本课目的

围绕 **Kernel：分析性能瓶颈并实现优化** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Kernel
- 分析性能瓶颈并实现优化

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：计算 Kernel 的 FLOPs、global/shared-memory bytes、算术强度、occupancy 约束与 Roofline 上界。
- **源码与产物**：定位 Triton/CUDA program id、tile、load/store、reduction 与编译后的 PTX/SASS，解释访问合并和同步。
- **性能与实验**：以 kernel latency、DRAM/L2 throughput、SM utilization 与 occupancy 对照基线，只改变 tile/warps/stages 等一个变量。
- **正确性与故障**：守住边界 mask、竞态、精度和任意 shape；用 sanitizer、差分测试、Nsight counter 与 SASS 诊断。
- **系统设计与评审**：权衡专用 shape 极致性能、通用性、编译组合爆炸与维护成本，定义回退 Kernel。

## 与既有经验的连接

- **数据库内核**：向量化内核与 SIMD 算子类比成立；但 GPU warp/memory hierarchy 决定的瓶颈不同。
- **存储引擎**：coalesced access 类似顺序访问；但 shared/L2/HBM 都是运行时层级，不提供持久性。
- **计算引擎**：tile 与批处理、fusion 与算子流水相似；但寄存器压力可能让理论融合收益反转。
- **分布式系统**：Kernel 是单设备执行单元，本周不能用网络扩展性掩盖本地低效。
- **可观测性**：Nsight counter 必须与源码/SASS 对齐；高 occupancy 既非必要也非充分的高性能证据。

## 知识型学习产出

Profiling 与 Kernel Benchmark

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P7：综合毕业项目与高级工程师面试](../README.md)
