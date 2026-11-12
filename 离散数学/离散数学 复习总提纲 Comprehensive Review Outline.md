# 离散数学 期末复习总提纲

> 覆盖第 1、2、6、8、9、10 章全部知识点（含课堂未讲但属教材范围的节），逐条给出中英术语对照。
>
> 依据：本库 `离散数学/` 下 35 篇分节讲义、6 个章节 MOC、3 篇作业与错题，以及 1–22 节课的录音转写稿。

## 使用说明

- **⭐** 老师课堂上点名会考、往年考过、或反复强调的内容。
- **⚠️** 高频失分点、易混约定、答题红线。
- **〔拓展〕** 课堂未讲、教材范围内、可能出现在卷面上的内容，按正文同等深度写出，复习时按时间取舍。
- 每个术语第一次出现时写成 **中文（English）**；全部术语另在附录 C 汇总。
- 配图沿用本库 `attachments/` 中的原图，按「图 章-序｜」编号，点击可放大；图注只说明它要讲的那一条结论。
- 每节或每章末尾的「自检」是最低通过线：三问问不出来，说明这一节还没到位。

## 考试情报卡（据第 17、22 节课宣布，以第 22 节为准）

| 项目 | 内容 |
|---|---|
| 时间 | **2026 年 11 月 19 日（周四）8:50–10:50**，共 120 分钟 |
| 地点 | **53A 210**（QQ 群同步通知） |
| 形式 | **闭卷**；**全英文作答**，卷面不得出现中文 |
| 范围 | 第 **9**、**6**、**8**、**10** 章为主；第 **1** 章仅 1 题；第 2 章 §2.1–2.3 课堂讲过，§2.4–2.6 未讲但属教材范围 |
| 题库 | 教材例题与课后习题（practice questions），"有些修改，但改动十分有限" |
| 重点 | 第 19 节课原话："**第十章最重要**"；第 21 节课补："哈密顿路径两年前考过一次" |
| 老师给的复习顺序 | 第 1 章 → 第 2 章 → 第 9 章 → 第 6 章 → 第 8 章 → 第 10 章 |
| 给分口径 | 平均分接近 90、中位数超过 90；59 分差 1 分到 60 会捞，89 分想要 90 不会帮 |

**三条全卷通行的答题规范**（老师三次强调）：

1. 每一步推导右侧必须写**规则名**（modus ponens、De Morgan's law…）或**规则表达式**；记不住名字写公式同样给分。
2. 结论是复合表达式时，必须推出**整个表达式**为真，不能推出各分量再口头组合。
3. 符号全卷统一：$\equiv$ 与 $\Leftrightarrow$ 选一种用到底；$\mathbf T/\mathbf F$ 不当变量用（代换用 $S,R$ 或 $A,B$）。

---

# 第一章 逻辑与证明 The Foundations: Logic and Proofs

**考试权重**：期末只保留 1 道题，但这一章是后面所有证明题的**语言**——推理规则、量词翻译、证明方法在计数、关系、图论里反复使用。按"会用"标准复习，不必按期中深度。

## 1.1 命题逻辑 Propositional Logic

**命题（proposition）**：陈述句，具有唯一的**真值（truth value）**，真 $\mathbf T$ 或假 $\mathbf F$。疑问句、祈使句、感叹句、含自由变量的句子、悖论都不是命题。

- **命题变量（propositional variable）** $p,q,r,s,\dots$，取值为真/假。
- **原子命题（atomic proposition）** 不可再分；**复合命题（compound proposition）** 由联结词组合而成。
- **真值表（truth table）**：$n$ 个变元共 **$2^n$ 行**；变元列按"折半交替"填（第一列前半 T 后半 F，逐列减半）；中间列按优先级由内向外逐列添加。

### 六个联结词（必背真值表）

| 表达式 | 名称 | 读法 | 为真的条件 |
|---|---|---|---|
| $\neg p$ | 否定 negation | not $p$ | $p$ 假 |
| $p\wedge q$ | 合取 conjunction | $p$ and $q$ | 两者皆真 |
| $p\vee q$ | 析取 disjunction（含或 inclusive or） | $p$ or $q$ | 至少一真 |
| $p\oplus q$ | 异或 exclusive or（排他或） | $p$ xor $q$ | 恰一真 |
| $p\to q$ | 蕴涵 implication / 条件语句 conditional statement | if $p$ then $q$ | **仅 $p$ 真 $q$ 假时为假** |
| $p\leftrightarrow q$ | 双条件 biconditional | $p$ iff $q$ | 同真同假 |

| $p$ | $q$ | $\neg p$ | $p\wedge q$ | $p\vee q$ | $p\oplus q$ | $p\to q$ | $p\leftrightarrow q$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| T | T | F | T | T | F | T | T |
| T | F | F | F | T | T | F | F |
| F | T | T | F | T | T | T | F |
| F | F | T | F | F | F | T | T |

### 条件语句的四个必考点

1. **术语**：$p$ 是**前件（antecedent / hypothesis / premise）**，$q$ 是**后件（consequent / conclusion）**。
2. **空真（vacuous truth）**：前件假时 $p\to q$ 恒真。这是**实质蕴涵（material implication）**——只由真值表定义，**不蕴涵任何因果关系**。⚠️ 选择题常拿"因为…所以…"的日常语义来设套。
3. **三种变形**：**逆命题（converse）** $q\to p$；**逆否命题（contrapositive）** $\neg q\to\neg p$；**否命题（inverse）** $\neg p\to\neg q$。⭐ **只有原命题与逆否命题等价**。
4. **八种英文说法**（翻译题必备）：if $p$, then $q$ · $p$ implies $q$ · $p$ only if $q$ · $q$ if $p$ · $q$ when/whenever $p$ · $p$ is sufficient for $q$ · $q$ is necessary for $p$ · $q$ unless $\neg p$。

> ⭐ **only if 的方向**：$p$ only if $q$ 是 $p\to q$；只有 **if and only if** 才是 $\leftrightarrow$。
>
> **充分条件（sufficient condition）** 放箭头左边，**必要条件（necessary condition）** 放箭头右边。

### 优先级 Precedence of Logical Operators（老师版，考试以此为准）

$$\boxed{\neg\ (1)\ >\ \wedge\ (2)\ >\ \vee,\ \oplus\ (3)\ >\ \to\ (4)\ >\ \leftrightarrow\ (5)}$$

- 教材 Table 8 未列 $\oplus$；**课件把 $\oplus$ 与 $\vee$ 并列为第 3 级**，以课件为准。
- 同级从左到右结合。加括号的通用算法：按优先级 1→5 逐级扫描，每级把该级运算连同操作数括起来，最外层（$\leftrightarrow$）不加括号。
- 例：$p\vee q\wedge r=p\vee(q\wedge r)$；$\neg s\wedge f=(\neg s)\wedge f$；$A\leftrightarrow f\to b=A\leftrightarrow(f\to b)$。

> ⭐ 课堂原话："优先级这种东西太容易出成考题了。"闭卷必须背下来。

### 位运算 Logic and Bit Operations

**位（bit）** 取值 0/1，对应 $\mathbf F/\mathbf T$；**位串（bit string）** 上的**按位运算（bitwise operations）** AND、OR、XOR 分别对应 $\wedge,\vee,\oplus$。

### 本节自检

1. "You can access the Internet only if you pay the fee" 译成什么？反过来 "only if" 换成 "if" 又是什么？
2. 写出 $p\to q$ 的逆、逆否、否，并指出哪两个等价。
3. $\neg p\vee q\leftrightarrow r$ 的默认括号怎么加？

## 1.2 命题逻辑的应用 Applications of Propositional Logic

### 翻译自然语言句子 Translating English Sentences

四步算法：① 划出原子命题并给字母；② 按句法确定联结词；③ 处理 **unless（$= \neg p\to q$）**、**but/however（$=\wedge$）**、"或"的含/排他歧义；④ 回读检验。

### 系统规约 System Specifications

- **系统规约（system specifications）**：用命题表达的约束集合；**一致的（consistent）** 当且仅当存在一组真值赋值使**所有**规约同时为真。
- 判定方法：真值表穷举，或由部分规约推出结论再与其余规约比对。
- ⭐ 常以"加一条规约后系统变得不一致"的小问出现；写答案必须**给出那组赋值**或**指出矛盾的两条**。

### 布尔检索 Boolean Searches

用 AND / OR / NOT 组合关键词，如 `(AI OR ML) AND NOT 1950`。

### 逻辑谜题 Logic Puzzles

**骑士与无赖（knights and knaves）**：骑士永真、无赖永假，按各人陈述列方程求解；**泥孩子问题（muddy children）**：公共知识推理。⚠️ 这类题必须**逐一验证**满足所有陈述，不能只给出答案。

### 逻辑电路 Logic Circuits

- **逻辑门（logic gates）**：反相器 inverter（NOT）、与门 AND gate、或门 OR gate、与非门 NAND、或非门 NOR、异或门 XOR。
- **组合电路（combinational circuit）**：多输入单输出的门网络；电路与命题表达式一一对应，**逻辑等价 ⟺ 电路等价**。

![[C1-图2-组合电路示例.png|560]]
*图 1-1｜组合电路：门网络与命题表达式一一对应，化简表达式就是化简电路*

### 加法器（拓展）

- **半加器（half adder）**：两个输入位 $x,y$，和 $s=x\oplus y$、进位 $c=x\wedge y$。
- **全加器（full adder）**：三个输入位 $x,y,c_i$，和 $s=x\oplus y\oplus c_i$，进位 $c_o=(x\wedge y)\vee\big(c_i\wedge(x\oplus y)\big)$。
- **行波进位加法器（ripple-carry adder）**：$n$ 个全加器串联，$n$ 位加法用 $2n-1$ 个门——这是"电路 ↔ 命题表达式"最标准的例子。

### 本节自检

1. 怎么证明一组规约不一致？给出两种写法。
2. "$q$ unless $p$" 与 "$q$ if not $p$" 是否同义？
3. 画一个实现 $(p\wedge\neg q)\vee r$ 的电路，最少几个门？

## 1.3 命题等价 Propositional Equivalences

### 四个基本概念（⭐ 必背定义）

| 术语 | 定义 | 判定 |
|---|---|---|
| **永真式（tautology / 重言式）** | 在**所有**真值赋值下都为真 | 真值表最后一列全 T |
| **矛盾式（contradiction）** | 在所有真值赋值下都为假 | 最后一列全 F |
| **可能式（contingency）** | 既非永真也非矛盾 | 最后一列 T、F 都有 |
| **可满足式（satisfiable）** | **存在**一组赋值使其为真 | 非矛盾式即可满足 |

⭐ 去年期末考过"什么是 tautology"，答题必须写出关键词 **under every truth assignment**，只写"总是真的"不够。
〔拓展〕**可满足性问题（satisfiability problem, SAT）**、**范式**与**功能完备**的完整内容见本节末「范式与功能完备」。

### 逻辑等价 Logical Equivalence

$p\equiv q$ 当且仅当对所有赋值 $p,q$ 真值相同，等价于 $p\leftrightarrow q$ 是永真式。两种证法：**真值表法（truth table）**、**等价推导法（a series of logical equivalences）**。

### 常用等价律（必背）

**Table 6 基本律**

| 名称 | 形式 |
|---|---|
| 同一律 identity laws | $p\wedge\mathbf T\equiv p$，$p\vee\mathbf F\equiv p$ |
| 支配律 domination laws | $p\vee\mathbf T\equiv\mathbf T$，$p\wedge\mathbf F\equiv\mathbf F$ |
| 幂等律 idempotent laws | $p\vee p\equiv p$，$p\wedge p\equiv p$ |
| 双重否定律 double negation | $\neg(\neg p)\equiv p$ |
| 交换律 commutative laws | $p\vee q\equiv q\vee p$，$p\wedge q\equiv q\wedge p$ |
| 结合律 associative laws | $(p\vee q)\vee r\equiv p\vee(q\vee r)$，$\wedge$ 同理 |
| 分配律 distributive laws | $p\vee(q\wedge r)\equiv(p\vee q)\wedge(p\vee r)$，$p\wedge(q\vee r)\equiv(p\wedge q)\vee(p\wedge r)$ |
| **德摩根律 De Morgan's laws** | $\neg(p\wedge q)\equiv\neg p\vee\neg q$，$\neg(p\vee q)\equiv\neg p\wedge\neg q$ |
| 吸收律 absorption laws | $p\vee(p\wedge q)\equiv p$，$p\wedge(p\vee q)\equiv p$ |
| 否定律 negation laws | $p\vee\neg p\equiv\mathbf T$，$p\wedge\neg p\equiv\mathbf F$ |

**含蕴涵的等价（只背第一条，其余可推）**

- ⭐ **$p\to q\equiv\neg p\vee q$**（消箭头核心公式）
- ⭐ $p\to q\equiv\neg q\to\neg p$（逆否等价）
- ⭐ **$\neg(p\to q)\equiv p\wedge\neg q$**（条件语句的否定）
- $p\vee q\equiv\neg p\to q$；$p\wedge q\equiv\neg(p\to\neg q)$
- $(p\to q)\wedge(p\to r)\equiv p\to(q\wedge r)$；$(p\to r)\wedge(q\to r)\equiv(p\vee q)\to r$
- $(p\to q)\vee(p\to r)\equiv p\to(q\vee r)$；$(p\to r)\vee(q\to r)\equiv(p\wedge q)\to r$

**含双条件的等价**

- ⭐ $p\leftrightarrow q\equiv(p\to q)\wedge(q\to p)$（**证"当且仅当"就是证两个方向**）
- $p\leftrightarrow q\equiv\neg p\leftrightarrow\neg q$
- $p\leftrightarrow q\equiv(p\wedge q)\vee(\neg p\wedge\neg q)$
- $\neg(p\leftrightarrow q)\equiv p\leftrightarrow\neg q$

### 推导题的写法（⭐ 老师三次强调）

- 一行只做一步，**右侧标注规则名或公式**；
- 从一边推到另一边时，**结论必须落到整个目标表达式**；
- 不能用 $\mathbf T/\mathbf F$ 当字母代换（用 $S,R$ 或 $A,B$）。

> ⚠️ 高频错：把 $\neg A\to B\equiv A\vee B$ 标成 De Morgan's law。德摩根律只处理 $\neg(\cdots\wedge\cdots)$、$\neg(\cdots\vee\cdots)$。

### 范式与功能完备 Normal Forms and Functional Completeness（拓展）

- **文字（literal）**：命题变量或其否定，如 $p,\neg q$。
- **极小项（minterm）**：$n$ 个变量各出现一次（取正或取反）的合取；**极大项（maxterm）** 是对偶的析取。
- **析取范式（disjunctive normal form, DNF）**：若干极小项的析取；**合取范式（conjunctive normal form, CNF）**：若干极大项的合取。
- **从真值表造范式**：DNF 取"使公式为真的每一行"对应极小项作析取；CNF 取"使公式为假的每一行"对应极大项作合取——**任何公式都有等价的 DNF 与 CNF**。
- **功能完备（functionally complete）**：一个联结词集合能表达一切命题公式。$\{\neg,\wedge,\vee\}$ 完备；$\{\neg,\wedge\}$、$\{\neg,\to\}$、**$\{\text{NAND}\}$**、**$\{\text{NOR}\}$** 各自单独就完备；$\{\wedge,\vee\}$ **不**完备（表达不出否定）。
- **可满足性问题（SAT）**：判定是否存在成真赋值。SAT 是 **NP-完全（NP-complete）** 的（Cook–Levin 定理）；**3-SAT** 是最常用的 NP-完全标准型；SAT 求解器用于硬件验证、规划、约束求解。
- **2-SAT** 有多项式算法（蕴含图 + 强连通分量），与 3-SAT 形成"一线之隔"的对照。

### 本节自检

1. 用等价推导证明 $(p\wedge q)\to p$ 是永真式，每步标规则。
2. 不查表证明 $\neg(p\leftrightarrow q)\equiv p\leftrightarrow\neg q$。
3. "可满足"与"永真"是什么关系？举一个可满足但非永真的例子。

## 1.4 谓词与量词 Predicates and Quantifiers

### 谓词 Predicate

- **谓词（predicate）** 或**命题函数（propositional function）** $P(x)$：含变量的陈述，变量取值后成为命题；**$n$ 元谓词（$n$-ary predicate）** $P(x_1,\dots,x_n)$。
- **论域（domain / universe of discourse）**：变量允许取的集合（要求非空）。
- **自由变量（free variable）** 与**约束变量（bound variable）**；量词的作用域是**紧跟在它后面的最小公式**。
- **前置条件（precondition）**：程序段执行前必须为真的断言；**后置条件（postcondition）**：执行后必须为真的断言。
- **霍尔三元组（Hoare triple）** $\{P\}\,S\,\{Q\}$：若 $P$ 在 $S$ 执行前成立，则 $Q$ 在执行后成立；**最弱前置条件（weakest precondition）** 是使 $Q$ 必然成立的最宽松前置条件。
- 例：交换 $x,y$ 的程序段，前置 $x=a\wedge y=b$，后置 $x=b\wedge y=a$——用谓词写规约比自然语言精确。

### 三个量词

| 量词 | 名称 | 为真条件 | 有限论域 $\{x_1,\dots,x_n\}$ 上的展开 |
|---|---|---|---|
| $\forall x\,P(x)$ | **全称量词 universal quantifier**（for all） | 论域中**每个** $x$ 都使 $P(x)$ 真 | $P(x_1)\wedge\cdots\wedge P(x_n)$ |
| $\exists x\,P(x)$ | **存在量词 existential quantifier**（there exists） | **至少一个** $x$ 使 $P(x)$ 真 | $P(x_1)\vee\cdots\vee P(x_n)$ |
| $\exists!x\,P(x)$ | **唯一量词 uniqueness quantifier** | **恰好一个** $x$ 使 $P(x)$ 真 | 恰有一个为真 |

- **受限论域（restricted domain）**：$\forall x<0\,(x^2>0)$ 表示"对所有满足 $x<0$ 的 $x$"；否定时**保留限制**：$\neg\forall x<0\,P(x)\equiv\exists x<0\,\neg P(x)$。
- **量词优先级最高**：$\forall xP(x)\vee Q(x)=(\forall xP(x))\vee Q(x)$。
- **量词的作用域（scope of a quantifier）**：量词后紧跟的最小公式；同一变量在作用域外出现即为**自由**的。
- **布尔变量（Boolean variable）**：取真/假的变量，谓词逻辑里由谓词承担这一角色。

### 量词的否定（⭐ 必背）

$$\neg\forall x\,P(x)\equiv\exists x\,\neg P(x),\qquad \neg\exists x\,P(x)\equiv\forall x\,\neg P(x)$$

直观：全称不成立 = 有反例；存在不成立 = 全都不是。多个量词时**逐个翻转**（见 §1.5）。

### 翻译自然语言

