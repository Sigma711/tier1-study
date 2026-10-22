# W38 · Speculative Decoding、Sampling、Structured Output、MoE 与多模态推理基础

## 本课目的

围绕 **Speculative Decoding、Sampling、Structured Output、MoE 与多模态推理基础** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Speculative Decoding
- Sampling
- Structured Output
- MoE 与多模态推理基础

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：推导 speculative decoding 在提议长度 `k`、接受率 `α` 下的期望接受 token 与加速条件；写出 temperature/top-k/top-p 重归一化，并估算 MoE 激活参数与多模态 token 增量。
- **源码与产物**：定位 vLLM speculative proposer/scorer、sampling metadata、structured-output grammar/bitmask、MoE router/expert kernel 与多模态 input mapper/processor 的调用边界。
- **性能与实验**：分别固定模型和请求，对照 speculative 开关/`k`、采样参数、grammar 开关、expert 分布、图像 token 数，报告 acceptance、TPOT、质量、约束开销、负载偏斜和显存。
- **正确性与故障**：验证 speculative 输出分布不被改变、采样概率归一、grammar 只允许合法 token、MoE 路由容量/权重一致、多模态 placeholder 对齐；用分布检验、invalid-token、router histogram 和输入映射日志诊断。
- **系统设计与评审**：评审草稿模型/提议长度、随机性、约束解码、专家容量与多模态预处理隔离，在吞吐、质量、确定性、尾延迟和复杂度间取舍。

## 与既有经验的连接

- **数据库内核**：Structured Output grammar 像语法/约束检查，MoE router 像条件执行计划；采样与 speculative 接受拒绝不是确定性 SQL 优化。
- **存储引擎**：多模态特征缓存与可重建派生数据缓存相似；它不具备源媒体的持久性、事务或权限语义。
- **计算引擎**：Speculative proposer/verifier 像乐观执行后校验，MoE 是稀疏条件计算；失败后保持目标分布的数学要求比普通任务回滚更特定。
- **分布式系统**：MoE expert 负载偏斜可类比分片热点；本课只讲推理基础，不提前展开跨 GPU EP 通信与路由。
- **可观测性**：acceptance rate、采样熵、grammar reject、expert histogram、多模态 token 数需分面观测；合并成总吞吐会掩盖机制差异。

## 知识型学习产出

研究吞吐与解码质量的权衡

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
