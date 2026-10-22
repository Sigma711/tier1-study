# W46 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [GPipe](https://arxiv.org/abs/1811.06965) — **选入理由**：microbatch pipeline 与 bubble 分析的原论文；**支撑 Scope**：Pipeline Parallelism、Microbatch、GPipe、Pipeline Bubble；**阅读深度**：推导 bubble/激活模型，读 batch-splitting 与实验限制。
- [PipeDream-Flush](https://arxiv.org/abs/2006.09503) — **选入理由**：PipeDream-Flush 论文给出 1F1B 调度时序、Flush 语义与 Activation Memory 分析，能从流水线图直接推导 Bubble 和一致参数版本之间的交换；**支撑 Scope**：1F1B、Pipeline Bubble；**阅读深度**：读 schedule、activation memory、flush 与同步语义。
- [PyTorch Pipeline Parallelism](https://pytorch.org/docs/stable/distributed.pipelining.html) — **选入理由**：stage、microbatch 与 schedule 的官方实现；**支撑 Scope**：Pipeline Parallelism、Microbatch、GPipe、1F1B；**阅读深度**：读 PipelineStage、ScheduleGPipe、Schedule1F1B、shape contract 与 send/recv。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
