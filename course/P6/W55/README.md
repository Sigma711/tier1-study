# W55 · DCGM、NVML、CUPTI、Nsight、OpenTelemetry、端到端 Tracing

## 本课目的

围绕 **DCGM、NVML、CUPTI、Nsight、OpenTelemetry、端到端 Tracing** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- DCGM
- NVML
- CUPTI
- Nsight
- OpenTelemetry
- 端到端 Tracing

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：从采样周期、事件率和 trace payload 推导观测开销与误差，区分 counter、event、sample 与 span 的时间/聚合语义。
- **源码与产物**：分别解释 NVML 设备管理 API、CUPTI Activity/Callback、Nsight Systems/Compute report、DCGM field/entity 与 OpenTelemetry context/span 的数据对象。
- **性能与实验**：以采样开销、时间戳对齐误差、丢事件率和诊断分辨率，对照 NVML polling、CUPTI tracing、Nsight profiling 与 OTel sampling。
- **正确性与故障**：守住 device/process/request identity 和 clock/context 传播；用 DCGM field status、CUPTI dropped records、Nsight timeline 与 trace links 诊断断链。
- **系统设计与评审**：按常驻监控、低层诊断、离线 Profile 和跨服务追踪四种目标组合工具，避免把 NVML、CUPTI、Nsight 当同层替代品。

## 与既有经验的连接

- **数据库内核**：NVML/DCGM 像系统视图，CUPTI 像执行事件 hook；但 GPU counter 不携带查询/请求语义。
- **存储引擎**：trace/profile 落盘类似诊断日志；但高频 CUPTI 数据会反向扰动被测系统，保留策略需受控。
- **计算引擎**：Nsight timeline 像算子执行剖面；但 Kernel 时间必须与 CUDA stream 异步语义一起解释。
- **分布式系统**：OTel context 连接跨服务因果链；它不能自动跨 CUDA/NCCL 补齐设备侧因果。
- **可观测性**：DCGM、NVML、CUPTI、Nsight、OTel 分属不同粒度；同名 utilization 若采样窗口不同不可直接对比。

## 知识型学习产出

关联请求、Kernel、GPU 与系统指标

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P6：AI Data、GPU Cluster 与生产级基础设施](../README.md)
