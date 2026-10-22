# W55 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [DCGM User Guide](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/index.html) — **选入理由**：数据中心 GPU field、entity、health 与 diagnostics 的官方说明；**支撑 Scope**：DCGM；**阅读深度**：读 field groups、watch/update、health/diagnostics 与 exporter 边界。
- [NVML API Reference](https://docs.nvidia.com/deploy/nvml-api/) — **选入理由**：NVML API Reference 定义设备、进程、显存和利用率查询的返回值、采样语义及错误码，是判断 GPU 指标到底由驱动暴露什么、不能推断什么的底层合同；**支撑 Scope**：NVML；**阅读深度**：读 device/process/memory/utilization 查询、采样语义与错误码。
- [CUPTI Documentation](https://docs.nvidia.com/cupti/) — **选入理由**：CUDA activity/callback/profiler 数据采集接口的一手文档；**支撑 Scope**：CUPTI；**阅读深度**：读 Activity records、Callback domains、buffer/dropped-record 处理与开销。
- [Nsight Systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/) — **选入理由**：CPU/CUDA/NCCL 时间线分析的官方文档；**支撑 Scope**：Nsight；**阅读深度**：读 capture、timeline、NVTX、report/export 与采样限制。
- [Nsight Compute Documentation](https://docs.nvidia.com/nsight-compute/) — **选入理由**：Kernel 级 counter/section 分析的官方文档；**支撑 Scope**：Nsight；**阅读深度**：读 metric collection、replay、sections/rules 与测量扰动。
- [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/) — **选入理由**：trace/span/context/links 的官方语义；**支撑 Scope**：OpenTelemetry、端到端 Tracing；**阅读深度**：读 context propagation、sampling、links/events 与跨异步边界限制。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
