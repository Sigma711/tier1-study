# W22 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [LLVM Language Reference](https://llvm.org/docs/LangRef.html) — **选入理由**：它是 LLVM IR 每种类型和指令的权威语义表，尤其能用 poison、undef、属性和 Data Layout 解释为什么看似等价的优化可能改变程序含义；**支撑 Scope**：LLVM IR；**阅读深度**：精读 SSA、类型、data layout、poison/undef。
- [LLVM New Pass Manager](https://llvm.org/docs/NewPassManager.html) — **选入理由**：它专门解释 AnalysisManager 的结果缓存、preservation/invalidation 与嵌套 pass pipeline，正好回答优化序列如何复用分析以及变换后为何必须使旧结论失效；**支撑 Scope**：Optimization Pass；**阅读深度**：精读 analysis manager、pipeline 与 invalidation。
- [LLVM Code Generator](https://llvm.org/docs/CodeGenerator.html) — **选入理由**：它连续呈现从 IR legalization、指令选择、Machine IR、寄存器分配到 MC emission 的后端阶段，可用来定位目标相关约束究竟在哪一步进入编译结果；**支撑 Scope**：CodeGen；**阅读深度**：精读 instruction selection、legalization、register allocation、MC。
- [LLVM ORC JIT](https://llvm.org/docs/ORCv2.html) — **选入理由**：它以 JITDylib、MaterializationUnit、ExecutionSession 和 layer 说明按需编译、符号解析与并发 materialization，提供静态 object emission 文档无法覆盖的运行时编译视角；**支撑 Scope**：JIT/AOT 对照中的 JIT；**阅读深度**：精读 layers、materialization、symbols 与并发；AOT 对照回到 object emission。
