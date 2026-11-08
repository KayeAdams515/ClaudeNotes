#!/usr/bin/env python3
"""C6 逐篇验收：机械项全查一遍，只报事实。"""
import os, re, sys, unicodedata

STAGE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 课件笔记-staging
COURSE = os.path.join(STAGE, "离散数学")
ATT = os.path.join(COURSE, "attachments")
VAULT = "/Users/andyue/Library/CloudStorage/OneDrive-个人/文档/obsidian/离散数学"

SECTIONS = {
    "C6.1 计数基础 The Basics of Counting": ("6.1", 23),
    "C6.2 鸽巢原理 The Pigeonhole Principle": ("6.2", 13),
    "C6.3 排列与组合 Permutations and Combinations": ("6.3", 15),
    "C6.4 二项式系数与恒等式 Binomial Coefficients and Identities": ("6.4", 4),
    "C6.5 广义排列与组合 Generalized Permutations and Combinations": ("6.5", 11),
    "C6.6 生成排列与组合 Generating Permutations and Combinations": ("6.6", 5),
    "C6 计数 Counting MOC": ("MOC", 0),
}

ALLOWED_LINKS = set(SECTIONS) | {
    "C1 基础：逻辑与证明 MOC", "C2 基本结构：集合、函数、序列、求和与矩阵 MOC",
    "C9 关系 Relations MOC",
    "C1.1 命题逻辑 Propositional Logic", "C1.2 命题逻辑的应用 Applications of Propositional Logic",
    "C1.3 命题等价 Propositional Equivalences", "C1.4 谓词与量词 Predicates and Quantifiers",
    "C1.5 嵌套量词 Nested Quantifiers", "C1.6 推理规则 Rules of Inference",
    "C1.7 证明导论 Introduction to Proofs", "C1.8 证明方法与策略 Proof Methods and Strategy",
    "C2.1 集合 Sets", "C2.2 集合运算 Set Operations", "C2.3 函数 Functions",
    "C2.4 序列与求和 Sequences and Summations", "C2.5 集合的基数 Cardinality of Sets",
    "C2.6 矩阵 Matrices",
    "C9.1 关系及其性质 Relations and Their Properties",
    "C9.2 n 元关系与数据库 n-ary Relations and Their Applications",
    "C9.3 关系的表示 Representing Relations", "C9.4 关系的闭包 Closures of Relations",
    "C9.5 等价关系 Equivalence Relations", "C9.6 偏序 Partial Orderings",
}

def mask_fences(text):
    out, inside = [], False
    for line in text.split("\n"):
        if re.match(r"^(```|~~~)", line.strip()):
            inside = not inside
            out.append("")
            continue
        out.append("" if inside else line)
    return "\n".join(out)

def fm_split(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            block = "\n".join(lines[1:i])
            data = {}
            for line in block.split("\n"):
                m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
                if m:
                    data[m.group(1)] = m.group(2).strip().strip('"')
            return data, i
    return {}, 0

problems = []
def rep(msg):
    problems.append(msg)

for stem, (sec, nex) in SECTIONS.items():
    path = os.path.join(COURSE, stem + ".md")
    if not os.path.exists(path):
        rep(f"[缺文件] {stem}.md 还没写")
        continue
    text = open(path, encoding="utf-8").read()
    masked = mask_fences(text)
    fm, fm_end = fm_split(text)
    n = len(text.split("\n"))
    print(f"\n{'='*70}\n## {stem}.md   ({n} 行, {len(text)} 字符)")
    # 1 frontmatter
    for k in ("title", "course", "chapter", "section", "tags", "aliases", "source"):
        if k not in fm:
            rep(f"{stem}: frontmatter 缺 {k}")
    if fm.get("title") and fm["title"] != stem:
        rep(f"{stem}: title「{fm['title']}」≠ 文件名")
    if sec != "MOC" and fm.get("section") not in (sec, f'"{sec}"'):
        rep(f"{stem}: section「{fm.get('section')}」≠ {sec}")
    # 2 叙述层
    body = masked.split("\n")[fm_end + 1:]
    nar = [(i + fm_end + 2, l.strip()) for i, l in enumerate(body)
           if ("课件" in l or "幻灯片" in l) and not l.lstrip().startswith("|")]
    if nar:
        rep(f"{stem}: 叙述层出现「课件」{len(nar)} 处：{nar[:3]}")
    tone = [l.strip() for l in body if re.search(r"老师说|老师讲|老师提到|老师给", l)]
    if tone:
        rep(f"{stem}: 转述口吻 {len(tone)} 处：{tone[:3]}")
    st = [l.strip() for l in masked.split("\n") if re.search(r"课后自测|本节自测|Self-Test|self-test", l)]
    if st:
        rep(f"{stem}: 自测板块：{st[:3]}")
    # 3 图片
    imgs = re.findall(r"!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]", masked)
    missing = [im for im in imgs if not os.path.exists(os.path.join(ATT, im))]
    if missing:
        rep(f"{stem}: 图片不存在 {missing}")
    if not imgs and sec != "MOC":
        rep(f"{stem}: 一篇图都没有（请确认是否合理）")
    print(f"  图片 {len(imgs)} 张：{imgs}")
    # 4 双链
    links = re.findall(r"(?<!!)\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]", masked)
    bad = sorted({l for l in links if l.split('#')[0].strip() and l.split('#')[0].strip() not in ALLOWED_LINKS})
    if bad:
        rep(f"{stem}: 非法双链 {bad}")
    # 5 骨架
    for need in ("[!abstract]", "[!info]"):
        if need not in text:
            rep(f"{stem}: 缺 {need}")
    if sec != "MOC":
        for need, label in (("## 这一讲的三句话", "三句话"), ("### 速查表", "速查表"),
                            ("## 下一讲预告", "下一讲预告"), ("## 0. 开场", "开场"),
                            ("```mermaid", "mermaid 路线图")):
            if need not in text:
                rep(f"{stem}: 缺 {label}（{need}）")
    q = text.count("[!question]")
    if sec != "MOC" and q < 3:
        rep(f"{stem}: [!question] 只有 {q} 处（要求 ≥3）")
    print(f"  callout: question {q}, important {text.count('[!important]')}, "
          f"example {text.count('[!example]')}, warning {text.count('[!warning]')}, note {text.count('[!note]')}")
    # 6 例题覆盖（机械启发式）
    if nex:
        found = set()
        for m in re.finditer(r"(?:例|EXAMPLE)\s*([0-9]{1,2})", text):
            found.add(int(m.group(1)))
        absent = [k for k in range(1, nex + 1) if k not in found]
        print(f"  例题：教材共 {nex} 道，笔记里提到编号 {len([k for k in range(1,nex+1) if k in found])} 道"
              + (f"，缺 {absent}" if absent else "，齐全"))
        if absent:
            rep(f"{stem}: 例题编号 {absent} 未出现（需人工确认是否漏讲）")
    # 7 数字复算痕迹
    num = len(re.findall(r"复算|原印|原稿|python", text))
    print(f"  复算/纠错痕迹 {num} 处")

print(f"\n\n{'#'*70}\n共 {len(problems)} 条待处理：")
for p in problems:
    print("  -", p)
