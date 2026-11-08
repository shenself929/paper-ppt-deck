# Authoring Rules (Beamer, Chinese, dense slides)

## 1. Preamble

Start from `assets/beamer-preamble.tex`. It already sets:

- Metropolis, 16:9, no section pages, progress bar in frametitle.
- Academic blue/gold palette.
- Microsoft YaHei for Chinese, Segoe UI for Latin.
- `amsmath`, `booktabs`, `tabularx`, `tikz`, `listings`.
- `\Hinv`, `\quant`, `\hl`, `\good`, `\bad`.
- The `takeaway` environment: a normal `block` with a short title, used 1–2 times per page to carry explanation.

If the project does not have the theme files, copy `assets/metropolis/*.sty` into the working directory. If `xelatex` still cannot find the theme, add the directory to `TEXINPUTS`.

Use `9pt` for dense 20+ page decks; `10pt` only if the page count can grow. At 9pt, body `\footnotesize` is about 7.2pt and `\scriptsize` about 6.3pt.

---

## 2. Integrated takeaway blocks

Do not use a separate full-width explanation band at the bottom of a page. Explanation is carried by **1–2 normal `block`s** with short judgment titles, placed in the content flow.

```latex
\begin{columns}[t]
\begin{column}[t]{0.49\textwidth}
\begin{takeaway}{读法}
...
\end{takeaway}
\end{column}
\begin{column}[t]{0.49\textwidth}
\begin{takeaway}{代价}
...
\end{takeaway}
\end{column}
\end{columns}
```

The environment is defined in the preamble:

```latex
\newenvironment{takeaway}[1]
  {\begin{block}{#1}}
  {\end{block}}
```

Rules:

- Prefer merging the explanation into an existing `block`; add a second block only when the page needs a separate “读法 / 结论 / 边界”.
- The two blocks must answer different questions. Do not repeat the same sentence in both.
- Titles are short judgments (“为什么模态免费”, “代价”, “边界”), never “讲述 / 讲稿 / 小结 / 本页内容”.
- Keep 2–4 sentences total across the pair; each block 1–2 sentences or 2–3 bullets.
- Place the blocks in the content flow, not glued to the bottom. Do not use `\vfill` to push them down.
- If the page already has two or more blocks, do not add a duplicate pair; merge the remaining prose into one block or repurpose one block.

---

## 3. Tables

The most common failure is a `tabularx` with `p{0.36\linewidth}` columns: the text can overflow into the next column or the table can exceed the page. Use **fixed cm widths** and `>{\raggedright\arraybackslash}`:

```latex
{\scriptsize\linespread{1.15}\selectfont
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.35}
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{1.0cm}%
  >{\raggedright\arraybackslash}p{2.5cm}%
  >{\raggedright\arraybackslash}p{5.4cm}X@{}}
...
\end{tabularx}}
```

Rules:

- Add `\linespread{1.15}\selectfont` inside the table group; global `\linespread{0.95}` makes multi-line cells cramped.
- Set `\arraystretch` to 1.3–1.5 for multi-line cells; add `\addlinespace[1.2pt]` between rows if needed.
- If a cell contains long math, put the math on its own line or shorten the text; a `$...$` token cannot break.
- For 5-column tables, use 6.5–7pt and drop a non-essential column rather than shrinking below 6pt.
- Check the right edge: if the last column touches the page border, reduce its width or shorten the header.

---

## 4. Code listings

Use `[fragile]` frames:

```latex
\begin{frame}[fragile]{代码对照：核心实现}
  \begin{lstlisting}[language=Python,
    basicstyle=\ttfamily\fontsize{5.4}{6.2}\selectfont,
    breaklines=true]
...
  \end{lstlisting}
\end{frame}
```

Rules:

- 15–22 lines per page. If longer, split the page or cut non-core lines.
- Remove blank lines before shrinking the font.
- Use `columns=fullflexible`, `keepspaces=true`, `showstringspaces=false`.
- Escape `_` in text mode (`static\_groups`), not inside `lstlisting`.
- Do not put a `lstlisting` inside a `block` with a long title unless you have checked the height; the block padding can push the last line off the page.

---

## 5. Figures and TikZ

- Prefer the paper's original figure or a redrawn TikZ; always caption it: `原文 Figure X 的重绘`.
- Set a fixed width (e.g. `width=0.95\linewidth`) and check the height; a 2.8:1 figure is safe, a square figure may eat half the page.
- For bar charts, use a simple TikZ with `x=0.018cm` per GB and label values at the bar end. Check that the longest label (`326 GB`) fits inside the column.
- For lineage diagrams, use three rows: trunk (3 boxes), branches (3 boxes), and one caption line. Do not let branch arrows cross labels.

---

## 6. Overfull troubleshooting order

