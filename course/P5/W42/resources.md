# W42 · 固定学习资料

以下资料已在课程初始化时固定。授课应优先使用这些一手来源，不得由未来 Agent 随机替换。

**资料状态核验：2026-10-22。**

- [PyTorch Autograd Mechanics](https://pytorch.org/docs/stable/notes/autograd.html) — **选入理由**：官方解释反向模式自动微分与 saved tensor；**支撑 Scope**：Forward、Backward、Activation Memory；**阅读深度**：读 graph recreation、saved tensors、non-differentiable functions，并沿 Node/grad_fn 对照源码。
- [PyTorch AdamW](https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html) — **选入理由**：PyTorch 同时公开 AdamW 的更新公式、参数组和一二阶矩状态，可据此逐字节计算优化器显存，并核对 foreach/fused/capturable 对训练执行路径的改变；**支撑 Scope**：Optimizer State、训练完整生命周期；**阅读深度**：逐项推导一二阶矩、参数与梯度字节量，读 foreach/fused/capturable 差异。
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — **选入理由**：该论文用模型规模、数据量和计算量的受控实验拟合幂律，并给出 compute-efficient frontier，是讨论预训练预算分配及外推风险的经典定量基线；**支撑 Scope**：预训练；**阅读深度**：精读 scaling-law 拟合、compute-efficient frontier、实验假设与外推限制。
- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) — **选入理由**：InstructGPT 原论文串起 SFT、reward model 与 PPO-RLHF；**支撑 Scope**：SFT、RLHF、评估；**阅读深度**：读三阶段流水线、KL 约束、人工偏好评估和局限。
- [LoRA](https://arxiv.org/abs/2106.09685) — **选入理由**：LoRA 原文把权重增量约束为低秩分解，报告 Rank、注入位置与任务质量消融，并说明推理时如何合并权重，是 PEFT 参数和显存收益的原始证据；**支撑 Scope**：LoRA；**阅读深度**：推导低秩增量参数量，读注入位置、rank ablation 与推理合并。
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — **选入理由**：DPO 原文从 KL 正则化奖励最大化推导出无需显式 Reward Model 的分类损失，提供理解 reference model、温度参数与偏好数据假设不可替代的推导链；**支撑 Scope**：DPO；**阅读深度**：精读由 KL-regularized RL 到 DPO loss 的推导、reference model 与失败边界。
- [DeepSeekMath](https://arxiv.org/abs/2402.03300) — **选入理由**：DeepSeekMath 是 GRPO 的原始公开出处，它用组内相对奖励替代 PPO Critic，并给出数学任务训练证据，能够准确界定算法节省了什么状态、又引入了什么采样依赖；**支撑 Scope**：GRPO；**阅读深度**：读 group-relative advantage、目标函数、与 PPO critic 的差异及数学任务证据。
- [HELM](https://arxiv.org/abs/2211.09110) — **选入理由**：HELM 把 Scenario、Metric 与模型适配组成显式评估矩阵，并同时报告准确性、校准、鲁棒性和公平性，适合揭示单一榜单分数遗漏的能力与风险；**支撑 Scope**：评估；**阅读深度**：读 scenario/metric taxonomy、校准/鲁棒/公平指标与覆盖限制。
- [Hugging Face Model Cards](https://huggingface.co/docs/hub/model-cards) — **选入理由**：Model Card 元数据把 base model、数据集、评估结果、许可证与 Hub revision 关联起来，是检查模型血缘和训练版本能否被公开追溯的实际格式约定；**支撑 Scope**：模型与训练版本管理；**阅读深度**：读 model card metadata、base model、datasets、evaluation results 与 revision 可追溯字段。

如某链接、版本或项目状态发生变化，只能核验并更新引用；不得借机改变本课 Scope。
