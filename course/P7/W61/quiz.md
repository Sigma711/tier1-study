# W61 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Distributed Runtime、通信、缓存传输、容错。

1. 用 payload、带宽、启动延迟和并行度推导分布式 runtime 通信临界路径。
2. 何时 KV 传输比重算划算，模型 revision/request generation 如何进入判断？
3. rank/worker group、collective/RPC、KV connector 与 failure detector 如何协作？
4. 如何用 fencing、checksum、timeout 与恢复 trace 诊断陈旧缓存或脑裂？
5. 比较并行方式、缓存迁移/重算、快速失败与恢复复杂度。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
