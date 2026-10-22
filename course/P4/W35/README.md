# W35 · Paged KV Cache、Block Allocator、Prefix Caching、引用计数与淘汰

## 本课目的

围绕 **Paged KV Cache、Block Allocator、Prefix Caching、引用计数与淘汰** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Paged KV Cache
- Block Allocator
- Prefix Caching
- 引用计数与淘汰

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：计算每 token KV 字节 `2·L·H_kv·D·bytes`、block 内部碎片和可容纳 token 数；推导共享前缀引用计数与 copy-on-write 条件。
- **源码与产物**：定位 vLLM KVCacheManager、BlockPool/Block、free queue、hash-based prefix lookup、ref count 与 eviction 路径，读出 block table。
- **性能与实验**：固定模型/精度/显存，对照 block size、prefix 重用率和淘汰策略，测 KV utilization、hit rate、碎片、recompute tokens 与吞吐。
- **正确性与故障**：验证 block 唯一所有权/共享引用、hash 包含完整前缀语义、释放后不可再引用；用 block table、ref-count log 和 checksum/输出差分诊断污染。
- **系统设计与评审**：评审 block 大小、hash 粒度、LRU 类淘汰与 copy-on-write，在元数据开销、碎片、命中率、隔离与回收延迟间取舍。

## 与既有经验的连接

- **数据库内核**：Prefix cache lookup 像 plan/result cache 命中；生成状态依赖完整 token/模型上下文，不能按 SQL 文本式弱键复用。
- **存储引擎**：Paged KV、free list、ref count 和 eviction 与 buffer pool 最接近；KV 可重算且没有脏页落盘、WAL 或崩溃恢复。
- **计算引擎**：block table 提供逻辑 token 到物理 KV 的间接寻址；它改变 attention kernel 访存，不只是内存分配器。
- **分布式系统**：共享前缀引用类似副本共享不可变对象；本课不保证跨节点 block 一致性与远程恢复。
- **可观测性**：命中率、碎片、free blocks、引用计数与重算量是核心证据；高显存占用本身不能区分有效缓存和泄漏。

## 知识型学习产出

实现 KV Cache Manager

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
