# W31 · Mini AI Compiler 综合考核

## 本课目的

围绕 **Mini AI Compiler 综合考核** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Mini AI Compiler 综合考核

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：对端到端编译器给出 `T_total=T_front+ΣT_pass+T_codegen` 与运行期 roofline/launch 模型，推导何时优化收益覆盖编译成本。
- **源码与产物**：能从输入 AST/图沿自定义 IR、rewrite/lowering 到 LLVM/Triton 产物，指出 verifier、pass pipeline、生成 kernel 与缓存对象的源码责任。
- **性能与实验**：设计基线、单变量消融和冷/热编译实验，统一 shape/硬件/精度，报告 compile latency、IR/op/kernel 数、峰值内存、吞吐与数值误差。
- **正确性与故障**：定义每层 IR 合法性、等价性、shape/layout 与缓存键不变量；用逐级 dump、差分测试、verifier 和反汇编完成故障归因。
- **系统设计与评审**：评审 Mini Compiler 的 IR 分层、pass 边界、动态 shape 策略、后端选择和缓存生命周期，明确可扩展性与复杂度预算。

## 与既有经验的连接

- **数据库内核**：完整编译链可对照 parser→binder→optimizer→executor；类比只帮助审查分层，张量数值和硬件 lowering 仍需独立证明。
- **存储引擎**：内存规划/代码缓存可对照 buffer pool/物化缓存；综合考核不能把可重建运行态误称为持久存储。
- **计算引擎**：fusion、tiling、codegen 与执行计划生成强相关；GPU occupancy 和寄存器压力超出一般算子调度模型。
- **分布式系统**：IR/制品版本契约类似跨服务兼容；Mini Compiler 仍是单机范围，不声称解决分布式编译和故障容错。
- **可观测性**：阶段耗时、IR diff、生成代码和运行 counters 形成端到端证据链；任何单一指标都不足以通过综合考核。

## 知识型学习产出

展示 IR、Pass、正确性测试、性能收益与失败案例

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
