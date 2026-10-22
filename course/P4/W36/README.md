# W36 · Paged Attention、FlashInfer、推理 Kernel、GQA

## 本课目的

围绕 **Paged Attention、FlashInfer、推理 Kernel、GQA** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Paged Attention
- FlashInfer
- 推理 Kernel
- GQA

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：推导 MHA/GQA 的 KV head 数对容量和每步读带宽的比例，计算 paged attention 的 block indirection 开销与 kernel 算术强度。
- **源码与产物**：定位 FlashInfer paged KV APIs、decode/prefill attention kernels、plan/run 接口和 GQA head mapping，并对照 vLLM attention backend 调用约定。
- **性能与实验**：固定模型、序列长度、batch、dtype 与 GPU，对照 contiguous/paged、不同 page size、MHA/GQA，报告 kernel latency、GB/s、occupancy 和数值误差。
- **正确性与故障**：识别 page table 越界、head-group 映射错误、ragged length 错配及 softmax 数值失稳；用 CUDA error、kernel trace 和参考实现差分定位。
- **系统设计与评审**：评审统一 kernel 与按 Prefill/Decode/GQA 特化 kernel，在编译/调度开销、代码复杂度、page size 与带宽利用率间取舍。

## 与既有经验的连接

- **数据库内核**：Paged attention 的间接寻址像通过页表/行标识访问数据；其 softmax 归约和 head 语义没有数据库算子直接对应。
- **存储引擎**：page table 与 buffer page mapping 相似；KV page 是 GPU 运行态且无持久页校验、写回与恢复。
- **计算引擎**：FlashInfer plan/run 类似准备物理算子后批执行；kernel 需要 warp、shared memory 和数值归约级别判断。
- **分布式系统**：GQA head 分组只是张量内共享，不等同副本组或一致性组；本课不覆盖跨 GPU 通信。
- **可观测性**：kernel latency、HBM GB/s、occupancy、page metadata 与误差对照构成证据；端到端 TPOT 还包含调度和其他层。

## 知识型学习产出

分析 Attention Backend 的性能

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
