# W44 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [ZeRO](https://www.microsoft.com/en-us/research/publication/zero-memory-optimizations-toward-training-trillion-parameter-models/) — **选入理由**：ZeRO 三阶段状态切分和通信分析的 SC20 原论文；**支撑 Scope**：ZeRO、参数与优化器状态切分；**阅读深度**：推导 model/gradient/optimizer partition 的显存与通信公式，核对实验假设。
- [PyTorch FSDP2](https://docs.pytorch.org/docs/stable/distributed.fsdp.fully_shard.html) — **选入理由**：fully_shard/DTensor 实现的官方 API 与语义；**支撑 Scope**：FSDP2；**阅读深度**：读 sharding placement、unshard/reshard、mixed precision 与 state-dict 行为。
- [PyTorch Distributed Checkpoint](https://pytorch.org/docs/stable/distributed.checkpoint.html) — **选入理由**：切分状态保存和 load-time reshard 的官方契约；**支撑 Scope**：参数与优化器状态切分；**阅读深度**：读 state_dict、planner、metadata 与 world-size 变化边界。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
