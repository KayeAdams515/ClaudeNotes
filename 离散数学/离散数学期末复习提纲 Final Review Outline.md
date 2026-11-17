# 离散数学期末复习提纲（Discrete Mathematics Final Review Outline）

本提纲汇总期末复习所需的定义、定理条件、证明要点与手算步骤；例题直接说明对象、条件、方法与结论。

> [!info] 范围与考试提醒
> 本提纲仅保留当前复习范围内的内容。4.3“分组与相邻约束”的基础方法及4.5沿用现有范围安排。考试提醒区分“明确会考、老师强调、历年考过、期中预告”；参考资料和范围核对记录集中见第七部分。

## 考试信息与标记说明（Examination Information and Labels）

| 项目 | 已有课堂证据与复习动作 |
|---|---|
| 时间（time） | 第22节宣布11月19日8:50–10:50，时长120分钟；按本学期日历为2026年11月19日（周四）。转写后文把星期重复识别成Wednesday，不据此改日期。 |
| 地点（venue） | 第22节转写分别出现“53A 210”和“F3A210”，均指二楼210。楼名存在转写歧义，须以QQ群正式通知核对，不能把机器转写当作确定楼号。 |
| 范围（scope） | 第17节说明以期中后的第2、9、6、8、10章为主，第1章约保留一道题；第21节再次明确图论是期末重点。复习保留第1章，已删去此前标为“拓展”的补充内容。 |
| 形式与语言（format and language） | 闭卷（closed-book examination）；学院要求英文作答（answers in English），第18节又提醒要认得英文专业词。 |
| 题源（question sources） | 第1、12、13节反复强调教材例题（worked examples）、课后习题（exercises）及作业变形；“课堂没逐句讲过”不等于对应小节的教材细节不会出现。 |
| 推导依据（justification） | 第1–8节反复要求写明所用规则名称或公式；不能只给结果。证明题若指定方法（specified proof method），按指定方法完成。 |
| 手算（calculation by hand） | 第15节明确要求能逐元素手算Warshall；程序输出不能代替考试中的中间步骤。 |

正文标记：

- **【老师明确会考】** 为直接考试预告；

- **【老师强调】** 为课堂重点或较大出题可能性；

- **【历年考过】** 为过去试题；

- **【期中预告】** 只说明期中，不当作本次期末承诺；

- **【考试注意】** 为课堂明确要求；

- **【易错】** 为数学或作业中需自查的错误。

出处用“课次＋原笔记/转写”定位，详细索引在文末。原笔记自行写的“必考”“不考”若没有直接证据，不升级为老师承诺。

## 阅读导航（Navigation）

