# W53 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/) — **选入理由**：驱动、toolkit、device plugin 与监控 operand 的官方生命周期文档；**支撑 Scope**：Kubernetes GPU Operator；**阅读深度**：读 ClusterPolicy、operand reconciliation、升级和故障排查。
- [Kubernetes Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) — **选入理由**：ListAndWatch/Allocate 与 extended resource 的官方规范；**支撑 Scope**：Device Plugin；**阅读深度**：读 gRPC lifecycle、Device 状态、CDI/Allocate 与 kubelet 行为。
- [NVIDIA MIG User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/) — **选入理由**：MIG User Guide 精确定义 GPU Instance、Compute Instance、Profile 和设备枚举，并列出硬件代际限制，是判断显存与计算隔离究竟由硬件保证到哪一层的依据；**支撑 Scope**：MIG、资源隔离；**阅读深度**：读 GPU/compute instance、profile、device enumeration 与限制。
- [NVIDIA MPS Documentation](https://docs.nvidia.com/deploy/mps/) — **选入理由**：MPS 文档说明 Client/Server 复用 GPU Context、Active Thread Percentage 配额以及故障传播行为，能揭示它提供的是共享与限流而非 MIG 式硬隔离；**支撑 Scope**：MPS、资源隔离；**阅读深度**：读 client/server、active thread percentage、fault containment 和 MIG 组合边界。
- [Kubernetes Topology Manager](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/) — **选入理由**：CPU/device NUMA hints 与 policy 的官方契约；**支撑 Scope**：NUMA 与资源隔离；**阅读深度**：读 hint providers、scope/policy、admission failure 与 static CPU manager 关系。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
