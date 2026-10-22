# W34 · Continuous Batching、Chunked Prefill、Admission Control、公平调度

## 本课目的

围绕 **Continuous Batching、Chunked Prefill、Admission Control、公平调度** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Continuous Batching
- Chunked Prefill
- Admission Control
- 公平调度

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：用 Little 定律与 token budget 推导并发、排队和在制 token；计算 chunk 大小时 Prefill 完成时间、Decode 干扰与调度轮数的权衡。
- **源码与产物**：定位 vLLM Scheduler 的 waiting/running 队列、scheduled token budget、chunked prefill 分配与 preemption/admission 分支，对照 Sarathi 调度机制。
- **性能与实验**：固定请求长度分布与到达率，对照静态/continuous batch、不同 chunk 与准入策略，报告 TTFT/TPOT、goodput、公平性和拒绝率。
- **正确性与故障**：识别长 Prefill 饥饿 Decode、短请求插队、过载排队爆炸和 preemption 抖动；以 per-request timeline、queue depth 与 scheduler decision 诊断。
- **系统设计与评审**：评审 FCFS、优先级或公平份额调度及准入阈值，在 SLO、利用率、租户隔离、取消成本和实现复杂度间取舍。

## 与既有经验的连接

- **数据库内核**：Continuous batching 类似细粒度查询多路复用与 admission control；每个 decode step 都重新组批，区别于查询一旦运行到结束。
- **存储引擎**：token budget 像有限 buffer/IO credit；它控制计算在制量，不保证持久数据公平或锁公平。
- **计算引擎**：Chunked Prefill 像把长算子切片以减少 pipeline 阻塞；切片还改变 GPU kernel 形状与 KV 增长。
- **分布式系统**：公平调度与背压类比成立；本课队列在单服务实例内，不含跨节点全局公平和网络分区。
- **可观测性**：queue time、chunk size、preemption、per-request TTFT/TPOT 揭示调度效果；平均 token/s 会掩盖饥饿。

## 知识型学习产出

实现一个可配置的推理 Scheduler

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
