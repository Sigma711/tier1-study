# W21 · CFG、SSA、Dominance、Dataflow、Liveness、Alias Analysis

## 本课目的

围绕 **CFG、SSA、Dominance、Dataflow、Liveness、Alias Analysis** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- CFG
- SSA
- Dominance
- Dataflow
- Liveness
- Alias Analysis

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：对含 `V` 个基本块、`E` 条边的 CFG 推导迭代数据流分析上界，手算 dominator、dominance frontier、φ 节点与活跃区间，并说明格高度如何决定收敛轮数。
- **源码与产物**：在 LLVM IR 中定位 `BasicBlock`、`PHINode`、`DominatorTree`、`LiveVariables` 与 `AAResults`，从一段分支循环 IR 读出 def-use 和 may/must-alias 结论。
- **性能与实验**：比较稠密 bit-vector 与稀疏 SSA 数据流实现的分析时间/峰值内存；固定 CFG，仅改变块数、边密度和变量数观察收敛轮次。
- **正确性与故障**：验证“定义支配所有使用”、φ 输入对应前驱、liveness 方程达到不动点；用 verifier、CFG 图和 alias-analysis 输出诊断错误变换或漏加 φ。
- **系统设计与评审**：在精确但昂贵的上下文/流敏感 alias analysis 与保守快速分析之间取舍，并解释分析失效如何限制后续优化而非冒险改语义。

## 与既有经验的连接

- **数据库内核**：CFG 数据流像查询计划上的属性传播，dominance 像“所有路径必经”；SQL 计划通常是算子 DAG，φ 与可变程序状态没有直接对应物。
- **存储引擎**：liveness 与 buffer pin/unpin 都回答资源何时仍被引用；活跃变量是静态近似，不处理持久页脏写、锁存和恢复次序。
- **计算引擎**：SSA def-use 链类似列式表达式 DAG，便于局部优化；控制流合流和 alias 会破坏纯数据流 DAG 的简单性。
- **分布式系统**：may-analysis 的保守性类似故障检测中的不确定性传播；编译分析面对封闭 CFG，不具备消息乱序与节点失联的不确定来源。
- **可观测性**：CFG、dom tree、活跃集合和 AA 查询结果是优化决策证据；它们是静态事实，不能证明热点路径实际被频繁执行。

## 知识型学习产出

分析 LLVM IR 的数据流关系

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
