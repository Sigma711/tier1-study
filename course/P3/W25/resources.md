# W25 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [MLIR Affine Dialect](https://mlir.llvm.org/docs/Dialects/Affine/) — **选入理由**：它用 affine map、integer set 和受限索引表达式把循环与访存变成可判定分析的数学对象，能解释依赖分析和循环变换为何需要比一般控制流更强的约束；**支撑 Scope**：Affine；**阅读深度**：精读 affine map/set、loop、load/store 与合法性限制。
- [MLIR SCF Dialect](https://mlir.llvm.org/docs/Dialects/SCFDialect/) — **选入理由**：它以 region 和 block argument 表达 `for`、`while`、`if`、`parallel` 的值传递，提供从高层结构化控制流向 CFG lowering 前最清晰的中间形态；**支撑 Scope**：SCF；**阅读深度**：精读 for/while/if/parallel 的 region 与 iteration arguments。
- [MLIR Linalg Dialect](https://mlir.llvm.org/docs/Dialects/Linalg/) — **选入理由**：它把算子计算与 indexing map、iterator type、destination-style operand 分离，使 tiling、fusion 和映射到硬件循环能够共享同一结构化表示，是本周变换主线不可替代的语义载体；**支撑 Scope**：Linalg、Tiling、Fusion；**阅读深度**：精读 structured ops、indexing maps、destination style 与 transform properties。
- [MLIR Bufferization](https://mlir.llvm.org/docs/Bufferization/) — **选入理由**：它详细说明 One-Shot Bufferize 如何依据 alias/equivalence 与读写冲突选择原地复用或分配新 buffer，直接连接 tensor SSA 语义、内存占用与复制成本；**支撑 Scope**：Bufferization；**阅读深度**：精读 One-Shot Bufferize、alias/equivalence、in-place analysis 与 ownership。
