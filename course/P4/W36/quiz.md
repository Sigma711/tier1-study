# W36 · 简短 Quiz

1. 推导 GQA 相对 MHA 的 KV 容量/带宽比例，并解释 query heads 到 KV heads 的映射。
2. Paged Attention 的 page table 带来哪些访存代价，又为何能改善容量管理？
3. 设计 contiguous/paged、MHA/GQA 对照，需固定哪些变量并报告哪些 kernel 指标？
4. page table 越界、ragged length 错配与 softmax 失稳分别如何诊断？
5. 何时采用统一 kernel，何时为 Prefill/Decode 特化？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
