# paper-ppt-deck

把一篇研究论文做成 **中文 Beamer 汇报 PPT + 逐页详细演讲稿** 的 ZCode / Claude-style skill。

A reusable skill that turns a paper (PDF or LaTeX source) into a dense, readable Chinese Beamer deck and a page-by-page speaker script.

---

## What it produces

- A 16:9 Beamer deck with an academic blue style, no cover / TOC / references page.
- Every slide ends with an **unlabeled** light-blue explanatory paragraph, so readers can understand the slide without a presenter.
- Method and algorithm pages dominate; experiments are compressed to conclusions, not full tables.
- A speaker script mapped 1:1 to the PDF pages, written in spoken Chinese, explaining terms, formulas, and numbers so listeners can follow without seeing the slides.
- Optional lineage mode: if and only if the user explicitly asks for a multi-paper relationship report, it adds a “one trunk + branches” section before the main paper.

## Install

Copy this folder into one of the skill discovery directories:

```text
~/.agents/skills/paper-ppt-deck/
```

or, for a single project:

```text
<project>/.agents/skills/paper-ppt-deck/
```

ZCode discovers skills at session start, so start a new session after installing.

## Usage

In a new session:

```text
用 paper-ppt-deck 把 D:\papers\my-paper.pdf 做成组会汇报 PPT，
页数按内容定，每页有解释文字；实验只讲结论；再配一份详细讲稿。
```

Or force-load the skill:

```text
/skill paper-ppt-deck 把这篇论文做成论文精读 PPT 和讲稿
```

### Lineage mode

Only when you explicitly ask:

```text
用 paper-ppt-deck 做一份五篇论文的脉络汇报，先讲五篇的关系，再重点讲 GPTQ。
页数按内容定。
```

Without that request, the skill focuses on the single paper and does not build a literature review.

## Structure

```text
paper-ppt-deck/
├── SKILL.md                     # trigger, workflow, style contract, quality gates
├── references/
│   ├── deck-structure.md        # page-order templates (not fixed page counts)
│   ├── authoring-rules.md       # Beamer/table/code/figure rules and overflow fixes
│   ├── language-passes.md       # anti-defensive → academic-humanizer checklist
│   └── test-prompts.md          # three realistic test prompts
├── assets/
│   ├── beamer-preamble.tex      # reusable preamble with the unlabeled explain box
│   ├── script-template.md       # speaker-script skeleton
│   └── metropolis/              # Metropolis theme files (CC BY-SA 4.0)
└── scripts/
    ├── render_check.py          # render PDF, check page edges and leftover labels
    └── extract_explain.py       # extract explain blocks into a script skeleton
```

## Requirements

- XeLaTeX from TeX Live 2025+ (or a TeX distribution with `xeCJK`, `beamer`, `tikz`, `listings`).
- Python 3 and PyMuPDF for the optional scripts:

```bash
pip install pymupdf
```

The Metropolis theme is bundled under `assets/metropolis/`; if your TeX distribution cannot find it, copy those `.sty` files into the working directory.

## Design principles

1. **Content before page count.** There is no fixed page target. Add pages when a page is dense; never shrink text to hide overflow.
2. **Single paper by default.** Do not fabricate a literature lineage unless the user asks for one.
3. **Every number has a source.** A claim on a slide must point back to a table, figure, or section in the paper.
4. **Experiments are conclusions, not tables.** Two pages are usually enough.
5. **Language passes in order:** anti-defensive first (decide the claim), then academic-humanizer (clean the prose). Facts, numbers, and necessary boundaries are preserved.
6. **No “讲述” label.** The bottom paragraph is part of the slide, not a speaker-note strip.

## License

The skill text, templates, and scripts are released under the MIT License. See `LICENSE`.

The bundled Metropolis theme files are third-party software under CC BY-SA 4.0. See `THIRD_PARTY_NOTICES.md`.

## Acknowledgements

- [Metropolis Beamer theme](https://github.com/matze/mtheme) by Matthias Vogelgesang and contributors, CC BY-SA 4.0.
- The workflow was distilled from a real paper-reading deck and speaker-script iteration.
