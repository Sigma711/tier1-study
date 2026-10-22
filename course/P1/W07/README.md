# W07 · Transformer、Self-Attention、Multi-Head Attention、RoPE、GQA/MQA

## 本课目的

围绕 **Transformer、Self-Attention、Multi-Head Attention、RoPE、GQA/MQA** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Transformer
- Self-Attention
- Multi-Head Attention
- RoPE
- GQA/MQA

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能推导 \(Attention(Q,K,V)=softmax(QK^T/\sqrt{d})V\) 的 \(O(L^2d)\) 计算/中间矩阵，并计算 MHA、GQA、MQA 的 KV 头数与容量差异；解释 RoPE 旋转。
- **源码与产物**：能定位 Hugging Face/PyTorch 中 q/k/v projection、head reshape、RoPE 频率与 GQA repeat_kv，核对 tensor shape。
- **性能与实验**：能固定 batch、长度、head_dim、dtype，对比 MHA/GQA/MQA 的 FLOPs、KV 字节、吞吐和误差。
- **正确性与故障**：能诊断 mask 方向、缩放因子、RoPE position、head 分组和 shape 错误，并用 attention 输出或中间张量证据定位。
- **系统设计与评审**：能说明质量、KV 容量、带宽与实现复杂度如何决定 MHA/GQA/MQA 选择，不提前讨论服务调度。

## 与既有经验的连接

- **数据库内核**：attention score 像按 key 计算关联权重，成立于配对计算；失效于 softmax 加权不是等值连接或关系语义。
- **存储引擎**：K/V 的按头布局像列式布局影响扫描带宽；失效于本课只讨论模型张量，不引入后续 KV cache 管理。
- **计算引擎**：多头拆分像分区并行后合并，成立于独立子计算；失效于 head 具有学习语义而非任意数据分区。
- **分布式系统**：GQA 的共享 K/V 类似共享状态减少复制量；失效于这里没有副本一致性协议。
- **可观测性**：按长度、头数分解耗时和内存可解释瓶颈；失效于 attention 热图不能证明模型推理因果。

## 知识型学习产出

从公式到张量运算完整解释 Attention

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P1：AI 计算基础与现代模型架构](../README.md)