- 信号词：every / all / each → $\forall$；some / at least one / there is → $\exists$；no / none / nobody → $\neg\exists$（或 $\forall\neg$）；not every / not all → $\neg\forall$；exactly one → $\exists!$。
- ⭐ **$\forall$ 配 $\to$，$\exists$ 配 $\wedge$**。用错的典型：$\exists x(Q(x)\wedge\forall y(R(y)\to P(x,y)))$ 写成 $\exists x\forall y((Q(x)\wedge R(y))\to P(x,y))$——随便取一个非学生的 $x$，式子就真了。

> ⭐ 老师说本次期末仍有自然语言 ↔ 量词表达式的翻译题，且是"送分题里最容易丢分的一道"。

### 本节自检

1. "No student can solve every problem" 的两种等价写法。
2. $\neg\exists x\forall y\,P(x,y)$ 推到量词全在内层。
3. 空论域上 $\forall xP(x)$ 与 $\exists xP(x)$ 的真值？

## 1.5 嵌套量词 Nested Quantifiers

- **嵌套量词（nested quantifiers）**：量词出现在另一个量词的作用域内。
- **顺序规则（⭐ 高频）**：
  - $\forall x\forall y\,P\equiv\forall y\forall x\,P$，$\exists x\exists y\,P\equiv\exists y\exists x\,P$（同型可换）；
  - **$\forall x\exists y$ 与 $\exists y\forall x$ 一般不等价**：前者 $y$ 可以**依赖** $x$，后者必须存在一个**对所有 $x$ 通用**的 $y$。
  - 例：$\forall x\exists y(x+y=0)$ 在 $\mathbf Z$ 上真；$\exists y\forall x(x+y=0)$ 假。
- **展开求值（⭐ 某年期末原题）**：把 $\forall x\exists y\,P(x,y)$ 在 $\{1,2,3\}$ 上展开为
  $$[\exists yP(1,y)]\wedge[\exists yP(2,y)]\wedge[\exists yP(3,y)]=\Big(\bigvee_{j}P(1,j)\Big)\wedge\Big(\bigvee_jP(2,j)\Big)\wedge\Big(\bigvee_jP(3,j)\Big)$$
- **翻译**：从**左往右**读，内层量词依赖外层变量；数学定义（极限、连续、一致连续）是标准素材。
- **否定**：$\neg\forall x\exists y\forall z\,P\equiv\exists x\forall y\exists z\,\neg P$（从左到右逐个翻转）。
- **量词与联结词**：$\forall x(P\wedge Q)\equiv\forall xP\wedge\forall xQ$；$\exists x(P\vee Q)\equiv\exists xP\vee\exists xQ$；但 $\forall x(P\vee Q)\not\equiv\forall xP\vee\forall xQ$，$\exists x(P\wedge Q)\not\equiv\exists xP\wedge\exists xQ$。

> ⚠️ $\forall x\exists y$ 的 $y$ 是 $x$ 的函数；答题时若写"取 $y=\dots$"，必须让 $y$ 的表达式里**出现 $x$**。

### 本节自检

1. 用 $\varepsilon$-$\delta$ 写出 $\lim_{x\to a}f(x)=L$，并写出它的否定。
2. $\exists y\forall x\,P$ 为真能否推出 $\forall x\exists y\,P$ 为真？反过来呢？

## 1.6 推理规则 Rules of Inference

### 基本概念

- **论证（argument）**：前提（premises）序列 + **结论（conclusion）**。
- **有效（valid）**：前提全真时结论必真，即 $(p_1\wedge\cdots\wedge p_n)\to q$ 是永真式。**有效性只看形式，不看前提实际真假**。
- **论证形式（argument form）**：把命题换成变量后的结构。

### 九条命题推理规则（⭐ 必背：名字 + 形式）

| 规则 | 形式 |
|---|---|
| **假言推理 modus ponens (MP)** | $p,\ p\to q\ \Rightarrow\ q$ |
| **拒取式 modus tollens (MT)** | $\neg q,\ p\to q\ \Rightarrow\ \neg p$ |
| **假言三段论 hypothetical syllogism** | $p\to q,\ q\to r\ \Rightarrow\ p\to r$ |
| **析取三段论 disjunctive syllogism** | $p\vee q,\ \neg p\ \Rightarrow\ q$ |
| **附加 addition** | $p\ \Rightarrow\ p\vee q$ |
| **化简 simplification** | $p\wedge q\ \Rightarrow\ p$ |
| **合取 conjunction** | $p,\ q\ \Rightarrow\ p\wedge q$ |
| **消解 resolution** | $p\vee q,\ \neg p\vee r\ \Rightarrow\ q\vee r$ |
| 消解特例 | $p\vee q,\ \neg p\vee q\ \Rightarrow\ q$ |

### 四条量词规则（⭐ 必背）

| 规则 | 形式 | 使用条件 |
|---|---|---|
| **全称实例化 universal instantiation (UI/US)** | $\forall xP(x)\Rightarrow P(c)$ | $c$ 为论域中任意元素 |
| **全称推广 universal generalization (UG)** | $P(c)$（$c$ **任意**）$\Rightarrow\forall xP(x)$ | $c$ 必须是任取的，不能是特殊元素 |
| **存在实例化 existential instantiation (EI/ES)** | $\exists xP(x)\Rightarrow P(c)$ | $c$ 必须是**新**常元，且此后再不能对它做 UG |
| **存在推广 existential generalization (EG)** | $P(c)\Rightarrow\exists xP(x)$ | 无额外限制 |

组合形式：**全称假言推理（universal modus ponens）** $\forall x(P\to Q),P(a)\Rightarrow Q(a)$；**全称拒取式（universal modus tollens）** $\forall x(P\to Q),\neg Q(a)\Rightarrow\neg P(a)$。

### 谬误 Fallacies（选择题常客）

- **肯定后件谬误（affirming the conclusion）**：由 $q$、$p\to q$ 推 $p$。
- **否定前件谬误（denying the hypothesis）**：由 $\neg p$、$p\to q$ 推 $\neg q$。
- **循环论证（circular reasoning / begging the question）**；**两个特称前提推不出结论**（$\exists xW(x)\wedge\exists xF(x)\not\Rightarrow\exists x(W\wedge F)$，两个 $\exists$ 各挑各的见证人）。

### 构造论证

自然语言 → 谓词化（选定论域可省掉谓词）→ 逐步应用规则 → 每步右侧标规则名。量词题的标准流程：US/EI 取出个体 → 用命题规则推 → UG/EG 收回。

> - ⚠️ 规则只能作用于**整行**：从 $(p\wedge q)\vee(r\wedge s)$ 不能直接 simplification 出 $p\vee r$。
> - ⚠️ MT 从 $\neg p\to r$ 与 $\neg r$ 只能得 $\neg\neg p$，还要补一步双重否定。
> - ⚠️ 由 $Q(a),T(a)$ 得 $Q(a)\wedge T(a)$ 是 conjunction，不是 addition。

### 本节自检

1. 写出"所有学生都努力；某人没努力；所以某人不是学生"的完整推理链，逐步标规则。
2. MP 与 MT 的区别？给出一个"看起来像 MT 其实是肯定后件"的例子。

## 1.7 证明导论 Introduction to Proofs

### 术语

| 术语 | English | 说明 |
|---|---|---|
| 定理 | theorem | 已被证明为真且有重要性的陈述 |
| 命题 | proposition | 重要性较低的定理（与 §1.1 的"命题"同名不同义） |
| 引理 | lemma | 为证明其他结果铺路的辅助定理 |
| 推论 | corollary | 由已证定理直接推出的结果 |
| 猜想 | conjecture | 尚未证明的断言；证出后升级为定理 |
| 公理 | axiom / postulate | 假定为真、不加证明 |
| 证明 | proof | 确立定理为真的有效论证 |

**形式证明（formal proof）** 每步都用推理规则；**非形式证明（informal proof）** 允许跳步——人写的是后者。定理常**省略全称量词**，证明开头"取任意 $c$"、结尾"$c$ 任意"，隐含 UI/UG。

### 四种基本证明方法（⭐ 可能指定方法）

目标：证 $\forall x(P(x)\to Q(x))$。

1. **直接证明（direct proof）**：设 $P(c)$ 真，推出 $Q(c)$。
   ⭐ **必背例**：$n$ 奇 $\Rightarrow n^2$ 奇。$n=2k+1\Rightarrow n^2=4k^2+4k+1=2(2k^2+2k)+1$，括号内是整数。（上学期期末原题）
2. **逆否证明（proof by contraposition）**：证 $\neg Q(c)\to\neg P(c)$，依据 $p\to q\equiv\neg q\to\neg p$。
   必背例：$3n+2$ 奇 $\Rightarrow n$ 奇（直接证明走不通）。
3. **空证明（vacuous proof）**：前件恒假 ⇒ 命题真；**平凡证明（trivial proof）**：后件恒真 ⇒ 命题真。
4. **反证法（proof by contradiction）**：设 $\neg p$（或 $p\wedge\neg q$）推出 $r\wedge\neg r$。
   ⭐ 必背例：$\sqrt2$ 无理——反设 $\sqrt2=a/b$ 为**最简分数（in lowest terms）**，推出 $a,b$ 同为偶数，与最简矛盾。

**逆否 vs 反证**：逆否是把结论否定当前提、把前提否定当目标；反证是假设整个命题为假。能用逆否时优先逆否（计算相同但结构更清楚）；结论是否定性的（"不存在""无理"）用反证更自然。

三个常考的直接证明素材：**完全平方数（perfect square）**（$a=b^2$，两个完全平方数之积仍是完全平方数）；**有理数（rational number）**（$r=p/q$，$p,q$ 整数且 $q\ne0$，两个有理数之和仍为有理数，注意验证分母不为零）；$n$ 为整数时 $n^2\ge n$（分 $n\le-1$、$n=0$、$n\ge1$ 三种情形）。

### 等价性证明 Proofs of Equivalence

- 证 $p\leftrightarrow q$：分别证 $p\to q$ 与 $q\to p$。
- ⭐ **多命题等价**：证 $p_1\to p_2\to\cdots\to p_n\to p_1$ 只需 $n$ 个蕴涵；两两互证要 $n(n-1)$ 个。链的顺序可自选，挑最容易证的。

### 反例 Counterexamples

证伪 $\forall xP(x)$ 只需一个反例，但必须**验证**它确实使 $P$ 为假，不能只报一个数。

### 证明中的错误

1. **除以零（division by zero）**——"$1=2$"型假证明的常见死因；
2. **肯定后件**、**否定前件**；
3. **循环论证**——把待证结论（或其等价说法）当步骤，如"设 $n=2l$"直接假设 $n$ 为偶。

### 本节自检

1. 用逆否证明"若 $n^2$ 是奇数，则 $n$ 是奇数"。
2. 为什么"$\sqrt2$ 无理"必须用反证而不能用直接证明？

## 1.8 证明方法与策略 Proof Methods and Strategy

- **穷举证明（exhaustive proof）**：有限个情形逐一验证（分情况证明的特例）。只对**有限**范围有效。
- **分情况证明（proof by cases）**：依据 $[(p_1\vee\cdots\vee p_n)\to q]\leftrightarrow[(p_1\to q)\wedge\cdots\wedge(p_n\to q)]$。
  ⚠️ 必须**覆盖所有情形**（实数分正/负/零三类，漏 0 是典型错误），各情形可换不同方法。
- **不失一般性（without loss of generality, WLOG）**：断言其他情形"由对称性同理"。⚠️ 必须能说出**具体变换**（如交换 $x,y$ 的角色）；说不出的 WLOG 就是漏洞。
- **存在性证明（existence proof）**：
  - **构造性（constructive）**：给出**见证（witness）** $a$ 并验证 $P(a)$；例：$1729=10^3+9^3=12^3+1^3$（**出租车数 taxi-cab number**）。
  - **非构造性（nonconstructive）**：不指出具体对象，常用反证或**排中律**；例：存在无理数 $x,y$ 使 $x^y$ 有理（$\sqrt2^{\sqrt2}$ 分两情形讨论）。
- **唯一性证明（uniqueness proof）**：① 存在性；② 若 $y$ 也满足则 $y=x$。形式化：$\exists x(P(x)\wedge\forall y(P(y)\to y=x))$。
- **正向推理（forward reasoning）** 与 **逆向推理（backward reasoning）**：逆向是从结论找充分条件，⚠️ 方向反了就成"肯定后件"。
- **染色论证（coloring argument）**：给棋盘染色，使每块骨牌覆盖各色格数固定；比较目标板的颜色分布即可判不可能。
  - 标准 8×8 棋盘去掉两个对角（同色）后黑白 30:32，**多米诺骨牌（domino）** 每块盖一黑一白 ⇒ 不能铺满。
  - 三色染色可判"三格直线骨牌（tromino）"铺砌问题。

![[C1-图9-去掉左上和右下角的棋盘.png|460]]
*图 1-2｜去掉对角两角后黑白 30:32，与 31 块骨牌所需的 31:31 不符，故铺不满*

### 著名的未解决问题（拓展）

- **费马大定理（Fermat's Last Theorem）**：$x^n+y^n=z^n$ 在 $n>2$ 时无 $xyz\ne0$ 的整数解；费马 1637 年提出，**Andrew Wiles 1994 年**用椭圆曲线与模形式证明，篇幅数百页。
- **$3x+1$ 猜想（Collatz conjecture）**：偶数除以 2、奇数乘 3 加 1，反复施加是否终到 1——至今未证，已验证到 $5.6\times10^{13}$ 以上；别名 Hasse 算法、Ulam 问题、角谷问题。
- **哥德尔不完备性定理（Gödel's incompleteness theorems）**：任何足够强、可递归公理化的算术系统都含"真而不可证"的命题，且不能自证一致性。
- **丘奇–图灵论题（Church–Turing thesis）**：可计算 = 图灵机可计算；由此**停机问题不可判定**，不存在判定一切命题的通用程序。
- 复习口径：这些只考"能陈述、能判断某问题是开放的"，不要求证明。

### 本节自检

1. 证明"任意 6 人中有 3 人互相认识或互相不认识"用的是什么方法？
2. WLOG 用在什么地方会失效？举一个反例。
3. 证明 $\sqrt[3]{2}$ 无理，哪些步骤必须改写？

---
# 第二章 基本结构 Basic Structures: Sets, Functions, Sequences, Sums, and Matrices

**考试权重**：老师复习顺序里的第 2 站。§2.1–2.3 课堂讲过（第 11、12 节课），**§2.4–2.6 课堂没讲**，但教材范围内、卷面可能出现；下面按正文同等深度写出并标〔拓展〕，优先级可后置，内容不省略。第 9、10 章的矩阵表示、势、序列全靠这一章打底。

## 2.1 集合 Sets

**集合（set）** 是互不相同的对象的汇集，**元素（element）** 无序、不重复：$\{1,3,3,5\}=\{5,3,1\}$。

- **列举法（roster method）**：$\{1,2,3\}$；**描述法（set builder notation）**：$\{x\in D\mid P(x)\}$。
- 常用数集：$\mathbf N=\{0,1,2,\dots\}$，$\mathbf Z$（整数），$\mathbf Z^+$（正整数），$\mathbf Q$（有理数），$\mathbf R$，$\mathbf C$。
- **空集（empty set / null set）** $\varnothing$；**全集（universal set）** $U$；**文氏图（Venn diagram）**。
- **基数（cardinality）** $|S|$：元素个数；$|P(S)|=2^{|S|}$。

### 子集与相等

- **子集（subset）**：$A\subseteq B\iff\forall x(x\in A\to x\in B)$（⭐ $\forall$ 配 $\to$）。
- **真子集（proper subset）**：$A\subset B\iff A\subseteq B\wedge\exists x(x\in B\wedge x\notin A)$（本书 $\subset$ **专指**真子集）。
- **相等（set equality）**：$A=B\iff\forall x(x\in A\leftrightarrow x\in B)$。
- ⭐ **证 $A=B$ 的标准动作是证双向包含**：任取 $x\in A$ 推出 $x\in B$；再任取 $x\in B$ 推出 $x\in A$。否证 $A\subseteq B$ 只需一个反例 $x\in A\wedge x\notin B$。
- **空集恒为子集**：$\varnothing\subseteq S$ 对一切 $S$ 成立（前件恒假）。
- **有限集（finite set）** 与**无限集（infinite set）**：前者元素个数为非负整数，后者不是有限集。
- ⚠️ 两个经典陷阱：$\varnothing\ne\{\varnothing\}$（后者有一个元素）；$P(\varnothing)=\{\varnothing\}\ne\varnothing$。

### 幂集与笛卡尔积

- **幂集（power set）** $P(S)$：全部子集之集；$|P(S)|=2^{|S|}$；$P(S)$ 永不为空。
- **笛卡尔积（Cartesian product）**：$A\times B=\{(a,b)\mid a\in A\wedge b\in B\}$，$|A\times B|=|A|\cdot|B|$。
  - ⚠️ **不交换**：$A\times B\ne B\times A$（除非 $A=B=\varnothing$ 或 $A=B$）；$A\times B\times C\ne(A\times B)\times C$（前者三元组，后者以有序对为元素）。
  - $A\times B=B\times A$ 的充要条件是 $A=\varnothing$ 或 $B=\varnothing$ 或 $A=B$。
- **关系（relation）** 就是 $A\times B$ 的子集——通往第 9 章。

### 集合与谓词的互译

- 受限量词写成集合：$\{x\in D\mid P(x)\}$ 是**真值集（truth set）**；$\forall xP(x)$ 真 $\iff$ 真值集 $=U$；$\exists xP(x)$ 真 $\iff$ 真值集 $\ne\varnothing$。
- $\forall$ 对应**交**、$\exists$ 对应**并**（$\forall$ 全真 = 落在每个集合里；$\exists$ 成立 = 至少落在一个里）。

### 朴素集合论与罗素悖论（拓展）

- **朴素集合论（naive set theory）**：允许用任意性质 $\{x\mid P(x)\}$ 造集合。
- **罗素悖论（Russell's paradox）**：取 $S=\{A\mid A\notin A\}$，则 $S\in S\iff S\notin S$，矛盾。
- 出路：**公理化集合论（axiomatic set theory，如 ZFC）** 用分离公理限制"从已有集合里挑元素"，禁止"所有集合的集合"。
- **理发师悖论（barber paradox）** 是同一结构的生活版：村里理发师只给"不自己刮脸的人"刮脸，且给所有这样的人刮——他给自己刮吗？

### 本节自检

1. 判断 $\varnothing\in\{\varnothing\}$ 与 $\varnothing\subseteq\{\varnothing\}$ 的真假。
2. 证明 $A\subseteq B\Rightarrow P(A)\subseteq P(B)$。
3. $|A|=3,|B|=4$，求 $|P(A\times B)|$。

## 2.2 集合运算 Set Operations

