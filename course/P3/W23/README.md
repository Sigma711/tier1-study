# W23 · MLIR：Operation、Region、Block、Dialect、Type、Attribute、ODS

## 本课目的

围绕 **MLIR：Operation、Region、Block、Dialect、Type、Attribute、ODS** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- MLIR
- Operation
- Region
- Block
- Dialect
- Type
- Attribute
- ODS

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：用 `Operation -> Region -> Block -> Operation` 的递归结构推导遍历复杂度 `O(#ops+#blocks)`，解释 SSA value、Type 与 Attribute 如何把验证条件前移。
- **源码与产物**：定位 MLIR `Operation`、`Region`、`Block`、`Dialect`、`Type`、`Attribute` C++ 对象及 TableGen ODS 生成的 op class/parser/verifier。
- **性能与实验**：固定同一 IR，比较通用属性查询与 ODS 生成访问器的解析/验证耗时和内存；控制 operation 数、属性数量与 region 深度。
- **正确性与故障**：以 region 隔离、block 参数、operand/result type 约束和未注册 dialect 为不变量；用 parser diagnostic 与 `verify()` 定位结构或语义非法 IR。
- **系统设计与评审**：评审新 dialect 应复用标准 Type/Attribute 还是自定义语义，以及 single/multi-region op 对可分析性、扩展性和 canonical form 的影响。

## 与既有经验的连接

- **数据库内核**：Dialect 像可扩展计划节点族，Type/Attribute 像 schema 与 plan property；MLIR 允许嵌套 region/SSA 控制流，远超关系算子树。
- **存储引擎**：ODS 的声明式 schema 类似页格式/元数据 schema 的集中定义；MLIR 文本/字节码并不自动承担长期格式兼容与崩溃恢复。
- **计算引擎**：Operation/Value 图与算子 DAG 可直接类比，Region/Block 支持结构化控制；执行引擎节点通常已有运行语义，而 MLIR op 可停留在抽象层。
- **分布式系统**：Dialect registration 和接口像插件协议；同进程 context 中注册成功不等于跨节点协议协商与滚动升级安全。
- **可观测性**：可打印 IR、op location 与 verifier diagnostic 提供结构化证据；location 可能被变换丢失，不能天然等同端到端 trace context。

## 知识型学习产出

实现一个基础 Tensor Dialect

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
