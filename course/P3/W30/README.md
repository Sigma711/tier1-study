# W30 · Triton Compiler、TTIR/TTGIR、PTX；XLA、StableHLO、IREE、TVM 对照

## 本课目的

围绕 **Triton Compiler、TTIR/TTGIR、PTX；XLA、StableHLO、IREE、TVM 对照** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Triton Compiler
- TTIR/TTGIR
- PTX
- XLA
- StableHLO
- IREE
- TVM 对照

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：以矩阵乘为例推导 program instance、tile、访存字节和算术强度，并比较各栈从张量语义到目标代码时保留/丢失的信息。
- **源码与产物**：定位 Triton AST→TTIR→TTGIR→LLVM/PTX 管线，并辨认 StableHLO ops、XLA HLO、IREE Flow/HAL 与 TVM TensorIR 的对应层次。
- **性能与实验**：固定算子、shape、GPU 与精度，对照各栈生成代码的 compile time、kernel 数、HBM 流量、occupancy 和运行时间，避免跨环境排行榜。
- **正确性与故障**：验证 TTIR/TTGIR layout、PTX target、StableHLO verifier 与各栈数值结果；用逐级 dump 和反汇编诊断非法 lowering 或性能退化。
- **系统设计与评审**：评审选择 Triton 专用 kernel DSL 或 XLA/IREE/TVM 端到端栈，在可移植性、可控 codegen、生态集成和部署体积之间取舍。

## 与既有经验的连接

- **数据库内核**：多级 IR 类似逻辑/物理/可执行计划层次；不同编译栈的 op 语义不能按同名算子假定等价。
- **存储引擎**：layout encoding 类似物理布局元数据；它描述设备内数据组织，不提供磁盘持久格式与升级兼容。
- **计算引擎**：Triton tile program 与向量化执行批处理相似；GPU 线程层次、共享内存和 PTX 是额外硬件约束。
- **分布式系统**：StableHLO 等交换 IR 类似跨组件协议；可序列化不等于不同后端数值、性能与版本完全一致。
- **可观测性**：各级 IR dump、PTX、编译时间与 GPU counters 可比较信息损失；跨栈只报最终 latency 会掩盖编译与环境差异。

## 知识型学习产出

比较不同编译路线和优化策略

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
