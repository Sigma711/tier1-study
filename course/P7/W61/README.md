# W61 · Distributed Runtime：通信、缓存传输、容错

## 本课目的

围绕 **Distributed Runtime：通信、缓存传输、容错** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Distributed Runtime
- 通信
- 缓存传输
- 容错

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：按 tensor/KV payload、带宽、启动延迟和并行度推导通信临界路径，并估算缓存传输收益需超过的重算成本。
- **源码与产物**：定位分布式 runtime 的 rank/worker group、collective/RPC、KV transfer connector 与 failure detector/restart state。
- **性能与实验**：以通信占比、KV transfer throughput、跨节点 TTFT/TPOT、失败检测和恢复时间对照拓扑、块大小与副本策略。
- **正确性与故障**：守住模型 revision、KV identity、传输完成和失败世代 fencing；用 rank log、checksum、timeout 与恢复 trace 诊断陈旧缓存或脑裂执行。
- **系统设计与评审**：在 tensor/pipeline 分布、KV 迁移/重算、快速失败与状态恢复复杂度之间选择。

## 与既有经验的连接

- **数据库内核**：分布式执行 fragment 类比成立；但 token-by-token 依赖和 KV 状态使重试不能简单幂等。
- **存储引擎**：KV 传输像缓存迁移；但它通常可重算且强绑定请求世代，不是持久副本。
- **计算引擎**：跨 worker 通信像 exchange；但每 token 临界路径让尾延迟比批作业总完成时间更敏感。
- **分布式系统**：failure detector、fencing 和恢复世代可沿用；但 collective communicator 失败不等于自动重配置。
- **可观测性**：通信、缓存传输和恢复 trace 要贯通 request id；节点 Ready 不能证明请求已安全恢复。

## 知识型学习产出

多 GPU 执行与故障实验

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P7：综合毕业项目与高级工程师面试](../README.md)
