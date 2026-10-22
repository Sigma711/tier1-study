# W64 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [Google Machine Learning Rules](https://developers.google.com/machine-learning/guides/rules-of-ml) — **选入理由**：Google 的实践规则覆盖目标定义、数据管线、Serving、监控和系统演进，每条都能转成带假设与反例的系统设计追问，适合作为面试答辩的工程检查表；**支撑 Scope**：高级技术面试模拟、系统设计；**阅读深度**：把每条规则转成可追问的假设、指标与失败边界。
- [PyTorch Developer Notes](https://docs.pytorch.org/docs/stable/notes.html) — **选入理由**：把 autograd、CUDA、数值精度与分布式的用户可见行为连接到实现约束，是从现象选择源码入口、建立证据链的官方索引；**支撑 Scope**：源码分析；**阅读深度**：选定问题后追到对应源码对象和运行证据，禁止只背 API。
- [MLPerf Inference Results](https://mlcommons.org/benchmarks/inference-datacenter/) — **选入理由**：公开结果把硬件、软件、场景、精度与性能放在同一披露框架里，是项目答辩时展示可复现证据和指出不可横比条件的范本；**支撑 Scope**：项目答辩、系统设计；**阅读深度**：审查 system description、accuracy、latency/throughput 与不可横比条件。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
