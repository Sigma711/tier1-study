# W48 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：NCCL、Ring/Tree Collectives、NVLink、RDMA、异步 Checkpoint。

1. 用 alpha-beta 模型比较 Ring 与 Tree 在不同消息规模/rank 数下的延迟趋势。
2. NCCL 如何利用 NVLink 与 RDMA，为什么 collective 完成不代表 checkpoint 已持久化？
3. 分别为 NCCL 和异步 Checkpoint 列出源码对象、性能指标与对照变量。
4. 如何用 topology/debug log 诊断 collective hang，并用 generation/完成标记诊断半成品 checkpoint？
5. 状态量 S、写带宽 B 下如何选择 staging 容量、保存频率和同步/异步策略？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
