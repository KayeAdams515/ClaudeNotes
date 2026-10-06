---
title: "C1 期中模拟卷 Mock Midterm"
course: 离散数学 Discrete Mathematics
chapter: "1 基础：逻辑与证明 The Foundations: Logic and Proofs"
type: 模拟卷
tags:
  - 离散数学
  - 期中复习
  - 模拟卷
created: 2026-09-23
---

# C1 期中模拟卷 Mock Midterm

> [!abstract] 使用说明
> - **命题方式**：按老师的说法，所有题目都以 Rosen §1.1–§1.7 的**例题 / 课后习题为蓝本改编**（换情境、换数字、换结构，**不是原题**）；每题答案里标注了“改编自”哪道题，做错可以回去翻原题。
> - **题型**：全部为解答题 (free-response)，英文命题。
> - **范围**：§1.1–§1.7。§1.8 课上没讲，不出题。
> - **分值**：共 140 分，**比真实期中长，是有意为之**，覆盖面优先。建议限时 150 分钟，闭卷做完再展开答案。
> - 重点照顾老师点名的五类：**tautology 定义**、**有限论域展开**、**直接证明**、**自然语言 ↔ 量词翻译**（含“恰好一个”）、**等价律推导**。

> [!warning] 答题规范（老师强调过三次，直接影响得分）
> 1. 推导题**每一步右侧写规则名或规则公式**（记不住名字写公式也给分）。
> 2. 结论是复合表达式时，要推出**整个表达式**，不能只推出各个分量。
> 3. $\mathbf T/\mathbf F$ 不能当变量用，做代换请用 $A,B$ 或 $S,R$；$\equiv$ 和 $\Leftrightarrow$ 全卷统一用一种。
> 4. 运算优先级按课件：$\neg\ >\ \wedge\ >\ \vee,\oplus\ >\ \to\ >\ \leftrightarrow$（同级从左到右）。

---

## Part I　Propositional Logic（§1.1–§1.3）

### Question 1 (8 points) — Definitions

(a) Define each of the following terms: **tautology**, **contradiction**, **contingency**.

(b) Classify each compound proposition as a tautology, a contradiction, or a contingency. Justify briefly.
　(i) $(p \to q) \vee (q \to p)$　　(ii) $(p \leftrightarrow q) \wedge (p \oplus q)$　　(iii) $(p \vee q) \to (p \wedge q)$

(c) Define what it means for two compound propositions $A$ and $B$ to be **logically equivalent**, and state how this relates to $A \leftrightarrow B$.

(d) Prove that if $A$ is a contradiction, then $\neg A$ is a tautology.

> [!success]- Solution（改编自 §1.3 定义、Ex 60）
> **(a)**
> - A **tautology** is a compound proposition that is **true for every** assignment of truth values to its propositional variables.
> - A **contradiction** is a compound proposition that is **false for every** assignment of truth values.
> - A **contingency** is a compound proposition that is neither a tautology nor a contradiction.
>
> **(b)**
> - (i) **Tautology.** If $q$ is T, then $p\to q$ is T. If $q$ is F, then $q\to p$ is T. Either way, the disjunction is T.
> - (ii) **Contradiction.** $p\leftrightarrow q$ is T exactly when $p,q$ have the same value, and $p\oplus q$ is T exactly when they differ. The two can never both be true.
> - (iii) **Contingency.** $p=q=\mathrm T$ gives $\mathrm T\to\mathrm T=\mathrm T$, while $p=\mathrm T, q=\mathrm F$ gives $\mathrm T\to\mathrm F=\mathrm F$.
>
> **(c)** $A$ and $B$ are logically equivalent, written $A\equiv B$, if they have the same truth value under **every** assignment. Equivalently, $A\equiv B$ **iff $A\leftrightarrow B$ is a tautology**.
>
> **(d)** Let $A$ be a contradiction. Then under every assignment $A$ is F, so $\neg A$ is T under every assignment. By definition, $\neg A$ is a tautology. $\blacksquare$
>
> 注：去年期末真题“什么是 tautology”有人没答上来。定义里的关键词是“**every** assignment / 所有真值赋值”，这个词不能漏。

---

### Question 2 (10 points) — Translation

Let
　$p$: "Li passes the midterm exam."
　$q$: "Li submits all four homework assignments."
　$r$: "Li gets an A in Discrete Mathematics."

(a) Write each sentence using $p, q, r$ and logical connectives.
　(i) Li gets an A, but he does not submit all four homework assignments.
　(ii) For Li to get an A, it is necessary that he passes the midterm.
　(iii) Passing the midterm and submitting all homework is sufficient for Li to get an A.
　(iv) Li gets an A if and only if he either passes the midterm or submits all homework.
　(v) Li does not get an A unless he passes the midterm.
　(vi) Li gets an A only if he passes the midterm and submits all homework.

(b) Express $(p \to r) \wedge \neg q$ as an English sentence.

(c) Consider the statement "The library closes early whenever there is a typhoon warning."
　Rewrite it in the form "if $p$, then $q$", then state its **converse**, **contrapositive**, and **inverse**.

(d) Rewrite each statement in the form "if $p$, then $q$":
　(i) You can enter the lab only if you wear safety goggles.
　(ii) The server will crash unless the patch is installed.

> [!success]- Solution（改编自 §1.1 Ex 14、22–24、27）
> **(a)**
> - (i) $r \wedge \neg q$（“but” 就是 $\wedge$）
> - (ii) $r \to p$（“necessary” 表示必要条件，必要条件放在箭头右边）
> - (iii) $(p \wedge q) \to r$
> - (iv) $r \leftrightarrow (p \vee q)$
> - (v) $\neg p \to \neg r$, or equivalently $r \to p$（“$\neg r$ unless $p$” 就是 “if $\neg p$ then $\neg r$”）
> - (vi) $r \to (p \wedge q)$（“only if” 后面跟的是结论）
>
> **(b)** "If Li passes the midterm exam, then he gets an A in Discrete Mathematics, and Li does not submit all four homework assignments."
>
> **(c)** Original: *If there is a typhoon warning, then the library closes early.*
> - **Converse**: If the library closes early, then there is a typhoon warning.
> - **Contrapositive**: If the library does not close early, then there is no typhoon warning.
> - **Inverse**: If there is no typhoon warning, then the library does not close early.
>
> 注：“whenever” 后面接的是条件；原命题只和逆否命题等价。
>
> **(d)**
> - (i) If you can enter the lab, then you wear safety goggles.
> - (ii) If the patch is not installed, then the server will crash.