| 运算 | 定义 | 逻辑对应 |
|---|---|---|
| **并集（union）** $A\cup B$ | $\{x\mid x\in A\vee x\in B\}$ | $\vee$ |
| **交集（intersection）** $A\cap B$ | $\{x\mid x\in A\wedge x\in B\}$ | $\wedge$ |
| **差集（difference）** $A-B$ | $\{x\mid x\in A\wedge x\notin B\}$ | $\wedge\neg$ |
| **补集（complement）** $\overline A$（或 $A^c$） | $\{x\in U\mid x\notin A\}$ | $\neg$ |
| **对称差（symmetric difference）** $A\oplus B$ | $(A-B)\cup(B-A)$，恰属其一 | $\oplus$ |

- ⚠️ **补集必须先指定全集**，离开 $U$ 无意义；$A-B=A\cap\overline B$。
- **两集合容斥**：$|A\cup B|=|A|+|B|-|A\cap B|$（第 6 章减法原理的起点）。
- **对称差性质**：$A\oplus A=\varnothing$，$(A\oplus B)\oplus B=A$（"自反消去"）。

![[C2-图3-集合运算的文氏图-并交差补.png|520]]
*图 2-1｜四种运算的文氏图：并、交、差、补——补集必须先画全集*

### 集合恒等式表（与 §1.3 Table 6 逐行对应）

| 恒等式 | 名称 | 逻辑版 |
|---|---|---|
| $A\cap U=A$；$A\cup\varnothing=A$ | 同一律 identity | $p\wedge\mathbf T\equiv p$；$p\vee\mathbf F\equiv p$ |
| $A\cup U=U$；$A\cap\varnothing=\varnothing$ | 支配律 domination | $p\vee\mathbf T\equiv\mathbf T$；$p\wedge\mathbf F\equiv\mathbf F$ |
| $A\cup A=A$；$A\cap A=A$ | 幂等律 idempotent | $p\vee p\equiv p$ |
| $\overline{\overline A}=A$ | 双重补 double complement | $\neg\neg p\equiv p$ |
| $A\cup B=B\cup A$；$A\cap B=B\cap A$ | 交换律 commutative | 同形 |
| $(A\cup B)\cup C=A\cup(B\cup C)$ | 结合律 associative | 同形 |
| $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$；$A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ | 分配律 distributive | 同形 |
| $\overline{A\cap B}=\overline A\cup\overline B$；$\overline{A\cup B}=\overline A\cap\overline B$ | ⭐ **德摩根律 De Morgan's laws** | $\neg(p\wedge q)\equiv\neg p\vee\neg q$ |
| $A\cup(A\cap B)=A$；$A\cap(A\cup B)=A$ | 吸收律 absorption | 同形 |
| $A\cup\overline A=U$；$A\cap\overline A=\varnothing$ | 补律 complement | $p\vee\neg p\equiv\mathbf T$ |

**替换字典**：$\cap\leftrightarrow\wedge$，$\cup\leftrightarrow\vee$，$\overline{A}\leftrightarrow\neg p$，$U\leftrightarrow\mathbf T$，$\varnothing\leftrightarrow\mathbf F$。**同一套定律在全书出现四次**：命题逻辑 → 集合 → 位串 → 布尔矩阵，第 12 章统一为**布尔代数（Boolean algebra）**。

### 证集合恒等式的四种方法

1. **双向包含（element method）**：逐元素追，最稳但最长；
2. **描述法 + 逻辑等价（chain of equivalences）**：首选，2–3 行搞定；
3. **隶属表（membership table）**：$n$ 个集合 $2^n$ 行，**4 个以上别用**；
4. **用已证恒等式推导**：与 §1.3 推导题规范相同。

### 广义并与交

$\bigcup_{i=1}^{n}A_i$、$\bigcap_{i=1}^{n}A_i$，可推广到无限族；$\bigcup_{i\in I}A_i=\{x\mid\exists i\in I,x\in A_i\}$（$\exists$ 配并），$\bigcap$ 配 $\forall$。

### 计算机表示：位串

给 $U$ 排序后，子集 $\leftrightarrow$ 长度 $|U|$ 的**位串（bit string）**；并、交、补对应 OR、AND、NOT，复杂度 $O(|U|)$。相较"元素列表"的朴素做法（并集需 $O(n^2)$ 查重），位串是数量级的改进。

### 两个扩展结构（拓展）

- **多重集（multiset）**：允许元素重复，用**重数（multiplicity）** 记录每个元素出现次数；并、交按重数取 $\max$、$\min$，基数按重数求和。
- **模糊集（fuzzy set）**：元素以**隶属度（degree of membership）** $\mu_A(x)\in[0,1]$ 部分属于 $A$；并取 $\max$、交取 $\min$、补为 $1-\mu_A(x)$。
- 用途：多重集对应"每个元素能取多次"的计数（第 6 章可重复组合），模糊集是模糊控制、聚类与可解释 AI 的基础。

### 本节自检

1. 用描述法证明 $A-(B\cup C)=(A-B)\cap(A-C)$。
2. $|A|=10,|B|=8,|A\cap B|=3$，求 $|A\oplus B|$。
3. 为什么 4 个集合以上不建议用隶属表？

## 2.3 函数 Functions

**函数（function）** $f:A\to B$：对每个 $a\in A$ **恰好**指派一个 $b\in B$。

- **三件套**：**定义域（domain）** $A$、**陪域（codomain）** $B$、映射规则。改任何一件都是另一个函数。
- ⚠️ **值域（range）$\subseteq$ 陪域，未必相等**——本章第一大易错点。
- **像（image）** $f(a)=b$ 称 $b$ 是 $a$ 的像；**原像（preimage）** $a$ 是 $b$ 的原像；子集的像 $f(S)=\{f(s)\mid s\in S\}$。
- 函数的加、乘：$(f+g)(x)=f(x)+g(x)$，$(fg)(x)=f(x)g(x)$。

### 单射、满射、双射

| 概念 | 定义 | 否定形式（举反例用） |
|---|---|---|
| **单射 injective / one-to-one** | $f(a)=f(b)\Rightarrow a=b$ | $\exists a\ne b,\ f(a)=f(b)$ |
| **满射 surjective / onto** | $\forall b\in B\ \exists a\in A,\ f(a)=b$ | $\exists b\in B\ \forall a,\ f(a)\ne b$ |
| **双射 bijective / one-to-one correspondence** | 既单又满 | 任一不满足 |

**证明模板**（照抄结构）：

- 证单射：设 $f(x)=f(y)$，推出 $x=y$；
- 证满射：任取 $y\in B$，**构造**出 $x$（并验证 $x$ 在定义域内）；
- 证双射：两条都写。

![[C2.3-映射类型-单射满射双射.png|560]]
*图 2-2｜五种映射形态：撞车（非单射）、漏点（非满射）、两者兼有（双射）*

> - ⭐ **有限集上**：$|A|=|B|=n$ 时，单射 $\iff$ 满射 $\iff$ 双射。**无限集上这条铁律崩塌**（$f(n)=2n$ 是 $\mathbf Z^+\to\mathbf Z^+$ 的单射但非满射）——这正是 §2.5 的起点。
> - ⭐ 判定单射的充分条件：**严格单调（strictly increasing/decreasing）**。

### 反函数与复合

- **反函数（inverse function）** $f^{-1}:B\to A$，仅当 $f$ 是**双射**时存在；$f^{-1}(b)=a\iff f(a)=b$。
  - ⚠️ $f^{-1}\ne 1/f$。
  - 非双射可**限制定义域/陪域**抢救（如 $f(x)=x^2$ 限制在 $[0,\infty)$）。
- **恒等函数（identity function）** $\iota_A(a)=a$；$f^{-1}\circ f=\iota_A$，$f\circ f^{-1}=\iota_B$。
- **复合（composition）** $(f\circ g)(x)=f(g(x))$——⭐ **先 $g$ 后 $f$**；需 $g$ 的值域 $\subseteq f$ 的定义域。
  - 复合**满足结合律、不满足交换律**；$f,g$ 都单（满/双）⇒ $f\circ g$ 也单（满/双）。

### 取整函数与阶乘

- **下取整（floor）** $\lfloor x\rfloor$：不超过 $x$ 的最大整数；**上取整（ceiling）** $\lceil x\rceil$：不小于 $x$ 的最小整数。
- 必背性质：
  - $\lfloor x\rfloor=n\iff n\le x<n+1$；$\lceil x\rceil=n\iff n-1<x\le n$；
  - $x-1<\lfloor x\rfloor\le x\le\lceil x\rceil<x+1$；
  - ⭐ $\lfloor -x\rfloor=-\lceil x\rceil$，$\lceil -x\rceil=-\lfloor x\rfloor$；
  - ⭐ $\lfloor x+n\rfloor=\lfloor x\rfloor+n$，$\lceil x+n\rceil=\lceil x\rceil+n$（$n$ 为**整数**）。
- ⚠️ **除"加整数"外，取整一律不能拆**：$\lceil x+y\rceil\ne\lceil x\rceil+\lceil y\rceil$（反例 $x=y=\tfrac12$）。负数是最高频的计算错误来源。
- 应用口径："至少要"用 $\lceil\ \rceil$，"最多能"用 $\lfloor\ \rfloor$。
- **阶乘（factorial）** $n!=n(n-1)\cdots1$，$0!=1$；**Stirling 公式** $n!\sim\sqrt{2\pi n}(n/e)^n$。

![[C2-图7-取整函数的图像-下取整与上取整.png|520]]
*图 2-3｜下取整与上取整的图像：阶梯位置决定为什么负数是易错区*

### 部分函数（拓展）

- **部分函数（partial function）** $f:A\rightharpoonup B$：只在 $A$ 的某个子集上有定义；前面定义的函数相应叫**全函数（total function）**。
- 例：$f(x)=1/x$ 在 $\mathbf R$ 上是部分函数（$x=0$ 无定义）；编程中"可能抛异常或返回 null"的函数就是部分函数。
- 处理方式：**限制定义域**使其成为全函数，或把值域扩成 $B\cup\{\bot\}$（**提升，lifting**）。

### 本节自检

1. $f:\mathbf Z\to\mathbf Z,f(n)=n^2$ 是单射吗？满射吗？改定义域/陪域能否变成双射？
2. 证明"$f,g$ 都是双射 ⇒ $f\circ g$ 是双射"，并写出 $(f\circ g)^{-1}$。
3. 计算 $\lfloor-2.5\rfloor$、$\lceil-2.5\rceil$、$\lfloor 3.7\rfloor+\lceil-3.7\rceil$。

## 2.4 序列与求和 Sequences and Summations〔拓展：课堂未讲〕

- **序列（sequence）**：定义域为整数集子集的函数，记 $\{a_n\}$；**通项（closed formula）** 与**递推**是描述序列的两条路。
- **等差数列（arithmetic progression）**：$a_n=a_0+nd$；**等比数列（geometric progression）**：$a_n=a_0r^n$。
- **字符串（string）**：有限序列，**空串（empty string）** $\lambda$，**长度（length）**；字母表 $\Sigma$ 上长度 $n$ 的串共 $|\Sigma|^n$ 个。
- **递推关系（recurrence relation）**：用前若干项表示 $a_n$ 的等式，配**初始条件（initial conditions）**。⭐ 初始条件个数必须配得上回看深度（二阶递推要两个初值）。
  - 斐波那契（Fibonacci）$f_n=f_{n-1}+f_{n-2}$，$f_0=0,f_1=1$；卢卡斯（Lucas）同递推、$L_1=1,L_2=3$——**递推定形状，初值定身份**。
- **迭代法（iteration）**：反复代入展开成通项。例 $a_n=2a_{n-1}+1$、$a_1=1$：
  $$a_n=2^{\,n-1}a_1+(2^{\,n-1}-1)=2^{\,n}-1$$
  （严格证明要靠归纳法，第 5 章。）
- **猜通项**：先看差（等差）、再看比（等比），再与 $n^2,n^3,2^n,3^n,n!,f_n$ 对照；必要时列**差分表（difference table）**。
- **求和（summation）** $\sum_{k=m}^{n}a_k$，**求积（product）** $\prod_{k=m}^{n}a_k$；**哑变量（dummy variable）** 可换名，值不变。

### 求和的性质

| 性质 | 形式 |
|---|---|
| 线性 | $\sum_{k}(ca_k+db_k)=c\sum_k a_k+d\sum_k b_k$ |
| 平移（换元） | $\sum_{k=1}^{n}a_k=\sum_{j=0}^{n-1}a_{j+1}$ |
| 拆分 | $\sum_{k=m}^{n}a_k=\sum_{k=m}^{p}a_k+\sum_{k=p+1}^{n}a_k$ |
| 双重求和交换 | $\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}=\sum_{j=1}^{n}\sum_{i=1}^{m}a_{ij}$（有限和总可换） |
| 对集合求和 | $\sum_{s\in S}f(s)$，与枚举顺序无关 |
| 求和与求积混合 | $\prod_{k}\Big(\sum_j a_{kj}\Big)\ne\sum_j\prod_k a_{kj}$（一般不等） |

### 必背求和公式

| 公式 | 闭式 | 备注 |
|---|---|---|
| $\sum_{k=0}^{n}ar^k$ | $\dfrac{ar^{n+1}-a}{r-1}$（$r\ne1$） | 几何级数 geometric series，$r=1$ 时为 $(n+1)a$ |
| $\sum_{k=1}^{n}k$ | $\dfrac{n(n+1)}2$ | 高斯配对 |
| $\sum_{k=1}^{n}k^2$ | $\dfrac{n(n+1)(2n+1)}6$ | — |
| $\sum_{k=1}^{n}k^3$ | $\dfrac{n^2(n+1)^2}4=\left(\sum k\right)^2$ | ⭐ 立方和 = 和的平方 |
| $\sum_{k=0}^{\infty}x^k$（$\lvert x\rvert<1$） | $\dfrac1{1-x}$ | 无穷几何级数 |
| $\sum_{k=1}^{\infty}kx^{k-1}$（$\lvert x\rvert<1$） | $\dfrac1{(1-x)^2}$ | 上式求导 |

> ⚠️ 两个坑：**项数差一**（$\sum_{k=0}^{n}$ 共 $n+1$ 项）；**区间求和要减到下限减 1**（$\sum_{k=5}^{20}=\sum_{1}^{20}-\sum_{1}^{4}$）。

### 本节自检

1. 求 $\sum_{k=3}^{50}(2k+1)$。
2. 用迭代法解 $a_n=2a_{n-1}+1$，$a_1=1$。
3. $\sum_{i=1}^{3}\sum_{j=1}^{2}ij$ 等于多少？

## 2.5 集合的基数 Cardinality of Sets〔拓展：课堂未讲〕

- **等势（equinumerous）**：$|A|=|B|\iff$ 存在双射 $A\to B$；$|A|\le|B|\iff$ 存在单射 $A\to B$。
- **可数集（countable set）**：有限集，或与 $\mathbf Z^+$ 存在双射的集合；否则**不可数（uncountable）**。可数集的基数记 $\aleph_0$（aleph null），实数集的基数记 $\mathfrak c$。
- **可数判据**：能**排成一列**（$a_1,a_2,\dots$，每一项都要数到，不能"先排完这一行"）。
  - $\mathbf Z$ 可数：$0,1,-1,2,-2,\dots$；$\mathbf Z^+\times\mathbf Z^+$ 可数：**按 $p+q$ 分层斜着走**（⚠️ 逐行扫永远轮不到第二行）。
  - $\mathbf Q^+$ 可数：同上分层枚举并去重（去重不改变可数性）。
- **希尔伯特大饭店（Hilbert's Grand Hotel）**：房间全满仍能安排新客人——$n\mapsto n+1$ 腾出 1 号房；可数批客人用 $n\mapsto2n$ 腾出无穷多间。直观的"整体大于部分"在无限集上失效。
- **可数个可数集的并仍可数**（$\aleph_0\cdot\aleph_0=\aleph_0$）：把第 $i$ 个集合的第 $j$ 个元素排在格点 $(i,j)$，按 $i+j$ 分层沿对角线走。
- ⭐⭐ **实数不可数：康托尔对角线法（Cantor diagonalization）**：假设 $(0,1)$ 可列为 $r_1,r_2,\dots$（十进制展开），构造 $r$ 使第 $n$ 位与 $r_n$ 的第 $n$ 位不同 ⇒ $r$ 不在表中，矛盾。
  - ⚠️ 细节：$0.1999\cdots=0.2000\cdots$ 表示不唯一，要约定不用结尾全 9 的展开；构造时每位至少留两个选择，保证 $r\ne r_n$ 对一切 $n$。
  - **康托尔定理（Cantor's theorem）**：$|P(A)|>|A|$ 对一切集合成立，故没有"最大的基数"。
- **Schröder–Bernstein 定理**：$|A|\le|B|$ 且 $|B|\le|A|$ ⇒ $|A|=|B|$。用途：不必显式构造双射，分两次构造单射即可（如 $(0,1)$ 与 $[0,1]$ 等势）。
- ⭐ **应用：存在不可计算的函数**，三步论证：① 每个程序是有限位串，程序全体可数（$\aleph_0$）；② $\mathbf Z^+\to\{0,1\}$ 的函数全体有 $2^{\aleph_0}$ 个；③ 可数 < 不可数，故必有函数无程序可算——**非构造性证明**，指不出是哪一个。
- **连续统假设（continuum hypothesis）**：不存在集合使 $\aleph_0<|A|<\mathfrak c$；与 ZFC 独立（哥德尔 1940、科恩 1963）。

![[C2-图8-正有理数可数的排列路径.png|520]]
*图 2-4｜正有理数按 $p+q$ 分层斜走：每条斜线有限，故每个数都会被数到*

### 本节自检

1. 证明正有理数集可数，并说明为什么不能逐行枚举。
2. $(0,1)$ 与 $\mathbf R$ 等势，构造一个双射。
3. 为什么"可数个可数集的并"仍可数？

## 2.6 矩阵 Matrices〔拓展：课堂未讲〕

- **矩阵（matrix）**：$m\times n$ 的数的矩形阵列，$a_{ij}$ 在第 $i$ 行第 $j$ 列；同型矩阵才谈相等与加法。
- **矩阵加法（matrix addition）** 逐元相加；**数乘（scalar multiplication）** 每个元素乘同一数。
- **矩阵乘法（matrix multiplication）**：$\mathbf A$ 的列数 $=$ $\mathbf B$ 的行数时才有定义，$(\mathbf{AB})_{ij}=\sum_{k=1}^{p}a_{ik}b_{kj}$。
  - ⚠️ **不满足交换律**（$\mathbf{AB}\ne\mathbf{BA}$，甚至不一定同型）；满足**结合律**与**分配律**。
  - **不满足消去律**：$\mathbf{AB}=\mathbf{AC}$ 推不出 $\mathbf B=\mathbf C$（$\mathbf A$ 可能奇异）。
