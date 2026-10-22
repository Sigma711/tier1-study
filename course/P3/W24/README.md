# W24 · Canonicalization、Pattern Rewrite、CSE、DCE、Pass Manager

## 本课目的

围绕 **Canonicalization、Pattern Rewrite、CSE、DCE、Pass Manager** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Canonicalization
- Pattern Rewrite
- CSE
- DCE
- Pass Manager

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：给定 `P` 个 pattern、`N` 个 op，分析 greedy rewrite 的匹配成本与不收敛风险；说明 CSE 的哈希等价条件和 DCE 的 use-count 不变量。
- **源码与产物**：定位 MLIR `RewritePattern`、`PatternRewriter`、canonicalizer、CSE/DCE pass 和 `PassManager`，从 before/after IR 解释每次替换。
- **性能与实验**：固定输入 IR，对照 pass 顺序、pattern benefit 与是否启用 canonicalization，测量 op 数、迭代次数、pass time 和最终运行时间。
- **正确性与故障**：识别 rewrite 循环、错误 side-effect 标注导致 DCE、错误等价键导致 CSE；用 IR verifier、`-mlir-print-ir-after-all` 和 pass statistics 取证。
- **系统设计与评审**：评审单一巨型 pass 与小 pass pipeline，在分析缓存、可测试性、编译时间、跨 pass canonicalization 和失败隔离之间取舍。

## 与既有经验的连接

- **数据库内核**：Pattern Rewrite/CSE/DCE 对应规则优化、公共子表达式消除与无用列裁剪；有副作用 op 的可删除性不能由关系代数纯函数假设决定。
- **存储引擎**：canonical form 类似统一 key 编码，减少等价表示；它不提供磁盘格式稳定性，改 canonicalizer 可改变缓存与产物。
- **计算引擎**：PassManager 类似物理优化 pipeline 编排；编译 pass 的 analysis invalidation 比静态算子链更严格。
- **分布式系统**：pass 顺序依赖类似服务变更编排的前置条件；这里失败通常是确定性 IR 变换，不包含部分失败和重试语义。
- **可观测性**：before/after IR、pattern 命中数与 pass timing 能归因代码变化；只比较最终 IR 会遗漏震荡和中间非法状态。

## 知识型学习产出

编写并测试 MLIR Rewrite Pass

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
