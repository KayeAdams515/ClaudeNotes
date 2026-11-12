# 离散数学期末复习提纲（Discrete Mathematics Final Review Outline）

本提纲以仓库 `pdfs/补充课件/` 中全部41份PDF的实际内容界定授课范围，共228页；逐页读取文字并核看公式、表格、图示及重传版本差异。教材小节名、目录预告和旧笔记标签均不单独决定范围。

范围内保留定义、定理条件与结论、证明要点和手算步骤；理解这些内容必需的记号与前置定义也保留。范围外内容在原章节压缩为要点，并标注 **【拓展】** ，不再与授课内容使用相同篇幅。完整来源与本轮范围处理见[[离散数学期末复习逐项核对表 Final Review Coverage]]。

> [!info] 范围与考试提醒
> 本次按你的要求，以补充课件作为实际授课范围。**【拓展】表示未在这些课件中独立讲解** ，不据此断言考试绝不会涉及。老师的考试预告、答题语言和手算要求继续按原课堂证据保留，不能将历史提醒反过来扩大本次课件范围。
>
> 同一小节可以同时有授课内容和拓展。关系矩阵、布尔积／幂虽无独立Ch2.6课件，却在Ch9.1、Ch9.3中实际出现；MST定义虽出现，也不意味着最短路算法已授。

## 考试信息与标记说明（Examination Information and Labels）

