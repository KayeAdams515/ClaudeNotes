"""从原始扫描 PDF 重新导出 raw_p01.jpg ... raw_p11.jpg（供 build_final.py 使用）。"""
import pymupdf, pathlib
SRC = pathlib.Path('/Users/andyue/Library/Application Support/dsh-desktop/harness/'
                   'attachments/v1/files/e8/e8fb499233a2f4c90a03cc2cb445f01848f16454a7592361ed6a3a7fbbac3793/电路.pdf')
doc = pymupdf.open(SRC)
for i, page in enumerate(doc, 1):
    xref = page.get_images(full=True)[0][0]
    info = doc.extract_image(xref)
    pathlib.Path(f'raw_p{i:02d}.jpg').write_bytes(info['image'])
    print(f'raw_p{i:02d}.jpg', info['width'], 'x', info['height'])
