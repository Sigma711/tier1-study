# P5：Distributed Training 与 GPU Communication

## 阶段目的

理解大规模模型如何跨 GPU 训练

## 阶段掌握标准

达到 L3–L4 之间的理解与架构分析能力；专项岗位再增加真实多节点研究。

## 课程

- [W42 · 训练完整生命周期：Forward、Backward、Optimizer State、Activation Memory](W42/README.md)
- [W43 · DDP、Gradient Synchronization、AllReduce、通信与计算重叠](W43/README.md)
- [W44 · ZeRO、FSDP2、参数与优化器状态切分](W44/README.md)
- [W45 · Tensor、Sequence、Context Parallelism、DTensor、DeviceMesh](W45/README.md)
- [W46 · Pipeline Parallelism、Microbatch、GPipe、1F1B、Pipeline Bubble](W46/README.md)
- [W47 · MoE、Expert Parallelism、All-to-All、负载均衡](W47/README.md)
- [W48 · NCCL、Ring/Tree Collectives、NVLink、RDMA、异步 Checkpoint](W48/README.md)
- [W49 · TorchTitan / Megatron 综合研究](W49/README.md)
