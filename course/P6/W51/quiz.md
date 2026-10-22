# W51 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：模型权重、Checkpoint、分布式存储、一致性与恢复语义。

1. 由状态量 S、rank 数 N、带宽 B 与间隔 I 推导 checkpoint 保存时长和故障浪费上界。
2. Distributed Checkpoint planner、StorageWriter/Reader 与 metadata 分别承担什么职责？
3. 可发布模型权重与可续训 checkpoint 的恢复契约有何不同？
4. 哪些 shard、generation、step/revision 证据能判定 torn checkpoint？
5. 比较全量/增量、同步/异步和不同分片粒度的性能与一致性取舍。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
