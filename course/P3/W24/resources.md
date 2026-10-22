# W24 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [MLIR Pattern Rewriting](https://mlir.llvm.org/docs/PatternRewriter/) — **选入理由**：它规定匹配、原位更新、替换和删除必须经 PatternRewriter 完成，并解释 pattern benefit、递归许可与 greedy 收敛风险，是判断 rewrite 是否安全终止的核心资料；**支撑 Scope**：Pattern Rewrite；**阅读深度**：精读 RewritePattern、PatternRewriter、benefit 与递归/收敛约束。
- [MLIR Canonicalization](https://mlir.llvm.org/docs/Canonicalization/) — **选入理由**：它区分全局 canonicalizer 行为、局部 `fold` hook 与声明式 canonicalization pattern，能够解释“规范形”如何形成以及为何 canonicalization 不等同于任意优化；**支撑 Scope**：Canonicalization；**阅读深度**：精读全局规则、fold 与 canonicalization patterns。
- [MLIR Pass Management](https://mlir.llvm.org/docs/PassManagement/) — **选入理由**：它展示 pass 如何锚定在不同 Operation 层级、如何组装 textual pipeline、保存分析并插入 instrumentation，是复原真实变换顺序与测量每个 pass 的唯一主线；**支撑 Scope**：Pass Manager；**阅读深度**：精读 operation pass、pipeline、analysis preservation 与 instrumentation。
- [MLIR CSE source](https://github.com/llvm/llvm-project/blob/0b5e65f208f29e5b676a605b1e485d03722100d9/mlir/lib/Transforms/CSE.cpp) — **选入理由**：这份固定 revision 的实现直接展示等价 Operation 的哈希查找、作用域隔离、dominance 与 memory-effect 判断如何共同决定能否消除重复计算，细节无法从 CSE 定义本身推出；**支撑 Scope**：CSE；**阅读深度**：精读等价查找、作用域、side effects 与 dominance。
- [MLIR Symbol DCE source](https://github.com/llvm/llvm-project/blob/0b5e65f208f29e5b676a605b1e485d03722100d9/mlir/lib/Transforms/SymbolDCE.cpp) — **选入理由**：这份实现以 SymbolTable 可见性和引用图计算活跃 symbol，再执行删除，清楚揭示 Symbol DCE 与普通“无 use 的 op 即删除”之间的语义差别；**支撑 Scope**：DCE；**阅读深度**：精读可达 symbol 收集与删除条件；同时区分一般 op DCE。
