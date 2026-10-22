# W19 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：GPU Kernel 专题综合学习与考核。

1. 任选一个本阶段 Kernel，给出 FLOPs、字节数、AI、work/span 与 occupancy 资源界，并判断主导上界。
2. 从源码到 IR、PTX/SASS、launch、timeline/counter，列出一条完整且可核验的证据链。
3. 设计跨 Shape、dtype、layout 的正确性矩阵；哪些边界输入最容易暴露 mask、race 和数值错误？
4. 库基线更快但自定义 Kernel 在一个热门 Shape 更快，是否值得上线？从覆盖率、回退、维护和证据回答。
5. 面对错误结果且性能 counter 异常，如何按算法、数值、并发、测量四类假设安排诊断顺序？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
