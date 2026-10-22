# W58 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Compiler、选择真实算子或执行路径进行优化。

1. 为选定算子计算 FLOPs、bytes 和算术强度，并用 Roofline 判断优化方向。
2. 追踪 TorchDynamo/FX→AOTAutograd→Inductor IR→Triton/CUDA 的 lowering 路径。
3. 如何设计 eager/原路径对照，隔离 compile time、cache、shape 和 dtype？
4. graph break、guard 或数值容差失败时，哪些 IR/generated code/差分证据可定位？
5. 比较专用 pattern、通用 pass 与 runtime dispatch 的覆盖面和维护成本。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
