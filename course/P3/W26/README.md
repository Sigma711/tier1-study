# W26 · Dialect Conversion、LLVM Lowering、GPU CodeGen

## 本课目的

围绕 **Dialect Conversion、LLVM Lowering、GPU CodeGen** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Dialect Conversion
- LLVM Lowering
- GPU CodeGen

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：将合法化问题建模为 conversion target 上的图重写，推导全/部分 conversion 的成功条件，并估算 GPU grid/block 映射下线程数与占用约束。
- **源码与产物**：定位 MLIR `ConversionTarget`、`TypeConverter`、conversion patterns、LLVM dialect，以及 GPU dialect 到 NVVM/ROCDL 的 lowering 产物。
- **性能与实验**：固定高层 op 与 GPU，对照 lowering 路径和 block size，记录转换耗时、生成 IR/PTX 大小、occupancy 与 kernel 时间。
- **正确性与故障**：验证 illegal op 清零、类型/ABI 一致、地址空间与 barrier 语义正确；以 conversion diagnostic、LLVM verifier、GPU sanitizer/launch error 为证据。
- **系统设计与评审**：评审一步直降 LLVM 与分层 lowering 的可维护性、优化窗口、诊断能力和多 GPU backend 复用成本。

## 与既有经验的连接

- **数据库内核**：Dialect conversion 像逻辑到物理计划合法化；GPU 地址空间和同步语义没有关系算子中的直接对应。
- **存储引擎**：Type conversion 与 ABI/layout 转换类似磁盘格式适配；本课转换不承担长期向后兼容和在线迁移。
- **计算引擎**：GPU launch lowering 对应把算子映射为具体执行资源；线程层次和 barrier 是设备特有约束，不能只看算子 DAG。
- **分布式系统**：conversion target 像节点能力集合，只有受支持操作才能落地；它不处理网络部分失败或跨节点协商。
- **可观测性**：逐级 IR、illegal-op diagnostic、PTX/ISA 和 kernel error 可定位 lowering 层；最终崩溃栈不足以证明是哪层破坏语义。

## 知识型学习产出

跟踪多级 IR 到目标代码的转换

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
