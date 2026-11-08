# Test Prompts

Use these to check whether the skill triggers and produces the right shape. Run one at a time in a fresh turn.

## 1. Single paper, group meeting

> 把 `D:\...\paper.pdf` 做成组会汇报 PPT，页数你按内容定。每页用 1–2 个带标题的模板框放解释，不要单独做底部灰带，也不要写“讲述”。实验只讲结论，不要把所有表都列出来。再给我一份逐页详细讲稿，听众不看幻灯片也能听懂。

Expected:

- Finds the paper's LaTeX source if available; otherwise uses PDF.
- Produces `*_PPT/` with `main.tex`, `*_完整版_*.pdf`, `*讲稿_*.md`.
- No cover/TOC/references.
- Experiment section is 2 pages, not a dump.
- Explanation lives in 1–2 titled `takeaway` blocks per page, in the content flow, not in a footer band.
- Script is 1:1 with pages and has transitions.

## 2. Series / lineage report

> 这是五篇论文的目录。帮我做一份脉络汇报，页数按内容定；先讲五篇论文的关系，再重点讲 GPTQ。每页用带标题的模板框放解释，最后配一份详细讲稿。

Expected:

- Pages 1–4 are lineage: trunk + branches, shared objective, relay table, transition.
- Main paper gets at least 60% of pages.
- Relations are verified against papers, not copied from an old deck.
- Script explains why each paper is a relay, not just a list of names.

## 3. Revise an existing deck

> 把现有 PPT 改成读者能看懂的版本：不要写“讲述”，每页用多个带标题的模板框放解释，实验只留结论。讲稿要详细一点，听众不看幻灯片也能跟上。

Expected:

- Removes the “讲述/讲稿” label.
- Converts any footer explanation band into 1–2 titled takeaway blocks in the content flow.
- Replaces bullet-only pages with prose explanations.
- Compresses experiment pages to conclusions.
- Expands the script with terminology and formula explanations.
