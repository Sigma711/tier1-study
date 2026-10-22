# W22 · 简短 Quiz

1. 从 LLVM `Module` 到 machine code 描述 IR、pass、instruction selection 与 object 的关系。
2. 若 JIT 比 AOT 多付编译成本 `C`、每次节省 `Δ`，推导盈亏平衡调用次数，并讨论代码缓存如何改变结论。
3. 解释 poison/undef、data layout 或 calling convention 错配为何可能通过编译却运行错误。
4. 设计 `-O0/-O2` 与 JIT/AOT 对照实验，必须报告哪些编译期和运行期指标？
5. 服务端何时选择 ORC JIT、AOT 或混合方案？

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
