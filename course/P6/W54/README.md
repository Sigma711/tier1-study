# W54 · Kueue、Ray、Slurm、配额、公平调度、Gang Scheduling、多租户安全

## 本课目的

围绕 **Kueue、Ray、Slurm、配额、公平调度、Gang Scheduling、多租户安全** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Kueue
- Ray
- Slurm
- 配额
- 公平调度
- Gang Scheduling
- 多租户安全

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：用 dominant share/配额和等待时间定义公平性，推导 gang 最小资源门槛及 head-of-line blocking 对集群利用率的影响。
- **源码与产物**：分别定位 Kueue ClusterQueue/AdmissionCheck、Ray placement group、Slurm multifactor/backfill 与 Kubernetes PodGroup/安全边界对象。
- **性能与实验**：以 queue wait、admission latency、GPU utilization、preemption 和 fairness deviation 为指标，对照配额、优先级、gang size 与 backfill。
- **正确性与故障**：守住 gang 全有或全无 admission、租户配额与身份隔离；用队列 condition、Ray/Slurm scheduler reason、审计日志诊断饥饿和越权。
- **系统设计与评审**：比较 Kueue、Ray、Slurm 的控制边界，权衡公平、利用率、抢占、gang 原子性与多租户最小权限。

## 与既有经验的连接

- **数据库内核**：admission 与资源组/并发控制相似；但 GPU gang 作业不能像短查询一样逐 task 渐进启动。
- **存储引擎**：队列持久状态像调度元数据；但它不保证训练 checkpoint 或数据本身的安全隔离。
- **计算引擎**：Ray placement group/Slurm allocation 像执行 slot 集；但 Kueue 主要决定准入，不替代作业内 task 调度。
- **分布式系统**：Gang Scheduling 像原子资源获取；但不是业务状态的分布式事务，已运行作业的容错另算。
- **可观测性**：queue reason、fairness、preemption 与 GPU idle 要联看；高利用率可能掩盖某租户长期饥饿或越权。

## 知识型学习产出

设计 AI 集群作业准入与调度策略

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P6：AI Data、GPU Cluster 与生产级基础设施](../README.md)
