# W28 · 简短 Quiz

1. 从 Python bytecode 经 eval-frame hook 到 FX Graph，说明 TorchDynamo 捕获了什么、保留了什么 guard。
2. 用编译成本、命中次数、compiled/eager 单次成本推导何时 `torch.compile` 获益。
3. 一个数据相关分支为何可能 graph break 或产生 guard？两种处理的语义风险是什么？
4. 如何用 explain、guard failure 与 bytecode offset 区分捕获失败和缓存不稳定？
5. 比较扩大捕获、允许 graph break 与显式禁编译区域。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
