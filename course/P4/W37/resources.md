# W37 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [SmoothQuant (ICML 2023)](https://proceedings.mlr.press/v202/xiao23c.html) — **选入理由**：它展示如何把 activation outlier 的难度平滑迁移到权重侧，使 W8A8 的误差来源和离线变换都可推导；**支撑 Scope**：INT8 与量化误差；**阅读深度**：精读 activation outlier 迁移、W8A8 与质量/性能实验。
- [AWQ (MLSys 2024)](https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) — **选入理由**：它用 activation 统计保护少量显著权重，连接 INT4 误差模型、group scale 与真正可加速的 weight-only Kernel；**支撑 Scope**：INT4/低比特格式；**阅读深度**：精读 activation-aware weight-only、group scales 与 kernel 实现。
- [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433) — **选入理由**：它明确 E4M3 与 E5M2 的范围—精度分工及 scaling 条件，是判断 FP8 溢出、舍入和累加风险的格式依据；**支撑 Scope**：FP8；**阅读深度**：精读 E4M3/E5M2 范围、精度与 scaling。
- [vLLM Quantization](https://docs.vllm.ai/en/latest/features/quantization/) — **选入理由**：其支持矩阵把量化格式、GPU capability 和实际 backend 对齐，可避免把“模型可量化”误当成“当前硬件能加速”；**支撑 Scope**：量化 Kernel 与硬件兼容；**阅读深度**：精读量化方法支持矩阵、GPU capability 与实际 backend。
