# W02 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Agent Harness、Context Engineering、仓库规范、本地自动化验证与基准测试、C++/Python/Rust/Linux 系统编程、并发/内存模型/异步执行/性能分析、Agent Skills 与 MCP。

1. 分别说明 Agent Harness、Context Engineering、Skill 与 MCP 的职责和信任边界；为什么 Skill 不能等同 MCP tool？
2. 比较 C++ RAII、Rust ownership 与 Python GC 管理资源生命周期的保证和失效边界。
3. 用 happens-before 解释数据竞争，并说明线程池、Future/Coroutine 与 GPU stream 的异步语义为何不能混为一谈。
4. 一个 Agent 工作流中自动化比例为 80%，该部分加速 5 倍。用 Amdahl 定律计算总加速比，并解释上下文读取成本如何改变结论。
5. 设计本地验证与基准证据清单，覆盖 Linux 进程/内存证据、正确性、性能统计、MCP 权限和仓库安全；不得依赖 CI。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