| 正文 | 快速入口 |
|---|---|
| [[#一、逻辑与证明（Logic and Proofs）\|一、逻辑与证明]] | 真值、翻译、等价、量词、推理与证明 |
| [[#二、集合、函数、序列与矩阵（Sets, Functions, Sequences and Matrices）\|二、基本结构]] | 集合、函数、序列与布尔矩阵 |
| [[#三、关系（Relations）\|三、关系]] | 六种性质、闭包、Warshall、等价类、偏序与格 |
| [[#四、计数（Counting）\|四、计数]] | 鸽巢、排列组合、恒等式、分配与后继算法 |
| [[#五、递推关系的应用（Applications of Recurrence Relations）\|五、递推]] | 初值、兔子、汉诺塔与受限位串 |
| [[#六、图论（Graph Theory）\|六、图论]] | 图类型、运算、同构、连通、树、欧拉／哈密顿、平面与着色 |

按考试证据确定先后时，可优先回看 **4.6生成算法、3.4手算Warshall、6.3图运算及整个第六部分** ；这只是复习时间分配建议，不缩小本提纲的知识范围。

> [!info]- 个人练习回看入口（更新至2026-11-17）
> [[前两轮练习总结与知识错题]]保留第1、2、9章的历史批改；[[第6章计数卷总结与知识错题]]整理另找的第6章计数卷及两题补交，实际作答现已覆盖第1、2、6、9章。正文保留复习范围内的个人知识错题与证明补充，均附英文题目和正确答案，并沿用原编号。计算、抄写、英文或符号笔误不作为个人知识错题；补交的Ramsey题已核验正确，冰球杆恒等式按思路正确、补充一般论证记录。完整历史批改仍可从上述入口回查。

---

## 一、逻辑与证明（Logic and Proofs）

### 1.1 命题、联结词与真值表（Propositions, Connectives and Truth Tables）

#### 命题与真值（Propositions and Truth Values）

- **命题（proposition）** 是能确定为真或假的陈述句；命令、问句及未确定变元的开放语句（open sentence）不是命题。

  命题变元（propositional variable）表示命题，真值（truth value）为T或F；不能判断真值不等于没有真值。

- **简单命题（atomic proposition）** 由逻辑联结词（logical connective）组成复合命题（compound proposition）。

  经典逻辑采用二值原则（principle of bivalence）；条件语句不自动表示因果关系（causality）。

| 名称 | 记号 | 为真的条件 |
|---|---|---|
| 否定（negation） | $\neg p$ | $p$假 |
| 合取（conjunction） | $p\land q$ | 两者都真；英文but在本课程通常按and处理 |
| 相容析取（inclusive disjunction） | $p\lor q$ | 至少一个真，可以同时真 |
| 异或／排斥或（exclusive or, XOR） | $p\oplus q$ | 恰有一个真 |
| 条件语句／蕴涵（conditional statement / implication） | $p\to q$ | 仅$p$真而$q$假时为假 |
| 双条件语句（biconditional statement） | $p\leftrightarrow q$ | 同真或同假 |

| $p$ | $q$ | $p\land q$ | $p\lor q$ | $p\oplus q$ | $p\to q$ | $p\leftrightarrow q$ |
|---|---|---|---|---|---|---|
| T | T | T | T | F | T | T |
| T | F | F | T | T | F | F |
| F | T | F | T | T | T | F |
| F | F | F | F | F | T | T |

#### 条件语句与英文表达（Conditionals and English Expressions）

- **前件／假设（antecedent / hypothesis）** 为$p$，后件／结论（consequent / conclusion）为$q$。

  $p$假时$p\to q$为空真（vacuously true），因为没有出现违反承诺的“真前件、假后件”。

  这种按真值定义的条件称实质蕴涵（material implication），不要求前后件之间具有因果联系。

- **充分条件（sufficient condition）** 在箭尾，必要条件（necessary condition）在箭头：`p if q`为$q\to p$，`p only if q`为$p\to q$；

  `p whenever q`、`p follows from q`均为$q\to p$。`A unless B`为$\neg B\to A\equiv A\lor B$；`cannot A unless B`为$A\to B$。

  `if and only if`缩写iff。

- “$p$对$q$充分但不必要（sufficient but not necessary）”应理解为$p\Rightarrow q$，反方向不普遍成立；

  “必要但不充分（necessary but not sufficient）”相反。不能只写一个蕴涵就把“but not”部分也视为已说明。

- **逆命题（converse）** $q\to p$；否命题（inverse）$\neg p\to\neg q$；逆否命题（contrapositive）$\neg q\to\neg p$。原命题与逆否等价，逆与否等价；其他配对一般不等价。

  条件的否定是$p\land\neg q$，不是否命题。

#### 真值表与运算顺序（Truth Tables and Precedence）

- **真值表（truth table）** 有$n$个不同命题变元时列$2^n$行，重复出现的同一变元不另计。先列变元，再按子式依赖逐列求值；多变元时等价变形通常比整表高效。

> [!warning] 【考试注意】课堂运算优先级（operator precedence）：
> $\neg$高于$\land$，高于同级的$\lor,\oplus$，高于$\to$，高于$\leftrightarrow$。同级混合及连续箭头应加括号；蕴涵不满足结合律（associativity）。
>
> $\equiv$是比较整个表达式的等价记号，不是再插入式中的普通联结词。

#### 检验条件与按位运算（Testing Conditionals and Bit Operations）

- **Wason选择任务（Wason selection task）** ：检验$p\to q$应翻查$p$和$\neg q$对应的卡；

  查$q$不能排除“另有原因”，查$\neg p$无法发现违例。饮酒—年龄、上网—收入、元音—偶数、圆形—黄色四题是同一结构。

- **位（bit）** 取0、1；位串（bit string）长度是位数。按位运算（bitwise operation）对等长串逐位AND、OR、XOR；

  $p\oplus q\equiv(p\lor q)\land\neg(p\land q)\equiv(p\land\neg q)\lor(\neg p\land q)$。可用OR = AND XOR XOR逐位自查。

> [!warning] 【易错】
> “今天不是周五”不能改成“今天是周一”；“至少32”之否定为“小于32”；不额外添加原句没有的信息。程序的if-then是控制流程（control flow），不等同于数学蕴涵的真值定义。

#### 命题逻辑的术语（Terminology of Propositional Logic）

- **命题逻辑／命题演算（propositional logic / propositional calculus）** 把完整陈述作原子；命题变元也称语句变元／布尔变量（statement / Boolean variable）。否定是一元运算符（unary operator），其余基本联结词为二元运算符（binary operator）；双条件也称双蕴涵（bi-implication）。

### 1.2 翻译、规约与逻辑谜题（Translation, Specifications and Logic Puzzles）

#### 翻译与一致性（Translation and Consistency）

- **自然语言翻译（translation）** ：先定义原子命题，再判断充分／必要／唯一等限制，最后定联结词与括号。不要把日常语境中暗含的双条件擅自加入只说“if”的数学题。

- **系统规约（system specification）** 是一组要求；一致性（consistency）指所有规约存在同一组满足赋值（satisfying assignment），不是每条分别可真。

  合取后找一组赋值即证一致；要证不一致（inconsistency），须推出矛盾或说明所有赋值均失败。加规约可能破坏一致性，删规约不能把一致系统变成不一致。

#### 骑士与无赖（Knights and Knaves）

- **骑士与无赖（knights and knaves）** ：骑士总说真话，无赖总说假话；也可分别称为Batman和Joker。设$K_A$为“A说真话”，发言内容为$S_A$，自洽条件为$K_A\leftrightarrow S_A$，对各人联立。

  例：A说“B是Batman”，B说“两人类型不同”。若A为真话者，则B也为真话者，却不能真的类型不同，矛盾；故A为Joker，B也为Joker，此时两句均假而自洽。一般题可有唯一解、多解或无解；“我是无赖”在固定两类规则下无解。

### 1.3 逻辑等价律（Logical Equivalence Laws）

#### 逻辑分类与基本等价律（Classification and Basic Equivalence Laws）

- **永真式（tautology）** 在所有赋值下真；矛盾式（contradiction）在所有赋值下假；可能式／偶然式（contingency）有真有假。

  逻辑等价（logical equivalence）$P\equiv Q$指所有赋值下真值相同，等价于$P\leftrightarrow Q$永真。

> [!info] 【历年考过】
> 老师曾以“什么是tautology”作为期末题，见C1汇总及§1.6课堂补充。

| 定律（law） | 全部基本形式 |
|---|---|
| 同一律（identity laws） | $p\land\mathbf T\equiv p$；$p\lor\mathbf F\equiv p$ |
| 支配律（domination laws） | $p\lor\mathbf T\equiv\mathbf T$；$p\land\mathbf F\equiv\mathbf F$ |
| 幂等律（idempotent laws） | $p\lor p\equiv p$；$p\land p\equiv p$ |
| 双重否定律（double negation law） | $\neg\neg p\equiv p$ |
| 交换律（commutative laws） | $p\lor q\equiv q\lor p$；$p\land q\equiv q\land p$ |
| 结合律（associative laws） | $(p\lor q)\lor r\equiv p\lor(q\lor r)$；合取同理 |
| 分配律（distributive laws） | $p\lor(q\land r)\equiv(p\lor q)\land(p\lor r)$；$p\land(q\lor r)\equiv(p\land q)\lor(p\land r)$ |
| 德摩根律（De Morgan's laws） | $\neg(p\land q)\equiv\neg p\lor\neg q$；$\neg(p\lor q)\equiv\neg p\land\neg q$ |
| 吸收律（absorption laws） | $p\lor(p\land q)\equiv p$；$p\land(p\lor q)\equiv p$ |
| 否定律（negation laws） | $p\lor\neg p\equiv\mathbf T$；$p\land\neg p\equiv\mathbf F$ |

- **广义德摩根律（generalized De Morgan's laws）** ：对$n\ge1$，

  $$\neg\bigwedge_{i=1}^np_i\equiv\bigvee_{i=1}^n\neg p_i,\qquad
  \neg\bigvee_{i=1}^np_i\equiv\bigwedge_{i=1}^n\neg p_i.$$

  证明要点：$n=2$为基本德摩根律；把前$n-1$项看成一个子式，再对剩余项应用二元德摩根律，递归展开即可。

> [!tip] 【老师强调】
> $p\to q\equiv\neg p\lor q$是箭头变换的核心；双条件先写成$(p\to q)\land(q\to p)$。其他式应会推，不把所有式子一律当作老师要求死记。

$$
\begin{aligned}
p\lor q&\equiv\neg p\to q,&p\land q&\equiv\neg(p\to\neg q),\\
\neg(p\to q)&\equiv p\land\neg q,&p\to q&\equiv\neg q\to\neg p,\\
(p\to q)\land(p\to r)&\equiv p\to(q\land r),\\
(p\to r)\land(q\to r)&\equiv(p\lor q)\to r,\\
(p\to q)\lor(p\to r)&\equiv p\to(q\lor r),\\
(p\to r)\lor(q\to r)&\equiv(p\land q)\to r,\\
p\leftrightarrow q&\equiv(\neg p\lor q)\land(\neg q\lor p)\\
&\equiv(p\land q)\lor(\neg p\land\neg q)\\
&\equiv\neg p\leftrightarrow\neg q,\\
\neg(p\leftrightarrow q)&\equiv p\leftrightarrow\neg q\equiv p\oplus q.
\end{aligned}
$$

#### 等价推导与书写要求（Derivation and Justification）

- **等价推导（equivalence derivation）** 通常“消箭头→否定内移→分配、吸收、幂等整理”。

  例：$(p\to r)\land(q\to r)\equiv(\neg p\lor r)\land(\neg q\lor r)\equiv(\neg p\land\neg q)\lor r\equiv\neg(p\lor q)\lor r\equiv(p\lor q)\to r$。各步依据依次是蕴涵等价、分配、德摩根、蕴涵等价。

> [!warning] 【考试注意】
> 第1–8节要求每步给规则名或公式；代换不要把T、F当作普通变元，以免与真值常量混淆；$\equiv$和$\Leftrightarrow$的等价记法在同一份答卷中保持一致。

> [!info] 【期中预告】
> 老师明确说过会有等价推导题，此预告针对期中。

- **替换原理与等价的传递性（substitution principle and transitivity of equivalence）** ：子式可替换为与其逻辑等价的公式而不改变整式真值；若$A\equiv B$、$B\equiv C$，则$A\equiv C$。因此等价推导中的每一行必须与上一行双向等价；仅成立单向蕴涵的化简不能直接接在$\equiv$链中。

### 1.4 谓词、论域与单层量词（Predicates, Domains and Quantifiers）

#### 谓词与量词的含义（Meaning of Predicates and Quantifiers）

- **谓词逻辑／谓词演算（predicate logic / predicate calculus）** 区分主语（subject）与谓语／性质（predicate），用量化描述整类对象。

- **谓词（predicate）** ／命题函数（propositional function）$P(x)$含变元，赋值或量化后才成为命题；

  $n$元谓词（$n$-ary predicate）有$n$个参数。

  论域（domain / universe of discourse）决定可取对象，同一式子在整数与实数上可能真假不同。

- **全称量词（universal quantifier）** $\forall xP(x)$要求所有对象满足；存在量词（existential quantifier）$\exists xP(x)$要求至少一个。

  有限域$\{a_1,\ldots,a_n\}$上分别展开为$\bigwedge_iP(a_i)$、$\bigvee_iP(a_i)$。证伪全称给反例（counterexample），证存在给见证；证无存在则证明所有对象都不满足。

#### 唯一性、论域与变量（Uniqueness, Domains and Variables）

- **唯一存在量词（uniqueness quantifier）** $\exists!xP(x)$展开为$\exists x(P(x)\land\forall y(P(y)\to y=x))$。仅写存在、仅写至多一个都不充分。

- **受限论域（restricted domain）** ：`Every A is B`为$\forall x(A(x)\to B(x))$；`Some A is B`为$\exists x(A(x)\land B(x))$；

  `No A is B`为$\forall x(A(x)\to\neg B(x))$；`Not every A is B`为$\exists x(A(x)\land\neg B(x))$。存在式写蕴涵会被不属于A的对象空真满足。

> [!warning]- 【个人知识错题 K02】动物个体与动物类别的论域不能混用
> **来源**：第一轮，第1章精选卷题组4，Rosen §1.6 Ex.9(f)；含后续“把is改成are”的讨论。
>
> **错点与标记**：把“某只动物具有性质”与“某一类动物全部具有性质”混用，改变了否定的含义。仅改is/are不能完成论域转换；本条记录历史概念错因，需通过重做确认已掌握。
>
> **原题（English）**：For this collection of premises, what relevant conclusion or conclusions can be drawn? Explain the rules of inference used to obtain each conclusion from the premises. “All rodents gnaw their food.” “Mice are rodents.” “Rabbits do not gnaw their food.” “Bats are not rodents.”
>
> **答案**：以动物个体为论域，令$R,G,M,H,B$分别表示“是啮齿动物、啃食、是老鼠、是兔子、是蝙蝠”。前提为$\forall x(R(x)\to G(x))$、$\forall x(M(x)\to R(x))$、$\forall x(H(x)\to\neg G(x))$、$\forall x(B(x)\to\neg R(x))$。由假言三段论得$\forall x(M(x)\to G(x))$；由逆否及兔子前提得$\forall x(H(x)\to\neg R(x))$。因此：**All mice gnaw their food. No rabbits are rodents.** 不能由“蝙蝠不是啮齿动物”断定蝙蝠是否啃食。
>
> **自查**：若把$P(X)$定义为“类别$X$中所有动物都是啮齿动物”，则$\neg P(X)$只是“并非全是”，不能解释成“这一类没有啮齿动物”。

- **作用域（scope）** 是量词管辖的子式；其中出现的同名变元为约束变元（bound variable），未被量词约束的为自由变元（free variable）。量词优先于普通联结词，但必须用括号明确范围；

  约束变量可一致改名（renaming bound variables），须防止变元捕获（variable capture）。

$$
\neg\forall xP(x)\equiv\exists x\neg P(x),\qquad
\neg\exists xP(x)\equiv\forall x\neg P(x).
$$

| 分配式（distribution） | 判断与原因 |
|---|---|
| $\forall x(P\land Q)\equiv(\forall xP)\land(\forall xQ)$ | 成立 |
| $\exists x(P\lor Q)\equiv(\exists xP)\lor(\exists xQ)$ | 成立 |
| $\forall x(P\lor Q)\equiv(\forall xP)\lor(\forall xQ)$ | 一般不成立：整数中“偶或奇”处处真，不能说全偶或全奇 |
| $\exists x(P\land Q)\equiv(\exists xP)\land(\exists xQ)$ | 一般不成立：某人会P、某人会Q，未必同一人两者都会 |

- **谓词公式的逻辑等价（logical equivalence of predicate formulas）** ：在同一非空论域上，对谓词符号的每一种解释（interpretation）及自由变量的每一种赋值（assignment），两公式真值始终相同，才称逻辑等价。某个特定论域、某个特定谓词下恰好同真，不足以建立一般等价律。

### 1.5 嵌套量词与精确数量（Nested Quantifiers and Exact Cardinalities）

#### 量词顺序与否定（Quantifier Order and Negation）

- **嵌套量词（nested quantifiers）** 逐层理解：$\forall x\exists yP(x,y)$中见证$y$可依赖$x$；

  $\exists y\forall xP(x,y)$要求固定一个$y$对所有$x$通用，后者蕴涵前者，反向一般不成立。同类量词可交换，异类量词不可随意交换。

  例如实数上$\forall x\exists y(x+y=0)$真，$\exists y\forall x(x+y=0)$假。

- **有限域嵌套展开（finite expansion）** ：$\forall x\exists yP(x,y)$按$x$合取、每项按$y$析取；不能把两层顺序颠倒。

> [!info] 【历年考过】
> 老师提到在$\{1,2,3\}$上展开此式曾作为期末题。

- 否定时逐层换$\forall/\exists$，最后否定谓词：$\neg\forall x\exists y\forall zP\equiv\exists x\forall y\exists z\neg P$。`every other`加$y\ne x$限制；

  `not necessarily`表示存在反例，不是处处相反。

> [!warning]- 【个人知识错题 K01】否定量词后还要正确否定蕴涵
> **来源**：第一轮，第1章精选卷题组3，Rosen §1.5 Ex.31(d)。
>
> **错点**：否定内移到$P\to Q$时未正确使用$\neg(P\to Q)\equiv P\land\neg Q$；这一步改变逻辑含义，属于知识性错误。
>
> **原题（English）**：Express the negation of $\forall x\exists y(P(x,y)\to Q(x,y))$ so that all negation symbols immediately precede predicates.
>
> **答案**：
> $$\neg\forall x\exists y(P(x,y)\to Q(x,y))\equiv\exists x\forall y\neg(P(x,y)\to Q(x,y))\equiv\boxed{\exists x\forall y(P(x,y)\land\neg Q(x,y))}.$$
> **自查**：量词经过否定时翻转，内层蕴涵被否定后变成“前件真且后件假”。

#### 恰好一个与恰好多个（Exactly One and Exact Counts）

- 令$L(x,y)$表示$x$爱$y$，以下区分施动者、对象、共同对象与唯一性质：

| 句意 | 正确形式 |
|---|---|
| Mary恰好爱一个人 | $\exists x(L(M,x)\land\forall z(L(M,z)\to z=x))$ |
| 恰好一个人爱Mary | $\exists x(L(x,M)\land\forall z(L(z,M)\to z=x))$ |
| 每个人恰好爱一个人 | $\forall y\exists x(L(y,x)\land\forall z(L(y,z)\to z=x))$ |
| 恰好一个人爱所有人 | $\exists x(\forall yL(x,y)\land\forall z((\forall wL(z,w))\to z=x))$ |
| 恰好一个人被所有人爱 | $\exists x(\forall yL(y,x)\land\forall z((\forall wL(w,z))\to z=x))$ |
| 恰好两人爱Mary | $\exists x\exists y(x\ne y\land L(x,M)\land L(y,M)\land\forall z(L(z,M)\to(z=x\lor z=y)))$ |

- 恰好$n$个（exactly $n$）：$n$个见证＋两两不等＋所有满足者均是这些见证之一。

  至多一个（at most one）为$\forall x\forall y((P(x)\land P(y))\to x=y)$，可没有满足者。

> [!info] 【期中预告】
> 老师明确说自然语言与量词翻译会出现在期中；期末仍应会做，但没有据此断言本次必考。

> [!warning] 【考试注意】
> 唯一性条件必须针对完整性质“爱所有人”，不能误写成“只要爱某个人就必须是他”。

- **朋友关系的量词表达（quantifying friendship）** ：令$F(x,y)$表示$x$与$y$是朋友。“存在一个人，他的任意两个不同朋友彼此都不是朋友”写为$\exists x\forall y\forall z((F(x,y)\land F(x,z)\land y\ne z)\to\neg F(y,z))$。内层只限制同时是$x$的朋友且互不相同的$y,z$；少于两个朋友时，该条件为空真。

#### 量词移动与依赖（Quantifier Movement and Dependence）

- 若$A$中无$x$自由出现，则$(\exists xP(x))\to A\equiv\forall x(P(x)\to A)$，$(\forall xP(x))\to A\equiv\exists x(P(x)\to A)$（后式按非空域）。量词从蕴涵前件移出会翻转；

  从后件移出不翻转，并须满足变量不自由出现及论域条件。

> [!warning] 【易错】
> 两式一般不等价；不能套用普通同类量词交换。

- **含独立命题的量词移动（moving quantifiers past an independent proposition）** ：假定论域非空，且$x$不自由出现在$A$中，下面八式均成立：

  | 联结词 | 全称量词（universal quantifier） | 存在量词（existential quantifier） |
  |---|---|---|
  | 合取（conjunction） | $\forall x(A\land P(x))\equiv A\land\forall xP(x)$ | $\exists x(A\land P(x))\equiv A\land\exists xP(x)$ |
  | 析取（disjunction） | $\forall x(A\lor P(x))\equiv A\lor\forall xP(x)$ | $\exists x(A\lor P(x))\equiv A\lor\exists xP(x)$ |
  | 量词在前件（quantifier in antecedent） | $(\forall xP(x))\to A\equiv\exists x(P(x)\to A)$ | $(\exists xP(x))\to A\equiv\forall x(P(x)\to A)$ |
  | 量词在后件（quantifier in consequent） | $A\to\forall xP(x)\equiv\forall x(A\to P(x))$ | $A\to\exists xP(x)\equiv\exists x(A\to P(x))$ |

  证明要点：先用$B\to C\equiv\neg B\lor C$消箭头，量词经过否定时翻转，再使用与独立命题的并交移动。量词位于蕴涵前件时翻转、位于后件时不翻转。若$x$自由出现在$A$里，不能照搬；空论域下也不能不加检查地照搬整张表。

### 1.6 推理规则与有效性（Rules of Inference and Validity）

#### 有效性与命题推理（Validity and Propositional Inference）

- **论证（argument）** 由前提（premises）及结论（conclusion）组成；有效性（validity）指不存在“所有前提真而结论假”的赋值，即$(P_1\land\cdots\land P_n)\to Q$永真。

  可靠／健全论证（sound argument）还要求前提实际为真。结论为真不保证推理有效，前提不全真也不自动使论证无效。

| 推理规则（rule of inference） | 从前提到结论 |
|---|---|
| 肯定前件式（modus ponens） | $p,p\to q\;\therefore q$ |
| 否定后件式（modus tollens） | $\neg q,p\to q\;\therefore\neg p$ |
| 假言三段论（hypothetical syllogism） | $p\to q,q\to r\;\therefore p\to r$ |
| 析取三段论（disjunctive syllogism） | $p\lor q,\neg p\;\therefore q$ |
| 附加律（addition） | $p\;\therefore p\lor q$ |
| 化简律（simplification） | $p\land q\;\therefore p$ |
| 合取律（conjunction） | $p,q\;\therefore p\land q$ |
| 归结（resolution） | $p\lor q,\neg p\lor r\;\therefore q\lor r$ |

#### 谬误与量化规则（Fallacies and Quantified Rules）

- **肯定后件谬误（fallacy of affirming the conclusion）** ：由$p\to q,q$误推$p$；

  否定前件谬误（fallacy of denying the hypothesis）：由$p\to q,\neg p$误推$\neg q$。给出真前提假结论的赋值即可否定论证。

| 量化规则（quantified inference rule） | 要求 |
|---|---|
| 全称实例化（universal instantiation, UI） | $\forall xP(x)\Rightarrow P(c)$，$c$为论域中对象 |
| 全称概括（universal generalization, UG） | 对任意对象$c$证明$P(c)$后得$\forall xP(x)$；$c$不能受特殊假设限制 |
| 存在实例化（existential instantiation, EI） | $\exists xP(x)$引入新的见证符号$c$并暂设$P(c)$；不能直接拿已受限制的对象替代 |
| 存在概括（existential generalization, EG） | $P(c)\Rightarrow\exists xP(x)$，$c$须为合法对象 |

#### 综合证明与作业错题（Combined Proofs and Homework Errors）

- 综合证明常先EI选见证，再UI把全称前提作用于该见证；不能从两个存在前提擅自选同一见证。全称肯定前件式（universal modus ponens）是UI＋MP的组合。

- **作业错题（homework error）** ：由$P(\text{Linda})$及$\forall x(P(x)\to Q(x))$依次写$P(\text{Linda})\to Q(\text{Linda})$（UI）、$Q(\text{Linda})$（MP）、$\exists xQ(x)$（EG）。

  不能在最后抄成$\exists xP(x)$。

> [!warning] 【考试注意】
> 最后必须得到题目要求的整个表达式，并给出最后组合／引入步骤；不能只列若干子结论。数学上若已证$\neg q$与$s$，当然可以经附加律和蕴涵等价推出$\neg q\to s$；
>
> 具体步骤：由$s$用附加律得$q\lor s$，再用蕴涵等价$q\lor s\equiv\neg q\to s$。这样才完成从已知子结论到目标表达式的推导。

- **综合量化证明的完整示例（worked quantified proof）** ：由$\exists x(C(x)\land\neg F(x))$和$\forall x(C(x)\to P(x))$，推出$\exists x(P(x)\land\neg F(x))$。

  | 步骤（step） | 依据（reason） |
  |---|---|
  | 1. $\exists x(C(x)\land\neg F(x))$ | 前提（premise） |
  | 2. $C(a)\land\neg F(a)$，$a$为新见证 | 由1存在实例化（EI） |
  | 3. $C(a)$ | 由2化简律（simplification） |
  | 4. $\forall x(C(x)\to P(x))$ | 前提（premise） |
  | 5. $C(a)\to P(a)$ | 由4全称实例化（UI） |
  | 6. $P(a)$ | 由3、5肯定前件式（MP） |
  | 7. $\neg F(a)$ | 由2化简律（simplification） |
  | 8. $P(a)\land\neg F(a)$ | 由6、7合取律（conjunction） |
  | 9. $\exists x(P(x)\land\neg F(x))$ | 由8存在概括（EG） |

  新见证$a$不能在证明结束后被当成任意对象全称概括；结论中的存在量词必须补回。

#### 归结（Resolution）

- **全称否定后件式（universal modus tollens）** ：由$\forall x(P(x)\to Q(x))$及$\neg Q(a)$，先UI得$P(a)\to Q(a)$，再MT得$\neg P(a)$。论证形式（argument form）用变元表达结构；肯定前件式也称分离律（law of detachment），归结产生的子句称归结式（resolvent）。

### 1.7 证明的基本方法（Basic Proof Methods）

#### 证明的语言与基础（Language and Foundations of Proof）

- **形式证明（formal proof）** 逐步遵循规则；非形式证明（informal proof）可合并显然步骤、使用已证结论，但仍必须给出有效理由。

  数学陈述常省略全称量词，证明时取“任意满足假设的对象”，不能只举几个例子。

#### 直接、逆否与反证（Direct Proof, Contraposition and Contradiction）

- **直接证明（direct proof）** ：从$p$出发，用定义与已知结论推出$q$。奇数（odd integer）$n=2k+1$，偶数（even integer）$n=2k$；

  有理数（rational number）$a/b$，$a,b\in\mathbb Z,b\ne0$；无理数（irrational number）是不属于$\mathbb Q$的实数。

> [!info] 【历年考过】奇数的平方为奇数：
> Let $n=2k+1$ for some integer $k$. Then $n^2=4k^2+4k+1=2(2k^2+2k)+1$, so $n^2$ is odd. 老师明确说过这是上学期期末的直接证明题；
>
> 不能据此保证本次原题重现。

- **逆否证明（proof by contraposition）** ：证$\neg q\to\neg p$。如“$3n+2$奇$\Rightarrow n$奇”，设$n=2k$得$3n+2=2(3k+1)$偶。

  多个前提的否定是析取，只须推翻其中一个合法的性质，不能尝试否定论域假设。

- **反证法（proof by contradiction）** ：假设目标否定，推出矛盾；证明$p\to q$时假设$p\land\neg q$。

  逆否证明有明确目标$\neg p$，反证法可由任何已知事实的冲突结束，不要混淆英文名称。

- **证明方法的选用与互相改写（choosing and converting proof methods）** ：可依次尝试直接证明、逆否证明与反证法；题目指定方法时按题目要求。

  已有$p\Rightarrow q$的直接证明，可在假设$p\land\neg q$后照原步骤推出$q\land\neg q$，改成反证法；已有$\neg q\Rightarrow\neg p$的逆否证明，可加上$p$后得到$p\land\neg p$，也改成反证法。两种间接证明（indirect proofs）的终点不同：逆否法明确推出$\neg p$，反证法只须得到矛盾。

- **正整数因子的平方根界（square-root bound on factors）** ：若$n=ab$且$a,b>0$，则$a\le\sqrt n$或$b\le\sqrt n$。用逆否法：若$a>\sqrt n$且$b>\sqrt n$，则$ab>n$，不可能$n=ab$。

- **有理数和的直接证明（direct proof of closure under rational addition）** ：若$r=p/q,s=t/u$，其中$p,q,t,u\in\mathbb Z$且$q,u\ne0$，则$r+s=(pu+qt)/(qu)$，分子分母为整数且$qu\ne0$，所以仍有理。

#### 平方根证明与等价性（Square-root Proof and Equivalence）

- $\sqrt2$无理的骨架：若$\sqrt2=a/b$且$a,b$互素（relatively prime），则$a^2=2b^2$；

  平方偶推出$a$偶，设$a=2k$得$b^2=2k^2$、$b$也偶，与互素矛盾。

> [!warning] 【考试注意】
> 最简分数及非零分母不能省；需要用英文表达“lowest terms / relatively prime”。

> [!info] 【历年考过：C1.7课堂补充】
> 老师在这类无理数证明处提及以往期末题，并提醒失分常在“把自然语言陈述及其否定准确形式化”。先写清反设中的整数、互素和非零分母，再进行推导；这是历年信息，不是本次原题预告。

- **等价性证明（proof of equivalence）** ：$p\leftrightarrow q$分别证两方向；

  $n$个陈述等价可用循环蕴涵（cyclic implications）$p_1\to p_2\to\cdots\to p_n\to p_1$，只需$n$条而非$n(n-1)$条。

### 1.8 分情况、存在唯一性与证明策略（Cases, Existence, Uniqueness and Strategies）

#### 穷举与分类证明（Exhaustive Proofs and Proofs by Cases）

- **穷举证明（exhaustive proof）** 检验有限论域中的全部对象；分情况证明（proof by cases）将全部可能分成若干类，各证目标。逻辑依据是$(p_1\lor\cdots\lor p_k)\to q\equiv\bigwedge_i(p_i\to q)$，不可漏0、等号或其他边界。

- **穷举证明例（examples of exhaustive proofs）** ：对$n=1,2,3,4$，$(n+1)^3$依次为$8,27,64,125$，$3^n$为$3,9,27,81$，故四个情形均满足严格大于。100以内完全幂（perfect power，底数为正整数、整数指数$>1$）为$1,4,8,9,16,25,27,32,36,49,64,81,100$，其中仅8、9相邻；这只证明有限范围。

- **分类证明例（examples of proofs by cases）** ：整数$n$满足$n^2\ge n$：$n\ge1$时$n^2\ge n\cdot1$；$n=0$时相等；$n\le-1$时$n^2>0>n$。等号恰在$n=0,1$时成立，所以结论应为$n^2\ge n$。

- **绝对值（absolute value）乘法证明** ：$|t|=t$（$t\ge0$）、$|t|=-t$（$t<0$）。当$(x,y)$符号分别为$(+,+),(-,+),(+,-),(-,-)$时，$|xy|$依次为$xy,-xy,-xy,xy$，均等于$|x||y|$；将0并入非负情形即可覆盖全部实数。

#### 存在与唯一性（Existence and Uniqueness）

- **存在性证明（existence proof）** 要证明$\exists xP(x)$；给出对象并验证即可。例如，$1729=10^3+9^3=12^3+1^3$给出了同一正整数的两种不同正立方和表示，从而证明这种整数存在。

- **唯一性证明（uniqueness proof）** 有两部分：先证明存在，再证明任意两个满足者相等，不能把“至多一个”当“恰好一个”。例：若$a,b\in\mathbb R,a\ne0$，则$ar+b=0$有唯一实解。

  存在：取$r=-b/a$，代入得$a(-b/a)+b=0$。唯一：设$s$也是解，$as+b=ar+b=0$，相减得$a(s-r)=0$，由$a\ne0$得$s=r$。若$a=0$，则按$b=0$或$b\ne0$分别为无穷多解或无解，不能沿用唯一性结论。

> [!tip] 【证明书写】存在与唯一分别论证
> 存在性须给出候选对象并验证；唯一性须从任意两个满足条件的对象出发，证明它们相等。两部分均须写出必要理由，不能仅用“显然”替代关键推理。

> [!todo]- 【待补证明 P01】存在唯一须分别验证，不直接判为概念错误
> **来源与状态**：第一轮，第1章精选卷题组7，Rosen §1.8 Ex.16。原作答给出了候选解，但存在性、唯一性的验证不完整；这是待补证明，不据此断言没有理解唯一性的定义。
>
> **原题（English）**：Show that if $a,b,c$ are real numbers and $a\ne0$, then there is a unique solution of the equation $ax+b=c$.
>
> **标准答案（English）**：Let $x_0=(c-b)/a$. Then $ax_0+b=c$, so a solution exists. If $u$ and $v$ are both solutions, then $au+b=av+b$, hence $a(u-v)=0$. Since $a\ne0$, $u=v$. Therefore the solution exists and is unique.

#### 归纳法前置知识（Induction Prerequisite）

- **数学归纳法（mathematical induction）** 用于证明带整数下标的一系列命题：先证基础步（base case）$P(n_0)$，再假设任意$k\ge n_0$的$P(k)$成立并证$P(k+1)$，才能推出所有$n\ge n_0$成立。关系幂、树边数和欧拉公式的具体证明保留在对应章。

## 二、集合、函数、序列与矩阵（Sets, Functions, Sequences and Matrices）

### 2.1 集合的基本语言（Basic Set Language）

#### 集合的表示与常用对象（Notation and Common Sets）

- **集合（set）** 是不计顺序与重复的对象整体；元素（element / member）用$\in$表示。

  列举法（roster method）写出元素，描述法（set-builder notation）写$\{x\in U\mid P(x)\}$；省略号必须有可辨认规则。集合中的元素可以也是集合。

- **常用数集（number sets）** ：自然数$\mathbb N$（本笔记约定含0）、整数$\mathbb Z$、正整数$\mathbb Z^+$、有理数$\mathbb Q$、实数$\mathbb R$、复数$\mathbb C$；

  题目另有约定时从其约定。$\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q\subseteq\mathbb R\subseteq\mathbb C$。

- **全集（universal set）** $U$限定讨论范围；空集（empty set / null set）$\varnothing$无元素；单元素集（singleton set）只有一个元素。

  $\varnothing\ne\{\varnothing\}$，后者基数为1；$\{\varnothing,\{\varnothing\}\}$有两个元素。

- **有理数（rational number）** 的精确定义为$\mathbb Q=\{p/q:p,q\in\mathbb Z,q\ne0\}$；实数（real number）中不属于$\mathbb Q$的为无理数（irrational number）。分母必须非零；$p/q$中的分子、分母均为整数。

#### 相等、包含与证明（Equality, Inclusion and Proof）

- **相等（equality）** ：$A=B\iff\forall x(x\in A\leftrightarrow x\in B)$。子集（subset）$A\subseteq B\iff\forall x(x\in A\to x\in B)$；真子集（proper subset）还要求$A\ne B$。

  总有$\varnothing\subseteq A$、$A\subseteq A$；$\varnothing\in A$则要看A是否真的把空集作为元素。

- 证包含取任意$x\in A$再证$x\in B$；否证找$x\in A\setminus B$；证集合相等可证双向包含（double inclusion）。

  $\in$比较对象与集合，$\subseteq$比较集合与集合，不可互换。文氏图（Venn diagram）可辅助理解，不代替一般证明；作业中的$A\subseteq B\subseteq C$可画三层嵌套区域。

#### 基数、幂集与积（Cardinality, Power Sets and Products）

- **有限集（finite set）** 的基数（cardinality）$|A|$为不同元素数；无限集（infinite set）没有有限基数。

  幂集（power set）$\mathcal P(A)$是所有子集组成的集合，$|\mathcal P(A)|=2^{|A|}$（A有限）；$\mathcal P(\varnothing)=\{\varnothing\}$。每个元素选／不选两种选择给出计数证明。

- **有序对（ordered pair）** $(a,b)=(c,d)\iff a=c\land b=d$；顺序不可丢失。笛卡尔积（Cartesian product）$A\times B=\{(a,b):a\in A,b\in B\}$，有限时$|A\times B|=|A||B|$；一方空则积空。

  一般$A\times B\ne B\times A$，但二者有自然双射。$n$元组（$n$-tuple）推广到多集合乘积，基数逐项相乘；$A^n$为n重笛卡尔积，不是幂集。

  边界结论：$A\times B=\varnothing$当且仅当$A=\varnothing$或$B=\varnothing$；$A\times B=B\times A$当且仅当$A=B$或至少一个集合为空。非空时可固定另一坐标，把任意$a\in A$放入有序对并利用积相等推出$a\in B$，再反向证包含。

- **二元关系（binary relation）** 是$A\times B$的子集，函数是具有单值且处处定义限制的关系。真值集（truth set）为$\{x\in U:P(x)\}$；

  $\forall x\in A\,P(x)$展开为$\forall x(x\in A\to P(x))$，存在则配合取。

- **真值集与量化真值（truth sets and quantified truth values）** ：$T_P=\{x\in U:P(x)\}$，则$\forall xP(x)$为真当且仅当$T_P=U$；$\exists xP(x)$为真当且仅当$T_P\ne\varnothing$。空论域情形仍与这两个判断一致。

### 2.2 集合运算与位串表示（Set Operations and Bit-string Representation）

| 运算（operation） | 定义及逻辑对应 |
|---|---|
| 并集（union）$A\cup B$ | $x\in A\lor x\in B$ |
| 交集（intersection）$A\cap B$ | $x\in A\land x\in B$ |
| 差集（difference）$A-B$ | $x\in A\land x\notin B$；$A-B=A\cap\overline B$ |
| 补集（complement）$\overline A=U-A$ | 相对于明确的U取“不属于A” |
| 对称差（symmetric difference）$A\oplus B$ | $(A-B)\cup(B-A)=(A\cup B)-(A\cap B)$，对应XOR |

#### 基本运算与容斥（Operations and Inclusion–Exclusion）

- **不相交（disjoint）** 指$A\cap B=\varnothing$；两两不交（pairwise disjoint）要求任意不同下标两集合不交，比“全部交集空”强。差集不交换、不结合；

  $A-(B-C)$与$(A-B)-C$一般不同。

- **容斥原理（inclusion–exclusion principle）** ：$|A\cup B|=|A|+|B|-|A\cap B|$；三集合为单集和减两两交加三重交。互不相交时直接相加。

  $|A\oplus B|=|A|+|B|-2|A\cap B|$，有限集求大小可先由包含关系排序。

![[C2.2-三集合容斥原理.png|600]]

- **三集合容斥的完整公式（three-set inclusion–exclusion formula）** ：对有限集合，

  $$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.$$

  证明要点：只在一集中的元素计1次；在两集中的元素计$2-1=1$次；在三集中的元素计$3-3+1=1$次。集合必须有限才能直接用这些普通整数减法；不能把无限基数当作整数随意相减。

#### 集合的位串表示（Bit-string Representation of Sets）

- **特征位串（characteristic bit string）** ：有限且大小可存储的全集$U=\{a_1,\ldots,a_n\}$先固定顺序；第$i$位为1当且仅当$a_i\in A$。相同位序下，并、交、补、对称差分别为逐位OR、AND、NOT、XOR，不能混用两种元素顺序。

  例：$U=\{1,\ldots,10\}$、$A=\{1,3,5,7,9\}$、$B=\{1,2,3,4,5\}$，对应$1010101010$与$1111100000$；交为$1010100000$，并为$1111101010$，补$B$为$0000011111$。

### 2.3 函数及其运算（Functions and Their Operations）

#### 函数定义与像（Definition and Images）

- **函数／映射（function / mapping）** $f:A\to B$把每个$a\in A$对应唯一$f(a)\in B$。

  定义域（domain）是A，陪域（codomain）是B，值域／像（range / image）$f(A)\subseteq B$；原像（preimage）是映到目标值的输入。

  判定函数要同时排除“一输入多输出”和“定义域有输入没有输出”。程序可能不终止或有副作用，不能直接等同于数学总函数（total function）。

- 函数相等需定义域、陪域的约定及各点输出一致；函数图像（graph of a function）为$\{(a,f(a)):a\in A\}\subseteq A\times B$。实值函数的和与积逐点定义：$(f+g)(x)=f(x)+g(x)$、$(fg)(x)=f(x)g(x)$。

#### 单射、满射与双射（Injection, Surjection and Bijection）

- **单射（injection / one-to-one）** ：$f(x)=f(y)\to x=y$，等价于$x\ne y\to f(x)\ne f(y)$；否证找不同输入同输出。

  满射（surjection / onto）：$\forall b\in B\exists a\in A:f(a)=b$；否证找陪域内漏掉的值。

  双射（bijection / one-to-one correspondence）同时单且满，证明需分两部分。

- **严格递增／严格递减（strictly increasing / strictly decreasing）** 函数单射；

  非严格递增／递减（increasing / decreasing）可能有平台，不能保证单射。若A、B有限且大小相同，单射当且仅当满射；无限集上不成立，如$n\mapsto n+1$在$\mathbb N$上单而不满。

- **单调性的定义（definitions of monotonicity）** ：对实数子集上的实值函数，对任意$x<y$，$f(x)\le f(y)$称递增／不减（increasing / nondecreasing），$f(x)\ge f(y)$称递减／不增（decreasing / nonincreasing）；把两式改为严格不等号，分别得到严格递增（strictly increasing）和严格递减（strictly decreasing）。

  严格单调蕴涵单射，因为不同输入可按大小排序，其输出严格不等；单射不必单调，例如在$\{1,2,3\}$上依次映为$1,3,2$。普通递增／递减只是不保证单射，不能说所有这类函数都不单射。

#### 恒等、反函数与复合（Identity, Inverses and Composition）

- **恒等函数（identity function）** $i_A(a)=a$。反函数（inverse function）$f^{-1}:B\to A$存在当且仅当f双射；交换输入输出即可。

  限制定义域或陪域（restriction of domain or codomain）可使$x^2$成为可逆函数，例如$[0,\infty)\to[0,\infty)$。

- **复合函数（composition）** $(f\circ g)(x)=f(g(x))$，先g后f，须保证中间像落在下一定义域。复合结合，但一般不交换。

  双射与逆函数满足恒等式：$f^{-1}\circ f=i_A$、$f\circ f^{-1}=i_B$，先代入$f^{-1}(f(a))=a$、$f(f^{-1}(b))=b$即可验证。

![[C2.3-映射类型-单射满射双射.png|650]]

- **反函数、倒数与逆运算（inverse functions, reciprocals and undoing operations）** ：$f^{-1}$是反函数，$(1/f)(x)=1/f(x)$是逐点倒数，只在$f(x)\ne0$时定义，二者不能互换。双射还满足$(f^{-1})^{-1}=f$。

#### 阶乘（Factorials）

- **阶乘（factorial）** 为$n!=1\cdot2\cdots n$，$0!=1$，表示$n$个不同对象的全排列数。

### 2.4 序列与递推预备（Sequences and Recurrence Prerequisites）

#### 序列、递推与迭代（Sequences, Recurrences and Iteration）

- **序列（sequence）** 按整数下标列项（term）$a_n$，须说明下标（index）起点；递推关系（recurrence relation）以前项给后项，配足初始条件（initial conditions）才确定解（solution）。递推建模与例题见第五部分。

- **复利与迭代（compound interest and iteration）** ：$P_n=(1+r)P_{n-1}$反复代入得$P_n=P_0(1+r)^n$。正向／反向代入（forward / backward substitution）是迭代求闭式（closed formula）的方式。初值取决于最大滞后及起始下标，如$a_n=a_{n-5}$通常需5个初值。

### 2.6 矩阵记号与布尔运算（Matrix Notation and Boolean Operations）

#### 矩阵记号（Matrix Notation）

- **矩阵（matrix）** 的$m\times n$表示$m$行$n$列，条目（entry）$a_{ij}$按先行后列编号；方阵（square matrix）行列数相同。关系矩阵以行、列分别对应有序对的第一、第二个分量。

#### 布尔矩阵及可达性（Boolean Matrices and Reachability）

- **零一矩阵／布尔矩阵（zero–one / Boolean matrix）** 条目0或1；并／合取的对偶运算（join / meet）逐项OR／AND；

  布尔积（Boolean product）记$A\odot B$：$(A\odot B)_{ij}=\bigvee_t(a_{it}\land b_{tj})$。普通积数中转方案个数，布尔积只问是否存在；不能把OR换成算术加法。

- **布尔幂（Boolean power）** $A^{[0]}=I$（$I$对角线为1，其余为0）、$A^{[r+1]}=A^{[r]}\odot A$表示恰好r步的可达性（reachability）。

  不同于任意正长度可达性，后者为$A\lor A^{[2]}\lor\cdots\lor A^{[n]}$，与传递闭包相接。

- 逐项并交有幂等、交换、结合、分配律，$A\lor0=A$、$A\land0=0$；布尔积有结合律和单位元I、零元0，也对逐项OR分配，但一般不交换。不要把逐项AND与布尔积当同一个运算。

## 三、关系（Relations）

### 3.1 二元关系的性质与运算（Properties and Operations of Binary Relations）

#### 关系与表示（Relations and Representations）

- **从A到B的关系（relation from A to B）** 为$R\subseteq A\times B$；A上的关系（relation on A）为$R\subseteq A\times A$；$aRb$表示$(a,b)\in R$。

  一般关系允许某输入无输出或多输出，函数不允许。

  一对多（one-to-many）、多对一（many-to-one）、多对多（many-to-many）描述相关对象的对应情况；“是关系”本身不要求单射、满射或单值。

- **表示法（representations）** ：有序对集合（set of ordered pairs）、描述条件（defining predicate）、零一矩阵（zero–one matrix）、有向图（directed graph / digraph）。

  判断任何性质前先确定底集A，尤其是没有出现在有序对清单里的元素。

| 性质（property） | 定义与矩阵／图判据 |
|---|---|
| 自反（reflexive） | $\forall a\in A:aRa$；主对角线全1，每点有自环 |
| 反自反／非自反（irreflexive） | $\forall a\in A:\neg aRa$；主对角线全0。不同于“不是自反” |
| 对称（symmetric） | $aRb\Rightarrow bRa$；$M=M^T$，所有边有反向边 |
| 非对称（asymmetric） | $aRb\Rightarrow\neg bRa$；不同点不能双向，自环也不允许 |
| 反对称（antisymmetric） | $aRb\land bRa\Rightarrow a=b$；仅禁止不同点双向，自环任意 |
| 传递（transitive） | $aRb\land bRc\Rightarrow aRc$；每条两步路有直接边，$M^{[2]}\le M$逐项比较 |

#### 六种性质的判断（Testing the Six Properties）

> [!question] 性质研究的对象是谁？（What do the properties apply to?）
> 研究的是给定的关系$R$本身，即$A\times A$中指定的那个子集，不是全集$A\times A$；$A\times A$只是背景，规定了所有可能的有序对。
>
> - **自反性（reflexivity）要看集合$A$** ：$R$自反当且仅当对$A$中**每个**元素$a$都有$(a,a)\in R$。同一个$R$放在不同的$A$上结论可能不同，如$R=\{(1,1),(2,2)\}$在$A=\{1,2\}$上自反，在$A=\{1,2,3\}$上不自反（缺$(3,3)$）。
> - **其余性质只看$R$中实际出现的有序对** ：对称、反对称、传递都是“若$R$中有某些对，则必须有／不能有另一些对”的条件；反自反只要求$R$中没有任何$(a,a)$。它们与$A$中是否有多余元素无关。

- 非对称等价于反对称＋反自反；对称与反对称可以同时成立，如对角关系（diagonal relation）$\Delta_A=\{(a,a):a\in A\}$及其子集。自环有些有、有些无时既不自反也不反自反。

  存在一对双向边不能证明全关系对称；需查全部边。空关系（empty relation）在非空A上反自反、对称、非对称、反对称、传递，但不自反，许多性质是空真。

- **常用关系（standard relations）** ：相等$=$是等价关系与偏序；$\le$、正整数上的整除（divisibility）$a\mid b$是偏序；

  $<$是非对称且传递的严格序（strict order）；模m同余（congruence modulo m）是等价关系。由距离接近定义的关系常缺传递，判不成立应给明确反例。

#### 集合运算与复合（Set Operations and Composition）

- **关系作为集合可取并、交、差、对称差、补关系（complementary relation）** $\overline R=(A\times B)-R$。两自反关系的并交仍自反、对称差反自反；对称关系的并交仍对称；

  反对称关系的交仍反对称，并不一定；传递关系的交仍传递，并不一定，例如$\{(1,2)\}\cup\{(2,3)\}$缺$(1,3)$。

- **复合关系（composition of relations）** 采用函数式顺序：$S\circ R=\{(a,c):\exists b(aRb\land bSc)\}$， **先R后S** 。

  复合结合、对两侧并集分配、对两侧包含关系单调（monotone），一般不交换，也不对交／差无条件取等。对交通常只有$T\circ(R\cap S)\subseteq(T\circ R)\cap(T\circ S)$等包含。

#### 关系幂与传递性（Powers and Transitivity）

- **关系幂（power of a relation）** $R^0=\Delta_A,R^{n+1}=R\circ R^n$；$R^{m+n}=R^m\circ R^n$，正好n步存在路径当且仅当$(a,b)\in R^n$。任意关系的幂不一定递增或递减；

  “最多n步”才用并$R\cup\cdots\cup R^n$。

- **传递性的幂刻画（power characterization）** ：$R$传递$\iff R^2\subseteq R\iff\forall n\ge1,R^n\subseteq R$；若自反，则$R\subseteq R^2$；

  自反且传递则$R^n=R$（$n\ge1$）。传递关系满足$R^{n+1}\subseteq R^n$且各次幂仍传递， **不保证$R^n=R^2$** 。反例$R=\{(1,2),(2,3),(1,3)\}$：$R^2=\{(1,3)\}$、$R^3=\varnothing$。

> [!todo]- 【待补证明 P03】自反与传递分别给出两个方向的包含
> **来源与状态**：第二轮，第9章题组4，Rosen §9.1 Ex.55。原作答明确写“不会”；这是方法缺口，与计算或书写失误分开记录。
>
> **原题（English）**：Let $R$ be a relation that is reflexive and transitive. Prove that $R^n=R$ for all positive integers $n$.
>
> **关键思路**：传递性给$R^2\subseteq R$；自反性允许插入自环，给$R\subseteq R^2$。先得$R^2=R$，再归纳到所有正整数次幂。
>
> **标准答案（English）**：Since $R$ is transitive, $R^2\subseteq R$. Conversely, if $(a,b)\in R$, reflexivity gives $(b,b)\in R$, so $(a,b)\in R^2$. Thus $R^2=R$. The case $n=1$ is immediate. If $R^k=R$, then $R^{k+1}=R\circ R^k=R^2=R$. By induction, $R^n=R$ for every positive integer $n$.

- **关系幂性质的证明要点（proofs of properties of relation powers）** ：

  1. **复合保包含（monotonicity of composition）** ：若$R\subseteq S$，复合中的中间见证在换成$S$后仍合法，故$T\circ R\subseteq T\circ S$，$R\circ T\subseteq S\circ T$。
  2. **幂与路径（powers and paths）** ：$n=1$是边的定义；长度$n+1$的路径拆出一条边与长度$n$的余段，按复合定义和归纳假设，恰好对应$R^{n+1}$。
  3. **传递性的幂刻画（power characterization of transitivity）** ：由$R^2\subseteq R$归纳得$R^{n+1}\subseteq R^2\subseteq R$；逆向只需取$n=2$。
  4. **各次幂仍传递（transitivity of every positive power）** ：由保包含归纳得$R\supseteq R^2\supseteq\cdots$。因此$(R^n)^2=R^{2n}\subseteq R^n$，即$R^n$传递。也可用捷径引理（shortcut lemma）：传递关系的两条相邻边能缩成一条，把$2n$步缩到$n$步。

  指数还满足$(R^m)^n=R^{mn}$；但一般$(R\circ S)^n\ne R^n\circ S^n$，展开后交替次序不能随意交换。这里的传递关系幂递减，不能推广到任意关系。

#### 逆关系与计数（Inverses and Counting）

- **逆关系（inverse relation）** $R^{-1}=\{(b,a):(a,b)\in R\}$；$(R^{-1})^{-1}=R$，逆保持并、交、差及适当全集下的补；$(S\circ R)^{-1}=R^{-1}\circ S^{-1}$，复合次序反转。

- **关系总数（number of relations）** ：若$|A|=m,|B|=n$，共有$2^{mn}$个A到B关系；n元集上为$2^{n^2}$，因为每个有序对可选或不选。

![[C9-四个性质的有向图判读.png|650]]

- **对称关系的逆刻画（inverse characterization of symmetry）** ：$R$对称当且仅当$R=R^{-1}$。正向由每条边都有反向边，分别得到双向包含；逆向由$(a,b)\in R=R^{-1}$立得$(b,a)\in R$。

  对同底集关系，$(R\cup S)^{-1}=R^{-1}\cup S^{-1}$、$(R\cap S)^{-1}=R^{-1}\cap S^{-1}$、$(R-S)^{-1}=R^{-1}-S^{-1}$；$(\overline R)^{-1}=\overline{R^{-1}}$的右侧补集须相对于反向笛卡尔积。逆关系总存在，不要求它还是函数。

### 3.2 多元关系与数据库（n-ary Relations and Databases）

#### 记录、属性与键（Records, Attributes and Keys）

- **$n$元关系（$n$-ary relation）** 为$R\subseteq A_1\times\cdots\times A_n$，各$A_i$是论域（domain），度（degree）为$n$，不是记录数。例如$R=\{(a,b,m)\in\mathbb Z\times\mathbb Z\times\mathbb Z^+:m\mid(a-b)\}$是三元关系，度为3，三个论域依次为$\mathbb Z,\mathbb Z,\mathbb Z^+$。

- **关系数据库（relational database）** 以元组为记录／行（record / row）、分量为字段／属性（field / attribute），展示为表；数学关系是集合，不保留重复行与自然行序。按条件筛选保留指定记录，连接则将不同表中符合匹配条件的记录拼接。

#### 选择、投影与连接（Selection, Projection and Join）

- **选择／条件筛选（selection）** 保留满足条件$C$的记录：$s_C(R)=\{\boldsymbol a\in R:C(\boldsymbol a)\}$，字段数不变。例如按“成绩$\ge60$”筛选成绩表，只保留及格记录，各行的字段结构不变。

- **连接（join）** 将两表公共字段值相同的记录拼接，公共部分只留一次。先对齐列序并检查全部共同字段；多对多匹配可产生多行，未匹配记录不进入内连接（inner join）。例如按学号连接成绩表与姓名表，不能仅因记录行号相同就配对。

### 3.3 矩阵与有向图表示（Matrix and Digraph Representations）

#### 矩阵、复合与图表示（Matrices, Composition and Digraphs）

- 固定$A=(a_1,\ldots,a_m),B=(b_1,\ldots,b_n)$的顺序，关系矩阵（relation matrix）$(M_R)_{ij}=1\iff a_iRb_j$。行是起点、列是终点；调换顺序会改矩阵外观，但不改关系本身。

- $M_{R\cup S}=M_R\lor M_S$，$M_{R\cap S}=M_R\land M_S$，$M_{R^{-1}}=M_R^T$；差与补逐项按集合定义。$M_{S\circ R}=M_R\odot M_S$，矩阵乘法顺序与复合记号表面相反，因为先走R对应左矩阵的行。

- $M_{R^n}=M_R^{[n]}$为布尔幂；普通矩阵幂不等同关系幂矩阵。

  有向图中顶点（vertex）对应元素，有向边／弧（directed edge / arc）$a\to b$对应有序对，自环（loop）对应$aRa$。图用于看反例、路径，矩阵适合统一计算与算法。

#### 用表示法判性质（Testing Properties from Representations）

- 自反看对角线全1，对称看转置相同，反对称看对角线外不能有互为对称位置的两个1；传递看布尔平方是否逐项不超过原矩阵。非对称还要求对角线全0。

  反对称关系的矩阵不叫“反对称矩阵（skew-symmetric matrix）”，后者是线性代数的$A^T=-A$，概念不同。

### 3.4 闭包与Warshall算法（Closures and Warshall's Algorithm）

#### 闭包的定义与三种闭包（Definition and Three Closures）

- **性质P的闭包（closure with respect to P）** 是包含R且满足P的最小关系：“最小”按集合包含，不只是元素数较少。

  并非任何性质都能只加有序对得到闭包，例如原R已违反反对称时不能靠加边修好。

- **自反闭包（reflexive closure）** $r(R)=R\cup\Delta_A$；对称闭包（symmetric closure）$s(R)=R\cup R^{-1}$；

  传递闭包（transitive closure）$t(R)=\bigcup_{k\ge1}R^k$。

  课程将最后一个记为$R^*$（连通性关系，connectivity relation）， **按正长度解释，不自动加$\Delta_A$** ；有的教材把星号定义成含0次幂，须明确区别。

#### 传递闭包的上界与证明（Bounds and Proof of Transitive Closure）

- **路径长度上界（path-length bound）** ：有限$n$元集上，若不同端点可达，删去重复点间的闭段得到至多$n-1$步；同点的正长度闭路只保留首尾相同，可缩为至多$n$步。因此$R^*=R\cup\cdots\cup R^n$，不能无条件截到$n-1$。

- **传递闭包的三步证明（three-step proof of transitive closure）** ：

  1. 包含：$R=R^1\subseteq R^*$。
  2. 传递：若$(x,y)\in R^m,(y,z)\in R^n$，拼接得$(x,z)\in R^{m+n}\subseteq R^*$。
  3. 最小：任取传递的$S\supseteq R$；由复合保包含得$R^k\subseteq S^k$，由$S$传递得$S^k\subseteq S$，故所有$R^k$及其并都在$S$中。

  “包含、传递、最小”缺一不可；只证明$R^*$传递不足以证明它就是闭包。

#### Warshall递推与执行顺序（Warshall Recurrence and Execution Order）

- **逐次布尔乘法（successive Boolean multiplication）** 并上各次幂可求闭包，按朴素实现$O(n^4)$。

  Warshall算法（Warshall's algorithm）按可用中间顶点（intermediate vertices）分层，把复杂度降到$O(n^3)$，空间$O(n^2)$。

$$
W^{(0)}=M_R,\qquad
w_{ij}^{(k)}=w_{ij}^{(k-1)}\lor
\left(w_{ik}^{(k-1)}\land w_{kj}^{(k-1)}\right).
$$

- 第k轮只允许编号$1,\ldots,k$的点作中间点；“原来可达”或“可经k接力”二者取OR。循环顺序是k最外层、再i与j；不可随意把k放里层。

  原地更新（in-place update）合法，但手算分层记录能看清变化。

> [!warning] 【考试注意：第15节转写】
> 老师明确说期末要能“by hand、one element by element”计算；不仅会写Python。写$W^{(0)},W^{(1)},\ldots$并圈出新增1，最终转回有序对或可达结论。

- **Warshall的完整步骤（complete Warshall procedure）** ：输入按固定顶点顺序排列的$n\times n$关系矩阵，输出正长度传递闭包矩阵。

```text
W := M
for k := 1 to n:
    for i := 1 to n:
        for j := 1 to n:
            W[i,j] := W[i,j] OR (W[i,k] AND W[k,j])
return W
```

  第$k$轮若$W[i,k]=1$，就把第$k$行逐位OR入第$i$行；若为0，该行这一轮无须因$k$而更新。内部顶点（interior vertex）按在路径中的位置判断：一个起点若中途再次出现，该次出现也算内部顶点。

  正确性要点：允许的内部顶点逐轮扩为$\{1,\ldots,k\}$，一条路要么不用$k$，要么在$k$处拆成两段；去掉重复绕行后可用这一分解。第$n$轮后所有中间顶点都已允许。不能初始化为全1，也不能把每个对角元预设为1来混淆正长度闭包与自反传递闭包。

#### 手算例（Worked Calculation）

- **四点Warshall手算例（a four-vertex Warshall example）** ：顶点顺序$a,b,c,d$，输入关系矩阵

$$
W^{(0)}=\begin{bmatrix}
0&0&0&1\\1&0&1&0\\1&0&0&1\\0&0&1&0
\end{bmatrix}.
$$

  第1轮允许$a$中转，只有$b\to a\to d$新增，故把$(b,d)$改1。第2轮允许$b$，但没有点能到$b$，无新增，$W^{(2)}=W^{(1)}$：

$$
W^{(1)}=W^{(2)}=\begin{bmatrix}
0&0&0&1\\1&0&1&1\\1&0&0&1\\0&0&1&0
\end{bmatrix}.
$$

  第3轮允许$c$，由$d\to c$把$c$行OR入$d$行，新增$(d,a),(d,d)$：

$$
W^{(3)}=\begin{bmatrix}
0&0&0&1\\1&0&1&1\\1&0&0&1\\1&0&1&1
\end{bmatrix}.
$$

  第4轮允许$d$，所有能到$d$的行并入$d$行，新增$(a,a),(a,c),(c,c)$，得到

$$
W^{(4)}=\begin{bmatrix}
1&0&1&1\\1&0&1&1\\1&0&1&1\\1&0&1&1
\end{bmatrix}=M_{R^*}.
$$

  $a,c,d$处在正长度回路上，对角为1；没有任何边进入$b$，故$b$列含对角始终为0。不能预先给所有对角填1。

![[C9-Warshall两种情形.png|600]]

#### 闭包的保留性质与次序（Preserved Properties and Order of Closures）

- 已有性质则闭包不变：$r(R)=R\iff R$自反，其余同理。三种闭包均包含原关系、幂等（idempotent）且对包含单调。自反闭包保持对称和传递，传递闭包保持自反和对称，对称闭包保持自反，但可破坏传递。

- **闭包次序（order of closure operations）** ：$r(s(R))=s(r(R))$，$r(t(R))=t(r(R))$；一般$s(t(R))\subseteq t(s(R))$且可能严格不等。

  例$R=\{(1,2),(3,2)\}$原本传递，先对称后传递得到3点全关系9对，先传递后对称只有4对。闭包不普遍对差、补分配；如$t(R_1-R_2)\ne t(R_1)-t(R_2)$。求逆与自反闭包相容：$r(R^{-1})=r(R)^{-1}$。

### 3.5 等价关系、等价类与划分（Equivalence Relations, Classes and Partitions）

#### 等价关系、等价类与划分（Equivalence, Classes and Partitions）

- **等价关系（equivalence relation）** 要求自反、对称、传递同时成立；逐条证明，或转化成$f(x)=f(y)$型关系。典型例子：同余、字符串等长、相同函数值；

  “有共同朋友”“差小于某阈值”等不自动传递。

- **等价类（equivalence class）** $[a]_R=\{x\in A:xRa\}$；$aRb\iff[a]=[b]\iff[a]\cap[b]\ne\varnothing$。不同代表元（representative）可表示同一类；类必非空，包含自己的代表元；

  不同的类两两不交。

> [!warning]- 【个人知识错题 K04】一个具体等价类不等于所有类的分类规则
> **来源**：第二轮，第9章题组7，Rosen §9.5 Ex.16、40(a,b)。
>
> **错点**：$(1,2)$的等价类求对了，但解释所有等价类时仍回答“第二个数是第一个数的两倍”，只解释了比值为$1/2$的那一类。
>
> **原题相关小问（English）**：Let $R$ be the relation on the set of ordered pairs of positive integers such that $((a,b),(c,d))\in R$ if and only if $ad=bc$. (a) What is the equivalence class of $(1,2)$ with respect to the equivalence relation in Exercise 16? (b) Give an interpretation of the equivalence classes for the equivalence relation $R$ in Exercise 16. [Hint: Look at the ratio $a/b$ corresponding to $(a,b)$.]
>
> **答案**：$[(1,2)]_R=\{(k,2k):k\in\mathbb Z^+\}$。一般有$ad=bc\iff a/b=c/d$，故每个等价类由**比值相同**的正整数对组成，不同类对应不同的正有理数。例如$(1,1),(2,2)$同属比值1的类，和比值$1/2$的类不同。
>
> **English answer**：Each equivalence class consists of all ordered pairs of positive integers having the same ratio. Distinct classes correspond to distinct positive rational numbers.

- **划分（partition）** 是非空块（block）的集合，块两两不交且并为A。等价关系与划分一一对应：R给出全部不同等价类；划分$\{A_i\}$反推$R=\bigcup_i(A_i\times A_i)$。

  商集（quotient set）$A/R=\{[a]:a\in A\}$的元素是类，不是A中的普通元素。

  三元集$\{a,b,c\}$的划分恰有5种：$\{\{a,b,c\}\}$、$\{\{a\},\{b,c\}\}$、$\{\{b\},\{a,c\}\}$、$\{\{c\},\{a,b\}\}$、$\{\{a\},\{b\},\{c\}\}$。

> [!warning]- 【个人知识错题 K05】从划分还原关系要判断同块，不是比较集合大小
> **来源**：第二轮，第9章题组8，Rosen §9.5 Ex.47(a)。
>
> **原错点**：写成$A\,R\,B\iff|A|=|B|$，把元素间的同块关系改成了集合间的等势关系；研究对象和关系条件都变了。
>
> **原题（English）**：List the ordered pairs in the equivalence relation produced by this partition of $\{0,1,2,3,4,5\}$: $\{0\},\{1,2\},\{3,4,5\}$.
>
> **答案**：同块中的元素全部配对，包括自环；不同块之间不配对。
> $$\begin{aligned}R=\{&(0,0),\\&(1,1),(1,2),(2,1),(2,2),\\&(3,3),(3,4),(3,5),\\&(4,3),(4,4),(4,5),\\&(5,3),(5,4),(5,5)\}.\end{aligned}$$
> 共$1^2+2^2+3^2=14$个有序对。块大小只用于检查对数，不是定义两个元素是否相关的条件。

- **等价类定理的证明要点（proof of the equivalence-class theorem）** ：$aRb\Rightarrow[a]=[b]$：用对称性与传递性证明两个类双向包含；$[a]=[b]\Rightarrow[a]\cap[b]\ne\varnothing$：自反性使$a\in[a]=[b]$；若$c\in[a]\cap[b]$，由$aRc,bRc$及对称、传递得$aRb$，闭合三向等价。

- **等价关系与划分定理的证明要点（proof of the equivalence–partition correspondence）** ：自反性保证每个元素属于一个类，等价类定理保证不同类不交，因此构成划分。反向规定“同块即相关”：同元素在同一块得自反，交换得对称；若$a,b$同块而$b,c$同块，由块不交且共享$b$可知两块相同，得$a,c$同块即传递。这样构造的关系唯一，其类恰好是原划分的块。

#### 等价类大小与关系对数（Equivalence-class Sizes and Pair Counts）

- **类大小与关系对数（class sizes and pair counts）** ：有限等价类$A_1,\ldots,A_k$给$R=\bigcup_i(A_i\times A_i)$，故$|R|=\sum_i|A_i|^2$；例如三块大小分别为3、2、1，对应$9+4+1=14$个有序对，各块内部全部成对，不能只连不同元素而漏自环。

![[C9-集合的划分示意.png|510]]

### 3.6 偏序、Hasse图与格（Partial Orders, Hasse Diagrams and Lattices）

#### 偏序、可比性与字典序（Partial Orders, Comparability and Lexicographic Order）

- **偏序（partial order）** 为自反、反对称、传递关系；偏序集（partially ordered set, poset）记$(A,\preccurlyeq)$。

  严格偏序（strict partial order）为反自反且传递，因而非对称；由非严格序删除对角得到严格序，反过来补对角。等价关系用对称，偏序用反对称。

- **可比（comparable）** 指$a\preccurlyeq b$或$b\preccurlyeq a$，否则不可比（incomparable）。任意两点可比为全序／线性序（total / linear order）；

  链（chain）为其中全序的子集。正整数整除与幂集包含一般只是偏序。

- **字典序／词典序（lexicographic order）** 比较第一个不同分量；前面分量都相等才比较后面。字符串中真前缀排在长串之前；分量若只偏序，则第一处不同分量不可比时不能越过去用后面的大小决定。

#### Hasse图、极值与界（Hasse Diagrams, Extrema and Bounds）

- **覆盖关系（covering relation）** ：$b$覆盖a当$a\prec b$且无$a\prec c\prec b$。Hasse图（Hasse diagram）删自环、删传递边、去箭头并把大者画高。

  连接线只表示覆盖；$x\preccurlyeq y$表示$x=y$，或能从$x$沿边向上走到$y$。因此恢复偏序时须包含每个元素与自身的关系，不能只看严格向上的路径，也不凭横向位置判断可比。

![[C9-Hasse图的三步构造.png|600]]

> [!warning]- 【个人知识错题 K06】Hasse图的高低与连线必须服从给定偏序
> **来源**：第二轮，第9章题组9，Rosen §9.6 Ex.22(a)。
>
> **错点**：把整除偏序上下画反，并把不可比的2、3连起来；还漏了1与3、2与6的覆盖连线。此前列出的整除有序对清单本身正确。
>
> **原题（English）**：Draw the Hasse diagram for divisibility on the set $\{1,2,3,4,5,6\}$.
>
> **答案**：若$a\mid b$且$a\ne b$，将$b$画在$a$上方；只连覆盖对。由下到上的覆盖对为$\boxed{(1,2),(1,3),(1,5),(2,4),(2,6),(3,6)}$。1在最下方，2与3之间不连线；1与6已有中间点，因此也不直接连线。
>
> **正确图**：下图左侧为本题，中间为K07，右侧为K08。画得更高本身不表示可比，还必须存在相应的向上路径。
> ![[C9-HW-两轮练习Hasse订正.png|900]]

先指定环境偏序集$(A,\preccurlyeq)$和目标子集$B\subseteq A$。**区别在于比较范围与候选元素的范围** ：

- **极大元、极小元、最大元、最小元** 都在所研究的集合内部比较，结果必须属于该集合。若题目问整个偏序集的极值，就在$A$中比较；若问子集$B$的极值，就只在$B$中比较，沿用$A$的偏序关系。因此它们也可以研究子集，并非只能研究整体。
- **上界、下界、上确界、下确界** 针对目标子集$B$，但在环境集合$A$中寻找候选元素，结果不必属于$B$。$B=A$也允许；若改变环境集合，可选的界及确界的存在性也可能改变。

下表统一讨论$B$；研究整个偏序集时令$B=A$。

| 极值／界（extrema and bounds） | 定义与必须区分的条件 |
|---|---|
| 极大元（maximal element） | $m\in B$且不存在$b\in B$使$m\prec b$，可多个；$B$外的元素不参与此判断 |
| 极小元（minimal element） | $m\in B$且不存在$b\in B$使$b\prec m$，可多个；$B$外的元素不参与此判断 |
| 最大元（greatest / maximum element） | $g\in B$且对所有$b\in B$都有$b\preccurlyeq g$，若存在则唯一 |
| 最小元（least / minimum element） | $g\in B$且对所有$b\in B$都有$g\preccurlyeq b$，若存在则唯一 |
| 上界（upper bound） | $u\in A$且对每个$b\in B$都有$b\preccurlyeq u$；允许$b=u$，$u$可以属于$B$，也可以在$A\setminus B$中 |
| 下界（lower bound） | $l\in A$且对每个$b\in B$都有$l\preccurlyeq b$；允许$l=b$，$l$可以属于$B$，也可以在$A\setminus B$中 |
| 最小上界／上确界（least upper bound, lub / supremum） | $s$是$B$的上界，且对$B$的每个上界$u$都有$s\preccurlyeq u$；若存在则唯一，也允许$s\in B$ |
| 最大下界／下确界（greatest lower bound, glb / infimum） | $t$是$B$的下界，且对$B$的每个下界$l$都有$l\preccurlyeq t$；若存在则唯一，也允许$t\in B$ |

- **对象对比示例** ：在整除偏序$(A,\mid)$中，取$A=\{1,2,3,6\}$、$B=\{2,3\}$。$B$中的2、3互不可比，所以都是$B$的极大元，也都是$B$的极小元，但$B$没有最大元或最小元。相对于环境$A$，$B$的上界为$\{6\}$、下界为$\{1\}$，故上确界是6、下确界是1。若题目改问整个$A$，其唯一极大元和最大元是6，唯一极小元和最小元是1。

- **判图注意：包含自身** 。找上界／下界时，每个点都包含自身；其他点须能沿边向上／向下到达，不能仅按画面高度判断。例如在$(\{1,2,3\},\le)$中，$B=\{1,2\}$的上界为$\{2,3\}$、下界为$\{1\}$，所以$\operatorname{lub}(B)=2$、$\operatorname{glb}(B)=1$，两者都属于$B$。$B$的上界若属于$B$，就是$B$的最大元；下界若属于$B$，就是$B$的最小元。

- 不能把“某一个上界”当lub，也不能把“上界集合中的极小元”不经比较就当最小元。做题先写环境集合、目标子集、全部上／下界，再求其最小／最大者。有限非空偏序集总有极小与极大元，但不一定有最小与最大元。

> [!warning]- 【个人知识错题 K07】极大极小与整除上下界的方向
> **来源**：第二轮，第9章题组9，Rosen §9.6 Ex.33(a–h)。
>
> **错点**：因Hasse图上下反向而交换了极大、极小，并把共同倍数方向的上界与共同因数方向的下界混淆；最大、最小元素不存在的两个结论原来答对了。
>
> **原题（English）**：Answer these questions for the poset $(\{3,5,9,15,24,45\},\mid)$. (a) Find the maximal elements. (b) Find the minimal elements. (c) Is there a greatest element? (d) Is there a least element? (e) Find all upper bounds of $\{3,5\}$. (f) Find the least upper bound of $\{3,5\}$, if it exists. (g) Find all lower bounds of $\{15,45\}$. (h) Find the greatest lower bound of $\{15,45\}$, if it exists.
>
> **答案**：
>
> | 小问 | 正确答案 |
> |---|---|
> | (a) maximal elements | $\{24,45\}$ |
> | (b) minimal elements | $\{3,5\}$ |
> | (c) greatest element | Does not exist. |
> | (d) least element | Does not exist. |
> | (e) upper bounds of $\{3,5\}$ | $\{15,45\}$ |
> | (f) least upper bound | $15$ |
> | (g) lower bounds of $\{15,45\}$ | $\{3,5,15\}$ |
> | (h) greatest lower bound | $15$ |
>
> **检查方法**：上界$u$须满足$3\mid u$且$5\mid u$；下界$l$须满足$l\mid15$且$l\mid45$。允许与自身比较，故15本身是$\{15,45\}$的下界。45不是其下界，因为$45\nmid15$。所有候选都从题设环境集合中取。

#### 格与并交（Lattices, Join and Meet）

- **格（lattice）** 要求每一对元素都有lub和glb，记$a\vee b=\operatorname{lub}\{a,b\}$（并，join）、$a\wedge b=\operatorname{glb}\{a,b\}$（交，meet）。格中的并交交换、结合、幂等、吸收；

  序可由$a\preccurlyeq b\iff a\wedge b=a\iff a\vee b=b$恢复。

| 偏序集 | 并／lub | 交／glb |
|---|---|---|
| $(\mathcal P(S),\subseteq)$ | $A\cup B$ | $A\cap B$ |
| $(\mathbb Z^+,\mid)$ | 最小公倍数（least common multiple, lcm） | 最大公因数（greatest common divisor, gcd） |
| 全序集（total order） | max | min |

- 在整除偏序的某个子集里，环境中未包含lcm时不能直接把外面的数当lub；在子集内可能另有最小共同上界，或根本没有。

> [!warning]- 【个人知识错题 K08】判非格时必须指出真正缺失的界
> **来源**：第二轮，第9章题组10，Rosen §9.6 Ex.44(a)。
>
> **错点**：“不是格”的结论正确，但把9与12的最大下界说成不存在；还在图中连接了不满足整除关系的6与9。这里需要订正并、交的含义与候选范围。
>
> **原题（English）**：Determine whether the poset $(\{1,3,6,9,12\},\mid)$ is a lattice.
>
> **答案**：共同下界为$\{1,3\}$，故$9\wedge12=3$存在；给定集合中没有9与12的共同上界，因此$9\vee12$不存在，偏序集不是格。不能把集合外的36当作本题最小上界。正确覆盖对为$(1,3),(3,6),(3,9),(6,12)$，图见K06右侧。
>
> **English answer**：The poset is not a lattice because 9 and 12 have no common upper bound in the given set. Hence their least upper bound does not exist. Their greatest lower bound does exist and equals 3.

- **格的四条运算律（four lattice laws）** ：对任意$a,b,c$，

  | 定律（law） | 并（join） | 交（meet） |
  |---|---|---|
  | 交换律（commutativity） | $a\vee b=b\vee a$ | $a\wedge b=b\wedge a$ |
  | 结合律（associativity） | $a\vee(b\vee c)=(a\vee b)\vee c$ | $a\wedge(b\wedge c)=(a\wedge b)\wedge c$ |
  | 幂等律（idempotence） | $a\vee a=a$ | $a\wedge a=a$ |
  | 吸收律（absorption） | $a\vee(a\wedge b)=a$ | $a\wedge(a\vee b)=a$ |

  证明要点：二元并交的唯一性给出交换、幂等；两个结合式都等于三元素集合的同一个lub／glb；$a\wedge b\preccurlyeq a$使$a$就是$\{a,a\wedge b\}$的lub，得吸收律，交的式子对偶。分配律是额外条件，不由以上四律直接保证。

> [!warning] 【易错】在给定偏序集内找上下界
> 整除偏序集$\{1,2,3,4,8,16\}$不是格：2、3在该集合中没有共同倍数，因此没有共同上界，更没有最小上界。lub／glb必须属于给定集合，不能借用集合外的6或其他数。

#### 格的类型与对偶（Lattice Types and Duality）

- **分配格（distributive lattice）** 满足$a\vee(b\wedge c)=(a\vee b)\wedge(a\vee c)$及对偶式；一般格未必分配。

  五元素菱形$M_3$的中间三点a、b、c使$a\vee(b\wedge c)=a$而$(a\vee b)\wedge(a\vee c)=1$。

- **有界格（bounded lattice）** 同时有底（bottom）0与顶（top）1；正整数整除格虽有底1但无顶，不有界。补元（complement）y满足$x\vee y=1,x\wedge y=0$；

  人人有补称补格（complemented lattice）。三元素链有界但中间元素无补；$M_3$有补但某点可有两个补。

- **对偶原理（principle of duality）** 反转序、互换并交与顶底，得到对偶格（dual lattice）的对应真命题；不能只换符号不换序。

## 四、计数（Counting）

组合数学（combinatorics）研究离散对象的计数、构造与结构；本部分同时讨论“有多少个”与“怎样不重不漏地生成”。

### 4.1 基本计数原理（Basic Counting Principles）

#### 加、乘、减、除四原理（The Four Counting Rules）

- **乘法原理（product rule）** ：任务分步，每个合法前缀的下一步都有固定的$n_i$个选择，总数$\prod_i n_i$。

  不要求概率意义的独立（independence），但若分支数依前面选择而不同，就应分类或用树形图逐支相加。

- **求和原理（sum rule）** ：互不相交的类型分别有$n_i$种，总数$\sum_i n_i$。“先分类、类内分步、最后求和”处理长度不同的密码、变量名与多方案任务。

- **减法原理（subtraction rule）** ：总数减不合法数；有交叠时用容斥。例：长度n位串“以1开头或以00结尾”，$n\ge3$时为$2^{n-1}+2^{n-2}-2^{n-3}$；“至少一个”常用总数减一个也没有。

- **除法原理（division rule）** ：若每个实际对象恰被表示d次，则实际数为表示数除d。纤维大小（fiber size）必须一致；对象有对称性（symmetry）时不能不检查就除固定阶乘。

- **计数应用例（counting examples）** ：BASIC变量名长1或2、首字符为字母、大小写不分并排除5个保留名，共$26+26\cdot36-5=957$。8位串以1开头或以00结尾为$2^7+2^6-2^5=160$；350名申请中两专业分别220、147、交51，均非两专业者$350-(220+147-51)=34$。

  病毒每次向50个新地址转发、无重叠的理想模型要先定轮起点：若初始1封为第1轮，前4轮和为$1+50+50^2+50^3=127551$；若初始后再转发4次，则总和为$\sum_{i=0}^450^i=6377551$。两种计数约定的差别在于是否把初始邮件算作第一轮，列式前须固定约定。

> [!warning]- 【个人知识错题 K09】同一情况内的两步相乘，不同情况之间再相加
> **来源**：自选第6章计数卷，2026-11-16，Q3(c)；教材来源按原卷为Rosen §6.3 Ex.30(b)。
>
> **原题（English）**：Seven women and nine men are on the faculty of a mathematics department. How many ways are there to select a committee of five members of the department if at least one woman and at least one man must be on the committee?
>
> **原步骤与错因**：已正确分成“1女4男、2女3男、3女2男、4女1男”，但每类写成$\binom7j+\binom9{5-j}$；选女性与选男性是组成同一个委员会的两步，每种女性选择都能搭配每种男性选择，应相乘。
>
> **正确答案**：
> $$\sum_{j=1}^{4}\binom7j\binom9{5-j}=882+1764+1260+315=\boxed{4221}.$$
> 补集核对为$\binom{16}5-\binom95-\binom75=4368-126-21=4221$。自查顺序：**先分类 → 类内分步相乘 → 类间互斥相加**。

> [!warning]- 【个人知识错题 K10】“至少四个”的补集是“至多三个”
> **来源**：同卷Q3(a)(iii)；Rosen §6.3 Ex.11(c)。
>
> **原题（English，节录）**：How many bit strings of length 10 contain at least four 1s? Evaluate the number.
>
> **原步骤与错因**：用总数减去上一问“至多四个1”的数量；即使修复上一问漏掉$\binom{10}1$的抄算问题，这样得到的仍是“至少五个1”。
>
> **正确答案**：
> $$\#(\text{至少4个1})=2^{10}-\sum_{k=0}^{3}\binom{10}k=1024-(1+10+45+120)=\boxed{848}.$$
> 对整数计数，$\neg(X\ge r)$是$X\le r-1$。本题恰好四个为210，至多四个为386；“至多四个”的漏项与本小问的补集边界错误分开处理。

#### 圆排列（Circular Arrangements）

- **圆排列（circular permutation）** ：n个不同人围圆桌、只把旋转看成同一排法时为$(n-1)!$；若座位编号则为$n!$；镜像（reflection）是否视同须题目说明。

  两方向相同的无向环游在$n\ge3$时常再除2。

### 4.2 鸽巢、拉姆齐与子序列（Pigeonhole, Ramsey and Subsequences）

#### 鸽巢与保证阈值（Pigeonhole Principle and Thresholds）

- **鸽巢原理／抽屉原理（pigeonhole principle / Dirichlet drawer principle）** ：$k+1$个物体进k盒至少一盒有两个；

  从更大有限集到更小有限集不存在单射。上取整（ceiling）$\lceil x\rceil$是不小于$x$的最小整数。广义鸽巢原理（generalized pigeonhole principle）：N个物体进k盒，至少一盒$\lceil N/k\rceil$个。

- **反问题（inverse problem）** ：要保证至少一盒有r个，最少$k(r-1)+1$个；若各盒容量上限不同则超过其上限和才强制违例。

  证明先写清“物体”“盒子”“分配规则”，给出最坏分配说明阈值不能再小。

- **鸽巢原理的证明与锋利性（proof and sharpness of pigeonhole bounds）** ：普通版若每盒至多1个，总数至多$k$，与至少$k+1$个矛盾。广义版若每盒都少于$\lceil N/k\rceil$个，总数至多$k(\lceil N/k\rceil-1)<N$，矛盾。

  要保证某盒至少$r$个，$k(r-1)$个时仍可每盒恰好$r-1$个，因此$k(r-1)+1$既足够又最小。定义域更大足以推出函数不单射；反过来，函数不单射不能推出定义域更大。

#### 用奇数核构造盒子（Constructing Boxes with Odd Parts）

- **因子分解（factorization）** 作盒子：$1,\ldots,2n$中的$n+1$个数写成$2^kq$，奇数q只有n种，两个共q者一个整除另一个。奇数核（odd part）而非数本身是盒子。

#### 生日问题与拉姆齐（Birthday Problem and Ramsey Theory）

- **生日问题（birthday problem）** ：保证同生日要考虑366种日期，367人才必然重复；这是必然性（certainty）。

- **拉姆齐数（Ramsey number）** $R(r,s)$是使任意红蓝边染色的完全图必含红$K_r$或蓝$K_s$的最小顶点数。$R(3,3)=6$：从一点的5条边至少3条同色；

  这3个邻点若有同色边，与原点成同色三角形，否则3条边全为另一色。五边形的边涂一种色、对角线另一色给出5点反例，故不能只证明上界6就直接写等号。

![[C6.2-K6二色染色必有同色三角形.png|510]]

> [!success]- 【补交核验】Ramsey题构造与结论正确，不再记为未作答
> **来源**：同卷Q2(d)，2026-11-17补交；原卷来源为Rosen §6.2 Example 13及Ex.26相关小问。
>
> **原题（English）**：Assume that every pair of people in a group are either friends or enemies. (i) Show that in any group of six people there are either three mutual friends or three mutual enemies. (ii) Show that in a group of five people there are not necessarily three mutual friends or three mutual enemies. (iii) What do (i) and (ii) together say about the Ramsey number $R(3,3)$?
>
> **作答状态**：选定$A$后用$\lceil5/2\rceil=3$分类、五边形反例和$R(3,3)=6$均正确。原英文未清楚表达“$D$同时与$B,C$都是敌人”，按条件表述规范处理，不另计概念错题。
>
> **正确证明**：任选$A$，其余5人中至少3人同为$A$的朋友或同为敌人。先设$B,C,D$同为$A$的朋友：若其中任意两人是朋友，他们与$A$组成三个共同朋友；否则$B,C,D$两两为敌。三个敌人的情形交换朋友、敌人作同样讨论，故$R(3,3)\le6$。五人置于五边形，规定相邻为朋友、非相邻为敌人；两种关系各形成一个5圈，均没有三角形，故$R(3,3)>5$。合得$\boxed{R(3,3)=6}$。
>
> **英文替换句**：If any two of $B,C,D$ are friends, they form three mutual friends together with $A$. Otherwise, $B,C,D$ are three mutual enemies. 保留原分支时则写：Otherwise, $D$ is an enemy of **both** $B$ and $C$.

#### 子序列定理（Monotone Subsequence Theorem）

- **子序列（subsequence）** 保留原顺序但可不连续；连续子串／连续子段（substring / contiguous segment）不可跳项。

  Erdős–Szekeres单调子序列定理（monotone subsequence theorem）：$n^2+1$个互异实数必有长$n+1$的严格递增或递减子序列。

  证明：给第$i$项标记以它结尾的最长递增、递减子序列长度$(I_i,D_i)$。若没有长$n+1$的任一类，则两坐标均在$1,\ldots,n$中，只有$n^2$种标签。$n^2+1$项中应有$i<j$标签相同；但两项互异，若$a_i<a_j$，可将$a_j$接在以$a_i$结尾的最长递增序列后，得$I_j\ge I_i+1$；若$a_i>a_j$，同理$D_j\ge D_i+1$。均与标签相同矛盾，故定理成立。互异条件不能漏，$n=3$时10项保证长4。

### 4.3 排列、组合与约束（Permutations, Combinations and Constraints）

#### 排列与组合公式（Permutation and Combination Formulas）

- **r排列（r-permutation）** 为从n个不同对象无放回取r个并排序，$P(n,r)=n(n-1)\cdots(n-r+1)=n!/(n-r)!$；r组合（r-combination）只选不排，$C(n,r)=\binom nr=n!/[r!(n-r)!]$。

  $P(n,0)=\binom n0=1$，空排列是唯一一种；$\binom nr=0$约定用于整数$r<0$或$r>n$。

- $P(n,r)=\binom nr r!$源于每个无序子集对应$r!$种顺序；$\binom nr=\binom n{n-r}$源于选入与选出互补。锦标赛名次／不同职务要排列，无职务委员会要组合；先选人再分配职务可能两步都要。

> [!warning]- 【个人知识错题 K11】指定两人中奖后，还要统计他们分别获得哪个奖
> **来源**：同卷Q3(b)(iii)；Rosen §6.3 Ex.25(e)。
>
> **原题（English，保留共同题干与本小问）**：One hundred tickets, numbered 1, 2, …, 100, are sold to 100 different people for a drawing. Four different prizes are awarded, including a grand prize. How many ways are there to award the prizes if the people holding tickets 19 and 47 both win prizes?
>
> **原步骤与错因**：只写$P(98,2)$，漏掉给19号、47号分别指定奖品的选择；奖品不同，即使中奖者已经固定，也仍有角色分配。
>
> **正确答案**：先给这两人依次分配不同奖品，共$P(4,2)=12$种；剩余两个奖品再分给其他98人，共$P(98,2)$种。因此
> $$P(4,2)P(98,2)=12\cdot98\cdot97=\boxed{114072}.$$
> 本题前两问列式$P(100,4)$和$4P(99,3)$正确；其数值被算成组合数，另列为计算核对项，不据此重复判为“不懂奖品有区别”。

#### 计算与应用（Calculation and Applications）

- 计算组合数可取$r\leftarrow\min(r,n-r)$，约分或用$\binom n{r+1}=\binom nr(n-r)/(r+1)$，避免先算巨大阶乘。阶乘与Stirling近似的区别见2.3。

- 位串恰有r个1为$\binom nr$；至少r个1为$\sum_{k=r}^n\binom nk$；两系分别选a、b人为$\binom{n_1}a\binom{n_2}b$；

  彩票匹配恰k个中奖号可用$\binom rk\binom{n-r}{r-k}$，全体结果为$\binom nr$（按题设抽取r号）。

- **委员会与职务分配（committees and assigned roles）** ：10人选四人委员会为$\binom{10}4$；再设一名主席乘4，设两名无区别联席主席（co-chairpersons）乘$\binom42$。若另设三人委员会及一名主席，若允许两委员会成员重合，则再乘$\binom{10}3\cdot3$；题目若要求不重合，第二组选人须改从剩余6人选。

#### 分组与相邻约束（Grouping and Adjacency Constraints）

相邻与不相邻限制先确定对象、位置和内部顺序；“两人不相邻”可用“全部排列数减去这两人相邻的排列数”。分组还须区分组是否有标签、是否允许空组及各组容量。

- 不同标签小组大小$n_1,\ldots,n_k$，总n人分组为$n!/(\prod_i n_i!)$；若等大小的组也不可区分，再除这些等类组的排列次数，不是所有分组一律除$k!$。

- **捆绑法（block method）** ：指定k人必须相邻，把他们当一块，与其他人一起排，再乘块内$k!$；指定内部顺序固定时不乘。

  插空法（gap method）：先排其余m人有$m+1$空，k个指定人两两不相邻时选k空再排人，$m!\binom{m+1}k k!$；可行条件$k\le m+1$。

- 相邻关系有重叠时用容斥，两个被禁止相邻对可能形成三人块；“至少一对相邻”的补集不总是“某指定一对相邻”。

  圆桌空隙为m而非$m+1$，固定旋转后为$(m-1)!\binom mk k!$（m个背景对象不同且$m\ge1$）。

![[C6-相邻约束的捆绑与插空.png|600]]

### 4.4 二项式系数与组合证明（Binomial Coefficients and Combinatorial Proofs）

#### 二项式系数与恒等式（Binomial Coefficients and Identities）

- **二项式系数（binomial coefficient）** $\binom nk$也就是$k$组合数；约定上指标$n\ge0$为整数、$\binom nk=0$当$k<0$或$k>n$，$\binom n0=\binom nn=1$。

| 组合恒等式（combinatorial identity） | 对象及条件 |
|---|---|
| 帕斯卡恒等式（Pascal's identity）：$\binom{n+1}k=\binom n{k-1}+\binom nk$ | 从$n+1$人选$k$，按固定一人入选与否分类 |
| 范德蒙德恒等式（Vandermonde's identity）：$\binom{m+n}r=\sum_{k=0}^r\binom mk\binom n{r-k}$ | 从两堆$m,n$人共选$r$；零值约定下$0\le r\le m+n$均可 |
| 曲棍球棒恒等式（hockey-stick identity）：$\sum_{j=r}^n\binom jr=\binom{n+1}{r+1}$ | $0\le r\le n$；按最大入选元素或最后一个1的位置分类 |

#### 帕斯卡三角与证明方法（Pascal’s Triangle and Proof Methods）

- **帕斯卡三角（Pascal's triangle）** 两边为1，内部每数为上方相邻两数和；边界与递推共同确定整表。

- **组合证明（combinatorial proof）** 用同一对象集的不同计数或双射证明等式；包括双重计数证明（double-counting proof）、双射证明（bijective proof）。须解释每个因子、分类互斥且覆盖全部；代数证明（algebraic proof）不能替代题目指定的组合证明。

> [!example] 完整例题：用组合证明帕斯卡恒等式（Pascal's identity）
> **题目** ：设$n,k$为正整数，$1\le k\le n$，证明$\binom{n+1}k=\binom n{k-1}+\binom nk$。
>
> **确定同一批计数对象** ：从$n+1$名不同学生中选出一个$k$人委员会（committee），成员没有职务区别，不计选出顺序。
>
> 1. **直接计数** ：从$n+1$人中选$k$人，共有$\binom{n+1}k$种，解释了等式左边。
> 2. **分类计数（counting by cases）** ：固定其中一名学生$a$，按$a$是否入选分类。
>    - **$a$入选** ：他占一个名额，只需从剩余$n$人中选$k-1$人，共$\binom n{k-1}$种。不额外乘$k$，因为固定的$a$没有可选择的位置或职务。
>    - **$a$不入选** ：全部$k$个名额都从剩余$n$人中选，共$\binom nk$种。
> 3. **说明为什么能相加** ：每个委员会恰好属于上述一类，两类互斥且覆盖全部委员会，没有重复或遗漏；按加法原理（sum rule），总数也等于$\binom n{k-1}+\binom nk$。
> 4. **得出结论** ：两种方法计算的是同一批委员会，因此$\binom{n+1}k=\binom n{k-1}+\binom nk$。
>
> **具体看一个数值** ：6人选3人，固定学生$a$。含$a$有$\binom52=10$种，不含$a$有$\binom53=10$种，所以$\binom63=10+10=20$；这也解释了帕斯卡三角中$20$为什么是上一行相邻两个$10$之和。
>
> **证明关键** ：上面的计数解释对所有符合条件的$n,k$成立；单独代入$6,3$验算，只能验证一个特例。
>

- **对称性证明（proof of symmetry）** ：从$n$元集合选$k$个与选剩余$n-k$个由取补一一对应，故$\binom nk=\binom n{n-k}$。

- **帕斯卡证明** ：固定$n+1$人中的$a$。包含$a$的$k$人组，另从$n$人选$k-1$；不含$a$则从$n$人选$k$。两类不交且无遗漏，相加即得恒等式。

- **Vandermonde证明** ：从不交的$m$人、$n$人两堆中共选$r$，总数$\binom{m+n}r$。按第一堆取$k$分类，第二堆取$r-k$，每类为$\binom mk\binom n{r-k}$；$k$不同互斥，求和覆盖全部。当$r\le\min(m,n)$时，各项组合数均在通常定义范围内；约定越界的组合数为0后，恒等式对$0\le r\le m+n$均成立。

> [!example]- 【证明规范 P04】Vandermonde分类已找对，还须写出互斥与穷尽
> **来源**：同卷Q4(d)；对应Rosen §6.4 Theorem 3。
>
> **原题（English）**：Give a combinatorial proof of Vandermonde's identity: for nonnegative integers $m,n,r$ with $r\le m$ and $r\le n$,
> $$\binom{m+n}r=\sum_{k=0}^{r}\binom m{r-k}\binom nk.$$
> Explain why the cases you add are disjoint and exhaustive.
>
> **作答状态**：两组球与按取球数分类的主要思路正确；需要说清球彼此可区分、两组事先固定且互不相交，并补题目要求的“不重不漏”。不计作独立概念错误。
>
> **正确证明**：固定不交集合$A,B$，大小分别为$m,n$，数$A\cup B$的$r$元子集$T$。直接数为$\binom{m+n}r$；设$k=|T\cap B|$，则这一类有$\binom m{r-k}\binom nk$个。每个$T$有唯一的$k$，故不同类互斥；每个$T$均有$0\le k\le r$，故分类穷尽。按求和原理得所证等式。
>
> **01串等价解释**：数长$m+n$、恰有$r$个1的位串，固定分成前$m$位与后$n$位；后段有$k$个1时，前段有$r-k$个1。这里按**固定的两段**分类，不按最后一个0分类。

- **曲棍球棒证明** ：数长度$n+1$、含$r+1$个1的位串，总数$\binom{n+1}{r+1}$。若最后一个1在第$k$位，$r+1\le k\le n+1$，前$k-1$位取$r$个1，共$\binom{k-1}r$；令$j=k-1$，求和即得。位置不同互斥，且每个合法串有唯一最后一个1。

> [!example]- 【证明规范 P05】冰球杆恒等式：图对应最后一个0，不是第一个0
> **来源**：同卷Q4(e)，2026-11-17补交；Rosen §6.4 Ex.27(a)的等价形式。补交后不再记为未作答。
>
> **原题（English）**：Prove the hockey-stick identity
> $$\sum_{k=0}^{r}\binom{n+k}k=\binom{n+r+1}r$$
> whenever $n$ and $r$ are positive integers, using a combinatorial argument. (Hint: count bit strings of length $n+r+1$ containing exactly $r$ ones, classified by the position of the last 0.)
>
> **作答状态**：总计数、图形分段与求和式正确，但把last反复写成first；图中单独取出的0前面已有$n$个0，实际画的是最后一个0。按英文与图不一致处理，不推断为概念不懂；原稿只展开$k=0,1$，另补一般$k$及分类理由。
>
> **正确证明**：数长$n+r+1$、恰有$r$个1的位串，总共$n+1$个0。直接选1的位置得$\binom{n+r+1}r$。设最后一个0前有$k$个1，则前缀含$n$个0、$k$个1，长度$n+k$，有$\binom{n+k}k$种；最后一个0之后固定是$r-k$个1。每个合法串有唯一的最后一个0，因此$k=0,\ldots,r$的分类互斥且穷尽，求和即得等式。
>
> **英文核心段**：Let $k$ be the number of ones before the last zero. Before this zero, there are exactly $n$ zeros and $k$ ones, giving $\binom{n+k}k$ possible prefixes. After it, all remaining $r-k$ bits must be ones. These cases are disjoint and exhaustive because every string has a unique last zero.

### 4.5 重复选择、物体分配与整数分拆（Repetition, Distribution and Integer Partitions）

| 选择方式 | r次从n种中选择的结果数 |
|---|---|
| 有序、不可重复（ordered without repetition） | $P(n,r)$ |
| 无序、不可重复（unordered without repetition） | $\binom nr$ |
| 有序、可重复（ordered with repetition） | $n^r$ |
| 无序、可重复（unordered with repetition） | $\binom{n+r-1}r$，$n\ge1$ |

- **四种选择公式的证明要点（proofs of the four selection formulas）** ：不可重复的$r$-排列按位置有$n,n-1,\ldots,n-r+1$种选择；每个$r$-组合恰有$r!$个内部次序，所以$P(n,r)=r!\binom nr$。允许重复的有序选择每步仍有$n$种，得$n^r$；无序重复选择与$r$颗星、$n-1$根隔板的位置串一一对应，得$\binom{n+r-1}r$。

  相同物体排列先临时贴标签计$n!$种，再除每类的内部置换数$\prod_i n_i!$；各盒规定人数时同理。相邻隔板和端点隔板已表示空类，无须再额外乘空盒的选择数。

> [!warning]- 【个人知识错题 K12】无序重复选择不是Stirling数：本题星条模型已做对
> **来源**：同卷Q5(a)(iv)；Rosen Chapter 6 Supplementary Ex.1相关小问。
>
> **原题（English，节录）**：How many ways are there to choose 6 items from 10 distinct items when the items in the choices are unordered and repetition is allowed? Name the formula used and evaluate it.
>
> **原步骤与错因**：先写$S(10,6)$并称为Stirling number，随后正确画出6颗星、9块板并算得5005；确认的是概念名称与记号混淆，不是星条构造错误。
>
> **正确答案**：这是重复组合（combinations with repetition）。令$x_i$为第$i$种物品选中的次数，则$x_1+\cdots+x_{10}=6,\ x_i\ge0$，故
> $$\boxed{\binom{10+6-1}{6}=\binom{15}{6}=5005}.$$
> 通常$S(10,6)$表示10个不同对象划分成6个非空无标号块，与本题不是同一对象集。这里只需分清含义，不因本题而新增Stirling递推或通式的背诵要求。

#### 星条法与整数解（Stars and Bars and Integer Solutions）

- **星条法（stars and bars）** ：r颗相同星代表物体，$n-1$条隔板代表n类，允许相邻隔板与端点隔板，分别表示空类；共$r+n-1$个位置选r个为星。

  它计无序重复选择，不计每个具体物体的身份。

- **弱组合（weak composition）** $x_1+\cdots+x_n=r,x_i\ge0$有$\binom{r+n-1}{n-1}$解；

  正整数解（positive integer solution）$x_i\ge1$有$\binom{r-1}{n-1}$解（$r\ge n$）。一般下界$x_i\ge l_i$先作$y_i=x_i-l_i$，剩余和为$r-\sum l_i$；

  剩余负则0解。

- **有上界（upper bounds）** 指单个变量有额外限制$x_i\le u_i$；普通星条公式会把超上界的解也计入，因此先数全部非负解，再扣除不合法的解，处理后仍可用星条法。

  例：$x_1+x_2+x_3=5,x_i\ge0$且$x_1\le2$。全部有$\binom72$解；不合法时$x_1\ge3$，令$y_1=x_1-3$，得$y_1+x_2+x_3=2$，有$\binom42$解，故合法数为$\binom72-\binom42=15$。

  对违反$x_i\le u_i$的情况作容斥，集合S中变量统一减$u_i+1$：$\sum_{S\subseteq\{1,\ldots,n\}}(-1)^{|S|}\binom{r-\sum_{i\in S}(u_i+1)+n-1}{n-1}$，上方不足$n-1$的项按0处理。

  **总和有上界** 如$x_1+\cdots+x_n\le r$则可加入非负松弛变量$x_{n+1}$，转成$x_1+\cdots+x_n+x_{n+1}=r$，直接用星条法。

> [!warning]- 【个人知识错题 K13】非负整数解不能套正整数解公式；上界违例也要保留下界
> **来源**：同卷Q5(b)(ii)；Rosen §6.5 Ex.15(c)。
>
> **原题（English）**：How many solutions are there to $x_1+x_2+x_3+x_4+x_5=21$, where each $x_i$ is a nonnegative integer and $0\le x_1\le10$?
>
> **原步骤与错因**：以$\binom{20}4$作总数；当$x_1=11$时把剩余和为10的四个变量算成$\binom93$，并只讨论到$x_1=17$。这些计数把允许0的变量当成了正整数；不合法解其实包括$(21,0,0,0,0)$。
>
> **正确答案**：全部非负解有$\binom{25}4=12650$个；不合法解满足$x_1\ge11$，令$y_1=x_1-11\ge0$，得到$y_1+x_2+\cdots+x_5=10$，共有$\binom{14}4=1001$个。因此
> $$\boxed{\binom{25}4-\binom{14}4=11649}.$$
> 若坚持分类，固定$x_1=t$时其余四变量的解数为$\binom{24-t}3$；不合法的$t=11,\ldots,21$应全部覆盖，首项是$\binom{13}3$，末项是$\binom33$。原式中额外减去$\binom{20}3$没有本题需排除的条件支持。
>
> **边界自查**：每问重新写清$x_i\ge0$或$x_i\ge1$。Q5(b)(i)采用$y_i=x_i-1\ge1$、总和16，再算$\binom{15}4=1365$是正确的，不能因参考答案改用$x_i-2\ge0$而改判。

> [!tip]- 【方法补充，不计概念错题】总和不等式：用松弛变量或核对求和换元后的上限
> **来源／原题（English）**：同卷Q5(b)(iii)，Rosen §6.5 Ex.20。How many solutions are there to the inequality $x_1+x_2+x_3\le11$, where $x_1,x_2,x_3$ are nonnegative integers?
>
> **原作答**：写$\sum_{k=2}^{10}\binom k2$，上限错误；仅凭这一行不判定为概念误解。
>
> **正确答案**：总和固定为$t$时有$\binom{t+2}2$解，故
> $$\sum_{t=0}^{11}\binom{t+2}2=\sum_{k=2}^{13}\binom k2=\boxed{\binom{14}3=364}.$$
> 其中$k=t+2$，所以$t=11$对应$k=13$。也可令$x_4=11-(x_1+x_2+x_3)\ge0$，原解与$x_1+\cdots+x_4=11$的非负解一一对应，直接星条得$\binom{14}3$。

#### 重复物体与循环计数（Repeated Objects and Loop Counts）

- **重复物体排列（permutations with indistinguishable objects）** 为多项式系数（multinomial coefficient）$n!/(n_1!\cdots n_k!)$，$\sum n_i=n$；各类内部交换不产生新排列。嵌套循环（nested loops）满足$1\le i_m\le\cdots\le i_1\le n$时次数$\binom{n+m-1}m$，严格不等时$\binom nm$。

- **物体与盒子的分类（classifying objects and boxes）** ：先判断物体可区分／不可区分（distinguishable / indistinguishable）、盒子有无标签、可否空盒及容量。相同物体进有标号盒用星条法；相同物体进相同盒须忽略盒序，按分拆列举。

![[C6.5-星条法示意图.png|600]]

> [!warning]- 【个人知识错题 K14】分配只计归属；先排列再切段会多计，去标签也不能一律除阶乘
> **来源**：同卷Q5(d)；Rosen §6.5 Ex.59。用分类即可，不要求Stirling公式。
>
> **原题（English）**：How many ways are there to distribute five balls into three boxes if each box must have at least one ball in it, if (i) both the balls and the boxes are labeled? (ii) the balls are labeled, but the boxes are unlabeled? (iii) the balls are unlabeled, but the boxes are labeled? (iv) both the balls and the boxes are unlabeled?
>
> **原步骤与错因**：先排5个不同球，再在4个内部空切成3段，意图计算$5!\binom42=720$；又将其除$3!$处理无标签盒。前一步把盒内顺序也算入：固定归属且盒装量为$(3,1,1)$时重复$3!1!1!=6$次，为$(2,2,1)$时重复$2!2!1!=4$次，不能用同一个常数直接修复。第(iv)问又将相同球、有标签盒的6种装量一律除$3!$，忽略相同装量的对称性。原稿$C(2,4)$的参数倒置、分母写$C(3,3)$是另列的记号问题。
>
> **正确答案与分类**：
>
> - **不同球、相同盒**：大小只可能$3+1+1$或$2+2+1$。前者选三球组有$\binom53=10$种；后者先选单球，再把其余四球分成两个无序对，有$5\binom42/2=15$种，合为$\boxed{25}$。
> - **不同球、不同盒**：每个非空分组的三个块按内容彼此不同，贴上三个盒标签恰有$3!$种，故$\boxed{25\cdot3!=150}$；也可用$3^5-3\cdot2^5+3=150$核对。
> - **相同球、不同盒**：正整数解$x_1+x_2+x_3=5$，共$\boxed{\binom42=6}$种，即$(3,1,1)$的3种不同排列及$(2,2,1)$的3种不同排列。
> - **相同球、相同盒**：只剩装量分拆$3+1+1,\ 2+2+1$，共$\boxed2$种。
>
> **除法条件**：本题(i)除以$3!$得到(ii)本身可以成立，因为不同球、三个盒均非空使每个无标签分组恰有6种贴标签方式；但原来的(i)已错。反之，(iii)不能直接除$3!$得到(iv)，因为$(3,1,1)$与$(2,2,1)$各只有3个不同的盒标签排列，而非6个。

#### 物体入盒与划分公式（Distribution and Partition Formulas）

- **通用入盒公式（general distribution formulas）** ：$n$个有身份物体进$k$个有标号盒，允许空为$k^n$、固定各盒人数为$n!/\prod n_i!$、各盒非空为$k!S(n,k)$；无标号非空盒为$S(n,k)$，至多$k$盒为$\sum_{j=0}^{\min(n,k)}S(n,j)$。第二类Stirling数见3.5；$S(n,k)=\frac1{k!}\sum_{i=0}^k(-1)^i\binom ki(k-i)^n$（$n,k\ge1$）。其中$S(n,k)$数无标号非空分组；再给各组分配不同盒号时乘$k!$。

#### 分拆、容量与边界（Integer Partitions, Capacities and Boundaries）

- **整数分拆（integer partition）** 不计盒序，写非增的装量；允许空盒时末尾补0。例如6本相同书进4个相同盒，允许空盒，9种为$(6,0,0,0),(5,1,0,0),(4,2,0,0),(4,1,1,0),(3,3,0,0),(3,2,1,0),(3,1,1,1),(2,2,2,0),(2,2,1,1)$。

- **混合水果入盒例（a mixed-fruit distribution example）** ：3苹果A、2橘子O、1香蕉B进3个相同盒，每盒2个。按B的同盒水果分类：$\{AB,AA,OO\}$、$\{AB,AO,AO\}$、$\{BO,AA,AO\}$，共3种。不能仅按总水果数6作整数分拆，因为还须保留类型。

> [!warning] 【易错】
> 无标号盒不能把有标号计数一律除$k!$，不同装法的重复次数可能不同。0物体用唯一空分配处理；$S(0,0)=1$。

### 4.6 生成排列与组合的算法（Algorithms for Generating Permutations and Combinations）

> [!important] 【老师明确会考：第19节，00:38:36–00:39:40】
> 老师在演示下一个排列时说“我一定会考这个算法”，并强调大学内容是怎样用算法找出排列与组合，不只是计算数量。以下三个后继算法（successor algorithms）均应能手算，尤其要解释最小性。

词典序（lexicographic order）按第一个不同位置比较。后继（successor）是所有更大对象中最小者，不是任意更大者。

以下伪代码均用1起始下标（one-based indexing）。

#### 下一个排列：操作、例子与证明（Next Permutation: Steps, Example and Proof）

**下一个排列（next permutation）** ，输入$n\ge1$个互异元素的当前排列；空排列只有一个，直接停止：

```text
j := n - 1
while j >= 1 and a[j] >= a[j+1]: j := j - 1
if j = 0: stop                    // 已是最后的降序排列
k := n
while a[k] <= a[j]: k := k - 1
swap a[j], a[k]
reverse a[j+1 .. n]
```

- 四步：从右找最后一个升序相邻对的左端j（枢轴，pivot）；从右找大于枢轴的最小值；交换（swap）；反转后缀（reverse the suffix）使其升序。

  原后缀降序，所以从右找到的第一个更大值就是最小可替换值。

- 手算$362541$：最长降序后缀为541，枢轴2，右边大于2的最小值为4；交换得$364521$，后缀521反转为125，得$364125$。不是把整个排列排序，也不是只交换最后两位。

- **最小性证明（minimality proof）** ：保留尽可能长前缀；在最靠右可增加处作最小增加；把尾巴压到最小。三点保证没有合法排列夹在两者之间。单次时间$O(n)$，原地额外空间$O(1)$；

  完整输出n!个对象仍有不可免的输出量。

![[C6.6-字典序下一排列的四个动作.png|620]]

- **下一个排列最小性的完整论证（full minimality argument for next permutation）** ：令$j$为枢轴位置、$a'$为输出，取任意比$a$大的排列$b$，看两者第一次不同的位置$p$。

  1. 若$p<j$，则$b_p>a_p=a'_p$，故$b>a'$。
  2. 若$p=j$，则$b_j>a_j$。算法选取的$a'_j$是可用元素中大于$a_j$的最小者，故$b_j\ge a'_j$；严格大时$b>a'$，相等时$a'$的升序后缀是剩余元素的最小排列，故$b\ge a'$。
  3. 若$p>j$，则$b$只重排$a$的原降序后缀，但原后缀已经是这些元素的最大排列，不可能使$b>a$。

  所以任意$b>a$都有$b\ge a'$，没有排列夹在$a$与$a'$之间。三种情形按第一次分歧位置划分，不能只写“显然是下一个”。

> [!todo]- 【待补证明 P06】能手算下一个排列，还要能写出没有中间排列的证明
> **来源**：同卷Q6(b)；Rosen §6.6 Ex.10。
>
> **原题（English）**：Show that the next-permutation algorithm produces the next larger permutation in lexicographic order. That is, if $a$ is the input and $a'$ the output, show that $a'>a$ and that no permutation $b$ satisfies $a<b<a'$.
>
> **原作答状态**：已写“任取$b>a$，令$p$为$b$与$a$的首个不同位置”，随后写不出来。Q6(a)三个手算过程全部正确；此处按证明未完成记录，不改判为不会执行算法。
>
> **正确证明（English）**：Assume that $a$ is not the largest permutation, and let $j$ be the pivot. The output agrees with $a$ before position $j$ and has $a'_j>a_j$, so $a'>a$. Take any permutation $b>a$, and let $p$ be the first position where $b$ and $a$ differ.
>
> 1. If $p<j$, then $b_p>a_p=a'_p$, so $b>a'$.
> 2. If $p=j$, the algorithm chooses the smallest available element greater than $a_j$, so $b_j\ge a'_j$. If the inequality is strict, then $b>a'$. If equality holds, both permutations have the same remaining elements, and the increasing suffix of $a'$ is their smallest arrangement. Hence $b\ge a'$.
> 3. If $p>j$, then $b$ changes only the original decreasing suffix of $a$. This suffix is already the largest arrangement of its elements, contradicting $b>a$.
>
> Thus every $b>a$ satisfies $b\ge a'$, so no permutation lies strictly between $a$ and $a'$. **记忆线索**：更早增加会更大；枢轴取最小可增值；尾部取最小排列。

#### 下一个位串：二进制加一（Next Bit String: Binary Increment）

**下一个位串（next bit string）** ：从右向左将末尾连续1改成0，遇第一个0改成1，等价于二进制加1（binary increment）。全1已是最后一个；

从全0开始会遍历$2^n$个子集的特征串，但普通加1不保持1的个数，不能直接当固定r组合后继。

  零长度位串只有空串，处理后立即结束；全1串无后继，不应默默绕回全0并造成重复。

#### 下一个组合：操作与例子（Next Combination: Steps and Examples）

**下一个r组合（next r-combination）** ：用严格递增整数序列$1\le a_1<\cdots<a_r\le n$表示，位置i上限为$n-r+i$。

```text
if r = 0: stop                    // 唯一空组合
i := r
while i >= 1 and a[i] = n-r+i: i := i - 1
if i = 0: stop                    // 已是最大组合，亦覆盖r=n
a[i] := a[i] + 1
for j := i+1 to r: a[j] := a[i] + j - i
```

- 从右找未顶格位置，增加1，再把后缀填成连续递增最小值；循环从$i+1$开始，不能覆盖刚加1的$a_i$。最大组合$(n-r+1,\ldots,n)$没有后继；$r=0$或$r=n$时各只有一个组合，停止检查可直接处理这些边界。

- **小规模演算（small example）** ：$n=4,r=2$时$12\to13\to14\to23\to24\to34$；$n=5,r=3$时$123,124,125,134,135,145,234,235,245,345$。换成a至e字母，逐位替换即可，顺序不变。

> [!tip]- 【过程书写提醒，不计知识错题】下一个组合须写当前值与位置上界的比较
> **来源／原题（English）**：同卷Q6(d)(ii)。Find the next larger 5-combination of $\{1,2,\ldots,8\}$ after $\{2,4,6,7,8\}$. Show the comparison $a_i$ versus $n-r+i$ for each position you inspect.
>
> **作答状态**：最终结果$\{2,5,6,7,8\}$正确，但未写题目要求的比较过程。
>
> **补全**：$n=8,r=5$，位置上界为$4,5,6,7,8$。从右检查：$i=5$时$8=8$，$i=4$时$7=7$，$i=3$时$6=6$，$i=2$时$4<5$；故第二位加1到5，后缀取6、7、8，答案$\boxed{\{2,5,6,7,8\}}$。Q6(d)(i)的10个3组合已列对，不另标为算法知识错误。

- **组合后继最小性的证明（minimality proof for next combination）** ：$i$为最右未顶格位置。候选把$a_i$加1，并令后续为连续最小整数，因此仍严格递增，末项不超过$n$。任意更大组合$b$的第一次分歧位置$p$不可能大于$i$，因为这些位置原本已达上限$n-r+p$；若$p<i$则$b$已超过候选，若$p=i$则$b_i\ge a_i+1$，相等时其后缀也不小于候选的连续最小后缀。因此候选是唯一最小的更大组合。

#### 全部枚举与不重不漏（Complete Enumeration without Repetition）

- **生成全部r排列（generate all r-permutations）** ：先遍历$\binom nr$个组合，每组内部再列r!个排列，总$P(n,r)$个，不重不漏，因为每个排列所属底集唯一。

  **这种分组输出不保证全部r排列整体按词典序** ，只保证组合组序及各组内部序。

- **不重不漏证明（completeness and uniqueness）** ：从最小对象开始，后继严格增加且是最小更大者，最大对象停；有限全序中因此恰遍历全部对象。不能只凭“数量对了”断言没重复没遗漏。

  组合特征位串的二进制顺序与递增元组词典序也须区别，不能混接两种后继。

---

## 五、递推关系的应用（Applications of Recurrence Relations）

### 5.1 建模与初始条件（Modeling and Initial Conditions）

#### 建模检查（Modeling Checks）

- **模型（model）** 先定义$a_n$数什么、单位是什么、n从哪里开始；再写初值、递推式与适用下标。每个分支须互斥且完备；删去／追加部分要能双向对应并保证接缝合法。

  求通项（find a closed form）与建立递推（form a recurrence）是不同任务。

- **候选解验证（verification of a candidate solution）** 直接代入并检查全部初值。

  例如$a_n=2a_{n-1}-a_{n-2}$允许$3n$与常数5，但不允许$2^n$，因为后者右侧是$3\cdot2^{n-2}$，不同于$4\cdot2^{n-2}$，任何n都不相等。

  初值$a_0=3,a_1=5$时，减法递推$a_n=a_{n-1}-a_{n-2}$给$a_2=2,a_3=-3$，不要看成加法。

- **复利（compound interest）** $S_n=(1+r)S_{n-1},S_0=P$得$P(1+r)^n$。时间单位、计息时刻改变时须重验下标。

### 5.2 兔子与汉诺塔（Rabbits and the Tower of Hanoi）

#### 兔子模型（Rabbit Model）

- **兔子繁殖（rabbit population）** ：设第1个月有一对幼兔，每对兔从出生后的第3个月起每月繁殖一对，且无死亡，$f_1=f_2=1$，$f_n=f_{n-1}+f_{n-2}$（$n\ge3$）。分为上月已有与本月新生，不能假定所有幼兔立即翻倍；

  不同月龄计数约定会改变初值。

#### 三柱汉诺塔（Three-peg Tower of Hanoi）

- **三柱汉诺塔（three-peg Tower of Hanoi）** ：n个大小不同圆盘，单次搬一个且大盘不能压小盘。把前$n-1$盘搬开、移动最大盘、再搬回小盘，得可行上界$H_n\le2H_{n-1}+1$；

  任何解移动最大盘前后都需搬开／恢复小盘，得同样下界，故$H_n=2H_{n-1}+1,H_0=0$，解为$2^n-1$。仅给构造不能证明最少（minimum）。

  64盘需$2^{64}-1$次，展示指数增长（exponential growth）。

### 5.3 受限位串（Restricted Bit Strings）

#### 禁止00与禁止000（Forbidding 00 and 000）

- **不含00（no consecutive zeros）** ：对$n\ge2$，末位为1的串删去1后对应任意合法$n-1$串；末位为0时倒数第二位必须为1，删去10后对应任意合法$n-2$串。因此$a_n=a_{n-1}+a_{n-2}$，$a_0=1$计唯一空串（empty string），$a_1=2$，得$1,2,3,5,8,13,\ldots$，$a_n=f_{n+2}$。

  两类互斥且覆盖全部合法串；后缀1或10均以1开头，接在任意合法前缀后仍合法。只在合法短串后任添0会产生非法接缝，不能两类均算$a_{n-1}$。不含11的计数可通过0、1互换得到同型递推。

- **不含000（no three consecutive zeros）** ：按末尾连续0的个数为0、1、2分类，分别得到后缀1、10、100；删去后缀后对应长度$n-1,n-2,n-3$的合法前缀。各后缀以1开头，追加时不会在接缝产生000，故$b_n=b_{n-1}+b_{n-2}+b_{n-3}$，$b_0=1,b_1=2,b_2=4$，从$n=3$适用得$b_3=7,b_4=13,b_5=24,b_6=44$。

  若采用$b_1,b_2,b_3$作初值，则递推从$n=4$开始。

## 六、图论（Graph Theory）

> [!tip] 【老师强调：第19、21节】
> 第十章是期末重点；第21节还要求未在课堂逐个展开的例题自行练习。以下不凭“课堂跳过”删去某一节，也不把充分条件当充要条件。

### 6.1 图的类型与建模（Graph Types and Modeling）

#### 图的组成与类型（Components and Types of Graphs）

- **图（graph）** $G=(V,E)$由顶点集（vertex set）与边集（edge set）组成；顶点（vertex / node）表示对象，边（edge）表示联系。

  本文有限图题默认$V\ne\varnothing$；$E$可以为空。先定义两者的含义，再决定方向、重数、自环，不只看图形外观。推广到零顶点图时需另声明约定，不能与“有顶点但没有边”的无边图（edgeless graph）混淆。

  有限图（finite graph）要求顶点集与边集都有限；任一集合无限则为无限图（infinite graph）。本课程的有限计数公式与算法均按有限图语境使用，不能只检查顶点数而忽略无限多重边的可能性。

| 类型（type） | 方向（direction） | 平行／多重边（parallel / multiple edges） | 自环（loop） |
|---|---|---|---|
| 简单图（simple graph） | 无向（undirected） | 不允许 | 不允许 |
| 多重图（multigraph，本课程约定） | 无向 | 允许 | 不允许 |
| 伪图（pseudograph） | 无向 | 允许 | 允许 |
| 简单有向图（simple directed graph） | 有向（directed） | 不允许同向重弧 | 不允许 |
| 有向多重图（directed multigraph） | 有向 | 允许 | 允许 |
| 混合图（mixed graph） | 有向、无向并存 | 按模型 | 按模型 |

![[C10.1-原图-同一批机房的三种建模.png|550]]

图解：同一批机房可建成简单图、多重图或伪图：只记录是否连通、分别记录多条链路、再允许诊断自环，得到不同的边模型。

#### 方向、权重与模型（Direction, Weights and Models）

- **有向图（directed graph / digraph）** 用有序对表示弧（arc），$(u,v)$与$(v,u)$一般不同；无向图（undirected graph）端点无序。简单图（simple graph）无重边、自环，多重图（multigraph）允许重边，伪图（pseudograph）还允许自环；本课具体约定见前表。

- **带权图（weighted graph）** 为边附权重（weight），可表示路程、费用等；“有权”与“有方向”是不同维度。

![[C10-带权图一例.png|440]]

图解：同样从$a$到$f$，红路线用3条边、权重和为12，绿路线用4条边、权重和为7；数边得到的长度与边权总和要分清。

- **有向边的端点（endpoints of a directed edge）** ：$(u,v)$中$u$是起点（initial vertex）、$v$是终点（terminal / end vertex）；$u$邻接到$v$（$u$ is adjacent to $v$），$v$邻接自$u$（$v$ is adjacent from $u$），不推出反方向。

### 6.2 度、图族与二分图（Degrees, Graph Families and Bipartite Graphs）

#### 邻接、度与握手定理（Adjacency, Degree and Handshaking）

- **邻接（adjacency）** 指两顶点由边相连；关联（incidence）指边以某点为端点（endpoint）。邻域／邻点集（neighborhood / neighbor set）$N(v)$含其邻接顶点，$N(S)=\bigcup_{v\in S}N(v)$。

- **度（degree）** $\deg v$数关联端点次数：重边逐条计，自环计2，故不总等于$|N(v)|$。孤立点（isolated vertex）度0，悬挂点／叶（pendant vertex / leaf）度1；最大／最小度（maximum / minimum degree）记$\Delta,\delta$。

![[C10-自环算两度.png|640]]

图解：每条普通边在两个端点各计1次，自环在同一点计2次。右例有7条边，三个顶点的度为5、5、4，度和14恰为$2|E|$。

- **握手定理1（handshaking theorem 1）** ：有限无向图$\sum_v\deg v=2|E|$，重边、自环均适用。证明：逐边计关联端点，每边恰贡献2。10个点均6度时，$2e=60$，故$e=30$。

- **握手定理2（handshaking theorem 2）** ：奇度顶点（odd-degree vertex）数为偶。证明：度和为偶，减去所有偶度项仍为偶；奇数项之和要为偶，其项数只能是偶。不是说每个顶点都偶度。

![[C10.2-握手定理计数示意.png|640]]

图解：左边逐条边数端点，右边逐个顶点数度；两种方式都得到$3+2+3+2=10=2\times5$。

#### 有向度与标准图族（Directed Degrees and Standard Families）

- **有向图入度（in-degree）** $\deg^-(v)$与出度（out-degree）$\deg^+(v)$分别数进入与离开的弧，自环各贡献1；$\sum_v\deg^-v=\sum_v\deg^+v=|E|$。

![[C10.2-原图-有向图入度出度.png|520]]

图解：沿箭头分别数入度和出度；自环同时贡献一个入度和一个出度，孤立顶点$f$两者都为0。

| 图族（graph family） | 点数v | 边数e | 度与补充 |
|---|---|---|---|
| 完全图（complete graph）$K_n$ | n | $n(n-1)/2$ | 每点$n-1$ |
| 圈图（cycle graph）$C_n$，$n\ge3$ | n | n | 每点2 |
| 轮图（wheel graph）$W_n$，本书由$C_n$加中心 | $n+1$ | $2n$ | 中心n，轮缘各3 |
| n维超立方体（n-cube / hypercube）$Q_n$ | $2^n$ | $n2^{n-1}$（$n\ge1$） | n正则，位串差一位相邻 |
| 完全二分图（complete bipartite graph）$K_{m,n}$ | $m+n$ | mn | 两侧度分别n、m |

- **轮图下标与低阶边界（wheel indices and low-order cases）** ：$W_n$的下标$n$表示轮缘点数，不包括中心；有些文献用$W_{n+1}$表示同一对象。上表的简单圈与轮图均取$n\ge3$。若另定义$C_1$为带一个自环的单点、$C_2$为以两条平行边相连的两点，再加中心与辐条可得到相应的$W_1,W_2$；这些低阶图须按实际边和自环计数，不能套用简单图条件。自环两端是同一顶点，无法分到二分划分的两侧，因此带自环的$C_1$不二分，也不能作合法顶点着色。$Q_0$为单点，$Q_{n+1}$由两份$Q_n$逐一连对应顶点构造，等价于位串恰差一位相邻。

- **标准图族的结构定义（structural definitions of standard graph families）** ：

  | 图族（family） | 构造／邻接规则（construction / adjacency rule） |
  |---|---|
  | 完全图（complete graph）$K_n$ | $n$个顶点的每一对不同顶点之间恰有一条边 |
  | 圈图（cycle graph）$C_n$，$n\ge3$ | 顶点$v_1,\ldots,v_n$，仅有$v_iv_{i+1}$及$v_nv_1$，首尾相接成一个圈 |
  | 轮图（wheel graph）$W_n$，$n\ge3$ | 在$C_n$外加一个中心，并把中心与全部$n$个圈上顶点相连 |
  | 超立方体（hypercube）$Q_n$ | 顶点为全部$n$位二进制串；两顶点恰好一位不同才相邻 |
  | 完全二分图（complete bipartite graph）$K_{m,n}$ | 两侧分别有$m,n$点，同侧无边，每一对跨侧顶点之间都有一条边 |

  点边数或度数表不能代替结构定义；例如多个不交圈同样每点度2，却不是单个$C_n$。

![[C10.2-原图-完全图Kn.png|640]]

图解：完全图$K_1$至$K_6$：每一对不同顶点都相连。边的交叉处没有顶点标记，就不另算顶点。

![[C10.2-原图-圈Cn.png|640]]

图解：圈图$C_3$至$C_6$：只把相邻顶点首尾相连，每个顶点度2；画成圈不表示还要补上对角线。

![[C10.2-原图-轮Wn.png|640]]

图解：轮图$W_3$至$W_6$：由轮缘$C_n$加一个中心构成。本课下标$n$只数轮缘顶点，所以$W_4$有5个顶点、8条边。

![[C10.2-原图-超立方体Qn.png|640]]

图解：超立方体$Q_1,Q_2,Q_3$：二进制标签恰差一位才相邻。例如$000$的邻点是$001,010,100$；$Q_3$有6个方形面。

![[C10.2-原图-完全二分图Kmn.png|640]]

图解：完全二分图：同侧不连边，跨侧全部相连。$K_{3,3}$有6个顶点、9条边；纸上的边交叉不算新顶点。

- **握手定理的证明要点（proof of the handshaking theorems）** ：无向图按顶点数关联端点，每边贡献2，故$\sum\deg v=2e$，减去偶度项后奇度项的和为偶，奇度项个数也必偶。有向图每条弧恰贡献一次出度和一次入度，得两总和均为$e$；自环仍满足这些端点计数。

- **完全有向图（complete directed graph）** 的每对不同顶点之间两个方向的弧均存在，无自环时有$n(n-1)$条弧；不能与无向$K_n$的$n(n-1)/2$边混算。

#### 二分图的判定（Bipartite Tests）

- **二分图（bipartite graph）** 的顶点可划为不交的$V_1,V_2$，所有边均跨两侧；$(V_1,V_2)$称二分划分（bipartition）。简单图二分，当且仅当能用至多两色使邻点异色。证明：划分两侧各染一色，反向按颜色分组即可。

- **标准图族的二分性（bipartiteness of standard families）** ：$C_n$（$n\ge3$）当且仅当$n$偶时二分；沿圈交替染色，奇圈末点会与起点冲突。含三角形的图不二分；$K_{m,n}$同侧无边、跨侧全连，是完全二分图（complete bipartite graph），边数$mn$。没有边的非空二分图只需1色，不能无条件写色数2。

![[C10.2-原图-二分图两例.png|640]]

图解：左图$G$可划为$\{a,b,d\}$与$\{c,e,f,g\}$，每条边均跨两侧；右图$H$含三角形$a,b,f$，不能用两色使邻点异色。画法杂乱不妨碍二分，关键是实际邻接关系。

### 6.3 图的运算、补图与度序列（Graph Operations, Complements and Degree Sequences）

#### 子图与图运算（Subgraphs and Graph Operations）

- **子图（subgraph）** $H=(W,F)$满足$W\subseteq V,F\subseteq E$且边端点都在W中；生成子图（spanning subgraph）保留全部顶点；

  真子图（proper subgraph）是与原图不同的子图，即至少删了一个顶点或一条边；生成子图也可能是真子图。

- **并图（union of graphs）** 取点边集合并，交图（intersection）取交。

- **不交并（disjoint union）** 记作$G\sqcup H$：先在需要时给顶点改名，使$V_G\cap V_H=\varnothing$，再取$G\sqcup H=(V_G\cup V_H,E_G\cup E_H)$。两图各保留一份，图间不加边；原来即使有同名顶点，也保留为不同顶点，不合并。

  点数$v_G+v_H$，边数$e_G+e_H$，各顶点的度不变。例如$K_2\sqcup K_2$是两条互不相连的边，共4个顶点、2条边、2个连通分量。

- **联图（join of graphs）** $G+H$在不交并基础上加上全部跨图边：点$v_G+v_H$、边$e_G+e_H+v_Gv_H$，G侧顶点度加$v_H$，H侧加$v_G$。

![[C10.2-原图-并图与G1G2.png|640]]

图解：并图保留两图顶点与边的集合并；相同标签视为同一顶点，共有的边只保留一次，不额外添加跨图边。

- **笛卡尔积图（Cartesian product of graphs）** $G\square H$的顶点集为$V_G\times V_H$，每个顶点是有序对$(g,h)$。对简单无向图，$(g,h)$与$(g',h')$相邻，当且仅当$g=g'$且$hh'\in E_H$，或$h=h'$且$gg'\in E_G$；即一个坐标不变、另一个坐标沿原图的一条边移动。

  点数$v_Gv_H$，边数$e_Gv_H+e_Hv_G$；$\deg(g,h)=\deg_Gg+\deg_Hh$。例如两条边$a-b$与$1-2$的积图有$(a,1),(a,2),(b,1),(b,2)$四个顶点，构成一个正方形；$(a,1)$与$(b,2)$不相邻，因为两个坐标同时改变。$Q_{r+s}\cong Q_r\square Q_s$。

> [!tip] 【老师强调：第20节转写约L501–521】
> 老师说很可能在图的运算这里出期末题，尤其join与Cartesian product，但随后明确未承诺一定作为题目。手算应同时会画图、算点边数、算新度数。

![[C10-join与笛卡尔积.png|650]]

#### 补图、自补图与方形子图（Complements, Self-complementarity and Square Subgraphs）

- **补图（complement）** $\overline G$与$G$同点集，在不同顶点原来不邻接时连边：$e(\overline G)=\binom v2-e(G)$、$\deg_{\overline G}x=v-1-\deg_Gx$。$G\cup\overline G=K_v$；例如$\overline{C_4}=2K_2$，$\overline{K_{m,n}}=K_m\cup K_n$。

- **自补图（self-complementary graph）** 满足$G\cong\overline G$。$C_4$与其补图不相同构，$C_5$与其补图同构；要给保持邻接的双射，不是图画相像即可。

![[C10.3-课件-C4与C5的补图.png|650]]

图解：上排$C_4$的补图只有两条互不相接的边，所以不同构；下排$C_5$的补图画成五角星，但沿边走仍是一个5圈，重新对应顶点即可与$C_5$同构。交叉处没有增加顶点。 来源：[[Ch10.3.pdf#page=2|Ch10.3.pdf · PDF p2，slide 7]]。

- **立方体的方形子图（square subgraphs of a cube）** ：$Q_3$有6个$Q_2$方形面，不能只数投影画法中的内外两个框。

#### 度序列（Degree Sequences）

- **度序列（degree sequence）** 将各点度按非增顺序列出，例如顶点度依次为$(2,3,2,2,0,1)$时，度序列为$(3,2,2,2,1,0)$。握手定理要求总和偶；简单图还须每项$\le v-1$。这些仅为必要条件，不能据此直接判可实现。

- **重边对度序列的影响（effects of parallel edges on degree sequences）** ：$(5,5,4)$在3点简单图不可实现，但允许重边可取前两点间3条边、它们到第三点各2条边。因此同一序列能否实现，取决于是否允许重边、自环等图类型条件。

### 6.4 图同构（Graph Isomorphism）

#### 同构的定义、排除与证明（Defining, Refuting and Proving Isomorphism）

- **图同构（graph isomorphism）** 为顶点双射$f:V_G\to V_H$，同时保留邻接与非邻接，简单图写$uv\in E_G\iff f(u)f(v)\in E_H$；有向图还须保持方向，多重图保持重数和自环。

  图相等（equality of graphs）要求标签相同，同构允许改名。同构本身是等价关系。

- **同构不变量（isomorphism invariant）** ：点数、边数和度序列在同构下保持不变；任一不同即不同构，全部相同仍不足以证明同构。$C_6$与$C_3\cup C_3$同为6点6边2正则却不同构，构成只检查这三项时的“魔鬼对（devil's pair）”反例。

- **证明同构须给完整双射并核对边与非边** 。双射$f$确定后逐条验证$uv\in E_G\iff f(u)f(v)\in E_H$；只试一次对应失败，不能证明不存在其他对应。

![[C10.3-课件-同构的完整双射.png|650]]

图解：取$f(a)=3,f(b)=1,f(c)=2,f(d)=4$。5条边逐一映为右图的5条边，唯一非边$bc$也映为非边$12$，所以这是完整的同构证明。 来源：[[Ch10.3.pdf#page=2|Ch10.3.pdf · PDF p2，slide 6]]。

  验证给定双射只需多项式比较，暴力找映射可达$v!$个候选。

![[C10.3-同构即重排行列.png|620]]

### 6.5 路径、连通性与树（Paths, Connectivity and Trees）

> [!warning] 【考试注意：术语约定】
> 本提纲采用以下术语约定：path允许重复，simple path要求顶点不重复；只要求边不重复的路线称为迹（trail）。有些教材将simple path用于不重复边的路线，因此做题时须先明确使用哪种约定；题目另有定义时按题目定义。
>
> 树中的“无圈”排除真正的简单圈，不把同一条无向边立即往返当作圈。哈密顿回路仅允许末尾复写起点。

#### 路径与连通性的语言（Language of Paths and Connectivity）

- **路径（path）** 是相邻顶点组成的序列，长度（length）等于边数，允许重复；简单路径（simple path）要求所有顶点不同。回路（circuit / cycle）为正长度闭合路径；简单圈（simple cycle）除首尾相同外顶点互异。无向单边往返不作为树中的圈。

![[C10.4-原图-路径判读一例.png|470]]

图解：沿原图的边检查顶点序列；例如$a\to b\to c\to f$长度为3，且顶点不重复，是本课约定下的简单路径。

- **连通（connected）** ：无向图任意两点有路径；连通分量（connected component）是极大连通部分。重复顶点段可删除，故有路径就有简单路径。强连通（strongly connected）要求有向图每对点双向可达；弱连通（weakly connected）只要求去方向后连通。

![[C10.4-原图-连通与分量.png|640]]

图解：$G_1$连通，$G_2$分成两个连通部分；右图$H$有3个连通分量$H_1,H_2,H_3$，不能把同一分量里的不同路径另算成分量。

![[C10.4-原图-强弱连通两例.png|510]]

图解：左图$G$含经过所有顶点的有向回路，强连通；右图$H$去方向后连通，但$a$没有出边，不能从$a$到其他顶点，所以只弱连通。

- **无环（acyclic）** ：没有圈；有向无环图（directed acyclic graph, DAG）无有向圈，去方向后可能有无向圈，不能混淆。

![[C10-DAG判三例.png|640]]

图解：中图没有有向圈，是DAG，但去掉箭头后出现无向圈；右图存在有向圈。检查DAG必须沿箭头走，不能只看轮廓。

#### 极小性、树与生成树（Minimality, Trees and Spanning Trees）

- **极小／极大（minimal / maximal）** 总是相对于具体性质：极小连通图（minimally connected graph）删任一边就不连通，是树；

  极大无圈图（maximal acyclic graph）若仍可加边连不同分量则不极大，固定非空点集时极大无圈即树。极大不等于最大（maximum），定义性质不能省略。

- **树（tree）** 为连通、无圈的简单无向图；森林（forest）为无圈图，可有多个分量。n点树有$n-1$边，任意两点间唯一不重复顶点路径；每边是桥；n≥2时至少两个叶。

  n点k分量森林有$n-k$边。对有限无向简单图，“连通且n−1边”“无圈且n−1边”“两点间唯一路径”均刻画树。

- **生成树（spanning tree）** 保留原图全部顶点、选边形成树；连通当且仅当有生成树，通常不唯一；非连通图只能取生成森林（spanning forest）。

  最小生成树（minimum spanning tree, MST）是在连通带权无向图的所有生成树中，使边权总和最小者。树先要覆盖全部顶点、连通且无圈，再比较权重；“极小连通”指不能删边，“最小权”指总权最优，二者不同。例如同一图的两棵生成树总权分别为22和31，则前者权重更小；但要证明其为最小生成树，仍须排除权重小于22的其他生成树。

![[C10-树与两个反例.png|600]]

![[C10-生成树不唯一.png|640]]

图解：同一张5点图可选出不同的生成树；两种选法都保留全部5个顶点、恰选4条边、连通且无圈。

![[C10.4-课件-生成树与最小权比较.png|650]]

图解：先检查是否覆盖全部顶点、连通且无圈，再比较总权重。右上生成树总权22，右下总权31；“是生成树”还不足以说明“是最小生成树”。 来源：[[Ch10.4.pdf#page=4|Ch10.4.pdf · PDF p4，slide 14]]。

- **树定理的证明要点（proofs of the tree theorems）** ：

  - 至少两叶：有限且至少两点的树取一条最长的不重复顶点路径。端点若有路径外邻点可延长路径；若另接路径内非相邻点则造圈，均矛盾。因此两个端点度都为1。
  - 边数$n-1$：$n=1$时零边；$n>1$剪掉一片叶及其唯一边，余图仍连通无圈，按归纳假设有$n-2$边，加回该边得$n-1$。
  - 唯一路径：连通保证存在；若两条不重复顶点路径不同，沿首次分歧到再次相遇的部分组成圈，违背无圈。反过来，若有圈，圈上两点有两条不同路径，违背唯一性。
  - 生成树存在：连通图若有圈，从圈中删一条边不破坏连通；不断删到无圈，仍保留所有顶点，得到生成树。

  这些等价刻画按有限非空无向简单图、且“不重复顶点路径”的约定使用；允许来回走同一边的走法不会唯一。

#### 桥（Bridges）

- **桥／割边（bridge / cut edge）** 删去后使连通分量数增加；等价于该边不在任何圈上。使用Fleury算法时，桥要在“尚未走过边组成的剩余图”中重新判断。

![[C10.4-原图-割点与割边.png|500]]

图解：边$ce$是连接左右两部分的唯一通道，删去它后分量数增加，因而是桥；圈上的边可沿圈绕行，不是桥。

### 6.6 欧拉与哈密顿（Euler and Hamilton）

| 概念（concept） | 恰好一次的对象 | 首尾 |
|---|---|---|
| 欧拉路径／欧拉迹（Euler path / Euler trail） | 每条边 | 开放版本起终点不同 |
| 欧拉回路（Euler circuit / Euler tour） | 每条边 | 相同 |
| 哈密顿路径（Hamilton path / Hamiltonian path） | 每个顶点 | 一般不同 |
| 哈密顿回路（Hamilton circuit / Hamiltonian cycle） | 每个顶点，终点复写起点仅表示闭合 | 相同 |

#### 欧拉与哈密顿的区别（Euler versus Hamilton）

- **欧拉与哈密顿（Euler and Hamilton）** ：欧拉路线恰好走每条边一次，可重复点；哈密顿路线恰好经过每个顶点一次，闭合时仅最后复写起点。柯尼斯堡七桥问题（Königsberg bridge problem）有4个奇度点，不能一笔走完。

![[C10.5-原图-七桥与多重图.png|640]]

图解：陆地区域作顶点、每座桥各作一条边，得到多重图；四个顶点度数均为奇数，不满足欧拉路径的0或2个奇度点条件。

- **欧拉图（Eulerian graph）的术语约定** ：本提纲将“连通且有欧拉路径”的图称为Eulerian，包括开放欧拉路径与欧拉回路两种情形。也有文献将Eulerian专用于有欧拉回路的图，因此答题时写清具有“Euler path”还是“Euler circuit”。哈密顿图（Hamiltonian graph）通常指有哈密顿回路。

![[C10.5-欧拉与哈密顿的区别.png|660]]

图解：同一张图，左边的欧拉回路用尽9条边，可多次经过同一顶点；右边的哈密顿回路经过6个顶点各一次，允许留下3条边不用。

- **Icosian游戏（Icosian puzzle）** 问十二面体骨架是否有经过各顶点一次的回路；十二面体有12个面、20个顶点，不能把面数当顶点数。

![[C10.5-原图-十二面体环游.png|640]]

图解：左图的立体骨架可重画成中图；右图蓝色路线经过全部20个顶点一次后回到起点，是哈密顿回路。

- **多重图中的边身份（edge identities in multigraphs）** ：路线需记$e_1,\ldots,e_r$及顶点序列，只写顶点不能区分平行边；不同平行边各走一次合法，同一条边重复两次不合法。

#### 欧拉判据及证明（Euler Criteria and Proof）

- 无向图有边时，先检查非孤立部分连通；有欧拉回路当且仅当所有度偶，有开放欧拉路径当且仅当恰两个奇度点，起终点必须是这两点。若题目把欧拉回路也算路径，则“有欧拉路径”的条件应写奇度点数0或2。

  空边图的零长度情形另按题目约定。

- **必要性（necessity）** 靠每个中途顶点的进出配对；充分性（sufficiency）先走一个闭回路，若还有未用边，找已有回路上仍接未用边的点另走子回路并拼接，直到用完所有边。

#### 求欧拉路线的算法（Algorithms for Euler Routes）

- **Fleury算法（Fleury's algorithm）** ：输入满足欧拉判据的无向图；0个奇度点可从任意非孤立点开始，2个奇度点从其中一个开始。每步在剩余图中选当前点关联的未走边，优先非桥；仅当无其他选择时才走桥。走过即删边并移动到另一端，直到所有边删完停止，记录的边序列即欧拉路线。

  手算须画出或更新剩余图，桥的身份会改变；开头检查0／2奇度和连通性，不能在不满足条件的图上照走后声称算法成功。

- **Hierholzer算法（Hierholzer's algorithm）** ：回路情形先从非孤立点$v$沿未用边走到回到$v$；若尚有未用边，找当前路线上的点$u$仍接未用边，从$u$再走一个闭回路，把新回路在$u$处接入旧路线；重复到所有边用尽。偶度保证不会在起点以外提前无边可走，连通性保证有剩边就有可拼接点。

  回路拼接例：$a\to d\to f\to a$与$d\to b\to e\to c\to d$，再接$f\to b\to c\to g\to e\to f$，得到$a\to d\to b\to e\to c\to d\to f\to b\to c\to g\to e\to f\to a$。检查每条原边恰出现一次。

![[C10.5-原图-拼接子回路.png|640]]

图解：另看这张原图：先走$a\to f\to c\to b\to a$，剩下三角形$cde$；在$c$处插入$c\to d\to e\to c$，得$a\to f\to c\to d\to e\to c\to b\to a$，7条边各走一次。

![[C10-Fleury为什么不能先走桥.png|620]]

#### 哈密顿回路的充分条件（Sufficient Conditions for Hamilton Circuits）

> [!info] 【历年考过：第21节转写L681附近】
> 老师明确说两年前期末用过哈密顿路径题。画出一条合法路线即可证存在；未找到路线不算证明不存在，要给排除理由或穷举论证。

- **Dirac定理（Dirac's theorem）** ：n≥3的简单图若$\delta\ge n/2$，则有哈密顿回路；Ore定理（Ore's theorem）：每对不相邻u、v都有$\deg u+\deg v\ge n$，则有哈密顿回路。

  Dirac条件蕴涵Ore条件；二者均充分非必要，$C_5$两者都不满足却本身有哈密顿回路。n奇时度的整数门槛是$\lceil n/2\rceil$。

![[C10.5-原图-哈密顿路径三例.png|640]]

图解：$G_1$有哈密顿回路$a\to b\to c\to d\to e\to a$；$G_2$有哈密顿路径$a\to b\to c\to d$，但$a$的度为1，不能形成哈密顿回路。$G_3$的3个叶子都必须成为路径端点，而一条路径只有两个端点，所以无哈密顿路径。

### 6.8 平面图、欧拉公式与不可平面障碍（Planarity, Euler's Formula and Obstructions）

#### 可平面与平面嵌入（Planarity and Plane Embeddings）

- **可平面图／平面图（planar graph）** 指 **存在** 一种无边交叉的平面画法；平面嵌入图／平图（plane graph）指已经给定的无交叉画法。现在画得有交叉不能否定可平面，重画或同构重排可能消除交叉；

  边在共同端点相会不算交叉。$K_4,Q_3$可平面，$K_5,K_{3,3}$不可平面。

  在原本交叉的两条边之间加一个新顶点，会改变顶点与邻接关系，得到的是另一张图；不能这样把交叉“改成端点”来证明原图可平面。合法重画须保留原图的点边关联。

![[C10.7-原图-K4与Q3的平面表示.png|640]]

图解：$K_4$与$Q_3$各有一幅交叉画法和一幅无交叉画法。移动顶点、弯曲边能消除交叉，同时保持原有邻接；这才证明原图可平面。

> [!info] 【历年考过：第22节转写L398附近】
> 老师在平面图与不交叉论证附近提到过去期末出过题，不能据此把本次具体题型写死。应会从定义分辨planar与plane、统计面并使用定理。

#### 面、欧拉公式与边数界（Faces, Euler’s Formula and Edge Bounds）

- **面／区域（face / region）** 由嵌入划开，外部无界面（unbounded / exterior face）也算一个；

  边界（boundary）围住面，面度（degree of a face）按边界边出现次数计，不按不同边集合大小。桥在同一面边界走两次，自环可围成面。

- **欧拉公式（Euler's formula）** ：连通平面图$v-e+f=2$。树只围一个面，代入$e=v-1$一致；从树逐条加闭圈边，每次e和f各加1；

  删桥减少连通性时不能沿用“面数必减1”的分支。

- **面度和（sum of face degrees）** $\sum_F\deg(F)=2e$，因为每边有两侧；桥同面计两次。度和式$\sum_v\deg v=2e$数顶点端点，两式各自的计数对象不同。

![[C10.7-原图-面与面度.png|610]]

| 平面性结论（planarity result） | 适用条件与推法 |
|---|---|
| $e\le3v-6$ | 简单可平面图，v≥3；连通证明由每面至少3条边与欧拉式得到 |
| 存在度≤5的点 | 简单可平面图；若每点度≥6则与边数上界矛盾，不能误写成“所有点度≤5” |
| $e\le2v-4$ | 简单、无三角形（triangle-free）、可平面，v≥3；二分图满足无三角形条件 |
| $K_5$不可平面 | v=5,e=10，违反$10\le9$ |
| $K_{3,3}$不可平面 | v=6,e=9且二分，违反$9\le8$ |

- **欧拉公式的归纳证明要点（inductive proof of Euler's formula）** ：连通树有$e=v-1,f=1$，等式成立；若图有圈，删去圈上一条非桥边，顶点与连通性不变、边数和面数各减1，等式保持。反复删到树即可证明原图公式。也可用加边归纳：$v=1,e=0,f=1$成立；从一条边开始，保持当前子图连通，每步添一条原图中的边。若引入一个新顶点，则$v,e$各加1、$f$不变；若两端都已有，则边在某个面的内部将它一分为二，$e,f$各加1、$v$不变。两种情况均保持$v-e+f=2$，直至得到原连通图。

#### 必要条件与不可平面障碍（Necessary Conditions and Obstructions）

- **以上边数不等式是必要条件（necessary conditions）** ，通过不能证明可平面。Petersen图v=10,e=15通过两条数值上界仍不可平面；

  要证存在可给无交叉嵌入，要证不存在可找结构障碍。$K_{2,5}$可平面且$e=2v-4=10$，两侧都至少3时才含$K_{3,3}$。

![[C10.7-不等式可行区域.png|640]]

图解：$K_5$与$K_{3,3}$分别违反相应边数界，可据此排除；Petersen图满足两条数值界却仍不可平面，说明通过不等式不等于证明可平面。

- **细分（subdivision）** 在边上插入度2新点；两图同胚（homeomorphic）指可由同一图的细分得到。细分与逆操作在合法条件下保持可平面性，但一般不保持同构。

  压缩度2点（suppressing a degree-two vertex）时要说明选中的子图及支路，不能让新路径共享内部顶点后还称标准细分。

![[C10.7-原图-同胚细分三例.png|640]]

图解：在一条边上插入度2点只把它拆成一条支路；各图可通过细分得到共同的结构，因而同胚，但顶点数不同的图不会同构。

- **Kuratowski定理（Kuratowski's theorem）** ：有限图不可平面，当且仅当含有同构于$K_5$或$K_{3,3}$某个细分的子图。不是必须直接含未细分的$K_5/K_{3,3}$。

  操作为选支点（branch vertices）→删无关点边→找内部不交支路（internally disjoint paths）→抑制度2点→核对完整邻接。Petersen图可由此证明非平面。

![[C10.7-原图-Petersen细分障碍.png|610]]

### 6.9 图着色、色数及资源分配（Graph Coloring, Chromatic Number and Resource Allocation）

#### 着色定义与最优性（Coloring and Optimality）

- **合法顶点着色（proper vertex coloring）** 为每点赋色且邻点异色；k着色（k-coloring）表示至多用k种颜色。

  色数／顶点色数（chromatic number）$\chi(G)$是最少用色数。非空无边图色数1；空顶点图常约定0。有自环时不能合法顶点着色，通常讨论简单图；重边不增加新的不同色约束。

- 求精确色数必须双向证明：给一个k着色证$\chi\le k$，再证明k−1色不够以证$\chi\ge k$。加边不会降低色数，删边不会提高；不同连通分量可复用颜色，整体色数取最大，不是相加。

- **色数达到顶点数的充要条件（characterization of graphs with chromatic number equal to their order）** ：有$n\ge1$个顶点的有限简单图满足$\chi(G)=n$，当且仅当$G\cong K_n$。

  证明要点：完全图的任意两点相邻，必须用$n$色；反过来，若不是完全图，存在不相邻的$u,v$，给它们同一色，其余$n-2$点各用一个新色，就得到$n-1$着色，与$\chi(G)=n$矛盾。因此非完全的$n$点简单图满足$\chi(G)\le n-1$，但不一定恰好等于$n-1$。

![[C10.8-原图-三色与四色两组着色.png|640]]

图解：左图含三角形，又给出了3着色，故$\chi(G)=3$；右图给出4着色，直接说明$\chi(H)\le4$，要认定等号还须证明3色不够。画出一种着色与证明最少用色是两个步骤。

#### 地图与标准图族的着色（Coloring Maps and Standard Graph Families）

- **地图着色（map coloring）** 把区域作顶点、共享一段边界的区域连边，仅在单点接触不算相邻；冲突图／地图对偶图（conflict graph / dual graph）将相邻限制转成边。

  一般平面图的几何对偶（geometric dual）可能有重边或桥对应的自环；用于区域异色的冲突图应去掉无实际不同区域约束的自环，不混淆这两种建图约定。

| 图 | 色数（chromatic number）及理由 |
|---|---|
| $K_n$ | n，任意两点冲突 |
| 有边的二分图／$K_{m,n}$（m,n≥1） | 2，两侧各一色 |
| $C_n$，n≥3 | n偶为2，n奇为3 |
| $W_n$，n≥3 | n偶为3，n奇为4；中心需一个轮缘未用色 |
| $Q_n$，n≥1 | 2；$Q_0$为1 |
| 非平凡树（nontrivial tree） | 2，按与根距离奇偶染色 |

![[C10.8-地图到冲突图到着色.png|620]]

#### 资源分配模型（Resource Allocation Models）

- **排考（exam scheduling）** ：点为课程，有共同学生就连边，颜色为时段。例如7门课程的冲突图中有完全子图$\{1,2,3,4\}$，故至少4时段；$\{1,6\},\{2\},\{3,5\},\{4,7\}$给4时段可行表，故最少4。证明最优须兼有下界与可行安排。

- **登机口分配（gate assignment）** ：点为航班，占用时间重叠就连边，颜色为登机口；若三个航班两两占用时间重叠，便至少需要3个登机口；再给出一个使用3个登机口的完整安排，才能证明最少恰为3。排考同理：四门课程的冲突图若含三角形且能给出3着色，则最少需3个时段，不能作二着色。

![[C10-六个航班三个登机口.png|660]]

图解：占用表转为冲突图，再把同色航班安排到同一登机口。$A,D,F$两两冲突，至少需3口；图中的3色安排给出可行方案，因此最少恰为3。

#### 团与色数下界（Cliques and Lower Bounds on the Chromatic Number）

- **团／完全子图（clique / complete subgraph）** 的顶点两两相邻，团数（clique number）$\omega(G)$为最大团大小。若含$K_k$子图，则$\chi(G)\ge k$，因为其中各点须异色；这一下界不总取等，$C_5$为例。

## 七、来源、考试证据与勘误（Sources, Examination Evidence and Corrections）

### 7.1 小节覆盖对照（Section Coverage Map）

下表用于从知识条目回查分节笔记；表中编号是本提纲编号。各节参考资料集中列于7.7，详细范围与历史核对记录见7.5–7.6。

> [!info]- 展开对照表
> | 原笔记（source note） | 正文落点 | 核对范围（coverage） |
> |---|---|---|
> | [[C1.1 命题逻辑 Propositional Logic]] | 1.1 | 命题、联结词、条件翻译、真值表、优先级与按位运算 |
> | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] | 1.2 | 翻译、规约一致性、骑士与无赖 |
> | [[C1.3 命题等价 Propositional Equivalences]] | 1.3 | 永真／矛盾／偶然式、逻辑等价律及等价推导 |
> | [[C1.4 谓词与量词 Predicates and Quantifiers]] | 1.4；1.5 | 谓词与论域、自由／约束变量、量词分配与否定、唯一性 |
> | [[C1.5 嵌套量词 Nested Quantifiers]] | 1.5 | 量词顺序、有限展开、exactly one/two、量词移动与依赖 |
> | [[C1.6 推理规则 Rules of Inference]] | 1.6 | 有效性、命题与量化推理规则、归结、谬误与作业纠错 |
> | [[C1.7 证明导论 Introduction to Proofs]] | 1.7 | 直接／逆否／反证／等价证明、奇偶性与平方根无理性 |
> | [[C1.8 证明方法与策略 Proof Methods and Strategy]] | 1.8 | 分情况、穷举、存在唯一性与归纳法前置知识 |
> | [[C2.1 集合 Sets]] | 2.1 | 集合语言、包含／属于、空集、幂集、笛卡尔积与真值集 |
> | [[C2.2 集合运算 Set Operations]] | 2.2 | 集合运算、二／三集合容斥与特征位串 |
> | [[C2.3 函数 Functions]] | 2.3 | 定义域／陪域／像、单满双射、单调、逆与复合、阶乘 |
> | [[C2.4 序列与求和 Sequences and Summations]] | 2.4 | 序列、递推初值、复利与迭代 |
> | [[C2.6 矩阵 Matrices]] | 2.6；3.3 | 矩阵记号、布尔并交／积／幂及可达性 |
> | [[C9.1 关系及其性质 Relations and Their Properties]] | 3.1 | 关系性质、集合运算、复合／幂及其证明、逆与补 |
> | [[C9.2 n 元关系与数据库 n-ary Relations and Their Applications]] | 3.2 | 多元关系、度／域、记录／属性与键、选择／投影／连接 |
> | [[C9.3 关系的表示 Representing Relations]] | 3.3 | 矩阵／有向图转换、判性质、并交逆、布尔复合与幂 |
> | [[C9.4 关系的闭包 Closures of Relations]] | 3.4 | 闭包最小性、三闭包、路径／幂、有限上界、Warshall及闭包次序 |
> | [[C9.5 等价关系 Equivalence Relations]] | 3.5 | 等价关系、同余、等价类、划分与商集 |
> | [[C9.6 偏序 Partial Orderings]] | 3.6 | 偏序／严格序、全序、字典序、Hasse图、极值／界、格与对偶 |
> | [[C6.1 计数基础 The Basics of Counting]] | 4.1 | 加乘减除、补集／容斥、基础模型与圆排列 |
> | [[C6.2 鸽巢原理 The Pigeonhole Principle]] | 4.2 | 普通／广义鸽巢、阈值反问题、生日、奇数核、Ramsey与子序列 |
> | [[C6.3 排列与组合 Permutations and Combinations]] | 4.3 | 排列／组合、端点、组合数算法、位串／彩票／分组、捆绑／插空与圆桌 |
> | [[C6.4 二项式系数与恒等式 Binomial Coefficients and Identities]] | 4.4 | 二项式系数恒等式、Pascal三角、Vandermonde、曲棍球棒及组合证明 |
> | [[C6.5 广义排列与组合 Generalized Permutations and Combinations]] | 4.5 | 重复选择、星条、上下界解、重物排列、四类盒子、Stirling与整数分拆 |
> | [[C6.6 生成排列与组合 Generating Permutations and Combinations]] | 4.6 | 三个后继算法、位串／子集对应、r排列、不重不漏及复杂度 |
> | [[C8.1 递推关系的应用 Applications of Recurrence Relations]] | 5.1–5.3 | 递推验证与初值、兔子／复利／汉诺塔、禁止00／000位串 |
> | [[C10.1 图与图模型 Graphs and Graph Models]] | 6.1 | 图类型、有限图、建模时的方向／重边／自环选择、图与关系 |
> | [[C10.2 图的术语与特殊类型 Graph Terminology and Special Types of Graphs]] | 6.2–6.3 | 邻接／度、握手、标准图族、二分、图运算、补图与度序列 |
> | [[C10.3 图的表示与图同构 Representing Graphs and Graph Isomorphism]] | 6.4 | 同构定义、点边数与度序列不变量、构造与验证同构双射 |
> | [[C10.4 连通性 Connectivity]] | 6.5 | 路径、连通分量、强弱连通、树／森林、生成树、MST与桥 |
> | [[C10.5 欧拉路径与哈密顿路径 Euler and Hamilton Paths]] | 6.6 | 欧拉判据与Fleury／Hierholzer算法、哈密顿路径及Dirac／Ore定理 |
> | [[C10.7 平面图 Planar Graphs]] | 6.8 | planar／plane、面／面度、Euler公式、边数界、细分／同胚与Kuratowski定理 |
> | [[C10.8 图着色 Graph Coloring]] | 6.9 | 顶点／地图着色、图族色数、排考等资源分配、团下界 |

章节汇总入口：[[C1 基础：逻辑与证明 MOC]]、[[C2 基本结构：集合、函数、序列、求和与矩阵 MOC]]、[[C9 关系 Relations MOC]]、[[C6 计数 Counting MOC]]、[[C8 高级计数技巧 Advanced Counting Techniques MOC]]、[[C10 图 Graphs MOC]]。

作业来源与历史批改：[[C1 作业与错题]]、[[C2 作业与错题]]、[[作业与错题 MOC]]、[[前两轮练习总结与知识错题]]、[[第6章计数卷总结与知识错题]]。

### 7.2 课堂考试证据索引（Classroom Examination Evidence Index）

> [!info]- 展开对照表
> | 正文标记 | 原始出处（original source） | 证据适用范围 |
> |---|---|---|
> | 时间、时长、楼号疑点 | [[第二十二节课_9b942d34-已合并.txt\|第二十二节课_9b942d34-已合并]]开头L12–40附近；对应同名SRT开场 | 11月19日8:50–10:50，楼名两种识别保留疑点；取QQ群正式通知 |
> | 第1章约一题，其余以期中后为主 | [[第十七节课-已合并.txt\|第十七节课-已合并]]约00:04:00–00:06:10，L108–165附近 | 原话保留“可能／约一题”的语气，不凭此删除第一章 |
> | 英文试卷与英文词汇 | [[第十八节课-已合并.txt\|第十八节课-已合并]]L492–543附近；[[第十二节-已合并.txt\|第十二节-已合并]]L43–55附近 | 第18节提醒期末英文术语，第12节说明学院英文作答要求 |
> | 教材与作业题源 | [[1-8节课-已合并.txt\|1-8节课-已合并]]第1节考试说明；[[第十二节-已合并.txt\|第十二节-已合并]]L102附近；[[第十三节课-已合并.txt\|第十三节课-已合并]]开头 | 例题、课后题与作业变形，不只课堂逐字讲过的句子 |
> | 每步写依据，T/F勿作普通变元 | [[1-8节课-已合并.txt\|1-8节课-已合并]]及[[9-11节课-已合并.txt\|9-11节课-已合并]]；原C1汇总“答题规范”与§1.3补充 | 规则名或公式均可；等价推导／证明步骤应交代理由 |
> | Warshall要手算 | [[第十五节课-已合并.txt\|第十五节课-已合并]]L1692–1701或重复识别段L4503附近 | 老师直接提到final examination、by hand、one element by element |
> | 下一个排列算法明确预告 | [[第十九节课-已合并.txt\|第十九节课-已合并]]00:38:36–00:39:40 | “我一定会考这个算法”；其他生成算法一并复习，但不把每个变体都说成逐项承诺 |
> | 图运算很可能出题 | [[第二十节课_f4ff9771-已合并.txt\|第二十节课_f4ff9771-已合并]]L501–521附近 | join／Cartesian product、运算及度；老师同时说未承诺必出 |
> | 图论为期末重点 | [[第二十一节课_233dd011-已合并.txt\|第二十一节课_233dd011-已合并]]L1198附近；第19节相关说明 | 章级重点，不把章内每个定理都视为逐项考试承诺 |
> | 哈密顿路径历年考过 | [[第二十一节课_233dd011-已合并.txt\|第二十一节课_233dd011-已合并]]L681附近 | 两年前试题，不是本次必考预告 |
> | 平面图部分历年出题 | [[第二十二节课_9b942d34-已合并.txt\|第二十二节课_9b942d34-已合并]]L398附近 | 过去出题经历，保留上下文，不猜本次原题 |
> | 第一章的历年与期中预告 | [[C1 基础：逻辑与证明 MOC]]考试说明；对应[[1-8节课-已合并.txt\|1-8节课-已合并]] | 永真式、有限量词展开、奇数平方直接证明为历年；翻译／推导明确预告针对期中 |

转写存在同一节重复识别，TXT行号仅辅助定位；若与SRT时间轴相比，优先按话语内容核对。“本节常考”“最可能考法”等只有笔记判断时，不标成老师亲口承诺。

“§9.2与§9.3只出小问”目前仅追溯到章节汇总，本提纲未据此承诺题量。

### 7.3 勘误与适用条件记录（Corrections and Conditions）

> [!info]- 展开对照表
> | 来源中的问题 | 提纲采用的表述及位置 |
> |---|---|
> | C1.5量词移动处有前后不同公式，另把蕴涵前件强弱说反 | 1.5区分两种量词前件公式，明确非空域、自由变量与依赖条件 |
> | C1汇总把“EI必须先UI”写成绝对顺序 | 1.6仅对需要同一存在见证的综合证明建议先EI，不作一切证明的普遍顺序 |
> | C1.6课堂“不行”的提醒易被误读为逻辑推论本身错误 | 1.6说明最终表达式的推导不能省；从子结论补足合法引入步骤即可 |
> | C9汇总称传递关系高次幂都等于平方 | 3.1给出$R^2\ne R^3$反例；只有自反且传递才保证各正幂等于R |
> | C8.1称$2^n$在n=2碰巧满足候选递推 | 5.1直接算两端，说明没有该特例 |
> | C10.5轮图哈密顿回路只指外圈，漏中心 | 6.6将中心插入外圈相邻两点之间 |
> | C10.5 K(m,n)开放欧拉路径表漏K(1,1) | 6.6补全$K_{1,1}$只有开放欧拉路径的边界 |

本轮另补的来源勘误：

| 原笔记问题 | 正文采用的条件或结论 |
|---|---|
| C2.4按右侧出现前项的“项数”决定初值数 | 2.4按最大滞后与递推起始下标检查，给出$a_n=a_{n-5}$反例 |
| C2.3把“非严格单调”笼统判为不单射 | 2.3改为“不保证单射”；严格单调的定义与证明分别写清 |
| C9.6旁注称一般偏序反向后未必仍是偏序 | 3.6明确任意偏序的对偶仍为偏序；任意格的对偶仍为格 |
| C9.6将覆盖关系恢复原序不加有限性限制 | 3.6限定本课Hasse算法为有限偏序，给出有理数稠密序反例 |
| C10.4把森林必须定义成不连通 | 6.5按无圈图定义，允许一棵树也是森林 |

这里仅列出与保留内容相关的勘误，原笔记未改动；完整历史记录见逐项核对表。

### 7.4 历史修订记录（Previous Revisions）

前几轮的全量核对与修补记录见[[离散数学期末复习逐项核对表 Final Review Coverage]]，不再在本提纲重复列出。

### 7.5 逐项核对入口（Item-by-item Audit）

原笔记出处、逐项检查和历史修订记录见[[离散数学期末复习逐项核对表 Final Review Coverage]]；本提纲只保留当前复习内容。

### 7.6 当前范围说明（Current Review Scope）

已删去此前标为“拓展”的整节、条目、局部补充及配套图示；混合条目中属于复习范围的部分保留。原笔记和历史批改文件保留完整内容。

4.3“分组与相邻约束”的基础方法及4.5沿用现有范围安排。小节和个人错题编号沿用旧编号，便于对照已有练习；删节后的编号可能不连续。

各节参考PDF入口见7.7，材料范围核对记录见[[离散数学期末复习逐项核对表 Final Review Coverage#本轮课件范围核对（Current Courseware Scope Audit）|范围核对记录]]。

### 7.7 各节参考资料（References by Section）

> [!info]- 参考PDF入口
> | 正文小节 | 参考资料 |
> |---|---|
> | [[#1.1 命题、联结词与真值表（Propositions, Connectives and Truth Tables）\|1.1]] | [[Ch1.1_Part1.pdf\|Ch1.1_Part1.pdf]]、[[Ch1.1_Part2.pdf\|Ch1.1_Part2.pdf]]、[[Ch1.1_Part3.pdf\|Ch1.1_Part3.pdf]]、[[Ch1.2.pdf\|Ch1.2.pdf]] |
> | [[#1.2 翻译、规约与逻辑谜题（Translation, Specifications and Logic Puzzles）\|1.2]] | [[Ch1.1_Part3.pdf\|Ch1.1_Part3.pdf]]、[[Ch1.2.pdf\|Ch1.2.pdf]] |
> | [[#1.3 逻辑等价律（Logical Equivalence Laws）\|1.3]] | [[Ch1.2.pdf\|Ch1.2.pdf]]、[[Ch1.3.pdf\|Ch1.3.pdf]] |
> | [[#1.4 谓词、论域与单层量词（Predicates, Domains and Quantifiers）\|1.4]] | [[Ch1.4_Part1.pdf\|Ch1.4_Part1.pdf]]、[[Ch1.4_Part2.pdf\|Ch1.4_Part2.pdf]] |
> | [[#1.5 嵌套量词与精确数量（Nested Quantifiers and Exact Cardinalities）\|1.5]] | [[Ch1.4_Part2.pdf\|Ch1.4_Part2.pdf]]、[[Ch1.5_Part1.pdf\|Ch1.5_Part1.pdf]]、[[Ch1.5_Part2.pdf\|Ch1.5_Part2.pdf]] |
> | [[#1.6 推理规则与有效性（Rules of Inference and Validity）\|1.6]] | [[Ch1.6_Part1.pdf\|Ch1.6_Part1.pdf]]、[[Ch1.6_Part2 (1).pdf\|Ch1.6_Part2 (1).pdf]] |
> | [[#1.7 证明的基本方法（Basic Proof Methods）\|1.7]] | [[Ch1.6_Part3.pdf\|Ch1.6_Part3.pdf]]、[[Ch1.6_Part4.pdf\|Ch1.6_Part4.pdf]] |
> | [[#1.8 分情况、存在唯一性与证明策略（Cases, Existence, Uniqueness and Strategies）\|1.8]] | [[Ch1.6_Part5.pdf\|Ch1.6_Part5.pdf]] |
> | [[#2.1 集合的基本语言（Basic Set Language）\|2.1]] | [[Ch2.1.pdf\|Ch2.1.pdf]] |
> | [[#2.2 集合运算与位串表示（Set Operations and Bit-string Representation）\|2.2]] | [[Ch2.2.pdf\|Ch2.2.pdf]] |
> | [[#2.3 函数及其运算（Functions and Their Operations）\|2.3]] | [[Ch2.3_Part1.pdf\|Ch2.3_Part1.pdf]]、[[Ch2.3_Part2.pdf\|Ch2.3_Part2.pdf]] |
> | [[#2.4 序列与递推预备（Sequences and Recurrence Prerequisites）\|2.4]] | [[Ch8.1.pdf\|Ch8.1.pdf]] |
> | [[#2.6 矩阵记号与布尔运算（Matrix Notation and Boolean Operations）\|2.6]] | [[Ch9.1_Part1.pdf\|Ch9.1_Part1.pdf]]、[[Ch9.1_Part3.pdf\|Ch9.1_Part3.pdf]]、[[Ch9.3_Part2.pdf\|Ch9.3_Part2.pdf]] |
> | [[#3.1 二元关系的性质与运算（Properties and Operations of Binary Relations）\|3.1]] | [[Ch9.1_Part1.pdf\|Ch9.1_Part1.pdf]]、[[Ch9.1_Part2 (1).pdf\|Ch9.1_Part2 (1).pdf]]、[[Ch9.1_Part3.pdf\|Ch9.1_Part3.pdf]] |
> | [[#3.2 多元关系与数据库（n-ary Relations and Databases）\|3.2]] | [[Ch9.2.pdf\|Ch9.2.pdf]] |
> | [[#3.3 矩阵与有向图表示（Matrix and Digraph Representations）\|3.3]] | [[Ch9.1_Part1.pdf\|Ch9.1_Part1.pdf]]、[[Ch9.1_Part2 (1).pdf\|Ch9.1_Part2 (1).pdf]]、[[Ch9.1_Part3.pdf\|Ch9.1_Part3.pdf]] |
> | [[#3.4 闭包与Warshall算法（Closures and Warshall's Algorithm）\|3.4]] | [[Ch9.3_Part1.pdf\|Ch9.3_Part1.pdf]]、[[Ch9.3_Part2.pdf\|Ch9.3_Part2.pdf]] |
> | [[#3.5 等价关系、等价类与划分（Equivalence Relations, Classes and Partitions）\|3.5]] | [[Ch9.5.pdf\|Ch9.5.pdf]] |
> | [[#3.6 偏序、Hasse图与格（Partial Orders, Hasse Diagrams and Lattices）\|3.6]] | [[Ch9.6.pdf\|Ch9.6.pdf]] |
> | [[#4.1 基本计数原理（Basic Counting Principles）\|4.1]] | [[Ch6.1.pdf\|Ch6.1.pdf]]、[[Ch6.5.pdf\|Ch6.5.pdf]] |
> | [[#4.2 鸽巢、拉姆齐与子序列（Pigeonhole, Ramsey and Subsequences）\|4.2]] | [[Ch6.2.pdf\|Ch6.2.pdf]]、[[Ch6.2&Ch6.3.pdf\|Ch6.2&Ch6.3.pdf]] |
> | [[#4.3 排列、组合与约束（Permutations, Combinations and Constraints）\|4.3]] | [[Ch6.2&Ch6.3.pdf\|Ch6.2&Ch6.3.pdf]]、[[Ch6.5.pdf\|Ch6.5.pdf]] |
> | [[#4.4 二项式系数与组合证明（Binomial Coefficients and Combinatorial Proofs）\|4.4]] | [[Ch6.2&Ch6.3.pdf\|Ch6.2&Ch6.3.pdf]] |
> | [[#4.5 重复选择、物体分配与整数分拆（Repetition, Distribution and Integer Partitions）\|4.5]] | [[Ch6.5.pdf\|Ch6.5.pdf]] |
> | [[#4.6 生成排列与组合的算法（Algorithms for Generating Permutations and Combinations）\|4.6]] | [[Ch6.6.pdf\|Ch6.6.pdf]] |
> | [[#5.1 建模与初始条件（Modeling and Initial Conditions）\|5.1]] | [[Ch8.1.pdf\|Ch8.1.pdf]] |
> | [[#5.2 兔子与汉诺塔（Rabbits and the Tower of Hanoi）\|5.2]] | [[Ch8.1.pdf\|Ch8.1.pdf]] |
> | [[#5.3 受限位串（Restricted Bit Strings）\|5.3]] | [[Ch8.1.pdf\|Ch8.1.pdf]] |
> | [[#6.1 图的类型与建模（Graph Types and Modeling）\|6.1]] | [[Ch10.1.pdf\|Ch10.1.pdf]] |
> | [[#6.2 度、图族与二分图（Degrees, Graph Families and Bipartite Graphs）\|6.2]] | [[Ch10.2.pdf\|Ch10.2.pdf]] |
> | [[#6.3 图的运算、补图与度序列（Graph Operations, Complements and Degree Sequences）\|6.3]] | [[Ch10.2.pdf\|Ch10.2.pdf]]、[[Ch10.3.pdf\|Ch10.3.pdf]] |
> | [[#6.4 图同构（Graph Isomorphism）\|6.4]] | [[Ch10.3.pdf\|Ch10.3.pdf]] |
> | [[#6.5 路径、连通性与树（Paths, Connectivity and Trees）\|6.5]] | [[Ch10.4.pdf\|Ch10.4.pdf]]、[[Ch10.5.pdf\|Ch10.5.pdf]] |
> | [[#6.6 欧拉与哈密顿（Euler and Hamilton）\|6.6]] | [[Ch10.5.pdf\|Ch10.5.pdf]] |
> | [[#6.8 平面图、欧拉公式与不可平面障碍（Planarity, Euler's Formula and Obstructions）\|6.8]] | [[Ch10.7.pdf\|Ch10.7.pdf]] |
> | [[#6.9 图着色、色数及资源分配（Graph Coloring, Chromatic Number and Resource Allocation）\|6.9]] | [[Ch10.8.pdf\|Ch10.8.pdf]] |

> [!info]- 例题与术语的具体来源
> - 分类、存在与唯一：[[Ch1.6_Part5.pdf#page=4|Ch1.6_Part5 · PDF p4，slide 16]]。
> - 分组、相邻约束与圆桌排列：[[Ch6.5.pdf#page=2|Ch6.5 · PDF p2，slide 5]]；容斥：[[Ch6.1.pdf#page=3|Ch6.1 · PDF p3–4]]。
> - 帕斯卡恒等式：[[Ch6.2&Ch6.3.pdf#page=4|Ch6.2&Ch6.3 · PDF p4，slides 13–14]]。
> - 整除偏序判格的反例：[[Ch9.6.pdf#page=9|Ch9.6 · PDF p9，slide 34]]。
