# W17 · 固定学习资料

> 资料状态核验：2026-10-22。GitHub 条目描述本日核验到的官方仓库。

- [FlashAttention](https://arxiv.org/abs/2205.14135) — **选入理由**：NeurIPS 论文作者公开的原始论文页，建立 IO-aware exact attention；**支撑 Scope**：FlashAttention、IO Complexity；**阅读深度**：精读算法 1、IO complexity 定理、实验设置和硬件假设。
- [Online normalizer calculation for softmax](https://arxiv.org/abs/1805.02867) — **选入理由**：online softmax 原始算法论文给出 running max/sum 递推；**支撑 Scope**：Online Softmax；**阅读深度**：精读递推式、正确性证明与内存访问次数。
- [FlashAttention-2](https://openreview.net/forum?id=mZn2Xyh9Ec) — **选入理由**：ICLR 论文聚焦 warp/work partition 改进；**支撑 Scope**：FlashAttention、Warp 分工；**阅读深度**：精读 work partitioning、non-matmul FLOPs、sequence parallelism 与实验控制。
- [FlashAttention repository @ 767386d](https://github.com/Dao-AILab/flash-attention/tree/767386d814051d1d853c45ac952d8259b5bc7235) — **选入理由**：2026-10-22 核验到的论文官方实现固定 revision；**支撑 Scope**：FlashAttention、Online Softmax、Warp 分工；**阅读深度**：追 forward Kernel 的 tile loop、softmax state、Q/K/V staging 与支持矩阵。
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) — **选入理由**：官方 API 是语义参考和框架 backend 入口；**支撑 Scope**：FlashAttention 对照；**阅读深度**：读等价实现、backend selection、mask/dropout/GQA 约束，用作正确性基线。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
