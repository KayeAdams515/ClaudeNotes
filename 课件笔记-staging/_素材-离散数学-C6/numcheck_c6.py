#!/usr/bin/env python3
"""把笔记里出现的组合数值全部抽出来独立复算。只报"抽出来的式子 + 算出来的值"，
   让人工核对哪些与正文写的不一致（正文里的结果需要人眼比对，本脚本至少保证式子本身不算错）。"""
import os, re, sys
from math import comb, perm, factorial

COURSE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "离散数学")

PATTERNS = [
    (re.compile(r"P\((\d+),\s*(\d+)\)"), lambda a, b: ("P", a, b, perm(a, b))),
    (re.compile(r"C\((\d+),\s*(\d+)\)"), lambda a, b: ("C", a, b, comb(a, b))),
    (re.compile(r"\\binom\{(\d+)\}\{(\d+)\}"), lambda a, b: ("binom", a, b, comb(a, b))),
]

def main(files):
    bad = 0
    for f in files:
        text = open(f, encoding="utf-8").read()
        # 去掉 fenced code 之外的都算；这里全都算，重复无妨
        hits = []
        for pat, mk in PATTERNS:
            for m in pat.finditer(text):
                a, b = int(m.group(1)), int(m.group(2))
                if b > a:
                    print(f"  [!] {os.path.basename(f)}: {m.group(0)} —— r > n，式子本身有问题")
                    bad += 1
                    continue
                kind, _, _, val = mk(a, b)
                hits.append((m.group(0), val))
        # 阶乘
        for m in re.finditer(r"(?<![\d.])(\d{1,3})!", text):
            n = int(m.group(1))
            hits.append((f"{n}!", factorial(n)))
        seen = {}
        for s, v in hits:
            seen.setdefault(s, v)
        print(f"\n## {os.path.basename(f)}  —— {len(seen)} 个不同式子")
        for s in sorted(seen, key=lambda x: (len(x), x)):
            print(f"   {s:<22} = {seen[s]}")
    print(f"\n式子本身有问题的：{bad} 条")
    return 0

if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        files = [os.path.join(COURSE, x) for x in sorted(os.listdir(COURSE))
                 if x.startswith("C6") and x.endswith(".md")]
    sys.exit(main(files))
