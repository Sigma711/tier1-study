# W33 · vLLM V1 架构：Engine、Scheduler、Worker、Model Runner

## 本课目的

围绕 **vLLM V1 架构：Engine、Scheduler、Worker、Model Runner** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- vLLM V1 架构
- Engine
- Scheduler
- Worker
- Model Runner

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：由每轮 token budget、running/waiting 请求与可用 KV blocks 推导 scheduler 可接纳工作量和单步复杂度，解释 Engine 到 Worker 的控制/数据边界。
- **源码与产物**：定位 vLLM V1 EngineCore、Scheduler、Worker 与 GPUModelRunner 的请求状态、调度输出和执行调用链，能把日志事件映射回对象。
- **性能与实验**：固定模型与请求流，对照 scheduler 配额、worker 数与 eager/graph 路径，测 queue time、step time、batch tokens、GPU utilization 和 engine overhead。
- **正确性与故障**：验证请求状态迁移、scheduled token 预算、worker/model-runner 输入一致；用 engine trace、scheduler dump、worker error 与请求输出定位卡死或重复调度。
- **系统设计与评审**：评审进程内/多进程 Engine、集中 Scheduler 与 Worker 隔离，在故障隔离、IPC 开销、可扩展性和调试性之间取舍。

## 与既有经验的连接

- **数据库内核**：Engine/Scheduler/Worker 类似 coordinator、调度器和执行器；token 逐步调度不是一次生成完整查询计划。
- **存储引擎**：Scheduler 持有的 block 使用状态类似 buffer manager 元数据；它不提供页持久化或事务锁。
- **计算引擎**：Model Runner 类似设备执行 backend，消费已调度批次；模型状态与 KV 让执行比无状态算子调用更强耦合。
- **分布式系统**：Engine 与 Worker 边界像控制面/数据面；本课 vLLM V1 组件关系不等同跨节点共识和容灾。
- **可观测性**：请求状态、scheduler decision、worker/model-runner step trace 能还原因果；仅看 API latency 无法区分排队和执行。

## 知识型学习产出

用 Agent 研究一次完整请求的调用链

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
