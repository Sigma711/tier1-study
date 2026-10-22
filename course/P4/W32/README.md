# W32 · 推理计算模型：Prefill、Decode、TTFT、TPOT、算力/带宽约束

## 本课目的

围绕 **推理计算模型：Prefill、Decode、TTFT、TPOT、算力/带宽约束** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 推理计算模型
- Prefill
- Decode
- TTFT
- TPOT
- 算力/带宽约束

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：按层计算 attention/MLP FLOPs 与 KV 读写字节，利用 arithmetic intensity 与 roofline 判断 Prefill/Decode 的算力或带宽瓶颈，并分解 `TTFT≈queue+prefill`、`TPOT≈decode step`。
- **源码与产物**：在 vLLM/TensorRT-LLM 的执行 trace 中辨认 prefill 与 decode batch、GEMM/GEMV、KV-cache 读写及 TTFT/TPOT 指标定义。
- **性能与实验**：固定模型、精度和硬件，扫描 input/output length 与 batch size，对照理论 FLOPs/bytes、实际 token/s、TTFT、TPOT 和带宽利用率。
- **正确性与故障**：识别计时边界混乱、异步 CUDA 未同步、预热不足和 KV 容量估算错误；用请求时间线、GPU trace 与显存水位交叉验证。
- **系统设计与评审**：为交互式与离线工作负载选择 batch、并发和容量余量，明确 TTFT、TPOT、吞吐、显存与成本之间不可同时最优的边界。

## 与既有经验的连接

- **数据库内核**：Prefill/Decode 像构建阶段与迭代执行阶段，可分别建模成本；自回归 token 依赖不同于一次性查询流水线。
- **存储引擎**：KV 读写字节可类比 buffer-pool 流量；KV 是请求运行态，既非持久页也没有 WAL/事务语义。
- **计算引擎**：roofline 与算子算术强度同构，可判断计算/带宽瓶颈；Decode 的小批量串行依赖限制了普通批执行类比。
- **分布式系统**：队列等待与服务时间分解类似排队服务；本课模型是单实例资源约束，不含跨节点通信和故障域。
- **可观测性**：TTFT、TPOT、token/s、GPU 带宽和显存水位必须同一请求关联；平均值会掩盖长度分布与尾延迟。

## 知识型学习产出

构建模型推理性能估算器

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P4：LLM Inference Runtime 与 Serving Systems](../README.md)
