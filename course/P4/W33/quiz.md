# W33 · 简短 Quiz

1. 沿 vLLM V1 Engine、Scheduler、Worker、Model Runner 描述一次请求从入队到执行的状态流。
2. 给定 token budget、running/waiting 请求及 KV blocks，计算一轮最多调度的 token，并说明约束。
3. 为什么 Model Runner 报错不一定是 Scheduler 错误？列出两层各自证据。
4. 对照不同 scheduler 配额时，应同时观测哪些 queue、step 和 GPU 指标？
5. 评审集中 Scheduler 与 Worker 进程隔离的 IPC/故障取舍。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 只检验知识、推导、源码理解、故障判断与设计取舍，不包含手工部署或机械操作任务。
