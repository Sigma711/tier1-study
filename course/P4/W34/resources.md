# W34 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [Sarathi-Serve (OSDI 2024)](https://www.usenix.org/conference/osdi24/presentation/agrawal) — **选入理由**：它用 chunked prefill 消除长 prompt 对 decode 的阻塞，并给出 chunk 大小、吞吐和延迟之间可推导的权衡；**支撑 Scope**：Chunked Prefill 与 stall-free scheduling；**阅读深度**：精读机制、chunk 选择、实验负载与局限。
- [Orca (OSDI 2022)](https://www.usenix.org/conference/osdi22/presentation/yu) — **选入理由**：它奠定 iteration-level scheduling 与 selective batching 的系统模型，是理解 continuous batching 为何能处理异长请求的源头；**支撑 Scope**：Continuous Batching；**阅读深度**：精读 iteration-level scheduling 与 selective batching。
- [vLLM Optimization and Tuning](https://docs.vllm.ai/en/latest/configuration/optimization.html) — **选入理由**：它把 token budget、chunked prefill 和 preemption 变成可核验配置，能将论文机制映射到真实容量约束；**支撑 Scope**：Admission Control 相关容量约束与 Chunked Prefill 配置；**阅读深度**：精读 token budget、preemption 与调优证据；公平策略需回看 scheduler 源码。
- [vLLM scheduler source](https://github.com/vllm-project/vllm/blob/9c66703eef1726bdd582370cbeed52ebdb7c2c80/vllm/v1/core/sched/scheduler.py) — **选入理由**：源码中的 waiting/running 队列、priority、preemption 分支才是实际准入与公平语义，可用来检验文档没有承诺的行为；**支撑 Scope**：Admission Control、公平调度的实际策略；**阅读深度**：精读 waiting/running、priority、preemption 与 token budget 分支。
