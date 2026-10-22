# W42 · 训练完整生命周期：Forward、Backward、Optimizer State、Activation Memory

## 本课目的

围绕 **训练完整生命周期：Forward、Backward、Optimizer State、Activation Memory** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 训练完整生命周期
- Forward
- Backward
- Optimizer State
- Activation Memory
- 预训练
- SFT
- LoRA
- RLHF
- DPO
- GRPO
- 评估
- 模型与训练版本管理

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：对参数量为 P、字节宽度为 bw/bg/bm/bv 的 Adam 训练，推导参数、梯度、一二阶矩与激活的峰值显存；解释反向模式自动微分为何以保存前向中间量换取反向计算。
- **源码与产物**：沿 PyTorch grad_fn、Node、AccumulateGrad 和 AdamW.step 追踪 Forward→Backward→更新路径，并从 autograd graph / saved tensor 指出激活生命周期。
- **性能与实验**：以 tokens/s、step time、峰值显存和 MFU 为指标，只改变 batch/sequence length 或 activation checkpointing，区分算力、带宽与激活容量瓶颈。
- **正确性与故障**：守住 loss/梯度/optimizer state 与 model revision 对齐、评估集隔离等不变量；能用 loss curve、grad norm、NaN/Inf 与 checkpoint metadata 诊断状态错位、爆炸或版本污染。
- **系统设计与评审**：在预训练、SFT、LoRA、RLHF、DPO、GRPO、评估与版本管理的同一生命周期内，评审全参/参数高效更新、在线/离线偏好优化和可复现成本的取舍。

## 与既有经验的连接

- **数据库内核**：Forward/Backward 的依赖图类似执行器的数据依赖，optimizer step 类似状态提交；但梯度更新不是满足 ACID 的事务，浮点次序也可非确定。
- **存储引擎**：参数、梯度和 Adam 矩可类比不同生命周期的页状态；但 Activation Memory 是可重算的瞬时中间量，不是必须持久化的脏页。
- **计算引擎**：autograd graph 类似从算子 DAG 反向生成执行计划；但反向算子由求导规则生成，不等同于普通关系代数逆算子。
- **分布式系统**：一次 step 的阶段边界类似 barrier 前后的状态跃迁；但本课只讨论训练生命周期，不把阶段顺序扩展成共识协议。
- **可观测性**：loss、grad norm、step time 与峰值显存共同描述训练状态；单看 GPU 利用率不能证明梯度或版本正确。

## 知识型学习产出

建立训练显存与 FLOPs 估算模型

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P5：Distributed Training 与 GPU Communication](../README.md)
