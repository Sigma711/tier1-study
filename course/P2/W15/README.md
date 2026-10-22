# W15 · Triton 编程模型、Block、Layout、Warp 映射

## 本课目的

围绕 **Triton 编程模型、Block、Layout、Warp 映射** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Triton 编程模型
- Block
- Layout
- Warp 映射

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能把 Triton program instance/block 映射到输出 tile，推导 grid、mask、num_warps 与 layout 对并行度和访存的影响。
- **源码与产物**：能读 `tl.program_id`、block pointer、layout encoding 以及 TTIR/TTGIR/LLVM IR 到 PTX 的 lowering 产物。
- **性能与实验**：能固定 shape/dtype，以参考实现对比 latency、GB/s/TFLOP/s，并控制 BLOCK_SIZE、num_warps 与布局变量。
- **正确性与故障**：能诊断边界 mask、指针算术、layout 转换、编译 specialization 和 warp 映射问题，用 IR、参考输出与 sanitizer 证据。
- **系统设计与评审**：能在 Triton 生产力、编译器可控性、shape 泛化和手写 CUDA 极限性能间作出选择。

## 与既有经验的连接

- **数据库内核**：Triton block 抽象像向量化批处理，成立于整块表达；失效于编译器负责 GPU warp/layout 映射。
- **存储引擎**：block pointer/layout 像逻辑视图到物理地址；失效于其描述易失张量而非持久页。
- **计算引擎**：TTIR lowering 像逐层物理化；失效于这些 IR 专为 Kernel 编译，不是通用查询计划。
- **分布式系统**：program grid 是独立工作单元集合；失效于无消息、重试或容错语义。
- **可观测性**：IR/PTX、编译元数据和 counter 可闭环归因；失效于高层 Triton 源码相似不保证生成代码相同。

## 知识型学习产出

用 Triton 实现 GEMM

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
