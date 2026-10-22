# W06 · 固定学习资料

> 资料状态核验：2026-10-22。

- [PyTorch Autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd.html) — **选入理由**：官方机制文档解释动态图、Node 与 saved tensor；**支撑 Scope**：神经网络计算图、Autograd；**阅读深度**：精读 graph recreation、saved tensors、in-place correctness 与 grad modes。
- [PyTorch autograd graph API](https://docs.pytorch.org/docs/stable/autograd.html#autograd-graph) — **选入理由**：官方 API 暴露 Node、next_functions、saved_tensors hooks；**支撑 Scope**：计算图、Autograd；**阅读深度**：定位 Node metadata、hooks 与 anomaly detection，连接到诊断证据。
- [Training Deep Nets with Sublinear Memory Cost](https://arxiv.org/abs/1604.06174) — **选入理由**：Activation 重算的经典论文给出复杂度权衡；**支撑 Scope**：计算与内存复杂度、Activation；**阅读深度**：精读分段算法、\(O(\sqrt n)\) 内存结论、计算代价和假设。
- [PyTorch Activation Checkpointing](https://docs.pytorch.org/docs/stable/checkpoint.html) — **选入理由**：官方文档给出当前重算 API 与 RNG/early-stop 边界；**支撑 Scope**：Activation、计算与内存复杂度；**阅读深度**：读 reentrant/non-reentrant 差异、RNG state、determinism_check。
- [PyTorch FX](https://docs.pytorch.org/docs/stable/fx.html) — **选入理由**：官方图表示用于区分 eager autograd graph 与显式 GraphModule；**支撑 Scope**：神经网络计算图；**阅读深度**：精读 symbolic tracing、Graph/Node、limitations，不把 FX 图等同设备 Kernel。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
