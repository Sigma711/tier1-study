# W30 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [Triton Compiler source](https://github.com/triton-lang/triton/tree/c1641abbb17a80b8c9cad1fa05b4c70d6ac260ab/lib) — **选入理由**：固定 revision 的 `lib` 目录同时包含 TTIR/TTGIR dialect、conversion pass 与目标 backend，可把每次 IR dump 对应到实际 lowering 代码，验证 layout 与硬件映射在哪一层形成；**支撑 Scope**：Triton Compiler、TTIR/TTGIR；**阅读深度**：精读 dialect、conversion 与 target backend 目录，结合 dump 对照。
- [NVIDIA PTX ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/) — **选入理由**：它逐条定义 PTX 执行模型、寄存器与各 state space、指令语义和 target feature 要求，是判断 Triton/LLVM 生成 PTX 是否语义合法且能在目标架构汇编的最终依据；**支撑 Scope**：PTX；**阅读深度**：精读 execution model、state spaces、instructions 与 target compatibility。
- [OpenXLA XLA architecture](https://openxla.org/xla/architecture) — **选入理由**：它以 HLO 为中心串起前端输入、图级优化、buffer assignment 与平台 backend，适合与 Triton 的 kernel-centric lowering 比较优化粒度和部署边界；**支撑 Scope**：XLA；**阅读深度**：精读 HLO、compiler pipeline 与 backend 边界。
- [StableHLO specification](https://openxla.org/stablehlo/spec) — **选入理由**：它为 StableHLO 每个 op 规定输入输出、shape constraints、类型规则和 compatibility 承诺，解释可序列化的稳定交换 IR 如何区别于持续演进的优化 IR；**支撑 Scope**：StableHLO；**阅读深度**：精读 op semantics、types、verification 与 compatibility。
- [IREE Developer Overview](https://iree.dev/developers/general/developer-overview/) — **选入理由**：它把 Flow、Stream、HAL、Codegen 与 runtime/HAL 放进同一部署链，展示 tensor program 如何变成设备命令、资源生命周期和可移植 runtime 调用，补足只看编译器 pass 无法看到的执行端；**支撑 Scope**：IREE；**阅读深度**：精读 compiler 中 Flow/Stream/HAL dialect、Codegen 与 runtime/HAL 的代码边界和部署目标。
- [TVM TensorIR](https://tvm.apache.org/docs/deep_dive/tensor_ir/index.html) — **选入理由**：它把 loop/block 计算表示与 schedule primitive 明确分离，使同一 TensorIR 程序能通过变换生成不同实现，是对照 MLIR rewrite 与 Triton 隐式调度时最有辨识度的路线；**支撑 Scope**：TVM 对照；**阅读深度**：精读 TensorIR 表示、schedule 与 lowering，对照而不混同各栈。