- **单位矩阵（identity matrix）** $\mathbf I_n$：对角 1、其余 0；$\mathbf{AI}_n=\mathbf I_n\mathbf A=\mathbf A$。
- **转置（transpose）** $\mathbf A^t$：$(\mathbf A^t)_{ij}=a_{ji}$；性质 $(\mathbf A^t)^t=\mathbf A$，$(\mathbf{A+B})^t=\mathbf A^t+\mathbf B^t$，**$(\mathbf{AB})^t=\mathbf B^t\mathbf A^t$（倒序）**。
- **对称矩阵（symmetric matrix）**：$\mathbf A=\mathbf A^t$；**斜对称（skew-symmetric）**：$\mathbf A=-\mathbf A^t$（对角线必为 0）。

### 零一矩阵与布尔运算

- **零一矩阵（zero–one matrix）**：元素只取 0/1。
  - **并（join）** $\mathbf A\vee\mathbf B$：逐位 OR；**交（meet）** $\mathbf A\wedge\mathbf B$：逐位 AND；**补（complement）** 逐位取反。
- ⭐ **布尔积（Boolean product）** $\mathbf A\odot\mathbf B$：$(\mathbf A\odot\mathbf B)_{ij}=\bigvee_k(a_{ik}\wedge b_{kj})$——乘法换 $\wedge$、加法换 $\vee$。
- **布尔幂（Boolean power）** $\mathbf A^{[n]}$：$n$ 次布尔积，$\mathbf A^{[0]}=\mathbf I$。
- 性质：布尔积满足结合律与分配律、**不满足交换律**；$\mathbf A\vee\mathbf B$ 与 $\mathbf A+\mathbf B$ 不同（后者按普通加法，可能出现 2）。

### 用途

- 第 9 章：关系用零一矩阵表示，$S\circ R$ 对应 $M_R\odot M_S$（顺序相反），传递闭包对应布尔幂的并。
- 第 10 章：图的邻接矩阵 $A$，$(A^r)_{ij}$ 是从 $v_i$ 到 $v_j$ 长 $r$ 的走法数。

### 本节自检

1. 两个 $3\times3$ 矩阵的布尔积怎么算？与普通乘法的差别在哪一步？
2. 对称矩阵的转置有什么性质？$\mathbf A\vee\mathbf B$ 与 $\mathbf A+\mathbf B$ 的区别？
3. 为什么 $(\mathbf{AB})^t=\mathbf B^t\mathbf A^t$ 而不是 $\mathbf A^t\mathbf B^t$？

# 第六章 计数 Counting

**考试权重**：高。老师复习顺序第 4 站，但内容是第 10 章（图论计数、复杂度）的工具。老师对本章的定位是"**会算、会手算过程比会证明重要**"；§6.2 鸽巢原理独立成节、性价比最高，别跳过。

## 6.1 计数基础 The Basics of Counting

**组合数学（combinatorics）** 研究对象的安排方式，**枚举（enumeration）** 是把个数数出来。

### 四个计数原理（⭐ 必背：见到什么信号用哪条）

| 原理 | 使用信号 | 公式 | 用错后果 |
|---|---|---|---|
| **乘法原理 product rule** | 任务拆成**依次执行的步骤** | $n_1n_2\cdots n_k$ | 把"或"当"且"⇒ 少数 |
| **求和原理 sum rule** | 任务拆成**互不相交的类** | $n_1+n_2+\cdots+n_k$ | 有重叠还相加 ⇒ 多数 |
| **减法原理 subtraction rule**（容斥 inclusion–exclusion） | 分类**有重叠**且重叠好数 | $n_1+n_2-\lvert A\cap B\rvert$ | 忘了减 ⇒ 多数 |
| **除法原理 division rule** | 同一结果被数了 $d$ 次 | 结果数 $=n/d$ | 不除 ⇒ 重复计数 |

> ⭐ 一句话判断："接着做/然后"⇒ 乘；"或者/分类"⇒ 加。本章一半的错题错在这一步。

**树形图（tree diagram）**：把分支摊开，叶子数即答案；遇到"某分支提前终止"（如五局三胜）时叶子数远小于 $2^5$。

![[C6.1-五局三胜的树形图.png|560]]
*图 6-1｜五局三胜的树形图：三胜即止，分支在第几层断掉决定叶子数（$2+6+12=20$，不是 $2^5$）*

### 经典计数模型

- IPv4 地址：32 位，按前缀分 A/B/C 类，各类地址数 $2^{31},2^{30},2^{29}$ 量级。
- 从 $m$ 元集到 $n$ 元集的函数个数 $n^m$；$n$ 元集的子集个数 $2^n$；长度 $n$ 的位串个数 $2^n$。
- 抽屉式的"至少"问题先想鸽巢（§6.2）。

## 6.2 鸽巢原理 The Pigeonhole Principle

| 名称 | 条件 | 结论 |
|---|---|---|
| **鸽巢原理（抽屉原理 Dirichlet drawer principle）** | $k+1$ 个物体放进 $k$ 个盒子 | 至少一个盒子含 $\ge2$ 个 |
| **推论 1** | 函数定义域 $>k$ 个元素，陪域只有 $k$ 个 | 函数**不是单射** |
| **广义鸽巢原理（generalized pigeonhole principle）** | $N$ 个物体放进 $k$ 个盒子 | 至少一个盒子含 $\ge\lceil N/k\rceil$ 个 |
| **拉姆齐（Ramsey）** | 6 人，任两人或友或敌 | 必有 3 人两两为友或两两为敌（$R(3,3)=6$） |
| **子序列定理** | $n^2+1$ 个**互不相同**的实数 | 必有长 $n+1$ 的递增或递减子序列 |

**证明套路**：鸽巢原理本身用**反证法**证（若每盒至多 1 个，总数 $\le k$，矛盾）。应用题的关键是**找出"物体"和"盒子"分别是什么**。

经典例：13 人中至少 2 人同月生（12 个月）；$n$ 个盒、$N$ 个物体求"至少几个"用 $\lceil N/k\rceil$；生日问题（23 人同生日概率过半）。

![[C6.2-广义鸽巢原理.png|520]]
*图 6-2｜最平均的放法给出下界：一定有盒子至少装 $\lceil N/k\rceil$ 个*

> ⚠️ 常见错误：把"至少 $\lceil N/k\rceil$"写成"至少 $\lfloor N/k\rfloor+1$"——$k\mid N$ 时后者会多算 1，正确写法是 $\lfloor (N-1)/k\rfloor+1$；另外要看清题目问的是"存在**一对**"还是"存在**一个盒子装 $m$ 个**"。

## 6.3 排列与组合 Permutations and Combinations

- **排列（permutation）**：有序安排；**$r$-排列（$r$-permutation）** $P(n,r)=\dfrac{n!}{(n-r)!}=n(n-1)\cdots(n-r+1)$。
- **组合（combination）**：无序选择；**$r$-组合（$r$-combination）** $C(n,r)=\dbinom nr=\dfrac{n!}{r!(n-r)!}$。
- ⭐ **两者的桥**：每个 $r$-组合恰好对应 $r!$ 个 $r$-排列，故 $P(n,r)=C(n,r)\cdot r!$。
- 对称性：$\dbinom nr=\dbinom n{n-r}$；边界 $\dbinom n0=\dbinom nn=1$。

**经典模型**：

| 问题 | 答案 |
|---|---|
| $n$ 人围圆桌（旋转视为同一） | $(n-1)!$ |
| $n$ 人围圆桌且翻转也视为同一 | $(n-1)!/2$ |
| 从 $n$ 人中选 $r$ 人组成委员会 | $\dbinom nr$ |
| 从 $n$ 人中选主席 + 委员会 | $n\dbinom{n-1}{r-1}$ |
| $n$ 个元素的排列中 $a,b$ 相邻 | $2\cdot(n-1)!$（捆绑法） |
| 扑克牌型计数 | 同花顺、四条、葫芦等按"选牌型 × 选花色 × 排面"三步 |

> ⚠️ 相邻/不相邻限制题：**捆绑法**（相邻）与**插空法**（不相邻），先处理限制强的。

## 6.4 二项式系数与恒等式 Binomial Coefficients and Identities

**二项式定理（binomial theorem）**：
$$(x+y)^n=\sum_{k=0}^{n}\binom nk x^{n-k}y^k$$
理由：从 $n$ 个括号里选 $k$ 个贡献 $y$，有 $\binom nk$ 种选法。

**三个推论**：

- $\displaystyle\sum_{k=0}^{n}\binom nk=2^n$（数全部子集）；
- $\displaystyle\sum_{k=0}^{n}(-1)^k\binom nk=0$（$n\ge1$，偶/奇大小子集一样多）；
- $\displaystyle\sum_{k=0}^{n}2^k\binom nk=3^n$（每个元素三种状态）。

**四个恒等式（⭐ 必背）**：

| 名称 | 恒等式 |
|---|---|
| **帕斯卡恒等式 Pascal's identity** | $\dbinom{n+1}{k}=\dbinom n{k-1}+\dbinom nk$（帕斯卡三角形每数 = 肩上两数之和） |
| **范德蒙德恒等式 Vandermonde's identity** | $\dbinom{m+n}{r}=\displaystyle\sum_{k=0}^{r}\binom mk\binom n{r-k}$ |
| 推论 | $\dbinom{2n}{n}=\displaystyle\sum_{k=0}^{n}\binom nk^2$ |
| **曲棍球棒 hockey-stick** | $\displaystyle\sum_{k=r}^{n}\binom kr=\binom{n+1}{r+1}$ |

![[C6.4-帕斯卡三角形.png|420]]
*图 6-3｜帕斯卡三角形：每个数等于肩上两数之和（帕斯卡恒等式）*

**组合证明（combinatorial proof）/ 双计数（double counting）**：找一个集合，用两种方式数它，两种数法给出同一个数，恒等式即得。⭐ 考试"证明恒等式"基本只认这个思路；代数变形可以用来自查。

## 6.5 广义排列与组合 Generalized Permutations and Combinations

### 允许重复

| 类型 | 公式 | 例 |
|---|---|---|
| 允许重复的 $r$-排列 | $n^r$ | 长度 4 的 PIN 码 $=10^4$ |
| 允许重复的 $r$-组合（**星条法 stars and bars**） | $\dbinom{n+r-1}{r}$ | $x_1+\cdots+x_n=r$ 的非负整数解数 |

**星条法**：$r$ 颗星 + $n-1$ 条竖线，共 $r+n-1$ 个位置，选 $r$ 个放星 ⇒ $\dbinom{r+n-1}{r}$。三种等价说法：允许重复的组合、非负整数解个数、$r$ 个不可区分小球放进 $n$ 个可区分盒子。

![[C6.5-星条法示意图.png|600]]
*图 6-4｜星条法：$r$ 颗星与 $n-1$ 条竖线的每种排法对应一种重复组合（例中 $r=5,n=4$，共 56 种）*

### 不可区分物体的排列

$n$ 个物体分 $k$ 类、第 $i$ 类有 $n_i$ 个相同 ⇒ $\dfrac{n!}{n_1!n_2!\cdots n_k!}$（如 MISSISSIPPI）。

### 物体进盒子的五种情形（⭐ 必背）

| 物体 | 盒子 | 方案数 |
|---|---|---|
| 可区分 distinguishable | 可区分 | $k^n$ |
| 不可区分 indistinguishable | 可区分 | $\dbinom{n+k-1}{n}$（星条法） |
| 可区分 | 不可区分，**不许空盒** | $S(n,k)$（**第二类斯特林数 Stirling number of the second kind**） |
| 可区分 | 不可区分，允许空盒 | $\sum_{j=1}^{k}S(n,j)$ |
| 不可区分 | 不可区分 | $n$ 的**整数拆分（partition）**数（无闭式） |

- **斯特林数递推**：$S(n,j)=S(n-1,j-1)+j\,S(n-1,j)$，$S(0,0)=1$，$S(n,0)=0$。
- 闭式：$S(n,j)=\dfrac1{j!}\sum_{i=0}^{j-1}(-1)^i\binom ji(j-i)^n$（用容斥可证，见 §8.6）。

## 6.6 生成排列与组合 Generating Permutations and Combinations

- **词典序（lexicographic order）**：先比第一位，相同再比下一位。
- ⭐ **求下一个排列的算法**（教材 Algorithm 1）：
  1. 从右往左找第一个**升序对** $a_j<a_{j+1}$；
  2. 在 $a_{j+1},\dots,a_n$ 中找**比 $a_j$ 大的最小者** $a_k$；
  3. 交换 $a_j,a_k$；
  4. **反转** $a_{j+1},\dots,a_n$。
  - 若找不到升序对（已降序）则为最后一个排列。
- **下一个位串（next bit string）**：从右往左找第一个 0，改为 1，右边全清 0。
- **下一个 $r$-组合（next $r$-combination）**：从右往左找第一个可增大的位置 $a_i<n-r+i$，加 1，后面依次加 1。
- ⭐ 老师原话："**可能考'为什么这是下一个排列'**"——要能论证：不存在介于两者之间的排列（比后缀大的最小者 + 后缀升序）。
- 用途：不重不漏地枚举；$r$-组合与长度 $n$ 的位串一一对应。

![[C6.6-字典序下一排列的四个动作.png|600]]
*图 6-5｜求下一个排列的四步：找升序对 → 换最小的大者 → 交换 → 反转后缀*

## 本章自检

1. 6 位密码含至少一个数字，共多少种？
2. 100 人中至少几人生日同月？用广义鸽巢原理给出下界。
3. 用组合证明求 $\sum_{k=1}^{n}k\binom nk$。
4. 写出 1 3 5 4 2 的下一个词典序排列，并说明每一步。

---
# 第八章 高级计数技巧 Advanced Counting Techniques

**考试权重**：中等，但**课堂范围只到 §8.1**。老师第 19 节课用半节课讲了这一节，原话是"**第 8 章只要掌握递推这部分**"；§8.2–§8.6 本学期没有讲（`Ch8.1.pdf` 是唯一课件），下面按正文同等深度补全并标〔拓展〕。本章得分点集中在"**建递推 + 动态规划填表**"，但 §8.2–8.6 的公式（主定理、错排、容斥）在第 6、10 章的复杂度题里会用到。

## 8.1 递推关系的应用 Applications of Recurrence Relations

**递推关系（recurrence relation）**：把 $a_n$ 用前面若干项表示的等式（对 $n$ 超过某个下界的一切成立）；**初始条件（initial conditions）** 给出起点；两者合起来唯一确定序列，其显式公式叫**解（solution）**。

### 四类建模（考试就考这四类）

| 模型 | 递推式 | 初始条件 | 解 |
|---|---|---|---|
| 细菌增长 | $a_n=2a_{n-1}$ | $a_0=5$ | $a_n=5\cdot2^n$ |
| **兔子繁殖（Fibonacci）** | $f_n=f_{n-1}+f_{n-2}$ | $f_1=f_2=1$ | $f_n$（斐波那契数） |
| **汉诺塔（Tower of Hanoi）** | $H_n=2H_{n-1}+1$ | $H_0=0$（或 $H_1=1$） | $H_n=2^n-1$ |
| 禁止 `00` 的位串 | $a_n=a_{n-1}+a_{n-2}$ | $a_0=1,a_1=2$ | $a_n=f_{n+2}$ |
| 偶数个 0 的十进制串 | $a_n=8a_{n-1}+10^{n-1}$ | $a_0=1$ | $a_n=(10^n+8^n)/2$ |
| **卡特兰数（Catalan numbers）** | $C_n=\sum_{k=0}^{n-1}C_kC_{n-k-1}$ | $C_0=1$ | $C_n=\dfrac{1}{n+1}\dbinom{2n}{n}$ |

**建模三步**：① 看 $a_n$ 的最后一步有几种"接法"；② 每种接法对应哪个更小的子问题；③ 写出递推并**核对初始条件**（$n$ 从几开始、有没有 $a_0$）。

**汉诺塔的上下界**：上界——递归算法给出 $2^n-1$ 步；下界——最大盘必须移动，且移动前后其余 $n-1$ 盘各要"清空/重建"一次，故 $H_n\ge 2H_{n-1}+1$。两边夹出 $H_n=2^n-1$。

**位串对应**：禁止 `00` 的位串按最后一位分类——以 1 结尾接在任意 $a_{n-1}$ 后，以 0 结尾则前一位必须是 1，接在 $a_{n-2}$ 后。下标偏移是最容易错的地方：$a_n=f_{n+2}$ 而非 $f_n$。

**卡特兰数**：$n+1$ 个因子的**完全加括号（parenthesization）**方案数、$n$ 对括号的合法串数、凸多边形三角剖分数、$n$ 个结点的二叉树形态数，答案都是 $C_n$。
- 递推依据：最后一次乘法把表达式切成左右两段，左段 $C_k$、右段 $C_{n-k-1}$，$k$ 从 0 到 $n-1$。
- 闭式证明要用 §8.4 生成函数，本节只要求会用递推算出前几项（$1,1,2,5,14,42,\dots$）。
- 增长率 $C_n\sim\dfrac{4^n}{n^{3/2}\sqrt\pi}$。

### 动态规划 Dynamic Programming

**问题**：一组活动（讲座），每个有开始时间 $s_j$、结束时间 $e_j$、权重 $w_j$（听众人次），选**两两相容（compatible，$e_i\le s_j$）**的子集使权重和最大。

- 按结束时间排序；定义**前驱（predecessor）** $p(j)=\max\{i<j: e_i\le s_j\}$（不存在记 0）。
- **最优值递推**：$T(j)=\max\{w_j+T(p(j)),\ T(j-1)\}$，$T(0)=0$。
  - 读法：要么选第 $j$ 场（则只能接在 $p(j)$ 之前），要么不选（退化成前 $j-1$ 场）。
- **复杂度**：填表 $O(n)$；排序 + 二分找前驱 $O(n\log n)$；空间 $O(n)$。暴力枚举 $2^n$ 不可行。
- **方案恢复**：从 $T(n)$ 回溯，若 $w_j+T(p(j))\ge T(j-1)$ 则选第 $j$ 场（平局任选一组）。

![[C8.1-讲座时间轴与相容前驱.png|600]]
*图 8-1｜区间调度：按结束时间排序后，$p(j)$ 指向与第 $j$ 场相容的最近一场*

**两个关键词**（老师课上强调的"为什么能这么算"）：

- **最优子结构（optimal substructure）**：全局最优解里，前段必然是相应子问题的最优解；
- **重叠子问题（overlapping subproblems）**：子问题反复出现，所以**存表**（tabulation）而不是重算；带记忆的递归叫**记忆化（memoization）**。

> ⚠️ 易错：$p(j)$ 用 $e_i\le s_j$（**允许端点相接**），写成 $<$ 会丢掉合法安排；$T(j)$ 存的是**前 $j$ 场的最优值**，不是"选第 $j$ 场的最优值"。

