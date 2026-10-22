# AGENTS.md

## 不可违背的课程边界

本仓库只服务于 **AI Infrastructure 高级工程师系统课程的学习与记录**。课程结构已经确定为 `course/` 中的 P0–P7、W01–W64；每课 `README.md` 的“固定 Scope”就是该课唯一内容边界。

- 不得新增、删除、合并、拆分、调序或改名阶段、周次和 Scope 条目。
- 不得让未来 Agent 根据概率重新生成课程范围。
- 不得在仓库落地 PRD、ADR、RFC、需求单、任务票、上下文转储或其他过程性设计文档。
- 不得创建要求学习者大量手写代码、手敲命令、手工部署或反复调参的操作课程。
- 不得创建 GitHub Actions、流水线配置或任何 CI/CD 设施。本仓库仅做本地检查。

## 课程使命

目标是帮助学习者正式进入 AI Infra 领域并胜任相关高级工程师岗位的完整技术面，覆盖 AI Compiler、GPU Computing、LLM Inference Runtime、Distributed Training、AI Data/Storage、GPU Cluster、Observability 与 Agent-Native Engineering。

教学必须主动连接学习者已有的数据库内核、存储引擎、计算引擎、分布式系统和可观测性经验，同时明确类比何时成立、何时失效。

以下是逐课都必须满足的硬性验收条件，而不是课程愿景：

- 所有相关知识的深度和广度必须能够支撑学习者通过对应领域高级工程师的全部技术面试。
- 每课都必须覆盖原理与定量推导、真实源码或编译产物、性能模型与证据、正确性与失效分析、系统设计与技术评审；不得只讲概念名词。
- 每课都必须分别连接数据库内核、存储引擎、计算引擎、分布式系统、可观测性五类既有经验，并写明类比成立与失效之处；不得用一句笼统的“联系已有知识”敷衍。
- 如果某课的固定 Scope、面试覆盖或五类经验连接缺失，该课即视为未初始化完成，禁止开始正式授课。

## 唯一允许的 skills

只允许使用本机 `/Users/sigma711/.agents/skills/` 中属于 `mattpocock/skills` 的 skill；不得调用其他来源的 skill。每项任务开始前必须选择并完整阅读适用的 Matt Pocock `SKILL.md`，不得只凭名称猜测工作流。

- 入口与选路：`ask-matt`、`find-skills`。
- 需求澄清与建模：`grill-me`、`grilling`、`grill-with-docs`、`brainstorming`、`domain-modeling`；这些工作流只能用于对话和内部推理，不得在仓库产生过程性设计文档。
- 调研与教学：`research`、`teach`。
- 实现与验证：`implement`、`tdd`、`test-driven-development`、`systematic-debugging`、`diagnosing-bugs`、`code-review`、`requesting-code-review`、`receiving-code-review`、`verification-before-completion`。
- 架构、执行与协作：`codebase-design`、`improve-codebase-architecture`、`executing-plans`、`dispatching-parallel-agents`、`subagent-driven-development`、`finishing-a-development-branch`、`resolving-merge-conflicts`、`using-git-worktrees`、`writing-for-agents`、`writing-plans`、`writing-skills`、`writing-great-skills`。
- 其他 Matt Pocock skill 仅在任务确实匹配时使用，不得为了“走流程”制造文件或工作量。

无条件禁止 `superpowers`、`using-superpowers` 和全部 `gstack*` skill；不得以更高效率、兼容入口或历史惯例为理由启用。不得使用已卸载的独立 GrillMe 插件。

## 授课风格

- 默认中文；重要术语首次出现时给出英文。
- 去 AI 味、小白向、生动形象、深入浅出、全面、成体系、专业、文采飞扬；同时简单明了、不啰嗦、不冗余，直接讲述给学习者听。
- 直接讲知识，不以连续追问、角色扮演、闯关或高互动练习代替教学。
- 每个概念依次说明：直觉、严格定义、运行机制、真实实现、关键权衡、失效条件、与既有经验的连接。
- 学术与工程品味必须好。教学使用的论文与著名开源项目必须较新或公认经典、质量高、持续活跃，并具有明确的学界或业界热度；优先顶级会议论文原文、官方文档、官方仓库和源码，禁止用聚合转载、营销软文或低质量二手教程替代一手材料。
- 每课资料必须说明它为何值得学、支撑哪个 Scope、阅读到什么深度；论文结论必须与当前项目源码和实际证据区分开。
- 对易变事实先核验当前状态，并在笔记中记录核验日期；不得把过期资料写成当前事实。

## Agent-Oriented 学习方式

课程以知识掌握为中心，不培养脱离 Agent 的机械操作熟练度。

- Coding Agent 负责检索、源码导航、实现、命令执行、环境操作、测试、Benchmark、Profiling、数据整理和证据保存。
- 学习者负责理解原理、复述机制、审查源码与原始证据、识别错误、解释因果、比较取舍、做技术决策和完成答辩。
- `quiz.md` 只能是简短知识检索题、推导题、源码理解题或系统判断题，不得变成操作任务。
- 必需的工程研究应由 Agent 完成操作并交付可复验证据；学习者不需要亲手重复全部步骤。
- Agent 产出代码不等于正确，正确不等于高性能，高性能不等于测量可信。结论必须能追溯到一手来源、源码、测试或原始测量。

## 每课目录契约

每个 `course/P*/W*/` 目录固定包含且只围绕以下五个文件学习：

- `README.md`：本课目的、固定 Scope、掌握目标和知识型产出；
- `notes.md`：正式知识笔记；
- `resources.md`：预先固定的一手资料；
- `quiz.md`：简短知识 Quiz；
- `record.md`：理解状态、证据和复习记录。

授课 Agent 可以在固定 Scope 内补充解释、示例、图示和经核验的资料，但不得改变课程边界。发现资料链接失效或项目演进时，只更新引用与版本说明。

每课 `README.md` 必须同时保留“高级工程师面试覆盖”和“与既有经验的连接”两节；本地检查器必须逐课验证，禁止只在课程总览里声明一次。

## Git 与公开安全

- 仓库公开并采用 MIT License。禁止提交凭据、内部地址、专有资料、个人数据、公司代码或不可公开的数据。
- 第三方项目在 `references/projects.yaml` 记录官方 Git URL 和固定 commit/tag；需要源码时使用 Git submodule，不复制上游源码快照。
- 不提交模型权重、数据集副本、构建产物、巨型 Profiler 报告或其他不可审查的大文件；只记录可重建方法、关键结果和校验值。
- 性能数字必须同时记录硬件、软件版本、模型、精度、Shape/长度、并发、预热与统计口径。
- 完成前必须运行 `python3 scripts/check_course.py`，检查 `git diff`，确认无敏感信息，并用 Matt Pocock `verification-before-completion` 完成新鲜验证。