---

### Question 3 (10 points) — Precedence and Truth Tables

(a) Using the precedence $\neg > \wedge > \vee, \oplus > \to > \leftrightarrow$, fully parenthesize
$$\neg p \vee q \wedge r \to p \oplus \neg r \leftrightarrow q$$

(b) Construct a truth table for $(p \oplus q) \to (p \wedge \neg q)$.

(c) Construct a truth table for $(p \to r) \wedge (\neg p \to q)$. Show all intermediate columns.

(d) How many rows are in the truth table of $(p \to \neg s) \vee (q \leftrightarrow t) \wedge (\neg r \oplus p)$?

> [!success]- Solution（改编自 §1.1 课件优先级练习、Ex 30、33、37）
> **(a)** 按优先级逐级加括号：先 $\neg$，再 $\wedge$，再 $\vee/\oplus$，再 $\to$，最外层 $\leftrightarrow$。
> $$\Big(\big((\neg p) \vee (q \wedge r)\big) \to \big(p \oplus (\neg r)\big)\Big) \leftrightarrow q$$
>
> **(b)**
>
> | $p$ | $q$ | $p\oplus q$ | $\neg q$ | $p\wedge\neg q$ | $(p\oplus q)\to(p\wedge\neg q)$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | F | F | F | **T** |
> | T | F | T | T | T | **T** |
> | F | T | T | F | F | **F** |
> | F | F | F | T | F | **T** |
>
> **(c)**
>
> | $p$ | $q$ | $r$ | $\neg p$ | $p\to r$ | $\neg p\to q$ | $(p\to r)\wedge(\neg p\to q)$ |
> |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | T | T | T | F | T | T | **T** |
> | T | T | F | F | F | T | **F** |
> | T | F | T | F | T | T | **T** |
> | T | F | F | F | F | T | **F** |
> | F | T | T | T | T | T | **T** |
> | F | T | F | T | T | T | **T** |
> | F | F | T | T | T | F | **F** |
> | F | F | F | T | T | F | **F** |
>
> 可以用来自查的规律：$p$ 为 T 时结果等于 $r$，$p$ 为 F 时结果等于 $q$。
>
> **(d)** The variables are $p, q, r, s, t$, which gives 5 variables and $2^5 = \mathbf{32}$ rows.

---

### Question 4 (8 points) — Applications

(a) Are these system specifications consistent? Explain.
> "The server is online if and only if the database is running. If the database is running, then the backup service is active. The backup service is not active or the system is in maintenance mode. If the system is in maintenance mode, then the server is not online. The system is not in maintenance mode."

(b) On the island of knights (always tell the truth) and knaves (always lie), you meet $A$ and $B$.
　$A$ says: "Exactly one of us is a knight."
　$B$ says: "$A$ is a knight."
　Determine what $A$ and $B$ are.

> [!success]- Solution（改编自 §1.2 Ex 9、Ex 19–23）
> **(a)** Let $s$: server online, $d$: database running, $b$: backup active, $m$: maintenance mode.
> Specifications: $s\leftrightarrow d,\ \ d\to b,\ \ \neg b\vee m,\ \ m\to\neg s,\ \ \neg m$.
> - $\neg m$ must be true, so $m=\mathrm F$.
> - Then $\neg b\vee m$ forces $b=\mathrm F$.
> - $d\to b$ with $b=\mathrm F$ forces $d=\mathrm F$.
> - $s\leftrightarrow d$ forces $s=\mathrm F$.
> - Check $m\to\neg s$: $\mathrm F\to\mathrm T=\mathrm T$ ✓.
>
> The assignment $s=d=b=m=\mathrm F$ makes all five true, so the specifications are **consistent**.
> 注：原题最后一句是“若 not online 则 maintenance”，那样就不一致。这里改成了反方向，结论也跟着变了。
>
> **(b)** Suppose $A$ is a knight. Then exactly one of them is a knight, so $B$ is a knave. But $B$'s statement "$A$ is a knight" would then be true, and a knave cannot say something true. Contradiction, so **$A$ is a knave**.
> Then "$A$ is a knight" is false. If $B$ were a knight, $B$ would be saying something false, which is impossible. So **$B$ is a knave**.
> Check: there are zero knights, so $A$'s statement "exactly one of us is a knight" is false, which is consistent with $A$ lying ✓.
> **Both are knaves.**

---

### Question 5 (14 points) — Logical Equivalences（推导题，每步写依据）

(a) Show that $\neg\big(q \vee (\neg q \wedge \neg p)\big) \equiv \neg q \wedge p$ without truth tables.

(b) Show that $p \to (\neg q \to r) \equiv \neg r \to (\neg p \vee q)$.

(c) Show that $\big[(p \vee q) \wedge \neg q\big] \to p$ is a tautology without truth tables.

(d) Show that $(p \wedge q) \to r \equiv p \to (q \to r)$.

(e) Show that $(p \vee q) \to r$ and $p \vee (q \to r)$ are **not** logically equivalent.

(f) Determine whether each compound proposition is satisfiable.
　(i) $(p \vee q) \wedge (\neg p \vee q) \wedge (p \vee \neg q)$
　(ii) $(p \vee q) \wedge (\neg p \vee q) \wedge (p \vee \neg q) \wedge (\neg p \vee \neg q)$
　(iii) $(p \leftrightarrow \neg q) \wedge (q \leftrightarrow \neg r) \wedge (r \leftrightarrow \neg p)$

