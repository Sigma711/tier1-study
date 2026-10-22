# W39 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [Megatron-LM paper](https://arxiv.org/abs/1909.08053) — **选入理由**：它给出 MLP 与 attention 的列切分/行切分方式以及对应 collective，是推导 TP 通信量和同步点的经典起点；**支撑 Scope**：TP；**阅读深度**：精读 tensor parallel partition 与 collective；训练部分只作机制来源。
- [GPipe](https://proceedings.neurips.cc/paper/2019/hash/093f65e080a295f8076b1c5722a46aa2-Abstract.html) — **选入理由**：它把模型分段、micro-batch 数量和 pipeline bubble 统一到一个调度模型中，便于定量判断 PP 的利用率上限；**支撑 Scope**：PP；**阅读深度**：精读 stage partition、micro-batch 与 bubble。
- [MegaBlocks (MLSys 2023)](https://proceedings.mlsys.org/paper_files/paper/2023/hash/5a54f79333768effe7e8927bcccffe40-Abstract-mlsys2023.html) — **选入理由**：它把 token routing、expert placement 与 block-sparse execution 连起来，揭示 EP 的不均衡与 dispatch 通信从何产生；**支撑 Scope**：EP 的 expert routing/dispatch 基础；**阅读深度**：精读稀疏 expert placement 与通信来源。
- [DistServe (OSDI 2024)](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) — **选入理由**：它用 goodput 模型决定 prefill/decode 的独立资源配置，并量化跨阶段 KV 传输的收益与代价，是 P/D 分离的完整系统证据；**支撑 Scope**：P/D 分离；**阅读深度**：精读 goodput 模型、资源分配、KV 传输与实验边界。
- [NIXL repository](https://github.com/ai-dynamo/nixl/tree/0b146a82d8efb52f40b1da872bb271978f510e94) — **选入理由**：固定源码展示内存注册、transfer descriptor、backend 与 completion，能检验 KV 跨节点搬运的生命周期和失败返回；**支撑 Scope**：KV 传输；**阅读深度**：精读 transfer API、memory registration 与 backend；不把仓库目标当已验证性能。
- [llm-d repository](https://github.com/llm-d/llm-d/tree/a98ceff122f873a06990b91e3429993710bde631) — **选入理由**：它把 inference scheduler、P/D 路由和 KV connector 组合成实际分布式拓扑，适合分析控制面与数据面如何协作；**支撑 Scope**：P/D 路由；**阅读深度**：精读 inference scheduler、prefill/decode routing 与 KV connector 架构。
