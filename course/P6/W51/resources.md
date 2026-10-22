# W51 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [Safetensors Format（固定 commit）](https://github.com/huggingface/safetensors/tree/e246a2560645b7525f5775669ed816eb57c5bcc8) — **选入理由**：模型权重的文件布局、offset 校验与安全加载官方实现；**支撑 Scope**：模型权重；**阅读深度**：读 header/data buffer、mmap、校验与不含 optimizer state 的边界。
- [PyTorch Distributed Checkpoint](https://pytorch.org/docs/stable/distributed.checkpoint.html) — **选入理由**：DCP 文档公开 Planner、StorageWriter/Reader、Metadata、异步保存和加载时 Reshard 的职责划分，可据此审查分布式 Checkpoint 的提交边界与恢复路径；**支撑 Scope**：Checkpoint、一致性与恢复语义；**阅读深度**：读 planner、StorageWriter/Reader、metadata、async save 与 load-time reshard。
- [Amazon S3 Consistency Model](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel) — **选入理由**：对象存储可见性的一手语义，用于区分对象成功与全局 checkpoint 提交；**支撑 Scope**：分布式存储、一致性与恢复语义；**阅读深度**：读 PUT/DELETE/LIST 可见性并设计 generation/manifest 完成协议。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
