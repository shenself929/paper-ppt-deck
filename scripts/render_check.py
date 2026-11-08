# -*- coding: utf-8 -*-
"""Render a Beamer PDF and run cheap layout checks.

Usage:
  python render_check.py deck.pdf preview/ --log main.log --dpi 110
"""
import argparse
import os
import re
import sys

try:
    import fitz  # PyMuPDF
except Exception as exc:
    print("PyMuPDF is required: pip install pymupdf", exc)
    sys.exit(2)


def parse_log(path):
    vbox, hbox = [], []
    if not path or not os.path.exists(path):
        return vbox, hbox
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = re.search(r"Overfull \\vbox \(([\d.]+)pt too high\)", line)
            if m:
                vbox.append(float(m.group(1)))
            m = re.search(r"Overfull \\hbox \(([\d.]+)pt too wide\)", line)
            if m:
                hbox.append(float(m.group(1)))
    return vbox, hbox


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("outdir")
    ap.add_argument("--log", default=None)
    ap.add_argument("--dpi", type=int, default=110)
    ap.add_argument("--margin", type=float, default=6.0)
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    doc = fitz.open(args.pdf)
    print(f"pages: {len(doc)}")

    bad = []
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=args.dpi)
        pix.save(os.path.join(args.outdir, f"page{i:02d}.png"))

        w, h = page.rect.width, page.rect.height
        blocks = page.get_text("blocks")
        if not blocks:
            continue
        maxx = max(b[2] for b in blocks)
        maxy = max(b[3] for b in blocks)
        if maxx > w - args.margin or maxy > h - args.margin:
            bad.append((i, round(maxx, 1), round(maxy, 1), round(w, 1), round(h, 1)))

    text = "".join(p.get_text() for p in doc)
    for word in ("讲述", "讲稿", "演讲提示"):
        if word in text:
            print(f"WARN: PDF contains {word!r}")

    if bad:
        print("WARN: text near page edge on:")
        for row in bad:
            print(f"  page {row[0]}: maxx={row[1]} maxy={row[2]} (page {row[3]}x{row[4]})")
    else:
        print("edge check: OK")

    vbox, hbox = parse_log(args.log)
    if vbox:
        print(f"Overfull vbox: {len(vbox)} (max {max(vbox):.1f}pt)")
        print("  " + ", ".join(f"{v:.1f}" for v in sorted(vbox, reverse=True)[:12]))
    if hbox:
        print(f"Overfull hbox: {len(hbox)} (max {max(hbox):.1f}pt)")
        print("  " + ", ".join(f"{v:.1f}" for v in sorted(hbox, reverse=True)[:12]))
    if not vbox and not hbox:
        print("log check: no Overfull warnings")

    print(f"preview written to: {args.outdir}")


if __name__ == "__main__":
    main()
