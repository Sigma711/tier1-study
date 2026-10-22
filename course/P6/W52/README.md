# W52 · CPU/GPU/NVMe 多级缓存、KV Offloading、模型加载、权重分发、GPUDirect

## 本课目的

围绕 **CPU/GPU/NVMe 多级缓存、KV Offloading、模型加载、权重分发、GPUDirect** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- CPU/GPU/NVMe 多级缓存
- KV Offloading
- 模型加载
- 权重分发
- GPUDirect

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：以工作集 W、各层容量 Ci/带宽 Bi/延迟 Li 推导命中率下的有效访问时间，并估算 KV Offloading 与权重加载能否被计算重叠。
- **源码与产物**：定位 vLLM KV offload connector、NIXL transfer descriptor/backend 与 CUDA GPUDirect 数据路径，区分 KV 块、模型权重和传输控制面。
- **性能与实验**：以 TTFT、TPOT、cache hit、eviction、load time 和 H2D/NVMe throughput 为指标，对照层级容量、传输块和并发。
- **正确性与故障**：守住 block/revision/tenant identity 与传输完成顺序；用 checksum、cache metadata、CUDA error 和 I/O counter 诊断陈旧 KV、半载权重或路径回退。
- **系统设计与评审**：在 GPU 容量、CPU/NVMe 带宽、GPUDirect 支持矩阵和冷启动目标间选择层级与分发路径。

## 与既有经验的连接

- **数据库内核**：KV block cache 像 buffer pool；但其 key 含请求前缀和模型版本，不能按普通页号复用。
- **存储引擎**：NVMe 层与预取/淘汰类比成立；但模型权重只读、KV 短生命周期，写回语义不同。
- **计算引擎**：传输与算子重叠像 I/O pipeline；但 GPU stream/event 依赖决定数据何时可消费，不能只看队列有数据。
- **分布式系统**：权重分发像大对象广播；但版本原子切换和失败回退需另行定义，GPUDirect 只优化数据面。
- **可观测性**：命中/淘汰、各层带宽与 TTFT/TPOT 要同时间线；缓存命中率高仍可能被慢传输尾部拖垮。

## 知识型学习产出

设计分层模型与 KV Cache 存储

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P6：AI Data、GPU Cluster 与生产级基础设施](../README.md)
