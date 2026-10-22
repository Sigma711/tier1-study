# W23 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [MLIR Language Reference](https://mlir.llvm.org/docs/LangRef/) — **选入理由**：它定义 Operation 如何嵌套 Region/Block、block argument 如何参与 SSA，以及 Type/Attribute 如何承载可扩展语义，是理解 MLIR 为何能容纳多层 IR 的根本文档；**支撑 Scope**：MLIR、Operation、Region、Block、Type、Attribute；**阅读深度**：精读 IR structure、SSA、regions/blocks、types/attributes。
- [MLIR Defining Dialects](https://mlir.llvm.org/docs/DefiningDialects/) — **选入理由**：它从 dialect registration 一直讲到 TableGen 生成的 C++ 定义，展示新语义如何注册进 MLIR，而不是只停留在手写 Operation 的概念示例；**支撑 Scope**：Dialect 与 ODS；**阅读深度**：精读 dialect registration、operation definition 与 generated C++。
- [MLIR Operation Definition Specification](https://mlir.llvm.org/docs/DefiningDialects/Operations/) — **选入理由**：它逐项说明如何在 ODS 中声明 operands/results、regions、traits、builders、parser/printer 与 verifier，能够把一条 operation 定义追到生成代码和静态约束；**支撑 Scope**：ODS、Operation、Type/Attribute constraints；**阅读深度**：精读 arguments/results/regions、traits、builders、parsers 与 verifier。
