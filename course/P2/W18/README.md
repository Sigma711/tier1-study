# W18 · Nsight Compute、Nsight Systems、Roofline、PTX/SASS、自动调优

## 本课目的

围绕 **Nsight Compute、Nsight Systems、Roofline、PTX/SASS、自动调优** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Nsight Compute
- Nsight Systems
- Roofline
- PTX/SASS
- 自动调优

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能计算 arithmetic intensity 与 Roofline 上界 \(P\le\min(P_{peak},AI\times BW)\)，区分 PTX 虚拟 ISA 与 SASS 机器指令及调优搜索空间规模。
- **源码与产物**：能把 Nsight Systems 时间线、Nsight Compute section/counter、PTX 和反汇编 SASS 对齐到同一 Kernel 与源码行。
- **性能与实验**：能先用 Systems 找端到端热点，再用 Compute 做受控 counter 对照；自动调优固定正确性门、shape 集、预热和统计口径。
- **正确性与故障**：能识别 profiling perturbation、采样不足、错误峰值/带宽口径、counter replay 影响和调优过拟合，并保留原始报告证据。
- **系统设计与评审**：能设计“热点发现—Roofline 分类—指令验证—候选搜索—留出 shape 验证”的性能评审流程。

## 与既有经验的连接

- **数据库内核**：执行计划 profile 与 GPU timeline 都是热点定位，成立于逐层下钻；失效于 GPU 指令/counter 语义专用。
- **存储引擎**：Roofline 的带宽顶可类比 I/O 上界；失效于 HBM 流量不是持久存储 I/O。
- **计算引擎**：自动调优像物理算子参数搜索，成立于代价比较；失效于 GPU 搜索需严格数值正确性和硬件特异验证。
- **分布式系统**：Systems 可观察 host/device 并发边界；失效于单机 timeline 不能解释网络一致性。
- **可观测性**：本课直接复用分层观测与因果对照方法；边界是 profiler 会扰动系统且 counter 需结合源码验证。

## 知识型学习产出

完整的 Kernel Profiling 与优化报告

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
