# Language Passes

Two passes, in this order:

1. **anti-defensive**: decide what the paper is allowed to claim, and frame its contribution as a strength.
2. **academic-humanizer**: remove AI tells and calibrate the sentence-level claims.

Do not reverse the order. The first pass changes the argument; the second changes the prose.

---

## 1. Anti-defensive pass

### Principle

A paper report is a launch, not a lab notebook. Organize around what the work actually contributes, not around a confession of what it did not do.

### What to remove

| Defensive pattern | Why it hurts | Rewrite |
|---|---|---|
| "它只是把已有方法工程化" | makes the contribution sound incremental | "它把已有精确方法做到 175B 可用，核心贡献在计算改造" |
| "它没有发明新的误差模型" | invites the audience to ask what is new | "它保留被验证的误差模型，把创新集中在规模化最需要的计算改造上" |
| "唯一近似、没有误差界" | turns a design choice into a global weakness | "这是最关键的取舍：用固定序换可扩展性；严格误差界后来由 X 补上" |
| "只省访存，不省计算" | reads as a limitation without context | "它针对访存瓶颈设计，在低 batch 生成场景收益最大" |
| "4-bit 反而装不下" | ends on a negative | "4-bit 约 88GB，略高于单卡；3-bit 的 63GB 才把 175B 放进一张 A100" |
| "论文自述局限" | frames the section as a confession | "需要说明的边界" |

### What to keep

- Every number, table, figure, and experimental condition.
- Every genuine boundary: "只适用于无截断的格", "校准分布偏移时不成立", "逐层最优不等于端到端最优".
- The difference between "近似" and "等价". Do not call an approximation exact.

### What to add

- A one-sentence contribution statement on the method overview page.
- The strongest 2–3 numbers on the experiment conclusion pages.
- A closing sentence on the paper's lasting role, not a new limitation.

### Fact/claim discipline

- If a result is not in the paper, do not put it on a slide.
- If a result is in the paper but not a strength, do not make it the main battlefield.
- If a comparison is unfavorable, narrow the claim, change the evaluation dimension, or state it as a boundary. Never change the number.
- Attribute first-time claims: "论文报告，这是第一次……".

---

## 2. Academic-humanizer pass

### Remove

- **Em dashes** (`——`): replace with commas, colons, parentheses, or separate sentences.
- **Filler**: "其实", "真正", "事实上", "值得一提的是", "众所周知".
- **Empty intensifiers**: "非常", "显著", "极大地", "完全", "唯一" (unless literal).
- **Negative parallelism** used as hype: "不是 X，而是 Y" → state Y directly. Keep contrast only when it is a real technical distinction.
- **Rule-of-three padding**: three adjectives that add no information.
- **Overlong clause chains**: split at semicolons; one idea per sentence.
- **Over-claiming verbs**: "证明", "保证", "彻底解决" → "显示", "在本文设置下", "报告".
- **Vague attributions**: "很多工作认为" → name the work or cut.
- **AI vocabulary**: "赋能", "闭环", "抓手", "范式", "生态" when used abstractly.

### Keep

- Evidence-tied hedging: "在本文的设置下", "论文报告", "这一趋势在 OPT 和 BLOOM 上都出现".
- Technical terms and symbols unchanged.
- Passive voice when the actor is irrelevant.
- Semicolons and an occasional triple, in moderation.

### Split long sentences

Before:

> 复杂度从 A 降到 B，加速 C 倍；4096 的方阵就是四千倍量级。

After:

> 复杂度从 A 降到 B。加速 C 倍，4096 的方阵就是四千倍量级。

Before:

> 代码里有三次调用：第一次……；第二次……；第三次……。

After:

> 代码里有三次调用。第一次……。第二次……。第三次……。

### Claim-evidence check

For every empirical sentence, ask:

1. Is there a number, table, figure, or section behind it?
2. Does the verb match the strength of that evidence?
3. Is the comparison against the strongest baseline, not the weakest?

Examples:

- "4-bit 基本无损" → "4-bit 下 OPT-175B 是 8.37 对 8.34，BLOOM-176B 是 8.21 对 8.11" (evidence added).
- "3-bit 也能用" → "3-bit 下 RTN 崩溃到 7300 / 571，GPTQ 仍在 8.68 / 8.64" (comparison added).
- "它是最好的方法" → "在本文比较的模型中，它的 4-bit PPL 最低" (scope narrowed).

---

## 3. Script-specific rules

- Write for the ear, not the eye: short sentences, explicit transitions, repeated terms instead of elegant variation.
- Define every term at first use: FP16, PTQ, RTN, PPL, Hessian, KV cache.
- Read formulas as words: "分母是这一步的价格，列是误差的传力路径".
- Every page ends with a transition sentence: "时间问题解决了，但带宽还在，于是有了第二个改造".
- Do not say "左边这张图" without describing what it shows; listeners may not see it.
- One page of script = 600–1000 Chinese characters; total length scales with the actual page count.

---

## 4. Final check

- [ ] No `——`.
- [ ] No "其实/真正/事实标准/显著" unless quoting.
- [ ] No sentence over 100 Chinese characters unless it is a list.
- [ ] Every number has a source in the paper.
- [ ] Every boundary is a claim boundary, not a confession.
- [ ] The last page ends on the paper's role, not on a new limitation.
