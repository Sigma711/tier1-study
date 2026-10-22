# W54 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [Kueue Concepts](https://kueue.sigs.k8s.io/docs/concepts/) — **选入理由**：Kubernetes 批作业准入与配额的官方对象模型；**支撑 Scope**：Kueue、配额、公平调度；**阅读深度**：读 ClusterQueue、LocalQueue、cohort、ResourceFlavor、admission 与 preemption。
- [Ray Scheduling](https://docs.ray.io/en/latest/ray-core/scheduling/index.html) — **选入理由**：Ray task/actor 与 placement group 调度的官方文档；**支撑 Scope**：Ray、Gang Scheduling；**阅读深度**：读 resources、placement group bundle/strategy、调度失败和容错边界。
- [Slurm Multifactor Priority](https://slurm.schedmd.com/priority_multifactor.html) — **选入理由**：Slurm 官方公式把 Age、Fair-share、Job Size、Partition 和 QOS 归一化后加权为作业优先级，可直接推演公平策略怎样改变排队顺序及何处会发生饥饿；**支撑 Scope**：Slurm、公平调度；**阅读深度**：读 age、fair-share、job size、partition/QOS 权重及归一化。
- [Slurm Gang Scheduling](https://slurm.schedmd.com/gang_scheduling.html) — **选入理由**：Slurm gang/time-slicing 行为的官方说明；**支撑 Scope**：Slurm、Gang Scheduling；**阅读深度**：读 gang 配置、preemption、oversubscribe 与和 Kueue/Ray 语义不同之处。
- [Kubernetes Multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/) — **选入理由**：namespace、RBAC、网络与节点隔离的官方安全边界；**支撑 Scope**：多租户安全；**阅读深度**：读 tenant model、control-plane/data-plane isolation 与限制。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
