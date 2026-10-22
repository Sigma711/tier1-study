# W20 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [LLVM Kaleidoscope Tutorial](https://llvm.org/docs/tutorial/) — **选入理由**：它让同一门小语言依次获得 lexer/parser、AST、IRGen、优化 pass、JIT 与 object code，因此每章新增能力都能在相同输入上观察到前端表示和编译产物如何变化；**支撑 Scope**：Frontend、AST 与语义分析、IR、Optimizer、Backend；**阅读深度**：精读 Chapters 2–8：AST 类、语义错误、IRGen、pass 与 object code 边界。
- [Clang Internals Manual](https://clang.llvm.org/docs/InternalsManual.html) — **选入理由**：它把工业级 C/C++ 前端拆到 SourceManager、Lexer/Parser、AST、Sema 与诊断等真实子系统，能够揭示教程编译器刻意省略的源码位置保持、语义检查和恢复式诊断；**支撑 Scope**：真实 Frontend、AST、Sema；**阅读深度**：精读 parser/sema/AST 表示与 source location，不把 Clang 特例泛化为所有语言。
- [LLVM Language Reference](https://llvm.org/docs/LangRef.html) — **选入理由**：它逐条规定 LLVM IR 的类型、指令、Data Layout、poison/undef 与调用约定语义，是判断前端生成是否合法、后端可以做哪些假设时不可由教程替代的裁决依据；**支撑 Scope**：IR 语义与 Frontend/Backend 契约；**阅读深度**：精读 module/function/instruction、data layout 与未定义行为语义。
