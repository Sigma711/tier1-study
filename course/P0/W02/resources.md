# W02 · 固定学习资料

> 资料状态核验：2026-10-22。GitHub 条目只陈述本日核验到的仓库与文件，不无日期声称“当前/活跃”。

- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/) — **选入理由**：官方工程文章具体讨论 repository、feedback loop 与 Agent legibility；**支撑 Scope**：Agent Harness、仓库规范、本地自动化验证；**阅读深度**：精读 harness 边界、validation 与 architecture constraint，提取可在本仓本地复验的原则。
- [Anthropic Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — **选入理由**：模型厂商工程文档具体分析 context selection/compaction；**支撑 Scope**：Context Engineering；**阅读深度**：读 context rot、just-in-time retrieval、compaction 与 sub-agent context，能够给出 token/信息损失取舍。
- [Matt Pocock skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2) — **选入理由**：该固定 revision 展示本课程唯一允许使用的 Skill 如何用 frontmatter、触发条件、步骤和验证门组成可审查工作流，是核对仓库 Agent 约束能否真正执行的直接样本；**支撑 Scope**：Agent Skills；**阅读深度**：精读一个 `SKILL.md` 的 frontmatter、触发条件、步骤与验证门，区分工作流说明和可执行工具。
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/latest) — **选入理由**：协议官方规范定义 host/client/server 与 primitives；**支撑 Scope**：MCP；**阅读深度**：精读 lifecycle、capability negotiation、tools/resources/prompts 与 security，能画出信任边界。
- [C++ Core Guidelines: Resource Management](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-resource) — **选入理由**：ISO C++ 社区权威指南具体覆盖 RAII 和 ownership；**支撑 Scope**：C++ 系统编程、内存管理；**阅读深度**：精读 R.1–R.6、R.20–R.24，并对照 native extension 生命周期。
- [Python C API: Memory Management](https://docs.python.org/3/c-api/memory.html) — **选入理由**：这份 C API 文档区分 Raw、Mem、Object 三类 allocator domain，并明确线程状态与成对释放约束，补足高层 Python 教程看不到的真实内存安全边界；**支撑 Scope**：Python 系统编程、内存管理；**阅读深度**：精读 allocator domains、PyMem/PyObject API 与 thread-state 边界。
- [The Rustonomicon: Concurrency](https://doc.rust-lang.org/nomicon/concurrency.html) — **选入理由**：Rust 官方书解释 Send/Sync、数据竞争与底层内存安全；**支撑 Scope**：Rust、并发与内存模型；**阅读深度**：精读 races、Send/Sync 和 atomics 相关章节，区分类型保证与逻辑死锁。
- [Linux man-pages](https://www.kernel.org/doc/man-pages/) — **选入理由**：Linux kernel.org 官方手册是 syscall/process/thread/fd/VM 的一手语义来源；**支撑 Scope**：Linux 系统编程；**阅读深度**：结合 `clone(2)`、`mmap(2)`、`epoll(7)`、`proc(5)` 阅读生命周期与观测接口。
- [C++ working draft: Multi-threaded executions and data races](https://eel.is/c++draft/intro.races) — **选入理由**：直接给出 C++ 标准草案对 sequenced-before、happens-before、conflict 与 data race 的规范定义，是判断并发程序合法性的首要语义依据；**支撑 Scope**：并发、内存模型；**阅读深度**：精读 happens-before、visible side effect 与 data race，能解释原子不自动解决复合不变量。
- [Python asyncio](https://docs.python.org/3/library/asyncio.html) — **选入理由**：官方库文档定义 event loop、Task、Future 与同步原语；**支撑 Scope**：异步执行；**阅读深度**：精读 event loop、Task cancellation、thread interaction，识别阻塞调用和取消泄漏。
- [Linux perf Wiki](https://perfwiki.github.io/main/) — **选入理由**：perf 官方维护文档覆盖采样、counter 与火焰图证据来源；**支撑 Scope**：性能分析、基准测试；**阅读深度**：读 sampling、stat/record/report 与 call graph，区分 CPU time、wall time 和采样偏差。
- [Google Benchmark User Guide](https://google.github.io/benchmark/user_guide.html) — **选入理由**：Google Benchmark 把重复次数、计时口径、自定义 Counter 和复杂度拟合变成显式配置，能把“跑得更快”收敛为本地可复验的测量协议；**支撑 Scope**：本地自动化验证与基准测试；**阅读深度**：精读 repetitions、time unit、counters、complexity 与 pitfalls，产出可复验本地证据而非 CI 配置。

如链接或项目状态变化，只更新引用与版本说明，不改变固定 Scope。
