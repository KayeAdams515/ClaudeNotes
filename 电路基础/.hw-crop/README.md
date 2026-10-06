# 作业裁剪脚本（隐藏工作目录）

从教材扫描照片裁剪出作业题目并排版成 A4 PDF。

用法：

```bash
python3 extract_raw.py     # 从扫描 PDF 导出 raw_p01.jpg ... raw_p11.jpg（11 页）
python3 build_final.py out.pdf
```

- `extract_raw.py` 依赖的扫描件：`电路.pdf`（第3章习题页 r03–r08 = 书上第 103–109 页）。
- `build_final.py` 里的 `PIECES` 是每道题的裁剪框 `(扫描页号, x0, y0, x1, y1)`，扫描图为 4284×5712（横向页）或 5712×4284（跨页照片按 4284×5712 存）。
- 输出：`../C3 第3章作业题目（E3-1等9题）.pdf`
