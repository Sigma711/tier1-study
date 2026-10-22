# W57 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [vLLM Architecture](https://docs.vllm.ai/en/latest/design/arch_overview/) — **选入理由**：真实推理系统的数据面、控制面和 worker 接口官方设计；**支撑 Scope**：架构、接口、约束；**阅读深度**：读 engine、scheduler、KV cache、executor/worker 边界并标出容量假设。
- [MLPerf Inference Policies](https://docs.mlcommons.org/inference/index_gh/) — **选入理由**：MLPerf Policies 把 Scenario、延迟约束、准确率、System Description 和结果有效性写成统一规则，可将毕业项目的性能目标变成能被第三方复核的验收口径；**支撑 Scope**：需求、性能目标；**阅读深度**：读 scenario、latency constraint、accuracy、system description 与结果有效性。
- [Google SRE Service Level Objectives](https://sre.google/workbook/implementing-slos/) — **选入理由**：Google SRE 的方法从用户旅程导出 SLI、目标值和错误预算，能迫使毕业项目先说明“对谁可靠、在什么窗口内可靠”，再讨论架构与性能；**支撑 Scope**：毕业项目方案、需求、约束；**阅读深度**：读 user journey、SLI specification、目标/错误预算和边界条件。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
