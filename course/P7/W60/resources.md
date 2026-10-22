# W60 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [PagedAttention paper](https://arxiv.org/abs/2309.06180) — **选入理由**：vLLM Paged KV Cache 与 continuous batching 的原论文；**支撑 Scope**：Runtime、Paged KV Cache；**阅读深度**：精读 block table、碎片模型、调度和实验口径。
- [vLLM Scheduler source](https://github.com/vllm-project/vllm/tree/9c66703eef1726bdd582370cbeed52ebdb7c2c80/vllm/v1/core) — **选入理由**：Scheduler、KVCacheManager 与 block pool 的官方源码目录；**支撑 Scope**：Scheduler、Paged KV Cache、Admission Control；**阅读深度**：沿 request status、schedule output、allocation/free/preemption 调用链。
- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics/) — **选入理由**：官方定义 queue、TTFT、TPOT 与 cache 指标；**支撑 Scope**：Admission Control、Runtime；**阅读深度**：读各 histogram/counter 的时间边界并用于验证过载取舍。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
