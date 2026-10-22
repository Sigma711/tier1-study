# W41 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [vLLM V1 design](https://docs.vllm.ai/en/latest/design/v1.html) — **选入理由**：它提供 Engine—Scheduler—Worker 的清晰责任切面，适合作为 Mini Engine 设计取舍和接口完整性的参照，而不是照抄实现；**支撑 Scope**：Mini Engine 的 Engine/Scheduler/Worker 主链；**阅读深度**：精读组件接口、scheduler step 与输出处理。
- [PagedAttention (SOSP 2023)](https://doi.org/10.1145/3600006.3613165) — **选入理由**：其 block table、共享与 copy-on-write 不变量给 Mini Engine 的 KV allocator 提供可证明的正确性和容量模型；**支撑 Scope**：Mini Engine 的 KV allocator/cache；**阅读深度**：精读容量、block table、共享和回收不变量。
- [FlashInfer documentation](https://docs.flashinfer.ai/) — **选入理由**：它精确规定 paged KV、prefill/decode plan/run 和 shape 契约，可用来划定 Mini Engine 与 attention Kernel 的集成边界；**支撑 Scope**：Mini Engine 的 attention kernel 边界；**阅读深度**：精读 paged KV、prefill/decode plan/run 与 shape 约束。
- [vLLM Metrics](https://docs.vllm.ai/en/latest/design/metrics.html) — **选入理由**：vLLM Metrics 直接给出综合考核所需 TTFT、TPOT 与队列证据的对象模型、接口和边界，是从概念进入真实工程实现的主线资料；**支撑 Scope**：综合考核的 TTFT/TPOT/队列证据；**阅读深度**：精读各指标的计时起止点、直方图桶、请求状态与日志关联，能够从排队、prefill 和 decode 分解尾延迟。
- [MLPerf Inference Policies](https://docs.mlcommons.org/inference/index_gh/) — **选入理由**：它用有效样本、延迟约束与披露要求约束 benchmark，可作为综合考核中识别 cherry-picking 和不可比结果的裁判规则；**支撑 Scope**：综合考核 benchmark 可复现性；**阅读深度**：精读 Server scenario、有效样本、延迟约束与报告。
