# AI Systems, Compilers & Infrastructure Engineering

高级 AI Infrastructure 工程师系统课程 · 64 周主课程 · 2026 年 10 月版

这是一个纯粹的学习与记录仓库。课程范围已经固定，目标是以系统知识、论文、源码和工程证据支撑 AI Infra 高级工程师技术面与真实工作；不以大量手工操作训练为中心。

## 从这里开始

- [课程使命与完成标准](MISSION.md)
- [64 周课程总览](course/README.md)
- [学习进度](PROGRESS.md)
- [全局学习资料](RESOURCES.md)
- [教学与学习约定](NOTES.md)

## 八个阶段

- [P0：学习环境、Agent 工程规范与能力基线](course/P0/README.md) — W01–W02
- [P1：AI 计算基础与现代模型架构](course/P1/README.md) — W03–W09
- [P2：GPU Architecture、CUDA 与高性能 Kernel](course/P2/README.md) — W10–W19
- [P3：编译器原理与 AI Compiler 内核](course/P3/README.md) — W20–W31
- [P4：LLM Inference Runtime 与 Serving Systems](course/P4/README.md) — W32–W41
- [P5：Distributed Training 与 GPU Communication](course/P5/README.md) — W42–W49
- [P6：AI Data、GPU Cluster 与生产级基础设施](course/P6/README.md) — W50–W56
- [P7：综合毕业项目与高级工程师面试](course/P7/README.md) — W57–W64

## 资料与成果

- [核心论文](references/papers.md)
- [开源项目 Git 引用](references/projects.yaml)
- [五项渐进式工程研究](projects/README.md)
- [16 周可选专精](specializations/README.md)

每课独立目录包含固定 Scope、知识笔记、固定资料、简短 Quiz 和学习记录。需要实现、命令、测试、Benchmark 或 Profiling 时，由 Coding Agent 执行并保存证据；学习者负责理解、审查、解释和决策。

本仓库不配置 GitHub Actions 或其他 CI/CD。结构与链接使用本地命令 `python3 scripts/check_course.py` 检查。

## License

[MIT](LICENSE)
