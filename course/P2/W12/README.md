# W12 · CUDA 编程模型、Kernel Launch、Stream、Event、异步执行

## 本课目的

围绕 **CUDA 编程模型、Kernel Launch、Stream、Event、异步执行** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- CUDA 编程模型
- Kernel Launch
- Stream
- Event
- 异步执行

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能画出 host、stream、kernel、memcpy、event 的 happens-before，计算 launch 开销占比与 copy/compute 理想重叠后的关键路径。
- **源码与产物**：能读 `<<<grid,block,shared,stream>>>`、runtime API、event record/wait 和默认流语义，并在时间线上对应具体 launch。
- **性能与实验**：能固定数据与 Kernel，对比同步、单流、多流和 pinned memory，以 CPU enqueue、GPU duration、overlap ratio 与端到端时间评估。
- **正确性与故障**：能诊断缺失同步、错误流依赖、pageable copy 隐式同步、异步错误延迟报告和对象提前释放，用 event/timeline/sanitizer 举证。
- **系统设计与评审**：能为依赖 DAG 选择 stream/event 边界，在并发收益、内存占用、调试难度和确定性之间取舍。

## 与既有经验的连接

- **数据库内核**：stream 内顺序像执行管线顺序，成立于依赖；失效于 CUDA 默认流与异步错误语义不同于事务顺序。
- **存储引擎**：host-device copy 像层级间搬运，成立于批量与带宽权衡；失效于 pinned memory 不是持久化缓存。
- **计算引擎**：多流与 event 像 DAG 异步调度；失效于实际并发受 GPU engine 与资源占用限制。
- **分布式系统**：event wait 可类比消息依赖和 happens-before；失效于设备内事件不提供容错或一致性。
- **可观测性**：CPU/GPU 时间线能揭示 enqueue、copy、compute 空洞；失效于 event elapsed time 不是完整端到端延迟。

## 知识型学习产出

实现多组 CUDA Kernel 和微基准

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
