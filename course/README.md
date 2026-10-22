# 64 周主课程索引

课程总目标是达到 AI Infrastructure 高级工程师所需的 L4 架构、内核、性能与评审能力。每课 Scope 已写入对应 `README.md`，是授课时不可漂移的边界。

## 15 个知识模块

| 编号 | 模块 | 目标深度 |
|---:|---|---|
| 01 | 数学与数值计算：线性代数、微积分、概率统计、数值稳定性、浮点误差、复杂度 | L3 |
| 02 | 机器学习与深度学习：反向传播、优化器、自动微分、Transformer、Attention、MoE、训练与推理 | L3–L4 |
| 03 | 系统编程：C++、Python、Rust、Linux、并发、内存模型、异步执行、性能分析 | L4 |
| 04 | GPU 体系结构：SM、Warp、SIMT、Tensor Core、内存层次、PCIe、NVLink | L4 |
| 05 | GPU 编程与优化：CUDA、Triton、GEMM、Reduction、Softmax、FlashAttention、Roofline | L4 |
| 06 | 编译器理论：AST、IR、SSA、CFG、数据流分析、优化 Pass、CodeGen、JIT/AOT | L4 |
| 07 | AI Compiler：LLVM、MLIR、TorchInductor、Triton Compiler、XLA、StableHLO、IREE、TVM | L4 |
| 08 | LLM 推理引擎：Prefill、Decode、Batching、KV Cache、PagedAttention、推测解码、量化 | L4 |
| 09 | 分布式推理：并行、P/D 分离、KV Cache 传输、路由、负载均衡、弹性伸缩 | L4 |
| 10 | 分布式训练：DDP、FSDP、ZeRO、TP、PP、CP、EP、通信、Checkpoint、故障恢复 | L3→L4 |
| 11 | 模型与训练生命周期：数据处理、预训练、SFT、LoRA、RLHF、DPO、GRPO、评估与版本 | L2–L3 |
| 12 | AI 数据与存储：Dataset Pipeline、Arrow/Parquet、对象存储、Checkpoint I/O、多级缓存 | L3–L4 |
| 13 | GPU 集群与调度：Kubernetes、GPU Operator、Kueue、Ray、Slurm、Quota、Gang Scheduling | L3–L4 |
| 14 | 性能、可观测与可靠性：Nsight、CUPTI、DCGM、Tracing、SLO、容量、成本、故障诊断 | L4 |
| 15 | Agent-Native Engineering：Context、Harness、Skills、MCP、任务分解、自动分析、测试与评审 | 全程贯穿 |

## 容易遗漏知识的固定落点

- 概率统计、分布、期望、方差、采样与估计固定在 W03。
- C++、Python、Rust、Linux、并发、内存模型、异步执行与性能分析固定在 W02。
- Skills、MCP、Context Engineering 与 Agent Harness 固定在 W02，并在后续各课按需应用，不再改变其概念 Scope。
- 预训练、SFT、LoRA、RLHF、DPO、GRPO、评估与模型版本管理固定在 W42。

这些落点属于本次课程初始化的最终范围，用于保证 15 个知识模块与 64 周逐课 Scope 一致；正式授课时不得再临时扩张或挪动。

## 每课学习结构

1. 原理讲授：从直觉进入严格模型与关键推导。
2. 论文研读：理解问题、设计、实验、限制与后续影响。
3. 源码分析：把论文机制对应到活跃开源项目的真实实现。
4. Agent 工程证据：由 Agent 完成实现、测试、Benchmark 与 Profiling，学习者审查证据和因果。
5. 技术复盘：用简短 Quiz、设计评审和面试问题检验理解。

## 统一考核

| 维度 | 权重 |
|---|---:|
| 原理与定量推导 | 25% |
| 源码与编译产物分析 | 20% |
| 工程正确性 | 20% |
| 性能研究方法 | 20% |
| 方案设计与技术答辩 | 15% |

阶段通过建议为 80/100；关键正确性和证据可复现是硬条件。评分依据可以由 Agent 采集，但解释和技术判断必须由学习者掌握。

## P0：学习环境、Agent 工程规范与能力基线

