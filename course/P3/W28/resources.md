# W28 · 固定学习资料

资料状态核验：2026-10-22。

以下资料按本课固定 Scope 精确分工。链接、项目结构或版本变化时只更新引用与版本说明，不改变 Scope。

- [TorchDynamo Deep Dive](https://docs.pytorch.org/docs/stable/torch.compiler_dynamo_deepdive.html) — **选入理由**：它沿 CPython bytecode evaluation、VariableTracker 和 bytecode rewriting 解释 TorchDynamo 如何截获 Python 执行、生成 FX Graph 并安装 guards，能把 graph break 的位置追溯到捕获机制本身；**支撑 Scope**：TorchDynamo、Python Bytecode、FX Graph、Guards、Graph Break；**阅读深度**：精读 bytecode transformation、VariableTracker、guards 与 graph breaks。
- [torch.compiler Troubleshooting](https://docs.pytorch.org/docs/stable/torch.compiler_troubleshooting.html) — **选入理由**：它给出 recompilation、guard failure、graph break 的实际日志分类，以及 `torch._dynamo.explain` 和 minifier 的证据采集路径，适合区分“捕获失败”“重复编译”和“后端报错”；**支撑 Scope**：Guards 与 Graph Break；**阅读深度**：精读 recompilation、logging、`torch._dynamo.explain` 与 minifier 证据。
- [torch.fx documentation](https://docs.pytorch.org/docs/stable/fx.html) — **选入理由**：它详细定义 Graph、Node、GraphModule 的可变图表示和 symbolic tracing 规则，使学习者能够逐节点阅读 Dynamo 产物，并判断 Python 控制流或副作用何时无法忠实进入 FX；**支撑 Scope**：FX Graph；**阅读深度**：精读 Graph/Node/GraphModule 与 symbolic tracing 的语义边界。
