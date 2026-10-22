# W62 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [KServe Architecture](https://kserve.github.io/website/docs/concepts/architecture) — **选入理由**：KServe 架构文档把 InferenceService CRD、Reconcile、Predictor、网络与 Autoscaling 串成真实控制面，适合定位模型服务部署和资源配置分别由谁负责；**支撑 Scope**：Platform、部署、资源控制；**阅读深度**：读 CRD/reconcile、predictor、networking、autoscaling 和 GPU 配置边界。
- [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/) — **选入理由**：OpenTelemetry 对 Trace、Span、Context、Link 与 Sampling 的定义提供跨组件关联的共同语义，也明确高基数 Attribute 和采样会怎样限制因果追踪；**支撑 Scope**：可观测；**阅读深度**：读 context、span、sampling、links 与 attribute cardinality。
- [MLPerf Inference Benchmark](https://mlcommons.org/benchmarks/inference-datacenter/) — **选入理由**：MLPerf 用 Server/Offline Scenario、Accuracy Gate、LoadGen 和系统描述约束压测过程，可防止通过改变负载、精度或未披露资源获得不可比较的吞吐数字；**支撑 Scope**：压测、资源控制；**阅读深度**：读 server/offline scenario、accuracy、loadgen 与提交系统描述。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
