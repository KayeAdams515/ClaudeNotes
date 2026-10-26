#!/usr/bin/env python3
"""自绘：Euler vs Hamilton —— 同一张图上的两种任务。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "attachments/C10.5-欧拉与哈密顿的区别.png"

# 六边形 + 内接三角形（0-2-4）：9 条边，全偶度，既有欧拉回路也有哈密顿回路
ang = {i: np.deg2rad(90 - 60 * i) for i in range(6)}
P = {i: (np.cos(ang[i]), np.sin(ang[i])) for i in range(6)}
rim = [(i, (i + 1) % 6) for i in range(6)]
tri = [(0, 2), (2, 4), (4, 0)]

# 复算过的欧拉回路：0-1-2-3-4-5-0-2-4-0（9 条边，每条一次）
euler = [0, 1, 2, 3, 4, 5, 0, 2, 4, 0]
hamil = [0, 1, 2, 3, 4, 5, 0]

fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.6), dpi=200)

def draw_base(ax):
    for (u, v) in rim:
        ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color="0.35", lw=1.4, zorder=2)
    for (u, v) in tri:
        ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color="0.35", lw=1.4,
                ls=(0, (4, 3)), zorder=2)
    for i in range(6):
        ax.plot(*P[i], "o", ms=11, color="0.15", zorder=5, mec="white", mew=1.2)
    for i in range(6):
        x, y = P[i]
        ax.text(x * 1.24, y * 1.24, "v%d" % i, ha="center", va="center",
                fontsize=12, color="0.1", zorder=6)
    ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal"); ax.axis("off")

# ---- 左：欧拉回路，走遍每条边一次 ----
ax = axes[0]
draw_base(ax)
for u, v in rim:
    ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color="#c0392b", lw=2.0, zorder=3)
for u, v in tri:
    ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color="#c0392b", lw=2.0,
            ls=(0, (4, 3)), zorder=3)
# 步骤号放在每条边的中点，向外偏一点
for k in range(len(euler) - 1):
    u, v = euler[k], euler[k + 1]
    mx, my = (P[u][0] + P[v][0]) / 2, (P[u][1] + P[v][1]) / 2
    # 无向图：同一对点可能出现两次（本回路里不会），按顺序标号
    ax.text(mx, my, str(k + 1), ha="center", va="center", fontsize=11,
            color="#1b4f72", fontweight="bold", zorder=7,
            bbox=dict(boxstyle="circle,pad=0.16", fc="white", ec="#1b4f72", lw=0.8))
ax.set_title("Euler circuit: walk every EDGE once\n"
             "v0-v1-v2-v3-v4-v5-v0-v2-v4-v0  (9 edges, 10 stops)",
             fontsize=11.5, color="0.12", pad=10)

# ---- 右：哈密顿回路，走遍每个点一次 ----
ax = axes[1]
draw_base(ax)
for u, v in rim:
    ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color="#1f6feb", lw=3.2, zorder=3)
for u, v in tri:
    ax.plot([P[u][0], P[v][0]], [P[u][1], P[v][1]], color="0.72", lw=1.1,
            ls=(0, (4, 3)), zorder=2.5)
ax.text(0, -0.12, "3 edges unused\n(the dashed ones)", ha="center", va="center",
        fontsize=9.5, color="0.45")
ax.set_title("Hamilton circuit: visit every VERTEX once\n"
             "v0-v1-v2-v3-v4-v5-v0  (6 vertices, 6 edges)",
             fontsize=11.5, color="0.12", pad=10)

fig.suptitle("Same graph, two different questions", fontsize=13.5, color="0.1", y=1.0)
fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight", facecolor="white")
print("saved", OUT)

# ---- 顺带复算 ----
edges = rim + tri
from collections import Counter
deg = Counter()
for u, v in edges:
    deg[u] += 1; deg[v] += 1
print("deg =", dict(sorted(deg.items())), " all even:", all(d % 2 == 0 for d in deg.values()))
pool = [tuple(sorted(e)) for e in edges]
ok = True
for k in range(len(euler) - 1):
    e = tuple(sorted((euler[k], euler[k + 1])))
    if e in pool:
        pool.remove(e)
    else:
        ok = False; print("bad step", k + 1, e)
print("欧拉回路合法且用尽 9 条边：", ok and not pool, "剩", len(pool))
