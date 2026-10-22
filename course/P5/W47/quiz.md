# W47 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：MoE、Expert Parallelism、All-to-All、负载均衡。

1. 由 T 个 token、E 个专家、top-k 和 capacity factor 推导期望负载与容量上界。
2. 从 router logits 到 token permutation、All-to-All、expert 计算再到还原，索引不变量是什么？
3. 如何用 expert load CV、router entropy、dropped tokens 和 All-to-All 时间评价负载均衡？
4. 为什么简单增加 capacity factor 可能缓解丢 token 却恶化显存与通信？
5. 在跨节点带宽受限时，如何评审 expert placement、top-k 与质量取舍？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
