# W33 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [vLLM V1 design](https://docs.vllm.ai/en/latest/design/v1.html) — **选入理由**：它解释 V1 为何把调度与 GPU 执行拆成 EngineCore、Worker 和 ModelRunner，是阅读源码前最清楚的组件边界图；**支撑 Scope**：V1 架构、Engine、Scheduler；**阅读深度**：精读 EngineCore、scheduler step 与请求状态。
- [vLLM worker source](https://github.com/vllm-project/vllm/tree/9c66703eef1726bdd582370cbeed52ebdb7c2c80/vllm/v1/worker) — **选入理由**：固定源码能核验调度输出怎样变成输入 batch、KV 映射和一次 GPU forward，补齐架构图刻意省略的执行细节；**支撑 Scope**：Worker、Model Runner；**阅读深度**：精读 worker/gpu_model_runner 的输入输出和执行边界。
- [vLLM core source](https://github.com/vllm-project/vllm/tree/9c66703eef1726bdd582370cbeed52ebdb7c2c80/vllm/v1/core) — **选入理由**：这里集中保存请求状态、token budget、KV 分配和调度结果，是验证 Engine 不变量与回压路径的直接证据；**支撑 Scope**：Engine/Scheduler 的真实对象；**阅读深度**：精读 scheduler、KV manager 与 output 处理调用链。
