# W37 · 模型量化：INT8、INT4、FP8、低比特格式、量化误差与 Kernel

## 本课目的

围绕 **模型量化：INT8、INT4、FP8、低比特格式、量化误差与 Kernel** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 模型量化
- INT8
- INT4
- FP8
- 低比特格式
- 量化误差与 Kernel

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：写出对称/非对称量化 `q=clip(round(x/s)+z)` 与反量化误差界，计算 INT8/INT4/FP8 权重容量、group-scale 开销与理论带宽节省。
- **源码与产物**：定位 vLLM quantization config/linear method 与 CUTLASS/Marlin 等低比特 kernel 接口，辨认权重、scale、zero-point、accumulator dtype 和硬件能力约束。
- **性能与实验**：固定模型、校准集、GPU 与请求分布，对照 BF16、INT8、INT4、FP8，报告模型大小、加载时间、TTFT/TPOT、吞吐及任务质量/误差。
- **正确性与故障**：识别 outlier、scale granularity 错配、溢出、unsupported kernel fallback 和 checkpoint metadata 不一致；用层级误差、kernel trace 与质量集诊断。
- **系统设计与评审**：评审 weight-only、weight-activation、per-channel/group 以及 FP8，在质量、校准成本、显存、硬件覆盖和 kernel 可用性间取舍。

## 与既有经验的连接

- **数据库内核**：量化像近似执行以资源换精度；数据库整数编码通常要求可逆或精确，不能照搬容许模型误差的前提。
- **存储引擎**：低比特 packing 与压缩编码都降容量/带宽；量化带数值误差，且 scale 元数据不同于无损页编码。
- **计算引擎**：量化 kernel 类似编码感知向量化算子；若硬件不支持会反量化或回退，容量节省不保证加速。
- **分布式系统**：各 worker 必须加载一致格式与 scale，可类比制品一致性；本课不讨论副本共识或容错。
- **可观测性**：层级误差、任务质量、实际 kernel、带宽和 latency 必须同时看；只看 dtype 名称会漏掉回退与混合精度。

## 知识型学习产出

对比不同量化方案的内存和延迟

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
