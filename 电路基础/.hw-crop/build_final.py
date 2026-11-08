# -*- coding: utf-8 -*-
"""从教材扫描照片裁剪出作业题目，排版为 A4 PDF。"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np, sys

RAW = {n: f'raw_p{n:02d}.jpg' for n in range(1, 12)}

PIECES = [
 ('E3-1',  [(3,  440, 2170, 2200, 2330), (3,  460, 2550, 2060, 3585)]),
 ('E3-4',  [(3,  480, 3730, 2650, 3900), (3, 1850, 3870, 3860, 4900)]),
 ('E3-6',  [(4,  700,  620, 3320,  850), (4, 2100, 1180, 3500, 2030)]),
 ('E3-9',  [(4,  760, 3345, 2250, 3520), (4,  900, 3640, 2120, 4720)]),
 ('E3-14', [(5,  180, 1085, 3960, 1545), (5,  420, 1480, 4160, 2330)]),
 ('E3-17', [(5,  250, 3990, 3650, 4285), (6,   50,  755, 2160, 1405)]),
 ('E3-20', [(5,  250, 4690, 3650, 5015), (6, 2300, 1345, 3530, 2265)]),
 ('E3-29', [(7,  500, 3390, 3700, 3525), (7,  900, 3530, 3610, 4315)]),
 ('E3-30', [(7,  450, 4385, 3650, 4785), (8, 1000, 1145, 1910, 1880)]),
]
TITLE = '电路  第3章  作业题  E3-1 / E3-4 / E3-6 / E3-9 / E3-14 / E3-17 / E3-20 / E3-29 / E3-30'

DPI = 150
PW, PH = int(8.27 * DPI), int(11.69 * DPI)
MARGIN = int(0.42 * DPI)
GAP = int(0.20 * DPI)
CONTENT_W = PW - 2 * MARGIN
USABLE_H = PH - 2 * MARGIN
BORDER = 3
FONT_CJK = '/System/Library/Fonts/STHeiti Light.ttc'
FONT_LAT = '/System/Library/Fonts/Helvetica.ttc'


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def trim(im, thresh=178, pad=12):
    g = np.asarray(im.convert('L')).astype(np.int16)
    ink = g < thresh
    rows = np.nonzero(ink.sum(1) > 2)[0]
    cols = np.nonzero(ink.sum(0) > 2)[0]
    if not len(rows) or not len(cols):
        return im
    y0, y1 = max(0, rows[0] - pad), min(im.height, rows[-1] + pad + 1)
    x0, x1 = max(0, cols[0] - pad), min(im.width, cols[-1] + pad + 1)
    return im.crop((x0, y0, x1, y1))


def load(pg, x0, y0, x1, y1):
    return trim(Image.open(RAW[pg]).convert('RGB').crop((x0, y0, x1, y1)))


def fit(im, max_w, max_h):
    w, h = im.size
    s = min(max_w / w, max_h / h, 1.8)
    return im.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)


def build(out_pdf):
    f_title = font(FONT_CJK, 26)
    f_head = font(FONT_LAT, 30)
    f_foot = font(FONT_LAT, 16)
    pages = []
    for idx, (name, pieces) in enumerate(PIECES):
        canvas = Image.new('RGB', (PW, PH), 'white')
        d = ImageDraw.Draw(canvas)
        y = MARGIN
        if idx == 0:
            d.text((MARGIN, y), TITLE, font=f_title, fill=(20, 20, 20))
            y += 46
        d.text((MARGIN, y), f'题目 {name}', font=f_head, fill=(150, 0, 0))
        y += 42
        ims = [load(*p) for p in pieces]
        # text piece gets full width; figure piece is fitted to remaining space
        avail = USABLE_H - (y - MARGIN)
        for i, im in enumerate(ims):
            rest = len(ims) - i - 1
            if rest == 0:
                maxh = USABLE_H - (y - MARGIN)
            else:
                maxh = max(120, (USABLE_H - (y - MARGIN)) * 0.30)
            out = fit(im, CONTENT_W, maxh)
            x = (PW - out.width) // 2
            canvas.paste(out, (x, y))
            d.rectangle([x - BORDER, y - BORDER, x + out.width + BORDER - 1,
                         y + out.height + BORDER - 1], outline=(160, 160, 160), width=2)
            y += out.height + 2 * BORDER + GAP
        d.text((PW - MARGIN - 40, PH - MARGIN // 2 - 6), f'{idx + 1} / {len(PIECES)}',
               font=f_foot, fill=(130, 130, 130))
        pages.append(canvas)
    pages[0].save(out_pdf, 'PDF', resolution=DPI, save_all=True, append_images=pages[1:])
    return len(pages)


if __name__ == '__main__':
    n = build(sys.argv[1] if len(sys.argv) > 1 else 'homework_final.pdf')
    print('pages:', n)
