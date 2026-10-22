# W37 · 简短 Quiz

1. 写出对称/非对称量化与反量化公式，说明 scale、zero-point、clip 和 rounding 的误差来源。
2. 计算 INT8、INT4、FP8 权重容量及 group scale 元数据，不能忽略什么开销？
3. 为何模型文件变小不保证 TPOT 下降？从 kernel 支持与瓶颈解释。
4. 如何用层级误差、质量集和 kernel trace 区分量化误差与 fallback？
5. 比较 weight-only、weight-activation 与 FP8 的部署取舍。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