| 项目 | 已有课堂证据与复习动作 |
|---|---|
| 时间（time） | 第22节宣布11月19日8:50–10:50，时长120分钟；按本学期日历为2026年11月19日（周四）。转写后文把星期重复识别成Wednesday，不据此改日期。 |
| 地点（venue） | 第22节转写分别出现“53A 210”和“F3A210”，均指二楼210。楼名存在转写歧义，须以QQ群正式通知核对，不能把机器转写当作确定楼号。 |
| 范围（scope） | 第17节说明以期中后的第2、9、6、8、10章为主，第1章约保留一道题；第21节再次明确图论是期末重点。这里保留第1章；范围内内容完整，范围外按本次课件规则压缩并标拓展。 |
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
| [[#二、集合、函数、序列与矩阵（Sets, Functions, Sequences and Matrices）\|二、基本结构]] | 集合、函数、取整、序列、可数性与矩阵 |
| [[#三、关系（Relations）\|三、关系]] | 六种性质、闭包、Warshall、等价类、偏序与格 |
| [[#四、计数（Counting）\|四、计数]] | 鸽巢、排列组合、恒等式、分配与后继算法 |
| [[#五、递推关系的应用（Applications of Recurrence Relations）\|五、递推]] | 汉诺塔、位串、码字、卡特兰数与动态规划 |
| [[#六、图论（Graph Theory）\|六、图论]] | 建模、运算、同构、连通、欧拉／哈密顿、最短路、平面与着色 |

按考试证据确定先后时，可优先回看 **4.6生成算法、3.4手算Warshall、6.3图运算及整个第六部分** ；这只是复习时间分配建议，不缩小本提纲的知识范围。

---

## 一、逻辑与证明（Logic and Proofs）

### 1.1 命题、联结词与真值表（Propositions, Connectives and Truth Tables）

授课依据：[[Ch1.1_Part1.pdf|Ch1.1_Part1.pdf]]、[[Ch1.1_Part2.pdf|Ch1.1_Part2.pdf]]、[[Ch1.1_Part3.pdf|Ch1.1_Part3.pdf]]、[[Ch1.2.pdf|Ch1.2.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

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

- **【拓展】相容或与异或的附加恒等式（additional inclusive OR and XOR identities）** ：$p\lor q$允许两者同时真，$p\oplus q$要求恰好一个真。异或满足交换律、结合律，$p\oplus\mathbf F\equiv p$、$p\oplus\mathbf T\equiv\neg p$、$p\oplus p\equiv\mathbf F$，因此重复异或同一项会消去。

#### 【拓展】广义逻辑与自指（Generalized Logic and Self-reference）

- **【拓展】模糊逻辑（fuzzy logic）** 用$[0,1]$真值；本笔记的否定、合取、析取分别取$1-v$、min、max，用于模糊控制（fuzzy control），不能直接当概率。

- **【拓展】自指（self-reference）与悖论（paradox）** ：说谎者悖论（liar paradox）不能一致赋经典真值；理发师悖论（barber paradox）与罗素悖论（Russell's paradox）揭示规则可能矛盾。自指、对角化（diagonalization）也用于停机问题的论证。

#### 术语层次与计算应用（Terminology and Computing）

- **命题逻辑／命题演算（propositional logic / propositional calculus）** 把完整陈述作原子；命题变元也称语句变元／布尔变量（statement / Boolean variable）。否定是一元运算符（unary operator），其余基本联结词为二元运算符（binary operator）；双条件也称双蕴涵（bi-implication）。

- **【拓展】对象语言与元语言（object language and metalanguage）** 分别指公式本身和谈论公式的语言；掩码（mask）、位并行（bit-parallel）、位图索引（bitmap index）用位运算筛选或编码，快速傅里叶变换（fast Fourier transform, FFT）也有相关位处理。

- **【拓展】异或应用（XOR applications）** ：$a\oplus b\oplus b=a$，即模2加法（addition modulo 2）。一次一密（one-time pad）用$c=m\oplus k$，要求密钥独立均匀、等长且仅用一次；CRC（cyclic redundancy check）与RAID（redundant array of independent disks）用它作奇偶校验（parity check）。

- **【拓展】布隆过滤器（Bloom filter）** 用位数组与哈希作允许假阳性的成员判断；二值神经网络（binary neural network, BNN）可用位运算及置位计数（population count / popcount）。XOR非线性可分（not linearly separable），单个线性感知机（linear perceptron）不能表达。

### 1.2 翻译、规约、谜题与电路（Translation, Specifications, Puzzles and Circuits）

授课依据：[[Ch1.1_Part3.pdf|Ch1.1_Part3.pdf]]、[[Ch1.2.pdf|Ch1.2.pdf]]。课件有规约、位运算及真话／假话谜题；检索、泥孩子、电路为拓展。

#### 翻译与一致性（Translation and Consistency）

- **自然语言翻译（translation）** ：先定义原子命题，再判断充分／必要／唯一等限制，最后定联结词与括号。不要把日常语境中暗含的双条件擅自加入只说“if”的数学题。

- **系统规约（system specification）** 是一组要求；一致性（consistency）指所有规约存在同一组满足赋值（satisfying assignment），不是每条分别可真。

  合取后找一组赋值即证一致；要证不一致（inconsistency），须推出矛盾或说明所有赋值均失败。加规约可能破坏一致性，删规约不能把一致系统变成不一致。

#### 检索与逻辑谜题（Search and Logic Puzzles）

- **骑士与无赖（knights and knaves）** ：课件用Batman代表总说真话者、Joker代表总说假话者。设$K_A$为“A说真话”，发言内容为$S_A$，自洽条件为$K_A\leftrightarrow S_A$，对各人联立。

  课件例：A说“B是Batman”，B说“两人类型不同”。若A为真话者，则B也为真话者，却不能真的类型不同，矛盾；故A为Joker，B也为Joker，此时两句均假而自洽。一般题可有唯一解、多解或无解；“我是无赖”在固定两类规则下无解。

- **【拓展】布尔检索（Boolean search）** 以AND、OR、NOT组合检索条件；谋杀案（murder puzzle）和美女与老虎（the lady or the tiger）也可建成逻辑约束。间谍／常人（spy / normal）可真可假，不能套骑士的双条件。

- **【拓展】泥孩子问题（muddy children puzzle）** ：公开公告（public announcement）建立共同知识（common knowledge）。在标准同步回答、人人正确推理的条件下，恰$m$人有泥，则前$m-1$轮无人知道，第$m$轮有泥者同时知道；对$m$归纳即可。知识逻辑（epistemic logic）研究这类状态变化，并联系分布式共识（distributed consensus）与多智能体系统（multi-agent systems）。

#### 【拓展】逻辑电路（Logic Circuits）

- **【拓展】逻辑门（logic gate）** 包括反相器（inverter / NOT gate）、与门（AND gate）、或门（OR gate）；组合电路（combinational circuit）输出仅依赖当前输入。沿信号流写中间子式，或按语法树（syntax tree）由内向外造电路；Shannon将布尔代数用于开关电路。

> [!info]- 【拓展】原图回看
> ![[C1-图2-组合电路示例.png|560]]

#### 【拓展】检索误差与电路化简（Retrieval Errors and Circuit Simplification）

- **【拓展】检索误差（retrieval errors）** ：假阳性（false positive）为误选，假阴性（false negative）为漏选；查准率（precision）是检出结果的相关比例，查全率（recall）是相关结果被检出的比例。语义检索（semantic retrieval）与检索增强生成（retrieval-augmented generation, RAG）为应用背景。

- **【拓展】电路化简（circuit simplification）** 中积之和（sum of products）对应DNF；小圆圈（bubble）表取反，扇出（fan-out）复用中间输出，公共子表达式消除（common subexpression elimination）减少重复。计算图（computational graph）与电路均可用DAG表示依赖。

### 1.3 等价律、范式与可满足性（Equivalence Laws, Normal Forms and Satisfiability）

授课依据：[[Ch1.2.pdf|Ch1.2.pdf]]、[[Ch1.3.pdf|Ch1.3.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

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

#### 【拓展】对偶与范式（Duality and Normal Forms）

- **【拓展】对偶（dual）** 互换$\land/\lor$、$\mathbf T/\mathbf F$，不改变元及否定号；等价式的对偶仍等价，二次对偶还原，称对合（involution）。对偶不等于否定。

- **【拓展】文字（literal）** 为变元或其否定；合取项（term）为文字合取，子句（clause）为文字析取。析取范式（disjunctive normal form, DNF）是项的析取，合取范式（conjunctive normal form, CNF）是子句的合取。真行造最小项后OR可得DNF；假行造仅在该行假的子句后AND可得CNF。

- **【拓展】否定范式（negation normal form, NNF）** 只用$\land,\lor,\neg$且否定只作用于变元；消箭头、用德摩根内移否定即可。NNF不要求已成DNF或CNF。

#### 【拓展】功能完备性（Functional Completeness）

- **【拓展】功能完备性（functional completeness）** 指可表达任意布尔函数（Boolean function）。DNF表示定理（DNF representation theorem）以每个真行的最小项（minterm）作OR证明$\{\neg,\land,\lor\}$完备；再用德摩根可去掉AND或OR之一。$n$变元有$2^{2^n}$个布尔函数，DNF最坏可有$2^n$项。

- **【拓展】与非（NAND / Sheffer stroke）** 和或非（NOR / Peirce arrow）各自完备：$p\mid p=\neg p$、$(p\mid q)\mid(p\mid q)=p\land q$；$p\downarrow p=\neg p$、$(p\downarrow q)\downarrow(p\downarrow q)=p\lor q$。它们交换但不结合。

- **【拓展】两层电路（two-level logic circuit）** 用AND后OR实现DNF；PLA（programmable logic array）、FPGA（field-programmable gate array）和LUT（lookup table）为实现背景。

#### 【拓展】SAT、数独与传播（SAT, Sudoku and Propagation）

- **【拓展】可满足性（satisfiability, SAT）** 指至少一个赋值为真；不可满足（unsatisfiable）即矛盾式，$P$永真当且仅当$\neg P$不可满足。可满足给见证（witness），不可满足须排除所有赋值；暴力枚举（brute-force enumeration）有$2^n$组。

- **【拓展】数独编码（Sudoku encoding）** 用$p(i,j,d)$表示填数，9阶数独729个变量；加入给定值（givens）、每行每列每块覆盖各数字、同格互斥等约束。一般$n^2\times n^2$需$n^6$个变量，满足约束不等于解唯一。

- **【拓展】单元传播（unit propagation）** 强制只剩一个文字的子句；传播停住不证明可满足。DPLL（Davis–Putnam–Logemann–Loveland）再分支与回溯；冲突驱动子句学习（conflict-driven clause learning, CDCL）从冲突学习子句并回跳。

- **【拓展】Cook–Levin定理（Cook–Levin theorem）** ：SAT为NP完全（NP-complete），即属NP且任意NP判定问题能多项式归约到它；若SAT有多项式算法则$P=NP$，不表示已证明$P\ne NP$。

### 1.4 谓词、论域与单层量词（Predicates, Domains and Quantifiers）

授课依据：[[Ch1.4_Part1.pdf|Ch1.4_Part1.pdf]]、[[Ch1.4_Part2.pdf|Ch1.4_Part2.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

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

- **【拓展】直言命题的四种形式（four categorical proposition forms）** ：A型全称肯定（universal affirmative）为$\forall x(A(x)\to B(x))$；E型全称否定（universal negative）为$\forall x(A(x)\to\neg B(x))$；I型特称肯定（particular affirmative）为$\exists x(A(x)\land B(x))$；O型特称否定（particular negative）为$\exists x(A(x)\land\neg B(x))$。O型“有的A不是B”与“并非所有A都是B”等价。

  A、E型本身不保证A存在；当A为空时可空真，不能据此推出对应的存在命题。

#### 【拓展】空论域（Empty Domains）

> [!warning] 【易错】
> $\neg\forall x(P(x)\to Q(x))\equiv\exists x(P(x)\land\neg Q(x))$，同时翻转量词和联结词；“没有人完美”与“并非人人完美”不能混写。

- **【拓展】空论域（empty domain）** 上全称为空真、存在为假；本课程通常默认论域非空。涉及删除空量词或移动量词时应保留该前提。

#### 【拓展】程序验证与逻辑程序（Verification and Logic Programming）

- **【拓展】程序验证（program verification）** 以执行前的前置条件（precondition）及执行后的后置条件（postcondition）描述正确性；部分正确性（partial correctness）不含终止保证，总正确性（total correctness）还要求终止。

- **【拓展】逻辑程序设计（logic programming / Prolog）** 用事实（fact）、规则（rule）、查询（query）表达知识，合一（unification）匹配表达式。符号人工智能（symbolic AI / GOFAI）、专家系统（expert system）、Datalog、答案集编程（answer set programming, ASP）及知识图谱推理（knowledge-graph reasoning）是相关应用；神经符号人工智能（neuro-symbolic AI）结合规则与学习，不能将学习预测当作演绎证明。

- **【拓展】声明式编程与验证（declarative programming and formal verification）** ：逻辑程序写关系和规则，不指定逐步控制流程；规则体的未定变量参与存在搜索（existential search）。元数学（metamathematics）研究证明系统本身，一阶逻辑（first-order logic）的一般问题不因某类Prolog查询可求解就都有终止算法。

### 1.5 嵌套量词与精确数量（Nested Quantifiers and Exact Cardinalities）

授课依据：[[Ch1.4_Part2.pdf|Ch1.4_Part2.pdf]]、[[Ch1.5_Part1.pdf|Ch1.5_Part1.pdf]]、[[Ch1.5_Part2.pdf|Ch1.5_Part2.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

#### 量词顺序与否定（Quantifier Order and Negation）

- **嵌套量词（nested quantifiers）** 逐层理解：$\forall x\exists yP(x,y)$中见证$y$可依赖$x$；

  $\exists y\forall xP(x,y)$要求固定一个$y$对所有$x$通用，后者蕴涵前者，反向一般不成立。同类量词可交换，异类量词不可随意交换。

  例如实数上$\forall x\exists y(x+y=0)$真，$\exists y\forall x(x+y=0)$假。

- **有限域嵌套展开（finite expansion）** ：$\forall x\exists yP(x,y)$按$x$合取、每项按$y$析取；不能把两层顺序颠倒。

> [!info] 【历年考过】
> 老师提到在$\{1,2,3\}$上展开此式曾作为期末题。

- 否定时逐层换$\forall/\exists$，最后否定谓词：$\neg\forall x\exists y\forall zP\equiv\exists x\forall y\exists z\neg P$。`every other`加$y\ne x$限制；

  `not necessarily`表示存在反例，不是处处相反。

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

- **【拓展】邻域独立与聚类系数（independent neighborhood and clustering coefficient）** ：课件的朋友语句$\exists x\forall y\forall z((F(x,y)\land F(x,z)\land y\ne z)\to\neg F(y,z))$属于范围内；将它解释为图中某点邻域独立，并以局部聚类系数（local clustering coefficient）$2e(N(x))/(d(x)(d(x)-1))$衡量邻居连边，是额外应用，$d<2$须另约定。

#### 量词移动与依赖（Quantifier Movement and Dependence）

- 若$A$中无$x$自由出现，则$(\exists xP(x))\to A\equiv\forall x(P(x)\to A)$，$(\forall xP(x))\to A\equiv\exists x(P(x)\to A)$（后式按非空域）。量词从蕴涵前件移出会翻转；

  从后件移出不翻转，并须满足变量不自由出现及论域条件。

> [!warning] 【易错】
> 两式一般不等价；不能套用普通同类量词交换。

- **【拓展】量化作嵌套循环（quantification as nested loops）** ：全称层找反例，存在层找见证；内层存在成功后可换下一个外层对象，但共同见证不能每次重选。

- **含独立命题的量词移动（moving quantifiers past an independent proposition）** ：假定论域非空，且$x$不自由出现在$A$中，下面八式均成立：

  | 联结词 | 全称量词（universal quantifier） | 存在量词（existential quantifier） |
  |---|---|---|
  | 合取（conjunction） | $\forall x(A\land P(x))\equiv A\land\forall xP(x)$ | $\exists x(A\land P(x))\equiv A\land\exists xP(x)$ |
  | 析取（disjunction） | $\forall x(A\lor P(x))\equiv A\lor\forall xP(x)$ | $\exists x(A\lor P(x))\equiv A\lor\exists xP(x)$ |
  | 量词在前件（quantifier in antecedent） | $(\forall xP(x))\to A\equiv\exists x(P(x)\to A)$ | $(\exists xP(x))\to A\equiv\forall x(P(x)\to A)$ |
  | 量词在后件（quantifier in consequent） | $A\to\forall xP(x)\equiv\forall x(A\to P(x))$ | $A\to\exists xP(x)\equiv\exists x(A\to P(x))$ |

  证明要点：先用$B\to C\equiv\neg B\lor C$消箭头，量词经过否定时翻转，再使用与独立命题的并交移动。量词位于蕴涵前件时翻转、位于后件时不翻转。若$x$自由出现在$A$里，不能照搬；空论域下也不能不加检查地照搬整张表。

#### 【拓展】分析与学习理论中的量词（Quantifiers in Analysis and Learning Theory）

- **【拓展】极限（limit）** 的量词次序为$\forall\varepsilon>0\exists\delta>0\forall x$；一致连续（uniform continuity）要求同一$\delta$适用于所有$x$。逐点收敛（pointwise convergence）的$N$可依赖$x$，一致收敛（uniform convergence）要求同一$N$适用于所有$x$，不能交换这两层量词。

- **【拓展】空量化规则（null quantification rule）** ：论域非空且$x$不自由出现在$A$中时，$\forall xA\equiv A\equiv\exists xA$。机器学习中的经验风险（empirical risk）与期望风险（expected risk）、泛化（generalization）及PAC学习（probably approximately correct learning）也涉及“所有样本／存在模型”等不同量词次序；不扩写相关理论。

- **【拓展】逐点连续（pointwise continuity）** 的$\delta$可依赖该点；一致连续则须对全部点统一。PAC学习还要区分样本量（sample size）、数据分布（data distribution）及误差、置信度；量词位置表达的是不同保证。

### 1.6 推理规则与有效性（Rules of Inference and Validity）

授课依据：[[Ch1.6_Part1.pdf|Ch1.6_Part1.pdf]]、[[Ch1.6_Part2 (1).pdf|Ch1.6_Part2 (1).pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

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
> 课堂提醒针对的是省略最终推导，不应解读为这条逻辑推论本身错误。

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

#### 归结与自动证明（Resolution and Automated Proof）

- **全称否定后件式（universal modus tollens）** ：由$\forall x(P(x)\to Q(x))$及$\neg Q(a)$，先UI得$P(a)\to Q(a)$，再MT得$\neg P(a)$。论证形式（argument form）用变元表达结构；肯定前件式也称分离律（law of detachment），归结产生的子句称归结式（resolvent）。

- **【拓展】归结反驳（resolution refutation）** 将命题前提与结论否定转为CNF，归结到空子句（empty clause）便证矛盾。命题归结具反驳完备性（refutation completeness）：有限CNF不可满足当且仅当能推出空子句；可靠性（soundness）保证不误推，完备性（completeness）不保证证明短。自动定理证明（automated theorem proving）搜不到证明也不等于目标为假。

### 1.7 证明的基本方法（Basic Proof Methods）

授课依据：[[Ch1.6_Part3.pdf|Ch1.6_Part3.pdf]]、[[Ch1.6_Part4.pdf|Ch1.6_Part4.pdf]]。Part3、Part4虽然文件名写1.6，实际讲教材证明方法；按内容归入本节。

#### 证明的语言与基础（Language and Foundations of Proof）

- **形式证明（formal proof）** 逐步遵循规则；非形式证明（informal proof）可合并显然步骤、使用已证结论，但仍必须给出有效理由。

  数学陈述常省略全称量词，证明时取“任意满足假设的对象”，不能只举几个例子。

- **【拓展】证明用语（proof terminology）** ：定理（theorem）／命题（proposition）／事实（fact）／结果（result）为已证明的结论；公理／公设（axiom / postulate）作为基础假设；

  引理（lemma）辅助证明；推论（corollary）直接由已有定理得到；猜想（conjecture）尚待证明或反驳。名称不改变逻辑地位。

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

- **证明方法的选用与互相改写（choosing and converting proof methods）** ：课堂建议先试直接证明，再试逆否证明，再试反证法；题目指定方法时按题目要求。

  已有$p\Rightarrow q$的直接证明，可在假设$p\land\neg q$后照原步骤推出$q\land\neg q$，改成反证法；已有$\neg q\Rightarrow\neg p$的逆否证明，可加上$p$后得到$p\land\neg p$，也改成反证法。两种间接证明（indirect proofs）的终点不同：逆否法明确推出$\neg p$，反证法只须得到矛盾。

- **【拓展】因子界与试除（factor bounds and trial division）** ：整数$n>1$若为合数（composite），存在素因子（prime factor）$p\le\sqrt n$；否则分解$n=ab$时两因子都大于$\sqrt n$将使$ab>n$。因此判定素数（prime number）只须试除到$\lfloor\sqrt n\rfloor$，也可只试其中的素数。1既不是素数也不是合数。


- **正整数因子的平方根界（square-root bound on factors）** ：若$n=ab$且$a,b>0$，则$a\le\sqrt n$或$b\le\sqrt n$。用逆否法：若$a>\sqrt n$且$b>\sqrt n$，则$ab>n$，不可能$n=ab$。课件的根号不能在转写中漏掉。

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

#### 【拓展】反例与错误证明（Counterexamples and Fallacious Proofs）

- **【拓展】空证明与平凡证明（vacuous and trivial proofs）** 分别证前件恒假、后件恒真；反例（counterexample）须满足全部前提而违反结论。错误证明（fallacious proof）常见除0、错误开方、增根（extraneous solution）、循环论证／窃取论题（circular reasoning / begging the question）。

- **【拓展】奇偶与有理性结论（parity and rationality results）** ：奇数为相邻平方差；有理数的和、积仍有理，非零有理数的倒数仍有理；无理数加有理数、乘非零有理数仍无理，两无理数的和或积则可能有理或无理。需按量词分别举例或反证。

- **【拓展】平均值论证（averaging argument）** 保证有限非空数列有项不小于平均值；否则求和矛盾。概率方法（probabilistic method）以正概率证明存在。圆排1至10的连续三数和重复计每数3次，平均16.5，故某组至少17。

- **【拓展】欧几里得引理（Euclid's lemma）** ：素数$p\mid ab\Rightarrow p\mid a$或$p\mid b$，可据此仿$\sqrt2$证明任意素数平方根无理。

- **【拓展】勒让德三平方和定理（Legendre's three-square theorem）** ：$n\ge0$可写为三个整数平方之和，当且仅当$n\ne4^a(8b+7)$（$a,b\ge0$整数）。7是三平方反例，3是两平方反例；四平方结论另见1.8。

#### 【拓展】估界、有理根与稠密性（Bounds, Rational Roots and Density）

- **【拓展】因子估界（bounding factors）** ：正数乘积$n=a_1\cdots a_k$至少一因子$\le n^{1/k}$；否则乘积大于自身。两因子的平方根界已在范围内证明方法处保留。

- **【拓展】有理根定理（rational root theorem）** ：整数系数多项式最简有理根$a/b$满足$a$整除常数项、$b$整除最高次系数；$x^3+x+1$的候选$\pm1$均非根。

- **【拓展】稠密性（density）** ：任意两实数间均有有理数和无理数；有理端点$r<s$间可取$r+(s-r)/\sqrt2$。稠密（dense）不等于不可数，$\mathbb Q$稠密仍可数。

### 1.8 分情况、存在唯一性与证明策略（Cases, Existence, Uniqueness and Strategies）

授课依据：[[Ch1.6_Part5.pdf|Ch1.6_Part5.pdf]]。Part5实际讲分类、穷举、存在与唯一；博弈、铺砌、深层数论另标拓展。

#### 分类与不失一般性（Cases and WLOG）

- **穷举证明（exhaustive proof）** 检验有限论域中的全部对象；分情况证明（proof by cases）将全部可能分成若干类，各证目标。逻辑依据是$(p_1\lor\cdots\lor p_k)\to q\equiv\bigwedge_i(p_i\to q)$，不可漏0、等号或其他边界。

- **课件穷举例（courseware exhaustive examples）** ：对$n=1,2,3,4$，$(n+1)^3$依次为$8,27,64,125$，$3^n$为$3,9,27,81$，故四个情形均满足严格大于。100以内完全幂（perfect power，底数为正整数、整数指数$>1$）为$1,4,8,9,16,25,27,32,36,49,64,81,100$，其中仅8、9相邻；这只证明有限范围。

- **课件分类例（courseware case proofs）** ：整数$n$满足$n^2\ge n$：$n\ge1$时$n^2\ge n\cdot1$；$n=0$时相等；$n\le-1$时$n^2>0>n$。课件一处写$n^2>n$应修正，因为0、1取等。

- **绝对值（absolute value）乘法证明** ：$|t|=t$（$t\ge0$）、$|t|=-t$（$t<0$）。当$(x,y)$符号分别为$(+,+),(-,+),(+,-),(-,-)$时，$|xy|$依次为$xy,-xy,-xy,xy$，均等于$|x||y|$；将0并入非负情形即可覆盖全部实数。

- **【拓展】不失一般性（without loss of generality, WLOG）** 依赖对称性（symmetry），不能任意假设$x\le y$。分段定义（piecewise definition）的最大／最小值（maximum / minimum）满足$\max(x,y)+\min(x,y)=x+y$，且$\max/\min=(x+y\pm|x-y|)/2$；三角不等式（triangle inequality）为$|x+y|\le|x|+|y|$。平方、四次方末位分别只能为$0,1,4,5,6,9$与$0,1,5,6$。

#### 存在、唯一与博弈策略（Existence, Uniqueness and Game Strategies）

- **存在性证明（existence proof）** 要证明$\exists xP(x)$；给出对象并验证即可。课件以$1729=10^3+9^3=12^3+1^3$证明同一正整数可有两种正立方和表示。

- **唯一性证明（uniqueness proof）** 有两部分：先证明存在，再证明任意两个满足者相等，不能把“至多一个”当“恰好一个”。课件例：若$a,b\in\mathbb R,a\ne0$，则$ar+b=0$有唯一实解。

  存在：取$r=-b/a$，代入得$a(-b/a)+b=0$。唯一：设$s$也是解，$as+b=ar+b=0$，相减得$a(s-r)=0$，由$a\ne0$得$s=r$。若$a=0$，则按$b=0$或$b\ne0$分别为无穷多解或无解，不能沿用唯一性结论。

> [!tip] 【课件要求：Ch1.6_Part5，PDF p4，slide 16】
> “DO NOT over simplify the proof”：写出存在与唯一两个部分，给必要理由，不能仅用“显然”替代关键推理。

- **【拓展】构造性与非构造性证明（constructive and nonconstructive proofs）** 区别在是否给出见证；经典无理数幂例将$r=(\sqrt2)^{\sqrt2}$分有理／无理两种情况，分别取$(a,b)=(\sqrt2,\sqrt2)$或$(r,\sqrt2)$，使无理数$a,b$满足$a^b$有理。

- **【拓展】Chomp游戏与策略窃取（Chomp and strategy stealing）** ：每步吃所选格及右下区域，左上毒格输；至少两格的矩形先手存在必胜策略。若先吃右下角后对手有制胜回应，先手可直接走该回应到同一局面，矛盾。取石子游戏（take-away game）每次取1至$m$且最后一颗胜时，$m+1$倍数为必败位置（losing / P-position），其余为必胜位置（winning / N-position）；倒推（backward induction）与极小化极大搜索（minimax search）为相关方法。

#### 【拓展】证明策略与不等式（Proof Strategies and Inequalities）

- **【拓展】正向／逆向推理（forward / backward reasoning）** 分别从假设向目标推、从目标找充分条件；改编证明（adapting a proof）须重验边界，反例搜索（searching for counterexamples）从0、负数、相等、空集着手。

- **【拓展】均值不等式（mean inequalities）** ：正数的调和、几何、算术、平方平均（harmonic / geometric / arithmetic / quadratic mean）满足HM≤GM≤AM≤QM，等号当两数相等。一般AM–GM对非负$a_i$给$\frac1n\sum a_i\ge(\prod a_i)^{1/n}$；等号当全部相等。非零实数$x$满足$x^2+x^{-2}\ge2$，等号$x=\pm1$。

- **【拓展】构造与估界后穷举（construction and bounding before exhaustion）** ：$m^2+1,\ldots,m^2+N$在$2m\ge N$时都是非平方；三个实数至少两个乘积非负。$n^2+n^3=100$在正整数无解；$2x^2+5y^2=14$在整数无解；$x^4+y^4=625$在正整数无解，均可先估界再检查有限候选。

- **【拓展】代数数与超越数（algebraic and transcendental numbers）** 分别是／不是非零整系数多项式的根。盖尔丰德–施奈德定理（Gelfond–Schneider theorem）：代数$a\ne0,1$、无理代数$b$使$a^b$超越；实幂取$a>0$。因此$2^{\sqrt2}$、$(\sqrt2)^{\sqrt2}$均超越。

- **【拓展】构造主义（constructivism）、直觉主义（intuitionism）** 不把任意经典存在证明当作已给见证算法；Curry–Howard对应（Curry–Howard correspondence）联系命题／类型、证明／程序，并联系依赖类型（dependent type）与Coq、Agda等证明助手（proof assistant）。

#### 【拓展】铺砌与不变量（Tilings and Invariants）

- **【拓展】铺砌与不变量（tilings and invariants）** ：骨牌（domino）各盖一黑一白，去对角两角的棋盘黑白数不同，不能铺；面积偶数或黑白平衡只给必要条件。将格子作点、相邻格连边，骨牌铺满等价于完美匹配（perfect matching）。

- **【拓展】三格骨牌（triomino）** 有直线形与L形；面积须为3倍数，直线块可用模3三色染色（three-coloring）排除部分缺角棋盘，不能照搬给L形。$2^k\times2^k$缺一格可用L形块按四象限和中心一块归纳铺砌。

> [!info]- 【拓展】原图回看
> ![[C1-图9-去掉左上和右下角的棋盘.png|360]]

#### 归纳法前置知识与【拓展】证明界限（Induction Prerequisite and Limits of Proof）

- **数学归纳法（mathematical induction）** 是后续课件证明所用的前置方法：先证基础步（base case）$P(n_0)$，再假设任意$k\ge n_0$的$P(k)$成立并证$P(k+1)$，才能推出所有$n\ge n_0$成立。关系幂、树边数和欧拉公式的具体证明保留在对应章。

- **【拓展】其他方法与数论背景（additional methods and number theory）** ：强归纳法（strong induction）可假设前面全部情形；结构归纳法（structural induction）沿基本对象与构造规则证明；康托尔对角线法（Cantor diagonalization）构造枚举外对象。拉格朗日四平方和定理（Lagrange's four-square theorem）称每个$n\ge0$是四个整数平方和；华林问题（Waring's problem）研究固定个数的$k$次幂表示，$g(4)=19$，79即说明18个四次方不足。

- **【拓展】素数与幂的背景（prime and power problems）** ：孪生素数猜想（twin prime conjecture）断言无穷多相差2的素数对；强哥德巴赫猜想（strong Goldbach conjecture）断言每个大于2偶数是两素数和。费马大定理（Fermat's Last Theorem）排除$n>2$、$xyz\ne0$的整数解$x^n+y^n=z^n$；Collatz猜想（Collatz conjecture，亦称$3x+1$/Hasse/Ulam/Syracuse/Kakutani问题）猜测按偶除2、奇乘3加1的轨迹都到1，有限计算不代替证明。

- **【拓展】欧拉数论定理（Euler's theorem in number theory）** ：$\gcd(a,m)=1,m\ge2$时$a^{\varphi(m)}\equiv1\pmod m$；欧拉函数（Euler's totient function）数与$m$互素的剩余数。勾股定理（Pythagorean theorem）为直角三角形$a^2+b^2=c^2$；勾股数组（Pythagorean triple）可取$(m^2-n^2,2mn,m^2+n^2)$，互素且奇偶相反的$m>n>0$给本原（primitive）数组。

- **【拓展】证明的界限（limits of proof）** ：哥德尔不完备性定理（Gödel's incompleteness theorems）称足够表达算术、相容且有效公理化的系统有既不可证又不可否证的语句，且在通常条件下不能内部证明自身相容。丘奇不可判定性定理（Church's undecidability theorem）排除一阶有效性的一般判定算法，亦称判定问题（Entscheidungsproblem）；停机问题（halting problem）以判定器自我输入的反向行为构造矛盾。均不表示每个具体命题或程序都不可处理。

#### 【拓展】铺砌补充与构造（Further Tilings and Constructions）

- **【拓展】Gomory铺砌论证（Gomory's tiling argument）** 以棋盘哈密顿回路说明去任意一黑一白可铺；各去两格则可能留下孤立角，故黑白平衡不充分。多联骨牌（polyomino）沿整边接格；自由四格骨牌（free tetrominoes）有I、O、T、L/J、S/Z五类，S/Z不能同类铺满矩形，不能用原笔记错误的列奇偶理由证明。

- **【拓展】卡塔兰猜想／米哈伊列斯库定理（Catalan's conjecture / Mihăilescu's theorem）** ：整数$x,y,a,b>1$满足$x^a-y^b=1$时只有$3^2-2^3=1$。这是一般定理，区别于课件100以内的穷举，也区别于卡特兰数（Catalan numbers）。出租车数（taxicab numbers）研究不同正立方和表示，1729为两种表示的最小例。

- **【拓展】历史联系（historical connections）** ：原笔记以哈代–温伯格定律（Hardy–Weinberg law）、代数数论（algebraic number theory）、椭圆曲线理论（theory of elliptic curves）说明应用或发展背景；广义Collatz类问题不可判定，不能据此说具体Collatz猜想已不可证明。

## 二、集合、函数、序列与矩阵（Sets, Functions, Sequences and Matrices）

### 2.1 集合的基本语言（Basic Set Language）

授课依据：[[Ch2.1.pdf|Ch2.1.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

#### 集合的表示与常用对象（Notation and Common Sets）

- **集合（set）** 是不计顺序与重复的对象整体；元素（element / member）用$\in$表示。

  列举法（roster method）写出元素，描述法（set-builder notation）写$\{x\in U\mid P(x)\}$；省略号必须有可辨认规则。集合中的元素可以也是集合。

- **常用数集（number sets）** ：自然数$\mathbb N$（本笔记约定含0）、整数$\mathbb Z$、正整数$\mathbb Z^+$、有理数$\mathbb Q$、实数$\mathbb R$、复数$\mathbb C$；

  题目另有约定时从其约定。$\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q\subseteq\mathbb R\subseteq\mathbb C$。

- **全集（universal set）** $U$限定讨论范围；空集（empty set / null set）$\varnothing$无元素；单元素集（singleton set）只有一个元素。

  $\varnothing\ne\{\varnothing\}$，后者基数为1；$\{\varnothing,\{\varnothing\}\}$有两个元素。

- **有理数（rational number）** 的精确定义为$\mathbb Q=\{p/q:p,q\in\mathbb Z,q\ne0\}$；实数（real number）中不属于$\mathbb Q$的为无理数（irrational number）。课件将分母变量误重复成$p$，此处按正确条件写。

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

- **【拓展／应用】数据类型（data type）** 可理解为一个取值集合连同允许的运算，例如布尔类型以$\{0,1\}$为值集并配AND、OR、NOT。集合只描述成员，类型还需说明可执行哪些操作，不能只由名字猜取值范围。

#### 【拓展】区间与集合论基础（Intervals and Foundations of Set Theory）

- **【拓展】区间记号（interval notation）** ：$(a,b),[a,b],(a,b],[a,b)$分别表示端点是否纳入，无穷端点永不用闭括号。

- **【拓展】朴素集合论（naive set theory）与公理化集合论（axiomatic set theory）** ：无条件允许$\{x:x\notin x\}$会导致罗素悖论；不能把任意文字描述都默认成一个合法集合。

### 2.2 集合运算、恒等式及扩展（Set Operations, Identities and Extensions）

授课依据：[[Ch2.2.pdf|Ch2.2.pdf]]。仅目录出现“Set Identities / Generalized Unions”不足以扩充范围；实际页有五种运算、容斥与位串。

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

#### 【拓展】无限集合族（Infinite Set Families）

- **【拓展】广义并与交（generalized unions and intersections）** 分别表示存在一个指标／所有指标满足成员关系。递增集合族（increasing family）的交由最小集决定，递减集合族（decreasing family）的并由最大集决定；另一运算须检查端点。

  无限集合族（infinite set family）中，每个$[0,1/i]$非空且交为$\{0\}$，每个$(0,1/i)$非空却交为空；不能把有限结论直接外推。

#### 【拓展】恒等式与证明（Identities and Proofs）

- **【拓展】集合恒等式（set identities）** ：$A\cup\varnothing=A$，$A\cap U=A$；$A\cup U=U$，$A\cap\varnothing=\varnothing$；$A\cup A=A\cap A=A$；$\overline{\overline A}=A$；并交均交换、结合；

  $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$、$A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$；$\overline{A\cup B}=\overline A\cap\overline B$、$\overline{A\cap B}=\overline A\cup\overline B$；

  $A\cup(A\cap B)=A$、$A\cap(A\cup B)=A$；$A\cup\overline A=U$、$A\cap\overline A=\varnothing$。分别对应逻辑中的同一、支配、幂等、双重否定、交换、结合、分配、德摩根、吸收、否定律（英文名称见1.3）。

  广义德摩根律同样适用于任意指标族。

- **【拓展／习题结论】集合运算与包含关系（set operations and inclusion）** ：$A\cup B=A\iff B\subseteq A$；$A\cap B=A\iff A\subseteq B$；$A-B=A\iff A\cap B=\varnothing$。

  对称差的消去律（cancellation law）：$A\oplus C=B\oplus C\Rightarrow A=B$，因为两边再对称差$C$，利用结合律及$C\oplus C=\varnothing$即可。并、交一般不能消去，例如$\{1\}\cup\{1,2\}=\{2\}\cup\{1,2\}$，却有$\{1\}\ne\{2\}$。

#### 【拓展】集合后继与自然数构造（Set Successors and Natural-number Construction）

- **【拓展】集合后继（set successor）** 为$S(A)=A\cup\{A\}$；$S(\varnothing)=\{\varnothing\}$，不是重复加入已有元素。在良基集合论（well-founded set theory）中有限$A$满足$|S(A)|=|A|+1$；冯·诺依曼自然数（von Neumann natural numbers）取$0=\varnothing,n+1=n\cup\{n\}$。

- **【拓展】集合恒等式证明（proof of set identities）** 可用双向包含、逐元素转逻辑、隶属表（membership table）或已证恒等式变形；特定文氏图不能独立证明一般结论。

#### 计算机表示与算法（Computer Representation and Algorithms）

- **特征位串（characteristic bit string）** ：有限且大小可存储的全集$U=\{a_1,\ldots,a_n\}$先固定顺序；第$i$位为1当且仅当$a_i\in A$。相同位序下，并、交、补、对称差分别为逐位OR、AND、NOT、XOR，不能混用两种元素顺序。

  课件例$U=\{1,\ldots,10\}$、$A=\{1,3,5,7,9\}$、$B=\{1,2,3,4,5\}$，对应$1010101010$与$1111100000$；交为$1010100000$，并为$1111101010$，补$B$为$0000011111$。

- **【拓展】集合交集算法（set-intersection algorithms）** ：双循环$O(nm)$；排序后双指针（two-pointer method）线性扫描；哈希集合（hash set）通常期望$O(n+m)$；先排序$B$再逐项二分查找（binary search）需$O(m\log m+n\log m)$。布尔标记数组（Boolean marking array）含初始化为$O(U+n+m)$，机器字位并行为$O(\lceil U/w\rceil)$；期望复杂度（expected complexity）不等于最坏复杂度（worst-case complexity）。

- **【拓展】特征函数（characteristic function）** 将成员关系映为0/1，联系布尔代数（Boolean algebra）；$A\oplus U=\overline A$、$A\oplus\overline A=U$，且对称差交换、结合、同项消去。

#### 【拓展】多重集与模糊集（Multisets and Fuzzy Sets）

- **【拓展】多重集（multiset）** 用重数（multiplicity）记录重复；逐元素的并取max、交取min、差取$\max(m_A-m_B,0)$、和（sum）取$m_A+m_B$。共用设备按最大需求，不共用按需求和；

  并不等于和。

- **【拓展】模糊集（fuzzy set）** 用隶属函数（membership function）$\mu_A:U\to[0,1]$；补为$1-\mu_A$、并为max、交为min。

  隶属度（degree of membership）不自动等于softmax概率，二者不能只因都在$[0,1]$便视为同一概念。

### 2.3 函数及其运算（Functions and Their Operations）

授课依据：[[Ch2.3_Part1.pdf|Ch2.3_Part1.pdf]]、[[Ch2.3_Part2.pdf|Ch2.3_Part2.pdf]]。函数后半、反函数与复合均有实际课件内容，保留；取整综合、部分函数与高级像集性质为拓展。

#### 函数定义与像（Definition and Images）

- **函数／映射（function / mapping）** $f:A\to B$把每个$a\in A$对应唯一$f(a)\in B$。

  定义域（domain）是A，陪域（codomain）是B，值域／像（range / image）$f(A)\subseteq B$；原像（preimage）是映到目标值的输入。

  判定函数要同时排除“一输入多输出”和“定义域有输入没有输出”。程序可能不终止或有副作用，不能直接等同于数学总函数（total function）。

- 函数相等需定义域、陪域的约定及各点输出一致；函数图像（graph of a function）为$\{(a,f(a)):a\in A\}\subseteq A\times B$。实值函数的和与积逐点定义：$(f+g)(x)=f(x)+g(x)$、$(fg)(x)=f(x)g(x)$。

- **【拓展】子集的像（image of a subset）** $f(S)=\{f(s):s\in S\}$。 **【拓展／补充】逆像（inverse image）** $f^{-1}(T)=\{a:f(a)\in T\}$不要求f可逆，勿与反函数混淆；

  像保持并，交一般仅有$f(S\cap T)\subseteq f(S)\cap f(T)$；逆像保持并、交及相对补。

- **【拓展】有限像集的基数（cardinality of a finite image）** ：有限$S\subseteq A$满足$|f(S)|\le|S|$。$f$单射当且仅当每个有限$S\subseteq A$都满足$|f(S)|=|S|$：单射不合并元素；反之若有$x\ne y$却同像，取$S=\{x,y\}$便违背等式。

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

  【拓展】单射复合单射、满射复合满射、双射复合双射。

  【拓展】若$f\circ g$单则g单，若$f\circ g$满则f满；反方向的另一因子不可无条件推出。$(f\circ g)^{-1}=g^{-1}\circ f^{-1}$。

  课件双射的恒等式：$f^{-1}\circ f=i_A$、$f\circ f^{-1}=i_B$，先代入$f^{-1}(f(a))=a$、$f(f^{-1}(b))=b$即可验证。

![[C2.3-映射类型-单射满射双射.png|650]]

- **反函数、倒数与逆运算（inverse functions, reciprocals and undoing operations）** ：$f^{-1}$是反函数，$(1/f)(x)=1/f(x)$是逐点倒数，只在$f(x)\ne0$时定义，二者不能互换。双射还满足$(f^{-1})^{-1}=f$。

  【拓展】只为修复满射，可把陪域改为$f(A)$；修复单射则要在定义域中保留各同像类的代表。限制后的映射是新函数。例如$\sin:[-\pi/2,\pi/2]\to[-1,1]$为双射，其反函数为反正弦（arcsine）$\arcsin$；不能直接把全实轴上的周期性正弦当作可逆函数。

#### 【拓展】取整函数（Floor and Ceiling Functions）

- **【拓展】下取整／上取整（floor / ceiling function）** 分别为不大于／不小于$x$的最近整数；$\lfloor-0.5\rfloor=-1,\lceil-0.5\rceil=0$。基本刻画为$n\le x<n+1\iff\lfloor x\rfloor=n$，$n-1<x\le n\iff\lceil x\rceil=n$。

  对整数$k$，取整可平移$k$；$\lfloor-x\rfloor=-\lceil x\rceil$。不能一般拆开实数和或积。鸽巢课件用到的$\lceil N/k\rceil$及含义在4.2按范围内内容保留。

#### 【拓展】取整证明与成立条件（Proofs and Conditions for Rounding Identities）

- **【拓展】取整恒等式（rounding identities）** ：$\lfloor2x\rfloor=\lfloor x\rfloor+\lfloor x+1/2\rfloor$；整数$n$满足$\lfloor n/2\rfloor+\lceil n/2\rceil=n$、两者积为$\lfloor n^2/4\rfloor$。

- **【拓展】可拆条件（conditions for splitting rounded sums）** ：写$x=m+\alpha,y=n+\beta$，$0\le\alpha,\beta<1$。下取整之和可拆当且仅当$\alpha+\beta<1$；上取整之和可拆当且仅当$\alpha=0$或$\beta=0$或$\alpha+\beta>1$；$\lceil x+y\rceil=\lfloor x\rfloor+\lceil y\rceil$当且仅当$\alpha=0$，或$\beta>0$且$\alpha+\beta\le1$。

#### 阶乘与部分函数（Factorials and Partial Functions）

- **阶乘（factorial）** 为$n!=1\cdot2\cdots n$，$0!=1$，计数课件直接使用。

- **【拓展】Stirling近似（Stirling's approximation）** ：$n!\sim\sqrt{2\pi n}(n/e)^n$，$\sim$指比值趋于1。比较排序（comparison sorting）的二元决策树（binary decision tree）须区分$n!$次序，故最坏比较次数$\ge\lceil\log_2(n!)\rceil=\Omega(n\log n)$，仅限比较模型。

- **【拓展】部分函数（partial function）** 只在部分输入上定义，未定义（undefined）不是一个输出。机器学习（machine learning）的函数拟合（function approximation）、物理信息神经网络（physics-informed neural network, PINN）不自动给出可解释性（interpretability）或证明。

- **【拓展】对数（logarithm）** ：教材$\log$默认底2，$\ln$为自然对数（natural logarithm）；$\log_bx=\ln x/\ln b$需$x>0,b>0,b\ne1$，数值与取整不能混底。

### 2.4 序列与递推预备及【拓展】求和（Sequences, Recurrence Prerequisites and Summations）

授课依据：[[Ch8.1.pdf|Ch8.1.pdf]]。数列、递推和复利在Ch8.1实际出现，相关预备定义保留；独立求和、Lucas、Binet等为拓展。

#### 序列、递推与迭代（Sequences, Recurrences and Iteration）

- **序列（sequence）** 按整数下标列项（term）$a_n$，须说明下标（index）起点；递推关系（recurrence relation）以前项给后项，配足初始条件（initial conditions）才确定解（solution）。这些概念在Ch8.1课件实际出现，完整建模与例题见第五部分。

- **复利与迭代（compound interest and iteration）** ：$P_n=(1+r)P_{n-1}$反复代入得$P_n=P_0(1+r)^n$。正向／反向代入（forward / backward substitution）是迭代求闭式（closed formula）的方式。初值取决于最大滞后及起始下标，如$a_n=a_{n-5}$通常需5个初值。

- **【拓展】等差与等比数列（arithmetic / geometric progression）** 分别为$a_0+nd$、$ar^n$，$d,r$称公差／公比（common difference / ratio）。一阶仿射递推（first-order affine recurrence）$a_n=ra_{n-1}+b$在$r\ne1$时为$r^na_0+b(r^n-1)/(r-1)$，$r=1$时为$a_0+nb$。

- **【拓展】Lucas数与Binet公式（Lucas numbers and Binet's formula）** ：$L_0=2,L_1=1$、$L_n=L_{n-1}+L_{n-2}$；斐波那契数取$f_0=0,f_1=1$时，$f_n=(\varphi^n-\psi^n)/\sqrt5$，$\varphi=(1+\sqrt5)/2$为黄金比例（golden ratio），$\psi=(1-\sqrt5)/2$。相同递推不代表相同初值。

#### 【拓展】规律识别与求和记号（Patterns and Summation Notation）

- **【拓展】规律识别（pattern recognition）** 可看差分（differences）、商（ratios）、周期（periodicity）或递推；有限项不能唯一确定通项。

- **【拓展】求和／连乘记号（summation / product notation）** 为$\sum,\prod$；哑指标（dummy index）换元（change of index）须同时改上下限，有限双重求和（double summation）可换序，空和／空积（empty sum / product）为0／1。有限求和具线性性（linearity），与指标有关的因子不可当常数提出。

| 【拓展】求和公式（summation formula） | 条件 |
|---|---|
| $\sum_{k=0}^nar^k=a(1-r^{n+1})/(1-r)$ | $r\ne1$；$r=1$时$(n+1)a$ |
| $\sum_{k=1}^nk=n(n+1)/2$；$\sum_{k=1}^n(2k-1)=n^2$ | $n\ge0$整数 |
| $\sum_{k=1}^nk^2=n(n+1)(2n+1)/6$；$\sum_{k=1}^nk^3=[n(n+1)/2]^2$ | $n\ge0$整数 |
| $\sum_{k=0}^{\infty}x^k=1/(1-x)$；$\sum_{k=1}^{\infty}kx^{k-1}=1/(1-x)^2$ | $\lvert x\rvert<1$ |

#### 【拓展】求和方法与补充序列（Summation Methods and Further Sequences）

- **【拓展】求和方法（summation methods）** ：等比和用$S-rS$错位相减，区间和用前缀和相减，望远镜和／积（telescoping sum / product）消去中间项；奇数和可看逐层扩方格。无穷级数（infinite series）须检查收敛条件（convergence conditions），不能随意逐项求导。

- **【拓展】Ulam数（Ulam numbers）** 从1、2起，每次选能唯一表示成两个不同已有项之和的最小数。在线整数序列大全（On-Line Encyclopedia of Integer Sequences, OEIS）帮助识别，有限项匹配不构成证明；接触数问题（kissing-number problem）问同半径球围绕中心球、彼此内部不重叠的最多相切球数。

### 2.5 【拓展】可数性与无限基数（Countability and Infinite Cardinality）

【拓展】全部补充课件中未见本节的独立讲解，保留压缩说明供回查。

#### 【拓展】等势与可数性（Cardinality and Countability）

- **【拓展】等势（equinumerosity / same cardinality）** 用双射定义，$|A|\le|B|$用单射定义；无限集可与真子集等势。可数集（countable set）指有限集或与$\mathbb Z^+$双射的可数无穷集（countably infinite set，基数$\aleph_0$）；其余为不可数（uncountable）。可数集的子集仍可数。

#### 【拓展】可数集的枚举（Enumerating Countable Sets）

- **【拓展】枚举（enumeration）** ：整数可列$0,1,-1,2,-2,\ldots$，有理数按分子分母之和分层并去重。可数个可数集的并（countable union of countable sets）、有限笛卡尔积及有限字母表上的全部有限串均可数；无限乘积不一定可数。

- **【拓展】Hilbert大饭店（Hilbert's Grand Hotel）** 以$n\mapsto n+1$或$2n$安排新客；二维对角枚举（diagonal enumeration）处理可数车客。Cantor配对函数（Cantor pairing function）$\pi(m,n)=(m+n-2)(m+n-1)/2+m$将正整数对双射到正整数，不能先列完一个无限行再列下一行。

> [!info]- 【拓展】原图回看
> ![[C2-图8-正有理数可数的排列路径.png|430]]

#### 【拓展】对角线与双射判据（Diagonalization and Bijection Criteria）

- **【拓展】Cantor对角线论证（Cantor's diagonal argument）** 令新数第$n$位不同于第$n$个数的第$n$位，构造枚举之外的实数，故$\mathbb R$及无理数集不可数；只用1、2等方式避免小数双重展开。

- **【拓展】Schröder–Bernstein定理（Schröder–Bernstein theorem）** ：两集合间双向有单射便有双射。例如$(0,1)\hookrightarrow[0,1]$用包含，反向用$x\mapsto(x+1)/3$，得等势；两个单射不必互为反函数。小数交织（digit interleaving）须处理双重表示。

#### 【拓展】不可计算函数与更大的无限（Uncomputable Functions and Larger Infinities）

- **【拓展】可计算／不可计算函数（computable / uncomputable functions）** ：有限程序只有可数多个，而$\mathbb N\to\{0,1\}$的函数不可数，故有函数无程序计算。Cantor定理（Cantor's theorem）称$|S|<|\mathcal P(S)|$，由$T=\{s:s\notin f(s)\}$对角化排除满射。

- **【拓展】连续统（continuum）** 基数$\mathfrak c=2^{\aleph_0}$；连续统假设（continuum hypothesis, CH）称不存在介于$\aleph_0$与$\mathfrak c$的基数。其对ZFC的独立性（independence）以相容性为前提，不是被证明为假。

- **【拓展】时间／空间层级定理（time / space hierarchy theorem）** ：对适当可构造（constructible）的资源界，$f=o(g/\log g)$保证$\operatorname{DTIME}(f)\subsetneq\operatorname{DTIME}(g)$；空间界至少$\log n$且$f=o(g)$时有对应严格空间层级。确定性图灵机（deterministic Turing machine）的较大资源允许模拟后对角化；不能外推成任意微增资源都更强或$P\ne NP$。[条件核对来源](https://cs.uwaterloo.ca/~r5olivei/courses/2024-fall-cs360/lecture-notes/lecture05/)。

- **【拓展】黎曼猜想（Riemann hypothesis）** 称黎曼ζ函数（Riemann zeta function）全部非平凡零点（nontrivial zeros）的实部为$1/2$，负偶整数的平凡零点另论。[原陈述](https://www.claymath.org/millennium/Riemann-Hypothesis/)。

### 2.6 矩阵预备与【拓展】普通运算（Matrix Prerequisites and Ordinary Operations）

授课依据：[[Ch9.1_Part1.pdf|Ch9.1_Part1.pdf]]、[[Ch9.1_Part3.pdf|Ch9.1_Part3.pdf]]、[[Ch9.3_Part2.pdf|Ch9.3_Part2.pdf]]。矩阵下标、零一矩阵、布尔积／幂服务于关系与Warshall，属于范围内；普通矩阵代数另标拓展。

#### 矩阵记号与【拓展】普通运算（Matrix Notation and Ordinary Operations）

- **矩阵（matrix）** 的$m\times n$表示$m$行$n$列，条目（entry）$a_{ij}$按先行后列编号；方阵（square matrix）行列数相同。关系矩阵的这些记法在Ch9.1课件中使用。

- **【拓展】普通矩阵运算（ordinary matrix operations）** ：行／列矩阵（row / column matrix）、零矩阵（zero matrix）按形状或条目命名；相等须同型逐项相等，加法（sum）与数乘（scalar multiplication）逐项进行。$A_{m\times k}B_{k\times n}$为$m\times n$，$(AB)_{ij}=\sum_ta_{it}b_{tj}$，一般不交换。

#### 【拓展】幂、转置与逆（Powers, Transposes and Inverses）

- **【拓展】单位矩阵（identity matrix）** 对角1其余0，$I_mA=A=AI_n$；幂满足$A^0=I,A^{r+s}=A^rA^s$。转置（transpose）交换行列，$(AB)^T=B^TA^T$；对称矩阵（symmetric matrix）满足$A^T=A$，故$A+A^T$对称。

- **【拓展】数量矩阵（scalar matrix）** 为$cI$，与全部同阶方阵交换；矩阵环的中心（center of a matrix ring）恰由此组成。逆矩阵（inverse matrix）须满足双侧乘积为$I$，并非逐项倒数；逆唯一且$(AB)^{-1}=B^{-1}A^{-1}$。

- **【拓展】周期矩阵幂（periodic matrix powers）** 例如$\begin{bmatrix}0&1\\-1&0\end{bmatrix}^2=-I$、四次幂为$I$，可按指数模4化简。

#### 布尔矩阵及可达性（Boolean Matrices and Reachability）

- **零一矩阵／布尔矩阵（zero–one / Boolean matrix）** 条目0或1；并／合取的对偶运算（join / meet）逐项OR／AND；

  布尔积（Boolean product）记$A\odot B$：$(A\odot B)_{ij}=\bigvee_t(a_{it}\land b_{tj})$。普通积数中转方案个数，布尔积只问是否存在；不能把OR换成算术加法。

- **布尔幂（Boolean power）** $A^{[0]}=I$、$A^{[r+1]}=A^{[r]}\odot A$表示恰好r步的可达性（reachability）。

  不同于任意正长度可达性，后者为$A\lor A^{[2]}\lor\cdots\lor A^{[n]}$，与传递闭包相接。

- 逐项并交有幂等、交换、结合、分配律，$A\lor0=A$、$A\land0=0$；布尔积有结合律和单位元I、零元0，也对逐项OR分配，但一般不交换。不要把逐项AND与布尔积当同一个运算。


- **【拓展】布尔幂最终周期性（eventual periodicity of Boolean powers）** 来自$n\times n$布尔矩阵仅$2^{n^2}$种；重复后再右乘，周期延续。它不保证最终不变：$\begin{bmatrix}0&1\\1&0\end{bmatrix}$的幂交替为$A,I$。单调的是累计并；若某次为全1矩阵$J$且$A$每列有1，则$J\odot A=J$保证后续稳定。

## 三、关系（Relations）

### 3.1 二元关系的性质与运算（Properties and Operations of Binary Relations）

授课依据：[[Ch9.1_Part1.pdf|Ch9.1_Part1.pdf]]、[[Ch9.1_Part2 (1).pdf|Ch9.1_Part2 (1).pdf]]、[[Ch9.1_Part3.pdf|Ch9.1_Part3.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

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

- **关系幂性质的证明要点（proofs of properties of relation powers）** ：

  1. **复合保包含（monotonicity of composition）** ：若$R\subseteq S$，复合中的中间见证在换成$S$后仍合法，故$T\circ R\subseteq T\circ S$，$R\circ T\subseteq S\circ T$。
  2. **幂与路径（powers and paths）** ：$n=1$是边的定义；长度$n+1$的路径拆出一条边与长度$n$的余段，按复合定义和归纳假设，恰好对应$R^{n+1}$。
  3. **传递性的幂刻画（power characterization of transitivity）** ：由$R^2\subseteq R$归纳得$R^{n+1}\subseteq R^2\subseteq R$；逆向只需取$n=2$。
  4. **各次幂仍传递（transitivity of every positive power）** ：由保包含归纳得$R\supseteq R^2\supseteq\cdots$。因此$(R^n)^2=R^{2n}\subseteq R^n$，即$R^n$传递。也可用捷径引理（shortcut lemma）：传递关系的两条相邻边能缩成一条，把$2n$步缩到$n$步。

  指数还满足$(R^m)^n=R^{mn}$；但一般$(R\circ S)^n\ne R^n\circ S^n$，展开后交替次序不能随意交换。这里的传递关系幂递减，不能推广到任意关系。

#### 逆关系与计数（Inverses and Counting）

- **逆关系（inverse relation）** $R^{-1}=\{(b,a):(a,b)\in R\}$；$(R^{-1})^{-1}=R$，逆保持并、交、差及适当全集下的补；$(S\circ R)^{-1}=R^{-1}\circ S^{-1}$，复合次序反转。

- **关系总数（number of relations）** ：若$|A|=m,|B|=n$，共有$2^{mn}$个A到B关系；n元集上为$2^{n^2}$，因为每个有序对可选或不选。

- **【拓展】按性质计数（counting by properties）** ：自反与反自反各$2^{n(n-1)}$；对称$2^{n(n+1)/2}$；

  反对称$2^n3^{\binom n2}$；非对称$3^{\binom n2}$；同时对称反对称$2^n$。方法是对角线逐位选、不同点的无序对分别选。传递性把不同位置的选择耦合，不能套上述独立选择法；

  原笔记列$n=4,5,6$的传递关系数3994、154303、9415189仅作计数背景。

![[C9-四个性质的有向图判读.png|650]]

- **对称关系的逆刻画（inverse characterization of symmetry）** ：$R$对称当且仅当$R=R^{-1}$。正向由每条边都有反向边，分别得到双向包含；逆向由$(a,b)\in R=R^{-1}$立得$(b,a)\in R$。

  对同底集关系，$(R\cup S)^{-1}=R^{-1}\cup S^{-1}$、$(R\cap S)^{-1}=R^{-1}\cap S^{-1}$、$(R-S)^{-1}=R^{-1}-S^{-1}$；$(\overline R)^{-1}=\overline{R^{-1}}$的右侧补集须相对于反向笛卡尔积。逆关系总存在，不要求它还是函数。

### 3.2 多元关系与数据库（n-ary Relations and Databases）

授课依据：[[Ch9.2.pdf|Ch9.2.pdf]]。保留n元关系、域、度、记录字段、条件筛选和拼表概念；键、投影、SQL及通用算子细节为拓展。

#### 记录、属性与键（Records, Attributes and Keys）

- **$n$元关系（$n$-ary relation）** 为$R\subseteq A_1\times\cdots\times A_n$，各$A_i$是论域（domain），度（degree）为$n$，不是记录数。课件例$(a,b,m)$满足$m>0$且$m\mid(a-b)$，度3、论域$\mathbb Z,\mathbb Z,\mathbb Z^+$。

- **关系数据库（relational database）** 以元组为记录／行（record / row）、分量为字段／属性（field / attribute），展示为表；数学关系是集合，不保留重复行与自然行序。课件实际讨论按条件筛元组及连接分表记录。

- **【拓展】外延／内涵（extension / intension）** 分别为当前元组与结构规则；主键（primary key）唯一标识记录，复合键（composite key）联合多个字段。不能由当前姓名不重名就认定未来也可作键；分表减少冗余（redundancy），连接条件仍须正确。

#### 选择、投影与连接（Selection, Projection and Join）

- **选择／条件筛选（selection）** 保留满足条件$C$的记录：$s_C(R)=\{\boldsymbol a\in R:C(\boldsymbol a)\}$，字段数不变。它对应课件“determining all n-tuples satisfying certain conditions”。

- **连接（join）** 将两表公共字段值相同的记录拼接，公共部分只留一次；对应课件“joining records in different tables”。先对齐列序并检查全部共同字段；多对多匹配可产生多行，未匹配记录不进入内连接（inner join）。例如按学号连接成绩表与姓名表，不能仅因记录行号相同就配对。

- **【拓展】关系代数（relational algebra）形式化** ：投影（projection）$P_{i_1,\ldots,i_k}(R)$选列并去重；教材$p$列连接$J_p(R,S)$匹配$R$末$p$列与$S$前$p$列，结果度$m+n-p$，$p=0$退化为笛卡尔积。课件没有展开投影及这些通用算子公式，不把整套运算升为授课内容。

#### 【拓展】SQL与考试信息的边界（SQL and Examination Evidence）

- **【拓展】SQL（Structured Query Language）** 的WHERE近似选择、SELECT列近似投影、JOIN依条件拼表；SQL默认可保留重复，而数学关系为集合，DISTINCT才去重。

> [!info] 历史考试提醒
> 第13节要求先掌握$n$元关系再学数据库语言；SQL考试题的具体承诺无直接证据。按本次课件范围，仅保留筛选与连接的概念为范围内，其余按拓展处理。

- **【拓展】外连接（outer join）** 的左／右／全版本（left / right / full outer join）保留相应未匹配行，并补空值；先筛选再连接（selection pushdown）是关系代数优化思路，但移动条件前须核对等价性。

### 3.3 矩阵与有向图表示（Matrix and Digraph Representations）

授课依据：[[Ch9.1_Part1.pdf|Ch9.1_Part1.pdf]]、[[Ch9.1_Part2 (1).pdf|Ch9.1_Part2 (1).pdf]]、[[Ch9.1_Part3.pdf|Ch9.1_Part3.pdf]]。课件将矩阵／有向图表示提前放在Ch9.1，不能只找同名Ch9.3文件。

#### 矩阵、复合与图表示（Matrices, Composition and Digraphs）

- 固定$A=(a_1,\ldots,a_m),B=(b_1,\ldots,b_n)$的顺序，关系矩阵（relation matrix）$(M_R)_{ij}=1\iff a_iRb_j$。行是起点、列是终点；调换顺序会改矩阵外观，但不改关系本身。

- $M_{R\cup S}=M_R\lor M_S$，$M_{R\cap S}=M_R\land M_S$，$M_{R^{-1}}=M_R^T$；差与补逐项按集合定义。$M_{S\circ R}=M_R\odot M_S$，矩阵乘法顺序与复合记号表面相反，因为先走R对应左矩阵的行。

- $M_{R^n}=M_R^{[n]}$为布尔幂；普通矩阵幂不等同关系幂矩阵。

  有向图中顶点（vertex）对应元素，有向边／弧（directed edge / arc）$a\to b$对应有序对，自环（loop）对应$aRa$。图用于看反例、路径，矩阵适合统一计算与算法。

#### 用表示法判性质（Testing Properties from Representations）

- 自反看对角线全1，对称看转置相同，反对称看对角线外不能有互为对称位置的两个1；传递看布尔平方是否逐项不超过原矩阵。非对称还要求对角线全0。

  反对称关系的矩阵不叫“反对称矩阵（skew-symmetric matrix）”，后者是线性代数的$A^T=-A$，概念不同。

### 3.4 闭包与Warshall算法（Closures and Warshall's Algorithm）

授课依据：[[Ch9.3_Part1.pdf|Ch9.3_Part1.pdf]]、[[Ch9.3_Part2.pdf|Ch9.3_Part2.pdf]]。课件文件名Ch9.3实际讲闭包，含Warshall、闭包保留性质与次序。

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

- **课件四点手算例（four-vertex courseware example）** ：顶点顺序$a,b,c,d$，输入关系矩阵

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

授课依据：[[Ch9.5.pdf|Ch9.5.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

#### 等价关系、等价类与划分（Equivalence, Classes and Partitions）

- **等价关系（equivalence relation）** 要求自反、对称、传递同时成立；逐条证明，或转化成$f(x)=f(y)$型关系。典型例子：同余、字符串等长、相同函数值；

  “有共同朋友”“差小于某阈值”等不自动传递。

- **等价类（equivalence class）** $[a]_R=\{x\in A:xRa\}$；$aRb\iff[a]=[b]\iff[a]\cap[b]\ne\varnothing$。不同代表元（representative）可表示同一类；类必非空，包含自己的代表元；

  不同的类两两不交。

- **划分（partition）** 是非空块（block）的集合，块两两不交且并为A。等价关系与划分一一对应：R给出全部不同等价类；划分$\{A_i\}$反推$R=\bigcup_i(A_i\times A_i)$。

  商集（quotient set）$A/R=\{[a]:a\in A\}$的元素是类，不是A中的普通元素。

- **等价类定理的证明要点（proof of the equivalence-class theorem）** ：$aRb\Rightarrow[a]=[b]$：用对称性与传递性证明两个类双向包含；$[a]=[b]\Rightarrow[a]\cap[b]\ne\varnothing$：自反性使$a\in[a]=[b]$；若$c\in[a]\cap[b]$，由$aRc,bRc$及对称、传递得$aRb$，闭合三向等价。

- **等价关系与划分定理的证明要点（proof of the equivalence–partition correspondence）** ：自反性保证每个元素属于一个类，等价类定理保证不同类不交，因此构成划分。反向规定“同块即相关”：同元素在同一块得自反，交换得对称；若$a,b$同块而$b,c$同块，由块不交且共享$b$可知两块相同，得$a,c$同块即传递。这样构造的关系唯一，其类恰好是原划分的块。

#### 类的大小与前缀分类（Class Sizes and Prefix Classification）

- **类大小与关系对数（class sizes and pair counts）** ：有限等价类$A_1,\ldots,A_k$给$R=\bigcup_i(A_i\times A_i)$，故$|R|=\sum_i|A_i|^2$；课件的三块大小3、2、1对应$9+4+1=14$个有序对，各块内部全部成对，不能只连不同元素而漏自环。

- **【拓展】前缀分类（prefix classification）** ：长度$n$的位串按前$r$位相同分等价类，共$2^r$类、每类$2^{n-r}$个；按相同长度等价时必须先说是否允许空串及长度范围。

![[C9-集合的划分示意.png|510]]

#### 【拓展】等价关系的构造与计数（Constructions and Counting）

- **【拓展】构造等价关系（constructing equivalence relations）** ：映射$f$诱导$x\sim y\iff f(x)=f(y)$；“模$m$相等或互为相反数”也成等价关系，例如模7有$\{[0]\},\{[1],[6]\},\{[2],[5]\},\{[3],[4]\}$四类。并不一定保等价，交保持等价；可用自反、对称、传递闭包生成最小等价关系。

- **【拓展】Bell数与第二类Stirling数（Bell numbers and Stirling numbers of the second kind）** ：$S(n,k)$数$n$元集合分成$k$个非空无标号块，$S(n,k)=kS(n-1,k)+S(n-1,k-1)$，$S(0,0)=1$，其余不合法边界为0；$B_n=\sum_kS(n,k)$数所有划分。课件只实际列出三元集的5种划分，不涉及这些一般计数公式。

- **【拓展】加法陪集（additive coset）** 可表示模$m$同余类$a+m\mathbb Z$；循环关系（circular relation）要求$aRb,bRc\Rightarrow cRa$，配合自反性可导对称、传递。前缀等价（prefix equivalence）及用标签分类（classification by labels）是构造等价类的应用。

### 3.6 偏序、Hasse图、格与拓扑排序（Partial Orders, Hasse Diagrams, Lattices and Topological Sorting）

授课依据：[[Ch9.6.pdf|Ch9.6.pdf]]。格、分配格、有界格、补格与对偶均在课件内；拓扑排序、一般障碍刻画和安全模型为拓展。

#### 偏序、可比性与字典序（Partial Orders, Comparability and Lexicographic Order）

- **偏序（partial order）** 为自反、反对称、传递关系；偏序集（partially ordered set, poset）记$(A,\preccurlyeq)$。

  严格偏序（strict partial order）为反自反且传递，因而非对称；由非严格序删除对角得到严格序，反过来补对角。等价关系用对称，偏序用反对称。

- **可比（comparable）** 指$a\preccurlyeq b$或$b\preccurlyeq a$，否则不可比（incomparable）。任意两点可比为全序／线性序（total / linear order）；

  链（chain）为其中全序的子集，【拓展】反链（antichain）为不同元素两两不可比的子集。正整数整除与幂集包含一般只是偏序。

- **字典序／词典序（lexicographic order）** 比较第一个不同分量；前面分量都相等才比较后面。字符串中真前缀排在长串之前；分量若只偏序，则第一处不同分量不可比时不能越过去用后面的大小决定。

#### Hasse图、极值与界（Hasse Diagrams, Extrema and Bounds）

- **覆盖关系（covering relation）** ：$b$覆盖a当$a\prec b$且无$a\prec c\prec b$。Hasse图（Hasse diagram）删自环、删传递边、去箭头并把大者画高。

  连接线只表示覆盖；通过向上路径恢复偏序，不凭横向位置判断可比。

![[C9-Hasse图的三步构造.png|600]]

| 极值／界（extrema and bounds） | 定义与必须区分的条件 |
|---|---|
| 极大元（maximal element） | A中没有严格大于它的元素，可多个 |
| 极小元（minimal element） | A中没有严格小于它的元素，可多个 |
| 最大元（greatest / maximum element） | A中大于等于所有元素，若存在唯一 |
| 最小元（least / minimum element） | A中小于等于所有元素，若存在唯一 |
| 上界（upper bound）／下界（lower bound） | 对子集B中所有元素都在其上／下，可在环境偏序集中但不在B内 |
| 最小上界／上确界（least upper bound, lub / supremum） | 所有上界中最小者，若存在唯一 |
| 最大下界／下确界（greatest lower bound, glb / infimum） | 所有下界中最大者，若存在唯一 |

- 不能把“某一个上界”当lub，也不能把“上界集合中的极小元”不经比较就当最小元。做题先写环境集合、目标子集、全部上／下界，再求其最小／最大者。有限非空偏序集总有极小与极大元，但不一定有最小与最大元。

#### 格与并交（Lattices, Join and Meet）

- **格（lattice）** 要求每一对元素都有lub和glb，记$a\vee b=\operatorname{lub}\{a,b\}$（并，join）、$a\wedge b=\operatorname{glb}\{a,b\}$（交，meet）。格中的并交交换、结合、幂等、吸收；

  序可由$a\preccurlyeq b\iff a\wedge b=a\iff a\vee b=b$恢复。

- **【拓展】格的有限子集（finite subsets of a lattice）** ：任意有限非空子集都有lub与glb，可反复取二元并交；单元素集合的两者都是该元素。

  对大小归纳，$\operatorname{lub}(B\cup\{x\})=\operatorname{lub}(B)\vee x$，glb同理。因此有限非空格必有最大元和最小元，即为有界格；不能把“有限”去掉后照搬。

  空子集另需边界条件：$\operatorname{lub}(\varnothing)$若存在是全格的最小元，$\operatorname{glb}(\varnothing)$若存在是最大元。一般格只保证二元并交，不自动保证空子集也有界。

| 偏序集 | 并／lub | 交／glb |
|---|---|---|
| $(\mathcal P(S),\subseteq)$ | $A\cup B$ | $A\cap B$ |
| $(\mathbb Z^+,\mid)$ | 最小公倍数（least common multiple, lcm） | 最大公因数（greatest common divisor, gcd） |
| 全序集（total order） | max | min |

- 在整除偏序的某个子集里，环境中未包含lcm时不能直接把外面的数当lub；在子集内可能另有最小共同上界，或根本没有。


- **格的四条运算律（four lattice laws）** ：对任意$a,b,c$，

  | 定律（law） | 并（join） | 交（meet） |
  |---|---|---|
  | 交换律（commutativity） | $a\vee b=b\vee a$ | $a\wedge b=b\wedge a$ |
  | 结合律（associativity） | $a\vee(b\vee c)=(a\vee b)\vee c$ | $a\wedge(b\wedge c)=(a\wedge b)\wedge c$ |
  | 幂等律（idempotence） | $a\vee a=a$ | $a\wedge a=a$ |
  | 吸收律（absorption） | $a\vee(a\wedge b)=a$ | $a\wedge(a\vee b)=a$ |

  证明要点：二元并交的唯一性给出交换、幂等；两个结合式都等于三元素集合的同一个lub／glb；$a\wedge b\preccurlyeq a$使$a$就是$\{a,a\wedge b\}$的lub，得吸收律，交的式子对偶。分配律是额外条件，不由以上四律直接保证。

- **【拓展】多级安全格（multilevel security lattice）** 以安全类（security class）$(\ell,C)$表示权限级别（authority level）和类别集合（category set）；逐分量偏序（componentwise order）取$\ell_1\le\ell_2,C_1\subseteq C_2$，并交为等级max／min与类别并／交。信息流格（information-flow lattice）是此应用背景，课件未展开。

> [!warning] 【课件勘误：Ch9.6，PDF p9，slide 34】
> 课件将整除偏序$\{1,2,3,4,8,16\}$判为格，但2、3在该集合中无共同上界，实际不是格。判断必须在给定集合内找lub／glb，不能借用集合外的6或其他数。

#### 格的类型与对偶（Lattice Types and Duality）

- **分配格（distributive lattice）** 满足$a\vee(b\wedge c)=(a\vee b)\wedge(a\vee c)$及对偶式；一般格未必分配。

  五元素菱形$M_3$的中间三点a、b、c使$a\vee(b\wedge c)=a$而$(a\vee b)\wedge(a\vee c)=1$。

- **有界格（bounded lattice）** 同时有底（bottom）0与顶（top）1；正整数整除格虽有底1但无顶，不有界。补元（complement）y满足$x\vee y=1,x\wedge y=0$；

  人人有补称补格（complemented lattice）。三元素链有界但中间元素无补；$M_3$有补但某点可有两个补。【拓展】分配格中的补若存在则唯一；有界、分配且有补的格为布尔代数（Boolean algebra）。

- **对偶原理（principle of duality）** 反转序、互换并交与顶底，得到对偶格（dual lattice）的对应真命题；不能只换符号不换序。

#### 【拓展】障碍、良序与排序（Obstructions, Well-orders and Sorting）

- **【拓展】分配格障碍（obstructions to distributivity）** 为作为子格（sublattice）的$M_3$或$N_5$，必须保持原并交，不能只看画得像菱形或五边形。有限非空格（finite nonempty lattice）有顶底，有限非空子集有并交；空子集须另要求顶底。

- **【拓展】良序（well-order）** 是每个非空子集有最小元的全序；不等于任意全序。拓扑排序（topological sorting）是保持偏序先后约束的线性扩张（linear extension），反复删除极小元；DAG可用Kahn算法（Kahn's algorithm）反复取入度0点，无可取点而仍剩顶点则有环。课件讲到格的对偶原理为止，没有拓扑排序算法。

- **【拓展】划分的细化序（refinement order）** 以每个细块包含于某粗块定义；最细为单点划分、最粗为全集一块。对偶偏序（dual poset）始终仍是偏序；有限覆盖关系可恢复原序，无限稠密序如$(\mathbb Q,\le)$没有覆盖边，不能照搬有限Hasse算法。

- **【拓展】良序归纳原理（well-ordered induction）** 以所有更小对象满足性质推出当前对象；用最小反例（minimal counterexample）证明，最小对象的情形也须被该条件覆盖。全部关系按包含排序，对应幂集偏序。

## 四、计数（Counting）

组合数学（combinatorics）研究离散对象的计数、构造与结构；本部分同时讨论“有多少个”与“怎样不重不漏地生成”。

### 4.1 基本计数原理（Basic Counting Principles）

授课依据：[[Ch6.1.pdf|Ch6.1.pdf]]、[[Ch6.5.pdf|Ch6.5.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

#### 加、乘、减、除四原理（The Four Counting Rules）

- **乘法原理（product rule）** ：任务分步，每个合法前缀的下一步都有固定的$n_i$个选择，总数$\prod_i n_i$。

  不要求概率意义的独立（independence），但若分支数依前面选择而不同，就应分类或用树形图逐支相加。

- **求和原理（sum rule）** ：互不相交的类型分别有$n_i$种，总数$\sum_i n_i$。“先分类、类内分步、最后求和”处理长度不同的密码、变量名与多方案任务。

- **减法原理（subtraction rule）** ：总数减不合法数；有交叠时用容斥。例：长度n位串“以1开头或以00结尾”，$n\ge3$时为$2^{n-1}+2^{n-2}-2^{n-3}$；“至少一个”常用总数减一个也没有。

- **除法原理（division rule）** ：若每个实际对象恰被表示d次，则实际数为表示数除d。纤维大小（fiber size）必须一致；对象有对称性（symmetry）时不能不检查就除固定阶乘。

- **课件计数例（courseware counting examples）** ：BASIC变量名长1或2、首字符为字母、大小写不分并排除5个保留名，共$26+26\cdot36-5=957$。8位串以1开头或以00结尾为$2^7+2^6-2^5=160$；350名申请中两专业分别220、147、交51，均非两专业者$350-(220+147-51)=34$。

  病毒每次向50个新地址转发、无重叠的理想模型要先定轮起点：若初始1封为第1轮，前4轮和为$1+50+50^2+50^3=127551$；若初始后再转发4次，则总和为$\sum_{i=0}^450^i=6377551$。课件混用了这两种轮数，不能直接照抄。

#### 圆排列与函数计数（Circular Arrangements and Function Counts）

- **圆排列（circular permutation）** ：n个不同人围圆桌、只把旋转看成同一排法时为$(n-1)!$；若座位编号则为$n!$；镜像（reflection）是否视同须题目说明。

  两方向相同的无向环游在$n\ge3$时常再除2。

- **【拓展】函数计数（counting functions）** ：m元集到n元集总函数$n^m$；单射在$m\le n$时为$P(n,m)$，$m>n$时0；每个输入依次选输出，单射使候选数递减。

  位串为$2^n$，长度r的n元字母串为$n^r$；首位、禁用字符等限制应单独处理。

#### 【拓展】树形图与受限计数（Tree Diagrams and Restricted Counts）

- **【拓展】树形图（tree diagram）** 以完整根叶分支对应结果；五局三胜（best-of-five series）结束即停，3、4、5场赛果分别2、6、12种，共20，不能计结束后的虚构比赛。

- **【拓展】历史IPv4分类计数（classful IPv4 counting）** 按原题A、B、C类位段及保留位计数，总3,737,091,842；属于教材历史模型，不当现行地址分配规则。

### 4.2 鸽巢、拉姆齐与子序列（Pigeonhole, Ramsey and Subsequences）

授课依据：[[Ch6.2.pdf|Ch6.2.pdf]]、[[Ch6.2&Ch6.3.pdf|Ch6.2&Ch6.3.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

#### 鸽巢与保证阈值（Pigeonhole Principle and Thresholds）

- **鸽巢原理／抽屉原理（pigeonhole principle / Dirichlet drawer principle）** ：$k+1$个物体进k盒至少一盒有两个；

  从更大有限集到更小有限集不存在单射。上取整（ceiling）$\lceil x\rceil$是不小于$x$的最小整数。广义鸽巢原理（generalized pigeonhole principle）：N个物体进k盒，至少一盒$\lceil N/k\rceil$个。

- **反问题（inverse problem）** ：要保证至少一盒有r个，最少$k(r-1)+1$个；若各盒容量上限不同则超过其上限和才强制违例。

  证明先写清“物体”“盒子”“分配规则”，给出最坏分配说明阈值不能再小。

- **鸽巢原理的证明与锋利性（proof and sharpness of pigeonhole bounds）** ：普通版若每盒至多1个，总数至多$k$，与至少$k+1$个矛盾。广义版若每盒都少于$\lceil N/k\rceil$个，总数至多$k(\lceil N/k\rceil-1)<N$，矛盾。

  要保证某盒至少$r$个，$k(r-1)$个时仍可每盒恰好$r-1$个，因此$k(r-1)+1$既足够又最小。定义域更大足以推出函数不单射；反过来，函数不单射不能推出定义域更大。

#### 构造盒子的三种方法（Three Ways to Construct Boxes）

- **【拓展】余数类（residue class）** 作盒子：两个数模n同余则差可被n整除。对$1,11,111,\ldots$的余数用鸽巢，或直接遇0余数，或两个相同余数相减，得到每个正整数都有一个仅含0、1的十进制正倍数。

- **【拓展】连续区间和（consecutive interval sum）** 先变前缀和（prefix sum）的差。

  例30天每天至少1场、总共至多45场：30个严格递增前缀和$a_j$与$a_j+14$共60数落在1至59，必跨组相等，故某连续天数正好14场。原证明对其他目标数是否适用要重验取值范围；

  证明失效不等于结论已被反驳。

- **因子分解（factorization）** 作盒子：$1,\ldots,2n$中的$n+1$个数写成$2^kq$，奇数q只有n种，两个共q者一个整除另一个。奇数核（odd part）而非数本身是盒子。

#### 生日问题与拉姆齐（Birthday Problem and Ramsey Theory）

- **生日问题（birthday problem）** ：保证同生日要考虑366种日期，367人才必然重复；这是必然性（certainty）。

  **【拓展】概率版本（probabilistic version）** 假设365天等可能且独立，n人至少一对同生日概率$1-\prod_{i=0}^{n-1}(365-i)/365$，n=23时约0.5073；“概率超过一半”不是“保证”。

- **拉姆齐数（Ramsey number）** $R(r,s)$是使任意红蓝边染色的完全图必含红$K_r$或蓝$K_s$的最小顶点数。$R(3,3)=6$：从一点的5条边至少3条同色；

  这3个邻点若有同色边，与原点成同色三角形，否则3条边全为另一色。五边形的边涂一种色、对角线另一色给出5点反例，故不能只证明上界6就直接写等号。

![[C6.2-K6二色染色必有同色三角形.png|510]]


- **【拓展】其他Ramsey结论（further Ramsey results）** ：$R(m,n)=R(n,m)$、$R(2,n)=n$、$R(4,4)=18$；教材$43\le R(5,5)\le49$仅保留为历史范围。指定花色凑$r$张须先计其他花色最多可拿多少，不能套“任意一种”的保证阈值。

- **【拓展】平移前缀和（shifted prefix sums）** ：$d$期每期至少1、总数至多$M$时，$1\le k\le2d-1-M$可由$d$个前缀和与其加$k$的平移强迫跨组相等，得连续区间恰$k$次；超出范围只说明该证明不保证。

#### 子序列定理（Monotone Subsequence Theorem）

- **子序列（subsequence）** 保留原顺序但可不连续；连续子串／连续子段（substring / contiguous segment）不可跳项。

  Erdős–Szekeres单调子序列定理（monotone subsequence theorem）：$n^2+1$个互异实数必有长$n+1$的严格递增或递减子序列。

  证明：给第$i$项标记以它结尾的最长递增、递减子序列长度$(I_i,D_i)$。若没有长$n+1$的任一类，则两坐标均在$1,\ldots,n$中，只有$n^2$种标签。$n^2+1$项中应有$i<j$标签相同；但两项互异，若$a_i<a_j$，可将$a_j$接在以$a_i$结尾的最长递增序列后，得$I_j\ge I_i+1$；若$a_i>a_j$，同理$D_j\ge D_i+1$。均与标签相同矛盾，故定理成立。互异条件不能漏，$n=3$时10项保证长4。

- **【拓展】拉姆齐理论的解释边界（limits of Ramsey-style conclusions）** ：规模足够大时保证某种结构存在，不保证该结构有预测价值。

  原笔记较大拉姆齐数的区间属于写作时的背景，不作为当前最新研究进展或本课程计算公式。

### 4.3 排列、组合与约束（Permutations, Combinations and Constraints）

授课依据：[[Ch6.2&Ch6.3.pdf|Ch6.2&Ch6.3.pdf]]、[[Ch6.5.pdf|Ch6.5.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

#### 排列与组合公式（Permutation and Combination Formulas）

- **r排列（r-permutation）** 为从n个不同对象无放回取r个并排序，$P(n,r)=n(n-1)\cdots(n-r+1)=n!/(n-r)!$；r组合（r-combination）只选不排，$C(n,r)=\binom nr=n!/[r!(n-r)!]$。

  $P(n,0)=\binom n0=1$，空排列是唯一一种；$\binom nr=0$约定用于整数$r<0$或$r>n$。

- $P(n,r)=\binom nr r!$源于每个无序子集对应$r!$种顺序；$\binom nr=\binom n{n-r}$源于选入与选出互补。锦标赛名次／不同职务要排列，无职务委员会要组合；先选人再分配职务可能两步都要。

#### 计算与应用（Calculation and Applications）

- 计算组合数可取$r\leftarrow\min(r,n-r)$，约分或用$\binom n{r+1}=\binom nr(n-r)/(r+1)$，避免先算巨大阶乘。阶乘与Stirling近似的区别见2.3。

- 位串恰有r个1为$\binom nr$；至少r个1为$\sum_{k=r}^n\binom nk$；两系分别选a、b人为$\binom{n_1}a\binom{n_2}b$；

  彩票匹配恰k个中奖号可用$\binom rk\binom{n-r}{r-k}$，全体结果为$\binom nr$（按题设抽取r号）。

- **课件委员会模型（courseware committee model）** ：10人选四人委员会为$\binom{10}4$；再设一名主席乘4，设两名无区别联席主席（co-chairpersons）乘$\binom42$。若另设三人委员会及一名主席，课件允许两委员会成员重合，故再乘$\binom{10}3\cdot3$；题目若要求不重合，第二组选人须改从剩余6人选。

#### 分组与相邻约束（Grouping and Adjacency Constraints）

- 【拓展】不同标签小组大小$n_1,\ldots,n_k$，总n人分组为$n!/(\prod_i n_i!)$；若等大小的组也不可区分，再除这些等类组的排列次数，不是所有分组一律除$k!$。

- **捆绑法（block method）** ：指定k人必须相邻，把他们当一块，与其他人一起排，再乘块内$k!$；指定内部顺序固定时不乘。

  【拓展】插空法（gap method）：先排其余m人有$m+1$空，k个指定人两两不相邻时选k空再排人，$m!\binom{m+1}k k!$；可行条件$k\le m+1$。

- 【拓展】相邻关系有重叠时用容斥，两个被禁止相邻对可能形成三人块；“至少一对相邻”的补集不总是“某指定一对相邻”。

  圆桌空隙为m而非$m+1$，固定旋转后为$(m-1)!\binom mk k!$（m个背景对象不同且$m\ge1$）。

![[C6-相邻约束的捆绑与插空.png|600]]

### 4.4 二项式系数与组合证明（Binomial Coefficients and Combinatorial Proofs）

授课依据：[[Ch6.2&Ch6.3.pdf|Ch6.2&Ch6.3.pdf]]。合并课件有Pascal、Vandermonde及曲棍球棒的证明；一般二项式展开与额外恒等式为拓展。

#### 二项式定理与恒等式（Binomial Theorem and Identities）

- **二项式系数（binomial coefficient）** $\binom nk$也就是$k$组合数；约定上指标$n\ge0$为整数、$\binom nk=0$当$k<0$或$k>n$，$\binom n0=\binom nn=1$。

| 课件恒等式（courseware identity） | 对象及条件 |
|---|---|
| 帕斯卡恒等式（Pascal's identity）：$\binom{n+1}k=\binom n{k-1}+\binom nk$ | 从$n+1$人选$k$，按固定一人入选与否分类 |
| 范德蒙德恒等式（Vandermonde's identity）：$\binom{m+n}r=\sum_{k=0}^r\binom mk\binom n{r-k}$ | 从两堆$m,n$人共选$r$；零值约定下$0\le r\le m+n$均可 |
| 曲棍球棒恒等式（hockey-stick identity）：$\sum_{j=r}^n\binom jr=\binom{n+1}{r+1}$ | $0\le r\le n$；按最大入选元素或最后一个1的位置分类 |

- **【拓展】二项式定理（binomial theorem）** ：$(x+y)^n=\sum_{k=0}^n\binom nkx^{n-k}y^k$（$n\ge0$整数）。代$1,1$、$1,-1$、$1,2$分别得系数和$2^n$、交替和0（$n\ge1$）、加权和$3^n$；Vandermonde取$m=n=r$得$\sum_k\binom nk^2=\binom{2n}n$。课件有上述三条恒等式，但未讲一般二项式展开定理。

#### 帕斯卡三角与证明方法（Pascal’s Triangle and Proof Methods）

- **帕斯卡三角（Pascal's triangle）** 两边为1，内部每数为上方相邻两数和；边界与递推共同确定整表。

- **组合证明（combinatorial proof）** 用同一对象集的不同计数或双射证明等式；包括双重计数证明（double-counting proof）、双射证明（bijective proof）。须解释每个因子、分类互斥且覆盖全部；代数证明（algebraic proof）不能替代题目指定的组合证明。

- **对称性证明（proof of symmetry）** ：从$n$元集合选$k$个与选剩余$n-k$个由取补一一对应，故$\binom nk=\binom n{n-k}$。

- **帕斯卡证明** ：固定$n+1$人中的$a$。包含$a$的$k$人组，另从$n$人选$k-1$；不含$a$则从$n$人选$k$。两类不交且无遗漏，相加即得恒等式。

- **Vandermonde证明** ：从不交的$m$人、$n$人两堆中共选$r$，总数$\binom{m+n}r$。按第一堆取$k$分类，第二堆取$r-k$，每类为$\binom mk\binom n{r-k}$；$k$不同互斥，求和覆盖全部。课件的$r\le\min(m,n)$是足够条件，采用零值约定后可扩至$r\le m+n$。

- **曲棍球棒证明** ：数长度$n+1$、含$r+1$个1的位串，总数$\binom{n+1}{r+1}$。若最后一个1在第$k$位，$r+1\le k\le n+1$，前$k-1$位取$r$个1，共$\binom{k-1}r$；令$j=k-1$，求和即得。位置不同互斥，且每个合法串有唯一最后一个1。

- **【拓展】其他组合结论（additional combinatorial results）** ：切换固定元素建立奇偶子集双射；三状态计嵌套集合对给$3^n$；任意$r$个连续整数的积被$r!$整除。中心二项式系数（central binomial coefficient）$\binom{2n}n$数等量上下步格路；反射原理（reflection principle）将越界路径与另一端点的无约束路径配对，用于卡特兰计数。

### 4.5 重复选择、物体分配与整数分拆（Repetition, Distribution and Integer Partitions）

授课依据：[[Ch6.5.pdf|Ch6.5.pdf]]。保留相邻／圆排列、星条、下界平移、无标号盒列举；Stirling通式与一般容量公式为拓展。

| 选择方式 | r次从n种中选择的结果数 |
|---|---|
| 有序、不可重复（ordered without repetition） | $P(n,r)$ |
| 无序、不可重复（unordered without repetition） | $\binom nr$ |
| 有序、可重复（ordered with repetition） | $n^r$ |
| 无序、可重复（unordered with repetition） | $\binom{n+r-1}r$，$n\ge1$ |

- **四种选择公式的证明要点（proofs of the four selection formulas）** ：不可重复的$r$-排列按位置有$n,n-1,\ldots,n-r+1$种选择；每个$r$-组合恰有$r!$个内部次序，所以$P(n,r)=r!\binom nr$。允许重复的有序选择每步仍有$n$种，得$n^r$；无序重复选择与$r$颗星、$n-1$根隔板的位置串一一对应，得$\binom{n+r-1}r$。

  【拓展】相同物体排列先临时贴标签计$n!$种，再除每类的内部置换数$\prod_i n_i!$；各盒规定人数时同理。相邻隔板和端点隔板已表示空类，无须再额外乘空盒的选择数。

#### 星条法与整数解（Stars and Bars and Integer Solutions）

- **星条法（stars and bars）** ：r颗相同星代表物体，$n-1$条隔板代表n类，允许相邻隔板与端点隔板，分别表示空类；共$r+n-1$个位置选r个为星。

  它计无序重复选择，不计每个具体物体的身份。

- **弱组合（weak composition）** $x_1+\cdots+x_n=r,x_i\ge0$有$\binom{r+n-1}{n-1}$解；

  正整数解（positive integer solution）$x_i\ge1$有$\binom{r-1}{n-1}$解（$r\ge n$）。一般下界$x_i\ge l_i$先作$y_i=x_i-l_i$，剩余和为$r-\sum l_i$；

  剩余负则0解。

- **【拓展】有上界（upper bounds）** 时星条法不能直接用；

  对违反$x_i\le u_i$的情况作容斥，集合S中变量统一减$u_i+1$：$\sum_{S\subseteq\{1,\ldots,n\}}(-1)^{|S|}\binom{r-\sum_{i\in S}(u_i+1)+n-1}{n-1}$，上方不足$n-1$的项按0处理。

#### 重复物体与循环计数（Repeated Objects and Loop Counts）

- **【拓展】重复物体排列（permutations with indistinguishable objects）** 为多项式系数（multinomial coefficient）$n!/(n_1!\cdots n_k!)$，$\sum n_i=n$；各类内部交换不产生新排列。嵌套循环（nested loops）满足$1\le i_m\le\cdots\le i_1\le n$时次数$\binom{n+m-1}m$，严格不等时$\binom nm$。

- **物体与盒子的分类（classifying objects and boxes）** ：课件要求先问物体可区分／不可区分（distinguishable / indistinguishable）、盒子有无标签、可否空盒及容量。相同物体进有标号盒用星条法；相同物体进相同盒须忽略盒序，按分拆列举。

![[C6.5-星条法示意图.png|600]]

#### 【拓展】物体入盒与划分公式（Distribution and Partition Formulas）

- **【拓展】通用入盒公式（general distribution formulas）** ：$n$个有身份物体进$k$个有标号盒，允许空为$k^n$、固定各盒人数为$n!/\prod n_i!$、各盒非空为$k!S(n,k)$；无标号非空盒为$S(n,k)$，至多$k$盒为$\sum_{j=0}^{\min(n,k)}S(n,j)$。第二类Stirling数见3.5；$S(n,k)=\frac1{k!}\sum_{i=0}^k(-1)^i\binom ki(k-i)^n$（$n,k\ge1$）。这些一般公式未在课件展开。

#### 分拆、容量与边界（Integer Partitions, Capacities and Boundaries）

- **整数分拆（integer partition）** 不计盒序，写非增的装量；允许空盒时末尾补0。课件6本相同书进4个相同盒，9种为$(6,0,0,0),(5,1,0,0),(4,2,0,0),(4,1,1,0),(3,3,0,0),(3,2,1,0),(3,1,1,1),(2,2,2,0),(2,2,1,1)$。

- **课件混合水果例（mixed-fruit example）** ：3苹果A、2橘子O、1香蕉B进3个相同盒，每盒2个。按B的同盒水果分类：$\{AB,AA,OO\}$、$\{AB,AO,AO\}$、$\{BO,AA,AO\}$，共3种。不能仅按总水果数6作整数分拆，因为还须保留类型。

> [!warning] 【易错】
> 无标号盒不能把有标号计数一律除$k!$，不同装法的重复次数可能不同。0物体用唯一空分配处理；$S(0,0)=1$。

### 4.6 生成排列与组合的算法（Algorithms for Generating Permutations and Combinations）

授课依据：[[Ch6.6.pdf|Ch6.6.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

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

#### 下一个位串：二进制加一（Next Bit String: Binary Increment）

**下一个位串（next bit string）** ：从右向左将末尾连续1改成0，遇第一个0改成1，等价于二进制加1（binary increment）。全1已是最后一个；

从全0开始会遍历$2^n$个子集的特征串，但普通加1不保持1的个数，不能直接当固定r组合后继。

- **【拓展】二进制加一的代价（cost of binary increment）** ：单次最坏翻转$n$位，时间$O(n)$；遍历全部$n$位串时，各位分别约每$1,2,4,\ldots$次翻转，所有翻转次数之和小于$2\cdot2^n$，因此不计输出时摊销代价（amortized cost）为$O(1)$。若每次打印全部$n$位，输出总量仍为$\Theta(n2^n)$。

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

- 从右找未顶格位置，增加1，再把后缀填成连续递增最小值；循环从$i+1$开始，不能覆盖刚加1的$a_i$。原教材过程限定非最大真子集，本提纲加了停止检查以显式处理$r=0,n$。

- **小规模演算（small example）** ：$n=4,r=2$时$12\to13\to14\to23\to24\to34$；$n=5,r=3$时$123,124,125,134,135,145,234,235,245,345$。换成a至e字母，逐位替换即可，顺序不变。

- **组合后继最小性的证明（minimality proof for next combination）** ：$i$为最右未顶格位置。候选把$a_i$加1，并令后续为连续最小整数，因此仍严格递增，末项不超过$n$。任意更大组合$b$的第一次分歧位置$p$不可能大于$i$，因为这些位置原本已达上限$n-r+p$；若$p<i$则$b$已超过候选，若$p=i$则$b_i\ge a_i+1$，相等时其后缀也不小于候选的连续最小后缀。因此候选是唯一最小的更大组合。

- **【拓展】组合顺序与位串顺序（combination order versus bit-string order）** ：固定$r$且把元素1的成员位放在最左侧高位时，递增元组的词典序与特征位串的整数值顺序正好相反。例如$n=4,r=2$时，组合$12<13$，对应$1100_2>1010_2$。若低位对应元素1，结论的方向须重验，不能脱离编码约定说“天然相同”。

#### 全部枚举与不重不漏（Complete Enumeration without Repetition）

- **生成全部r排列（generate all r-permutations）** ：先遍历$\binom nr$个组合，每组内部再列r!个排列，总$P(n,r)$个，不重不漏，因为每个排列所属底集唯一。

  **这种分组输出不保证全部r排列整体按词典序** ，只保证组合组序及各组内部序。

- **不重不漏证明（completeness and uniqueness）** ：从最小对象开始，后继严格增加且是最小更大者，最大对象停；有限全序中因此恰遍历全部对象。不能只凭“数量对了”断言没重复没遗漏。

  组合特征位串的二进制顺序与递增元组词典序也须区别，不能混接两种后继。

---

## 五、递推关系的应用（Applications of Recurrence Relations）

### 5.1 建模与初始条件（Modeling and Initial Conditions）

授课依据：[[Ch8.1.pdf|Ch8.1.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

本章范围是已有的§8.1；没有把尚未整理的§8.2–8.6扩写成新章节。第19节课堂讲了递推定义、代入验证、复利、兔子、汉诺塔及受限位串；

码字、卡特兰数、讲座调度在原笔记中已补足，以下同样完整保留并标为拓展。

#### 建模检查（Modeling Checks）

- **模型（model）** 先定义$a_n$数什么、单位是什么、n从哪里开始；再写初值、递推式与适用下标。每个分支须互斥且完备；删去／追加部分要能双向对应并保证接缝合法。

  求通项（find a closed form）与建立递推（form a recurrence）是不同任务。

- **候选解验证（verification of a candidate solution）** 直接代入并检查全部初值。

  例如$a_n=2a_{n-1}-a_{n-2}$允许$3n$与常数5，但不允许$2^n$，因为后者右侧是$3\cdot2^{n-2}$，不同于$4\cdot2^{n-2}$，任何n都不相等。

  初值$a_0=3,a_1=5$时，减法递推$a_n=a_{n-1}-a_{n-2}$给$a_2=2,a_3=-3$，不要看成加法。

- **【拓展】细菌翻倍（bacterial doubling）** $a_n=2a_{n-1},a_0=5$得$5\cdot2^n$。

- **复利（compound interest）** $S_n=(1+r)S_{n-1},S_0=P$得$P(1+r)^n$。时间单位、计息时刻改变时须重验下标。

### 5.2 兔子与汉诺塔（Rabbits and the Tower of Hanoi）

授课依据：[[Ch8.1.pdf|Ch8.1.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

#### 兔子模型（Rabbit Model）

- **兔子繁殖（rabbit population）** ：按原模型幼兔满两个月才繁殖、无死亡，$f_1=f_2=1$，$f_n=f_{n-1}+f_{n-2}$（$n\ge3$）。分为上月已有与本月新生，不能假定所有幼兔立即翻倍；

  不同月龄计数约定会改变初值。

#### 三柱汉诺塔（Three-peg Tower of Hanoi）

- **三柱汉诺塔（three-peg Tower of Hanoi）** ：n个大小不同圆盘，单次搬一个且大盘不能压小盘。把前$n-1$盘搬开、移动最大盘、再搬回小盘，得可行上界$H_n\le2H_{n-1}+1$；

  任何解移动最大盘前后都需搬开／恢复小盘，得同样下界，故$H_n=2H_{n-1}+1,H_0=0$，解为$2^n-1$。仅给构造不能证明最少（minimum）。

  64盘需$2^{64}-1$次，展示指数增长（exponential growth）。

#### 【拓展】四柱变式（Four-peg Variant）

- **【拓展】四柱汉诺塔（four-peg Tower of Hanoi）** 的Frame–Stewart策略取$T_4(n)=\min_{0\le k<n}(2T_4(k)+2^{n-k}-1)$，$T_4(0)=0$；四柱最优性已证，不能外推到任意柱数，也不把教材旧说“尚未解决”当现状。

### 5.3 受限位串与状态（Restricted Bit Strings and States）

授课依据：[[Ch8.1.pdf|Ch8.1.pdf]]。课件用互斥后缀1／10／100建模，完整递推与初值保留；一般自动机状态法为拓展。

#### 禁止00与禁止000（Forbidding 00 and 000）

- **不含00（no consecutive zeros）** ：合格n串按末尾1或10分类，$a_n=a_{n-1}+a_{n-2}$，$a_0=1$计唯一空串（empty string），$a_1=2$，得$1,2,3,5,8,13,\ldots$，$a_n=f_{n+2}$。

  只在合法短串后任添0会产生非法接缝，不能两类均算$a_{n-1}$。不含11的计数可通过0、1互换得到同型递推。

- **不含000（no three consecutive zeros）** ：末尾为1、10、100三类；$b_n=b_{n-1}+b_{n-2}+b_{n-3}$，$b_0=1,b_1=2,b_2=4$，从$n=3$适用得$b_3=7,b_4=13,b_5=24,b_6=44$。

  若采用原笔记$b_1,b_2,b_3$作初值，则递推从$n=4$开始。

#### 【拓展】状态与转移（States and Transitions）

- **【拓展】状态转移（state transition）** 按末尾连续0的个数建有限状态机（finite-state machine, FSM）或自动机（automaton），可由转移矩阵（transition matrix）统一求受限位串数；课件本身用互斥的1、10、100后缀分类，无须额外算法才能完成对应题。

> [!info]- 【拓展】原图回看
> ![[C8-三连零的状态转移.png|580]]

### 5.4 【拓展】码字与卡特兰数（Codewords and Catalan Numbers）

【拓展】全部补充课件中未见本节的独立讲解，保留压缩说明供回查。

#### 【拓展】偶数零码字（Codewords with Even Numbers of Zeros）

- **【拓展】偶数零码字（codewords with even numbers of zeros）** ：十进制长$n$串中0个数为偶者，$a_0=1$、$a_n=8a_{n-1}+10^{n-1}$，闭式$(10^n+8^n)/2$。按末位0／非0及前缀奇偶分类即可建立递推。

#### 【拓展】卡特兰递推与闭式（Catalan Recurrence and Closed Form）

- **【拓展】卡特兰数（Catalan numbers）** 数合法括号串、二叉结构或不越界格路，$C_0=1$、$C_n=\sum_{k=0}^{n-1}C_kC_{n-1-k}=\binom{2n}n/(n+1)$。递推按首对括号内部规模分类；闭式以反射原理从全部格路扣掉越界路径。朴素填表$O(n^2)$，不把这些补充推导当作Ch8.1课件内容。

- **【拓展】等价计数对象（equivalent counting objects）** 包括保持因子顺序的完整加括号（full parenthesization）、合法括号串（balanced parentheses）、Dyck路径（Dyck paths）及适当的二叉树形（binary tree shapes）；生成函数（generating functions）可求闭式，但此方法未在课件讲解。

> [!info]- 【拓展】原图回看
> ![[C8-卡特兰数的合法与非法路径.png|560]]

### 5.5 【拓展】动态规划与加权区间调度（Dynamic Programming and Weighted Interval Scheduling）

【拓展】全部补充课件中未见本节的独立讲解，保留压缩说明供回查。

#### 【拓展】动态规划的两个条件（Conditions for Dynamic Programming）

- **【拓展】动态规划（dynamic programming, DP）** 利用最优子结构（optimal substructure）与重叠子问题（overlapping subproblems），采用记忆化（memoization）或填表（tabulation）。分治（divide and conquer）同样拆子问题，但不以重叠为必要特征；递归（recursion）须有可达终止条件（termination condition）。保存汉诺塔步数能省重复计算，不能省掉实际输出$2^n-1$次移动。

#### 【拓展】调度建模与递推（Scheduling Model and Recurrence）

- **【拓展】加权区间调度（weighted interval scheduling）** ：按结束时间排活动，前驱（predecessor）$p(j)=\max\{i<j:e_i\le s_j\}$、空集取0；端点相接视为相容（compatible）。$T(0)=0$、$T(j)=\max\{T(j-1),w_j+T(p(j))\}$，分别对应不选／选第$j$场；替换论证（replacement argument）保证所配子方案也最优。

#### 【拓展】贪心反例（A Counterexample to the Greedy Choice）

- **【拓展】最早结束贪心（earliest-finish-time greedy choice）** 可最大化场次数，却不能保证最大权重；两场各10权与覆盖二者时间的一场100权即为反例。总人次（total attendances）也不等于去重听众数（number of distinct attendees）。原题权重组(a)填表最优110，取$\{1,3,7\}$。

> [!info]- 【拓展】原图回看
> ![[C8.1-讲座时间轴与相容前驱.png|650]]

#### 【拓展】方案恢复、平局与效率（Reconstruction, Ties and Efficiency）

- **【拓展】恢复方案（reconstruction）** 从$j=n$倒推，若$w_j+T(p(j))\ge T(j-1)$可选$j$并跳到$p(j)$，否则$j\leftarrow j-1$；两种编号均严格下降，最终到0停止。平局（tie）可有不同最优解，不表示该活动必选。原其余权重组(b)、(c)、(d)最优分别140、20、40。

- **【拓展】效率（efficiency）** ：已有$p(j)$时填表、恢复均$O(n)$；含排序和二分求前驱总$O(n\log n)$，逐项扫描求前驱则可到$O(n^2)$。Ch8.1课件止于兔子、汉诺塔和两类受限位串，没有这套调度算法。

## 六、图论（Graph Theory）

> [!tip] 【老师强调：第19、21节】
> 第十章是期末重点；第21节还要求未在课堂逐个展开的例题自行练习。以下不凭“课堂跳过”删去某一节，也不把充分条件当充要条件。

### 6.1 图的类型与建模（Graph Types and Modeling）

授课依据：[[Ch10.1.pdf|Ch10.1.pdf]]。以下保留课件实际出现的内容；夹列的范围外独立结论另标“拓展”。

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

#### 方向、权重与模型（Direction, Weights and Models）

- **有向图（directed graph / digraph）** 用有序对表示弧（arc），$(u,v)$与$(v,u)$一般不同；无向图（undirected graph）端点无序。简单图（simple graph）无重边、自环，多重图（multigraph）允许重边，伪图（pseudograph）还允许自环；本课具体约定见前表。

- **带权图（weighted graph）** 为边附权重（weight），可表示路程、费用等；“有权”与“有方向”是不同维度。

- **【拓展】图模型（graph models）** 可按题意建立通信网络（communication network）、社交网络（social network）、合作图（collaboration graph）、网页图（web graph）、先后依赖图（precedence graph）、竞赛图（tournament graph）；混合图（mixed graph）严格指并存有向边和无向边，课件分类表误将带自环的有向情形直接称mixed，不照抄该错误。

- **有向边的端点（endpoints of a directed edge）** ：$(u,v)$中$u$是起点（initial vertex）、$v$是终点（terminal / end vertex）；课件称$u$邻接到$v$（$u$ is adjacent to $v$），$v$邻接自$u$（$v$ is adjacent from $u$），不推出反方向。

#### 【拓展】模型计数与交集图（Counting in Models and Intersection Graphs）

- **【拓展】模型计数与交集图（model counts and intersection graphs）** ：点代表对象、边代表给定关系，不能把纸上交叉当新顶点。同代图（contemporaneous graph）以生命区间相交连边，是区间交集图（interval intersection graph）；无向简单邻接关系对称且反自反，重边不能只用有序对集合记录。

- **【拓展】其他模型术语（additional graph-model terminology）** ：相识图（acquaintanceship graph）、影响图（influence graph）、呼叫图（call graph）、引用图（citation graph）、模块依赖图（module dependency graph）、航空图（airline graph）、道路网络（road network）、生态位重叠图（niche overlap graph）、蛋白质相互作用图（protein interaction graph）。循环赛图（round-robin tournament graph）给比赛方向，单淘汰赛树（single-elimination tournament tree）为有根树（rooted tree）；稀疏（sparse）只描述相对点数较少的边。

### 6.2 度、图族、二分图与匹配（Degrees, Graph Families, Bipartite Graphs and Matchings）

授课依据：[[Ch10.2.pdf|Ch10.2.pdf]]。度序列和标准图族属于范围内；Hall匹配、网络拓扑、平均度和一般无奇圈算法为拓展。

#### 邻接、度与握手定理（Adjacency, Degree and Handshaking）

- **邻接（adjacency）** 指两顶点由边相连；关联（incidence）指边以某点为端点（endpoint）。邻域／邻点集（neighborhood / neighbor set）$N(v)$含其邻接顶点，$N(S)=\bigcup_{v\in S}N(v)$。

- **度（degree）** $\deg v$数关联端点次数：重边逐条计，自环计2，故不总等于$|N(v)|$。孤立点（isolated vertex）度0，悬挂点／叶（pendant vertex / leaf）度1；最大／最小度（maximum / minimum degree）记$\Delta,\delta$。

- **握手定理1（handshaking theorem 1）** ：有限无向图$\sum_v\deg v=2|E|$，重边、自环均适用。证明：逐边计关联端点，每边恰贡献2。10个点均6度时，$2e=60$，故$e=30$。

- **握手定理2（handshaking theorem 2）** ：奇度顶点（odd-degree vertex）数为偶。证明：度和为偶，减去所有偶度项仍为偶；奇数项之和要为偶，其项数只能是偶。不是说每个顶点都偶度。

- **【拓展】平均度与正则图（average degree and regular graph）** ：$v>0$时$\overline d=2e/v$，$\delta\le\overline d\le\Delta$；$r$正则（$r$-regular）每点度$r$，故$rv=2e$。图神经网络（graph neural network, GNN）的平均聚合（mean aggregation）可写$H'=\sigma(\widehat D^{-1}\widehat AHW)$，按行和作度归一化（degree normalization）；度分布（degree distribution）、幂律（power law）、重尾（heavy tail）为额外网络统计背景。

- **【拓展】GNN记号（GNN notation）** 中$H$为特征、$W$为权重矩阵（weight matrix）、$\sigma$为激活函数（activation function），$\widehat A=A+I$、$\widehat D$为$\widehat A$行和的对角矩阵；这一层的“度”按行和约定，不把自环重复计数代入归一化。

#### 有向度与标准图族（Directed Degrees and Standard Families）

- **有向图入度（in-degree）** $\deg^-(v)$与出度（out-degree）$\deg^+(v)$分别数进入与离开的弧，自环各贡献1；$\sum_v\deg^-v=\sum_v\deg^+v=|E|$。

  【拓展】底层无向图（underlying undirected graph）去掉方向；本课程保留每条弧的身份与重数，因此反向的两条弧变为两条平行边，且$\deg_{\mathrm{underlying}}(v)=\deg^-(v)+\deg^+(v)$。自环在右边贡献$1+1$，与无向度计2一致。若题目另要求合并平行边成简单图，这个等式不再直接适用。

| 图族（graph family） | 点数v | 边数e | 度与补充 |
|---|---|---|---|
| 完全图（complete graph）$K_n$ | n | $n(n-1)/2$ | 每点$n-1$ |
| 圈图（cycle graph）$C_n$，$n\ge3$ | n | n | 每点2 |
| 轮图（wheel graph）$W_n$，本书由$C_n$加中心 | $n+1$ | $2n$ | 中心n，轮缘各3 |
| n维超立方体（n-cube / hypercube）$Q_n$ | $2^n$ | $n2^{n-1}$（$n\ge1$） | n正则，位串差一位相邻 |
| 完全二分图（complete bipartite graph）$K_{m,n}$ | $m+n$ | mn | 两侧度分别n、m |
| 【拓展】路径图（path graph）$P_n$ | n | $n-1$ | $n\ge2$时两端度1，其余度2 |

- 课件轮图下标$n$表示轮缘点数，不包括中心；别的书可能用$W_{n+1}$表示同一对象。课件slide 18把$C_1$画成单点自环、$C_2$画成两点两条平行边，slide 19的$W_1,W_2$继承这些边，再加中心和辐条；它们不属于上表$n\ge3$的简单图范围。若题目采用这些低阶课件图，须按图数度数、边数，自环图不能作通常合法顶点着色。slide 23称$C_1$为二分的例外与其自环图矛盾，不作为正确结论。$Q_0$为单点，$Q_{n+1}$由两份$Q_n$逐一连对应顶点构造，等价于位串恰差一位相邻。

- **标准图族的结构定义（structural definitions of standard graph families）** ：

  | 图族（family） | 构造／邻接规则（construction / adjacency rule） |
  |---|---|
  | 完全图（complete graph）$K_n$ | $n$个顶点的每一对不同顶点之间恰有一条边 |
  | 圈图（cycle graph）$C_n$，$n\ge3$ | 顶点$v_1,\ldots,v_n$，仅有$v_iv_{i+1}$及$v_nv_1$，首尾相接成一个圈 |
  | 轮图（wheel graph）$W_n$，$n\ge3$ | 在$C_n$外加一个中心，并把中心与全部$n$个圈上顶点相连 |
  | 超立方体（hypercube）$Q_n$ | 顶点为全部$n$位二进制串；两顶点恰好一位不同才相邻 |
  | 完全二分图（complete bipartite graph）$K_{m,n}$ | 两侧分别有$m,n$点，同侧无边，每一对跨侧顶点之间都有一条边 |
  | 【拓展】路径图（path graph）$P_n$，$n\ge1$ | 顶点$v_1,\ldots,v_n$，仅连相邻编号$v_iv_{i+1}$；$P_1$为单点 |

  点边数或度数表不能代替结构定义；例如多个不交圈同样每点度2，却不是单个$C_n$。

- **【拓展】星图（star graph）** 为$K_{1,n}$（$n\ge1$）：一个中心与$n$个叶子相连，叶子之间无边。共$n+1$点、$n$边，中心度$n$、各叶度1，是星形网络的图模型；$K_{n,n}$为$n$正则二分图，$K_{2,2}\cong C_4$。

- **握手定理的证明要点（proof of the handshaking theorems）** ：无向图按顶点数关联端点，每边贡献2，故$\sum\deg v=2e$，减去偶度项后奇度项的和为偶，奇度项个数也必偶。有向图每条弧恰贡献一次出度和一次入度，得两总和均为$e$；自环仍满足这些端点计数。

- **完全有向图（complete directed graph）** 的每对不同顶点之间两个方向的弧均存在，无自环时有$n(n-1)$条弧；不能与无向$K_n$的$n(n-1)/2$边混算。

#### 二分图的判定（Bipartite Tests）

- **二分图（bipartite graph）** 的顶点可划为不交的$V_1,V_2$，所有边均跨两侧；$(V_1,V_2)$称二分划分（bipartition）。课件判据：简单图二分，当且仅当能用至多两色使邻点异色。证明：划分两侧各染一色，反向按颜色分组即可。

- **课件例（courseware examples）** ：$C_n$（$n\ge3$）当且仅当$n$偶时二分；沿圈交替染色，奇圈末点会与起点冲突。含三角形的图不二分；$K_{m,n}$同侧无边、跨侧全连，是完全二分图（complete bipartite graph），边数$mn$。没有边的非空二分图只需1色，不能无条件写色数2。

- **【拓展】无奇圈判据（no-odd-cycle criterion）** ：图二分当且仅当无奇圈；按BFS距离奇偶分层可证反向。BFS／DFS两色判定须遍历所有分量。一般简单二分图$e\le|V_1||V_2|\le\lfloor v^2/4\rfloor$，$r>0$的正则二分图两侧等大，$r=0$无此结论。

#### 【拓展】匹配、Hall与代表系（Matching, Hall and SDR）

- **【拓展】匹配（matching）** 为不共端点的边集；极大（maximal）不能再加边，最大（maximum）边数最多。饱和（saturate）表示覆盖指定顶点，完美匹配（perfect matching）覆盖全部顶点；教材的单侧完全匹配（complete matching）只配满指定侧。

- **【拓展】Hall婚姻定理（Hall's marriage theorem）** ：有限二分图可配满左侧，当且仅当每个左侧子集$A$满足$|N(A)|\ge|A|$；相异代表系（system of distinct representatives, SDR）是等价集合表述。缺额（deficiency）$d(A)=|A|-|N(A)|$，最大匹配大小为$|L|-\max_{A\subseteq L}d(A)$。

- **【拓展】增广路（augmenting path）** 两端未匹配，非匹配边与匹配边交替，翻转使边数加1；匹配最大当且仅当无增广路。匈牙利法（Hungarian method）的名称须按无权匹配／带权指派语境区分。Kőnig定理（Kőnig's theorem）称二分图最大匹配数等于最小顶点覆盖（vertex cover）大小，$\nu=\tau$；不同于支配集。

#### 【拓展】网络拓扑（Network Topologies）

- **【拓展】网络拓扑（network topology）** ：局域网（local area network, LAN）的星形（star）、环形（ring）、总线（bus），以及并行互连（parallel interconnection）的线性阵列（linear array）、网格（mesh）、超立方体，按链路数、最大度、通信跳数（hop count）取舍。未在补充课件展开。

### 6.3 图的运算、补图与度序列（Graph Operations, Complements and Degree Sequences）

授课依据：[[Ch10.2.pdf|Ch10.2.pdf]]、[[Ch10.3.pdf|Ch10.3.pdf]]。补图、自补图和Q3的6个Q2子图均在课件；诱导子图通式与度序列实现算法为拓展。

#### 子图与图运算（Subgraphs and Graph Operations）

- **子图（subgraph）** $H=(W,F)$满足$W\subseteq V,F\subseteq E$且边端点都在W中；生成子图（spanning subgraph）保留全部顶点；

  【拓展】诱导子图（induced subgraph）$G[W]$保留W内原有全部边。删点（vertex deletion）同时删关联边；删边（edge deletion）保留点。

  真子图（proper subgraph）是与原图不同的子图，即至少删了一个顶点或一条边；生成子图也可能是真子图，诱导子图也可以等于原图。

  【拓展】边收缩（edge contraction）把一条边两端粘合，并按题设处理新自环、平行边。

- **并图（union of graphs）** 取点边集合并，交图（intersection）取交；不交并（disjoint union）先保证点集互不相交。

  联图（join of graphs）$G+H$在不交并基础上加上全部跨图边：点$v_G+v_H$、边$e_G+e_H+v_Gv_H$，G侧顶点度加$v_H$，H侧加$v_G$。

- **笛卡尔积图（Cartesian product of graphs）** $G\square H$顶点为$(g,h)$；只有“一坐标相同、另一坐标相邻”才连边，不能两坐标同时变。

  点数$v_Gv_H$，边数$e_Gv_H+e_Hv_G$；$\deg(g,h)=\deg_Gg+\deg_Hh$。$P_m\square P_n$是网格，$Q_{r+s}\cong Q_r\square Q_s$。

> [!tip] 【老师强调：第20节转写约L501–521】
> 老师说很可能在图的运算这里出期末题，尤其join与Cartesian product，但随后明确未承诺一定作为题目。手算应同时会画图、算点边数、算新度数。

![[C10-join与笛卡尔积.png|650]]

#### 补图、自补图与子图计数（Complements, Self-complementarity and Subgraph Counts）

- **补图（complement）** $\overline G$与$G$同点集，在不同顶点原来不邻接时连边：$e(\overline G)=\binom v2-e(G)$、$\deg_{\overline G}x=v-1-\deg_Gx$。$G\cup\overline G=K_v$；例如$\overline{C_4}=2K_2$，$\overline{K_{m,n}}=K_m\cup K_n$。

- **自补图（self-complementary graph）** 满足$G\cong\overline G$。课件比较$C_4$与其补图不相同构，$C_5$与其补图同构；要给保持邻接的双射，不是图画相像即可。

- **课件立方体子图例（cube-subgraph example）** ：$Q_3$有6个$Q_2$方形面，不能只数投影画法中的内外两个框。

- **【拓展】一般计数（general counting）** ：$Q_n$的$k$维坐标面（coordinate face）有$\binom nk2^{n-k}$个；非空点集任意子图数为$\sum_{\varnothing\ne W\subseteq V}2^{e(G[W])}$，允许空点集的诱导子图有$2^v$个。自补必要条件为$v\equiv0,1\pmod4$，不充分保证给定图自补。

#### 度序列与【拓展】实现判据（Degree Sequences and Realization Criteria）

- **度序列（degree sequence）** 将各点度按非增顺序列出，课件$(2,3,2,2,0,1)$应排序为$(3,2,2,2,1,0)$。握手定理要求总和偶；简单图还须每项$\le v-1$。这些仅为必要条件，不能据此直接判可实现。

- **课件的重边边界（parallel-edge boundary）** ：$(5,5,4)$在3点简单图不可实现，但允许重边可取前两点间3条边、它们到第三点各2条边。课件此处的“Yes”须保留图类型条件。

- **【拓展】图形序列（graphic sequence）** 指简单图可实现的非负整数序列。Havel–Hakimi算法（Havel–Hakimi algorithm）删最大项$d$、对余下最大$d$项各减1后重排，全0成功，负数或越界失败；Erdős–Gallai判据（Erdős–Gallai criterion）为和偶且各$k$满足$\sum_{i=1}^kd_i\le k(k-1)+\sum_{i>k}\min(d_i,k)$。伪图允许自环重边时只需和偶；简单图至少两点时必有两点同度。

### 6.4 图的表示与同构（Graph Representations and Isomorphism）

授课依据：[[Ch10.3.pdf|Ch10.3.pdf]]。Ch10.3正文实际只讲同构、自补及不变量例；邻接／关联表示和谱判据为拓展。

#### 【拓展】表示法与自环约定（Representations and Loop Conventions）

- **【拓展】图的表示（graph representations）** ：邻接表（adjacency list）用$O(v+e)$空间；邻接矩阵（adjacency matrix）$A$按点对记录边重数，用$O(v^2)$；关联矩阵（incidence matrix）按点×边，用$O(ve)$。这些图表示细节没有在Ch10.3课件展开；关系的零一矩阵则是范围内内容，见3.3。

- **【拓展】自环约定（loop conventions）** ：本教材邻接矩阵自环对角计1，度却计2，故有自环时行和不能直接当度；无向无自环图的0/1关联矩阵满足$MM^T=D+A$，$D$为度对角矩阵（degree diagonal matrix）。有向邻接矩阵行和为出度、列和为入度。

> [!info]- 【拓展】原图回看
> ![[C10.3-原图-关联矩阵一例.png|560]]

#### 同构的定义、排除与证明（Defining, Refuting and Proving Isomorphism）

- **图同构（graph isomorphism）** 为顶点双射$f:V_G\to V_H$，同时保留邻接与非邻接，简单图写$uv\in E_G\iff f(u)f(v)\in E_H$；有向图还须保持方向，多重图保持重数和自环。

  图相等（equality of graphs）要求标签相同，同构允许改名。同构本身是等价关系。

- **同构不变量（isomorphism invariant）** ：课件明确列出点数、边数和度序列；任一不同即不同构，全部相同仍不足以证明同构。$C_6$与$C_3\cup C_3$同为6点6边2正则却不同构，是原笔记的“魔鬼对（devil's pair）”反例。

  【拓展】入出度、分量、圈长度／数量、三角形数、邻点度分布、割点、二分性、距离也保持；用于排除，不能反向当作一般充分判据。

- **证明同构须给完整双射并核对边与非边** 。双射$f$确定后逐条验证$uv\in E_G\iff f(u)f(v)\in E_H$；只试一次对应失败，不能证明不存在其他对应。

  【拓展】置换矩阵（permutation matrix）$P$可写$A_H=PA_GP^T$，须用同一顶点置换重排行列；补图与反向图保持同构。

  验证给定双射只需多项式比较，暴力找映射可达$v!$个候选；

  【拓展】原笔记介绍图同构的准多项式算法（quasipolynomial-time algorithm），不把“没有简单充分判据”误说成绝无充要定义。

![[C10.3-同构即重排行列.png|620]]


- **【拓展】矩阵判据与谱不变量（matrix criterion and spectral invariants）** ：存在置换矩阵（permutation matrix）$P$使$B=P^TAP$当且仅当对应图同构；谱（spectrum）、秩（rank）、行列式（determinant）、迹（trace）由此保持，但相同仍不充分。$K_{1,4}$与$C_4\cup K_1$同谱而不同构；图同构判定不等于已证明只能枚举全部$n!$映射。

#### 【拓展】反向图、带宽与计数（Converse, Bandwidth and Counting）

- **【拓展】反向图（converse digraph）** 反转全部弧，对应邻接矩阵转置；不自动与原图同构。带宽（bandwidth）是在顶点编号中最小化相邻点编号差的最大值，依赖编号。

- **【拓展】有标签／非同构图计数（labeled / nonisomorphic graph counts）** ：$n$点有标签简单图有$2^{\binom n2}$个；非同构图不能一律除$n!$，因自同构（automorphism）数不同。2、3、4点分别有2、4、11类。

- **【拓展】矩阵重排（matrix reordering）** ：无向图按分量排列邻接矩阵为分块对角（block diagonal）形式；Cuthill–McKee重排序（Cuthill–McKee ordering）是减小带宽的启发方法，不保证任意图均最优。

### 6.5 路径、连通性、树与网络可靠性（Paths, Connectivity, Trees and Reliability）

授课依据：[[Ch10.4.pdf|Ch10.4.pdf]]、[[Ch10.5.pdf|Ch10.5.pdf]]。保留路径、简单路径、连通、树的定理及MST定义；桥是Fleury所需前置定义，其余可靠性理论为拓展。

> [!warning] 【考试注意：术语约定】
> 本提纲按Ch10.4课件：path允许重复，simple path要求顶点不重复；只要求边不重复的路线另称迹（trail）。教材将simple path用于不重复边的另一约定，作为术语差异保留，答题先依课件及题目说明。
>
> 树中的“无圈”排除真正的简单圈，不把同一条无向边立即往返当作圈。哈密顿回路仅允许末尾复写起点。

#### 路径与连通性的语言（Language of Paths and Connectivity）

- **路径（path）** 按课件为相邻顶点序列，长度（length）等于边数，允许重复；简单路径（simple path）要求所有顶点不同。回路（circuit / cycle）为正长度闭合路径；简单圈（simple cycle）除首尾相同外顶点互异。无向单边往返不作为树中的圈。

- **连通（connected）** ：无向图任意两点有路径；连通分量（connected component）是极大连通部分。重复顶点段可删除，故有路径就有简单路径。强连通（strongly connected）要求有向图每对点双向可达；弱连通（weakly connected）只要求去方向后连通。

- **无环（acyclic）** ：没有圈；有向无环图（directed acyclic graph, DAG）无有向圈，去方向后可能有无向圈，不能混淆。

- **【拓展】强连通分量（strongly connected component, SCC）** 按互达划分，缩点（condensation）后成DAG；Kosaraju算法（Kosaraju's algorithm）两遍DFS、Tarjan算法（Tarjan's algorithm）用低链接值（low-link value）与栈，均$O(v+e)$。课件只讲强／弱连通定义，没有这些求分量算法。

#### 极小性、树与生成树（Minimality, Trees and Spanning Trees）

- **极小／极大（minimal / maximal）** 总是相对于具体性质：极小连通图（minimally connected graph）删任一边就不连通，是树；

  极大无圈图（maximal acyclic graph）若仍可加边连不同分量则不极大，固定非空点集时极大无圈即树。极大不等于最大（maximum），定义性质不能省略。

- **树（tree）** 为连通、无圈的简单无向图；森林（forest）为无圈图，可有多个分量。n点树有$n-1$边，任意两点间唯一不重复顶点路径；每边是桥；n≥2时至少两个叶。

  n点k分量森林有$n-k$边。对有限无向简单图，“连通且n−1边”“无圈且n−1边”“两点间唯一路径”均刻画树。

- **生成树（spanning tree）** 保留原图全部顶点、选边形成树；连通当且仅当有生成树，通常不唯一；非连通图只能取生成森林（spanning forest）。

  最小生成树（minimum spanning tree, MST）是在连通带权无向图的所有生成树中，使边权总和最小者。树先要覆盖全部顶点、连通且无圈，再比较权重；“极小连通”指不能删边，“最小权”指总权最优，二者不同。课件示例生成树总权22优于31；本课件只给MST定义与比较，没有Prim／Kruskal算法，也没有Dijkstra最短路算法。

![[C10-树与两个反例.png|600]]

- **树定理的证明要点（proofs of the tree theorems）** ：

  - 至少两叶：有限且至少两点的树取一条最长的不重复顶点路径。端点若有路径外邻点可延长路径；若另接路径内非相邻点则造圈，均矛盾。因此两个端点度都为1。
  - 边数$n-1$：$n=1$时零边；$n>1$剪掉一片叶及其唯一边，余图仍连通无圈，按归纳假设有$n-2$边，加回该边得$n-1$。
  - 唯一路径：连通保证存在；若两条不重复顶点路径不同，沿首次分歧到再次相遇的部分组成圈，违背无圈。反过来，若有圈，圈上两点有两条不同路径，违背唯一性。
  - 生成树存在：连通图若有圈，从圈中删一条边不破坏连通；不断删到无圈，仍保留所有顶点，得到生成树。

  这些等价刻画按有限非空无向简单图、且“不重复顶点路径”的约定使用；允许来回走同一边的走法不会唯一。

#### 桥与【拓展】故障连通度（Bridges and Connectivity under Failures）

- **桥／割边（bridge / cut edge）** 删去后使连通分量数增加；等价于该边不在任何圈上。这是课件Fleury算法所必需的术语，按范围内保留；桥要在“尚未走过边组成的剩余图”中重新判断。

- **【拓展】割点（cut vertex / articulation point）** 删点及关联边使分量数增加；叶通常不是割点。不可分图（nonseparable graph）为无割点的连通图，至少3点时对应双连通／2连通（biconnected / 2-connected）；块（block）为极大不可分子图，桥与孤立点是否单列成块须约定。

- **【拓展】点割／边割（vertex / edge cut）** 分别删点／边使图断开，最小数为点／边连通度（vertex / edge connectivity）$\kappa,\lambda$。简单图$\kappa\le\lambda\le\delta$，完全图约定$\kappa(K_n)=n-1$，不连通取0；$k$连通（$k$-connected）要求点数$>k$且删少于$k$点仍连通，最优连通（optimally connected）指$\kappa=\lambda=\delta$。

#### 【拓展】距离与路径冗余（Distances and Path Redundancy）

- **【拓展】距离（distance）** 为最少边数；离心率（eccentricity）为到各点距离最大值，直径／半径（diameter / radius）分别取离心率最大／最小，中心（center）达半径。有限连通图$\mathrm{rad}\le\mathrm{diam}\le2\mathrm{rad}$；不连通须约定无穷或逐分量讨论。

- **【拓展】Menger定理（Menger's theorem）** ：不邻接两点的内部点不交路径（internally vertex-disjoint paths）最大数等于最小分离点割；不同两点的边不交路径（edge-disjoint paths）版对应最小边割。Robbins定理（Robbins' theorem）称连通无向图有强连通定向（strong orientation）当且仅当无桥；顶点基（vertex basis）可在缩点DAG每个源分量选一点。

#### 【拓展】边数、矩阵幂与走法（Edge Bounds, Matrix Powers and Walks）

- **【拓展】边数与分量（edge bounds and components）** ：$n$点连通图至少$n-1$边；$k$分量简单图$e\le\binom{n-k+1}2$；$e>\binom{n-1}2$保证连通，反向“$e\ge n-1$即连通”错误。

- **【拓展】普通邻接矩阵幂（ordinary adjacency matrix powers）** $(A^r)_{ij}$数恰长$r$的走法（walk），允许重复；简单图$(A^2)_{ii}=\deg v_i$，非对角数共同邻点（common neighbors）。普通积数方案，布尔积只判断存在，不能把两者混作关系矩阵。

#### 【拓展】状态图与应用（State Graphs and Applications）

- **【拓展】状态图（state graph）** 将合法状态作点、一步合法操作作边；Alcuin过河问题（Alcuin river-crossing puzzle）的狼羊菜题最少7次。广度／深度优先搜索（breadth-first / depth-first search, BFS / DFS）可求最少边路径／可达性；六度分隔（six degrees of separation）、好莱坞图（Hollywood graph）与GNN邻接聚合（neighborhood aggregation）是应用背景，不意味着任意图直径至多6或一般网络等于$A^LXW$。

### 6.6 欧拉与哈密顿（Euler and Hamilton）

授课依据：[[Ch10.5.pdf|Ch10.5.pdf]]。Fleury、Hierholzer均在课件；有向欧拉、闭包引理和Gray码等为拓展。

| 概念（concept） | 恰好一次的对象 | 首尾 |
|---|---|---|
| 欧拉路径／欧拉迹（Euler path / Euler trail） | 每条边 | 开放版本起终点不同 |
| 欧拉回路（Euler circuit / Euler tour） | 每条边 | 相同 |
| 哈密顿路径（Hamilton path / Hamiltonian path） | 每个顶点 | 一般不同 |
| 哈密顿回路（Hamilton circuit / Hamiltonian cycle） | 每个顶点，终点复写起点仅表示闭合 | 相同 |

#### 欧拉与哈密顿的区别（Euler versus Hamilton）

- **欧拉与哈密顿（Euler and Hamilton）** ：欧拉路线恰好走每条边一次，可重复点；哈密顿路线恰好经过每个顶点一次，闭合时仅最后复写起点。柯尼斯堡七桥问题（Königsberg bridge problem）有4个奇度点，不能一笔走完。

- **欧拉图（Eulerian graph）的课件约定** ：Ch10.5 slide 5把“连通且有欧拉路径”称Eulerian，包含开放路径与回路。部分教材专指有欧拉回路，本提纲按课件回答，但写清“Euler path”还是“Euler circuit”，避免只写Eulerian造成歧义。哈密顿图（Hamiltonian graph）通常指有哈密顿回路。

- **Icosian游戏（Icosian puzzle）** 问十二面体骨架是否有经过各顶点一次的回路；十二面体有12个面、20个顶点，不能把面数当顶点数。

- **多重图中的边身份（edge identities in multigraphs）** ：路线需记$e_1,\ldots,e_r$及顶点序列，只写顶点不能区分平行边；不同平行边各走一次合法，同一条边重复两次不合法。

#### 欧拉判据及证明（Euler Criteria and Proof）

- 无向图有边时，先检查非孤立部分连通；有欧拉回路当且仅当所有度偶，有开放欧拉路径当且仅当恰两个奇度点，起终点必须是这两点。若题目把欧拉回路也算路径，则“有欧拉路径”的条件应写奇度点数0或2。

  空边图的零长度情形另按题目约定。

- **必要性（necessity）** 靠每个中途顶点的进出配对；充分性（sufficiency）先走一个闭回路，若还有未用边，找已有回路上仍接未用边的点另走子回路并拼接，直到用完所有边。

#### 求欧拉路线的算法（Algorithms for Euler Routes）

- **Fleury算法（Fleury's algorithm）** ：输入满足欧拉判据的无向图；0个奇度点可从任意非孤立点开始，2个奇度点从其中一个开始。每步在剩余图中选当前点关联的未走边，优先非桥；仅当无其他选择时才走桥。走过即删边并移动到另一端，直到所有边删完停止，记录的边序列即欧拉路线。

  手算须画出或更新剩余图，桥的身份会改变；开头检查0／2奇度和连通性，不能在不满足条件的图上照走后声称算法成功。

- **Hierholzer算法（Hierholzer's algorithm）** ：回路情形先从非孤立点$v$沿未用边走到回到$v$；若尚有未用边，找当前路线上的点$u$仍接未用边，从$u$再走一个闭回路，把新回路在$u$处接入旧路线；重复到所有边用尽。偶度保证不会在起点以外提前无边可走，连通性保证有剩边就有可拼接点。

  课件拼接例：$a\to d\to f\to a$与$d\to b\to e\to c\to d$，再接$f\to b\to c\to g\to e\to f$，得到$a\to d\to b\to e\to c\to d\to f\to b\to c\to g\to e\to f\to a$。检查每条原边恰出现一次。

  **【拓展】栈实现（stack implementation）** 可实现$O(e)$；开放路线可先连一条临时边将两奇点变偶，求回路后删临时边并从该处断开。朴素Fleury反复判桥可到$O(e^2)$。

![[C10-Fleury为什么不能先走桥.png|620]]

#### 【拓展】有向欧拉与分笔覆盖（Directed Euler Routes and Trail Covers）

- **【拓展】有向欧拉（directed Euler routes）** 要求非零度底层连通；回路每点入度等于出度，开放路线仅起点出多1、终点入多1，其余平衡。有$2k$个奇度点的无向有边连通图，覆盖全部边最少$\max(1,k)$条迹，抬笔次数再减1。

- **【拓展】邮递员问题（Chinese postman problem）** 求覆盖全部边的最短闭走，必要时重复边；不同于要求每边恰走一次的欧拉问题。

- **【拓展】DNA片段组装（DNA fragment assembly）** 可把重叠关系建图，视建模对象选欧拉或哈密顿形式；“每片段一次”与“每重叠边一次”不能混作同一要求。

#### 哈密顿的排除与充分条件（Hamiltonian Tests and Sufficient Conditions）

- **【拓展】哈密顿回路的排除条件（necessary-condition tests）** ：n≥3时每点度至少2、无割点；二分图两侧必须等大；

  度2点的两条边被强制纳入，若迫使某点用三条边或提前封成不含全部点的小圈，则不可能。哈密顿路径在二分图两侧大小差至多1，不能照搬回路的等大条件。

> [!info] 【历年考过：第21节转写L681附近】
> 老师明确说两年前期末用过哈密顿路径题。画出一条合法路线即可证存在；未找到路线不算证明不存在，要给排除理由或穷举论证。

- **Dirac定理（Dirac's theorem）** ：n≥3的简单图若$\delta\ge n/2$，则有哈密顿回路；Ore定理（Ore's theorem）：每对不相邻u、v都有$\deg u+\deg v\ge n$，则有哈密顿回路。

  Dirac条件蕴涵Ore条件；二者均充分非必要，$C_5$两者都不满足却本身有哈密顿回路。n奇时度的整数门槛是$\lceil n/2\rceil$。

#### 【拓展】闭包证明与结构条件（Closure Proof and Structural Conditions）

- **【拓展】Bondy–Chvátal闭包引理（Bondy–Chvátal closure lemma）** ：简单$n$点图中，不邻接$u,v$度和$\ge n$时加边$uv$不改变哈密顿性；可用断开的哈密顿路径与度数鸽巢重接证明。它能推出Ore，但课件只陈述Dirac、Ore及其充分不必要性。

- **【拓展】结构必要条件（necessary structural conditions）** ：删非空点集$S$后，有哈密顿回路者分量数$\le|S|$，有哈密顿路径者$\le|S|+1$。$K_{m,n}$有哈密顿回路须$m=n\ge2$，有哈密顿路径须$|m-n|\le1$；轮图回路必须含中心。

> [!info]- 【拓展】原图回看
> ![[C10.5-欧拉与哈密顿的区别.png|620]]

#### 【拓展】Gray码、骑士与Petersen（Gray Codes, Knight’s Tours and Petersen Graph）

- **【拓展】Gray码（Gray code）** 相邻位串恰差一位，循环版本对应$Q_n$哈密顿回路（$n\ge2$），可用反射构造。旋转编码（rotating-drum code）借此避免多位同时切换。

- **【拓展】骑士周游（knight's tour）** 将棋盘格作点、马步作边，遍历为哈密顿路径，可复返周游（reentrant / closed tour）为回路。Petersen图（Petersen graph）有10点15边、3正则，无哈密顿回路但删任一点后有，是次哈密顿图（hypohamiltonian graph）的例子。

- **【拓展】Warnsdorff启发式（Warnsdorff's heuristic）** 在骑士周游中优先走剩余可走邻点较少的格子，不是任意棋盘都成功的定理。

### 6.7 【拓展】最短路径与旅行商（Shortest Paths and the Traveling Salesperson Problem）

【拓展】全部补充课件中未见本节的独立讲解，保留压缩说明供回查。补充课件没有Ch10.6；MST定义在6.5按范围内保留，不由此引入最短路算法。

#### 【拓展】代价与松弛（Costs and Relaxation）

- **【拓展】最短路与松弛（shortest paths and relaxation）** ：带权路径长度（weighted path length）为边权和；若$d(u)+w(u,v)<d(v)$，更新$d(v)$并记前驱（predecessor）$u$。有限标签是已找到走法的上界，松弛局部改善不等于全局完成；有可达负回路（negative cycle）时相关目标可能无有限最短走法。

#### 【拓展】Dijkstra：条件与步骤（Dijkstra: Conditions and Steps）

- **【拓展】Dijkstra算法（Dijkstra's algorithm）** 解非负权单源最短路（single-source shortest paths）：$d(s)=0$、其余$\infty$，反复确定未确定点中标签最小者，再松弛其出边。最小标签为$\infty$时其余不可达；只问一个目标也须等目标被确定才能停，首次发现不够。非负权使已确定距离不会再改善，负边会破坏此保证。

- **【拓展】路径恢复与代价（path reconstruction and cost）** 沿前驱反向回溯；原例$a\to c\to b\to d\to e\to z$长13。朴素实现$O(v^2)$，二叉堆（binary heap）版$O((v+e)\log v)$；有负边可用Bellman–Ford算法（Bellman–Ford algorithm）$O(ve)$并检测可达负回路。

- **【拓展】路由应用（routing application）** ：开放式最短路径优先协议（Open Shortest Path First, OSPF）的SPF（shortest path first）计算是原笔记中的应用联系，不能由协议名称断言课件已授Dijkstra。

> [!info]- 【拓展】原图回看
> ![[C10.6-原图-Dijkstra逐步标签.png|650]]

#### 【拓展】Floyd：分层递推与路径恢复（Floyd: Layered Recurrence and Reconstruction）

- **【拓展】Floyd／Floyd–Warshall算法（Floyd / Floyd–Warshall algorithm）** 解全对最短路（all-pairs shortest paths）。直接边取最小权，无边为$\infty$，对角取0与自环权较小者；按中转$k$最外层，更新$D_{ij}\leftarrow\min(D_{ij},D_{ik}+D_{kj})$，$O(v^3)$时间、$O(v^2)$空间。

  可有负边；$D_{kk}<0$提示负回路，仅对能到该回路且从它能到终点的点对失去有限最短值。next表（next-hop table）可恢复路线。它与Warshall用相同分层结构，但min／加法与OR／AND不能混用。

#### 【拓展】DAG与A星（DAG and A-star）

- **【拓展】DAG最短／最长路（shortest / longest paths in a DAG）** 可按拓扑序松弛，用min／max，$O(v+e)$；一般最长简单路径（longest simple path）不能按此直接求。

- **【拓展】A星搜索（A* search）** 以$f=g+h$选择点，启发函数（heuristic）可采纳（admissible）指不高估；若不重开点，通常还需一致性（consistency）$h(u)\le w(u,v)+h(v)$，否则须允许重开（reopening）。$h=0$退化为Dijkstra。

#### 【拓展】旅行商、启发式与近似（TSP, Heuristics and Approximation）

- **【拓展】旅行商问题（traveling salesperson problem, TSP）** 求访问每城一次并返回的最小权哈密顿回路；无向完全图$n\ge3$固定起点并同一正反方向，有$(n-1)!/2$候选。原五城例最优458；不能由Floyd最短距离矩阵直接宣称已解TSP，度量闭包（metric closure）仍有访问顺序优化。

- **【拓展】精确、启发式与近似（exact optimization, heuristic and approximation）** ：最近邻（nearest-neighbor）、2-opt／3-opt局部搜索（local search）不保证最优；近似比（approximation ratio）$c$要求$\mathrm{OPT}\le W\le c\mathrm{OPT}$。Christofides算法（Christofides' algorithm）对非负无向、满足三角不等式的度量TSP（metric TSP）保证$3/2$，不能套任意权重。

- **【拓展】复杂度类（complexity classes）** ：P为多项式时间可判定问题；NP为“是”的证书（certificate）可多项式验证，非“非多项式”。若每个NP问题都可多项式归约（polynomial-time reduction）到某问题，则该问题NP难（NP-hard）；自身再属NP才NP完全（NP-complete）。TSP优化版NP难、阈值判定版NP完全，不等于已证明$P\ne NP$。

### 6.8 平面图、欧拉公式与不可平面障碍（Planarity, Euler's Formula and Obstructions）

授课依据：[[Ch10.7.pdf|Ch10.7.pdf]]。保留Euler公式、归纳证明、边数界、细分同胚与Kuratowski；交叉数、厚度、曲面为拓展。

#### 可平面与平面嵌入（Planarity and Plane Embeddings）

- **可平面图／平面图（planar graph）** 指 **存在** 一种无边交叉的平面画法；平面嵌入图／平图（plane graph）指已经给定的无交叉画法。现在画得有交叉不能否定可平面，重画或同构重排可能消除交叉；

  边在共同端点相会不算交叉。$K_4,Q_3$可平面，$K_5,K_{3,3}$不可平面。

  在原本交叉的两条边之间加一个新顶点，会改变顶点与邻接关系，得到的是另一张图；不能这样把交叉“改成端点”来证明原图可平面。合法重画须保留原图的点边关联。

> [!info] 【历年考过：第22节转写L398附近】
> 老师在平面图与不交叉论证附近提到过去期末出过题，不能据此把本次具体题型写死。应会从定义分辨planar与plane、统计面并使用定理。

- **【拓展】Jordan曲线定理（Jordan curve theorem）** ：平面内一条简单闭曲线（simple closed curve，即无自交的闭合曲线）把其余平面分成恰好两个连通区域，一个有界、一个无界，曲线是两者共同边界。它可解释圈内／圈外，但不能直接用于自交曲线或环面闭曲线；作为背景压缩保留。

#### 面、欧拉公式与边数界（Faces, Euler’s Formula and Edge Bounds）

- **面／区域（face / region）** 由嵌入划开，外部无界面（unbounded / exterior face）也算一个；

  边界（boundary）围住面，面度（degree of a face）按边界边出现次数计，不按不同边集合大小。桥在同一面边界走两次，自环可围成面。

- **欧拉公式（Euler's formula）** ：连通平面图$v-e+f=2$；【拓展】c个连通分量推广为$v-e+f=1+c$。树只围一个面，代入$e=v-1$一致；从树逐条加闭圈边，每次e和f各加1；

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
| 【拓展】$K_n$可平面 | 当且仅当$n\le4$ |
| 【拓展】$K_{m,n}$可平面 | m,n非负时当且仅当$\min(m,n)\le2$；一侧空也自然可平面 |
| 【拓展】$Q_n$可平面 | 当且仅当$n\le3$，包含n=0的单点约定 |

- **欧拉公式的归纳证明要点（inductive proof of Euler's formula）** ：连通树有$e=v-1,f=1$，等式成立；若图有圈，删去圈上一条非桥边，顶点与连通性不变、边数和面数各减1，等式保持。反复删到树即可证明原图公式。课件的加边归纳可这样写完整：$v=1,e=0,f=1$成立；从一条边开始，保持当前子图连通，每步添一条原图中的边。若引入一个新顶点，则$v,e$各加1、$f$不变；若两端都已有，则边在某个面的内部将它一分为二，$e,f$各加1、$v$不变。两种情况均保持$v-e+f=2$，直至得到原连通图。

  【拓展】对$c$个分量，在面内补$c-1$条连接边而不新增面，得$v-e+f=1+c$。

- **【拓展】极大平面图与三角剖分（maximal planar graph and triangulation）** ：对$v\ge3$的简单图，极大可平面是指不能在同一顶点集上再加边而保持可平面。其平面嵌入每个面（包括外面）都是三角形，等价于$e=3v-6$；反向若仍能添边，就会违反该上界。$K_3$已是最小的这类例子，不能把$K_4$称为最小。

  无三角形简单平面图在$e=2v-4$取等时，各面边界度须为4，计数仍按边的出现次数；不能忽略桥的重复边界。仅有数值等式但未先证可平面，不能倒推存在该面结构。

#### 必要条件与不可平面障碍（Necessary Conditions and Obstructions）

- **以上边数不等式是必要条件（necessary conditions）** ，通过不能证明可平面。Petersen图v=10,e=15通过两条数值上界仍不可平面；

  要证存在可给无交叉嵌入，要证不存在可找结构障碍。$K_{2,5}$可平面且$e=2v-4=10$，两侧都至少3时才含$K_{3,3}$。

- **细分（subdivision）** 在边上插入度2新点；两图同胚（homeomorphic）指可由同一图的细分得到。细分与逆操作在合法条件下保持可平面性，但一般不保持同构。

  压缩度2点（suppressing a degree-two vertex）时要说明选中的子图及支路，不能让新路径共享内部顶点后还称标准细分。

- **Kuratowski定理（Kuratowski's theorem）** ：有限图不可平面，当且仅当含有同构于$K_5$或$K_{3,3}$某个细分的子图。不是必须直接含未细分的$K_5/K_{3,3}$。

  操作为选支点（branch vertices）→删无关点边→找内部不交支路（internally disjoint paths）→抑制度2点→核对完整邻接。Petersen图可由此证明非平面。

![[C10.7-原图-Petersen细分障碍.png|610]]

#### 【拓展】交叉数与厚度（Crossing Number and Thickness）

- **【拓展】交叉数（crossing number）$\operatorname{cr}(G)$** 为所有平面画法中最少边交叉数，通常排除三边同点交叉。可平面时为0；

  原例$\operatorname{cr}(K_5)=\operatorname{cr}(K_{3,3})=1$，Petersen为2，$K_6$为3、$K_7$为9、$K_{3,4}$为2、$K_{4,4}$为4、$K_{5,5}$为16。

  每个精确值均需“某画法达到”的上界及“不能更少”的下界。

- **【拓展】Zarankiewicz式上界（Zarankiewicz upper bound）** ：$\operatorname{cr}(K_{m,n})\le\lfloor m/2\rfloor\lfloor(m-1)/2\rfloor\lfloor n/2\rfloor\lfloor(n-1)/2\rfloor$；

  原笔记的$mn(m-2)(n-2)/16$只是两边均偶时的写法，不能无条件用于m=n=3，否则甚至会得到小于1的错误上界。一般取等是原笔记介绍的猜想背景，此处不把它当已证通式。

- **【拓展】厚度（thickness）$\theta(G)$** 为分解成可平面子图覆盖所有边所需的最少层数（可把重复边归给一层，因此可按边划分理解）。v≥3时$\theta\ge\lceil e/(3v-6)\rceil$；

  无三角形时$\theta\ge\lceil e/(2v-4)\rceil$。$K_5,K_{3,3},K_{4,4},K_{5,5}$厚度均为2，须同时有两层构造；对$K_{m,n}$可直接用下界$\lceil mn/(2m+2n-4)\rceil$（分母正）。

  原笔记把它无条件写成等号，省略了通式的适用限制；这里保留可直接由欧拉上界证明的普遍下界，具体取等须给分层构造。

  相关原始研究：[Hu与Chen，A note on the thickness of some complete bipartite graphs（2018）](https://dlib.si/details/URN:NBN:SI:DOC-82EJ9W21)。

- **【拓展】完全图厚度（thickness of complete graphs）** ：n≥3时$\theta(K_n)=\lfloor(n+7)/6\rfloor$，n=9、10是例外，均为3。

  注意厚度并非一次画法的交叉数，层数与交叉次数不能互换。

#### 【拓展】曲面与布线（Surfaces and Layout）

- **【拓展】环面（torus）与亏格（genus）** ：在环面上$K_5,K_{3,3}$可无交叉嵌入；闭曲线不一定分隔曲面，平面中Jordan曲线（Jordan curve）分隔的论证不能直接搬过去。

  球面（sphere）与平面可平面性等价；换曲面改变可嵌入图类。

- **【拓展／应用】超大规模集成电路（very-large-scale integration, VLSI）** 可用平面性、厚度、交叉数表达布线约束；实际布线还受位置、层方向和过孔规则限制，不仅是抽象图。

  平面性判定（planarity testing）可在线性时间实现，Kuratowski是刻画定理（characterization theorem），手工枚举全部障碍不是唯一算法。

### 6.9 图着色、色数及资源分配（Graph Coloring, Chromatic Number and Resource Allocation）

授课依据：[[Ch10.8.pdf|Ch10.8.pdf]]。保留地图、色数、标准图族、完全子图下界、航班与排考；四色／六色及Brooks等未在课件陈述。

#### 着色定义与最优性（Coloring and Optimality）

- **合法顶点着色（proper vertex coloring）** 为每点赋色且邻点异色；k着色（k-coloring）表示至多用k种颜色。

  色数／顶点色数（chromatic number）$\chi(G)$是最少用色数。非空无边图色数1；空顶点图常约定0。有自环时不能合法顶点着色，通常讨论简单图；重边不增加新的不同色约束。

- 求精确色数必须双向证明：给一个k着色证$\chi\le k$，再证明k−1色不够以证$\chi\ge k$。加边不会降低色数，删边不会提高；不同连通分量可复用颜色，整体色数取最大，不是相加。

- **色数达到顶点数的充要条件（characterization of graphs with chromatic number equal to their order）** ：有$n\ge1$个顶点的有限简单图满足$\chi(G)=n$，当且仅当$G\cong K_n$。

  证明要点：完全图的任意两点相邻，必须用$n$色；反过来，若不是完全图，存在不相邻的$u,v$，给它们同一色，其余$n-2$点各用一个新色，就得到$n-1$着色，与$\chi(G)=n$矛盾。因此非完全的$n$点简单图满足$\chi(G)\le n-1$，但不一定恰好等于$n-1$。

#### 地图、标准图族与四色（Maps, Families and Four Colors）

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


- **【拓展】四色／六色定理（four-color / six-color theorem）** 分别给每个有限简单可平面图$\chi\le4$／$\chi\le6$；四是通用上界，不是每图恰需四。六色可由反复删度至多5点后归纳着色证明。课件未陈述这两个一般定理，不能由所画地图例题推成整套定理已授。

- **【拓展】区间图（interval graph）** 以相交时间区间连边，色数等于最大同时重叠数：共同重叠给下界，按开始时间贪心分配空闲色给上界。端点常取半开$[s,e)$；不连续多片段的活跃区间不保证此等式。

![[C10.8-地图到冲突图到着色.png|620]]

#### 资源分配模型（Resource Allocation Models）

- **排考（exam scheduling）** ：点为课程，有共同学生就连边，颜色为时段。课件7门课例有完全子图$\{1,2,3,4\}$，故至少4时段；$\{1,6\},\{2\},\{3,5\},\{4,7\}$给4时段可行表，故最少4。证明最优须兼有下界与可行安排。

- **登机口分配（gate assignment）** ：点为航班，占用时间重叠就连边，颜色为登机口；课件6航班例最少3口。4课程课件小例也需3时段，不能因示意图旁误写“Bipartite”而断言可2着色。

- **【拓展】其他资源分配（other resource allocation）** ：教材12课程例需5时段；委员会排程（committee scheduling）按共同成员连边，频率／频道分配（frequency / channel assignment）按干扰连边，寄存器分配（register allocation）按生存期重叠（overlapping live ranges）连边。都是同色共享资源，课件未逐项展开。

![[C10.8-原图-考试排程的着色与时段表.png|620]]

#### 团下界与【拓展】独立集（Clique Bound and Independent Sets）

- **团／完全子图（clique / complete subgraph）** 的顶点两两相邻，团数（clique number）$\omega(G)$为最大团大小。课件实际使用：若含$K_k$子图，则$\chi(G)\ge k$，因为其中各点须异色；这一下界不总取等，$C_5$为例。

- **【拓展】独立集（independent set）** 的点两两不邻，独立数（independence number）$\alpha$为最大大小；非空颜色类（color class）是独立集，构成划分。对$v>0$，$\max\{\omega,\lceil v/\alpha\rceil\}\le\chi\le\min\{\Delta+1,v-\alpha+1\}$；每色至多$\alpha$点给下界，最大独立集共色、其余点各色给上界。

#### 【拓展】贪心与Brooks（Greedy Coloring and Brooks）

- **【拓展】贪心着色（greedy coloring）** 按顶点顺序选邻点未用的最小色，至多$\Delta+1$色，依赖顺序且未必最优。Brooks定理（Brooks' theorem）称连通简单图除完全图与奇圈外满足$\chi\le\Delta$；例外达到$\Delta+1$。3着色判定（3-colorability decision）为NP完全，但仍能有限枚举判定。

#### 【拓展】边着色与多重名额（Edge and k-tuple Coloring）

- **【拓展】边着色（edge coloring）** 让共端点的边异色，边色数（edge chromatic number）$\chi'$不同于顶点色数。Vizing定理（Vizing's theorem）对简单图给$\Delta\le\chi'\le\Delta+1$；$K_n$（$n\ge2$）偶$n$为$n-1$、奇$n$为$n$，对应循环赛轮数。

- **【拓展】$k$重着色（$k$-tuple coloring）** 每点分$k$个不同颜色，邻点色集不交，最少总色数$\chi_k$；$\chi_k(K_n)=kn$，有边二分图为$2k$，无边非空图为$k$。一般不等于$k\chi$，如$\chi_2(C_5)=5$。

#### 【拓展】支配与画廊（Domination and Art Galleries）

- **【拓展】支配集（dominating set）** 要求每个集外点有集内邻点，最小大小为支配数（domination number）$\gamma$；极大独立集（maximal independent set）必支配，但未必最大独立集（maximum independent set）或最小支配集。

- **【拓展】画廊问题（art gallery problem）** ：无洞简单$n$边形（simple polygon without holes）最坏需且总够$\lfloor n/3\rfloor$个顶点守卫（vertex guards）。以$n-3$对角线三角剖分（triangulation）成$n-2$三角形，所得外平面图（outerplanar graph，全部点在外面边界）可逐耳顶点（ear vertex）3着色，取最小色类覆盖各三角形。不是每个展厅恰需该数，也不是任意平面三角剖分均可3着色。

## 七、来源、考试证据与勘误（Sources, Examination Evidence and Corrections）

### 7.1 小节覆盖对照（Section Coverage Map）

下表逐篇列出来源及正文落点，用于定位，不能单独证明每个知识点都已覆盖。原笔记中的例题、自测和习题若只重复同一知识，合并为方法条目；原笔记知识来源仍可回查；本轮授课范围以各节课件依据及7.6为准。表中编号是本提纲编号。

> [!info]- 展开对照表
> | 原笔记（source note） | 正文落点 | 核对范围（coverage） |
> |---|---|---|
> | [[C1.1 命题逻辑 Propositional Logic]] | 1.1 | 命题、六联结词、条件翻译、Wason、优先级、位串、模糊逻辑与悖论 |
> | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] | 1.2；1.3 | 规约一致性、布尔检索、骑士／泥孩子、逻辑电路与传播 |
> | [[C1.3 命题等价 Propositional Equivalences]] | 1.3 | 全部等价律、对偶、DNF/CNF、功能完备、NAND/NOR、SAT与数独 |
> | [[C1.4 谓词与量词 Predicates and Quantifiers]] | 1.4；1.5 | 谓词与论域、自由／约束变量、量词分配／否定、唯一性、Prolog |
> | [[C1.5 嵌套量词 Nested Quantifiers]] | 1.5 | 量词顺序、有限展开、exactly one/two、量词移动、极限与一致性 |
> | [[C1.6 推理规则 Rules of Inference]] | 1.6 | 有效／可靠、八条命题规则、四条量化规则、归结、谬误与作业纠错 |
> | [[C1.7 证明导论 Introduction to Proofs]] | 1.7 | 证明术语、直接／逆否／反证／等价、空／平凡、反例与错误证明 |
> | [[C1.8 证明方法与策略 Proof Methods and Strategy]] | 1.8 | 分情况、WLOG、存在唯一、策略窃取、均值、铺砌、开放问题与证明界限 |
> | [[C2.1 集合 Sets]] | 2.1 | 集合语言、包含／属于、空集、幂集、积、真值集、罗素悖论 |
> | [[C2.2 集合运算 Set Operations]] | 2.2 | 五运算、二／三集合容斥、恒等式、无限族、位串、多重／模糊集 |
> | [[C2.3 函数 Functions]] | 2.3 | 定义域／陪域／像、单满双射、单调、逆与复合、取整、阶乘与部分函数 |
> | [[C2.4 序列与求和 Sequences and Summations]] | 2.4 | 序列、递推与迭代、猜规律、换指标、双重和／连乘、有限及无穷求和 |
> | [[C2.5 集合的基数 Cardinality of Sets]] | 2.5 | 可数／不可数、饭店、整数／有理数枚举、对角线、Bernstein、不可计算与CH |
> | [[C2.6 矩阵 Matrices]] | 2.6；3.3；6.5 | 矩阵运算、幂／转置／逆、布尔积／幂、可达与走法计数 |
> | [[C9.1 关系及其性质 Relations and Their Properties]] | 3.1 | 六种性质、集合运算、复合／幂及其证明、逆／补与关系计数 |
> | [[C9.2 n 元关系与数据库 n-ary Relations and Their Applications]] | 3.2 | 多元关系、度／域、记录／属性、键、选择／投影／连接与SQL |
> | [[C9.3 关系的表示 Representing Relations]] | 3.3 | 矩阵／有向图转换、判性质、并交逆、布尔复合与幂 |
> | [[C9.4 关系的闭包 Closures of Relations]] | 3.4 | 闭包最小性、三闭包、路径／幂、有限上界、Warshall及次序问题 |
> | [[C9.5 等价关系 Equivalence Relations]] | 3.5 | 等价关系、同余、类相同或不交、划分／商集、前缀类与计数 |
> | [[C9.6 偏序 Partial Orderings]] | 3.6 | 偏序／严格序、全序／良序、字典序、Hasse、极值／界、格及拓扑排序 |
> | [[C6.1 计数基础 The Basics of Counting]] | 4.1 | 加乘减除、补集／容斥、函数／密码／地址、树形计数与圆排列 |
> | [[C6.2 鸽巢原理 The Pigeonhole Principle]] | 4.2 | 普通／广义鸽巢、阈值反问题、生日、余数／前缀和／奇数核、Ramsey与子序列 |
> | [[C6.3 排列与组合 Permutations and Combinations]] | 4.3 | 排列／组合、端点、组合数算法、位串／彩票／分组、捆绑／插空与圆桌 |
> | [[C6.4 二项式系数与恒等式 Binomial Coefficients and Identities]] | 4.4 | 二项式、全部系数恒等式、Pascal三角、Vandermonde、曲棍球棒及组合证明 |
> | [[C6.5 广义排列与组合 Generalized Permutations and Combinations]] | 4.5；3.5 | 重复选择、星条、上下界解、重物排列、四类盒子、Stirling与整数分拆 |
> | [[C6.6 生成排列与组合 Generating Permutations and Combinations]] | 4.6 | 三个后继算法、排列例、位串／子集对应、组合例、r排列、不重不漏及复杂度 |
> | [[C8.1 递推关系的应用 Applications of Recurrence Relations]] | 5.1–5.5 | 递推验证与初值、兔子／复利／汉诺塔、00/000位串、码字／Catalan、DP调度 |
> | [[C10.1 图与图模型 Graphs and Graph Models]] | 6.1 | 图类型、三问建模、全部14类模型、交集图／同代图与关系联系 |
> | [[C10.2 图的术语与特殊类型 Graph Terminology and Special Types of Graphs]] | 6.2–6.3 | 邻接／度、握手、图族、二分／匹配／Hall、SDR、网络、图运算及度序列 |
> | [[C10.3 图的表示与图同构 Representing Graphs and Graph Isomorphism]] | 6.4；6.5 | 三表示法、复杂度、同构与矩阵置换、不变量、反向图、带宽与计数 |
> | [[C10.4 连通性 Connectivity]] | 6.5 | 路径语义、分量、割点／桥、连通度、强弱连通、树／生成树、距离与Menger |
> | [[C10.5 欧拉路径与哈密顿路径 Euler and Hamilton Paths]] | 6.6 | 欧拉判据与算法、哈密顿排除及Dirac/Ore、闭包证明、Gray、骑士与Petersen |
> | [[C10.6 最短路径问题 Shortest-Path Problems]] | 6.7 | 松弛、Dijkstra／Floyd、负权、路径恢复、DAG/A*、TSP与近似 |
> | [[C10.7 平面图 Planar Graphs]] | 6.8 | planar/plane、面／面度、Euler、边界不等式、细分／同胚、Kuratowski与拓扑延伸 |
> | [[C10.8 图着色 Graph Coloring]] | 6.9 | 顶点／地图着色、图族／四色、全部应用、边／k重着色、独立／支配／画廊与界 |

六篇章节汇总也参与了知识核对：[[C1 基础：逻辑与证明 MOC]]的考试说明、证明与铺砌补充归入篇首及1.7–1.8；

[[C2 基本结构：集合、函数、序列、求和与矩阵 MOC]]中的取整条件、Ulam数、望远镜积、矩阵周期归入2.3–2.6；

[[C9 关系 Relations MOC]]的循环关系、划分计数与加细偏序归入3.1–3.6；[[C6 计数 Counting MOC]]的计数总表与勘误归入第四部分；

[[C8 高级计数技巧 Advanced Counting Techniques MOC]]的模型条件归入第五部分；[[C10 图 Graphs MOC]]的跨节结论归入第六部分。

作业来源为[[C1 作业与错题]]、[[C2 作业与错题]]及[[作业与错题 MOC]]：谓词求值、量词翻译、德摩根、Linda结论抄错及子集链均已覆盖。未用现有《C1复习提纲》或模拟卷作为组织模板；

没有把尚未整理的章节题目当作已经存在的讲义。

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
> | 图论为期末重点 | [[第二十一节课_233dd011-已合并.txt\|第二十一节课_233dd011-已合并]]L1198附近；第19节相关说明 | 章级重点，不是本章每个拓展定理都被单独点名 |
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
> | C1汇总铺砌反例先删角又称角孤立；S/Z列染色理由错误 | 1.8给出保留角的准确四格坐标，保留S/Z结论并不用错误列染色证明 |
> | C2汇总取整混合等式答案未完成 | 2.3用小数部分给出完整充要条件，并检验负数与整数边界 |
> | C2模糊集把隶属度直接等同softmax概率 | 2.2区分模糊隶属与概率，不因同值域便视为相同 |
> | C2.5用十进制展开直接声称双射，未顾双重展开 | 2.5以二进制函数对角化说明不可数，明确避开小数表示歧义 |
> | C2.6把布尔幂稳定解释为OR只增不减 | 2.6区分单次幂与累计并，给出交替反例；最终周期不代表最终不变 |
> | C9汇总称传递关系高次幂都等于平方 | 3.1给出$R^2\ne R^3$反例；只有自反且传递才保证各正幂等于R |
> | C9汇总“格的每个有限子集都有界”未排除空集 | 3.6将一般格的结论限定为有限非空子集，空集需顶底存在 |
> | C9.6把“图形像菱形／五边形”当分配格判据 | 3.6要求是保持并交的子格，修正N5不可比条件 |
> | C8.1称$2^n$在n=2碰巧满足候选递推 | 5.1直接算两端，说明没有该特例 |
> | C10.2把一般二分图写e=mn，遗漏0正则边界 | 6.2改e≤mn，正则两侧等大限定r>0 |
> | C10.2 Havel–Hakimi步骤先把最大项减1再删除 | 6.3删除原最大项d，将后续d项各减1 |
> | C10.2子图计数把诱导边数只写成顶点数函数 | 6.3逐个顶点子集W求$2^{e(G[W])}$再求和 |
> | C10.3带宽例称按自然圈序即可使C5带宽2 | 6.4给出正确的非自然顶点编号顺序 |
> | C10.5轮图哈密顿回路只指外圈，漏中心 | 6.6将中心插入外圈相邻两点之间 |
> | C10.5 K(m,n)开放欧拉路径表漏K(1,1)，七桥两笔称必须重画 | 6.6补单边图边界；两迹覆盖不必重复边 |
> | C10.5 Ore闭包证明位置集合下标漏邻点 | 6.6改为1至n−1的位置集合，按度和与鸽巢正确计数 |
> | C10.6在目标确定时把未确定点也写成“全部”；A*未限定是否重开 | 6.7区分目标停机与全源完成，补一致性或重开要求 |
> | C10.6由标签严格下降直接断言更新次数有限 | 6.7补可达负权回路反例，终止性与正确性须结合具体算法前提 |
> | C10.7交叉数上界遗漏奇偶取整，厚度把下界无条件当等号 | 6.8给出四个floor的上界；厚度保留普遍下界与已证小图精确值，注明通式有适用限制 |
> | C10.8把允许空颜色类直接称划分；画廊界称每个展厅精确值 | 6.9只取非空类构成划分，画廊公式为最坏保证且限定无洞简单多边形 |

本轮另补的来源勘误：

| 原笔记问题 | 正文采用的条件或结论 |
|---|---|
| C2.4按右侧出现前项的“项数”决定初值数 | 2.4按最大滞后与递推起始下标检查，给出$a_n=a_{n-5}$反例 |
| C2.3把“非严格单调”笼统判为不单射 | 2.3改为“不保证单射”；严格单调的定义与证明分别写清 |
| C9.6旁注称一般偏序反向后未必仍是偏序 | 3.6明确任意偏序的对偶仍为偏序；任意格的对偶仍为格 |
| C9.6将覆盖关系恢复原序不加有限性限制 | 3.6限定本课Hasse算法为有限偏序，给出有理数稠密序反例 |
| C10.4把森林必须定义成不连通 | 6.5按无圈图定义，允许一棵树也是森林 |
| C10.6把TSP优化版与NP完全判定版混称 | 6.7分清优化为NP难、阈值判定为NP完全，补P／NP与归约定义 |
| C10.7称$K_4$为最小极大平面图 | 6.8注明$K_3$已满足，给出$v\ge3$条件与三角面刻画 |
| C10.8画廊3着色表述易被泛化成所有平面三角剖分 | 6.9限定为无洞简单多边形的剖分图，区分外平面与可平面 |
| C6.2旧研究范围把上、下界方向混写 | 4.2保留教材历史范围并标明，未当作当前新界 |

这里的勘误只写入新提纲，未改动原笔记。历史统计与未解问题背景按原笔记的历史语境保留，不把旧的计算验证界或规模数字冒充当前纪录；计算验证有限实例也不替代一般证明。

### 7.4 历史记录：前一轮38组补入（Previous Audit: 38 Additions）

> [!info]- 展开上一轮38组历史修补记录
> 以下是前一轮修订留下的38组记录，保留供查阅历史变化；本轮的全量提示块核对、正文条目索引与新增修订另见7.5及逐项核对表。下表不是当前完整知识点清单。
>
> 这份修订记录便于回查，不能把未列在修订表中的内容理解为不重要，也不能把修订记录冒充逐字逐题的教材替代品。合并的只是重复实例，不能据此自行缩小考试范围。
>
> #### 逻辑与证明（Logic and Proofs）
>
> | 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
> |---|---|---|
> | 实质蕴涵（material implication） | [[C1.1 命题逻辑 Propositional Logic\|C1.1]]条件语句 | 补全名称与非因果含义，1.1 |
> | XOR消去、一次一密、CRC与RAID（XOR cancellation, one-time pad, CRC and RAID） | [[C1.1 命题逻辑 Propositional Logic\|C1.1]]异或与计算机联系 | 补入可逆公式、密钥条件及校验应用，1.1 |
> | 布隆过滤器、BNN、XOR非线性可分（Bloom filter, BNN and XOR nonseparability） | [[C1.1 命题逻辑 Propositional Logic\|C1.1]]位并行与AI联系 | 补入应用与概念区别，1.1；模糊控制名称同步补全 |
> | 第三类人谜题（puzzles with spies / normals） | [[C1.2 命题逻辑的应用 Applications of Propositional Logic\|C1.2]]骑士与无赖习题说明 | 补入三类人的不同约束，1.2 |
> | 知识逻辑与共同知识（epistemic logic and common knowledge） | [[C1.2 命题逻辑的应用 Applications of Propositional Logic\|C1.2]]泥孩子旁注 | 补全名称、知道的层次及应用联系，1.2 |
> | 否定范式（negation normal form, NNF） | [[C1.3 命题等价 Propositional Equivalences\|C1.3]]七步等价推导后的方法说明 | 补入定义、转化次序、例子及与DNF／CNF的区别，1.3 |
> | 符号与神经符号AI（symbolic and neuro-symbolic AI） | [[C1.4 谓词与量词 Predicates and Quantifiers\|C1.4]]Prolog旁注 | 补入原笔记列举的应用联系，1.4 |
> | 邻域独立与聚类系数（independent neighborhood and clustering coefficient） | [[C1.5 嵌套量词 Nested Quantifiers\|C1.5]]朋友关系例题旁注 | 补入量词公式、图论解释及度数边界，1.5 |
> | 平均值论证与概率方法（averaging argument and probabilistic method） | [[C1.7 证明导论 Introduction to Proofs\|C1.7]]习题平均值结论后的联系 | 补全方法名称与存在性解释，1.7 |
> | 构造主义及证明程序联系（constructivism and proofs as programs） | [[C1.8 证明方法与策略 Proof Methods and Strategy\|C1.8]]无理数幂例题旁注 | 补入Gelfond–Schneider、直觉主义、Curry–Howard与证明助手背景，1.8 |
> | 卡塔兰猜想（Catalan's conjecture） | [[C1.8 证明方法与策略 Proof Methods and Strategy\|C1.8]]100以内连续完全幂例题 | 补入一般定理与有限穷举的区别，1.8 |
> | 证明与数论背景术语（background terminology of proofs and number theory） | [[C1.8 证明方法与策略 Proof Methods and Strategy\|C1.8]]人物、费马与Collatz旁注 | 补全原笔记背景名称与不可判定性边界，1.8 |
>
> #### 集合、序列与矩阵（Sets, Sequences and Matrices）
>
> | 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
> |---|---|---|
> | 笛卡尔积相等与空积条件（equality and emptiness of Cartesian products） | [[C2.1 集合 Sets\|C2.1]]笛卡尔积习题 | 补全两个充要条件与非空情形证明方法，2.1 |
> | 运算与包含、对称差消去（operations, inclusion and symmetric-difference cancellation） | [[C2.2 集合运算 Set Operations\|C2.2]]相关习题与自测7 | 补入结论、证明与并集不能消去的反例，2.2 |
> | 集合后继（set successor） | [[C2.2 集合运算 Set Operations\|C2.2]]自测8、习题59–60 | 补入定义、三个例子、基数及自然数构造，2.2 |
> | 比例增长加固定增量（affine recurrence） | [[C2.4 序列与求和 Sequences and Summations\|C2.4]]工资增长模型 | 补入递推、迭代闭式及$r=1$边界，2.4 |
> | 正奇数求和（sum of positive odd integers） | [[C2.4 序列与求和 Sequences and Summations\|C2.4]]求和与几何解释 | 补入公式及逐层添方格证明，2.4 |
> | $A+A^T$的对称性（symmetry of a matrix plus its transpose） | [[C2.6 矩阵 Matrices\|C2.6]]自测6、习题14 | 补入一般证明，2.6 |
> | 数量矩阵与中心（scalar matrices and center） | [[C2.6 矩阵 Matrices\|C2.6]]自测7、补充习题38–39 | 补入正向证明及$2\times2$逆向构造，2.6 |
> | 布尔幂最终周期性（eventual periodicity of Boolean powers） | [[C2.6 矩阵 Matrices\|C2.6]]自测8 | 补入有限性证明、交替反例与全1稳定条件，2.6 |
>
> #### 关系（Relations）
>
> | 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
> |---|---|---|
> | 一对多等对应情况（one-to-many and related correspondences） | [[C9.1 关系及其性质 Relations and Their Properties\|C9.1]]关系与函数的区别 | 补全名称，3.1 |
> | 数据库外延与内涵（extension and intension） | [[C9.2 n 元关系与数据库 n-ary Relations and Their Applications\|C9.2]]键的时间条件 | 补入两者定义与选键依据，3.2 |
> | 关系代数（relational algebra） | [[C9.2 n 元关系与数据库 n-ary Relations and Their Applications\|C9.2]]三个运算及SQL联系 | 原有运算，补全统称与输入输出含义，3.2 |
> | 正负同余合并（congruence up to sign） | [[C9 关系 Relations MOC\|C9汇总]]自测11(b)、12(c) | 补入三性质证明及模7四个类，3.5 |
> | 格的有限子集与有限格（finite subsets of lattices and finite lattices） | [[C9 关系 Relations MOC\|C9汇总]]自测19 | 补入归纳方法、有界结论及空子集条件，3.6 |
>
> #### 计数与递推（Counting and Recurrences）
>
> | 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
> |---|---|---|
> | 组合数学（combinatorics） | [[C6.1 计数基础 The Basics of Counting\|C6.1]]导言 | 补全统称与计数／构造联系，第四部分开头 |
> | 分治与动态规划（divide and conquer and dynamic programming） | [[C8.1 递推关系的应用 Applications of Recurrence Relations\|C8.1]]动态规划比较 | 补全区别，并区分汉诺塔求步数与输出移动，5.5 |
>
> #### 图论（Graph Theory）
>
> | 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
> |---|---|---|
> | 有限图与无限图（finite and infinite graphs） | [[C10.1 图与图模型 Graphs and Graph Models\|C10.1]]Remark | 补入点集、边集两方面的条件，6.1 |
> | 真子图（proper subgraph） | [[C10.2 图的术语与特殊类型 Graph Terminology and Special Types of Graphs\|C10.2]]定义7 | 补入与生成／诱导子图的区别，6.3 |
> | 立方体的六个面（six square faces of a cube） | [[C10.2 图的术语与特殊类型 Graph Terminology and Special Types of Graphs\|C10.2]]$Q_3$子图例 | 补入六个$Q_2$及坐标面计数说明，6.3 |
> | 强分量算法（SCC algorithms） | [[C10.4 连通性 Connectivity\|C10.4]]§5末尾 | 补入Kosaraju／Tarjan思路与复杂度，6.5 |
> | 不可分图、双连通与块（nonseparable, biconnected graphs and blocks） | [[C10.4 连通性 Connectivity\|C10.4]]§3、§4 | 补入定义与小图约定，6.5 |
> | 六度分隔与好莱坞图（six degrees of separation and Hollywood graph） | [[C9.4 关系的闭包 Closures of Relations\|C9.4]]应用；[[C10.4 连通性 Connectivity\|C10.4]]连通例 | 补全名称与不能泛化到任意图的边界，6.5 |
> | 欧拉图与哈密顿图（Eulerian and Hamiltonian graphs） | [[C10.5 欧拉路径与哈密顿路径 Euler and Hamilton Paths\|C10.5]]术语定义 | 原有路线判据，补全图的名称与区别，6.6 |
> | Icosian游戏（Icosian puzzle） | [[C10.5 欧拉路径与哈密顿路径 Euler and Hamilton Paths\|C10.5]]哈密顿背景 | 补入模型及原笔记已说明的20顶点／12面区别，6.6 |
> | 松弛的三条性质（three properties of relaxation） | [[C10.6 最短路径问题 Shortest-Path Problems\|C10.6]]§3 | 补全上界性、局部性及终止性限制，6.7 |
> | 交叉处加点改变原图（adding vertices at crossings changes the graph） | [[C10.7 平面图 Planar Graphs\|C10.7]]平面画法说明 | 补入操作限制，6.8 |
> | OSPF与SPF（Open Shortest Path First and shortest path first） | [[C10.6 最短路径问题 Shortest-Path Problems\|C10.6]]开场及路由应用 | 补全应用名称，6.7 |

### 7.5 本轮逐项核对入口（Current Item-by-item Audit）

上一轮按原笔记的593个重要块及其上下文补全70组内容，属于“原笔记全量核对”历史；本轮另按41份补充课件重新划定深度，范围外已压缩。原笔记出处与当时修补记录仍保留在[[离散数学期末复习逐项核对表 Final Review Coverage]]历史部分，不能据此将教材拓展认作老师实际授课。

### 7.6 补充课件范围与本轮调整（Courseware Scope and Current Revision）

全部41份PDF的逐文件页码清单、正文分项处理及重传修正见[[离散数学期末复习逐项核对表 Final Review Coverage#本轮课件范围核对（Current Courseware Scope Audit）|本轮课件范围核对]]。正文各小节开头提供实际课件入口；同节范围内与拓展分别判断。

- 恢复为范围内：函数后半、关系矩阵与布尔运算、闭包次序、度序列、补图、自补图、Fleury、Hierholzer，以及MST定义。
- 压缩并标拓展：普通矩阵代数、独立可数性、一般二项式展开、Stirling通式、拓扑排序、动态规划、最短路与TSP、四色／六色定理及其他图论延伸。相关课件实际出现的局部概念与公式保留。
- 术语按课件修订：simple path要求顶点不重复；Eulerian在该课件包括有开放欧拉路径的连通图。低阶$C_1,C_2,W_1,W_2$按课件图示单列，不混套简单图公式。
- 数学勘误继续保留：课件不是不会出错。否定后件、关系复合／矩阵顺序、Warshall下标、格判定等均采用核算后的正确形式，具体页码见核对表。
