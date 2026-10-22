# W08 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：LLM 架构、Embedding、MLP、Normalization、Dense/MoE、Tokenization。

1. 词表 V、hidden H 的 embedding 参数量是多少？token id 与 tokenizer vocab 不匹配会发生什么？
2. 比较 LayerNorm 与 RMSNorm 的统计量、计算和语义；epsilon 放置为什么影响结果？
3. 推导门控 MLP 主要矩阵乘法的参数量与 FLOPs，并指出 activation 位置。
4. Dense 模型与 top-2 MoE 在总参数、每 token 激活参数和路由负载方面有何区别？
5. 发现少数 expert 过载时，需要哪些 router/dropped-token/耗时证据，哪些结论不能仅凭负载推出？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
