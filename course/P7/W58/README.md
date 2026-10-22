# W58 · Compiler：选择真实算子或执行路径进行优化

## 本课目的

围绕 **Compiler：选择真实算子或执行路径进行优化** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Compiler
- 选择真实算子或执行路径进行优化

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：为选定算子写出 FLOPs、bytes 和算术强度，用 Roofline 上界判断融合、布局或重计算的理论收益。
- **源码与产物**：从 TorchDynamo/FX graph 经 AOTAutograd、Inductor IR 到 Triton/CUDA Kernel，定位真实 lowering 与生成代码。
- **性能与实验**：以 compile time、kernel latency、内存流量和端到端 speedup 对照 eager/原路径，控制 shape、dtype 与缓存。
- **正确性与故障**：守住 graph break 边界、shape/stride/dtype 和数值容差；用 guard、IR dump、generated code 与差分输出诊断误编译。
- **系统设计与评审**：比较专用 pattern、通用 pass 与 runtime dispatch 的收益覆盖面、维护成本和回退路径。

## 与既有经验的连接

- **数据库内核**：compiler pass 像查询重写；但浮点重排可能改变数值，不能仅凭代数等价判定。
- **存储引擎**：layout 变换像物理布局选择；但 tensor layout 主要服务 Kernel 访存而非持久化。
- **计算引擎**：FX/Inductor IR 与逻辑/物理计划类比最强；但动态 shape guards 会把正确性延伸到运行时。
- **分布式系统**：编译缓存 key 类似分布式制品身份；但本周不讨论跨节点运行协议。
- **可观测性**：IR、generated code、kernel trace 和端到端指标要闭环；单 Kernel 加速不保证整图加速。

## 知识型学习产出

编译器优化与正确性测试

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P7：综合毕业项目与高级工程师面试](../README.md)
