# W60 · Runtime：Scheduler、Paged KV Cache、Admission Control

## 本课目的

围绕 **Runtime：Scheduler、Paged KV Cache、Admission Control** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Runtime
- Scheduler
- Paged KV Cache
- Admission Control

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：由 block size、层数、heads、head dimension 和 dtype 推导每 token KV bytes、block 碎片与最大并发，并用排队模型解释 admission。
- **源码与产物**：定位 vLLM Scheduler、KVCacheManager/BlockPool、请求状态和 worker 执行路径，说明 continuous batching 的状态跃迁。
- **性能与实验**：以 TTFT、TPOT、goodput、queue time、KV utilization 和 preemption 为指标，对照并发、block size 与 admission 阈值。
- **正确性与故障**：守住请求到 KV block 的所有权、refcount 和释放顺序；用 scheduler event、block table 与 OOM/preemption 日志诊断泄漏或串请求。
- **系统设计与评审**：在吞吐、尾延迟、碎片、抢占和过载保护间选择调度与准入策略。

## 与既有经验的连接

- **数据库内核**：Scheduler/admission 类似查询调度与并发控制；但 autoregressive 请求每轮只推进 token，服务时间更不确定。
- **存储引擎**：Paged KV 像页式 buffer pool；但 KV 是请求/模型绑定的瞬时状态，不能跨版本任意复用。
- **计算引擎**：continuous batching 像动态批执行；但每个序列的完成时刻和 shape 持续变化。
- **分布式系统**：过载保护类似入口背压；但单机 admission 不提供跨副本公平或故障转移。
- **可观测性**：queue、KV occupancy、preemption 与 TTFT/TPOT 必须关联；吞吐上升可能以尾延迟失控为代价。

## 知识型学习产出

推理 Runtime 核心实现

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P7：综合毕业项目与高级工程师面试](../README.md)