- [P0/W01 · AI Infra 全景、从模型计算到 GPU 执行、性能指标、现有能力测评](P0/W01/README.md)
- [P0/W02 · Agent Harness、Context Engineering、仓库规范、自动化验证与基准测试](P0/W02/README.md)

## P1：AI 计算基础与现代模型架构

- [P1/W03 · 张量、向量、矩阵、Shape、Stride、Broadcasting、矩阵乘法](P1/W03/README.md)
- [P1/W04 · 微积分、链式法则、梯度、反向传播、SGD、AdamW](P1/W04/README.md)
- [P1/W05 · 浮点数与数值计算：FP32、FP16、BF16、FP8、量化误差](P1/W05/README.md)
- [P1/W06 · 神经网络计算图、Autograd、计算与内存复杂度、Activation](P1/W06/README.md)
- [P1/W07 · Transformer、Self-Attention、Multi-Head Attention、RoPE、GQA/MQA](P1/W07/README.md)
- [P1/W08 · LLM 架构：Embedding、MLP、Normalization、Dense/MoE、Tokenization](P1/W08/README.md)
- [P1/W09 · 模型训练与生成过程、显存占用模型、推理工作负载](P1/W09/README.md)

## P2：GPU Architecture、CUDA 与高性能 Kernel

- [P2/W10 · GPU 微架构：SM、Warp、SIMT、线程调度、Occupancy](P2/W10/README.md)
- [P2/W11 · GPU 内存层次：Register、Shared Memory、L1/L2、HBM、Coalescing](P2/W11/README.md)
- [P2/W12 · CUDA 编程模型、Kernel Launch、Stream、Event、异步执行](P2/W12/README.md)
- [P2/W13 · 并行算法：Reduction、Scan、Atomic、Synchronization](P2/W13/README.md)
- [P2/W14 · GEMM、Tiling、Tensor Core、MMA、CUTLASS](P2/W14/README.md)
- [P2/W15 · Triton 编程模型、Block、Layout、Warp 映射](P2/W15/README.md)
- [P2/W16 · Operator Fusion：Softmax、LayerNorm、RMSNorm、内存流量优化](P2/W16/README.md)
- [P2/W17 · FlashAttention、Online Softmax、IO Complexity、Warp 分工](P2/W17/README.md)
- [P2/W18 · Nsight Compute、Nsight Systems、Roofline、PTX/SASS、自动调优](P2/W18/README.md)
- [P2/W19 · GPU Kernel 专题综合学习与考核](P2/W19/README.md)

## P3：编译器原理与 AI Compiler 内核

- [P3/W20 · 编译器整体架构：Frontend、IR、Optimizer、Backend；AST 与语义分析](P3/W20/README.md)
- [P3/W21 · CFG、SSA、Dominance、Dataflow、Liveness、Alias Analysis](P3/W21/README.md)
- [P3/W22 · LLVM：IR、Optimization Pass、CodeGen、JIT/AOT](P3/W22/README.md)
- [P3/W23 · MLIR：Operation、Region、Block、Dialect、Type、Attribute、ODS](P3/W23/README.md)
- [P3/W24 · Canonicalization、Pattern Rewrite、CSE、DCE、Pass Manager](P3/W24/README.md)
- [P3/W25 · Affine、SCF、Linalg、Tiling、Fusion、Bufferization](P3/W25/README.md)
- [P3/W26 · Dialect Conversion、LLVM Lowering、GPU CodeGen](P3/W26/README.md)
- [P3/W27 · Tensor Layout、Shape Inference、动态形状、符号维度、内存规划](P3/W27/README.md)
- [P3/W28 · TorchDynamo、Python Bytecode、FX Graph、Guards、Graph Break](P3/W28/README.md)
- [P3/W29 · AOTAutograd、TorchInductor、Kernel Fusion、Code Generation、编译缓存](P3/W29/README.md)
- [P3/W30 · Triton Compiler、TTIR/TTGIR、PTX；XLA、StableHLO、IREE、TVM 对照](P3/W30/README.md)
- [P3/W31 · Mini AI Compiler 综合考核](P3/W31/README.md)

## P4：LLM Inference Runtime 与 Serving Systems

