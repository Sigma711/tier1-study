# W16 · Operator Fusion：Softmax、LayerNorm、RMSNorm、内存流量优化

## 本课目的

围绕 **Operator Fusion：Softmax、LayerNorm、RMSNorm、内存流量优化** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Operator Fusion
- Softmax
- LayerNorm
- RMSNorm
- 内存流量优化

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能推导稳定 softmax、LayerNorm 均值/方差、RMSNorm 均方根，并计算未融合与融合实现的 HBM 读写次数和理论节省。
- **源码与产物**：能读 Triton fused softmax 与主流 fused norm Kernel 的 reduction、mask、epsilon、affine 参数和中间值驻留方式。
- **性能与实验**：能固定行数、hidden size、dtype，对比 unfused/fused latency、DRAM bytes、GB/s、launch 数和数值误差。
- **正确性与故障**：能诊断 softmax 溢出、reduction 顺序误差、epsilon/轴错误、RMSNorm 与 LayerNorm 语义混淆及寄存器压力退化。
- **系统设计与评审**：能判断融合收益是否覆盖编译、寄存器和 shape 专化成本，并选择库实现或自定义 Kernel。

## 与既有经验的连接

- **数据库内核**：operator fusion 像 pipeline fusion，成立于消除物化；失效于 norm/softmax 的数值 reduction 约束更强。
- **存储引擎**：减少 HBM round trip 像减少中间页读写；失效于 HBM 中间张量不是持久数据。
- **计算引擎**：融合改变算子边界和中间表示，成立于端到端代价；失效于过度融合会因寄存器压力反向退化。
- **分布式系统**：本课融合局限单设备数据路径；不能由此推出跨设备通信融合收益。
- **可观测性**：launch 数、DRAM bytes、寄存器和误差共同验证融合；失效于只看 Kernel 时间会忽略编译与端到端开销。

## 知识型学习产出

对比独立算子与融合算子的性能

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P2：GPU Architecture、CUDA 与高性能 Kernel](../README.md)