## 8.2 求解线性递推 Solving Linear Recurrence Relations〔拓展：课堂未讲〕

- **线性齐次常系数递推**：$a_n=c_1a_{n-1}+\cdots+c_ka_{n-k}$（$c_k\ne0$），**特征方程（characteristic equation）** 为 $r^k-c_1r^{k-1}-\cdots-c_k=0$。
- **二阶三种情形**（$r^2-c_1r-c_2=0$）：

| 情形 | 通解 | 说明 |
|---|---|---|
| 两个不同实根 $r_1,r_2$ | $a_n=\alpha_1r_1^n+\alpha_2r_2^n$ | 用两个初值解 $\alpha_1,\alpha_2$ |
| 重根 $r$ | $a_n=\alpha_1r^n+\alpha_2nr^n$ | 重根必须乘 $n$ |
| 共轭复根 | $a_n=\rho^n(C_1\cos n\theta+C_2\sin n\theta)$ | 了解即可 |

- **斐波那契**：$r^2=r+1$ ⇒ $r=(1\pm\sqrt5)/2$，得 **Binet 公式**
  $$f_n=\frac{1}{\sqrt5}\left[\left(\frac{1+\sqrt5}{2}\right)^n-\left(\frac{1-\sqrt5}{2}\right)^n\right]$$
- **非齐次（nonhomogeneous）**：$a_n=c_1a_{n-1}+c_2a_{n-2}+F(n)$ 的通解 $=$ 齐次通解 $+$ 一个**特解（particular solution）**；$F(n)$ 为多项式或指数时按同型设特解，与齐次解撞型时乘 $n$。
- ⚠️ 求出的系数必须代回初值验证；根为复数时保留 $r^n$ 形式即可，不必强行化三角式。

## 8.3 分治递推 Divide-and-Conquer Algorithms〔拓展：课堂未讲〕

- **分治递推**：$f(n)=af(n/b)+g(n)$——规模 $n$ 的问题拆成 $a$ 个规模 $n/b$ 的子问题，合并代价 $g(n)$。
- ⭐ **主定理（Master Theorem）**：设 $g(n)=cn^d$（$c>0,d\ge0,b>1$），则

| 条件 | 解 |
|---|---|
| $a<b^d$ | $f(n)=O(n^d)$ |
| $a=b^d$ | $f(n)=O(n^d\log n)$ |
| $a>b^d$ | $f(n)=O(n^{\log_ba})$ |

- 常用对照：**二分查找** $f(n)=f(n/2)+1=O(\log n)$；**归并排序** $f(n)=2f(n/2)+n=O(n\log n)$；**Karatsuba 乘法** $3f(n/2)+n=O(n^{\log_23})\approx O(n^{1.585})$；**汉诺塔** $f(n)=2f(n-1)+1=O(2^n)$。
- 主定理不适用时（$g$ 非多项式、$a,b$ 随 $n$ 变）用**递归树（recursion tree）** 或展开法逐层求和。

## 8.4 生成函数 Generating Functions〔拓展：课堂未讲〕

- **生成函数（generating function）**：把序列 $a_0,a_1,\dots$ 编码成幂级数 $G(x)=\sum_{n\ge0}a_nx^n$。
- **五个基本展开**：

| 序列 | 生成函数 |
|---|---|
| $1,1,1,\dots$ | $\dfrac{1}{1-x}$ |
| $1,c,c^2,\dots$ | $\dfrac{1}{1-cx}$ |
| $1,2,3,\dots$（即 $n+1$） | $\dfrac{1}{(1-x)^2}$ |
| 第 $k$ 位为 1、其余 0 | $x^k$ |
| $\dbinom{n}{k}$（固定 $k$） | $\dfrac{x^k}{(1-x)^{k+1}}$ |

- **三条运算**：加法逐项相加；**移位（shifting）** $x^kG(x)$ 右移 $k$ 位；**卷积（convolution）** $G(x)H(x)$ 的 $x^n$ 系数是 $\sum_{k=0}^{n}a_kb_{n-k}$。
- **解递推的流程**（斐波那契）：设 $G(x)=\sum f_nx^n$，由 $f_n=f_{n-1}+f_{n-2}$ 得 $G=xG+x^2G+x$ ⇒ $G(x)=\dfrac{x}{1-x-x^2}$ ⇒ 部分分式拆开、按 $\dfrac{1}{1-cx}$ 展开即得 Binet 公式。
- **卡特兰数**：$C(x)=1+xC(x)^2$ ⇒ $C(x)=\dfrac{1-\sqrt{1-4x}}{2x}$ ⇒ 展开得 $C_n=\dfrac{1}{n+1}\dbinom{2n}{n}$，这就是 §8.1 闭式的证明。
- **广义二项式定理**：$(1+x)^u=\sum_k\dbinom ukx^k$（$u$ 可为负或实数），是拆部分分式的工具。

## 8.5 容斥原理 The Principle of Inclusion–Exclusion〔拓展：课堂未讲〕

- **两集合**：$|A\cup B|=|A|+|B|-|A\cap B|$。
- **三集合**：$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$。
- **一般形式**：
  $$\Big|\bigcup_{i=1}^{n}A_i\Big|=\sum_i|A_i|-\sum_{i<j}|A_i\cap A_j|+\sum_{i<j<k}|A_i\cap A_j\cap A_k|-\cdots+(-1)^{n+1}|A_1\cap\cdots\cap A_n|$$
- **补集形式**（最常用）：数"一个性质都不满足"的对象
  $$\Big|\bigcap_{i=1}^{n}\overline{A_i}\Big|=|U|-\sum_i|A_i|+\sum_{i<j}|A_i\cap A_j|-\cdots$$
- 例：$1$ 到 $100$ 中不被 $2,3,5$ 整除的个数 $=100-(50+33+20)+(16+10+6)-3=26$。
- ⚠️ 正负号交替，漏掉最后一项是最常见的错。

## 8.6 容斥的应用 Applications of Inclusion–Exclusion〔拓展：课堂未讲〕

- **错排（derangement）**：$n$ 个元素的排列中没有一个在原位，个数
  $$D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}=n!\Big(1-\frac1{1!}+\frac1{2!}-\cdots+\frac{(-1)^n}{n!}\Big)$$
  - 递推 $D_n=(n-1)(D_{n-1}+D_{n-2})$，$D_1=0,D_2=1$；$D_n/n!\to1/e\approx0.368$。
- **满射个数**：从 $n$ 元集到 $m$ 元集的满射数 $=\sum_{j=0}^{m}(-1)^j\dbinom mj(m-j)^n$（容斥扣掉"漏掉某个像"）。
- **欧拉函数**：$\varphi(n)=n\prod_{p\mid n}\big(1-\frac1p\big)$，用容斥数"与 $n$ 互素"的对象。
- **筛法**：埃拉托色尼筛（Sieve of Eratosthenes）本质是反复容斥，逐个划掉合数。
- 建模套路：把"至少满足一个坏性质"写成并集再取补；**先明确"性质"是什么**，比记公式重要。

## 本章自检

1. 用递推建模：$n$ 级台阶每次迈 1 或 2 级，共几种走法？初始条件是什么？
2. 汉诺塔 $n=10$ 要多少步？下界论证的关键句是什么？
3. 给定 5 场讲座的时间与权重，写出 $p(j)$ 与 $T(j)$ 表，并恢复最优方案。

---
# 第九章 关系 Relations

**考试权重**：高。老师复习顺序第 3 站。课堂节奏提示：**§9.2 与 §9.3 各只花十几分钟，"考试只出小问"**；主战场是 **§9.1 的六个性质**、**§9.4 的闭包与 Warshall**、**§9.6 的偏序**。老师还说 §9.3 的有向图表示会在第 10 章"从一种画法升级成研究对象"。

## 9.1 关系及其性质 Relations and Their Properties

**二元关系（binary relation from $A$ to $B$）**：$A\times B$ 的子集；$A$ 上的关系是 $A\times A$ 的子集。$(a,b)\in R$ 记作 $aRb$。

- **定义域（domain）/ 值域（range）**；$|A|=m,|B|=n$ 时 $A$ 到 $B$ 的关系共 $2^{mn}$ 个。
- **逆关系（inverse relation）** $R^{-1}=\{(b,a)\mid(a,b)\in R\}$；$R$ 对称 $\iff R=R^{-1}$。

### 六个性质：定义、逻辑写法与判据（⭐ 全章核心）

**约定**：以下 $a,b,c$ 都是**在 $A$ 中取值的个体变元**（量词只在 $A$ 上遍历，不在 $R$ 上遍历）；$aRb$ 与 $(a,b)\in R$ 是同一种写法。$\Delta=\{(a,a)\mid a\in A\}$ 是**对角关系（diagonal relation）**。

| 性质 | 一阶逻辑定义 | 等价写法（集合/运算） | 矩阵判据（$M_R$） | 有向图判据 |
|---|---|---|---|---|
| **自反 reflexive** | $\forall a\,(a,a)\in R$ | $\Delta\subseteq R$ | 主对角线全 1 | 每个顶点有自环 |
| **非自反 irreflexive** | $\forall a\,(a,a)\notin R$ | $R\cap\Delta=\varnothing$ | 主对角线全 0 | 无自环 |
| **对称 symmetric** | $\forall a\forall b\,\big((a,b)\in R\to(b,a)\in R\big)$ | $R=R^{-1}$ | $M=M^t$ | 不同顶点间边成对 |
| **非对称 asymmetric** | $\forall a\forall b\,\big((a,b)\in R\to(b,a)\notin R\big)$ | $R\cap R^{-1}=\varnothing$ | $i\ne j$ 时 $m_{ij},m_{ji}$ 不同时为 1，**且对角线全 0** | 无双向边**且**无自环 |
| **反对称 antisymmetric** | $\forall a\forall b\,\big((a,b)\in R\wedge(b,a)\in R\to a=b\big)$ | $R\cap R^{-1}\subseteq\Delta$ | $i\ne j$ 时 $m_{ij},m_{ji}$ 不同时为 1 | 不同顶点间无双向边 |
| **传递 transitive** | $\forall a\forall b\forall c\,\big((a,b)\in R\wedge(b,c)\in R\to(a,c)\in R\big)$ | $R\circ R\subseteq R$ | $M^{[2]}$ 的 1 处 $M$ 也必为 1 | 两步可达 ⇒ 一步可达 |

**读法**：六条都是"**若……则……**"的全称句，前件列条件、后件下结论；**量词只在 $A$ 上遍历**，所以 $a,b,c$ 允许取同一个元素（除非另写 $a\ne b$）。

### 否定式：要证"不具备"，就找这些反例

把 $\neg$ 推过全称量词（§1.4 的量词德摩根律），六条性质的否定都变成**存在句**：

| 要证不具备 | 否定式（一阶逻辑） | 反例是什么 |
|---|---|---|
| 自反（$\neg$自反） | $\exists a\,(a,a)\notin R$ | 某个点没有自环 |
| 非自反（$\neg$非自反） | $\exists a\,(a,a)\in R$ | 某个点有自环 |
| 对称（$\neg$对称） | $\exists a\exists b\,\big((a,b)\in R\wedge(b,a)\notin R\big)$ | 一条**单向边** |
| 非对称（$\neg$非对称） | $\exists a\exists b\,\big((a,b)\in R\wedge(b,a)\in R\big)$ | 一对**双向边**（含自环） |
| 反对称（$\neg$反对称） | $\exists a\exists b\,\big(a\ne b\wedge(a,b)\in R\wedge(b,a)\in R\big)$ | 不同点之间的**一对双向边** |
| 传递（$\neg$传递） | $\exists a\exists b\exists c\,\big((a,b)\in R\wedge(b,c)\in R\wedge(a,c)\notin R\big)$ | 一条**缺口的二步链** |

> - ⚠️ **非自反 ≠ 自反的否定**。$\neg$自反只要求"有一个点没自环"，非自反要求"**每个点**都没自环"——前者弱、后者强，中间还有一大片"部分有自环"的关系。
> - ⚠️ **$\neg$对称 ≠ 反对称**。$\neg$对称只要一条单向边；反对称要求**任何**一对双向边都只能是自环。
> - ⚠️ **$\neg$非对称 ≠ 对称**。$\neg$非对称只要求存在一对双向边（哪怕是自环），对称要求**所有**边都成双。

### 三个必须说清的逻辑细节

1. **空真是"白送"的**：蕴含前件为假时整句为真（§1.1）。所以**空关系** $\varnothing$ 天然对称、反对称、传递、非自反；只有当 $A=\varnothing$ 时它才自反。反过来，**对角关系** $\Delta$ 自反、对称、反对称、传递，但不是非自反。
2. **传递要三个量词**：$\forall a\forall b\forall c$，第三个变量不能省，也不能写成 $\forall a\forall b\big((a,b)\in R\wedge(b,a)\in R\to(a,a)\in R\big)$（那只是"往返一趟"的特例）。
3. **反对称的 $a=b$ 是结论**：它不假设两点不同；等价地写成 $\forall a\forall b\big(a\ne b\to((a,b)\notin R\vee(b,a)\notin R)\big)$，两种写法在证明里各有用处（前者适合直接证，后者适合反证）。

### 三类经典搭配（合取式）

把性质当命题用 $\wedge$ 拼起来，就是第 9 章后半的全部研究对象（§9.1 末、§9.5、§9.6 反复出现）：

| 名称 | 合取式 | 一阶逻辑合成 |
|---|---|---|
| **等价关系 equivalence relation** | 自反 $\wedge$ 对称 $\wedge$ 传递 | $\forall a\,(a,a)\in R\ \wedge\ \forall a\forall b\big((a,b)\in R\to(b,a)\in R\big)\ \wedge\ \forall a\forall b\forall c\big((a,b),(b,c)\in R\to(a,c)\in R\big)$ |
| **偏序 partial ordering** | 自反 $\wedge$ **反对称** $\wedge$ 传递 | 把中间一条换成 $\forall a\forall b\big((a,b),(b,a)\in R\to a=b\big)$ |
| **严格序 strict order** | **非自反** $\wedge$ 非对称 $\wedge$ 传递 | 即 $<$ 型关系；非自反 + 传递已能推出非对称 |

**证明模板**（把定义直接翻译成写法）：

- 证自反：任取 $a\in A$，验证 $(a,a)\in R$；
- 证对称：设 $(a,b)\in R$（$a,b$ 任意），推出 $(b,a)\in R$；
- 证反对称：设 $(a,b)\in R$ 且 $(b,a)\in R$，推出 $a=b$；
- 证传递：设 $(a,b)\in R$ 且 $(b,c)\in R$，推出 $(a,c)\in R$；
- 证不具备：按上面的否定式**举出具体元素**，并逐项验证（不能只报反例不验证）。

> ⭐ **全章第一大坑：对称与反对称不是反义词**。可以都有（$\{(1,1),(2,2)\}$）、可以都没有（$\{(1,2),(2,1),(1,3)\}$）。唯一禁止的是：存在 $a\ne b$ 使 $(a,b)$ 与 $(b,a)$ 同时在 $R$ 里。**自环对这两条判断毫无影响**。
>
> ⭐ **非对称 = 反对称 + 非自反**（逻辑上：$R\cap R^{-1}=\varnothing$ ⟺ $R\cap R^{-1}\subseteq\Delta$ 且 $R\cap\Delta=\varnothing$）。

![[C9-四个性质的有向图判读.png|560]]
*图 9-1｜四个性质的有向图判读：自反看自环、对称看双向、反对称看有无双向边、传递看二步能否并成一步*


### 关系的运算与复合

- 集合运算：$R_1\cup R_2$、$R_1\cap R_2$、$R_1-R_2$、$\overline{R}$（相对 $A\times A$）。
- **复合（composite）** $S\circ R$：先 $R$ 后 $S$，$(a,c)\in S\circ R\iff\exists b\,(aRb\wedge bSc)$。
  - ⚠️ 记号与函数复合方向相反：$S\circ R$ 是"先 $R$ 后 $S$"。
- **幂（powers）**：$R^1=R$，$R^{n+1}=R^n\circ R$；$R^m\circ R^n=R^{m+n}$。
- ⭐ **传递的等价刻画**：$R$ 传递 $\iff$ 对一切 $n\ge1$ 有 $R^n\subseteq R$；$R$ 传递 $\Rightarrow R^n$ 传递。
- 复合的单调性：$R\subseteq S\Rightarrow R\circ T\subseteq S\circ T$（§9.4 证明"传递闭包最小"时的桥）。
- **补关系（complementary relation）** $\overline R=(A\times A)-R$：把"没关系"也收进来。
- **运算律**：复合满足**结合律** $R\circ(S\circ T)=(R\circ S)\circ T$，但一般**不满足交换律**；**复合的逆倒序**：$(S\circ R)^{-1}=R^{-1}\circ S^{-1}$。
- **六种性质的三类搭配**：自反 + 对称 + 传递 = **等价关系**；自反 + 反对称 + 传递 = **偏序**；非自反 + 非对称 + 传递 = **严格序（strict order）**。

## 9.2 $n$ 元关系与数据库 n-ary Relations and Their Applications〔考试只出小问〕

- **$n$ 元关系（$n$-ary relation）**：$A_1\times\cdots\times A_n$ 的子集；**域（domain）** 是各 $A_i$，**度（degree）** 是 $n$。
- **关系数据模型（relational data model）**：表 = $n$ 元关系，行 = **元组（tuple）**，列 = 属性。
  - **主键（primary key）**：单个域即可唯一确定元组；**复合键（composite key）**：需几个域的笛卡尔积。
  - **外延（extension）**：当前元组集合；**内涵（intension）**：表名与属性定义。
- 三个运算（对应 SQL）：

| 运算 | 记号 | 作用 | SQL |
|---|---|---|---|
| **选择（selection）** | $s_C(R)$ | 挑出满足条件 $C$ 的行 | `WHERE` |
| **投影（projection）** | $P_{i_1\dots i_m}(R)$ | 只保留指定列（**可能减少行数**） | `SELECT` |
| **连接（join）** | $J_p(R,S)$ | 按 $p$ 个公共列拼表，度 $=m+n-p$ | 多表 `FROM` |

## 9.3 关系的表示 Representing Relations

- **零一矩阵（zero–one matrix）** $M_R$：$m_{ij}=1\iff(a_i,b_j)\in R$。
- **有向图（directed graph / digraph）**：顶点为 $A$ 的元素，$(a,b)\in R$ 画有向边 $a\to b$；$a$ 是**起点（initial vertex）**、$b$ 是**终点（terminal vertex）**；$(a,a)$ 是**自环（loop）**。
- 关系运算 ↔ 矩阵运算：

| 关系 | 矩阵 |
|---|---|
| $R_1\cup R_2$ | $M_1\vee M_2$ |
| $R_1\cap R_2$ | $M_1\wedge M_2$ |
| ⭐ $S\circ R$ | $M_R\odot M_S$（**顺序相反**，布尔积） |
| $R^n$ | $M_R^{[n]}$ |
| $R^{-1}$ | $M_R^t$ |

