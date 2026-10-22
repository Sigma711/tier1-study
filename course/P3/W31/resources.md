# W31 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [MLIR Toy Tutorial](https://mlir.llvm.org/docs/Tutorials/Toy/) — **选入理由**：它围绕同一个 Toy 语言逐章加入 AST、Toy Dialect、shape inference、变换、lowering 和 LLVM codegen，天然提供一条可在每层打印 IR、运行 verifier 并比较语义的 Mini Compiler 基线；**支撑 Scope**：Mini AI Compiler 的 Frontend、Dialect、Lowering 主链；**阅读深度**：精读 Ch1–7 并把每层 verifier/产物列入考核。
- [MLIR Pass Management](https://mlir.llvm.org/docs/PassManagement/) — **选入理由**：它提供 textual pipeline、analysis preservation、IR printing、timing 与 instrumentation 的统一控制点，能把综合项目的每次变换、耗时和中间产物组织成可复核证据链；**支撑 Scope**：综合考核的 pass pipeline 与证据；**阅读深度**：精读 pipeline、analysis、instrumentation。
- [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html) — **选入理由**：向量加、融合 softmax 和矩阵乘三个教程逐步引入 program id、mask、片上复用、autotune 与基准对照，能检验 Mini Compiler 的 GPU backend 是否既生成正确 kernel 又解释得出性能差异；**支撑 Scope**：综合考核的 GPU kernel backend；**阅读深度**：精读向量加、softmax、matmul 的 program model 与性能测量，不要求手抄。
- [LLVM Testing Guide](https://llvm.org/docs/TestingGuide.html) — **选入理由**：它说明 `lit`、FileCheck、IR regression test 与不同测试层次如何验证精确编译产物，能把“结果能运行”提升为对 pass 行为和失败回归都可定位的测试体系；**支撑 Scope**：综合考核的可验证性；**阅读深度**：精读 IR/FileCheck、回归测试与测试层次。
