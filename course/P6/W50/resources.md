# W50 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/) — **选入理由**：Rust tokenizer pipeline 的官方文档；**支撑 Scope**：Tokenization、数据管道；**阅读深度**：读 normalizer、pre-tokenizer、model、post-processor 与 offset/special-token 语义。
- [Megatron Energon（固定 commit）](https://github.com/NVIDIA/Megatron-Energon/tree/fb2aaf8ca9f9817b654dcfb36ca9d97547e77af9) — **选入理由**：大规模训练数据加载与 sample packing 的官方实现；**支撑 Scope**：Packing、Streaming Dataset、数据管道；**阅读深度**：定位 sample loader、packing、worker/shard 与 checkpointable iterator。
- [Hugging Face Datasets Streaming](https://huggingface.co/docs/datasets/stream) — **选入理由**：官方说明 IterableDataset、shard、shuffle buffer 与流式批处理；**支撑 Scope**：Streaming Dataset；**阅读深度**：读 sharding、shuffle、epoch/seed 与分布式 worker 行为。
- [Apache Arrow Format](https://arrow.apache.org/docs/format/Columnar.html) — **选入理由**：Arrow 格式规范逐 Buffer 定义 validity bitmap、offset、变长与嵌套布局，是判断跨语言零拷贝是否成立以及一次 Batch 实际占用多少字节的权威依据；**支撑 Scope**：Arrow；**阅读深度**：读 validity bitmap、offset buffer、nested layout 与零拷贝边界。
- [Apache Parquet Concepts](https://parquet.apache.org/docs/concepts/) — **选入理由**：Parquet 文件、row group、column chunk/page 的官方说明；**支撑 Scope**：Parquet；**阅读深度**：读物理布局、encoding/compression 与 row-group 粒度的 I/O 权衡。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
