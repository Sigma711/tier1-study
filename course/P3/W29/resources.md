# W29 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [AOTAutograd documentation](https://docs.pytorch.org/functorch/stable/notebooks/aot_autograd_optimizations.html) — **选入理由**：它展示 AOTAutograd 如何把 eager autograd 追踪为 joint forward/backward graph，再由 partitioner 决定重算与 saved tensors，为理解反向图为何能交给编译器优化提供完整桥梁；**支撑 Scope**：AOTAutograd；**阅读深度**：精读 joint graph、partitioner、saved tensors 与编译边界。
- [TorchInductor CPU backend debug tutorial](https://docs.pytorch.org/tutorials/intermediate/inductor_debug_cpu.html) — **选入理由**：它从一个可运行 CPU 模型逐层导出 FX graph、Inductor IR、生成代码和 profiling 工件，能够把性能异常反查到具体 scheduler/codegen 决策，而不依赖 GPU 环境掩盖编译流程；**支撑 Scope**：TorchInductor、Code Generation；**阅读深度**：精读 FX/Inductor IR、generated code 与 profiling 工件。
- [TorchInductor GPU profiling](https://docs.pytorch.org/docs/stable/torch.compiler_inductor_profiling.html) — **选入理由**：它把 Inductor 生成的 Triton kernel 名称、fusion 分组和 GPU profiler 时间线对齐，能够用实际 launch 数、内核耗时与访存行为验证“发生了融合”是否真的带来收益；**支撑 Scope**：Kernel Fusion 与性能证据；**阅读深度**：精读 generated Triton kernels、fusion 与 profiler 对照。
- [PyTorch Compiler Caching](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_configuration_tutorial.html) — **选入理由**：它集中列出 Dynamo、AOTAutograd、Inductor 等内存/磁盘/远端缓存层及配置方式，使首次编译、跨进程复用和失效重编译能够按 cache key 与命中层次分别分析；**支撑 Scope**：编译缓存；**阅读深度**：精读 in-memory/on-disk/remote cache 层次、key 与失效边界。
