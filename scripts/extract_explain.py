# -*- coding: utf-8 -*-
"""Extract frame titles and `takeaway` blocks from a Beamer .tex file.

Usage:
  python extract_explain.py main.tex script_skeleton.md

The deck convention is 1-2 `takeaway{标题}` blocks per frame, placed in the
content flow. This script concatenates them into a per-page draft.
"""
import argparse
import re
import sys


def clean(text):
    text = re.sub(r"\\textbf\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\underline\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\texttt\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\hl\{([^{}]*)\}", r"\1", text)
    text = text.replace("\\Hinv", "H^{-1}")
    text = text.replace("\\widehat W", "\\hat W")
    text = text.replace("\\Delta", "\\Delta ")
    text = re.sub(r"[ \t]+", " ", text)
    text = text.replace("\n", " ")
    return text.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("out")
    args = ap.parse_args()

    src = open(args.tex, encoding="utf-8").read()
    frames = re.findall(
        r"\\begin\{frame\}(?:\[[^\]]*\])?\{([^\n]*)\}(.*?)\\end\{frame\}",
        src,
        re.S,
    )
    if not frames:
        print("no frames found")
        sys.exit(1)

    lines = [
        f"# 演讲稿骨架（{len(frames)} 页）\n",
        "> 由 extract_explain.py 从 Beamer 源文件生成。每页 takeaway 模板框已抽出，需扩写成口语讲稿并补过渡。\n",
        "---\n",
    ]
    for i, (title, body) in enumerate(frames, 1):
        blocks = re.findall(
            r"\\begin\{takeaway\}\{([^{}]*)\}(.*?)\\end\{takeaway\}", body, re.S
        )
        if blocks:
            pieces = []
            for btitle, btext in blocks:
                pieces.append(f"【{clean(btitle)}】{clean(btext)}")
            text = " ".join(pieces)
        else:
            text = "（未找到 takeaway 模板框）"
        lines.append(f"## 第 {i} 页 · {title}\n")
        lines.append("**讲稿**\n")
        lines.append(text + "\n")
        lines.append("**过渡**\n")
        lines.append("（补一句到下一页的过渡）\n")
        if i < len(frames):
            lines.append("---\n")

    open(args.out, "w", encoding="utf-8").write("\n".join(lines))
    print(f"written {args.out}: {len(frames)} pages")


if __name__ == "__main__":
    main()
