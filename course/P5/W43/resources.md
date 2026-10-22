# W43 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [PyTorch DDP Design Note](https://pytorch.org/docs/stable/notes/ddp.html) — **选入理由**：Reducer、bucket 与 autograd hook 的官方设计；**支撑 Scope**：DDP、Gradient Synchronization、通信与计算重叠；**阅读深度**：读 constructor/forward/backward 三阶段并追到 Reducer 源码。
- [PyTorch DDP paper](https://arxiv.org/abs/2006.15704) — **选入理由**：PyTorch DDP 论文公开 Reducer 的 Bucket、Autograd Hook 与通信重叠设计，并用实验拆分各优化收益，是理解当前框架实现为何不等同“反向后做一次 AllReduce”的原始系统证据；**支撑 Scope**：DDP、Gradient Synchronization；**阅读深度**：读 bucketing、hook、动态图支持、实验变量与限制。
- [NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) — **选入理由**：AllReduce 计数、原地语义与 collective 顺序的官方说明；**支撑 Scope**：AllReduce；**阅读深度**：读 AllReduce/ReduceScatter/AllGather 等价关系、count 语义和 rank 参与约束。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