> ⚠️ 复合的矩阵顺序最易错：$S\circ R$ 对应 $M_R\odot M_S$，因为矩阵乘法是"行 × 列"，而关系复合是"先行的关系先作用"。

## 9.4 关系的闭包 Closures of Relations

**闭包（closure w.r.t. property P）**：包含 $R$、具有性质 P、且被一切这样的关系包含的最小关系。

| 闭包 | 记号 | 公式 | 矩阵 | 代价 |
|---|---|---|---|---|
| **自反闭包 reflexive closure** | $r(R)$ | $R\cup\Delta$，$\Delta=\{(a,a)\mid a\in A\}$ | $M\vee I$ | $O(n)$ |
| **对称闭包 symmetric closure** | $s(R)$ | $R\cup R^{-1}$ | $M\vee M^t$ | $O(n^2)$ |
| **传递闭包 transitive closure** | $t(R)=R^*$ | $\bigcup_{n\ge1}R^n$ | 见定理 / Warshall | $O(n^4)$ / $O(n^3)$ |

- **路径（path）**：首尾相接的边序列，长度 = 边数；$(a,b)\in R^n\iff$ 存在从 $a$ 到 $b$ 长度 $n$ 的路径。
- **回路（circuit / cycle）**：起点终点相同、长度 $\ge1$ 的路径。
- **内部顶点（interior vertices）**：路径中除首尾以外的顶点——Warshall 算法里"允许经过的中间点"正是它。
- **连通性关系（connectivity relation）** $R^*=\{(a,b)\mid$ 存在长度 $\ge1$ 的路径 $\}$。
- ⭐ **定理**：$R^*=R\cup R^2\cup\cdots\cup R^n$（$n=|A|$，由鸽巢原理，长度 $\ge n$ 的路径必含回路可删）。
- ⭐ **Warshall 算法**：按"允许经过的内部顶点集合"逐轮扩张，只做赋值判断，$2n^3=O(n^3)$ 次位运算（朴素法 $2n^3(n-1)=O(n^4)$）。
  - 内层循环写法：对每个 $i,j$，$w_{ij}\leftarrow w_{ij}\vee(w_{ik}\wedge w_{kj})$。

![[C9-Warshall例题有向图.png|460]]
*图 9-2｜Warshall 的输入图：每轮允许经过一个新顶点，$W_k$ 记录「只许经过前 $k$ 个点」的可达性*

> ⚠️ 三种闭包**不能随便交换顺序**；求"既自反又对称又传递"的闭包要按 $t(s(r(R)))$ 之类的顺序做，结果与顺序有关。

## 9.5 等价关系 Equivalence Relations

- **等价关系（equivalence relation）**：自反 + 对称 + 传递；$aRb$ 时称 $a$ 与 $b$ **等价（equivalent）**，记 $a\sim b$。
- **等价类（equivalence class）** $[a]_R=\{x\mid xRa\}$；**代表元（representative）** 类中任一元素。
- ⭐ **定理 1（三句话等价）**：$aRb\iff[a]_R\cap[b]_R\ne\varnothing\iff[a]_R=[b]_R$。
- **划分（partition）**：非空、两两不交、并为全集。
- ⭐ **定理 2**：等价关系 ↔ 划分一一对应（等价类构成划分；划分定义"同块即等价"的关系）。

![[C9-集合的划分示意.png|480]]
*图 9-3｜划分：非空、两两不交、并为全集——每一块就是一个等价类*

- **同余类（congruence class）** $[a]_m$：模 $m$ 同余的等价类，共 $m$ 个；$\mathbf Z=\bigcup_{a=0}^{m-1}[a]_m$。
- 计数结论：$n$ 元集上关系总数 $2^{n^2}$，其中自反的 $2^{n(n-1)}$，**传递的个数无通项公式**；划分块大小 $n_1,\dots,n_k$ 对应的等价关系有序对数 $=\sum n_i^2$。

## 9.6 偏序 Partial Orderings

- **偏序（partial ordering）**：自反 + **反对称** + 传递；**偏序集（poset）** $(S,R)$。
  - "偏"= **允许不可比**。标准例：$(\mathbf Z^+,\mid)$、$(P(S),\subseteq)$、$(\mathbf Z,\le)$、字典序。
- **可比（comparable）/ 不可比（incomparable）**；**全序（total / linear ordering）** 任意两元素可比，全序集也叫**链（chain）**。
- **良序集（well-ordered set）**：全序 + 每个非空子集有最小元（$\mathbf Z^+$ 良序，$\mathbf Z$ 不是）。
- **字典序（lexicographic order）**：先比第一分量，相同再比下一个；长度不同时短串视为更小（或按约定的填充）。
- ⭐ **Hasse 图（Hasse diagram）**：删自环、删传递边、边朝上不画箭头；剩下的边是**覆盖关系（covering relation）**——偏序 = 覆盖关系的自反传递闭包，**信息一点不丢**。

![[C9-Hasse图的三步构造.png|600]]
*图 9-4｜Hasse 图三步：删自环 → 删传递边 → 边一律朝上，剩下的正是覆盖关系*

### 四组极值概念（⭐ 最大的易错点）

| 概念 | 定义 | 关键 |
|---|---|---|
| **极大元（maximal）** | 不存在 $b$ 使 $a\prec b$ | 可以有多个 |
| **极小元（minimal）** | 不存在 $b$ 使 $b\prec a$ | 可以有多个 |
| **最大元（greatest）** | $\forall b,\ b\preccurlyeq a$ | 有则唯一（不唯一 = 不存在） |
| **最小元（least）** | $\forall b,\ a\preccurlyeq b$ | 有则唯一 |
| **上界（upper bound）** | 对**指定子集** $A$，$\forall a\in A,\ a\preccurlyeq u$ | 针对子集，不是全集 |
| **最小上界（lub / supremum）** | 上界中最小的 | 有则唯一 |
| **下界（lower bound）/ 最大下界（glb / infimum）** | 对偶 | 有则唯一 |

- 三个标准偏序集的"同一套概念，三张脸"：

| | $(\mathbf Z^+,\mid)$ | $(P(S),\subseteq)$ | $(\mathbf Z,\le)$ |
|---|---|---|---|
| $a\preccurlyeq b$ | $a\mid b$ | $A\subseteq B$ | $a\le b$ |
| lub | $\operatorname{lcm}$ | $\cup$ | $\max$ |
| glb | $\gcd$ | $\cap$ | $\min$ |
| 最小元 | $1$ | $\varnothing$ | 无 |
| 最大元 | 无 | $S$ | 无 |

### 格与格的类型

- **格（lattice）**：任意两元素都有 lub 和 glb 的偏序集；记 $a\vee b=\operatorname{lub}\{a,b\}$，$a\wedge b=\operatorname{glb}\{a,b\}$。
  - 四条运算律：交换、结合、幂等、**吸收**（$a\vee(a\wedge b)=a$）。
- **分配格（distributive lattice）**：$\vee,\wedge$ 互相可分配；$(P(S),\subseteq)$ 是，菱形格不是。
- **有界格（bounded lattice）**：有最小元 0 和最大元 1；有限格必有界。
- **补格（complemented lattice）**：每个 $x$ 存在 $y$ 使 $x\vee y=1$、$x\wedge y=0$（补元可多个）。
- **对偶原理（principle of duality）**：把 $\preccurlyeq$ 换成 $\succcurlyeq$、$\vee\leftrightarrow\wedge$、$0\leftrightarrow1$，真命题仍真。

### 拓扑排序 Topological Sorting（拓展：课堂未讲）

- **相容全序（compatible total ordering）**：包含给定偏序 $R$ 的全序，即 $aRb\Rightarrow a\preccurlyeq b$。
- **引理**：有限非空偏序集必有**极小元**（否则沿"更小"无限下降，与有限性矛盾）。
- **算法**：反复 ① 取一个极小元输出；② 从偏序集中删掉它；直到集合空。
- 例：先修关系 $\{(1,2),(2,3),(1,4)\}$ ⇒ 拓扑序 $1,2,4,3$（不唯一）。
- **复杂度**：朴素实现（每次扫描找极小元）$O(n^2)$；队列 + 入度表（Kahn 算法）$O(n+m)$。
- 应用：先修课安排、编译依赖、项目排期、**DAG 上的动态规划**（按拓扑序递推）。
- ⚠️ 有环图没有拓扑序；Kahn 算法输出不足 $n$ 个点即可判环。

## 本章自检

1. 举一个"既对称又反对称"的关系，以及一个"既不…也不…"的关系。
2. $A=\{1,2,3\}$，$R=\{(1,1),(2,2),(3,3),(1,2)\}$，求 $r(R),s(R),t(R)$，并写出 $M_{R^*}$。
3. 画 $(\{1,2,3,4,6,12\},\mid)$ 的 Hasse 图，指出极大/最大元、上界与 lub。
4. 模 5 同余有几个等价类？各是什么？

---
# 第十章 图 Graphs

**考试权重**：**最高**。老师第 19 节课原话"**第十章最重要**"，理由是"图既有助于学 AI，也有助于学数据库原理"；第 21 节课补"哈密顿路径两年前考过一次"。本章复习优先级：**10.2（度与握手）→ 10.5（欧拉/哈密顿）→ 10.7（平面性判据）→ 10.8（着色）→ 10.4（连通度）**；§10.6 课堂没讲，正文按同等深度补全并标〔拓展〕，优先级最低。

## 10.1 图与图模型 Graphs and Graph Models

- **图（graph）** $G=(V,E)$：**顶点（vertex / node）** 集 $V$、**边（edge）** 集 $E$；**端点（endpoint）**、**关联（incident）**。
- **无向边（undirected edge）** $\{u,v\}$ 与**有向边（directed edge / arc）** $(u,v)$；**自环（loop）** 两端相同；**重边（multiple edges）** 同端点多条，其条数为**重数（multiplicity）**。
- **有限图 / 无限图**。

### 六类图（三问定类）

| 图 | 边有方向 | 允许多重边 | 允许自环 | 典型模型 |
|---|---|---|---|---|
| **简单图 simple graph** | 无 | 否 | 否 | 相识图、合作图、$K_n$ |
| **多重图 multigraph** | 无 | 是 | 否 | 城市间多条航班 |
| **伪图 pseudograph** | 无 | 是 | 是 | 带自环的链路 |
| **简单有向图 simple directed graph** | 有 | 否 | 否 | 影响图、引用图、循环赛 |
| **有向多重图 directed multigraph** | 有 | 是 | 是 | 电话记录 |
| **混合图 mixed graph** | 有无并存 | 是 | 是 | 双向+单向骨干网 |

三问顺序：**方向有没有意义 → 同一对端点会不会有多条边 → 会不会自己连自己**。允许 ≠ 一定出现；一旦需要记录重数或方向，就只能升级到更宽的一类，**升级不可逆**。

### 图模型（考试常以"建模"小问出现）

- **相识图（acquaintanceship graph）**、**影响图（influence graph）**、**合作图（collaboration graph）**；
- **通话图（call graph）**、**网页图（web graph）**、**引用图（citation graph）**；
- **模块依赖图（module dependency graph）**、**先序图（precedence graph）**（课程先修、项目排期）；
- **航线图（airline route）**、**道路图（road map）**、**生态位重叠图（niche overlap graph）**、**蛋白质作用图（protein interaction）**；
- **循环赛（round-robin tournament）**：$n$ 队两两赛一场共 $\binom n2$ 场（6 队 15 场）；**单淘汰赛（single-elimination）** 16 队共 15 场（每场淘汰一队）。

## 10.2 图的术语与特殊类型 Graph Terminology and Special Types〔本章第一大考点〕

- **邻接（adjacent）**、**邻域（neighborhood）** $N(v)$、**度（degree）** $\deg v$（自环计 2）、**悬挂点（pendant vertex，度 1）**、**孤立点（isolated vertex，度 0）**、**正则图（regular graph）**（每点同度，$k$-正则）。
- ⭐⭐ **握手定理（the handshaking theorem）**：
  $$\sum_{v\in V}\deg v=2|E|$$
  无向图中**奇度顶点个数必为偶数**。有向图版：$\sum\deg^-(v)=\sum\deg^+(v)=|E|$。
- **入度（in-degree）/ 出度（out-degree）**；有向图的**底层无向图（underlying undirected graph）**。

### 五个标准图族（必背数值）

| 图族 | 顶点数 | 边数 | 度 | 要点 |
|---|---|---|---|---|
| **完全图 $K_n$（complete graph）** | $n$ | $\binom n2$ | $n-1$ | 每对点恰一条边；$\chi(K_n)=n$ |
| **圈 $C_n$（cycle）** | $n\ge3$ | $n$ | $2$ | 二分 $\iff n$ 偶 |
| **轮 $W_n$（wheel）** | $n+1$ | $2n$ | 中心 $n$、轮缘 $3$ | $C_n$ 加一个连所有点的中心 |
| **$n$ 立方体 $Q_n$（$n$-cube）** | $2^n$ | $n2^{n-1}$ | $n$ | 顶点是长度 $n$ 的位串，差一位相邻；二分 |
| **完全二分图 $K_{m,n}$** | $m+n$ | $mn$ | $m$ / $n$ | 跨侧全连；$\chi=2$ |

自查：每条都用握手定理验一遍（$W_n$：$n+3n=4n=2\cdot2n$ ✓）。

![[C10.2-原图-超立方体Qn.png|460]]
*图 10-1｜$n$ 立方体 $Q_n$：顶点是长度 $n$ 的位串，只差一位就相邻（$Q_3$ 有 8 点 12 边，每点度 3）*

### 二分图与匹配

- **二分图（bipartite graph）**：$V=V_1\cup V_2$、同侧无边；$(V_1,V_2)$ 是**二分划分（bipartition）**。
- ⭐ **判据**：简单图二分 $\iff$ 可二着色 $\iff$ **不含奇圈**。
- **匹配（matching）**：两两不共享端点的边集；**最大匹配（maximum matching）**、**完全匹配（complete matching）**（覆盖 $V_1$ 全部顶点）。
- **Hall 婚姻定理（Hall's marriage theorem / SDR）**：存在 $V_1\to V_2$ 的完全匹配 $\iff$ 对一切 $A\subseteq V_1$，$|N(A)|\ge|A|$。

### 子图与补图

- **子图（subgraph）**、**诱导子图（induced subgraph）**、**生成子图（spanning subgraph）**、**并图（union）**、**收缩（contraction）**。
- **补图（complement）** $\overline G$：同顶点集，边取反；**自补图（self-complementary）**。
- **度序列（degree sequence）**、**图形序列（graphical sequence）**（能否由某简单图实现）。

## 10.3 图的表示与图同构 Representing Graphs and Graph Isomorphism

- **邻接表（adjacency list）**、**邻接矩阵（adjacency matrix）** $A$、**关联矩阵（incidence matrix）**（顶点 × 边）。
  - **稀疏（sparse）** 图用邻接表省空间，**稠密（dense）** 图用矩阵方便查边。
- **同构（isomorphic）**：存在双射 $f:V_1\to V_2$ 保持邻接关系；$G_1\cong G_2$。
- **不变量（invariant）**：顶点数、边数、度序列、连通分量数、圈长分布——**不变量不同必不同构；不变量相同未必同构**。
- 判非同构的实用顺序：比顶点数 → 比边数 → 比度序列 → 比特殊结构（圈、割点、二分性）。
- **反向图（converse digraph）**：把所有有向边反向，记 $G^{\text{rev}}$；$G\cong G^{\text{rev}}$ 当且仅当存在反自同构。
- **带宽（bandwidth）**：在所有顶点标号中，使相邻顶点标号差的最大值最小，这个最小值叫带宽；衡量图的"细长程度"，与矩阵带宽（非零元集中在对角线附近）是同一件事。
- **自同构（automorphism）**：图到自身的同构；自同构的个数是不变量之一，可用来排除同构候选。

> ⚠️ 同构映射要**双向验证**：既验证"有边 ⇒ 像之间有边"，也验证"像之间有边 ⇒ 原像有边"。

## 10.4 连通性 Connectivity

- **路径（path）**（本书允许重复边，等同通行的 walk）、**简单路径（simple path）**（不重复边）、**回路（circuit）**（长 $\ge1$ 的闭合路径）。
- **连通（connected）**：任意两点有路径；**连通分量（connected component）**：极大连通子图。
- **割点（cut vertex / articulation point）**：删去后连通分量增加；**桥（bridge / cut edge）** 同理；**不可分图（nonseparable）** 无割点。
- **点割（vertex cut）/ 边割（edge cut）**；**点连通度（vertex connectivity）** $\kappa(G)$、**边连通度（edge connectivity）** $\lambda(G)$、**最小度** $\delta(G)$。
  - ⭐ 三条不等式：$\kappa(G)\le\lambda(G)\le\delta(G)$（简单图）；$K_n$ 的 $\kappa=\lambda=n-1$；不连通图或 $K_1$ 取 0。
  - **$k$-连通（$k$-connected）**：$\kappa(G)\ge k$。
- **强连通（strongly connected）/ 弱连通（weakly connected）**、**强连通分量**；**无环（acyclic）** 与**有向无环图（DAG）**——拓扑排序（§9.6）的处理对象。
- **极大图（maximal）/ 极小图（minimal）**：必须先点名性质 $P$——关于 $P$ 极大 = 再加一条边就失去 $P$；关于 $P$ 极小 = 再删一条边就失去 $P$。例：$K_n$ 关于"是简单图"极大；树关于"连通"极小、关于"无环"极大。
- **树（tree）** 与**生成树（spanning tree）**：课堂插入讲，教材在 §11.1——$n$ 点连通图至少有 $n-1$ 条边，生成树恰有 $n-1$ 条边且无圈。
- **Menger 定理**：$u,v$ 之间**内部不相交的路径**的最大条数 $=$ 分离 $u,v$ 所需删去的最少顶点数（点版）；边版把"顶点"换成"边"。
  - 推论：$\kappa(G)\ge k$ 当且仅当任意两点间有 $k$ 条内部不相交路径——这是连通度的**路径刻画**。
- **强连通定向（strong orientation）**：无桥连通图可把每条边定向使结果强连通（Robbins 定理）；有桥则不可能。
- 应用：网络**容错度**（$k$ 条独立路径 ⇒ 坏 $k-1$ 条仍连通）、并行机网络的连通度与直径权衡。

![[C10.4-原图-连通度五例.png|600]]
*图 10-2｜五张连通图：先判"是否连通"，再数"最少删几个点/边才断"——这就是 $\kappa$ 与 $\lambda$；$\delta$ 只是度的下界*

- **距离（distance）** $d(u,v)$、**离心率（eccentricity）**、**直径（diameter）**、**半径（radius）**。
- ⭐ **走法数**：$(A^r)_{ij}$ = 从 $v_i$ 到 $v_j$ 长 $r$ 的**走法**数（允许重复顶点）。

