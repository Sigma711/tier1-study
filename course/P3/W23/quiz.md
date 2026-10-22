# W23 · 简短 Quiz

1. 解释 Operation、Region、Block、SSA Value、Type、Attribute 的包含/引用关系，并给出一个多 region op 的合法性约束。
2. 含 `N` 个 op、`B` 个 block 的 IR，全遍历复杂度为何是 `O(N+B)`？递归 region 深度还影响什么？
3. ODS 能生成哪些 parser/builder/verifier 代码，哪些语义仍必须手写？
4. 未注册 dialect、operand/result type 不匹配和 region isolation 违规分别如何诊断？
5. 设计新 dialect 时，何时复用标准 Type/Attribute，何时自定义？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
