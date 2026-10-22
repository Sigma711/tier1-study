# W22 · LLVM：IR、Optimization Pass、CodeGen、JIT/AOT

## 本课目的

围绕 **LLVM：IR、Optimization Pass、CodeGen、JIT/AOT** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- LLVM
- IR
- Optimization Pass
- CodeGen
- JIT/AOT

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：以 `T_total=T_front+T_opt+T_codegen+N·T_run` 推导 JIT 相对 AOT 的盈亏平衡调用次数，并说明 LLVM SSA IR 到 machine instruction 的信息逐步具体化。
- **源码与产物**：定位 LLVM `Module`/`Function`/`Instruction`、new pass manager、SelectionDAG/GlobalISel 与 ORC JIT，能读 `.ll`、bitcode、object 和反汇编的对应关系。
- **性能与实验**：固定源程序和目标 CPU，对照 `-O0/-O2`、JIT/AOT，分别记录 compile latency、code size、启动时间与 steady-state cycles，禁止只报总耗时。
- **正确性与故障**：解释 poison/undef、data layout、calling convention 与 target feature 不匹配造成的错编译或崩溃；以 verifier、optimization remarks 和反汇编为诊断证据。
- **系统设计与评审**：评审服务内 ORC JIT、离线 AOT 或混合缓存方案，在冷启动、峰值性能、部署可移植性、代码缓存和攻击面之间作取舍。

## 与既有经验的连接

- **数据库内核**：LLVM pass pipeline 类似查询优化流水线，二者都依赖分析与变换；LLVM 的等价性受语言/IR 未定义行为约束，不是关系代数等价。
- **存储引擎**：bitcode/object/code cache 类似不同层次的物化表示；它们没有事务 durability，缓存键错误会执行错误代码而非返回旧页。
- **计算引擎**：JIT CodeGen 对应表达式编译和向量化执行生成本地代码；LLVM 指令合法化与寄存器分配比算子调度更贴近硬件。
- **分布式系统**：AOT 制品的 target triple/features 类似部署兼容契约；单个 object 的 ABI 兼容不保证集群节点版本与状态一致。
- **可观测性**：pass timing、optimization remarks、IR diff 与 perf counters 可串起优化因果；仅看最终 QPS 无法区分 JIT 冷启动和代码质量。

## 知识型学习产出

用 LLVM Kaleidoscope 研究基础编译流程

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P3：编译器原理与 AI Compiler 内核](../README.md)
