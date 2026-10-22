# W52 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：CPU/GPU/NVMe 多级缓存、KV Offloading、模型加载、权重分发、GPUDirect。

1. 用容量 Ci、带宽 Bi、延迟 Li 和命中率推导多级缓存的有效访问时间。
2. 区分 KV Offloading、模型加载、权重分发中的对象身份、生命周期和传输方向。
3. vLLM KV connector、NIXL descriptor/backend 与 GPUDirect 数据路径各处于哪一层？
4. 如何用 checksum、revision、cache metadata、CUDA/I/O counter 诊断陈旧 KV 或路径回退？
5. 在 TTFT、TPOT、GPU 容量和 NVMe/CPU 带宽约束下设计层级与预取。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
