# W39 · 多 GPU 推理：TP、PP、EP、P/D 分离、KV 传输与路由

## 本课目的

围绕 **多 GPU 推理：TP、PP、EP、P/D 分离、KV 传输与路由** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 多 GPU 推理
- TP
- PP
- EP
- P/D 分离
- KV 传输与路由

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：推导 TP all-reduce/all-gather、PP bubble、EP all-to-all 与 KV transfer 字节量，建立 `T=max(compute,communication)+queue` 的瓶颈模型。
- **源码与产物**：定位 vLLM distributed parallel state/executor、pipeline stage、MoE expert placement，以及 DistServe/llm-d/NIXL 的 Prefill/Decode 路由和 KV connector 接口。
- **性能与实验**：固定模型、GPU/互连与请求分布，对照 TP/PP/EP 度数、共置/P-D 分离，记录通信 GB/s、bubble、TTFT/TPOT、KV transfer time 与 goodput。
- **正确性与故障**：验证 rank/world-size、collective 次序、stage tensor shape、expert ownership 和 KV 请求身份一致；用 NCCL trace、rank log、router/KV transfer trace 诊断 hang 或错配。
- **系统设计与评审**：评审并行维度组合与 P/D 分离拓扑，在显存、通信、故障域、扩缩容、路由局部性和 SLO 之间取舍。

## 与既有经验的连接

- **数据库内核**：TP/PP/EP 可类比分区执行与 exchange；张量 collective 和逐层同步比数据库 shuffle 更严格频繁。
- **存储引擎**：KV transfer 像远程页搬运；KV 可重算且按请求身份绑定，不具备持久副本一致性。
- **计算引擎**：PP stage 与流水执行、EP 与条件分区相似；同步 collective 会决定关键路径，不能只看算子局部成本。
- **分布式系统**：路由、负载均衡、背压和故障域类比直接成立；但模型参数/KV 一致性是本系统特有正确性条件。
- **可观测性**：rank/span 关联、collective time、link throughput、KV transfer 与请求 SLO 必须贯通；单卡利用率无法定位跨卡等待。

## 知识型学习产出

设计分布式推理执行方案

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
