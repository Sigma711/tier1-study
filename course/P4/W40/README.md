# W40 · Serving Benchmark、Goodput、SLO、Tail Latency、负载模型

## 本课目的

围绕 **Serving Benchmark、Goodput、SLO、Tail Latency、负载模型** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Serving Benchmark
- Goodput
- SLO
- Tail Latency
- 负载模型

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：定义 goodput 为满足 TTFT/TPOT/E2E SLO 的完成请求或 token 率，利用分位数与 Little 定律解释到达率接近容量时尾延迟为何非线性上升。
- **源码与产物**：定位 vLLM benchmark serving 的请求生成、timestamp/latency 统计和输出字段，对照 MLPerf Server scenario 的 loadgen、latency constraint 与有效样本规则。
- **性能与实验**：固定模型/硬件/数据集，使用相同 input/output length、到达过程和 SLO，对照并发/泊松/trace-driven 负载，报告 p50/p95/p99、goodput、吞吐和拒绝率。
- **正确性与故障**：识别 coordinated omission、客户端瓶颈、预热混入、输出长度截断和失败请求被剔除；保存原始时间戳、请求状态与负载发生器利用率审计。
- **系统设计与评审**：评审开放/封闭负载、合成/生产 trace、token/request goodput 与多维 SLO，在可复现性、代表性、成本和容量风险间取舍。

## 与既有经验的连接

- **数据库内核**：Serving benchmark 与数据库 workload replay/压测方法相通；token 长度和逐步生成让单请求成本方差更大。
- **存储引擎**：负载分布与 cache 热度会改变结果；本课 benchmark 不证明持久性、恢复或数据正确性。
- **计算引擎**：吞吐/延迟曲线与执行引擎容量测试相同；LLM 还需同时约束 TTFT、TPOT 和变长输出。
- **分布式系统**：Goodput/SLO/尾延迟与过载控制直接同构；单轮 benchmark 不能推出故障下可用性。
- **可观测性**：必须保存请求级 timestamp、长度、状态和系统资源 trace；聚合 QPS 会隐藏 coordinated omission 与失败剔除。

## 知识型学习产出

构建真实请求分布下的压力测试

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
