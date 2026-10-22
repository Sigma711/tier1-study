# W27 · 简短 Quiz

1. 写出带 shape 与 stride 的 tensor 元素地址公式，并比较 contiguous 与 strided layout。
2. 给定多个 buffer 的生命周期区间与大小，计算最小峰值内存，并说明动态 shape 为何只能给保守上界。
3. Shape inference、动态维与符号维各解决什么问题？guard 失败意味着什么？
4. 举出生命周期复用导致 use-after-free/覆盖的案例及可验证证据。
5. 比较通用动态实现、按符号范围特化和回退方案。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
