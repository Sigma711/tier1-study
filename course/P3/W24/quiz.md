# W24 · 简短 Quiz

1. 说明 Canonicalization、Pattern Rewrite、CSE、DCE 与 Pass Manager 的职责边界及顺序依赖。
2. 给定两个互相反向的 rewrite，解释 greedy driver 不收敛的原因与可验证修复条件。
3. CSE 判断两个 op 等价必须包含哪些语义；副作用标注错误为何会让 DCE 破坏程序？
4. 设计只改变 pass 顺序的实验，应观测哪些编译期与运行期指标？
5. 比较巨型 pass 与小 pass pipeline 的分析缓存、测试和失败隔离。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
