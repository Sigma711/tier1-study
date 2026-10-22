# W50 · 数据管道、Tokenization、Packing、Arrow/Parquet、Streaming Dataset

## 本课目的

围绕 **数据管道、Tokenization、Packing、Arrow/Parquet、Streaming Dataset** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- 数据管道
- Tokenization
- Packing
- Arrow/Parquet
- Streaming Dataset

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：由原始字节量 D、token 膨胀率 r、平均有效序列长度与 block size 推导 token 数、packing efficiency、padding waste 和稳态输入带宽需求。
- **源码与产物**：定位 Hugging Face Tokenizers normalizer/pre-tokenizer/model，Datasets iterable streaming/Arrow table，以及 packing 的 sample-to-block 映射产物。
- **性能与实验**：以 tokens/s、packing efficiency、data wait、scan bandwidth 为指标，分别对照 tokenizer、packing 策略、Arrow/Parquet row group 与 streaming prefetch。
- **正确性与故障**：守住 tokenizer revision、special-token 边界、sample provenance 与 epoch/shard 不重不漏；用 token histogram、sample id 和 reader metrics 诊断污染、重复与饥饿。
- **系统设计与评审**：在离线物化和 Streaming Dataset、随机性和顺序读、packing 利用率和样本隔离间取舍。

## 与既有经验的连接

- **数据库内核**：Tokenization 像解析，packing 像向量批成形；但 token 边界由模型词表决定，不是 SQL 语法边界。
- **存储引擎**：Arrow/Parquet 的列式布局、row group 与谓词下推类比成立；但训练 shuffle/epoch 语义不由文件格式自动保证。
- **计算引擎**：Streaming Dataset 像持续输入 source，prefetch 像上游流水；但训练需要可复现采样与全局 shard，而非只追求低延迟。
- **分布式系统**：worker shard 类似分区消费；但重启后的样本 exactly-once 需要显式游标/种子，不能从对象存储读成功推导。
- **可观测性**：data wait、读取带宽、packing efficiency 与 token 分布需关联；GPU idle 只能提示供给不足，不能定位 tokenizer 或存储。

## 知识型学习产出

分析数据供给吞吐和训练瓶颈

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P6：AI Data、GPU Cluster 与生产级基础设施](../README.md)
