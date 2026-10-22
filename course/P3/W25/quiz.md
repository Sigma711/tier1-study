# W25 · 简短 Quiz

1. 从 Linalg 迭代域分别 lowering 到 tiled loops，说明 Affine/SCF/Linalg 各承载什么语义。
2. 给定 cache 容量 `C` 与元素宽度 `b`，推导二维 tile 尺寸的容量约束，并解释为何工作量不变但流量可下降。
3. Fusion 何时减少中间物化，何时因工作集/寄存器压力反而变慢？
4. One-Shot Bufferize 判定 in-place 时必须维护哪些 alias/读写不变量？
5. 比较 destination-passing style 与额外 copy 对峰值内存和正确性的影响。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