1. `Overfull \vbox > 10pt`: the page is too tall. Cut 1–2 lines of body text or split the page.
2. `Overfull \vbox < 10pt`: reduce the takeaway text by 10–20 characters, or tighten the block spacing.
3. `Overfull \hbox` in a table: use fixed cm widths, `\raggedright`, and shorten the longest cell.
4. `Overfull \hbox` in a paragraph: look for an unbreakable token (`LLM.int8()`, a long formula, a URL); rephrase or add `\allowbreak`.
5. Code page: reduce `basicstyle` from 6.3pt to 5.4pt, remove blank lines, then cut lines.
6. Table page: reduce `\arraystretch` before reducing font; if still over, drop a row.

Never use `\shrink` or `\resizebox` on a whole frame. It hides the problem and makes the page inconsistent.

---

## 7. Visual QA

Render every page at 110–150 dpi and inspect. Check:

- Takeaway blocks: are the last lines visible? Do any two blocks repeat the same point?
- Table: does any cell cross the column boundary?
- Code: is the last line inside the frame?
- Figure: are axis labels readable at the final size?
- Title: is it a judgment, not a generic noun?
- Page balance: is there a large empty band that could hold a missing explanation?

If a visual-judge agent is available, use it on the PNGs. If not, inspect the PNGs in the main session; do not rely on `.log` alone.

---

## 8. Chinese typesetting

- Use `xeCJK` with Microsoft YaHei; set `BoldFont=Microsoft YaHei Bold`.
- Use `\setCJKmonofont{SimSun}` for code comments if needed.
- Do not put Chinese inside `\texttt{}` unless the font supports it.
- Use full-width punctuation in Chinese prose; use `$...$` for math.
- Avoid em dashes in the final script; in slides, use commas or parentheses.

---

## 9. Silent failures in Beamer frames

These fail without an error in the log. Check them before debugging the content.

### 9.1 A frame body that starts with `{`

Symptom: a whole table or a whole block compiles with no Error/Overfull, but is missing from the PDF.

Cause: Beamer parses a leading brace group in the frame body as a grouping/overlay specification and drops it.

Fix: use `\begingroup ... \endgroup` instead of `{ ... }`:

```latex
\begin{frame}{...}
\begingroup\scriptsize
...
\endgroup
\end{frame}
```

Do not write `{\scriptsize ... }` as the first thing after `\begin{frame}`.

### 9.2 The last table column wraps one character per line

Symptom: the last column of a `tabularx` shows two or three characters per line.

Cause: the `X` column receives the leftover width, which is too small.

Fix: give the last column a fixed `p{2.8cm}`, move `X` to the long-text column, or drop a non-essential column. Reduce `\tabcolsep` to 2pt before reducing the font.

### 9.3 A flow diagram is 3–20pt too wide

Symptom: `Overfull \hbox` at the `\end{frame}` line, diagram touches the right edge.

Fix: reduce node `text width` first, then the `x=` scale. Never wrap the whole `tikzpicture` in `\resizebox`; it makes fonts inconsistent across pages.

### 9.4 Source line height varies from page to page

Symptom: the `\src{}` line floats at different heights, so pages look top-heavy or bottom-heavy.

Fix: put `\vfill` immediately before `\src{}` in every frame.

---

## 10. Flowchart recipes

Use `assets/flow-snippets.tex` for three copy-paste skeletons.

### 10.1 Method overview pipeline

- Five nodes, width 2.1–2.3cm, center spacing 2.8cm, `minimum height` 1.1–1.2cm.
- Arrow labels above the arrows, `\sffamily\scriptsize`, 2–5 characters.
- Under the chain, two braces: “改目标” over the modeling stages and “改变量” over the relaxation/hardening stages.
- If the chain exceeds `\textwidth`, reduce node width to 2.0cm before shrinking the font.

### 10.2 Two-lane data-flow diagram

- Two rows, 1.2cm apart; each row has 3–4 nodes of 1.8–1.9cm.
- First node of each row states the input regime: `x (FP32)` on top, `x̂ (已量化)` below.
- A loss box on the right, 3.2cm wide, receives arrows from both lanes.
- Use a dashed arrow from the previous-layer block into `x̂` when the point is “input already quantized”.

### 10.3 Per-layer loop diagram

- Five nodes stacked vertically, 1.0–1.1cm apart.
- Last node → right → up → first node, with the label `ℓ←ℓ+1`.
- Put the loop on the left 55–60% of the page and the two takeaway blocks on the right.

### 10.4 Knob diagram for continuous relaxation

- A horizontal axis with ticks at `floor` and `ceil`, a filled dot at `h(V)`, and a double arrow above labeled “0 → 1”.
- Width 5–6cm; it fits under a formula in a 0.55 column.