- [P4/W32 · 推理计算模型：Prefill、Decode、TTFT、TPOT、算力/带宽约束](P4/W32/README.md)
- [P4/W33 · vLLM V1 架构：Engine、Scheduler、Worker、Model Runner](P4/W33/README.md)
- [P4/W34 · Continuous Batching、Chunked Prefill、Admission Control、公平调度](P4/W34/README.md)
- [P4/W35 · Paged KV Cache、Block Allocator、Prefix Caching、引用计数与淘汰](P4/W35/README.md)
- [P4/W36 · Paged Attention、FlashInfer、推理 Kernel、GQA](P4/W36/README.md)
- [P4/W37 · 模型量化：INT8、INT4、FP8、低比特格式、量化误差与 Kernel](P4/W37/README.md)
- [P4/W38 · Speculative Decoding、Sampling、Structured Output、MoE 与多模态推理基础](P4/W38/README.md)
- [P4/W39 · 多 GPU 推理：TP、PP、EP、P/D 分离、KV 传输与路由](P4/W39/README.md)
- [P4/W40 · Serving Benchmark、Goodput、SLO、Tail Latency、负载模型](P4/W40/README.md)
- [P4/W41 · Mini LLM Inference Engine 综合考核](P4/W41/README.md)

## P5：Distributed Training 与 GPU Communication

- [P5/W42 · 训练完整生命周期：Forward、Backward、Optimizer State、Activation Memory](P5/W42/README.md)
- [P5/W43 · DDP、Gradient Synchronization、AllReduce、通信与计算重叠](P5/W43/README.md)
- [P5/W44 · ZeRO、FSDP2、参数与优化器状态切分](P5/W44/README.md)
- [P5/W45 · Tensor、Sequence、Context Parallelism、DTensor、DeviceMesh](P5/W45/README.md)
- [P5/W46 · Pipeline Parallelism、Microbatch、GPipe、1F1B、Pipeline Bubble](P5/W46/README.md)
- [P5/W47 · MoE、Expert Parallelism、All-to-All、负载均衡](P5/W47/README.md)
- [P5/W48 · NCCL、Ring/Tree Collectives、NVLink、RDMA、异步 Checkpoint](P5/W48/README.md)
- [P5/W49 · TorchTitan / Megatron 综合研究](P5/W49/README.md)

## P6：AI Data、GPU Cluster 与生产级基础设施

- [P6/W50 · 数据管道、Tokenization、Packing、Arrow/Parquet、Streaming Dataset](P6/W50/README.md)
- [P6/W51 · 模型权重、Checkpoint、分布式存储、一致性与恢复语义](P6/W51/README.md)
- [P6/W52 · CPU/GPU/NVMe 多级缓存、KV Offloading、模型加载、权重分发、GPUDirect](P6/W52/README.md)
- [P6/W53 · Kubernetes GPU Operator、Device Plugin、MIG/MPS、NUMA 与资源隔离](P6/W53/README.md)
- [P6/W54 · Kueue、Ray、Slurm、配额、公平调度、Gang Scheduling、多租户安全](P6/W54/README.md)
- [P6/W55 · DCGM、NVML、CUPTI、Nsight、OpenTelemetry、端到端 Tracing](P6/W55/README.md)
- [P6/W56 · SLO、容量规划、成本模型、弹性伸缩、故障注入与恢复](P6/W56/README.md)

## P7：综合毕业项目与高级工程师面试

- [P7/W57 · 毕业项目方案：需求、架构、接口、约束、性能目标](P7/W57/README.md)
- [P7/W58 · Compiler：选择真实算子或执行路径进行优化](P7/W58/README.md)
- [P7/W59 · Kernel：分析性能瓶颈并实现优化](P7/W59/README.md)
- [P7/W60 · Runtime：Scheduler、Paged KV Cache、Admission Control](P7/W60/README.md)
- [P7/W61 · Distributed Runtime：通信、缓存传输、容错](P7/W61/README.md)
- [P7/W62 · Platform：部署、可观测、压测、资源控制](P7/W62/README.md)
- [P7/W63 · 论文复现、对照实验、回归审计、开源贡献准备](P7/W63/README.md)
- [P7/W64 · 高级技术面试模拟、系统设计、源码分析、项目答辩](P7/W64/README.md)
