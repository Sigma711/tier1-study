# W40 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [MLPerf Inference Policies](https://docs.mlcommons.org/inference/index_gh/) — **选入理由**：它严格定义 Server 场景的请求到达、延迟约束、有效样本与报告规则，为跨系统 benchmark 提供最低可比性门槛；**支撑 Scope**：Serving Benchmark 与负载模型；**阅读深度**：精读 Server scenario、LoadGen、latency constraints、validity 与报告规则。
- [DistServe (OSDI 2024)](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) — **选入理由**：它把满足多维延迟 SLO 的有效吞吐定义为 goodput，并公开 workload 方法，适合校正只看 tokens/s 的错误评测；**支撑 Scope**：Goodput 与 SLO；**阅读深度**：精读 goodput 定义、多维 SLO 和 workload methodology。
- [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/) — **选入理由**：它解释大规模 fan-out 如何放大尾延迟，并讨论 hedging 等手段的条件与代价，是 p99 系统推理的经典基线；**支撑 Scope**：Tail Latency；**阅读深度**：精读 tail amplification、hedging 背景与适用边界。
- [vLLM Benchmark CLI](https://docs.vllm.ai/en/latest/cli/bench/serve.html) — **选入理由**：它明确请求率、burstiness、数据集长度分布与输出字段如何进入测量，可直接审查 benchmark 是否复现真实负载；**支撑 Scope**：serving benchmark 的请求率/数据集/指标实现；**阅读深度**：精读 request-rate、burstiness、length 参数和输出字段。