> [!success]- Solution（改编自 §1.3 例 7、例 8、Ex 10–12、26、31、61）
> **(a)**
> $$\begin{aligned}
> \neg\big(q \vee (\neg q \wedge \neg p)\big)
> &\equiv \neg q \wedge \neg(\neg q \wedge \neg p) && \text{De Morgan's law}\\
> &\equiv \neg q \wedge \big(\neg\neg q \vee \neg\neg p\big) && \text{De Morgan's law}\\
> &\equiv \neg q \wedge (q \vee p) && \text{double negation law}\\
> &\equiv (\neg q \wedge q) \vee (\neg q \wedge p) && \text{distributive law}\\
> &\equiv \mathbf F \vee (\neg q \wedge p) && \text{negation law } (q\wedge\neg q\equiv\mathbf F)\\
> &\equiv (\neg q \wedge p) \vee \mathbf F && \text{commutative law}\\
> &\equiv \neg q \wedge p && \text{identity law}
> \end{aligned}$$
>
> **(b)**
> $$\begin{aligned}
> p \to (\neg q \to r)
> &\equiv \neg p \vee (\neg q \to r) && p\to q\equiv\neg p\vee q\\
> &\equiv \neg p \vee (\neg\neg q \vee r) && p\to q\equiv\neg p\vee q\\
> &\equiv \neg p \vee (q \vee r) && \text{double negation law}\\
> &\equiv (\neg p \vee q) \vee r && \text{associative law}\\
> &\equiv r \vee (\neg p \vee q) && \text{commutative law}\\
> &\equiv \neg\neg r \vee (\neg p \vee q) && \text{double negation law}\\
> &\equiv \neg r \to (\neg p \vee q) && p\to q\equiv\neg p\vee q
> \end{aligned}$$
>
> **(c)** Let $A$ denote $p\vee q$（用 $A$ 代换，不要用 $T$）.
> $$\begin{aligned}
> \big[(p \vee q) \wedge \neg q\big] \to p
> &\equiv \neg\big[(p \vee q) \wedge \neg q\big] \vee p && p\to q\equiv\neg p\vee q\\
> &\equiv \big(\neg(p \vee q) \vee \neg\neg q\big) \vee p && \text{De Morgan's law}\\
> &\equiv \big(\neg(p \vee q) \vee q\big) \vee p && \text{double negation law}\\
> &\equiv \neg(p \vee q) \vee (q \vee p) && \text{associative law}\\
> &\equiv \neg(p \vee q) \vee (p \vee q) && \text{commutative law}\\
> &\equiv \neg A \vee A \equiv \mathbf T && \text{negation law (with commutative law)}
> \end{aligned}$$
> Therefore it is a tautology.
>
> **(d)**
> $$\begin{aligned}
> (p \wedge q) \to r
> &\equiv \neg(p \wedge q) \vee r && p\to q\equiv\neg p\vee q\\
> &\equiv (\neg p \vee \neg q) \vee r && \text{De Morgan's law}\\
> &\equiv \neg p \vee (\neg q \vee r) && \text{associative law}\\
> &\equiv \neg p \vee (q \to r) && p\to q\equiv\neg p\vee q\\
> &\equiv p \to (q \to r) && p\to q\equiv\neg p\vee q
> \end{aligned}$$
>
> **(e)** Take $p=\mathrm T,\ q=\mathrm T,\ r=\mathrm F$:
> - $(p\vee q)\to r = \mathrm T\to\mathrm F = \mathrm F$
> - $p\vee(q\to r) = \mathrm T\vee \mathrm F = \mathrm T$
>
> The two sides differ under this assignment, so they are not logically equivalent.
> 注：证“不等价”只需要**一组**赋值，但必须把两边的值都算出来写清楚。
>
> **(f)**
> - (i) **Satisfiable**: with $p=q=\mathrm T$, all three clauses are T.
> - (ii) **Unsatisfiable**:
>   $(p\vee q)\wedge(\neg p\vee q)\equiv (q\vee p)\wedge(q\vee\neg p)\equiv q\vee(p\wedge\neg p)\equiv q\vee\mathbf F\equiv q$ (commutative, distributive, negation, identity).
>   In the same way, $(p\vee\neg q)\wedge(\neg p\vee\neg q)\equiv\neg q$.
>   The whole formula is therefore $\equiv q\wedge\neg q\equiv\mathbf F$.
> - (iii) **Unsatisfiable**: the three biconditionals force $p=\neg q$, $q=\neg r$ and $r=\neg p$. From the first two, $p=\neg\neg r=r$. The third says $r=\neg p$, so $p=\neg p$, which is impossible.

---

## Part II　Predicates and Quantifiers（§1.4–§1.5）

### Question 6 (8 points) — Finite Domains

(a) Let the domain of $x$ be $\{0,1\}$ and the domain of $y$ be $\{1,2,3\}$. Write out, using only $\wedge,\vee,\neg$:
　(i) $\forall x\,\exists y\,P(x,y)$　(ii) $\exists y\,\forall x\,P(x,y)$　(iii) $\neg\forall x\,\exists y\,P(x,y)$, with negations only in front of $P$

(b) Now let $P(x,y)$ be "$x + y = 3$". Find the truth values of (i) and (ii) in (a).

(c) Let the domain be $\{-1,0,1\}$. Write $\exists!x\,Q(x)$ using only $\wedge,\vee,\neg$. Then find its truth value when
　(i) $Q(x)$: "$x^2 = x$"　(ii) $Q(x)$: "$x + 1 = 0$"

> [!success]- Solution（改编自 §1.5 Ex 29 = 老师点名的往年期末题、§1.4 Ex 54）
> **(a)**
> - (i) $\big(P(0,1)\vee P(0,2)\vee P(0,3)\big)\wedge\big(P(1,1)\vee P(1,2)\vee P(1,3)\big)$
> - (ii) $\big(P(0,1)\wedge P(1,1)\big)\vee\big(P(0,2)\wedge P(1,2)\big)\vee\big(P(0,3)\wedge P(1,3)\big)$
> - (iii) First move the negation inside: $\neg\forall x\exists yP\equiv\exists x\forall y\neg P(x,y)$. Expanded:
> $\big(\neg P(0,1)\wedge\neg P(0,2)\wedge\neg P(0,3)\big)\vee\big(\neg P(1,1)\wedge\neg P(1,2)\wedge\neg P(1,3)\big)$
>
> 口诀：$\forall$ 展开成 $\wedge$，$\exists$ 展开成 $\vee$；**外层量词决定最外层的联结词**。
>
> **(b)**
> - (i) **True**: for $x=0$ take $y=3$, and for $x=1$ take $y=2$.
> - (ii) **False**: a fixed $y$ cannot satisfy both $0+y=3$ and $1+y=3$.
>
> 这就是“$\forall x\exists y$ 中的 $y$ 可以随 $x$ 变，$\exists y\forall x$ 中的 $y$ 不能变”。
>
> **(c)** The expansion is
> $$\big(Q(-1)\wedge\neg Q(0)\wedge\neg Q(1)\big)\vee\big(\neg Q(-1)\wedge Q(0)\wedge\neg Q(1)\big)\vee\big(\neg Q(-1)\wedge\neg Q(0)\wedge Q(1)\big)$$
> - (i) $Q(0)$ and $Q(1)$ are both true, so every disjunct contains a false conjunct. The statement is **False**.
> - (ii) Only $Q(-1)$ is true, so the first disjunct is true. The statement is **True**.

---

### Question 7 (14 points) — English → Logic

(a) Let $B(x)$, $S(x)$, $M(x)$ mean "$x$ has a bicycle / a scooter / a motorcycle". The domain is the students in your class.
　(i) Some student has a bicycle and a scooter but not a motorcycle.
　(ii) Every student has a bicycle, a scooter, or a motorcycle.
　(iii) No student has all three.
　(iv) For each of the three vehicles, some student in the class has one.

(b) Translate each sentence **in two ways**: first with the domain = students in your class, then with the domain = all people. Use $C(x)$: "$x$ is in your class".
　(i) Everyone in your class has used Python.
　(ii) Someone in your class has never been to Beijing.
　(iii) No one in your class has failed a math course.

(c) Let $H(x,y)$ be "$x$ has helped $y$". The domain is all students in the college.
　(i) Everybody has helped somebody.
　(ii) There is someone whom everybody has helped.
　(iii) No one has helped everybody.
　(iv) Nobody has helped both Alice and Bob.
　(v) Alice has helped exactly one person.
　(vi) There is exactly one person whom everybody has helped.
　(vii) Bob has helped exactly two people.
　(viii) Someone has helped everyone except himself or herself.

(d) Use quantifiers, predicates, and mathematical operators. The domain is all real numbers.
　(i) The average of two negative real numbers is negative.
　(ii) Every nonzero real number has exactly one multiplicative inverse.
　(iii) There is a real number that has no real square root.
　(iv) The product of two real numbers is not necessarily greater than both of them.

> [!success]- Solution（改编自 §1.4 Ex 10、23；§1.5 Ex 9–10、19–23）
> **(a)**
> - (i) $\exists x\big(B(x)\wedge S(x)\wedge\neg M(x)\big)$
> - (ii) $\forall x\big(B(x)\vee S(x)\vee M(x)\big)$
> - (iii) $\neg\exists x\big(B(x)\wedge S(x)\wedge M(x)\big)$, equivalently $\forall x\big(\neg B(x)\vee\neg S(x)\vee\neg M(x)\big)$
> - (iv) $\exists x\,B(x)\wedge\exists x\,S(x)\wedge\exists x\,M(x)$（三个不同的学生也可以，所以要写成三个独立的 $\exists$）
>
> **(b)** Let $P(x)$: "$x$ has used Python", $J(x)$: "$x$ has been to Beijing", $F(x)$: "$x$ has failed a math course".
>
> | | Domain = class | Domain = all people |
> |---|---|---|
> | (i) | $\forall x\,P(x)$ | $\forall x\big(C(x)\to P(x)\big)$ |
> | (ii) | $\exists x\,\neg J(x)$ | $\exists x\big(C(x)\wedge\neg J(x)\big)$ |
> | (iii) | $\neg\exists x\,F(x)$ | $\neg\exists x\big(C(x)\wedge F(x)\big)\equiv\forall x\big(C(x)\to\neg F(x)\big)$ |
>
> ⚠️ 铁律：**$\forall$ 配 $\to$，$\exists$ 配 $\wedge$**。
> - $\forall x(C(x)\wedge P(x))$ 的意思是“所有人都在班里且用过 Python”，是错的。
> - $\exists x(C(x)\to\neg J(x))$ 只要有一个人不在班里就为真，也是错的。
>
> **(c)**
> - (i) $\forall x\,\exists y\,H(x,y)$
> - (ii) $\exists y\,\forall x\,H(x,y)$
> - (iii) $\neg\exists x\,\forall y\,H(x,y)\ \equiv\ \forall x\,\exists y\,\neg H(x,y)$
> - (iv) $\neg\exists x\big(H(x,\text{Alice})\wedge H(x,\text{Bob})\big)$
> - (v) $\exists y\Big(H(\text{Alice},y)\wedge\forall z\big(H(\text{Alice},z)\to z=y\big)\Big)$
> - (vi) $\exists y\Big(\forall x\,H(x,y)\wedge\forall z\big(\forall x\,H(x,z)\to z=y\big)\Big)$
> - (vii) $\exists y\,\exists z\Big(y\neq z\wedge H(\text{Bob},y)\wedge H(\text{Bob},z)\wedge\forall w\big(H(\text{Bob},w)\to(w=y\vee w=z)\big)\Big)$
> - (viii) $\exists x\,\forall y\big(H(x,y)\leftrightarrow y\neq x\big)$
>
> (viii) 如果只理解成“帮过所有别人”，写 $\exists x\,\forall y\big(y\neq x\to H(x,y)\big)$ 一般也能拿分。严格的 “except” 还要求没帮过自己，所以用 $\leftrightarrow$。
>
> “恰好一个”的模板：**存在性**用 $\exists$ 写出来，**唯一性**用 $\forall z(\cdots\to z=y)$ 把其他的排除掉。(vi) 里被 $\forall z$ 排除的对象是“被所有人帮过的人”，所以条件部分是整句 $\forall x\,H(x,z)$。
>
> **(d)**
> - (i) $\forall x\,\forall y\Big(\big(x<0\wedge y<0\big)\to\dfrac{x+y}{2}<0\Big)$
> - (ii) $\forall x\Big(x\neq0\to\exists y\big(xy=1\wedge\forall z(xz=1\to z=y)\big)\Big)$
> - (iii) $\exists x\,\forall y\,(y^2\neq x)$
> - (iv) $\neg\forall x\,\forall y\big(xy>x\wedge xy>y\big)$, equivalently $\exists x\,\exists y\big(xy\le x\vee xy\le y\big)$
>
> “not necessarily” 就是“并非总是”，写成 $\neg\forall$。

---

### Question 8 (6 points) — Logic → English

(a) Let $S(x)$: "$x$ is a student", $D(x)$: "$x$ drinks coffee". The domain is all people. Translate:
　(i) $\forall x\big(S(x)\to D(x)\big)$　(ii) $\forall x\big(S(x)\wedge D(x)\big)$　(iii) $\exists x\big(S(x)\to D(x)\big)$　(iv) $\exists x\big(S(x)\wedge D(x)\big)$

(b) The domain is all real numbers. Translate each into an English sentence that expresses a mathematical fact:
　(i) $\forall x\,\exists y\,(x + y = 0)$
　(ii) $\forall x\,\forall y\big((x>0\wedge y>0)\to xy>0\big)$
　(iii) $\forall x\,\forall y\big(x<y\to\exists z\,(x<z\wedge z<y)\big)$

> [!success]- Solution（改编自 §1.4 Ex 7；§1.5 Ex 24–25）
> **(a)**
> - (i) Every student drinks coffee.
> - (ii) Everyone is a student and drinks coffee.
> - (iii) There is a person who, if he or she is a student, drinks coffee. This is automatically true as soon as there is any non-student, so it is almost never what is meant.
> - (iv) Some student drinks coffee.
>
> **(b)**
> - (i) Every real number has an additive inverse.
> - (ii) The product of two positive real numbers is positive.
> - (iii) Between any two distinct real numbers there is another real number.

---

### Question 9 (10 points) — Negation

(a) Express each statement with quantifiers. Then form its negation so that **no negation is to the left of a quantifier**, and express the negation in simple English. Do not simply write "It is not the case that…".
　(i) All cats like fish.
　(ii) There is a student who can solve every problem on the exam.
　(iii) No robot can feel pain.
　(iv) There is a bird that can swim but cannot fly.

(b) Rewrite each formula so that negation symbols appear only immediately before predicates.
　(i) $\neg\exists x\,\forall y\,\exists z\,P(x,y,z)$
　(ii) $\neg\forall x\big(\exists y\,P(x,y)\wedge\forall z\,Q(x,z)\big)$
　(iii) $\neg\exists x\,\forall y\big(P(x,y)\to Q(x,y)\big)$
　(iv) $\neg\forall x\,\exists y\big(P(x,y)\leftrightarrow Q(x,y)\big)$

(c) Let $R(x,y)$ mean "student $x$ has read book $y$". The domain of $x$ is the students in this class and the domain of $y$ is the books on the reading list. Express "**Every student in this class has read exactly one book on the reading list**" with quantifiers, negate it (no negation left of a quantifier), and state the negation in English.

> [!success]- Solution（改编自 §1.4 Ex 32–34；§1.5 Ex 30–31、36–38）
> **(a)**
> - (i) With $C(x)$: cat and $F(x)$: likes fish, the statement is $\forall x\big(C(x)\to F(x)\big)$.
>   Negation: $\exists x\big(C(x)\wedge\neg F(x)\big)$, "Some cat does not like fish."
> - (ii) With $S(x,y)$: student $x$ can solve problem $y$, the statement is $\exists x\,\forall y\,S(x,y)$.
>   Negation: $\forall x\,\exists y\,\neg S(x,y)$, "Every student fails to solve at least one problem."
> - (iii) The statement is $\neg\exists x\big(R(x)\wedge P(x)\big)\equiv\forall x\big(R(x)\to\neg P(x)\big)$.
>   Negation: $\exists x\big(R(x)\wedge P(x)\big)$, "Some robot can feel pain."
> - (iv) The statement is $\exists x\big(B(x)\wedge S(x)\wedge\neg F(x)\big)$.
>   Negation: $\forall x\big(B(x)\to(\neg S(x)\vee F(x))\big)$, "Every bird either cannot swim or can fly."
>
> 注：(i) 否定后 $\to$ 变成 $\wedge$，这是因为 $\neg(C\to F)\equiv C\wedge\neg F$，不是只翻转量词就行。
>
> **(b)**（规则：量词从左到右逐个翻转，$\neg$ 一路推到谓词前；遇到联结词用德摩根律或 $\neg(p\to q)\equiv p\wedge\neg q$）
> - (i) $\forall x\,\exists y\,\forall z\,\neg P(x,y,z)$
> - (ii) $\exists x\big(\forall y\,\neg P(x,y)\vee\exists z\,\neg Q(x,z)\big)$
> - (iii) $\forall x\,\exists y\big(P(x,y)\wedge\neg Q(x,y)\big)$
> - (iv) $\exists x\,\forall y\big(P(x,y)\leftrightarrow\neg Q(x,y)\big)$（用了 $\neg(p\leftrightarrow q)\equiv p\leftrightarrow\neg q$）
>
> **(c)** The statement is
> $$\forall x\,\exists y\Big(R(x,y)\wedge\forall z\big(R(x,z)\to z=y\big)\Big)$$
> Its negation, pushed inward, is
> $$\exists x\,\forall y\Big(\neg R(x,y)\vee\exists z\big(R(x,z)\wedge z\neq y\big)\Big)$$
> In English: **Some student in this class has read either none of the books on the list or at least two of them.**

---

### Question 10 (10 points) — Truth Values

Determine the truth value of each statement. Justify each answer with a witness or a counterexample.

(a) The domain is all real numbers.
　(i) $\forall x\,\exists y\,(y^3 = x)$
　(ii) $\exists y\,\forall x\,(x^2 > y)$
　(iii) $\forall x\big(x \neq 1 \to \exists y\,(y(x-1) = 1)\big)$
　(iv) $\exists x\,\exists y\,(x + y = 3 \wedge 2x + 2y = 7)$
　(v) $\forall x\,\exists y\,(x - y = 1 \wedge x + y = 3)$

(b) The domain is all integers.
　(i) $\exists n\,\forall m\,(n \le m^2)$
　(ii) $\forall n\,\exists m\,(n = 2m)$
　(iii) $\exists! n\,(n^2 = 4)$
　(iv) $\exists! n\,(2n + 1 = 7)$

(c) Determine the truth value of $\forall x\,\exists y\,(x + y = 0)$ when the domain of both variables is
　(i) the integers　(ii) the positive integers　(iii) the nonnegative integers

> [!success]- Solution（改编自 §1.5 Ex 27–28、45；§1.4 Ex 52）
> **(a)**
> - (i) **T**: take $y=\sqrt[3]{x}$, since every real number has a real cube root.
> - (ii) **T**: take $y=-1$. Then $x^2\ge0>-1$ for every $x$.
> - (iii) **T**: take $y=\dfrac{1}{x-1}$, which is defined because $x\neq1$.
> - (iv) **F**: if $x+y=3$, then $2x+2y=6\neq7$.
> - (v) **F**: the system forces $x=2,\ y=1$. For $x=0$ no $y$ works.
>
> **(b)**
> - (i) **T**: take $n=0$ (or any negative $n$), since $m^2\ge0$.
> - (ii) **F**: counterexample $n=1$, which is odd.
> - (iii) **F**: both $n=2$ and $n=-2$ work, so the solution is not unique.
> - (iv) **T**: $n=3$ is the only solution.
>
> **(c)**
> - (i) **T**: take $y=-x$.
> - (ii) **F**: for $x=1$, $y=-1$ is not a positive integer.
> - (iii) **F**: for $x=1$, no nonnegative $y$ gives $1+y=0$.
>
> 同一个式子，论域一换真值就变，所以**判断真值前先看清论域**。

---

### Question 11 (6 points) — Quantifier Equivalences

(a) Show that $\exists x\big(P(x)\to Q(x)\big)\equiv\forall x\,P(x)\to\exists x\,Q(x)$. Justify each step.

(b) Show that $\exists x\big(P(x)\to Q(x)\big)$ and $\exists x\,P(x)\to\exists x\,Q(x)$ are **not** logically equivalent.

(c) Show that $\forall x\big(P(x)\vee Q(x)\big)$ and $\forall x\,P(x)\vee\forall x\,Q(x)$ are not logically equivalent.

> [!success]- Solution（改编自 §1.4 Ex 43–45、49–51）
> **(a)**
> $$\begin{aligned}
> \exists x\big(P(x)\to Q(x)\big)
> &\equiv \exists x\big(\neg P(x)\vee Q(x)\big) && p\to q\equiv\neg p\vee q\\
> &\equiv \exists x\,\neg P(x)\vee\exists x\,Q(x) && \exists \text{ distributes over } \vee\\
> &\equiv \neg\forall x\,P(x)\vee\exists x\,Q(x) && \text{De Morgan's law for quantifiers}\\
> &\equiv \forall x\,P(x)\to\exists x\,Q(x) && p\to q\equiv\neg p\vee q
> \end{aligned}$$
>
> **(b)** Let the domain be $\{1,2\}$, $P(x)$: "$x=1$", and $Q(x)$: "$x=3$", so $Q$ is always false.
> - $\exists x(P(x)\to Q(x))$: at $x=2$, $P(2)\to Q(2)$ is $\mathrm F\to\mathrm F=\mathrm T$, so the statement is **T**.
> - $\exists x P(x)\to\exists x Q(x)$: this is $\mathrm T\to\mathrm F$, so the statement is **F**.
>
> The truth values differ, so the two are not equivalent. 由 (a) 可知，正确的等价式里左边是 $\forall x P(x)$，不是 $\exists x P(x)$。
>
> **(c)** Let the domain be the integers, $P(x)$: "$x\ge0$", and $Q(x)$: "$x<0$".
> - $\forall x(P(x)\vee Q(x))$ is **T**, because every integer is either $\ge0$ or $<0$.
> - $\forall x P(x)$ is F (take $x=-1$) and $\forall x Q(x)$ is F (take $x=1$), so the disjunction is **F**.
>
> 记住：$\forall$ 对 $\wedge$ 可以分配，对 $\vee$ 不能分配；$\exists$ 对 $\vee$ 可以分配，对 $\wedge$ 不能分配。

---

## Part III　Rules of Inference（§1.6）

### Question 12 (16 points)

(a) Translate the argument into propositional logic, then use rules of inference to show that the conclusion follows. **Name the rule used at each step.**
> "If it is not windy or it is not raining, then the football match will be played and the fireworks show will go ahead. If the football match is played, then the stadium lights will be on. The stadium lights are not on. Therefore, it is windy."

(b) Show that the premises $p\to(q\wedge r)$, $(q\vee s)\to t$, and $\neg t\vee u$ imply the conclusion $p\to u$.

(c) Use **resolution** to show that the premises "It is not snowing or the bus is late", "The bus is not late or I walk to school", and "It is snowing or I walk to school" imply the conclusion "I walk to school".

(d) Translate the argument using predicates and quantifiers, then prove it with rules of inference.
> "Some student in this class passed the quiz but did not attend the review session. Every student who passed the quiz either attended the review session or studied the textbook. Everyone who studied the textbook understands De Morgan's laws. Therefore, some student who passed the quiz understands De Morgan's laws."

(e) For each argument, determine whether it is valid. If it is valid, name the rule. If it is not, name the fallacy.
　(i) If a number is divisible by 6, then it is divisible by 3. 21 is divisible by 3. Therefore, 21 is divisible by 6.
　(ii) If a number is divisible by 6, then it is divisible by 3. 14 is not divisible by 3. Therefore, 14 is not divisible by 6.
　(iii) If a number is divisible by 6, then it is divisible by 3. 15 is not divisible by 6. Therefore, 15 is not divisible by 3.

(f) Find the error in this "proof" that $\forall x\,\exists y\,L(x,y)$ implies $\exists y\,\forall x\,L(x,y)$:

| Step | Statement | Reason |
|:-:|---|---|
| 1 | $\forall x\,\exists y\,L(x,y)$ | Premise |
| 2 | $\exists y\,L(c,y)$ | Universal instantiation from (1) |
| 3 | $L(c,d)$ | Existential instantiation from (2) |
| 4 | $\forall x\,L(x,d)$ | Universal generalization from (3) |
| 5 | $\exists y\,\forall x\,L(x,y)$ | Existential generalization from (4) |

> [!success]- Solution（改编自 §1.6 Ex 6、12、29–31、19、23，例 6 / 例 12）
> **(a)** Let $w$: windy, $r$: raining, $m$: match played, $f$: fireworks go ahead, $l$: lights on.
> Premises: $(\neg w\vee\neg r)\to(m\wedge f)$, $m\to l$, $\neg l$. Conclusion: $w$.
>
> | Step | Statement | Reason |
> |:-:|---|---|
> | 1 | $\neg l$ | Premise |
> | 2 | $m\to l$ | Premise |
> | 3 | $\neg m$ | Modus tollens (1)(2) |
> | 4 | $\neg m\vee\neg f$ | Addition (3) |
> | 5 | $\neg(m\wedge f)$ | De Morgan's law (4) |
> | 6 | $(\neg w\vee\neg r)\to(m\wedge f)$ | Premise |
> | 7 | $\neg(\neg w\vee\neg r)$ | Modus tollens (5)(6) |
> | 8 | $\neg\neg w\wedge\neg\neg r$ | De Morgan's law (7) |
> | 9 | $w\wedge r$ | Double negation law (8) |
> | 10 | $w$ | Simplification (9) |
>
> **(b)**（结论是复合式 $p\to u$，要把**整个** $p\to u$ 推出来）
>
> | Step | Statement | Reason |
> |:-:|---|---|
> | 1 | $p\to(q\wedge r)$ | Premise |
> | 2 | $(p\to q)\wedge(p\to r)$ | (1), $p\to(q\wedge r)\equiv(p\to q)\wedge(p\to r)$ |
> | 3 | $p\to q$ | Simplification (2) |
> | 4 | $(q\vee s)\to t$ | Premise |
> | 5 | $\neg(q\vee s)\vee t$ | (4), $p\to q\equiv\neg p\vee q$ |
> | 6 | $(\neg q\wedge\neg s)\vee t$ | De Morgan's law (5) |
> | 7 | $t\vee(\neg q\wedge\neg s)$ | Commutative law (6) |
> | 8 | $(t\vee\neg q)\wedge(t\vee\neg s)$ | Distributive law (7) |
> | 9 | $t\vee\neg q$ | Simplification (8) |
> | 10 | $q\to t$ | (9), commutative law and $p\to q\equiv\neg p\vee q$ |
> | 11 | $p\to t$ | Hypothetical syllogism (3)(10) |
> | 12 | $\neg t\vee u$ | Premise |
> | 13 | $t\to u$ | (12), $p\to q\equiv\neg p\vee q$ |
> | 14 | $p\to u$ | Hypothetical syllogism (11)(13) |
>
> 另一种做法（教材 Ex 11 的方法）：把 $p$ 当作附加前提推出 $u$，由此得到 $p\to u$。用这种方法时，最后一行要**明确写出**“由此 $p\to u$ 成立”。
>
> **(c)** Let $s$: snowing, $b$: bus late, $w$: I walk.
>
> | Step | Statement | Reason |
> |:-:|---|---|
> | 1 | $\neg s\vee b$ | Premise |
> | 2 | $\neg b\vee w$ | Premise |
> | 3 | $\neg s\vee w$ | Resolution (1)(2) |
> | 4 | $s\vee w$ | Premise |
> | 5 | $w\vee w$ | Resolution (3)(4) |
> | 6 | $w$ | Idempotent law (5) |
>
> **(d)** Domain: students in this class. Let $P(x)$: passed the quiz, $A(x)$: attended the review session, $T(x)$: studied the textbook, $D(x)$: understands De Morgan's laws.
> Premises: $\exists x\big(P(x)\wedge\neg A(x)\big)$, $\forall x\big(P(x)\to(A(x)\vee T(x))\big)$, $\forall x\big(T(x)\to D(x)\big)$.
> Conclusion: $\exists x\big(P(x)\wedge D(x)\big)$.
>
> | Step | Statement | Reason |
> |:-:|---|---|
> | 1 | $\exists x\big(P(x)\wedge\neg A(x)\big)$ | Premise |
> | 2 | $P(c)\wedge\neg A(c)$ | Existential instantiation (1), $c$ is a new element |
> | 3 | $P(c)$ | Simplification (2) |
> | 4 | $\neg A(c)$ | Simplification (2) |
> | 5 | $\forall x\big(P(x)\to(A(x)\vee T(x))\big)$ | Premise |
> | 6 | $P(c)\to(A(c)\vee T(c))$ | Universal instantiation (5) |
> | 7 | $A(c)\vee T(c)$ | Modus ponens (3)(6) |
> | 8 | $T(c)$ | Disjunctive syllogism (4)(7) |
> | 9 | $\forall x\big(T(x)\to D(x)\big)$ | Premise |
> | 10 | $T(c)\to D(c)$ | Universal instantiation (9) |
> | 11 | $D(c)$ | Modus ponens (8)(10) |
> | 12 | $P(c)\wedge D(c)$ | Conjunction (3)(11) |
> | 13 | $\exists x\big(P(x)\wedge D(x)\big)$ | Existential generalization (12) |
>
> ⚠️ **先做存在实例化，再做全称实例化**。$c$ 必须是存在实例化引入的那个特定元素，全称式可以实例化到任何元素，所以后做。
>
> **(e)**
> - (i) **Invalid**: this is the fallacy of **affirming the conclusion**. 21 is divisible by 3 but not by 6.
> - (ii) **Valid**: this is **modus tollens**.
> - (iii) **Invalid**: this is the fallacy of **denying the hypothesis**. 15 is divisible by 3.
>
> **(f)** **Step 4 is wrong.** Universal generalization requires $c$ to be an **arbitrary** element. In step 3, $d$ was chosen by existential instantiation, so $d$ depends on $c$. The statement $L(c,d)$ therefore does not hold for an arbitrary $c$ with the same $d$, and we cannot generalize to $\forall x\,L(x,d)$.
> Counterexample: in the integers with $L(x,y)$: "$x+y=0$", the premise $\forall x\exists y\,L(x,y)$ is true, but $\exists y\forall x\,L(x,y)$ is false.

---

## Part IV　Proofs（§1.7）

### Question 13 (20 points)

(a) **Direct proof.**
　(i) Prove that if $n$ is an odd integer, then $n^3$ is odd.
　(ii) Prove that every multiple of 4 is the difference of two squares of integers.

(b) Let $n$ be an integer. Prove that if $5n + 3$ is even, then $n$ is odd, using
　(i) a proof by contraposition;　(ii) a proof by contradiction.

(c) Prove by contraposition: if $x, y$ are real numbers with $x + y \ge 10$, then $x \ge 5$ or $y \ge 5$.

(d) **Proof by contradiction.**
　(i) Prove that the difference of an irrational number and a rational number is irrational.
　(ii) Prove that $\sqrt[3]{2}$ is irrational.
　(iii) Prove that there is no rational number $r$ with $r^3 + r^2 + 1 = 0$.

(e) Let $P(n)$ be "If $n$ is a positive integer greater than 2, then $n^2 > 2n$," and let $Q(n)$ be "If $a$ and $b$ are positive real numbers with $a > b$, then $a^n \ge b^n$." Prove $P(1)$ and $Q(0)$. What kind of proof did you use in each case?

(f) Prove that for every integer $n$, $n$ is odd **if and only if** $3n + 5$ is even.

(g) Show that these three statements about an integer $x$ are equivalent: (i) $x^2$ is odd; (ii) $x + 7$ is even; (iii) $5x - 2$ is odd.

(h) Prove or disprove: the sum of two irrational numbers is irrational.

(i) Find a counterexample to: "For every positive integer $n$, $n^2 + n + 11$ is prime."

(j) What is wrong with this reasoning for solving $\sqrt{2x+3} = x$?
　(1) $\sqrt{2x+3}=x$ is given; (2) $2x+3=x^2$, by squaring both sides; (3) $x^2-2x-3=0$; (4) $(x-3)(x+1)=0$; (5) so $x=3$ or $x=-1$.

> [!success]- Solution（改编自 §1.7 例 1、例 7–8、例 10；Ex 1–9、15、17–20、25–27、31、35、38–42）
> **(a)(i)**（和老师点名的上学期期末题同一个模板）Assume $n$ is odd. Then $n=2k+1$ for some integer $k$, and
> $$n^3=(2k+1)^3=8k^3+12k^2+6k+1=2(4k^3+6k^2+3k)+1.$$
> Since $4k^3+6k^2+3k$ is an integer, $n^3$ is odd. $\blacksquare$
> 得分点：① 写出奇数的定义 $n=2k+1$；② 化成 $2(\cdot)+1$ 的形式；③ **明确指出括号里是整数**。
>
> **(a)(ii)** Let $n$ be a multiple of 4, so $n=4k$ for some integer $k$. Then $(k+1)^2-(k-1)^2=(k^2+2k+1)-(k^2-2k+1)=4k=n$. Since $k+1$ and $k-1$ are integers, $n$ is a difference of two squares. $\blacksquare$
>
> **(b)(i) Contraposition.** We prove "if $n$ is even, then $5n+3$ is odd". Let $n=2k$. Then $5n+3=10k+3=2(5k+1)+1$, which is odd because $5k+1$ is an integer. Therefore, if $5n+3$ is even, $n$ is odd. $\blacksquare$
>
> **(b)(ii) Contradiction.** Suppose $5n+3$ is even and $n$ is **not** odd, so $n=2k$. Then $5n+3=2(5k+1)+1$ is odd. So $5n+3$ is both even and odd, which is a contradiction. Hence $n$ is odd. $\blacksquare$
>
> 逆否法和反证法的计算完全一样，**开头的假设不同**：逆否法只假设 $\neg q$；反证法同时假设 $p$ 和 $\neg q$，最后推出矛盾。
>
> **(c)** The contrapositive is: if **not** ($x\ge5$ or $y\ge5$), then $x+y<10$. By De Morgan's law, the hypothesis is $x<5$ **and** $y<5$. Adding the two inequalities gives $x+y<10$, which is the negation of $x+y\ge10$. $\blacksquare$
>
> **(d)(i)** Let $x$ be irrational and $r=\frac ab$ be rational ($a,b$ integers, $b\neq0$). Suppose, for contradiction, that $x-r=\frac cd$ is rational ($c,d$ integers, $d\neq0$). Then
> $$x=\frac cd+\frac ab=\frac{cb+ad}{db},$$
> with $cb+ad$ and $db$ integers and $db\neq0$. So $x$ is rational, contradicting the assumption that $x$ is irrational. $\blacksquare$
>
> **(d)(ii)** Suppose, for contradiction, that $\sqrt[3]{2}=\frac ab$, where $a,b$ are integers, $b\neq0$, and the fraction is **in lowest terms**.
> - Cubing gives $a^3=2b^3$, so $a^3$ is even.
> - If $a$ were odd, $a^3$ would be odd. So $a$ is even; write $a=2c$.
> - Then $8c^3=2b^3$, so $b^3=4c^3$ is even, and in the same way $b$ is even.
> - Now $a$ and $b$ share the factor 2, which contradicts lowest terms. Hence $\sqrt[3]{2}$ is irrational. $\blacksquare$
>
> 这题和 $\sqrt2$ 的证明是同一个骨架：最简分数 → 代入 → 奇偶性 → 与最简矛盾。
>
> **(d)(iii)** Suppose $r=\frac ab$ is a root in lowest terms. Multiplying by $b^3$ gives $a^3+a^2b+b^3=0$. Since the fraction is in lowest terms, $a$ and $b$ are not both even. Consider the three cases:
> - $a,b$ both odd: odd + odd + odd = odd $\neq0$.
> - $a$ odd, $b$ even: odd + even + even = odd $\neq0$.
> - $a$ even, $b$ odd: even + even + odd = odd $\neq0$.
>
> In every case the left side is odd, so it cannot equal 0. This is a contradiction, so no rational root exists. $\blacksquare$
>
> **(e)**
> - $P(1)$: "If 1 is a positive integer greater than 2, then $1^2>2$." The hypothesis "1 > 2" is false, so the conditional is true. This is a **vacuous proof**.
> - $Q(0)$: "If $a>b>0$, then $a^0\ge b^0$." The conclusion $1\ge1$ is always true, so the conditional is true. This is a **trivial proof**.
>
> **(f)**
> - ($\Rightarrow$, direct) Let $n=2k+1$. Then $3n+5=6k+8=2(3k+4)$, which is even.
> - ($\Leftarrow$, contraposition) Suppose $n$ is even, $n=2k$. Then $3n+5=6k+5=2(3k+2)+1$, which is odd. So if $3n+5$ is even, $n$ is odd.
>
> Both directions hold, so $n$ is odd $\leftrightarrow$ $3n+5$ is even. $\blacksquare$（**两个方向都要写**）
>
> **(g)** Prove the cycle (i) → (ii) → (iii) → (i).
> - (i)→(ii): First, $x^2$ odd implies $x$ odd. By contraposition: if $x=2k$, then $x^2=2(2k^2)$ is even. So $x=2k+1$ and $x+7=2k+8=2(k+4)$, which is even.
> - (ii)→(iii): $x+7=2m$ gives $x=2m-7$. Then $5x-2=10m-37=2(5m-19)+1$, which is odd.
> - (iii)→(i): First, $5x-2$ odd implies $x$ odd. By contraposition: if $x=2k$, then $5x-2=2(5k-1)$ is even. So $x=2k+1$ and $x^2=4k^2+4k+1=2(2k^2+2k)+1$, which is odd. $\blacksquare$
>
> 循环蕴涵只需要证 3 个条件句，两两互证需要 6 个。
>
> **(h)** **False.** Counterexample: $\sqrt2$ and $-\sqrt2$ are both irrational, but $\sqrt2+(-\sqrt2)=0$ is rational.
> We still need to check that $-\sqrt2$ is irrational. If $-\sqrt2=\frac ab$, then $\sqrt2=\frac{-a}{b}$ would be rational, which is a contradiction. 反例本身也要验证，这是得分点。
>
> **(i)** For $n=10$: $10^2+10+11=121=11^2$, which is not prime. ($n=11$ also works: $11\cdot13=143$.)
>
> **(j)** Step (2) is not reversible. Squaring shows that every solution of (1) satisfies (2), but a solution of (2) need not satisfy (1). Checking $x=-1$ in the original equation gives $\sqrt{1}=1\neq-1$, so $-1$ is an **extraneous root**. The only solution is $x=3$, since $\sqrt9=3$ ✓.

---

## 关联
- [[C1 复习提纲 Review Outline]] · [[C1 基础：逻辑与证明 MOC]] · [[C1 作业与错题]]
