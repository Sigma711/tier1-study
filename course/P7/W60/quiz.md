# W60 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Runtime、Scheduler、Paged KV Cache、Admission Control。

1. 由层数、KV heads、head dimension、dtype 与 block size 推导每 token KV bytes 和碎片。
2. Scheduler、KVCacheManager/BlockPool 与 worker 如何完成 continuous batching 状态跃迁？
3. admission 阈值如何影响 queue time、TTFT、TPOT、goodput 和 preemption？
4. 哪些 block ownership/refcount/release 不变量能防止 KV 泄漏或串请求？
5. 在吞吐、尾延迟、KV 利用率与过载保护间选择调度策略。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
