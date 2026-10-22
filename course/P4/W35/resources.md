# W35 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [PagedAttention (SOSP 2023)](https://doi.org/10.1145/3600006.3613165) — **选入理由**：它把操作系统分页思想引入 KV Cache，定量解释连续预留造成的内部/外部碎片以及 copy-on-write 共享收益；**支撑 Scope**：Paged KV Cache、Block Allocator；**阅读深度**：精读容量模型、block table、copy-on-write 与实验边界。
- [vLLM Automatic Prefix Caching](https://docs.vllm.ai/en/latest/design/prefix_caching.html) — **选入理由**：它给出 prefix block 的 hash 身份、复用条件与 salt 隔离，能同时分析命中率、正确性和多租户安全；**支撑 Scope**：Prefix Caching；**阅读深度**：精读 block hash、可共享条件、salt 与安全边界。
- [vLLM KV cache manager source](https://github.com/vllm-project/vllm/blob/9c66703eef1726bdd582370cbeed52ebdb7c2c80/vllm/v1/core/kv_cache_manager.py) — **选入理由**：固定源码完整展示 block pool、free queue、引用计数和淘汰顺序，可用于证明无泄漏、无悬挂复用等分配器不变量；**支撑 Scope**：引用计数与淘汰；**阅读深度**：精读 block pool/free queue、ref count、touch/free 与 eviction。
