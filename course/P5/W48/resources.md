# W48 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [NCCL User Guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/) — **选入理由**：NCCL collective、communicator 与故障语义的官方文档；**支撑 Scope**：NCCL、Ring/Tree Collectives；**阅读深度**：读 collective semantics、group calls、environment/algorithm selection 与 troubleshooting。
- [NCCL GitHub（固定 commit）](https://github.com/NVIDIA/nccl/tree/3e46c089f4ae4732722a419eb6096aead7e47a30) — **选入理由**：核对 Ring/Tree channel、transport 和 topology 的官方源码；**支撑 Scope**：Ring/Tree Collectives、NVLink、RDMA；**阅读深度**：沿 graph/search、transport、collectives/device 调用链阅读，不以 README 代替源码。
- [GPUDirect RDMA](https://docs.nvidia.com/cuda/gpudirect-rdma/) — **选入理由**：GPU 与 RDMA 设备直达内存路径的官方规范；**支撑 Scope**：RDMA、NVLink 的边界对照；**阅读深度**：读 memory pinning、peer-memory、ordering 与平台限制，明确它不描述 NVLink collective。
- [NVLink Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#nvlink) — **选入理由**：官方说明 CUDA 可见的 NVLink peer/interconnect 能力；**支撑 Scope**：NVLink；**阅读深度**：读 peer access、拓扑可见性和一致性限制。
- [PyTorch Distributed Checkpoint](https://pytorch.org/docs/stable/distributed.checkpoint.html) — **选入理由**：异步保存与分布式 state_dict 的官方入口，与 NCCL 数据路径分开；**支撑 Scope**：异步 Checkpoint；**阅读深度**：读 async_save staging、planner、StorageWriter、Future 与 load-time reshard 契约。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
