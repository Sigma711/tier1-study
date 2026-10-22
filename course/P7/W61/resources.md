# W61 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [DistServe](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) — **选入理由**：OSDI 2024 分离 prefill/decode 的分布式推理论文；**支撑 Scope**：Distributed Runtime、通信；**阅读深度**：读 placement、goodput 模型、跨阶段传输和故障/限制。
- [NIXL](https://github.com/ai-dynamo/nixl/tree/0b146a82d8efb52f40b1da872bb271978f510e94) — **选入理由**：NIXL 的固定实现把 Descriptor、Backend、内存注册、异步 Completion 和失败返回组织为跨介质传输协议，可直接审查分布式 KV 传输的资源生命周期与错误路径；**支撑 Scope**：缓存传输、通信；**阅读深度**：定位 descriptor、backend、registration、completion 与失败返回路径。
- [Ray Task Fault Tolerance](https://docs.ray.io/en/latest/ray-core/fault_tolerance/tasks.html) — **选入理由**：明确 task、worker 与 node 失败时的重试、重放和异常传播语义，可作为区分“运行时重试”与“模型/KV 状态恢复”的一手基线；**支撑 Scope**：容错、Distributed Runtime；**阅读深度**：读 task/worker/node failure 与 lineage reconstruction，再对照同目录的 actor/object/GCS 容错页面，辨明重试与 KV/模型状态恢复的差距。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
