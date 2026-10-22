# W04 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：微积分、链式法则、梯度、反向传播、SGD、AdamW。

1. 对 y=(Wx+b)^2 写出关于 W 的链式求导路径，并说明反向传播为何按逆拓扑序累积梯度。
2. 比较 SGD 与 AdamW 的状态量和更新式；AdamW 的 weight decay 为什么称为解耦？
3. PyTorch 张量被 in-place 修改后 backward 报 version mismatch，saved tensor 与 version counter 如何解释该错误？
4. 设计有限差分梯度检查：选择步长、误差指标与失败判据时应避免什么数值陷阱？
5. 在相同模型下比较 SGD/AdamW，必须固定哪些变量，观察哪些收敛、耗时和内存指标？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
