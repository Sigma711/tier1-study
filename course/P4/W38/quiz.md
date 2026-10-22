# W38 · 简短 Quiz

1. 给定 speculative 提议长度 `k` 和接受率 `α`，计算期望接受 token，并说明何时验证开销抵消收益。
2. 解释 temperature、top-k、top-p 如何改变归一化后的采样分布；哪些配置退化为 greedy？
3. Structured Output 如何用 grammar/bitmask 限制合法 token，为什么不能只在生成后校验？
4. MoE router 偏斜与多模态 token 扩张分别如何影响容量、延迟和诊断指标？
5. 设计同时保证 speculative 目标分布、grammar 合法性、MoE 路由和多模态输入对齐的验证方案。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
