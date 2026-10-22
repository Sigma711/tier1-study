# W26 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [MLIR Dialect Conversion](https://mlir.llvm.org/docs/DialectConversion/) — **选入理由**：它把合法/非法 Operation、rewrite pattern、TypeConverter 与 source/target materialization 组合成可验证的 lowering 算法，并明确 full、partial、analysis conversion 的不同完成条件；**支撑 Scope**：Dialect Conversion；**阅读深度**：精读 ConversionTarget、TypeConverter、materialization 与 full/partial conversion。
- [MLIR LLVM Dialect](https://mlir.llvm.org/docs/Dialects/LLVM/) — **选入理由**：它说明 LLVM IR 的指针、聚合、调用约定和 Data Layout 如何先在 MLIR 中获得可转换表示，再跨越 translation 边界生成 LLVM IR，避免把 dialect lowering 误解为文本改写；**支撑 Scope**：LLVM Lowering；**阅读深度**：精读 LLVM-compatible types/ops、data layout 与 translation 边界。
- [MLIR GPU Dialect](https://mlir.llvm.org/docs/Dialects/GPU/) — **选入理由**：它同时表示 host 侧 `gpu.launch`、device 侧 `gpu.module`、层级 ID、内存空间与异步 token，并给出通往 NVVM/ROCDL 的路径，能完整追踪 GPU CodeGen 的主客机分界；**支撑 Scope**：GPU CodeGen；**阅读深度**：精读 gpu.module/launch、memory spaces 与 NVVM/ROCDL lowering 路径。
