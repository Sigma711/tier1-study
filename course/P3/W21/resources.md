# W21 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [LLVM Language Reference: Functions and SSA](https://llvm.org/docs/LangRef.html) — **选入理由**：它精确定义 basic block 必须以 terminator 结束、phi 的前驱对应关系以及 SSA use-def 约束，使 CFG 与 SSA 的推导能直接接受 LLVM verifier 语义检验；**支撑 Scope**：CFG、SSA 与 phi；**阅读深度**：精读 basic block、terminator、phi 与 dominance 约束。
- [LLVM DominatorTree documentation](https://llvm.org/doxygen/classllvm_1_1DominatorTree.html) — **选入理由**：它展示 LLVM 如何表示 dominator tree、回答支配查询并在 CFG 边增删后增量维护结果，能把教科书定义连接到优化 pass 真正依赖的数据结构与更新代价；**支撑 Scope**：Dominance；**阅读深度**：追到 GenericDomTree 与更新接口，理解查询/维护边界。
- [LLVM Data-Flow Analysis](https://clang.llvm.org/docs/DataFlowAnalysisIntro.html) — **选入理由**：它用格、转移函数、不动点迭代和 widening 的完整例子推导 Clang 数据流分析，并把变量活跃性放进同一求解框架，适合检验分析为何收敛以及精度在哪里丢失；**支撑 Scope**：Dataflow 与 Liveness；**阅读深度**：精读格、不动点、widening 与活跃性示例。
- [LLVM Alias Analysis](https://llvm.org/docs/AliasAnalysis.html) — **选入理由**：它把 NoAlias/MayAlias/MustAlias 与 ModRef 查询、分析组合及保守回退放在 LLVM 优化流水线中解释，是理解别名不确定性如何限制变换合法性的直接依据；**支撑 Scope**：Alias Analysis；**阅读深度**：精读 AliasResult、ModRef 与保守分析链。
