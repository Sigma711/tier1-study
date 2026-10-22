# W29 · 简短 Quiz

1. 描述 AOTAutograd joint graph、partition、TorchInductor IR、生成 kernel 与 code cache 的关系。
2. 给定中间 tensor 大小、launch 成本和重用次数，判断 fusion 何时节省流量、何时增加重计算/寄存器压力。
3. 冷缓存和热缓存实验必须如何控制，才能不把编译时间误算成运行收益？
4. mutation/alias 或 cache key 漏项会造成什么错编译，如何差分验证？
5. 设计 forward/backward 分割与缓存粒度的取舍。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
