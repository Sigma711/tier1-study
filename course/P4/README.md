# P4：LLM Inference Runtime 与 Serving Systems

## 阶段目的

深入推理引擎内核

## 阶段掌握标准

理解 Mini LLM Inference Engine 的调度、缓存、并发和 Benchmark，能够完成系统复盘。

## 课程

- [W32 · 推理计算模型：Prefill、Decode、TTFT、TPOT、算力/带宽约束](W32/README.md)
- [W33 · vLLM V1 架构：Engine、Scheduler、Worker、Model Runner](W33/README.md)
- [W34 · Continuous Batching、Chunked Prefill、Admission Control、公平调度](W34/README.md)
- [W35 · Paged KV Cache、Block Allocator、Prefix Caching、引用计数与淘汰](W35/README.md)
- [W36 · Paged Attention、FlashInfer、推理 Kernel、GQA](W36/README.md)
- [W37 · 模型量化：INT8、INT4、FP8、低比特格式、量化误差与 Kernel](W37/README.md)
- [W38 · Speculative Decoding、Sampling、Structured Output、MoE 与多模态推理基础](W38/README.md)
- [W39 · 多 GPU 推理：TP、PP、EP、P/D 分离、KV 传输与路由](W39/README.md)
- [W40 · Serving Benchmark、Goodput、SLO、Tail Latency、负载模型](W40/README.md)
- [W41 · Mini LLM Inference Engine 综合考核](W41/README.md)
