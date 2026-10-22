# W56 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [Google SRE Implementing SLOs](https://sre.google/workbook/implementing-slos/) — **选入理由**：Google SRE Workbook 从 User Journey 推到 SLI 规格、统计窗口和 Error Budget Policy，能把抽象可靠性目标落成可决策、可复盘的服务合同；**支撑 Scope**：SLO；**阅读深度**：读 user journey、SLI specification、window 与 error budget policy。
- [MLPerf Inference](https://mlcommons.org/benchmarks/inference-datacenter/) — **选入理由**：其流量场景、延迟约束、准确率门槛和 system description 为容量模型提供可比的吞吐与硬件基线，但它不单独证明成本；**支撑 Scope**：容量规划、成本模型的性能输入；**阅读深度**：读 server/offline scenario、LoadGen 与 system description；仅计算 tokens/s、tokens/s/GPU 等容量指标，成本还须显式引入采购或租赁价格、功耗、折旧、利用率、运维和时间窗口，并做敏感性分析。
- [AWS Cost Modeling](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/cost-modeling.html) — **选入理由**：它把资源用量、费率、利用率与业务单位成本组织成显式假设，补足性能基准不能提供的财务输入；**支撑 Scope**：成本模型；**阅读深度**：建立 `单位成本 = 时间窗口内总拥有成本 / 有效 token`，分别列出租赁或折旧、功耗、网络、存储、运维、空闲容量与失败重算，并对利用率和价格做敏感性分析。
- [Kubernetes HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) — **选入理由**：HPA 文档给出 Desired Replicas 公式以及 Missing Metrics、Tolerance 和 Stabilization 的具体处理，能解释为何指标正确也可能出现扩缩容迟滞或振荡；**支撑 Scope**：弹性伸缩；**阅读深度**：读 desired replicas 公式、missing metrics、tolerance、stabilization 与模型冷启动差距。
- [Chaos Mesh](https://chaos-mesh.org/docs/) — **选入理由**：Chaos Mesh 把 Pod、Network 等故障的目标选择、持续时间、工作流与终止恢复条件声明化，可用来审查故障实验是否受控、是否留下可证明的恢复证据；**支撑 Scope**：故障注入与恢复；**阅读深度**：读 workflow/experiment scope、network/pod fault、安全边界与终止恢复证据。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
