# W38 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [Fast Inference from Transformers via Speculative Decoding](https://proceedings.mlr.press/v202/leviathan23a.html) — **选入理由**：它给出 draft—verify 的接受/拒绝算法以及输出分布不变的证明，使“猜多个 token”为何仍然精确可被严格推导；**支撑 Scope**：Speculative Decoding；**阅读深度**：精读接受/拒绝算法、分布保持证明、期望加速与实验条件。
- [vLLM Speculative Decoding](https://docs.vllm.ai/en/latest/features/spec_decode.html) — **选入理由**：它列出 proposer/scorer 的可用组合、acceptance 指标和兼容限制，揭示论文算法落地时真正限制收益的工程条件；**支撑 Scope**：工程中的 proposer/scorer 与限制；**阅读深度**：精读配置、acceptance 指标、兼容边界；与论文算法分开。
- [vLLM Sampling Parameters](https://docs.vllm.ai/en/latest/api/vllm/sampling_params.html) — **选入理由**：它精确定义 temperature、top-k/top-p、随机种子与 logits processor 的执行语义，是分析可复现性和输出分布的接口契约；**支撑 Scope**：Sampling；**阅读深度**：精读 temperature、top-k、top-p、seed 与 logits processors。
- [vLLM Structured Outputs](https://docs.vllm.ai/en/latest/features/structured_outputs.html) — **选入理由**：它说明 grammar 或 JSON Schema 如何转成逐 token mask，可据此分析格式保证、backend 差异和解码开销；**支撑 Scope**：Structured Output；**阅读深度**：精读 grammar/JSON schema/choice、backend 与 token mask 限制。
- [MegaBlocks (MLSys 2023)](https://proceedings.mlsys.org/paper_files/paper/2023/hash/5a54f79333768effe7e8927bcccffe40-Abstract-mlsys2023.html) — **选入理由**：它以 dropless block-sparse computation 处理专家负载不均，为理解单节点 MoE 路由后的稀疏执行成本提供直接模型；**支撑 Scope**：MoE 推理基础中的稀疏专家计算与负载不均；**阅读深度**：精读 routing、dropless block-sparse computation；不提前扩展到多 GPU EP。
- [vLLM Multimodal Inputs](https://docs.vllm.ai/en/latest/contributing/model/multimodal.html) — **选入理由**：它展示图像等输入如何经过 processor、placeholder 和 token 对齐进入模型，能定位多模态接入最常见的长度与映射错误；**支撑 Scope**：多模态推理基础；**阅读深度**：精读 input mapper/processor、placeholder/token 对齐与模型接入边界。
