# W35 · 简短 Quiz

1. 根据层数、KV heads、head dimension 与 dtype 计算每 token KV 字节和给定显存下容量。
2. 给定 block size 与若干序列长度，计算内部碎片，并解释为何更小 block 不是免费收益。
3. Prefix Caching 的 hash key 与引用计数必须满足哪些不变量？
4. 描述 eviction 与 copy-on-write 交错时可能出现的缓存污染及诊断证据。
5. 选择 block 大小和淘汰策略时如何权衡元数据、命中和回收延迟？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
