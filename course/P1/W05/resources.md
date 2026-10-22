# W05 · 固定学习资料

> 资料状态核验：2026-10-22。

- [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/) — **选入理由**：IEEE 754 是浮点格式、舍入方向、NaN/Inf 与异常行为的规范源头，没有它就无法区分硬件或框架差异与标准本身允许的结果空间；**支撑 Scope**：浮点数与数值计算、FP32；**阅读深度**：掌握 interchange format、rounding、NaN/Inf 与异常语义，不需背全部条款。
- [NVIDIA Floating Point and IEEE 754](https://docs.nvidia.com/cuda/floating-point/) — **选入理由**：官方白皮书把舍入、FMA 和 GPU 行为具体化；**支撑 Scope**：FP32、FP16、量化误差；**阅读深度**：精读 representation、rounding、FMA 与 comparison pitfalls。
- [PyTorch Numerical Accuracy](https://docs.pytorch.org/docs/stable/notes/numerical_accuracy.html) — **选入理由**：官方文档列出低精度、reduction 和 extremal values 的真实边界；**支撑 Scope**：FP16、BF16、量化误差；**阅读深度**：读 reduced-precision reduction、TF32、non-finite values 与验证建议。
- [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433) — **选入理由**：NVIDIA、Arm、Intel 作者给出 E4M3/E5M2 的原始格式与实验；**支撑 Scope**：FP8、量化误差；**阅读深度**：精读格式范围、特殊值、scaling 与训练实验，论文结论与具体框架实现分别核对。
- [PyTorch AMP examples](https://docs.pytorch.org/docs/stable/notes/amp_examples.html) — **选入理由**：官方示例说明 autocast 与 GradScaler 的职责；**支撑 Scope**：FP16、BF16、数值计算；**阅读深度**：读 typical/multiple models/custom autograd，识别 overflow 与 unscale 顺序。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
