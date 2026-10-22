# W36 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [FlashInfer repository](https://github.com/flashinfer-ai/flashinfer/tree/6a2f2661d24db6400466db51f482cd3c95faffaa) — **选入理由**：固定仓库把 paged/ragged KV、prefill/decode 与 plan/run 生命周期落实到真实 Kernel 和绑定层，便于追性能路径；**支撑 Scope**：FlashInfer 与推理 Kernel；**阅读深度**：精读 paged/ragged KV APIs、prefill/decode attention 与 plan/run。
- [FlashInfer documentation](https://docs.flashinfer.ai/) — **选入理由**：它集中定义 page table、head 数量与 workspace 等调用契约，是判断 Kernel 输入布局和 GQA 兼容性的权威入口；**支撑 Scope**：Paged Attention 与 GQA 接口；**阅读深度**：精读 batch decode/prefill、page table、num_qo_heads/num_kv_heads 约束。
- [GQA (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.298/) — **选入理由**：它系统比较 MHA、MQA 与分组共享 KV head，在质量、KV 容量和 decode 带宽之间给出直接证据；**支撑 Scope**：GQA；**阅读深度**：精读 head sharing、质量/速度评估与适用边界。
