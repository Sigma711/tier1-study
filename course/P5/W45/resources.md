# W45 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [Megatron-LM](https://arxiv.org/abs/1909.08053) — **选入理由**：Transformer tensor parallel 的经典原论文；**支撑 Scope**：Tensor Parallelism；**阅读深度**：精读 MLP/attention 的 row/column split、collective 与 scaling 实验。
- [PyTorch Tensor Parallel](https://docs.pytorch.org/docs/stable/distributed.tensor.parallel.html) — **选入理由**：TP 与 sequence parallel style 的官方实现；**支撑 Scope**：Tensor、Sequence Parallelism；**阅读深度**：读 Colwise/Rowwise/SequenceParallel、输入输出 layout 与 parallelize_module。
- [PyTorch Context Parallel Tutorial](https://docs.pytorch.org/tutorials/unstable/context_parallel.html) — **选入理由**：以 TorchTitan 为例串起 Context Parallel 的 buffer 分片、attention 通信与多维并行组合，是当前可访问的官方端到端机制说明；**支撑 Scope**：Context Parallelism；**阅读深度**：读 ring attention、buffer、load balance、组合并行与限制。
- [PyTorch DTensor](https://pytorch.org/docs/stable/distributed.tensor.html) — **选入理由**：DTensor 文档精确定义 DeviceMesh 以及 Shard、Replicate、Partial placement，并说明 redistribute 与布局传播怎样触发 Collective，是把张量并行布局写成可组合语义的官方依据；**支撑 Scope**：DTensor、DeviceMesh；**阅读深度**：读 DeviceMesh 与 Shard/Replicate/Partial placement、redistribute 和 layout propagation。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
