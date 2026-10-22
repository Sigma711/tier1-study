# W03 · 固定学习资料

> 资料状态核验：2026-10-22。

- [PyTorch Tensor Views](https://docs.pytorch.org/docs/stable/tensor_view.html) — **选入理由**：官方文档直达 view、contiguous 与 stride 语义；**支撑 Scope**：张量、Shape、Stride；**阅读深度**：精读 view ops、contiguity 与 reshape 行为，并能手算 storage offset。
- [NumPy Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) — **选入理由**：NumPy 明确定义从尾维对齐的兼容规则，并给出 Broadcasting 何时避免复制、何时制造巨大中间量的反例，是判断 Shape 推导是否合法的最小权威依据；**支撑 Scope**：向量、矩阵、Shape、Broadcasting；**阅读深度**：精读 general broadcasting rules 与会导致物化/大中间量的例子。
- [PyTorch matmul](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html) — **选入理由**：官方 API 明确 1D/2D/batched matmul 的维度规则；**支撑 Scope**：向量、矩阵、矩阵乘法；**阅读深度**：逐种 rank 推导输出 shape、broadcast batch 与复杂度。
- [NumPy Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html) — **选入理由**：NumPy 的 mean/var 接口把 axis、累加 dtype 与 ddof/correction 对结果的影响暴露出来，可直接验证数学定义落到数组计算后为何会改变精度与估计偏差；**支撑 Scope**：期望、方差、估计；**阅读深度**：精读 mean/var 的 axis、dtype、ddof/correction，区分总体方差和样本估计。
- [PyTorch Distributions](https://docs.pytorch.org/docs/stable/distributions.html) — **选入理由**：官方实现将分布参数、采样、log_prob 和统计量具体化；**支撑 Scope**：分布、采样、期望、方差；**阅读深度**：精读 Distribution、Normal/Categorical、sample/rsample、mean/variance，解释随机种子与重参数化边界。
- [NIST/SEMATECH e-Handbook: Estimation](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm) — **选入理由**：NIST 将点估计、区间估计、标准误和样本量放进同一统计框架，能校正“一个样本值就是总体性质”这类工程测量误判；**支撑 Scope**：采样与估计；**阅读深度**：读 point/interval estimation、标准误与样本量，避免把单次样本当总体结论。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
