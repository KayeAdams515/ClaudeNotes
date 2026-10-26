#!/usr/bin/env python3
"""按页面归一化坐标裁切 PDF 里的图（矢量图也能裁）。

用法:
  python3 crop_frac.py --page 15 --frac 0.05,0.20,0.95,0.31 --out attachments/C10-xxx.png [--scale 4]

--frac 是 (x0,y0,x1,y1)，都以页面宽/高的比例给出（0=左/上，1=右/下）。
默认 PDF 为 离散数学/pdfs/第十章.pdf，可用 --pdf 覆盖。
"""
import argparse, sys
import pymupdf

DEFAULT_PDF = "/Users/andyue/Library/CloudStorage/OneDrive-个人/文档/obsidian/离散数学/pdfs/第十章.pdf"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=DEFAULT_PDF)
    ap.add_argument("--page", type=int, required=True, help="物理页号，从 1 开始")
    ap.add_argument("--frac", required=True, help="x0,y0,x1,y1 归一化坐标")
    ap.add_argument("--out", required=True)
    ap.add_argument("--scale", type=float, default=4.0)
    a = ap.parse_args()
    x0, y0, x1, y1 = [float(v) for v in a.frac.split(",")]
    doc = pymupdf.open(a.pdf)
    page = doc[a.page - 1]
    r = page.rect
    clip = pymupdf.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height,
                        r.x0 + x1 * r.width, r.y0 + y1 * r.height)
    pix = page.get_pixmap(clip=clip, matrix=pymupdf.Matrix(a.scale, a.scale))
    pix.save(a.out)
    print(f"{a.out}  {pix.width}x{pix.height}  clip={clip}")

if __name__ == "__main__":
    main()
