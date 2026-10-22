# W50 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：数据管道、Tokenization、Packing、Arrow/Parquet、Streaming Dataset。

1. 由原始字节量、token 膨胀率和 block size 推导 token 数、padding waste 与 packing efficiency。
2. Tokenizers 的 normalizer、pre-tokenizer、model 各自如何影响 token 边界与版本兼容？
3. Arrow/Parquet row group 与 Streaming Dataset 的顺序读、shuffle、prefetch 如何共同决定 data wait？
4. 如何用 sample id、shard/epoch cursor 验证 packing 与 streaming 不重、不漏、不串样本？
5. 在离线物化和流式读取之间选择时，如何权衡吞吐、随机性、可复现性和存储成本？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