> ⚠️ 本书 `path` 允许重复边，`simple path` 才禁重边。$A^r$ 数的是走法，**不是简单路径**；$r>n-1$ 时必然重复。

## 10.5 欧拉路径与哈密顿路径 Euler and Hamilton Paths〔本章第二大考点〕

| | **欧拉 Euler**（走遍**边**） | **哈密顿 Hamilton**（走遍**点**） |
|---|---|---|
| 回路定义 | 含每条边**恰好一次**的简单回路 | 经每个顶点**恰好一次**的回路 |
| 充要判据 | ⭐ **有**：非孤立部分连通 + 奇度点 0 个（回路）/ 恰 2 个（路径） | ⭐ **没有已知判据**，判定是 NP-完全的 |
| 有向版 | 每点入度 = 出度（路径版：起点出度多 1、终点入度多 1） | 同样无实用判据 |
| 充分条件 | — | **Dirac**：$\delta(G)\ge n/2$；**Ore**：任意非邻点对 $\deg u+\deg v\ge n$（都是充分非必要，$C_5$ 是反例） |
| 算法 | **Fleury**（$O(m^2)$）、**Hierholzer**（$O(m)$） | 已知最好算法指数最坏时间 |
| 在 $K_n$ 上 | 有欧拉回路 $\iff n$ 奇 | $n\ge3$ 一律有哈密顿回路 |
| 应用 | 七桥、一笔画、扫街/邮递员、DNA 拼接 | 十二面体、**Gray 码**、旋转编码、TSP |

- 欧拉回路判据的证明要点：必要性——回路进出每个顶点成对，度必为偶；充分性——从任一点出发不断走未用边，回到起点得闭迹；若未走完，因连通且所有度仍为偶，可在已用顶点上"拼接"。
- **一笔画谜题（continuous motion puzzle）**：图形能否一笔画成，正是"欧拉路径是否存在"；弯刀谜题（scimitars）是同一判据的变体。
- **Gray 码（Gray code）**：$Q_n$ 的哈密顿回路，相邻码字只差一位；用于**旋转编码器（rotary encoder）**。存在性由 $Q_n$ 的哈密顿性保证（习题 49）。
- **骑士周游（knight's tour）**：棋盘上马的哈密顿路径/回路，是"看起来能走、判起来很难"的典型。
- 常见图族的欧拉/哈密顿速查：$K_n$ 欧拉 $\iff n$ 奇、哈密顿 $\iff n\ge3$；$C_n$ 两者都有；$Q_n$ 两者都有（$n\ge2$）；Petersen 图**无**哈密顿回路（但删任一点后有），也无欧拉回路（3-正则，度全奇）。
- **名称陷阱**：欧拉公式（平面图）、欧拉回路、欧拉函数（数论）都冠 Euler 之名，但说的是不同的事，写 by Euler's formula 时必须看语境；哈密顿回路与物理里的哈密顿量无关。

![[C10.5-原图-欧拉路径三例.png|600]]
*图 10-3｜欧拉路径三例：奇度点 0 个 ⇒ 有回路；恰 2 个 ⇒ 只有路径；4 个 ⇒ 都没有*

## 10.6 最短路径问题 Shortest-Path Problems〔拓展：课堂未讲〕

- **带权图（weighted graph）**：每条边带实数权（长度、费用、时延）；路线的**长度（length）** 是边权之和；**最短路问题（shortest-path problem）** 求两点间长度最小的路径。

**Dijkstra 算法（单源、非负权）** 分四步：

1. 源点标 0、其余标 $\infty$，$S=\varnothing$；
2. 取不在 $S$ 中、标号最小的顶点 $u$，加入 $S$；
3. **松弛（relaxation）**：对 $u$ 的每个邻点 $v$，若 $L(u)+w(u,v)<L(v)$ 则更新 $L(v)$；
4. 重复至所有顶点入 $S$。

- 正确性依据：非负权保证"已确定的标号不会再变小"。例：$a\to d\to e\to z$ 长 $2+3+1=6$。
- 复杂度：邻接矩阵 $O(n^2)$；二叉堆 $O((n+m)\log n)$。⚠️ **负权边会破坏正确性**，改用 Bellman–Ford（$O(nm)$）。
- **Floyd 算法**（全对最短路）：按"允许经过的中间顶点集合"逐轮扩张，$d_{ij}\leftarrow\min(d_{ij},d_{ik}+d_{kj})$，三重循环 $O(n^3)$；允许负权但**不允许负圈**。
- **旅行商问题（TSP, traveling salesperson problem）**：经过每个城市恰好一次并回到起点的最短回路；$n$ 城市不同回路数 $\dfrac{(n-1)!}{2}$；TSP 是 NP-难。
  - **近似算法**：用 MST 构造 2-近似解（**近似比 approximation ratio** 为 2），Christofides 算法做到 1.5-近似。
- 应用：地图导航、网络路由、物流排线、电路布线。

![[C10.6-原图-Dijkstra逐步标签.png|600]]
*图 10-4｜Dijkstra 的逐步标号：每次钉死当前最小标号，再松弛它的邻点*

## 10.7 平面图 Planar Graphs〔第三大考点〕

- **平面图（planar graph）**：能画在平面上使边只在顶点相交；这样的画法叫**平面表示（planar representation）**，被边围成的区域叫**面（region / face）**，**面的度（degree of a region）** 是围成它的边数（桥被同一个面数两次）。
- ⭐ **欧拉公式（Euler's formula）**：连通平面图
  $$v-e+r=2$$
  推广：$c$ 个连通分量时 $v-e+r=1+c$；且 $\sum_{R}\deg(R)=2e$。

![[C10.7-原图-面与面度.png|520]]
*图 10-5｜面与面度：每条边被两个面各数一次，桥被同一个面数两次*

- ⭐ **两条边数上界**：
  - 简单连通平面图、$v\ge3$：$e\le3v-6$（排除 $K_5$：$10>9$）；
  - 再加"无三角形"：$e\le2v-4$（排除 $K_{3,3}$：$9>8$）；
  - 推论：连通平面简单图必有 $\deg\le5$ 的顶点（5 色/6 色归纳的入场券）。
- ⚠️ **不等式只能用来排除，不能用来确认**：$K_{3,3}$ 过得了 $e\le3v-6$ 却非平面；**Petersen 图**两条不等式全过（$v=10,e=15$）仍非平面。要"确认不平面"必须找**障碍子图**。
- **细分（subdivision）**、**同胚（homeomorphic）**；⭐ **Kuratowski 定理**：图非平面 $\iff$ 含与 $K_5$ 或 $K_{3,3}$ 同胚的子图（证明超出本书范围，只要求会陈述、会用）。
- **对偶图（dual graph）** $G^*$：每个面取一个顶点，跨每条边连一条边（桥对应自环）；平面图的对偶仍平面，连通时 $(G^*)^*=G$。
  - 欧拉公式在对偶图里"角色互换"：$v^*=r$，$e^*=e$，$r^*=v$。
  - 用途：地图着色 $=$ 对偶图的顶点着色，四色定理等价于"平面图的对偶图 4-可着色"。
- **交叉数（crossing number）**：画在平面上所需的最少交叉数；平面图交叉数为 0，$\operatorname{cr}(K_5)=\operatorname{cr}(K_{3,3})=1$。
- **厚度（thickness）**：把图分解成多少个平面图之并，$K_n$ 的厚度约 $\lceil(n+7)/6\rceil$；用于电路板分层。
- **曲面嵌入**：环面上 $K_5,K_{3,3}$ 都能无交叉嵌入——"平面"是欧拉公式的前提，换曲面要加**亏格（genus）** 项。

![[C10.8-原图-地图与对偶图.png|600]]
*图 10-6｜地图到对偶图：每个面变成一个顶点，跨边连边——地图着色变成对偶图顶点着色*

## 10.8 图着色 Graph Coloring

- **着色（coloring）**、**真着色（proper coloring）**：相邻顶点不同色；**色数（chromatic number）** $\chi(G)$：最少颜色数。
- ⭐ **常见色数**：

| 图 | $\chi$ | 理由 |
|---|---|---|
| $K_n$ | $n$ | 两两相邻 |
| $K_{m,n}$ | $2$ | 同侧不相邻 |
| $C_n$ | $2$（$n$ 偶）/ $3$（$n$ 奇） | 交替涂色，奇数绕回撞色 |
| $W_n$ | $3$（$n$ 偶）/ $4$（$n$ 奇） | 轮缘 + 中心 |

- ⭐ **上下界**：$\omega(G)\le\chi(G)\le\Delta(G)+1$（下界来自团 clique，上界来自贪心算法）。
- ⭐ **四色定理（four color theorem）**：每个平面图 $\chi\le4$；4 是紧的（$K_4$ 需要 4 色）。
- **应用**：地图着色、**排考（考试时段安排）**、频道分配——建模为"冲突图（conflict graph）"，色数 = 最小时段数/频道数。

![[C10.8-原图-考试排程的着色与时段表.png|600]]
*图 10-7｜排考：冲突图 $\chi=4$ ⇒ 最少 4 个时段，每个时段是一个独立集*

### 边色数与相关参数（拓展）

- **边着色（edge coloring）**：相邻边不同色；**边色数（edge chromatic number）** $\chi'(G)$ 是最少颜色数。
- ⭐ **Vizing 定理**：简单图 $\Delta\le\chi'\le\Delta+1$；二分图更强，$\chi'=\Delta$（König 定理）。
- **独立集（independent set）**：两两不相邻的顶点集；**独立数（independence number）** $\alpha(G)$ 是最大独立集大小。
  - 关系：$\alpha(G)=\omega(\overline G)$（补图的团数）；$\chi(G)\ge\dfrac{n}{\alpha(G)}$（每个颜色类都是独立集）。
- **支配集（dominating set）**：每个不在集合里的顶点都与集合中某点相邻；**支配数（domination number）** $\gamma(G)$。应用：基站选址、监控布点。
- **$k$-重着色（$k$-tuple coloring）** $\chi_k(G)$：每顶点给 $k$ 种颜色、相邻顶点颜色集合不交；$\chi_1=\chi$。
- **团（clique）与团数** $\omega(G)$：两两相邻的顶点集；$\omega\le\chi$ 是最容易得的下界。

> ⚠️ 加一条边色数可能 +1（老师课上举的 $G$ 与 $H=G+ag$，$\chi$ 从 3 变 4），不能想当然认为"边多了色数不变"。

## 本章三个高频失分点（老师点名）

1. **自环算 2 度**（握手定理里最容易错），而邻接矩阵里自环只记 1——两处约定不同，别混。
2. **$A^r$ 数的是走法，不是简单路径**；题目问"不重复点的路径"时不能套 $A^r$。
3. **Kuratowski 与四色定理都不要求证明**，但要求能**陈述**并会用：前者判不平面，后者给"$\chi\le4$"上界。

## 本章自检

1. 8 个点的简单图能否每个点度数都为 3？为什么？
2. $K_5$ 有欧拉回路吗？有哈密顿回路吗？
3. 12 点、每点度 3 的连通平面图，边数和面数各是多少？
4. 一个 7 点图含三角形若干，$\chi=4$，能否据此判定它非平面？

---
# 附录 A 跨章必背表

## A1 命题逻辑与等价律

| 名称 | 形式 |
|---|---|
| 消箭头 | $p\to q\equiv\neg p\vee q$ |
| 逆否 | $p\to q\equiv\neg q\to\neg p$ |
| 条件否定 | $\neg(p\to q)\equiv p\wedge\neg q$ |
| 双条件定义 | $p\leftrightarrow q\equiv(p\to q)\wedge(q\to p)$ |
| 德摩根 | $\neg(p\wedge q)\equiv\neg p\vee\neg q$；$\neg(p\vee q)\equiv\neg p\wedge\neg q$ |
| 量词德摩根 | $\neg\forall xP\equiv\exists x\neg P$；$\neg\exists xP\equiv\forall x\neg P$ |

优先级：$\neg>\wedge>\vee,\oplus>\to>\leftrightarrow$（同级从左到右）。

## A2 推理规则

| 规则 | 形式 |
|---|---|
| modus ponens | $p,\ p\to q\Rightarrow q$ |
| modus tollens | $\neg q,\ p\to q\Rightarrow\neg p$ |
| hypothetical syllogism | $p\to q,\ q\to r\Rightarrow p\to r$ |
| disjunctive syllogism | $p\vee q,\ \neg p\Rightarrow q$ |
| addition | $p\Rightarrow p\vee q$ |
| simplification | $p\wedge q\Rightarrow p$ |
| conjunction | $p,\ q\Rightarrow p\wedge q$ |
| resolution | $p\vee q,\ \neg p\vee r\Rightarrow q\vee r$ |
| universal instantiation | $\forall xP(x)\Rightarrow P(c)$ |
| universal generalization | $P(c)$（$c$ 任意）$\Rightarrow\forall xP(x)$ |
| existential instantiation | $\exists xP(x)\Rightarrow P(c)$（$c$ 新） |
| existential generalization | $P(c)\Rightarrow\exists xP(x)$ |

## A3 计数公式

| 场景 | 公式 |
|---|---|
| 乘法/加法/减法/除法原理 | $n_1n_2$；$n_1+n_2$（不交）；$n_1+n_2-\lvert A\cap B\rvert$；$n/d$ |
| 鸽巢（广义） | 至少一盒含 $\ge\lceil N/k\rceil$ |
| $r$-排列 | $P(n,r)=\dfrac{n!}{(n-r)!}$ |
| $r$-组合 | $\dbinom nr=\dfrac{n!}{r!(n-r)!}$ |
| 允许重复的排列 | $n^r$ |
| 允许重复的组合 | $\dbinom{n+r-1}{r}$ |
| 不可区分物体排列 | $\dfrac{n!}{n_1!\cdots n_k!}$ |
| 圆桌 | $(n-1)!$（翻转同则除以 2） |
| 二项式定理 | $(x+y)^n=\sum_k\binom nk x^{n-k}y^k$ |
| 帕斯卡 / 范德蒙德 | $\binom{n+1}{k}=\binom n{k-1}+\binom nk$；$\binom{m+n}{r}=\sum_k\binom mk\binom n{r-k}$ |
| 曲棍球棒 | $\sum_{k=r}^{n}\binom kr=\binom{n+1}{r+1}$ |
| 斯特林数 | $S(n,j)=S(n-1,j-1)+jS(n-1,j)$ |

## A4 递推与动态规划

| 对象 | 递推 | 解 |
|---|---|---|
| 汉诺塔 | $H_n=2H_{n-1}+1$ | $2^n-1$ |
| 斐波那契 | $f_n=f_{n-1}+f_{n-2}$ | $f_1=f_2=1$ |
| 卡特兰 | $C_n=\sum_{k=0}^{n-1}C_kC_{n-k-1}$ | $\dfrac{1}{n+1}\dbinom{2n}{n}$ |
| 区间调度 | $T(j)=\max\{w_j+T(p(j)),T(j-1)\}$ | $T(0)=0$，$O(n\log n)$ |
| 主定理 | $f(n)=af(n/b)+cn^d$ | $a<b^d:O(n^d)$；$a=b^d:O(n^d\log n)$；$a>b^d:O(n^{\log_ba})$ |
| 错排 | $D_n=(n-1)(D_{n-1}+D_{n-2})$ | $D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$ |

## A5 关系

| 性质 | 一阶逻辑（$a,b,c\in A$） | 判据（$M_R$） | 闭包 |
|---|---|---|---|
| 自反 | $\forall a\,(a,a)\in R$ | 对角线全 1 | $r(R)=R\cup\Delta$，$M\vee I$ |
| 非自反 | $\forall a\,(a,a)\notin R$ | 对角线全 0 | — |
| 对称 | $\forall a\forall b\big((a,b)\in R\to(b,a)\in R\big)$ | $M=M^t$ | $s(R)=R\cup R^{-1}$，$M\vee M^t$ |
| 非对称 | $\forall a\forall b\big((a,b)\in R\to(b,a)\notin R\big)$ | 双向不同真且对角线全 0 | — |
| 反对称 | $\forall a\forall b\big((a,b),(b,a)\in R\to a=b\big)$ | $i\ne j$ 时 $m_{ij},m_{ji}$ 不同时 1 | — |
| 传递 | $\forall a\forall b\forall c\big((a,b),(b,c)\in R\to(a,c)\in R\big)$ | $M^{[2]}\subseteq M$ | $t(R)=R^*=\bigcup_{n\ge1}R^n$，Warshall $O(n^3)$ |

## A6 图论判据汇总

| 问题 | 判据 |
|---|---|
| 握手定理 | $\sum\deg v=2\lvert E\rvert$（自环计 2） |
| 二分 | $\iff$ 可二着色 $\iff$ 无奇圈 |
| 欧拉回路 | 连通 + 奇度点 0 个 |
| 欧拉路径 | 连通 + 奇度点 0 或 2 个 |
| 哈密顿 | 无充要判据；Dirac $\delta\ge n/2$、Ore $\deg u+\deg v\ge n$ 为充分条件 |
| 平面（必要） | $e\le3v-6$；无三角形 $e\le2v-4$ |
| 平面（充要） | 含 $K_5$ 或 $K_{3,3}$ 的细分 $\iff$ 非平面（Kuratowski） |
| 欧拉公式 | $v-e+r=2$（连通平面图） |
| 色数 | $\omega\le\chi\le\Delta+1$；平面图 $\chi\le4$ |

## A7 复杂度速查

| 算法/操作 | 复杂度 |
|---|---|
| 集合并交（位串） | $O(n)$ |
| 关系复合（布尔积） | $O(n^3)$ |
| 传递闭包（朴素 / Warshall） | $O(n^4)$ / $O(n^3)$ |
| Dijkstra | $O(n^2)$ |
| Floyd | $O(n^3)$ |
| Fleury / Hierholzer | $O(m^2)$ / $O(m)$ |
| 区间调度 DP | $O(n\log n)$ |

---

# 附录 B 考试注意事项

## B1 答题规范（违反即扣分）

1. **全英文作答**。学院明确要求卷面不出现中文；术语用教材原词（见附录 C），推导依据写英文规则名。
2. **每一步写依据**。右侧标规则名（by modus ponens / by De Morgan's law）或公式；记不住名字写公式同样给分。
3. **复合结论要落到整个表达式**。证明 $A\equiv B$ 必须给出 $A\equiv\cdots\equiv B$ 的完整链条，不能只证各分量。
4. **符号统一**：$\equiv$ 与 $\Leftrightarrow$ 二选一用到底；$\mathbf T/\mathbf F$ 不当变量；$\subset$ 表示真子集。
5. **量词题写清论域**。论域选"全班学生"比"所有人 + 谓词"更省事，但一旦省略谓词，结论里也不能再出现该谓词。
6. **构造性证明要给见证**（witness）并验证；**唯一性证明分两段**（存在 + 唯一）。
7. **反例必须验证**：不能只报一个数，要说明它确实使命题为假。

