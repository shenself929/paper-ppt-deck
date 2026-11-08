# Deck Structure Templates

Page counts below are reference shapes, not fixed targets. Decide the page count after the content outline, not before.

## 1. Choosing a template

| Paper type | Length | Core |
|---|---:|---|
| Single algorithmic paper | 按内容 | method + algorithm + complexity |
| Single empirical paper | 按内容 | setup + main effects + ablations |
| Theory paper | 按内容 | definitions + theorem chain + proof sketch |
| Series / lineage report | 按内容，不固定 | relations first, then main paper |

Default to the single-paper or series template. Add pages rather than shrinking type.

---

## 2. Single algorithmic paper (page count varies)

The numbers in the left column are a reference order, not a fixed page count. Merge, split, add, or drop rows as the content requires.

| Page | Role | Must contain | Common failure |
|---|---|---|---|
| 1 | Problem and cost | one concrete number that makes the problem real | starting with a generic "deep learning is important" |
| 2 | Why existing methods fail | 2–3 routes, each with a specific blocker | listing methods without saying where they break |
| 3 | Problem formulation | objective, notation, assumptions, boundary | formula without reading instructions |
| 4 | Precursor method | the one method the paper builds on | explaining three precursors and losing the thread |
| 5 | Precursor's bottleneck | 2–3 bottlenecks, each mapped to a fix | bottleneck list without consequences |
| 6 | Fix overview | bottleneck → fix → nature (approximate/equivalent) | no distinction between approximation and equivalence |
| 7–9 | Fixes one by one | mechanism, why correct, cost | repeating the overview without new detail |
| 10 | Full algorithm | pseudocode, annotation, complexity | pseudocode without mapping to fixes |
| 11 | Code correspondence | 15–25 lines, line-to-equation mapping | dumping 60 lines |
| 12 | Exact/approximate audit | table: step, nature, why, who challenges | hiding the approximation |
| 13 | Engineering | runtime, memory, block strategy | treating engineering as an afterthought |
| 14–15 | Experiment conclusions | 2 pages: accuracy + ability/deployment | full model-by-model tables |
| 16 | Assumptions and boundaries | 4–6 assumptions, when they fail, who picks up | ending on a list of weaknesses |
| 17 | Summary | 4 actions, 3 numbers, 1 lineage | restating the abstract |

If the paper has a strong theoretical component, expand pages 3–10 into definitions + theorem chain + proof sketch; keep experiments to 2 pages.

---

## 3. Series / lineage report (page count varies)

The page numbers below are a reference order only; use as many pages as the lineage and the main paper need.

Use this only when the user explicitly says "五篇论文""这条线""从 A 到 B" or asks to place a paper in a lineage. Do not add lineage pages on your own.

| Page | Role |
|---|---|
| 1 | One trunk + three branches diagram; one-line table of five papers |
| 2 | Shared objective; A/B/C/D four-link table |
| 3 | Relay table: inherited / left open / who picks up |
| 4 | Transition: three questions and one roadmap into the main paper |
| remaining | Main paper, following the single-paper template compressed by 1–2 pages; page count varies |

Rules:

- The main paper gets at least 60% of the pages.
- Do not give every paper equal space. The lineage page is context, not a literature review.
- Every relation must be traceable to a specific section or claim in the papers.
- If the user already has a lineage deck, reuse its diagram but re-check the numbers.

---

## 4. Page recipe: algorithm page

A good algorithm page has four layers:

1. **What problem is being solved** (one sentence).
2. **The mechanism** (formula or diagram).
3. **Why it works** (one paragraph, not a proof).
4. **What it costs** (complexity, memory, approximation).

Template:

```latex
\begin{frame}{判断句标题}
  \begin{block}{目标/问题}
    ...
  \end{block}
  \begin{columns}[T]
    \begin{column}{0.55\textwidth}
      % formula or diagram
    \end{column}
    \begin{column}{0.43\textwidth}
      % why it works / cost
    \end{column}
  \end{columns}
  \begin{columns}[t]
    \begin{column}[t]{0.49\textwidth}
      \begin{takeaway}{读法}
        这一段用 1–2 句说明公式怎么读：分子、分母、列各代表什么。
      \end{takeaway}
    \end{column}
    \begin{column}[t]{0.49\textwidth}
      \begin{takeaway}{代价}
        这一段用 1–2 句说明这个近似或改造的代价。
      \end{takeaway}
    \end{column}
  \end{columns}
\end{frame}
```

The old version put a single `explain` paragraph at the bottom. Do not do that: the explanation must sit in the content flow as 1–2 titled takeaway blocks, and the two blocks must not repeat each other.

---

## 5. Page recipe: experiment conclusion page

Do not paste the paper's full table. Use this structure:

- Left: one representative figure or a 2–4 row table.
- Right: three conclusions, each with one number.
- Bottom: a `takeaway{结论}` block with one sentence on what the result means. Do not use a separate footer band.

Example conclusion sentences:

- "4-bit 下主模型与 FP16 的差距是 0.03 / 0.10，基本可以当作无损替换。"
- "3-bit 下基线崩溃到 7300 / 571，本方法仍在 8.68 / 8.64。"
- "模型越大越好量化；唯一例外是 OPT-66B，原因是早期层死单元，不是方法失效。"

Rules:

- One page = one question ("准不准" or "能不能部署").
- Do not list every model size.
- If a number is not in the paper, do not put it on the slide.
- Add a small source line if the page mixes several tables: `来源：§5 Table 6 / Table 7`.

---

## 6. Page recipe: derivation page

Use a four-step chain:

1. Define the deviation and partition it.
2. Write the quadratic objective in block form.
3. Take the derivative / apply the block-inverse identity.
4. Substitute back and read the result.

At the bottom, add a "读法" block with three bullets: numerator, denominator, column. If the page already has a derivation block, merge the reading into it; do not add a second footer band.

Do not skip the "why this identity" step; that is where listeners get lost.

---

## 7. Page recipe: summary page

Use three blocks:

- **Four actions**: the method in four verbs.
- **Three numbers**: the three numbers you want the audience to remember.
- **One lineage**: where this paper sits and what it changes.

End with one sentence that states the paper's lasting role, not a list of limitations.

---

## 8. Length control

- Body text overflows: split the page, do not shrink below 7pt.
- Table overflows: use fixed cm widths; reduce text, not font below 6.5pt.
- Code overflows: 5.0–5.5pt, remove blank lines, keep the core loop.
- Explanatory paragraph overflows: cut 20–30 characters; do not delete the whole paragraph.
- If a page has more than 3 blocks plus a formula plus a paragraph, split it.

Page count is not fixed. A detailed deck usually takes 2–3 minutes per page with the script. If the script is under ~600 characters per page, it is probably too thin for "listeners can understand without slides".
