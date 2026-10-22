# W12 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：CUDA 编程模型、Kernel Launch、Stream、Event、异步执行。

1. 画出两个 stream 中 H2D、Kernel、D2H 的 happens-before；event record/wait 如何建立跨流依赖？
2. 若 launch 开销为 10 μs、Kernel 为 5 μs，批量合并 10 次工作理论上减少多少 launch 开销？
3. pageable host memory 为什么可能破坏预期异步 copy？pinned memory 又付出什么代价？
4. 异步 Kernel 的错误为什么可能在后续同步 API 才报告？如何定位首次失败 launch？
5. 什么条件下多 stream 能重叠 copy/compute，什么资源冲突会让时间线仍串行？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
