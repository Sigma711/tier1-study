# W27 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [MLIR Shape Inference](https://mlir.llvm.org/docs/ShapeInference/) — **选入理由**：它围绕 `InferTypeOpInterface` 展示 Operation 如何从 operand 推出 result shape、传播约束并报告不一致，使 shape inference 从“猜尺寸”变成可组合的编译期证明步骤；**支撑 Scope**：Shape Inference；**阅读深度**：精读 inference interface、constraints 与 error propagation。
- [MLIR Shape Dialect](https://mlir.llvm.org/docs/Dialects/ShapeDialect/) — **选入理由**：它用 `size`、`shape`、`witness`、`cstr_*` 与 `assuming` 显式表示运行期尺寸和约束成立性，提供静态 tensor type 无法表达的符号形状推理与守卫机制；**支撑 Scope**：动态形状、符号维度；**阅读深度**：精读 size/shape/witness 与 assuming/cstr ops。
- [MLIR Builtin Dialect](https://mlir.llvm.org/docs/Dialects/Builtin/) — **选入理由**：它并列定义 ranked/unranked tensor、memref、动态维标记、stride 与 affine layout map，能够精确区分逻辑 Tensor Shape 和实际 Buffer Layout；**支撑 Scope**：Tensor Layout 与动态维；**阅读深度**：精读 tensor/memref types、dynamic dimensions、strides 与 layout maps。
- [MLIR Bufferization](https://mlir.llvm.org/docs/Bufferization/) — **选入理由**：它把 tensor 到 memref 的选择与 buffer ownership、deallocation、alias 冲突和复用机会联系起来，是从形状/布局信息推导实际内存生命周期与峰值占用的关键资料；**支撑 Scope**：内存规划；**阅读深度**：精读 buffer 生命周期、deallocation/ownership 与复用约束。
