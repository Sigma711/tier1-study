# 核心论文清单

本清单固定课程明确点名的第一批核心论文。正式教学时按对应周次研读，并记录论文设计、当前源码与实测结果之间的差异。

| 主题 | 论文 | 课程中的用途 |
|---|---|---|
| Transformer | [Attention Is All You Need（NeurIPS 2017）](https://arxiv.org/abs/1706.03762) | 理解现代大模型计算的源头 |
| 位置编码 | [RoFormer: Enhanced Transformer with Rotary Position Embedding（2021）](https://arxiv.org/abs/2104.09864) | RoPE 的复数旋转形式、相对位置信号与长度外推边界 |
| Attention 架构 | [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints（EMNLP 2023）](https://aclanthology.org/2023.emnlp-main.298/) | MHA、MQA、GQA 的质量、KV 容量与吞吐权衡 |
| 稀疏模型 | [Switch Transformers（JMLR 2022）](https://www.jmlr.org/papers/v23/21-0998.html) | 稀疏 MoE 路由、容量、负载均衡与训练稳定性 |
| AI Compiler | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning（OSDI 2018）](https://www.usenix.org/conference/osdi18/presentation/chen) | 图优化、算子调度与自动调优的经典系统 |
| GPU Compiler | [Triton（MAPL 2019）](https://dl.acm.org/doi/abs/10.1145/3315508.3329973) | 以 Tile 为核心的 GPU 编程抽象 |
| Compiler IR | [MLIR（2020）](https://arxiv.org/abs/2002.11054) | 多层 IR、Dialect 与编译器基础设施 |
| 分布式训练 | [Megatron-LM（2019）](https://arxiv.org/abs/1909.08053) | 模型并行的经典起点 |
| 显存优化 | [ZeRO（SC 2020）](https://sc20.supercomputing.org/proceedings/tech_paper/tech_paper_pages/pap379.html) | 分布式训练中的状态切分 |
| Attention Kernel | [FlashAttention（NeurIPS 2022）](https://arxiv.org/abs/2205.14135) | 访存感知算法设计 |
| GPU 并行优化 | [FlashAttention-2（ICLR 2024）](https://proceedings.iclr.cc/paper_files/paper/2024/hash/98ed250b203d1ac6b24bbcf263e3d4a7-Abstract-Conference.html) | 线程分工与 GPU 利用率 |
| 推理内存管理 | [Efficient Memory Management for Large Language Model Serving with PagedAttention（SOSP 2023）](https://doi.org/10.1145/3600006.3613165) | 系统级显存管理与推理吞吐 |
| 推理调度 | [Sarathi-Serve（OSDI 2024）](https://www.usenix.org/conference/osdi24/presentation/agrawal) | Chunked Prefill 与延迟/吞吐权衡 |
| 推测解码 | [Fast Inference from Transformers via Speculative Decoding（ICML 2023）](https://proceedings.mlr.press/v202/leviathan23a.html) | 精确分布保持、接受率与加速上界 |
| 分布式推理 | [DistServe（OSDI 2024）](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) | Prefill/Decode 分离 |
| 推理 Runtime | [SGLang（NeurIPS 2024）](https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html) | 结构化生成程序的高效执行 |
| Attention 工程 | [FlashInfer（MLSys 2025）](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) | 可组合的高性能 Attention Kernel |
| 最新编译研究 | [Flashlight（MLSys 2026）](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bc52716d13d2d72ea0f335667d86c0f8-Abstract-Conference.html) | 编译器自动生成融合 Attention Kernel |
| 现代训练系统 | [TorchTitan（ICLR 2025）](https://openreview.net/forum?id=SFN6Wm7YBI) | 可组合的 FSDP2、TP、PP、CP、EP 训练架构 |