## B2 审题关键词

| 题干词 | 要求 |
|---|---|
| determine / find / compute | 给结果，计算过程可简写但关键步骤要在 |
| prove / show that | 完整证明，方法可自选（若指定方法必须用指定的） |
| disprove | 举反例并验证 |
| construct / give an example | 给出对象 + 验证满足条件 |
| justify / explain | 说明理由，不能只写答案 |
| how many | 给数值 + 计数依据（用了哪条原理） |
| if and only if | 两个方向都要证 |

## B3 时间分配建议（120 分钟）

- 开卷 5 分钟通读，按分值排序，先做会的；
- 计算题（计数、闭包、最短路、色数）控制在每题 10–15 分钟；
- 证明题留足 15 分钟，先写骨架再补细节；
- 最后 10 分钟只做三件事：检查符号统一、检查每步是否有依据、检查是否漏问（"求 $x$ 并说明"这类）。

## B4 三十条高频失分

**逻辑与证明**

1. 推导步骤不写规则名。
2. $\neg(p\to q)$ 错写成 $\neg p\to\neg q$（正确是 $p\wedge\neg q$）。
3. "only if" 方向搞反（$p$ only if $q$ 是 $p\to q$）。
4. 用 $\mathbf T/\mathbf F$ 当代换字母。
5. $\forall$ 配 $\wedge$ 或 $\exists$ 配 $\to$（正确：$\forall$ 配 $\to$，$\exists$ 配 $\wedge$）。
6. 否定句不把量词推到底，直接写 "It is not the case that…"。
7. 把逆命题当成逆否命题用。
8. 证明中出现除以零、开方增根。
9. 用待证结论当步骤（循环论证）。
10. WLOG 说不出具体变换。
11. 分情况漏掉边界（实数漏 0）。
12. 存在性证明只构造不验证。

**集合与函数**

13. 混淆 $\varnothing$ 与 $\{\varnothing\}$。
14. 把值域当陪域（$f:\mathbf R\to\mathbf R,f(x)=x^2$ 不是满射）。
15. $f\circ g$ 顺序写反（先 $g$ 后 $f$）。
16. 取整函数随意拆分（$\lceil x+y\rceil\ne\lceil x\rceil+\lceil y\rceil$）。
17. 无限集上仍用"单射 $\iff$ 满射"。

**计数**

18. "或"当成"且"，把加法做成乘法。
19. 容斥忘记减交集。
20. 星条法写成 $\binom{n+r-1}{n-1}$ 却按 $r$ 取（两者相等但别混口径）。
21. 圆桌排列忘记除以旋转（或翻转）。
22. 递推初始条件个数与回看深度不匹配。
23. 二项式系数下标错位（$n$ 与 $n+1$）。

**关系**

24. 把"对称"与"反对称"当反义词。
25. 复合的矩阵顺序写成 $M_S\odot M_R$。
26. 求传递闭包只算到 $R^2$（应到 $R^n$）。
27. Hasse 图忘删传递边、忘删自环。
28. 混淆极大元与最大元（极大可多个，最大唯一）。

**图**

29. 握手定理中自环只算 1 度（应为 2）。
30. 用 $A^r$ 数"不重复顶点的路径"；把 $e\le3v-6$ 当成平面性的充分条件。

---
# 附录 C 术语总表（中英对照）

> 左列是中文叫法，右列是**卷面上会出现的教材原文术语**。答题时推导依据也用右列（by modus ponens、by De Morgan's law）。

## C1 逻辑与证明

| 中文 | English |
|---|---|
| 命题 | proposition |
| 真值 | truth value |
| 命题变量 | propositional variable |
| 原子命题 / 复合命题 | atomic proposition / compound proposition |
| 否定 | negation |
| 合取 | conjunction |
| 析取 / 含或 | disjunction / inclusive or |
| 异或 / 排他或 | exclusive or |
| 蕴涵 / 条件语句 | implication / conditional statement |
| 前件 | antecedent (hypothesis, premise) |
| 后件 | consequent (conclusion) |
| 逆命题 / 逆否命题 / 否命题 | converse / contrapositive / inverse |
| 充分条件 / 必要条件 | sufficient condition / necessary condition |
| 空真 | vacuous truth |
| 实质蕴涵 | material implication |
| 双条件 | biconditional |
| 真值表 | truth table |
| 运算符优先级 | precedence of logical operators |
| 位 / 位串 / 按位运算 | bit / bit string / bitwise operations |
| 系统规约 / 一致的 | system specification / consistent |
| 布尔检索 | Boolean search |
| 逻辑门 / 反相器 / 与门 / 或门 | logic gate / inverter / AND gate / OR gate |
| 组合电路 | combinational circuit |
| 骑士与无赖谜题 | knights and knaves puzzle |
| 永真式 | tautology |
| 矛盾式 | contradiction |
| 可能式 | contingency |
| 可满足的 | satisfiable |
| 逻辑等价 | logical equivalence |
| 同一律 / 支配律 / 幂等律 | identity law / domination law / idempotent law |
| 双重否定律 | double negation law |
| 交换律 / 结合律 / 分配律 | commutative / associative / distributive law |
| 德摩根律 | De Morgan's laws |
| 吸收律 / 否定律 | absorption law / negation law |
| 对偶式 | dual |
| 析取范式 / 合取范式 | disjunctive / conjunctive normal form |
| 功能完备 | functionally complete |
| 可满足性问题 | satisfiability problem (SAT) |
| NP-完全 | NP-complete |
| 谓词 / 命题函数 | predicate / propositional function |
| 论域 | domain (universe) of discourse |
| 自由变量 / 约束变量 | free variable / bound variable |
| 全称量词 | universal quantifier |
| 存在量词 | existential quantifier |
| 唯一量词 | uniqueness quantifier |
| 受限论域 | restricted domain |
| 嵌套量词 | nested quantifiers |
| 论证 / 前提 / 结论 | argument / premise / conclusion |
| 有效论证 | valid argument |
| 论证形式 | argument form |
| 假言推理 | modus ponens |
| 拒取式 | modus tollens |
| 假言三段论 | hypothetical syllogism |
| 析取三段论 | disjunctive syllogism |
| 附加 / 化简 | addition / simplification |
| 合取（规则） | conjunction |
| 消解 | resolution |
| 全称实例化 / 全称推广 | universal instantiation / generalization |
| 存在实例化 / 存在推广 | existential instantiation / generalization |
| 谬误 | fallacy |
| 肯定后件 / 否定前件 | affirming the conclusion / denying the hypothesis |
| 循环论证 | circular reasoning (begging the question) |
| 定理 / 命题 / 引理 / 推论 | theorem / proposition / lemma / corollary |
| 猜想 / 公理 / 证明 | conjecture / axiom / proof |
| 直接证明 | direct proof |
| 逆否证明 | proof by contraposition |
| 空证明 / 平凡证明 | vacuous proof / trivial proof |
| 反证法 | proof by contradiction |
| 等价性证明 | proof of equivalence |
| 反例 | counterexample |
| 穷举证明 / 分情况证明 | exhaustive proof / proof by cases |
| 不失一般性 | without loss of generality (WLOG) |
| 存在性证明 | existence proof |
| 构造性 / 非构造性 | constructive / nonconstructive |
| 见证 | witness |
| 唯一性证明 | uniqueness proof |
| 染色论证 | coloring argument |
| 多米诺骨牌 | domino |
| 开放问题 | open problem |

## C2 基本结构

| 中文 | English |
|---|---|
| 集合 / 元素 | set / element |
| 列举法 / 描述法 | roster method / set builder notation |
| 空集 / 全集 | empty (null) set / universal set |
| 文氏图 | Venn diagram |
| 子集 / 真子集 | subset / proper subset |
| 集合相等 | set equality |
| 基数 | cardinality |
| 幂集 | power set |
| 笛卡尔积 | Cartesian product |
| 真值集 | truth set |
| 罗素悖论 | Russell's paradox |
| 并集 / 交集 / 差集 | union / intersection / difference |
| 补集 / 对称差 | complement / symmetric difference |
| 容斥原理 | inclusion–exclusion |
| 隶属表 | membership table |
| 多重集 / 模糊集 | multiset / fuzzy set |
| 函数 | function |
| 定义域 / 陪域 / 值域 | domain / codomain / range |
| 像 / 原像 | image / preimage |
| 单射 | injective (one-to-one) |
| 满射 | surjective (onto) |
| 双射 / 一一对应 | bijective / one-to-one correspondence |
| 反函数 | inverse function |
| 恒等函数 | identity function |
| 复合函数 | composition |
| 下取整 / 上取整 | floor / ceiling function |
| 阶乘 | factorial |
| 部分函数 | partial function |
| 序列 | sequence |
| 等差数列 / 等比数列 | arithmetic / geometric progression |
| 字符串 / 空串 | string / empty string |
| 递推关系 / 初始条件 | recurrence relation / initial conditions |
| 迭代法 | iteration |
| 求和 / 求积 | summation / product |
| 几何级数 | geometric series |
| 可数集 / 不可数集 | countable / uncountable set |
| 阿列夫零 | aleph null |
| 康托尔对角线法 | Cantor diagonalization |
| 施罗德–伯恩斯坦定理 | Schröder–Bernstein theorem |
| 连续统假设 | continuum hypothesis |
| 不可计算函数 | uncomputable function |
| 矩阵 / 转置 | matrix / transpose |
| 对称矩阵 / 单位矩阵 | symmetric / identity matrix |
| 零一矩阵 | zero–one matrix |
| 并 / 交 / 布尔积 | join / meet / Boolean product |

## C6 计数

| 中文 | English |
|---|---|
| 组合数学 / 枚举 | combinatorics / enumeration |
| 乘法原理 | product rule |
| 求和原理 | sum rule |
| 减法原理 | subtraction rule |
| 除法原理 | division rule |
| 树形图 | tree diagram |
| 鸽巢原理 / 抽屉原理 | pigeonhole principle / Dirichlet drawer principle |
| 广义鸽巢原理 | generalized pigeonhole principle |
| 拉姆齐理论 | Ramsey theory |
| 单调子序列 | monotonic subsequence |
| 排列 / $r$-排列 | permutation / $r$-permutation |
| 组合 / $r$-组合 | combination / $r$-combination |
| 允许重复 | repetition allowed |
| 二项式系数 | binomial coefficient |
| 二项式定理 | binomial theorem |
| 帕斯卡三角形 / 帕斯卡恒等式 | Pascal's triangle / Pascal's identity |
| 范德蒙德恒等式 | Vandermonde's identity |
| 组合证明 / 双计数 | combinatorial proof / double counting |
| 星条法 | stars and bars |
| 可区分 / 不可区分 | distinguishable / indistinguishable |
| 无标号盒子 | unlabeled boxes |
| 第二类斯特林数 | Stirling number of the second kind |
| 整数拆分 | partition of an integer |
| 词典序 | lexicographic order |
| 下一个排列 / 下一个位串 | next permutation / next bit string |

## C8 高级计数

| 中文 | English |
|---|---|
| 递推关系 / 初始条件 / 解 | recurrence relation / initial conditions / solution |
| 斐波那契数 | Fibonacci numbers |
| 汉诺塔 | Tower of Hanoi |
| 码字 | codeword |
| 完全加括号 | parenthesization |
| 卡特兰数 | Catalan numbers |
| 相容（区间） | compatible |
| 权重 / 前驱 | weight / predecessor |
| 最优子结构 | optimal substructure |
| 重叠子问题 | overlapping subproblems |
| 动态规划 / 记忆化 / 填表 | dynamic programming / memoization / tabulation |
| 特征方程 | characteristic equation |
| 分治 | divide-and-conquer |
| 主定理 | Master Theorem |
| 生成函数 | generating function |
| 错排 | derangement |

## C9 关系

| 中文 | English |
|---|---|
| 二元关系 | binary relation |
| 自反 / 非自反 | reflexive / irreflexive |
| 对称 / 非对称 / 反对称 | symmetric / asymmetric / antisymmetric |
| 传递 | transitive |
| 复合 / 幂 | composite / powers |
| 逆关系 | inverse relation |
| $n$ 元关系 / 度 | $n$-ary relation / degree |
| 主键 / 复合键 | primary key / composite key |
| 外延 / 内涵 | extension / intension |
| 选择 / 投影 / 连接 | selection / projection / join |
| 零一矩阵 | zero–one matrix |
| 有向图 / 自环 | directed graph / loop |
| 闭包 | closure |
| 自反闭包 / 对称闭包 / 传递闭包 | reflexive / symmetric / transitive closure |
| 路径 / 回路 | path / circuit |
| 连通性关系 | connectivity relation |
| Warshall 算法 | Warshall's algorithm |
| 等价关系 / 等价类 | equivalence relation / equivalence class |
| 代表元 | representative |
| 划分 | partition |
| 同余类 | congruence class |
| 偏序 / 偏序集 | partial ordering / poset |
| 可比 / 不可比 | comparable / incomparable |
| 全序 / 链 | total (linear) ordering / chain |
| 良序集 | well-ordered set |
| 字典序 | lexicographic order |
| Hasse 图 / 覆盖关系 | Hasse diagram / covering relation |
| 极大元 / 极小元 | maximal / minimal element |
| 最大元 / 最小元 | greatest / least element |
| 上界 / 下界 | upper / lower bound |
| 最小上界 / 最大下界 | least upper bound / greatest lower bound |
| 格 | lattice |
| 分配格 / 有界格 / 补格 | distributive / bounded / complemented lattice |
| 对偶原理 | principle of duality |
| 拓扑排序 / 相容全序 | topological sort / compatible total ordering |

## C10 图

| 中文 | English |
|---|---|
| 图 / 顶点 / 边 | graph / vertex (node) / edge |
| 端点 / 关联 | endpoint / incident |
| 自环 / 重边 / 重数 | loop / multiple edges / multiplicity |
| 简单图 / 多重图 / 伪图 | simple graph / multigraph / pseudograph |
| 有向图 / 弧 / 混合图 | directed graph / arc / mixed graph |
| 邻接 / 邻域 / 度 | adjacent / neighborhood / degree |
| 悬挂点 / 孤立点 | pendant / isolated vertex |
| 正则图 | regular graph |
| 握手定理 | handshaking theorem |
| 入度 / 出度 | in-degree / out-degree |
| 底层无向图 | underlying undirected graph |
| 完全图 / 圈 / 轮 / 立方体 | complete graph / cycle / wheel / cube |
| 二分图 / 二分划分 / 完全二分图 | bipartite graph / bipartition / $K_{m,n}$ |
| 匹配 / 最大匹配 / 完全匹配 | matching / maximum matching / complete matching |
| Hall 婚姻定理 | Hall's marriage theorem |
| 子图 / 诱导子图 / 生成子图 | subgraph / induced / spanning subgraph |
| 收缩 / 补图 | contraction / complement |
| 度序列 / 图形序列 | degree sequence / graphical sequence |
| 邻接表 / 邻接矩阵 / 关联矩阵 | adjacency list / adjacency matrix / incidence matrix |
| 稀疏 / 稠密 | sparse / dense |
| 同构 / 不变量 | isomorphism / invariant |
| 路径 / 简单路径 / 回路 | path / simple path / circuit |
| 连通 / 连通分量 | connected / connected component |
| 割点 / 桥 | cut vertex / bridge |
| 点连通度 / 边连通度 | vertex / edge connectivity |
| $k$-连通 | $k$-connected |
| 强连通 / 弱连通 | strongly / weakly connected |
| 距离 / 离心率 / 直径 / 半径 | distance / eccentricity / diameter / radius |
| 欧拉回路 / 欧拉路径 | Euler circuit / Euler path |
| Fleury 算法 / Hierholzer 算法 | Fleury's / Hierholzer's algorithm |
| 哈密顿回路 / 哈密顿路径 | Hamilton circuit / Hamilton path |
| Dirac 定理 / Ore 定理 | Dirac's theorem / Ore's theorem |
| Gray 码 / 旋转编码 | Gray code / rotary encoder |
| 带权图 / 最短路 | weighted graph / shortest path |
| Dijkstra 算法 / Floyd 算法 | Dijkstra's / Floyd's algorithm |
| 旅行商问题 / 近似比 | traveling salesperson problem / approximation ratio |
| 平面图 / 平面表示 / 面 | planar graph / planar representation / region |
| 面的度 | degree of a region |
| 欧拉公式 | Euler's formula |
| 细分 / 同胚 | subdivision / homeomorphic |
| Kuratowski 定理 | Kuratowski's theorem |
| 对偶图 / 交叉数 | dual graph / crossing number |
| 着色 / 真着色 / 色数 | coloring / proper coloring / chromatic number |
| 四色定理 | four color theorem |
| 冲突图 | conflict graph |
| 边色数 | edge chromatic number |
| 独立集 / 独立数 | independent set / independence number |
| 支配集 | dominating set |

## 补充术语（拓展节新增）

| 中文 | English |
|---|---|
| 半加器 / 全加器 / 行波进位加法器 | half adder / full adder / ripple-carry adder |
| 文字 / 极小项 / 极大项 | literal / minterm / maxterm |
| 析取范式 / 合取范式 | disjunctive / conjunctive normal form (DNF / CNF) |
| 功能完备 | functionally complete |
| 霍尔三元组 / 最弱前置条件 | Hoare triple / weakest precondition |
| 公理化集合论 / 理发师悖论 | axiomatic set theory / barber paradox |
| 有限集 / 无限集 | finite / infinite set |
| 多重集 / 重数 / 隶属度 | multiset / multiplicity / degree of membership |
| 全函数 / 部分函数 / 提升 | total / partial function / lifting |
| 差分表 / 哑变量 | difference table / dummy variable |
| 等势 / 希尔伯特大饭店 | equinumerous / Hilbert's Grand Hotel |
| 康托尔定理 | Cantor's theorem |
| 数乘 / 斜对称矩阵 / 布尔幂 | scalar multiplication / skew-symmetric matrix / Boolean power |
| 特征方程 / 特解 | characteristic equation / particular solution |
| 主定理 / 递归树 | Master Theorem / recursion tree |
| 移位 / 卷积 | shifting / convolution |
| 广义二项式定理 | generalized binomial theorem |
| 错排 | derangement |
| 埃拉托色尼筛 | Sieve of Eratosthenes |
| 相容全序 / 卡恩算法 | compatible total ordering / Kahn's algorithm |
| 自同构 / 反向图 | automorphism / converse digraph |
| 内部不相交路径 / 强连通定向 | internally disjoint paths / strong orientation |
| 松弛 / 近似比 | relaxation / approximation ratio |
| 对偶图 / 交叉数 / 厚度 / 亏格 | dual graph / crossing number / thickness / genus |
| 团 / 团数 | clique / clique number |
| 边着色 / $k$-重着色 | edge coloring / $k$-tuple coloring |