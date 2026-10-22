# W02 · Agent Harness、Context Engineering、仓库规范、自动化验证与基准测试

## 本课目的

围绕 **Agent Harness、Context Engineering、仓库规范、自动化验证与基准测试** 建立可用于高级 AI Infra 工程判断的知识模型。重点是理解原理、实现位置、性能边界和失效条件，不训练脱离 Agent 的机械操作熟练度。

## 固定 Scope

本课只覆盖以下已经确定的主题：

- Agent Harness
- Context Engineering
- 仓库规范
- 自动化验证与基准测试
- 系统编程基础：C++、Python、Rust 与 Linux
- 并发、内存模型、异步执行与性能分析
- Agent Skills 与 Model Context Protocol（MCP）

这些条目是本课内容边界。授课 Agent 可以补充解释、例子和一手证据，但不得新增课程主题、删除条目或把后续周内容提前替代本课。

## 掌握目标

- 能用自己的语言解释本课全部 Scope，说明各概念之间的因果关系。
- 能指出真实系统中承载这些机制的组件、源码位置或运行证据。
- 能说明关键性能、正确性、可靠性或成本权衡，以及至少一种失效条件。
- 能分别把本课知识连接到数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，并指出每个类比的失效边界。

## 高级工程师面试覆盖

- **原理与推导**：能用 Amdahl 定律 \(S=1/((1-p)+p/s)\) 判断 Agent 自动化上限，并解释 C++/Rust/Python 的对象生命周期、happens-before、异步队列及上下文窗口的容量约束。
- **源码与产物**：能审读 `AGENTS.md`、Skill `SKILL.md`、MCP tool/resource schema、C++ RAII、Rust ownership/async 和 Python native-extension 边界，并追到 Linux 进程、线程、fd 与虚拟内存证据。
- **性能与实验**：能设计本地可复验 Benchmark，固定输入、版本、并发、预热和统计口径，用 wall time、CPU、RSS、火焰图与异步时间线比较基线；不以 CI 作为课程设施。
- **正确性与故障**：能从编译器诊断、sanitizer、数据竞争、死锁、悬垂引用、event-loop 阻塞、上下文污染、MCP 权限越界和陈旧证据中建立最小复现。
- **系统设计与评审**：能划分人、Agent、Skill、MCP server 与本地验证的信任边界，权衡 C++ 性能、Rust 安全、Python 生产力和上下文成本。

## 与既有经验的连接

- **数据库内核**：Harness 的指令、工具与验证门像内核模块契约，C++/Rust 所有权经验可约束资源生命周期；失效于 LLM 输出是概率生成，不具备确定性执行计划。
- **存储引擎**：仓库版本、上下文来源与实验产物像 WAL/血缘，成立于可追溯和恢复；失效于 Git 历史不自动提供事务隔离或运行态一致性。
- **计算引擎**：Agent 任务图和异步 Future 像 DAG 调度，Benchmark 像算子微基准；失效于 Skill/MCP 编排本身不是代价优化器。
- **分布式系统**：MCP 能力协商、超时、幂等和最小权限可按 RPC 边界审查；失效于本地工具成功不代表远端副作用已达成一致。
- **可观测性**：日志、火焰图、系统调用与 Agent 工具记录可关联因果链；失效于缺少受控对照时，Trace 只能显示共现。

## 知识型学习产出

建立统一工程仓库、`AGENTS.md`、本地检查、实验记录与 Agent 工作流

涉及实现、命令、部署、Benchmark 或 Profiling 的部分，由 Coding Agent 执行并保存证据；学习者负责阅读、质疑、解释和形成技术判断。不得改造成要求学习者反复进行机械操作的训练。

## 本课资料

- [知识笔记](notes.md)
- [固定学习资料](resources.md)
- [简短 Quiz](quiz.md)
- [学习记录](record.md)

## 所属阶段

[P0：学习环境、Agent 工程规范与能力基线](../README.md)
