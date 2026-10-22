# W18 · 固定学习资料

> 资料状态核验：2026-10-22。

- [Nsight Systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html) — **选入理由**：官方工具从进程/线程到 CUDA 时间线定位端到端热点；**支撑 Scope**：Nsight Systems；**阅读深度**：精读 CUDA trace、NVTX、sampling 与 perturbation，先回答“时间花在哪”。
- [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) — **选入理由**：官方工具解释 Kernel counter、section 与 replay；**支撑 Scope**：Nsight Compute；**阅读深度**：读 collection/replay、SpeedOfLight、MemoryWorkloadAnalysis、Occupancy 及指标限制。
- [Roofline: An Insightful Visual Performance Model](https://dl.acm.org/doi/10.1145/1498765.1498785) — **选入理由**：CACM 原论文定义 arithmetic intensity 与性能屋顶；**支撑 Scope**：Roofline；**阅读深度**：精读 operational intensity、ridge point、ceilings，能手算上界且不把模型当实测。
- [PTX ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/) — **选入理由**：PTX ISA 定义虚拟指令、State Space、Target Feature 和版本兼容规则，是区分编译器中间汇编与最终 SASS、判断生成代码是否合法的权威来源；**支撑 Scope**：PTX；**阅读深度**：读 ISA model、state spaces、instructions 与 target features，明确 PTX 不是最终机器码。
- [CUDA Binary Utilities](https://docs.nvidia.com/cuda/cuda-binary-utilities/) — **选入理由**：官方 `cuobjdump`/`nvdisasm` 文档用于读取真实 SASS；**支撑 Scope**：SASS；**阅读深度**：读 cubin/fatbin、disassembly、source line mapping，并把 SASS 与 profiler 对齐。
- [OpenTuner](https://dl.acm.org/doi/10.1145/2628071.2628092) — **选入理由**：PACT 论文系统讨论 program autotuning 搜索；**支撑 Scope**：自动调优；**阅读深度**：精读 search ensemble、objective/evaluation 与 benchmark suite，迁移到 Kernel 时增加正确性门与留出 Shape。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
