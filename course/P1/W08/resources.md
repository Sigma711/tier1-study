# W08 · 固定学习资料

> 资料状态核验：2026-10-22。

- [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/index) — **选入理由**：官方库文档覆盖 normalization、pre-tokenization、model 与 vocabulary；**支撑 Scope**：Tokenization、Embedding 输入契约；**阅读深度**：读 pipeline 四阶段、BPE/Unigram 与 id/vocab serialization。
- [PyTorch Embedding](https://docs.pytorch.org/docs/stable/generated/torch.nn.Embedding.html) — **选入理由**：官方 API 明确 lookup table、padding_idx、sparse gradient；**支撑 Scope**：Embedding；**阅读深度**：推导参数量与输出 shape，精读 padding/sparse/max_norm 边界。
- [Root Mean Square Layer Normalization](https://papers.neurips.cc/paper/9403-root-mean-square-layer-normalization) — **选入理由**：RMSNorm 原文删去 re-centering、保留按均方根缩放，并用实验检验这一简化的速度和质量影响，是比较 LayerNorm 与 RMSNorm 不变量的原始依据；**支撑 Scope**：Normalization；**阅读深度**：精读 RMS 统计量、与 LayerNorm 的差别、计算和实验限制。
- [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) — **选入理由**：该论文在参数量对齐条件下比较 ReGLU、GEGLU、SwiGLU 等前馈结构，能解释现代 LLM MLP 为何常选门控变体而非普通两层 FFN；**支撑 Scope**：MLP；**阅读深度**：精读各 GLU 公式、参数匹配方式与实验设置。
- [Switch Transformers](https://www.jmlr.org/papers/v23/21-0998.html) — **选入理由**：JMLR 论文具体描述 sparse expert routing；**支撑 Scope**：LLM 架构、Dense/MoE；**阅读深度**：精读 router、top-1 dispatch、capacity factor、load balancing 与 failure modes。
- [Hugging Face Transformers model outputs/source](https://github.com/huggingface/transformers/tree/ab7e5ac33f234b41665fee663fefd441d35ad3d4) — **选入理由**：本日核验到的官方仓库包含主流 LLM Embedding/MLP/Norm/MoE 实现；**支撑 Scope**：LLM 架构各组件；**阅读深度**：选一个固定模型版本，追 `modeling_*.py` 的模块与 tensor shape，不把仓库整体当单一证据。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
