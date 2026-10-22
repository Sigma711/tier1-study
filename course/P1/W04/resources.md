# W04 · 固定学习资料

> 资料状态核验：2026-10-22。

- [Automatic Differentiation in Machine Learning: a Survey](https://www.jmlr.org/papers/v18/17-468.html) — **选入理由**：JMLR 综述严格建立微积分、链式法则和 reverse mode；**支撑 Scope**：微积分、链式法则、梯度、反向传播；**阅读深度**：精读 2–3 节的 computational graph、Jacobian accumulation 与复杂度。
- [PyTorch Autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd.html) — **选入理由**：官方说明 graph、saved tensors 与 in-place correctness；**支撑 Scope**：梯度、反向传播；**阅读深度**：读 graph creation、saved tensors、in-place checks 和 multithreaded autograd。
- [SGD PyTorch](https://docs.pytorch.org/docs/stable/generated/torch.optim.SGD.html) — **选入理由**：PyTorch 把 momentum、dampening、weight decay 与 Nesterov 的实际更新次序写成公式并映射到参数选项，可核对课堂推导与主流框架实现是否同义；**支撑 Scope**：SGD；**阅读深度**：逐项推导 momentum、dampening、weight_decay、nesterov。
- [Decoupled Weight Decay Regularization](https://openreview.net/forum?id=Bkg6RiCqY7) — **选入理由**：AdamW 的 ICLR 原论文解释解耦权重衰减；**支撑 Scope**：AdamW；**阅读深度**：精读算法、与 L2 regularization 的差别及实验控制。
- [AdamW PyTorch](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html) — **选入理由**：PyTorch 的 AdamW 文档同时给出解耦 weight decay 公式、优化器状态和 foreach/fused/capturable 实现选项，能把算法差异与显存、捕获和吞吐代价对应起来；**支撑 Scope**：AdamW；**阅读深度**：核对公式、state tensors、foreach/fused/capturable 选项与内存代价。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
