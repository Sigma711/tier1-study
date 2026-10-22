# W07 · 固定学习资料

> 资料状态核验：2026-10-22。

- [Attention Is All You Need](https://papers.nips.cc/paper/7181-attention-is-all-you-need) — **选入理由**：Transformer 原始 NeurIPS 论文；**支撑 Scope**：Transformer、Self-Attention、Multi-Head Attention；**阅读深度**：精读 3.1–3.2、表 1 与复杂度讨论，独立推导 shape/FLOPs。
- [RoFormer](https://arxiv.org/abs/2104.09864) — **选入理由**：RoFormer 原文从旋转矩阵推导位置编码如何让 Attention 显式依赖相对位移，是理解 RoPE 数学性质及其外推局限的首要出处；**支撑 Scope**：RoPE；**阅读深度**：精读 3.2 节复数/旋转矩阵形式与相对位置性质，区分论文性质和具体实现。
- [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150) — **选入理由**：这篇论文首次系统化提出 Multi-Query Attention，用共享 K/V Head 直接换取更低解码带宽，并给出质量与速度对照，是追溯 MQA 设计动机的原始证据；**支撑 Scope**：MQA；**阅读深度**：读模型改动、memory bandwidth 动机与质量/速度实验。
- [GQA: Training Generalized Multi-Query Transformer Models](https://aclanthology.org/2023.emnlp-main.298/) — **选入理由**：GQA 原文定义 K/V Head 分组并给出从 MHA Checkpoint uptraining 的方法，恰好量化了 MHA 质量与 MQA 带宽之间的折中；**支撑 Scope**：GQA；**阅读深度**：精读 group 数定义、uptraining 方法与质量/速度对照。
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) — **选入理由**：官方 API 具体呈现 mask、scale、causal 与 enable_gqa 语义；**支撑 Scope**：Self-Attention、GQA/MQA；**阅读深度**：逐行读等价实现、shape 约束与 backend 选择注意事项。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
