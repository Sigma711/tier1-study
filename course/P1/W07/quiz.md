# W07 · 简短 Quiz

本课 Quiz 固定检验以下知识范围：Transformer、Self-Attention、Multi-Head Attention、RoPE、GQA/MQA。

1. 推导 self-attention 中 QKᵀ 和乘 V 的主要 FLOPs 与 L 的关系，为什么称为二次复杂度？
2. 给定 32 个 query heads、8 个 KV heads、head_dim=128，比较 MHA 与 GQA 每 token 的 K/V 元素数。
3. 解释 RoPE 如何对成对维度做旋转；position 或频率设置错误会留下什么证据？
4. 给出 causal mask 方向写反与缩放因子遗漏的最小诊断方法。
5. 在质量、KV 容量和带宽约束下比较 MHA、GQA、MQA，说明适用边界。

## 答题与订正

正式学习后记录答案、参考依据和错因。Quiz 用于知识检索，不设计互动式操作题。
