# W08 · LLM 架构：Embedding、MLP、Normalization、Dense/MoE、Tokenization

## 本课目的

围绕 **LLM 架构：Embedding、MLP、Normalization、Dense/MoE、Tokenization** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- LLM 架构
- Embedding
- MLP
- Normalization
- Dense/MoE
- Tokenization

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能计算词表 Embedding 参数量、门控 MLP FLOPs、Normalization 统计量，并比较 Dense 与 top-k MoE 的总参数和每 token 激活参数。
- **源码与产物**：能定位 tokenizer model/vocab、Embedding lookup、RMSNorm/LayerNorm、SwiGLU/MLP、router logits 与 expert dispatch 的具体模块和张量。
- **性能与实验**：能固定 tokens、hidden size、dtype 比较 Embedding/MLP/Norm 与 Dense/MoE 的耗时、参数字节、激活稀疏度和路由负载。
- **正确性与故障**：能诊断 tokenizer/词表不匹配、padding id、norm epsilon、MLP shape、MoE expert imbalance 与 dropped tokens，并指出证据位置。
- **系统设计与评审**：能按质量、参数容量、每 token 成本、路由复杂度选择 Dense 或 MoE，并说明 tokenizer 变更为何属于模型契约变更。

## 与既有经验的连接

- **数据库内核**：token id 到 embedding 像字典编码查表，MoE router 像数据依赖分派；失效于 learned routing 不是确定性优化规则。
- **存储引擎**：词表与权重 layout 像格式契约和列布局；失效于权重兼容性不提供事务演进保证。
- **计算引擎**：Dense/MLP 是规则算子流，MoE 是稀疏条件执行；失效于专家负载由模型输出决定，不等于静态分区。
- **分布式系统**：专家负载均衡可借鉴分片热点分析；失效于本课不涉及跨节点专家通信。
- **可观测性**：router 分布、expert load、norm 统计和 token 长度能形成分层信号；失效于均衡指标好不代表模型质量好。

## 知识型学习产出

用 Agent 实现并验证一个小型 Transformer

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P1：AI 计算基础与现代模型架构](../README.md)
