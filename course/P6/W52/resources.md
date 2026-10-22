# W52 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [vLLM KV Offloading](https://docs.vllm.ai/en/latest/features/kv_offloading_usage/) — **选入理由**：官方当前 KV offload 使用与 connector 契约；**支撑 Scope**：CPU/GPU 多级缓存、KV Offloading；**阅读深度**：读配置、connector、block 生命周期、限制与性能警告。
- [NIXL](https://github.com/ai-dynamo/nixl/tree/0b146a82d8efb52f40b1da872bb271978f510e94) — **选入理由**：NIXL 的固定源码展示 Transfer Descriptor、Backend Plugin、内存注册与异步 Completion 如何统一承载 GPU、主存和存储介质的数据搬运，是分析 GPUDirect 数据路径的直接实现证据；**支撑 Scope**：NVMe 多级缓存、权重分发、GPUDirect；**阅读深度**：定位 transfer descriptor、backend/plugin、registration 与 completion API。
- [Safetensors（固定 commit）](https://github.com/huggingface/safetensors/tree/e246a2560645b7525f5775669ed816eb57c5bcc8) — **选入理由**：Safetensors 的固定实现把 Header、Tensor Offset、mmap 与边界校验放在同一加载路径中，可核验所谓零拷贝加载依赖哪些文件布局和安全检查；**支撑 Scope**：模型加载；**阅读深度**：读 header/offset、mmap、零拷贝边界与格式校验。
- [PyTorch Tensor Parallel Tutorial](https://pytorch.org/tutorials/intermediate/TP_tutorial.html) — **选入理由**：官方展示分片权重加载和 DeviceMesh 语义；**支撑 Scope**：权重分发；**阅读深度**：读 sharded tensor layout、加载时布局与 collective，不扩展到训练并行课程。
- [CUDA GPUDirect RDMA](https://docs.nvidia.com/cuda/gpudirect-rdma/) — **选入理由**：GPUDirect RDMA 内存注册、ordering 和支持矩阵的一手规范；**支撑 Scope**：GPUDirect；**阅读深度**：读 peer-memory、BAR/pinning、同步与平台限制。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
