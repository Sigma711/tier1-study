# W41 · Mini LLM Inference Engine 综合考核

## 本课目的

围绕 **Mini LLM Inference Engine 综合考核** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Mini LLM Inference Engine 综合考核

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：综合推导模型权重、KV 容量、每 token FLOPs/bytes、队列容量与 `TTFT/TPOT/goodput`，能用统一预算解释瓶颈迁移。
- **源码与产物**：沿 API 请求、Engine/Scheduler、KV allocator、Model Runner 到 attention/quantized kernel 检查源码对象、状态与 trace 对齐。
- **性能与实验**：设计朴素基线、单变量消融和真实长度/到达分布实验，报告冷/热启动、TTFT/TPOT 分位数、goodput、显存、GPU counters 与输出正确性。
- **正确性与故障**：定义请求状态、token 顺序、KV block 所有权、采样/输出、取消与资源回收不变量；用差分结果、请求 trace、allocator audit 和故障注入证据定位问题。
- **系统设计与评审**：在调度、缓存、kernel、量化、并行边界与可观测性间做端到端设计评审，说明容量余量、降级路径和复杂度预算。

## 与既有经验的连接

- **数据库内核**：Mini Engine 可按接入、调度、执行与缓存审查，类似数据库内核分层；自回归状态与概率输出仍须独立证明。
- **存储引擎**：KV allocator/cache 最像 buffer manager；综合考核必须明确它可重建、无 WAL/事务/持久恢复。
- **计算引擎**：Model Runner 与 kernels 构成物理执行层；逐 token 重调度和变长批次不同于固定 DAG 执行。
- **分布式系统**：若设计包含 worker 边界，可讨论背压与故障隔离；不得从单机考核外推分布式一致性。
- **可观测性**：请求 trace、scheduler decision、KV audit、kernel counters 与 SLO 必须同一证据链；“跑通”不是性能或正确性证明。

## 知识型学习产出

展示调度、缓存、并发、Benchmark 与完整复盘

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
