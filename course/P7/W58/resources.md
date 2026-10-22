# W58 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [PyTorch 2 Compiler Architecture](https://docs.pytorch.org/docs/stable/torch.compiler_dynamo_deepdive.html) — **选入理由**：TorchDynamo graph capture/guards 的官方深度文档；**支撑 Scope**：Compiler、真实执行路径；**阅读深度**：读 frame evaluation、FX graph、guards、graph breaks 并跟到源码对象。
- [TorchInductor](https://docs.pytorch.org/docs/stable/torch.compiler_inductor_profiling.html) — **选入理由**：官方说明 Inductor 生成代码与 profiling 证据；**支撑 Scope**：选择执行路径进行优化；**阅读深度**：读 generated code、coordinate-descent tuning、kernel profiling 与回退。
- [Triton Compiler](https://github.com/triton-lang/triton/tree/c1641abbb17a80b8c9cad1fa05b4c70d6ac260ab) — **选入理由**：固定 revision 的 Triton 编译器能把一个真实算子从 Frontend AST 一路追到 Triton IR、MLIR、LLVM/PTX，使优化前后的 IR、合法性和生成代码都有同一源码基线；**支撑 Scope**：Compiler、真实算子优化；**阅读深度**：沿 frontend AST、Triton IR/MLIR lowering 到 LLVM/PTX，不以示例性能代替端到端证据。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
