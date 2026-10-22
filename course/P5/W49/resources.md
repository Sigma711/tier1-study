# W49 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [TorchTitan](https://github.com/pytorch/torchtitan/tree/ed3c713afeb21a514714ff59fec4fd4bb2d3b09d) — **选入理由**：固定 revision 的 TorchTitan 把训练入口、配置、模型、并行维度和 Checkpoint 串在同一代码库中，可沿一条真实调用链审查组合式训练系统的控制面与数据面；**支撑 Scope**：TorchTitan 综合研究；**阅读深度**：读 train.py、config、parallelisms、models 与 checkpoint 调用链，并固定 revision 复核。
- [Megatron Core Developer Guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/) — **选入理由**：Megatron 并行、Transformer 与训练组件的官方入口；**支撑 Scope**：Megatron 综合研究；**阅读深度**：读 parallel_state、transformer、pipeline schedules、distributed optimizer 与 checkpoint。
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM/tree/aa46a57229995b4c537ed2f554e78d10473e4964) — **选入理由**：Megatron-LM 的固定源码提供另一套成熟的训练 Loop、并行组和融合 Kernel 组织方式，使 TorchTitan 的可组合设计能够在同一模型配置下做实现级对照，而不是停留在项目口号；**支撑 Scope**：TorchTitan / Megatron 对照；**阅读深度**：固定同一模型/配置，逐项对照训练 loop、并行组、Kernel 和指标口径。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
