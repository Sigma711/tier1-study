# W43 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：DDP、Gradient Synchronization、AllReduce、通信与计算重叠。

1. 推导 p 个 rank 对 M 字节梯度执行 ring AllReduce 时每 rank 的通信量。
2. 说明 DDP Reducer、autograd hook 与 gradient bucket 如何决定 AllReduce 启动时刻。
3. bucket 太小和太大分别如何影响启动延迟与计算通信重叠？
4. 某 rank 的 collective 顺序不同为何会 hang，哪些 rank stack/NCCL trace 能证伪网络带宽不足？
5. 给定模型显存可容纳但 scaling efficiency 下降，如何评审继续 DDP 还是改用状态切分？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
