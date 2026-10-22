# W47 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [Switch Transformers](https://jmlr.org/papers/v23/21-0998.html) — **选入理由**：稀疏 MoE、capacity factor 与负载均衡的经典一手论文；**支撑 Scope**：MoE、负载均衡；**阅读深度**：读 router、capacity、auxiliary loss、dropped token 与 scaling 证据。
- [Megatron Core MoE](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/moe.html) — **选入理由**：把 Expert Parallelism、token dispatcher、All-to-All 与并行折叠放在同一实现框架中，是理解生产级 MoE 通信路径的官方主线；**支撑 Scope**：Expert Parallelism、All-to-All；**阅读深度**：读 router、token dispatcher、parallel folding 与 load-balancing 配置。
- [Megatron-LM MoE source](https://github.com/NVIDIA/Megatron-LM/tree/aa46a57229995b4c537ed2f554e78d10473e4964/megatron/core/transformer/moe) — **选入理由**：核验 token permutation/router/expert 的官方源码；**支撑 Scope**：MoE、Expert Parallelism、负载均衡；**阅读深度**：沿 router→dispatcher→experts→unpermutation 调用链。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
