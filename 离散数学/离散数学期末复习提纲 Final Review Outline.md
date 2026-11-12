# 离散数学期末复习提纲（Discrete Mathematics Final Review Outline）

本提纲依据仓库中的35篇小节讲义、6篇章节汇总、作业错题及课堂转写重新组织。复习顺序为逻辑与证明、基本结构、关系、计数、递推、图论；章节权重不影响知识覆盖。

本提纲的整理目标是保留原笔记中的定义、公式条件、算法、证明方法及习题带出的新概念；不能根据某项是否出现在提纲里判断其考试重要性。本轮查出的遗漏已补入相应正文，具体出处与位置见7.4。

**【拓展】表示原笔记注明的延伸、课堂未展开内容或明确列出的补充，不表示可以省略。** 相同知识合并，重复题的具体数值不逐题抄录，但不同解题方法与新结论保留。

> [!warning] 关于遗漏与考试范围
> 未写入不等于不重要，也不等于不考；没有“老师明确会考”标记，也不等于不会考。只有能追溯到老师原话的说明才用来标注考试范围。“拓展”“课堂未讲”只说明内容来源与授课情况。
>
> 7.1是小节来源导航，不能作为逐知识点无遗漏的证明。排版前后内容一致，也只能说明排版没有删内容。

## 考试信息与标记说明（Examination Information and Labels）

| 项目 | 已有课堂证据与复习动作 |
|---|---|
| 时间（time） | 第22节宣布11月19日8:50–10:50，时长120分钟；按本学期日历为2026年11月19日（周四）。转写后文把星期重复识别成Wednesday，不据此改日期。 |
| 地点（venue） | 第22节转写分别出现“53A 210”和“F3A210”，均指二楼210。楼名存在转写歧义，须以QQ群正式通知核对，不能把机器转写当作确定楼号。 |
| 范围（scope） | 第17节说明以期中后的第2、9、6、8、10章为主，第1章约保留一道题；第21节再次明确图论是期末重点。这里仍完整保留第1章及全部已有拓展。 |
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

#### 【拓展】广义逻辑与自指（Generalized Logic and Self-reference）

- **【拓展】模糊逻辑（fuzzy logic）** ：本笔记采用真值$[0,1]$、$v(\neg P)=1-v(P)$、$v(P\land Q)=\min(v(P),v(Q))$、$v(P\lor Q)=\max(v(P),v(Q))$；这不是概率（probability）。

  例如0.8和0.4的合取为0.4、析取为0.8；排中律与矛盾律不再按经典二值形式成立。

  模糊控制（fuzzy control）用这类分级真值表达“温度较高”等规则。

- **【拓展】自指（self-reference）与悖论（paradox）** ：说谎者悖论（liar paradox）无法在经典二值体系中一致赋值；

  理发师悖论（barber paradox）通过讨论理发师是否替自己刮胡子推出不存在满足规则者，与罗素悖论（Russell's paradox）同构。

  自指与对角化（diagonalization）也是停机问题（halting problem）相关论证的线索。

#### 术语层次与计算应用（Terminology and Computing）

- 术语补充：命题逻辑／命题演算（propositional logic / propositional calculus）把完整陈述作原子；

  命题变元也称语句变元／布尔变量（statement / Boolean variable）。

  否定是一元运算符（unary operator），其余基本联结词为二元运算符（binary operator）；双条件也称双蕴涵（bi-implication）。

  公式属于对象语言（object language），谈论公式等价的$\equiv$属于元语言（metalanguage），不要把两层混作同一公式。

- **【拓展／应用】掩码（mask）** 用按位与（bitwise AND）筛位，按位或（bitwise OR）置位，按位异或（bitwise XOR）翻位；

  位并行（bit-parallel）同时处理多个布尔值，数据库位图索引（bitmap index）即用位串表达记录集合。

  它们与高效编码、快速傅里叶变换（fast Fourier transform, FFT）中的位处理有关，但本课程不扩写FFT算法。

- **【拓展／应用】异或的消去性质（XOR cancellation）** ：$a\oplus b\oplus b=a$；异或等于模2加法（addition modulo 2）。

  一次一密（one-time pad）以$c=m\oplus k$加密，以$c\oplus k=m$解密；完整安全条件包括密钥均匀随机、独立、与消息等长且只使用一次。重复密钥会使$c_1\oplus c_2=m_1\oplus m_2$，消去密钥。

  循环冗余校验（cyclic redundancy check, CRC）及独立磁盘冗余阵列（redundant array of independent disks, RAID）的奇偶校验（parity check）也使用异或；校验与加密的目标不同。

- **【拓展／应用】布隆过滤器（Bloom filter）与二值神经网络（binary neural network, BNN）** ：前者用位数组与多个哈希位置近似判断集合成员，通常允许假阳性；后者可用按位运算与置位计数（population count / popcount）加速二值计算。

  XOR问题不是线性可分（linearly separable）的，单个线性感知机（linear perceptron）无法表示其真值表；它与位运算可快速计算XOR是两个层面的结论。

### 1.2 翻译、规约、谜题与电路（Translation, Specifications, Puzzles and Circuits）

#### 翻译与一致性（Translation and Consistency）

- **自然语言翻译（translation）** ：先定义原子命题，再判断充分／必要／唯一等限制，最后定联结词与括号。不要把日常语境中暗含的双条件擅自加入只说“if”的数学题。

- **系统规约（system specification）** 是一组要求；一致性（consistency）指所有规约存在同一组满足赋值（satisfying assignment），不是每条分别可真。

  合取后找一组赋值即证一致；要证不一致（inconsistency），须推出矛盾或说明所有赋值均失败。加规约可能破坏一致性，删规约不能把一致系统变成不一致。

#### 检索与逻辑谜题（Search and Logic Puzzles）

- **布尔检索（Boolean search）** ：AND取交集，OR取并集，NOT排除。先明确括号及检索系统的运算约定，不能只按自然语言猜范围。

- **骑士与无赖（knights and knaves）** ：设$K_A$为“A是骑士”，其发言内容为$S_A$，自洽条件是$K_A\leftrightarrow S_A$；对所有人联立，可能唯一解、多解或无解。

  “我是无赖”在固定两类规则下无自洽解。谋杀案（murder puzzle）、美女与老虎（the lady or the tiger）等同样是约束求解。

  【拓展】若加入间谍／常人（spy / normal），其发言可真可假，不能对他套用“是骑士当且仅当发言为真”。应分别设类型变量，要求每人恰属于一类，再以“骑士则发言真”“无赖则发言假”约束，常人的发言不受真假限制。

- **泥孩子问题（muddy children puzzle）** ：父亲的公开公告（public announcement）把“至少一人脏”变为共同知识（common knowledge）；

  第一轮无人知道也提供新信息，第二轮据此推断。重点是知识状态随公开回应变化，不能只看静态真假。

  【拓展】这一背景属于知识逻辑／认知逻辑（epistemic logic）。人人知道某事，还不一定人人知道“别人也知道”，共同知识要求这类“知道别人知道”的层次不断成立；公开公告为大家提供了共同可见的依据。它与分布式系统共识（distributed consensus）、多智能体系统（multi-agent systems）的信息状态相关。

#### 逻辑电路（Logic Circuits）

- **逻辑门（logic gate）** ：反相器（inverter / NOT gate）、与门（AND gate）、或门（OR gate）；

  组合电路（combinational circuit）输出仅由当前输入决定。读电路时沿信号流为中间节点写子式；造电路时从语法树（syntax tree）或最内层子式开始；等价化简可减少门数。

  布尔代数用于开关电路的思想与Shannon的早期工作相联系。

![[C1-图2-组合电路示例.png|560]]

图中每个中间输出都可作为下一门的输入；先写每个节点表达式，再写最终输出。

#### 【拓展】检索误差与电路化简（Retrieval Errors and Circuit Simplification）

- **【拓展／应用】检索误差（retrieval errors）** ：假阳性（false positive）为不相关结果被选入，假阴性（false negative）为相关结果被排除；

  查准率（precision）为检出结果中相关的比例，查全率（recall）为全部相关结果中检出的比例。布尔条件精确执行也可能因词义歧义检索不准；

  语义检索（semantic retrieval）与检索增强生成（retrieval-augmented generation, RAG）是原笔记提及的应用背景。

- **【拓展／应用】电路化简（circuit simplification）** ：积之和（sum of products）即若干AND输出再OR，对应DNF；小圆圈（bubble）表示信号取反；

  扇出（fan-out）把同一中间输出送往多个后续门，公共子表达式消除（common subexpression elimination）避免重复计算。

  计算图（computational graph）与组合电路都可用DAG描述算子依赖。

### 1.3 等价律、范式与可满足性（Equivalence Laws, Normal Forms and Satisfiability）

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

- 德摩根律可推广到有限多个命题。

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

#### 【拓展】对偶与范式（Duality and Normal Forms）

- **【拓展】对偶（dual）** ：互换$\land/\lor$、$\mathbf T/\mathbf F$，变元和否定号不变；$(s^*)^*=s$称对合（involution）。等价式的对偶仍等价；不能把“对偶”误作“取否定”。

- **【拓展】文字（literal）** 为变元或其否定；合取项（term）为若干文字的合取；子句（clause）为若干文字的析取。

  析取范式（disjunctive normal form, DNF）为合取项的析取；合取范式（conjunctive normal form, CNF）为子句的合取。

  由真值表造DNF：每个真行写一个包含全部变元的合取项，再析取；由假行造CNF：每个假行写一个仅在该行假的子句，再合取。全假、全真可分别用$\mathbf F,\mathbf T$表示。

- **【拓展】否定范式（negation normal form, NNF）** 只使用$\land,\lor,\neg$，并且否定号只作用于单个命题变元。

  转换时先消去$\to,\leftrightarrow$，再用德摩根律与双重否定把$\neg$向内推。例如$\neg(p\to(q\land r))\equiv p\land(\neg q\lor\neg r)$。

  NNF只限制否定的位置，不要求整体是合取项的析取或子句的合取；转成DNF／CNF还可能需要分配律。

#### 【拓展】功能完备性（Functional Completeness）

- **【拓展】功能完备性（functional completeness）** ：运算符集能表达任意布尔函数（Boolean function）。

  $\{\neg,\land,\lor\}$、$\{\neg,\land\}$、$\{\neg,\lor\}$均完备，后两者由德摩根律获得另一运算。

  与非（NAND / Sheffer stroke）$p\mid q=\neg(p\land q)$、或非（NOR / Peirce arrow）$p\downarrow q=\neg(p\lor q)$各自单独完备：$p\mid p=\neg p$，$(p\mid q)\mid(p\mid q)=p\land q$；

  $p\downarrow p=\neg p$，$(p\downarrow q)\downarrow(p\downarrow q)=p\lor q$。二者交换但不结合。$n$变元共有$2^{2^n}$个布尔函数／不同真值表。

#### 【拓展】SAT、数独与传播（SAT, Sudoku and Propagation）

- **【拓展】可满足性（satisfiability, SAT）** 指至少一组赋值为真；不可满足（unsatisfiable）等同矛盾式。$P$永真当且仅当$\neg P$不可满足。

  证可满足给见证（witness），证不可满足要排除全部可能。暴力枚举（brute-force enumeration）有$2^n$组输入，DNF也可能指数长；

  原笔记以SAT的NP完全性（NP-completeness）说明一般问题的困难，不等于每个实例都难。

- **【拓展】数独（Sudoku）编码** ：令$p(i,j,d)$表示第$i$行、第$j$列填数字$d$，$9\times9$数独用729个变元。

  约束包括给定值（givens）、每行每列每块含各数字、每格至多一个数字。

  例如行约束$\bigwedge_i\bigwedge_d\bigvee_jp(i,j,d)$，列约束互换$i,j$，块约束$\bigwedge_{a,b=0}^2\bigwedge_{d=1}^9\bigvee_{u,v=1}^3p(3a+u,3b+v,d)$；

  同格互斥为$\neg p(i,j,d)\lor\neg p(i,j,e)$（$d\ne e$）。每格至少一个为$\bigwedge_{i,j}\bigvee_dp(i,j,d)$；在行覆盖与每格至多一个已成立时可推得。$4\times4$有64个变元；

  一般$n^2\times n^2$有$n^6$个变元。给定约束不保证唯一解（unique solution），唯一性需要另验。

- **【拓展】单元传播（unit propagation）** ：在CNF中某子句只剩一个未确定文字时，满足该子句就强制该文字为真，据此简化其他子句，迭代到稳定或矛盾。

  它是SAT求解与规约一致性检查的基本方法，但传播停住而未见矛盾不自动证明整个公式可满足。

### 1.4 谓词、论域与单层量词（Predicates, Domains and Quantifiers）

#### 谓词与量词的含义（Meaning of Predicates and Quantifiers）

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

#### 否定与空论域（Negation and Empty Domains）

> [!warning] 【易错】
> $\neg\forall x(P(x)\to Q(x))\equiv\exists x(P(x)\land\neg Q(x))$，同时翻转量词和联结词；“没有人完美”与“并非人人完美”不能混写。

- **【拓展】空论域（empty domain）** 上全称为空真、存在为假；本课程通常默认论域非空。涉及删除空量词或移动量词时应保留该前提。

#### 【拓展】程序验证与逻辑程序（Verification and Logic Programming）

- **【拓展】前置条件与后置条件（preconditions and postconditions）** ：程序执行前满足的谓词与执行后要求成立的谓词，如交换变量前后值的对应关系；不是只检查某个输入。

- **【拓展】逻辑程序设计（logic programming / Prolog）** ：事实（fact）、规则（rule）、查询（query）；

  `,`表示合取，`head :- body`表示由body推出head。规则中变量按全称闭包理解；

  只出现在规则体的变量在查询／证明规则体时体现存在搜索（existential search），不能简单称整条规则把它语法上改成存在量词。

  Lewis Carroll论证将自然语言命题翻译成全称蕴涵再串联；关于命题自身的量化须另行说明论域是命题。

- **【拓展／术语】谓词逻辑／谓词演算（predicate logic / predicate calculus）** 把主语（subject）和谓语／性质（predicate）分开，借全称量化（universal quantification）与存在量化（existential quantification）表达对象内部结构。

  形式化验证（formal verification）用逻辑证明规约；Prolog属于声明式编程（declarative programming），描述事实与推理关系，区别于直接列执行步骤。

  元数学（metamathematics）研究形式系统本身；命题逻辑有限真值表可判定，不代表一般一阶逻辑（first-order logic）的有效性也有判定算法。

- **【拓展／应用】符号人工智能（symbolic AI / GOFAI）** 以事实、规则与推理操作表示知识；原笔记列举专家系统（expert system）、Datalog、答案集编程（answer set programming, ASP）和知识图谱推理（knowledge-graph reasoning）作为关联应用。

  神经符号人工智能（neuro-symbolic AI）尝试结合神经网络的表示学习与逻辑规则推理，例如先从数据提取谓词，再交由逻辑规则推断。这里保留应用联系，不将这些工具冒充课堂单独讲授的算法。

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

- **【拓展／应用】邻域独立与聚类系数（independent neighborhood and clustering coefficient）** ：在无向简单的朋友图中，“某人的任意两个不同朋友都不是朋友”可写为

  $$\exists x\,\forall y\,\forall z\bigl((F(x,y)\land F(x,z)\land y\ne z)\to\neg F(y,z)\bigr).$$

  这等价于存在顶点$x$的邻域$N(x)$是独立集，即$x$不在任何三角形中。度$d(x)\ge2$时，局部聚类系数（local clustering coefficient）为$C(x)=e(G[N(x)])/\binom{d(x)}2$，故此处为0；度小于2时分母为0，须注明采用的约定，不能直接做除法。

#### 量词移动与依赖（Quantifier Movement and Dependence）

- 若$A$中无$x$自由出现，则$(\exists xP(x))\to A\equiv\forall x(P(x)\to A)$，$(\forall xP(x))\to A\equiv\exists x(P(x)\to A)$（后式按非空域）。量词从蕴涵前件移出会翻转；

  从后件移出不翻转，并须满足变量不自由出现及论域条件。

> [!warning] 【易错】
> 两式一般不等价；不能套用普通同类量词交换。

- **【拓展】量化作嵌套循环（quantification as nested loops）** ：全称层找反例，存在层找见证；内层存在成功后可换下一个外层对象，但共同见证不能每次重选。

#### 【拓展】分析与学习理论中的量词（Quantifiers in Analysis and Learning Theory）

- **【拓展】极限（limit）** $\lim_{x\to a}f(x)=L$为$\forall\varepsilon>0\exists\delta>0\forall x(0<|x-a|<\delta\to|f(x)-L|<\varepsilon)$；

  否定为存在$\varepsilon_0>0$使任意$\delta>0$都能找到违反误差界的$x$。逐点连续（pointwise continuity）为$\forall a\forall\varepsilon\exists\delta\forall x\cdots$；

  一致连续（uniform continuity）为$\forall\varepsilon\exists\delta\forall a\forall x\cdots$，同一$\delta$适用于所有点。不能随意消去依赖关系。

- **【拓展／补充】空量化规则（null quantification rule）** ：在非空论域且x不自由出现在A中时，$\forall xA\equiv A\equiv\exists xA$；移动量词也须先验自由变量条件。

  乘法逆元（multiplicative inverse）的表达为$\forall x\in\mathbb R\,(x\ne0\to\exists y\in\mathbb R\,xy=1)$，不能为每个x要求同一个y。

- **【拓展／应用】逐点收敛与一致收敛（pointwise and uniform convergence）** ：前者$\forall x\forall\varepsilon>0\exists N\forall n\ge N:|f_n(x)-f(x)|<\varepsilon$，后者$\forall\varepsilon>0\exists N\forall x\forall n\ge N:\cdots$，差别在N能否依赖x。

  大概近似正确学习（probably approximately correct learning, PAC learning）的误差$\varepsilon$、失败概率$\delta$、样本量（sample size）及数据分布（data distribution）也需明确量词次序；

  本提纲保留这一联系，不以一串省略量词冒充完整PAC定义。

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
> 课堂提醒针对的是省略最终推导，不应解读为这条逻辑推论本身错误。

#### 归结与自动证明（Resolution and Automated Proof）

- **【拓展】归结反驳（resolution refutation）** ：把前提与结论否定合取，消箭头、否定内移、分配为CNF，再归结；推出空子句（empty clause）表示矛盾。

  这里是命题层做法，不能据此声称任意一阶公式均可无条件直接变成等价的量词自由子句。

- **全称否定后件式（universal modus tollens）** ：由$\forall x(P(x)\to Q(x))$及$\neg Q(a)$推出$\neg P(a)$；论证形式（argument form）是用变元表达推理结构。

  肯定前件式也叫分离律（law of detachment）；归结产生的子句叫归结式（resolvent）。

  自动定理证明（automated theorem proving）可搜索规则链，但“某个系统搜不到证明”不等于已证明目标为假。

### 1.7 证明的基本方法（Basic Proof Methods）

#### 证明的语言与基础（Language and Foundations of Proof）

- **形式证明（formal proof）** 逐步遵循规则；非形式证明（informal proof）可合并显然步骤、使用已证结论，但仍必须给出有效理由。

  数学陈述常省略全称量词，证明时取“任意满足假设的对象”，不能只举几个例子。

- **【拓展】定理（theorem）／命题（proposition）／事实（fact）／结果（result）** 为已证明的结论；公理／公设（axiom / postulate）作为基础假设；

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

#### 平方根证明与等价性（Square-root Proof and Equivalence）

- $\sqrt2$无理的骨架：若$\sqrt2=a/b$且$a,b$互素（relatively prime），则$a^2=2b^2$；

  平方偶推出$a$偶，设$a=2k$得$b^2=2k^2$、$b$也偶，与互素矛盾。

> [!warning] 【考试注意】
> 最简分数及非零分母不能省；需要用英文表达“lowest terms / relatively prime”。

- **等价性证明（proof of equivalence）** ：$p\leftrightarrow q$分别证两方向；

  $n$个陈述等价可用循环蕴涵（cyclic implications）$p_1\to p_2\to\cdots\to p_n\to p_1$，只需$n$条而非$n(n-1)$条。

#### 【拓展】反例与错误证明（Counterexamples and Fallacious Proofs）

- **【拓展】空证明（vacuous proof）** 证前件永假；平凡证明（trivial proof）证后件恒真。反例（counterexample）必须在论域内、满足所有前提而违反结论；

  一个反例即可反驳全称。

- **【拓展】错误证明（fallacious proof）** 包括除以0、对负数或不等式作无依据操作、开平方漏$\pm$、非等价变形引入增根（extraneous solution）、循环论证／窃取论题（circular reasoning / begging the question）。

  倒推解方程后须把候选根代回原式。

- 习题方法归纳：奇偶性先代$2k$或$2k+1$；有理数加法须检验分母非零；无理＋有理仍无理可反证；两无理数和／积却可能有理或无理，须分辨量词；奇数$2k+1=(k+1)^2-k^2$；

  $x+y\ge2\Rightarrow x\ge1\lor y\ge1$用逆否；至少有一个数不小于平均值（average）可假设全部小于平均值后求和矛盾。圆周数列可把相邻和整体相加，利用每项被计相同次数。

- **【拓展／方法】平均值论证（averaging argument）** ：有限非空数列至少有一项不小于平均值，也至少有一项不大于平均值；否则把所有严格不等式求和就与平均值定义矛盾。

  概率方法（probabilistic method）把“找对象”转为“证明满足性质的随机对象出现的概率大于0”，从而推出至少存在一个对象，不必直接构造它。有限样本空间中，至少有一个取值不小于随机变量的期望（expectation），是平均值思想的另一种表述。

#### 【拓展】估界、有理根与稠密性（Bounds, Rational Roots and Density）

- **【拓展／补充】因子估界（bounding factors）** ：正数乘积$n=a_1\cdots a_k$至少有一因子$\le n^{1/k}$，否则全部严格大于阈值，相乘得到$n>n$。

  $\sqrt[3]2$无理可仿平方根反证：最简$a/b$满足$a^3=2b^3$，推出a、b均偶。

- **【拓展／补充】有理根定理（rational root theorem）** ：整数系数多项式若有最简有理根a/b，则a整除常数项、b整除最高项系数。

  例如$x^3+x+1$若有有理根，只可能$\pm1$，代入均非0；也可按最简分数整除性直接反证。

- **【拓展／补充】稠密性（density）** ：对有理数r<s，$r+(s-r)/\sqrt2$在二者之间且无理；结合任意实数区间内可找有理端点，说明无理数在实数中稠密（dense），有理数也稠密。

  稠密性和可数性（countability）不同，$\mathbb Q$稠密仍可数。

### 1.8 分情况、存在唯一性与证明策略（Cases, Existence, Uniqueness and Strategies）

#### 分类与不失一般性（Cases and WLOG）

- **穷举证明（exhaustive proof）** 检验有限域全部对象；分情况证明（proof by cases）把假设分为覆盖全部可能的几类，并各证目标。

  逻辑依据是$(p_1\lor\cdots\lor p_k)\to q\equiv\bigwedge_i(p_i\to q)$。实数分正、负、零；整数分奇偶或余数类；漏0、等号或空集会使命题失效。

- 用末位分类可证平方末位只可能为0、1、4、5、6、9，四次方末位只可能0、1、5、6。

  分段定义（piecewise definition）的绝对值（absolute value）、最大值（maximum）、最小值（minimum）也用分类，例如$\max(x,y)+\min(x,y)=x+y$，$\max(x,y)=(x+y+|x-y|)/2$、$\min(x,y)=(x+y-|x-y|)/2$；

  三角不等式（triangle inequality）为$|x+y|\le|x|+|y|$。

- **【拓展】不失一般性（without loss of generality, WLOG）** 只有在对象交换等对称性（symmetry）使未写情形可还原时合法；不能凭方便假定$x\le y$。

  有限样例不能证明无限域命题，数值实验（numerical experiment）主要用于猜想或找反例。

#### 存在、唯一与博弈策略（Existence, Uniqueness and Game Strategies）

- **存在性证明（existence proof）** 分构造性（constructive）与非构造性（nonconstructive）。$1729=1^3+12^3=9^3+10^3$为具体见证；

  以$(\sqrt2)^{\sqrt2}$的有理／无理两种情形说明存在无理数$a,b$使$a^b$有理，是经典非构造性论证。

  【拓展】盖尔丰德–施奈德定理（Gelfond–Schneider theorem）可进一步判定$(\sqrt2)^{\sqrt2}$为超越数（transcendental number），但上述分情况证明不依赖它。原笔记借此引出直觉主义（intuitionism）与构造主义数学（constructive mathematics）：它们不接受把排中律当作无需说明的普遍构造依据。

  Curry–Howard对应（Curry–Howard correspondence）把命题与类型、证明与程序联系起来，是依赖类型（dependent type）语言及Coq、Agda等证明助手（proof assistant）的思想背景；不应据此把任意经典存在证明都说成已给出见证算法。

- **【拓展】Chomp游戏（Chomp game）** 用策略窃取（strategy stealing）：若某一步后的对手存在必胜策略，可由先手先走那一步反用，矛盾；证明存在策略不一定给出具体策略。

  取石子游戏（take-away game）可从终局反推必败位置（losing position），与必胜位置（winning position）交替分析。

- **唯一性证明（uniqueness proof）** 必须同时有存在性与唯一性：先构造$x$满足性质，再设任意$y$也满足并证$y=x$。常见例子为线性方程、加法逆元；

  不要把“至多一个”当成“恰好一个”。

> [!tip] 【老师强调】
> C1.8课堂补充提醒“DO NOT over simplify the proof”，须把两部分写出来。

- **【拓展】取石子策略（take-away strategy）** ：每次可取1至m颗、取最后一颗胜时，$n\equiv0\pmod{m+1}$是必败位置（P-position），其余是必胜位置（N-position）；

  先取到m+1的倍数，之后对手取k就取m+1−k。15颗且每次1–3颗时先取3，再给对手依次留12、8、4。

  终局倒推（backward induction）与极小化极大搜索（minimax search）由此联系，不能把必败位置的策略用于“最后一颗输”的不同规则。

#### 【拓展】证明策略与不等式（Proof Strategies and Inequalities）

- **【拓展】正向推理（forward reasoning）** 从前提出发，逆向推理（backward reasoning）从目标寻找充分条件；逆向寻找完成后，要验证每步能正向推出目标，不能犯肯定后件谬误。

  例：$(\sqrt a-\sqrt b)^2\ge0$正向得$a+b\ge2\sqrt{ab}$。

- **【拓展】均值不等式（mean inequalities）** ：对正数$a,b$，调和平均（harmonic mean, HM）$2ab/(a+b)$，几何平均（geometric mean, GM）$\sqrt{ab}$，算术平均（arithmetic mean, AM）$(a+b)/2$，平方平均（quadratic mean, QM）$\sqrt{(a^2+b^2)/2}$；

  $\mathrm{HM}\le\mathrm{GM}\le\mathrm{AM}\le\mathrm{QM}$，等号当且仅当$a=b$。乘不等式、平方及开根号前先检查符号条件。

- **【拓展】改编证明（adapting a proof）与反例搜索（searching for counterexamples）** ：改变参数时重验每步；从小数、0、负数、相等、空集、边界值开始找反例。

  整式方程无解可先估界（bounding）把无限候选缩到有限，再穷举。100个连续非平方数可选在相邻足够大的平方之间。

#### 【拓展】铺砌与不变量（Tilings and Invariants）

- **【拓展】铺砌（tiling）、骨牌（domino）、三格骨牌（triomino）** ：先检查面积整除（divisibility），再检查不变量（invariant）。

  $8\times8$棋盘可用骨牌覆盖，去一格后面积奇数不行；去对角两角后面积虽偶，但黑白数32与30，每块骨牌各盖一黑一白，故不行。

  直线三格骨牌可用三色染色（three-coloring）制造每块各色一格的不变量；L形与直线形的可铺性不能混用。

![[C1-图9-去掉左上和右下角的棋盘.png|360]]

- **【拓展】直线与L形三格骨牌（straight and right triominoes）** ：三格块要求面积为3的倍数，故不能铺完整64格棋盘；去一角剩63格，直线块仍不能铺。

  用按行列和模3循环的三色染色，每个横／竖直线块各覆盖一格三种颜色；旋转染色使去掉角原属21格的颜色，则余三色20、21、22，不能由21块各覆盖三色。L形块不满足同样的三色覆盖规律，不能照搬该反证；

  $2^k\times2^k$缺一格可用L形块铺砌是笔记指向归纳法的后续例子，核心是四象限加中心一块。

#### 【拓展】数论与证明界限（Number Theory and Limits of Proof）

- **【拓展】数论背景（number-theoretic background）** ：拉格朗日四平方和定理（Lagrange's four-square theorem）说明每个非负整数是四个整数平方之和；

  “前面若干数可表示为三个平方”不能推出全称结论。华林问题（Waring's problem）讨论每个正整数能否用固定数目的$k$次幂表示。

  勾股数组（Pythagorean triple）可构造为$(m^2-n^2,2mn,m^2+n^2)$，$m>n>0$，从而有无穷多组。

- **【拓展／补充】华林反例（Waring-type counterexample）** ：1至78均可表示为至多18个整数四次方之和，不代表所有正整数都行；

  79低于81，只能用0、1、16，最多选四个16仍需15个1，共19项，故18项不足。原笔记引用$g(4)=19$为一般背景，有限样例验证不能代替该一般定理。

- **【拓展】开放问题与证明界限（open problems and limits of proof）** ：费马大定理（Fermat's Last Theorem）排除$n>2$、$xyz\ne0$的整数解$x^n+y^n=z^n$，原笔记介绍Wiles在1990年代的证明；

  Collatz／$3x+1$猜想（Collatz conjecture）对偶数取$x/2$、奇数取$3x+1$，猜测每个正整数轨迹到达1。

  原笔记的计算验证上界是历史记录，不能充当全称证明。

  素数（prime）相关的孪生素数猜想（twin prime conjecture）、哥德巴赫猜想（Goldbach's conjecture）也属于笔记列出的背景，不扩写成另一个课程章节。

- **【拓展】其他证明方式（additional proof methods）** ：数学归纳法（mathematical induction）需基础步（base case）和归纳步（inductive step）；

  结构归纳法（structural induction）沿递归构造证明；康托尔对角线法（Cantor diagonalization）构造漏掉的对象；

  组合证明（combinatorial proof）对同一集合两种计数。哥德尔不完备性定理（Gödel's incompleteness theorems）针对足够强、有效公理化且相容的形式系统；

  丘奇不可判定性定理（Church's undecidability theorem）说明一阶逻辑有效性无一般判定算法。这不等于不能枚举形式证明，也不等于每个具体定理都不可证明。

#### 【拓展】铺砌补充与构造（Further Tilings and Constructions）

- **【拓展／补充】更多铺砌结论（further tiling results）** ：面积偶数的完整矩形可沿偶数边分行铺；$8\times8$去同侧两角、去全部四角均可按行铺；

  $5\times5$去三角剩22格但黑白10:12，不能铺。完整$8\times8$去任意一黑一白可沿覆盖全棋盘的哈密顿回路删两点，把剩余偶长度链逐对覆盖；

  这称Gomory铺砌论证（Gomory's tiling argument）。黑白各删两格则可能失败：删$(1,2),(2,1),(2,2),(3,3)$后保留的$(1,1)$孤立，且仍黑白平衡；

  这比原笔记先删掉角本身再说角被孤立的写法准确。

- **【拓展】多联骨牌（polyomino）** 由单位格沿整边相连；允许旋转、翻转视同的四格骨牌（free tetrominoes）有I、O、T、L/J、S/Z五类。

  标准棋盘可用I、O、L、T同类块分别铺满：I按行，O按$2\times2$，两个L拼$2\times4$，四个T拼$4\times4$；

  S/Z类不能铺满矩形，需边界排布阻碍论证，原笔记“每块在奇列覆盖奇数格”的理由不成立（某朝向覆盖2格）。不将该错误染色理由用于证明。

- **【拓展／补充】完全幂（perfect power）** 为$a^b$（a,b为规定范围的整数且b>1），完全平方数（perfect square）为平方情形；存在问题须先定范围。

  卡塔兰猜想／米哈伊列斯库定理（Catalan's conjecture / Mihăilescu's theorem）指出：在$x,y,a,b>1$的整数中，$x^a-y^b=1$只有$3^2-2^3=1$这一组解，即8与9是唯一一对连续完全幂。原笔记介绍其2002年的证明。

  在100以内列出完全幂并穷举，只证明该有限范围的结论，不能代替上述一般定理。这里的卡塔兰猜想与5.4的卡特兰数（Catalan numbers）是不同概念。

  出租车数（taxicab numbers）以不同方式表示为正立方和，1729是两种表示的最小例。

  Euclid勾股参数式在m、n互素且奇偶相反时给出本原勾股数组（primitive Pythagorean triples），允许交换两直角边；不能省互素与奇偶条件。

- **【拓展／背景】证明方法的相关背景（background connections of proof methods）** ：原笔记人物与历史旁注还提到哈代–温伯格定律（Hardy–Weinberg law）的遗传模式应用、代数数论（algebraic number theory）及椭圆曲线理论（theory of elliptic curves）与数论证明的发展联系。

  $3x+1$猜想也称Collatz问题（Collatz problem）、Hasse算法（Hasse's algorithm）、Ulam问题（Ulam's problem）、Syracuse问题（Syracuse problem）或角谷问题（Kakutani's problem）。广义Collatz类问题的不可判定性（undecidability）不能直接推成这个具体猜想不可证明。

  一阶逻辑判定问题也称Entscheidungsproblem；“没有通用判定算法”与“某个实例没有证明”是不同判断。

---

## 二、集合、函数、序列与矩阵（Sets, Functions, Sequences and Matrices）

### 2.1 集合的基本语言（Basic Set Language）

#### 集合的表示与常用对象（Notation and Common Sets）

- **集合（set）** 是不计顺序与重复的对象整体；元素（element / member）用$\in$表示。

  列举法（roster method）写出元素，描述法（set-builder notation）写$\{x\in U\mid P(x)\}$；省略号必须有可辨认规则。集合中的元素可以也是集合。

- **常用数集（number sets）** ：自然数$\mathbb N$（本笔记约定含0）、整数$\mathbb Z$、正整数$\mathbb Z^+$、有理数$\mathbb Q$、实数$\mathbb R$、复数$\mathbb C$；

  题目另有约定时从其约定。$\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q\subseteq\mathbb R\subseteq\mathbb C$。

- **全集（universal set）** $U$限定讨论范围；空集（empty set / null set）$\varnothing$无元素；单元素集（singleton set）只有一个元素。

  $\varnothing\ne\{\varnothing\}$，后者基数为1；$\{\varnothing,\{\varnothing\}\}$有两个元素。

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

#### 【拓展】区间与集合论基础（Intervals and Foundations of Set Theory）

- **【拓展】区间记号（interval notation）** ：$(a,b),[a,b],(a,b],[a,b)$分别表示端点是否纳入，无穷端点永不用闭括号。

- **【拓展】朴素集合论（naive set theory）与公理化集合论（axiomatic set theory）** ：无条件允许$\{x:x\notin x\}$会导致罗素悖论；不能把任意文字描述都默认成一个合法集合。

### 2.2 集合运算、恒等式及扩展（Set Operations, Identities and Extensions）

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

#### 无限集合族（Infinite Set Families）

- **无限集合族的边界例（boundary examples for infinite set families）** ：$A_i=[0,1/i]$（$i\ge1$）的交为$\{0\}$、并为$[0,1]$；

  $B_i=(0,1/i)$的交为空，不能因为每个集合非空就断言无限交非空；$\{i,i+1,\ldots\}$的交也为空。

- **广义并与交（generalized unions and intersections）** $\bigcup_iA_i$对应“存在一个i”，$\bigcap_iA_i$对应“对所有i”；

  有限和无限族都按定义，不把无限交误当作某个有限阶段。

  递增族（increasing family）的交通常由最小集合决定，递减族（decreasing family）的并通常由最大集合决定，另一运算需实际检查极限边界。

#### 【拓展】恒等式与证明（Identities and Proofs）

- **【拓展】集合恒等式（set identities）** ：$A\cup\varnothing=A$，$A\cap U=A$；$A\cup U=U$，$A\cap\varnothing=\varnothing$；$A\cup A=A\cap A=A$；$\overline{\overline A}=A$；并交均交换、结合；

  $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$、$A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$；$\overline{A\cup B}=\overline A\cap\overline B$、$\overline{A\cap B}=\overline A\cup\overline B$；

  $A\cup(A\cap B)=A$、$A\cap(A\cup B)=A$；$A\cup\overline A=U$、$A\cap\overline A=\varnothing$。分别对应逻辑中的同一、支配、幂等、双重否定、交换、结合、分配、德摩根、吸收、否定律（英文名称见1.3）。

  广义德摩根律同样适用于任意指标族。

- **【拓展／习题结论】集合运算与包含关系（set operations and inclusion）** ：$A\cup B=A\iff B\subseteq A$；$A\cap B=A\iff A\subseteq B$；$A-B=A\iff A\cap B=\varnothing$。

  对称差的消去律（cancellation law）：$A\oplus C=B\oplus C\Rightarrow A=B$，因为两边再对称差$C$，利用结合律及$C\oplus C=\varnothing$即可。并、交一般不能消去，例如$\{1\}\cup\{1,2\}=\{2\}\cup\{1,2\}$，却有$\{1\}\ne\{2\}$。

#### 【拓展】集合后继与自然数构造（Set Successors and Natural-number Construction）

- **【拓展】集合后继（set successor）** 定义为$S(A)=A\cup\{A\}$：把集合$A$整体作为一个元素加入，不是把$A$的元素再重复一遍。

  $S(\varnothing)=\{\varnothing\}$，$S(\{\varnothing\})=\{\varnothing,\{\varnothing\}\}$，$S(\{1,2,3\})=\{1,2,3,\{1,2,3\}\}$。

  在通常良基集合论（well-founded set theory）中$A\notin A$，故有限$A$满足$|S(A)|=|A|+1$。冯·诺依曼自然数（von Neumann natural numbers）用$0=\varnothing$、$n+1=n\cup\{n\}$递归构造；每个$n$就是前$n$个自然数组成的集合。

- **【拓展】恒等式证明（proof of set identities）** 有四法：双向包含；描述法逐元素转换为逻辑等价；隶属表（membership table）列0／1；用已证恒等式逐步变形。

  不能由一张特定文氏图声称证了一切情况。

#### 计算机表示与算法（Computer Representation and Algorithms）

- **有限全集固定顺序后，用特征位串／特征函数（characteristic bit string / characteristic function）** 表示集合；

  并、交、补、对称差分别按位OR、AND、NOT、XOR。对称差交换、结合，$A\oplus A=\varnothing$，$A\oplus\varnothing=A$。

  同一套恒等式贯穿逻辑、集合、位串和零一矩阵，统属布尔代数（Boolean algebra）。

- **计算集合交集（set intersection）** ：双循环最坏$O(nm)$，排序后双指针（two-pointer method）扫描为排序加$O(n+m)$，哈希集合（hash set）在通常散列假设下期望$O(n+m)$。

  不能把期望复杂度（expected complexity）无条件写成最坏复杂度（worst-case complexity）；C++ `set`与`unordered_set`的结构和复杂度不同。

#### 【拓展】多重集与模糊集（Multisets and Fuzzy Sets）

- **【拓展】多重集（multiset）** 用重数（multiplicity）记录重复；逐元素的并取max、交取min、差取$\max(m_A-m_B,0)$、和（sum）取$m_A+m_B$。共用设备按最大需求，不共用按需求和；

  并不等于和。

- **【拓展】模糊集（fuzzy set）** 用隶属函数（membership function）$\mu_A:U\to[0,1]$；补为$1-\mu_A$、并为max、交为min。

  隶属度（degree of membership）不自动等于softmax概率，二者不能只因都在$[0,1]$便视为同一概念。

### 2.3 函数及其运算（Functions and Their Operations）

#### 函数定义与像（Definition and Images）

- **函数／映射（function / mapping）** $f:A\to B$把每个$a\in A$对应唯一$f(a)\in B$。

  定义域（domain）是A，陪域（codomain）是B，值域／像（range / image）$f(A)\subseteq B$；原像（preimage）是映到目标值的输入。

  判定函数要同时排除“一输入多输出”和“定义域有输入没有输出”。程序可能不终止或有副作用，不能直接等同于数学总函数（total function）。

- 函数相等需定义域、陪域的约定及各点输出一致；函数图像（graph of a function）为$\{(a,f(a)):a\in A\}\subseteq A\times B$。实值函数的和与积逐点定义：$(f+g)(x)=f(x)+g(x)$、$(fg)(x)=f(x)g(x)$。

- **子集的像（image of a subset）** $f(S)=\{f(s):s\in S\}$。 **【拓展／补充】逆像（inverse image）** $f^{-1}(T)=\{a:f(a)\in T\}$不要求f可逆，勿与反函数混淆；

  像保持并，交一般仅有$f(S\cap T)\subseteq f(S)\cap f(T)$；逆像保持并、交及相对补。

#### 单射、满射与双射（Injection, Surjection and Bijection）

- **单射（injection / one-to-one）** ：$f(x)=f(y)\to x=y$，等价于$x\ne y\to f(x)\ne f(y)$；否证找不同输入同输出。

  满射（surjection / onto）：$\forall b\in B\exists a\in A:f(a)=b$；否证找陪域内漏掉的值。

  双射（bijection / one-to-one correspondence）同时单且满，证明需分两部分。

- **严格递增／严格递减（strictly increasing / strictly decreasing）** 函数单射；

  非严格递增／递减（increasing / decreasing）可能有平台，不能保证单射。若A、B有限且大小相同，单射当且仅当满射；无限集上不成立，如$n\mapsto n+1$在$\mathbb N$上单而不满。

#### 恒等、反函数与复合（Identity, Inverses and Composition）

- **恒等函数（identity function）** $i_A(a)=a$。反函数（inverse function）$f^{-1}:B\to A$存在当且仅当f双射；交换输入输出即可。

  限制定义域或陪域（restriction of domain or codomain）可使$x^2$成为可逆函数，例如$[0,\infty)\to[0,\infty)$。

- **复合函数（composition）** $(f\circ g)(x)=f(g(x))$，先g后f，须保证中间像落在下一定义域。复合结合，但一般不交换；单射复合单射、满射复合满射、双射复合双射。

  若$f\circ g$单则g单，若$f\circ g$满则f满；反方向的另一因子不可无条件推出。$f^{-1}\circ f=i_A$、$f\circ f^{-1}=i_B$，$(f\circ g)^{-1}=g^{-1}\circ f^{-1}$。

![[C2.3-映射类型-单射满射双射.png|650]]

#### 取整函数（Floor and Ceiling Functions）

- **下取整（floor function）** $\lfloor x\rfloor$为不大于x的最大整数，上取整（ceiling function）$\lceil x\rceil$为不小于x的最小整数；如$\lfloor-0.5\rfloor=-1$、$\lceil-0.5\rceil=0$。

  存储块数、分组数等“装满才够”的问题用上取整，能凑出多少完整组用下取整。

$$
\begin{gathered}
\lfloor x\rfloor=n\iff n\le x<n+1\iff x-1<n\le x,\\
\lceil x\rceil=n\iff n-1<x\le n\iff x\le n<x+1,\\
x-1<\lfloor x\rfloor\le x\le\lceil x\rceil<x+1,\\
\lfloor-x\rfloor=-\lceil x\rceil,\qquad\lceil-x\rceil=-\lfloor x\rfloor,\\
\lfloor x+n\rfloor=\lfloor x\rfloor+n,\quad
\lceil x+n\rceil=\lceil x\rceil+n\quad(n\in\mathbb Z).
\end{gathered}
$$

#### 取整证明与成立条件（Proofs and Conditions for Rounding Identities）

- 取整证明写$x=m+\alpha$，$m\in\mathbb Z,0\le\alpha<1$，按跨越整数的位置分类。$\lfloor2x\rfloor=\lfloor x\rfloor+\lfloor x+1/2\rfloor$；

  整数n满足$\lfloor n/2\rfloor+\lceil n/2\rceil=n$、$\lfloor n/2\rfloor\lceil n/2\rceil=\lfloor n^2/4\rfloor$。一般不能拆开实数和或积的取整。

- **【拓展／补充】取整可拆的精确条件** ：写$x=m+\alpha,y=n+\beta$。下取整之和等式成立当且仅当$\alpha+\beta<1$；上取整之和等式成立当且仅当$\alpha=0$或$\beta=0$或$\alpha+\beta>1$；

  $\lceil x+y\rceil=\lfloor x\rfloor+\lceil y\rceil$成立当且仅当$\alpha=0$，或$\beta>0$且$\alpha+\beta\le1$。后一个条件补齐了原章节汇总中的未完成答案。

#### 阶乘与部分函数（Factorials and Partial Functions）

- **阶乘（factorial）** $n!=1\cdot2\cdots n$，$0!=1$；

  **【拓展／补充】Stirling近似（Stirling's approximation）** $n!\sim\sqrt{2\pi n}(n/e)^n$，$\sim$表示比值趋于1，不是精确等号。

- **【拓展】部分函数（partial function）** 只在所称输入集合的某个子集上定义；未定义（undefined）不是一个普通输出值。

  机器学习（machine learning）中把模型看作输入到输出的映射有助于区分定义域与值域；

  物理信息神经网络（physics-informed neural network, PINN）把物理约束加入学习，函数拟合（function approximation）不自动提供可解释性（interpretability）或精确证明。

### 2.4 【拓展：本小节课堂未讲】序列与求和（Sequences and Summations）

#### 序列、递推与迭代（Sequences, Recurrences and Iteration）

- **序列（sequence）** 是以整数下标集为定义域的函数；项（term）$a_n$、下标（index）n、起始下标必须说明。

  等差数列／算术序列（arithmetic progression）$a_n=a_0+nd$，d为公差（common difference）；

  等比数列／几何序列（geometric progression）$a_n=ar^n$，r为公比（common ratio）。有限字符串（string）是有序符号序列，空串（empty string）长0。

- **递推关系（recurrence relation）** 由前项定义后项，初始条件（initial conditions）与递推起始下标共同确定序列；验证解（solution）须同时满足递推和初值。

  斐波那契数（Fibonacci numbers）约定$f_0=0,f_1=1,f_n=f_{n-1}+f_{n-2}$。

- **迭代法（iteration）** 可正向代入（forward substitution）或反向代入（backward substitution）得闭式（closed formula）；

  加常数得等差，乘常数得等比；复利（compound interest）$P_n=P_0(1+r)^n$。由有限项猜规律不唯一；猜出的通项要用归纳法确认。

- **一阶仿射递推（first-order affine recurrence）** 同时含比例增长与固定增量：$a_n=ra_{n-1}+b$（$n\ge1$）。例如年薪先增长5%再固定加1000，对应$a_n=1.05a_{n-1}+1000$。

  反向代入得$a_n=r^na_0+b\sum_{j=0}^{n-1}r^j$，故$r\ne1$时$a_n=r^na_0+b(r^n-1)/(r-1)$；$r=1$时$a_n=a_0+nb$。先增薪再按比例上涨会得到不同递推，须按叙述顺序建模。

#### 规律识别与求和记号（Patterns and Summation Notation）

- **常见整数序列（integer sequences）** 包括正整数、奇数、偶数、平方、立方、幂、阶乘、斐波那契数、素数。

  识别规律可检查差分（differences）、商（ratios）、周期（periodicity）、递推与已知数列，不能把猜想当证明。

- **求和记号（summation notation）** $\sum_{k=m}^na_k$中k是哑指标（dummy index），项数为$n-m+1$；换元（change of index）必须同时改上下限和被加式。

  双重求和（double summation）有限情形可换序，矩形范围可分离时才可拆乘积；按集合求和（sum over a set）每个元素算一次。

  连乘记号（product notation）$\prod$同样遵守下标与项数规则；空和（empty sum）为0，空积（empty product）为1。

| 求和公式（summation formula） | 条件 |
|---|---|
| $\sum_{k=0}^nar^k=a(1-r^{n+1})/(1-r)$ | $r\ne1$；$r=1$时为$(n+1)a$ |
| $\sum_{k=1}^nk=n(n+1)/2$ | $n\ge0$ |
| $\sum_{k=1}^n(2k-1)=n^2$ | $n\ge0$；前n个正奇数之和 |
| $\sum_{k=1}^nk^2=n(n+1)(2n+1)/6$ | $n\ge0$ |
| $\sum_{k=1}^nk^3=[n(n+1)/2]^2$ | $n\ge0$ |
| $\sum_{k=0}^{\infty}x^k=1/(1-x)$ | $\vert x\vert <1$ |
| $\sum_{k=1}^{\infty}kx^{k-1}=1/(1-x)^2$ | $\vert x\vert <1$；可由前式逐项求导 |

#### 求和方法与补充序列（Summation Methods and Further Sequences）

- **几何求和（geometric sum）** 由S与rS错位相减；区间和$\sum_{k=m}^na_k$用从起点到n的和减去到$m-1$的和；

  望远镜求和／乘积（telescoping sum / product）消去中间项，例如$\prod_{k=1}^n(k+1)/k=n+1$。

  无穷级数（infinite series）须检查收敛条件（convergence condition），逐项求导不是任意级数都合法。

  奇数和的几何证明（geometric proof）：从$(n-1)\times(n-1)$方格扩成$n\times n$方格，新增一行一列但角格只计一次，共$n+(n-1)=2n-1$格；逐层相加得到$n^2$。

- **【拓展／补充】Ulam数（Ulam numbers）** 以1、2开头，每次选能唯一表示为两个不同较小已入选项之和的最小整数；开头$1,2,3,4,6,8,11,13,16,18,26,28,36,38,47,48,53,57,62,69$。

  相同两项相加不算，存在多种表示也不算。

### 2.5 【拓展：本小节课堂未讲】可数性与无限基数（Countability and Infinite Cardinality）

#### 等势与可数性（Cardinality and Countability）

- **等势（same cardinality / equinumerosity）** 用双射定义；$|A|\le|B|$用A到B的单射定义，严格小于还要求不等势。无限集可与自身真子集等势，不能机械套有限集结论。

- **可数集（countable set）** 指有限集或可数无穷集；可数无穷（countably infinite）与$\mathbb Z^+$双射，基数$\aleph_0$；不可数（uncountable）不能如此枚举。

  证明无限集可数可给双射或不重不漏的序列；可数集的子集仍可数。

#### 可数集的枚举（Enumerating Countable Sets）

- **希尔伯特大饭店（Hilbert's Grand Hotel）** ：房间$n\mapsto n+1$可腾一间，$n\mapsto2n$可容纳又一列客人；

  可数辆车各有可数客人时，用二维对角枚举（diagonal enumeration）安置。$\mathbb Z$按$0,1,-1,2,-2,\ldots$列；正有理数按分子分母之和分层并去重；加0和负数得$\mathbb Q$可数。

![[C2-图8-正有理数可数的排列路径.png|430]]

- **可数个可数集的并（countable union of countable sets）** 可沿二维对角线枚举，重复元素删去；有限笛卡尔积、有限字母表上的所有有限串也可数。

  不是说可数个集合的无限笛卡尔积仍可数；无限二进制串已不可数。

#### 对角线与双射判据（Diagonalization and Bijection Criteria）

- **康托尔对角线论证（Cantor's diagonal argument）** ：假设$(0,1)$实数列为$x_1,x_2,\ldots$，构造y的第n位与$x_n$第n位不同，如只用1、2避免小数双重表示，y不在列表中，矛盾。

  故$\mathbb R$不可数；无理数若可数，与$\mathbb Q$并就使$\mathbb R$可数，也矛盾。

- **Schröder–Bernstein定理（Schröder–Bernstein theorem）** ：若A到B、B到A各有单射，则有双射。用来证明区间与整条实数轴等势、平面与直线等势时，不必硬构造双射；

  小数交织（digit interleaving）需处理双重展开问题。

#### 不可计算函数与更大的无限（Uncomputable Functions and Larger Infinities）

- **可计算函数（computable function）** 有有限程序对每个合法输入给出输出；

  有限字母表的程序只有可数多个，而$\mathbb N\to\{0,1\}$的函数已有不可数多个，故存在不可计算函数（uncomputable function）。这是非构造性存在证明；

  不能把十进制展开直接当一一对应而忽略$0.4999\ldots=0.5000\ldots$。

- **康托尔定理（Cantor's theorem）** ：$|S|<|\mathcal P(S)|$。若f满射到幂集，取$T=\{s:s\notin f(s)\}$，考察$f(t)=T$即矛盾。

  连续统（continuum）基数$\mathfrak c=|\mathbb R|=2^{\aleph_0}$；

  连续统假设（continuum hypothesis, CH）称不存在严格介于$\aleph_0$与$\mathfrak c$之间的基数，在通常选择公理框架下表述为$\mathfrak c=\aleph_1$。

  它相对于标准ZFC公理的独立性（independence）以公理系统相容为前提，不是已证明为假的猜想。

### 2.6 【拓展：本小节课堂未讲】矩阵与布尔矩阵（Matrices and Boolean Matrices）

#### 普通矩阵运算（Ordinary Matrix Operations）

- $m\times n$矩阵（matrix）有m行、n列，条目（entry）为$a_{ij}$；

  行矩阵（row matrix）、列矩阵（column matrix）、方阵（square matrix）、零矩阵（zero matrix）按形状或条目命名。相等要求同型且逐项相等；

  和（sum）、数乘（scalar multiplication）逐项运算。

- **普通矩阵积（matrix product）** ：A为$m\times k$、B为$k\times n$才可作AB，$(AB)_{ij}=\sum_{t=1}^ka_{it}b_{tj}$，结果$m\times n$。

  AB与BA可能一方无定义或形状不同，即使同型也一般不相等；结合律、对加法分配律在维数合法时成立。

#### 幂、转置与逆（Powers, Transposes and Inverses）

- **单位矩阵（identity matrix）** I对角1其余0；$A^0=I$、$A^{r+s}=A^rA^s$。转置（transpose）$(A^T)_{ij}=a_{ji}$，$(A+B)^T=A^T+B^T$，$(AB)^T=B^TA^T$。

  对称矩阵（symmetric matrix）满足$A^T=A$。

  对任意实方阵$A$，$A+A^T$是对称矩阵，因为$(A+A^T)^T=A^T+A=A+A^T$。证明时用转置的加法规则与二次转置还原，不是只观察一个数值例。

- **数量矩阵（scalar matrix）** 形如$cI$，它与每个同阶方阵$B$交换：$(cI)B=cB=B(cI)$。

  原自测还要求反向判断：若实$2\times2$矩阵$A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$与所有同阶矩阵交换，先令$B=\begin{bmatrix}1&0\\0&0\end{bmatrix}$，由$AB=BA$得$b=c=0$；再令$B=\begin{bmatrix}0&1\\0&0\end{bmatrix}$得$a=d$，故$A=aI$。矩阵环的中心（center of a matrix ring）就是这些与所有元素交换的矩阵。

- **逆矩阵（inverse matrix）** 满足$AA^{-1}=A^{-1}A=I$；不是逐项取倒数。$A=\begin{bmatrix}0&1\\-1&0\end{bmatrix}$有$A^2=-I,A^4=I$，幂按模4循环；

  这是周期矩阵幂（periodic matrix powers）的例子。

#### 布尔矩阵及可达性（Boolean Matrices and Reachability）

- **零一矩阵／布尔矩阵（zero–one / Boolean matrix）** 条目0或1；并／合取的对偶运算（join / meet）逐项OR／AND；

  布尔积（Boolean product）记$A\odot B$：$(A\odot B)_{ij}=\bigvee_t(a_{it}\land b_{tj})$。普通积数中转方案个数，布尔积只问是否存在；不能把OR换成算术加法。

- **布尔幂（Boolean power）** $A^{[0]}=I$、$A^{[r+1]}=A^{[r]}\odot A$表示恰好r步的可达性（reachability）。

  不同于任意正长度可达性，后者为$A\lor A^{[2]}\lor\cdots\lor A^{[n]}$，与传递闭包相接。

- 逐项并交有幂等、交换、结合、分配律，$A\lor0=A$、$A\land0=0$；布尔积有结合律和单位元I、零元0，也对逐项OR分配，但一般不交换。不要把逐项AND与布尔积当同一个运算。

- **布尔幂的最终周期性（eventual periodicity of Boolean powers）** ：$n\times n$布尔矩阵只有$2^{n^2}$种，幂序列必有$A^{[p]}=A^{[q]}$（$p<q$）；继续右乘$A$，得到对所有$k\ge0$都有$A^{[p+k]}=A^{[q+k]}$。

  “最终周期”不等于“最终不变”。例如$A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$的布尔幂在$A,I$间交替，并不逐项只增不减；逐项单调的是累计并$A\lor\cdots\lor A^{[r]}$。

  若某次幂等于全1矩阵$J$，且$A$每列至少有一个1，则$J\odot A=J$，后续幂才保持为$J$。原例的稳定性应由这一乘法条件解释，不能只说“OR不会把1改回0”。

---

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

#### 逆关系与计数（Inverses and Counting）

- **逆关系（inverse relation）** $R^{-1}=\{(b,a):(a,b)\in R\}$；$(R^{-1})^{-1}=R$，逆保持并、交、差及适当全集下的补；$(S\circ R)^{-1}=R^{-1}\circ S^{-1}$，复合次序反转。

- **【拓展／补充】关系计数（counting relations）** ：若$|A|=m,|B|=n$共有$2^{mn}$个A到B关系。n元集上总数$2^{n^2}$；自反与反自反各$2^{n(n-1)}$；对称$2^{n(n+1)/2}$；

  反对称$2^n3^{\binom n2}$；非对称$3^{\binom n2}$；同时对称反对称$2^n$。方法是对角线逐位选、不同点的无序对分别选。传递性把不同位置的选择耦合，不能套上述独立选择法；

  原笔记列$n=4,5,6$的传递关系数3994、154303、9415189仅作计数背景。

![[C9-四个性质的有向图判读.png|650]]

### 3.2 多元关系与数据库（n-ary Relations and Databases）

#### 记录、属性与键（Records, Attributes and Keys）

- $n$元关系（$n$-ary relation）$R\subseteq A_1\times\cdots\times A_n$，度（degree）为n，不是记录条数。

  关系数据库（relational database）把n元组作为记录／行（record / row），各分量为字段／属性（field / attribute），各$A_i$为属性论域（domain）。

  数学关系是集合，不保留重复行与自然行序。

- **外延（extension）与内涵（intension）** ：外延是当前实际存储的元组集合，内涵是表名、属性、论域及取值规则等相对固定的结构约束。

  选键不能只看当前外延碰巧没有重复，还须确认内涵允许的未来记录也符合唯一性约束；这正是“当前姓名不重名”不能保证姓名永远可作键的原因。

- **主键（primary key）** 可唯一标识记录；复合键（composite key）由多个属性联合区分。当前记录恰好不重不等于未来数据也受唯一性保证，新增记录须维持键约束。学号比姓名更适合作标识；

  分表减少重复信息（redundancy），但需正确的连接条件才能恢复。

#### 选择、投影与连接（Selection, Projection and Join）

选择、投影、连接属于关系代数（relational algebra）：输入关系，按明确规则生成新的关系。

- **选择（selection）** $s_C(R)$按条件C筛行，度不变；投影（projection）$P_{i_1,\ldots,i_k}(R)$按指定次序选列，度变为k，并去除重复元组，故行数可能减少。

- **连接（join）** $J_p(R,S)$把R末p列与S前p列相同的记录配对，公共部分只留一次，结果度$m+n-p$。先对齐列序，再比较公共字段全部取值；

  匹配是多对多时可能产出多行，行数不是简单取最小值或固定乘积。未配上的记录不在内连接（inner join）结果中。

#### SQL与考试信息的边界（SQL and Examination Evidence）

- **【拓展／补充】SQL（Structured Query Language）** 中WHERE对应选择，SELECT对应投影；数学投影去重，在SQL中须留意DISTINCT与默认重复保留语义。

  JOIN…ON指定连接条件；左／右／全外连接（left / right / full outer join）保留未匹配行并填NULL，不是本节$J_p$的定义。

  先筛选再连接（selection pushdown）常可减少中间表，但须保证条件只依赖对应输入属性。

- **【复习定位】** 原章节汇总称§9.2、§9.3通常出小问；现有转写未找到足以逐字确认该承诺的原话，因此按“笔记中的复习提示”保留，不标成老师明确限定题量。六种性质、偏序与闭包仍完整掌握。

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

- **路径长度（path length）** 为边数；正长度回路（circuit）可使$(a,a)$进入传递闭包。有限n元集上$t(R)=R\cup R^2\cup\cdots\cup R^n$；

  不同端点的路径可去掉重复段缩到至多$n-1$步，自身到自身的正长度回路最多需n步，不能统一删成$n-1$上界。

- 证明闭包正确需三件事：包含R；满足目标性质；被任意满足性质的R之超关系（superrelation）包含。传递闭包的传递性靠拼接路径，最小性靠任意传递超关系都包含各次幂。

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

#### 手算例（Worked Calculation）

- 手算练习：$R=\{(1,2),(2,3),(3,2)\}$，有

$$
W^{(0)}=W^{(1)}=\begin{bmatrix}0&1&0\\0&0&1\\0&1&0\end{bmatrix},\quad
W^{(2)}=\begin{bmatrix}0&1&1\\0&0&1\\0&1&1\end{bmatrix},\quad
W^{(3)}=\begin{bmatrix}0&1&1\\0&1&1\\0&1&1\end{bmatrix}.
$$

2与3在正长度回路中，所以对角变1；1没有返回自己的路，对角仍0。不能在初始化时不加说明地填满对角线。

![[C9-Warshall两种情形.png|600]]

#### 闭包的保留性质与次序（Preserved Properties and Order of Closures）

- 已有性质则闭包不变：$r(R)=R\iff R$自反，其余同理。三种闭包均包含原关系、幂等（idempotent）且对包含单调。自反闭包保持对称和传递，传递闭包保持自反和对称，对称闭包保持自反，但可破坏传递。

- **【拓展】闭包次序（order of closure operations）** ：$r(s(R))=s(r(R))$，$r(t(R))=t(r(R))$；一般$s(t(R))\subseteq t(s(R))$且可能严格不等。

  例$R=\{(1,2),(3,2)\}$原本传递，先对称后传递得到3点全关系9对，先传递后对称只有4对。闭包不普遍对差、补分配；如$t(R_1-R_2)\ne t(R_1)-t(R_2)$。求逆与自反闭包相容：$r(R^{-1})=r(R)^{-1}$。

### 3.5 等价关系、等价类与划分（Equivalence Relations, Classes and Partitions）

#### 等价关系、等价类与划分（Equivalence, Classes and Partitions）

- **等价关系（equivalence relation）** 要求自反、对称、传递同时成立；逐条证明，或转化成$f(x)=f(y)$型关系。典型例子：同余、字符串等长、相同函数值；

  “有共同朋友”“差小于某阈值”等不自动传递。

- **等价类（equivalence class）** $[a]_R=\{x\in A:xRa\}$；$aRb\iff[a]=[b]\iff[a]\cap[b]\ne\varnothing$。不同代表元（representative）可表示同一类；类必非空，包含自己的代表元；

  不同的类两两不交。

- **划分（partition）** 是非空块（block）的集合，块两两不交且并为A。等价关系与划分一一对应：R给出全部不同等价类；划分$\{A_i\}$反推$R=\bigcup_i(A_i\times A_i)$。

  商集（quotient set）$A/R=\{[a]:a\in A\}$的元素是类，不是A中的普通元素。

#### 类的大小与前缀分类（Class Sizes and Prefix Classification）

- 有限块大小为$n_i$时，关系中有$\sum_i n_i^2$个有序对，商集大小为块数。模m同余（m为正整数）有m类$[0]_m,\ldots,[m-1]_m$，$a\equiv b\pmod m\iff m\mid(a-b)$。

- **位串前n位关系（prefix equivalence）** ：$sRt$当$s=t$或两串长度均至少n且前n位相同。

  短于n的串每串单独一类，长串按$2^n$个前缀分类，共$(2^n-1)+2^n=2^{n+1}-1$类，n=3时15类，不能只答8。

![[C9-集合的划分示意.png|510]]

- 等价关系在非空底集上必自反，因而不反自反、也不非对称；它若还反对称，就只能是相等关系$\Delta_A$。

  由$f(a)=f(b)$定义的关系自动满足三条性质，是“用标签分类（classification by labels）”的通用构造。

#### 【拓展】等价关系的构造与计数（Constructions and Counting）

- **带正负号的同余关系（congruence up to sign）** ：整数上$aRb\iff a\equiv b\pmod7$或$a\equiv-b\pmod7$，也是等价关系。

  自反取正号；对称可反解；传递时若$a\equiv\varepsilon_1b$、$b\equiv\varepsilon_2c$且$\varepsilon_i\in\{1,-1\}$，则$a\equiv\varepsilon_1\varepsilon_2c$，符号仍在$\{1,-1\}$中。

  等价类是把原同余类按相反数合并，四个类分别为$7\mathbb Z$、$(7\mathbb Z+1)\cup(7\mathbb Z+6)$、$(7\mathbb Z+2)\cup(7\mathbb Z+5)$、$(7\mathbb Z+3)\cup(7\mathbb Z+4)$。这些类由整数构成，不是把“余数类本身”误当作底集元素。

- **【拓展／补充】两类构造** ：$(a,b)\sim(c,d)\iff a-b=c-d$在整数对上的类是固定差的整点；这也是用自然数对构造整数的思想。

  实数上$x\sim y\iff x-y\in\mathbb Q$，$[1]=[1/2]=\mathbb Q$、$[\pi]=\pi+\mathbb Q$，类称加法陪集（additive coset）。

- **【拓展／补充】循环关系（circular relation）** 满足$aRb\land bRc\Rightarrow cRa$；自反＋循环当且仅当等价关系。证明先用$bRb$得对称，再用循环＋对称得传递，不可提前使用待证结论。

- **【拓展／补充】划分计数（counting partitions）** ：第二类Stirling数（Stirling number of the second kind）$S(n,k)=kS(n-1,k)+S(n-1,k-1)$，$S(0,0)=1$；

  Bell数（Bell number）$B_n=\sum_kS(n,k)$计所有等价关系。$S(5,3)=\binom53+5\binom42/2=25$，$B_5=52$；块无序，大小相同的块不能重复编号计数。

### 3.6 偏序、Hasse图、格与拓扑排序（Partial Orders, Hasse Diagrams, Lattices and Topological Sorting）

#### 偏序、可比性与字典序（Partial Orders, Comparability and Lexicographic Order）

- **偏序（partial order）** 为自反、反对称、传递关系；偏序集（partially ordered set, poset）记$(A,\preccurlyeq)$。

  严格偏序（strict partial order）为反自反且传递，因而非对称；由非严格序删除对角得到严格序，反过来补对角。等价关系用对称，偏序用反对称。

- **可比（comparable）** 指$a\preccurlyeq b$或$b\preccurlyeq a$，否则不可比（incomparable）。任意两点可比为全序／线性序（total / linear order）；

  链（chain）为其中全序的子集，反链（antichain）为不同元素两两不可比的子集。正整数整除与幂集包含一般只是偏序。

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

- **格的有限子集（finite subsets of a lattice）** ：任意有限非空子集都有lub与glb，可反复取二元并交；单元素集合的两者都是该元素。

  对大小归纳，$\operatorname{lub}(B\cup\{x\})=\operatorname{lub}(B)\vee x$，glb同理。因此有限非空格必有最大元和最小元，即为有界格；不能把“有限”去掉后照搬。

  空子集另需边界条件：$\operatorname{lub}(\varnothing)$若存在是全格的最小元，$\operatorname{glb}(\varnothing)$若存在是最大元。一般格只保证二元并交，不自动保证空子集也有界。

| 偏序集 | 并／lub | 交／glb |
|---|---|---|
| $(\mathcal P(S),\subseteq)$ | $A\cup B$ | $A\cap B$ |
| $(\mathbb Z^+,\mid)$ | 最小公倍数（least common multiple, lcm） | 最大公因数（greatest common divisor, gcd） |
| 全序集（total order） | max | min |

- 在整除偏序的某个子集里，环境中未包含lcm时不能直接把外面的数当lub；在子集内可能另有最小共同上界，或根本没有。

  信息流格（information-flow lattice）用安全级别与允许流动关系建模，并交表示共同约束的合成。

#### 格的类型与对偶（Lattice Types and Duality）

- **分配格（distributive lattice）** 满足$a\vee(b\wedge c)=(a\vee b)\wedge(a\vee c)$及对偶式；一般格未必分配。

  五元素菱形$M_3$的中间三点a、b、c使$a\vee(b\wedge c)=a$而$(a\vee b)\wedge(a\vee c)=1$。

- **有界格（bounded lattice）** 同时有底（bottom）0与顶（top）1；正整数整除格虽有底1但无顶，不有界。补元（complement）y满足$x\vee y=1,x\wedge y=0$；

  人人有补称补格（complemented lattice）。三元素链有界但中间元素无补；$M_3$有补但某点可有两个补。分配格中的补若存在则唯一；有界、分配且有补的格为布尔代数。

- **对偶原理（principle of duality）** 反转序、互换并交与顶底，得到对偶格（dual lattice）的对应真命题；不能只换符号不换序。

#### 【拓展】障碍、良序与排序（Obstructions, Well-orders and Sorting）

- **【拓展】分配格障碍（obstructions to distributivity）** ：格分配当且仅当不含同构于$M_3$或五边形$N_5$的 **子格（sublattice）** 。

  必须保留并交运算，不是画面“像菱形／五边形”就够；$N_5$是一条$0<a<b<1$链加$0<c<1$且c与a、b均不可比，原笔记的描述需如此修正。

- **【拓展】良序（well-order）** 为全序且每个非空子集有最小元；$\mathbb Z^+$及其二元组的字典序是良序，$(\mathbb Z,\le)$不是。

  良序归纳原理（well-ordered induction）若对每个y，由所有$x\prec y$的P(x)可推出P(y)，则处处成立；

  最小元的情形已包含在该条件中，不能只说“省略基础步”而不证明它也被覆盖。证明用最小反例（minimal counterexample）。

- **【拓展】拓扑排序（topological sorting）／线性扩张（linear extension）** 将有限偏序排为与原序一致的线性序。反复选极小元、输出并删除；

  有向无环图（directed acyclic graph, DAG）中等价于反复选入度0的顶点（Kahn's algorithm）。可能有多个合法答案；若尚有顶点但无入度0点则有环。

  邻接表实现$O(v+e)$，用于先修课与项目依赖排期。

- **【拓展／补充】关系的偏序（orders on relations）** ：全部关系按包含构成幂集偏序；全部划分按加细（refinement）排序，加细表示每块包含在另一划分某块中，对应等价关系包含。

  最细划分为每元素一块，最粗为全集一块。

---

## 四、计数（Counting）

组合数学（combinatorics）研究离散对象的计数、构造与结构；本部分同时讨论“有多少个”与“怎样不重不漏地生成”。

### 4.1 基本计数原理（Basic Counting Principles）

#### 加、乘、减、除四原理（The Four Counting Rules）

- **乘法原理（product rule）** ：任务分步，每个合法前缀的下一步都有固定的$n_i$个选择，总数$\prod_i n_i$。

  不要求概率意义的独立（independence），但若分支数依前面选择而不同，就应分类或用树形图逐支相加。

- **求和原理（sum rule）** ：互不相交的类型分别有$n_i$种，总数$\sum_i n_i$。“先分类、类内分步、最后求和”处理长度不同的密码、变量名与多方案任务。

- **减法原理（subtraction rule）** ：总数减不合法数；有交叠时用容斥。例：长度n位串“以1开头或以00结尾”，$n\ge3$时为$2^{n-1}+2^{n-2}-2^{n-3}$；“至少一个”常用总数减一个也没有。

- **除法原理（division rule）** ：若每个实际对象恰被表示d次，则实际数为表示数除d。纤维大小（fiber size）必须一致；对象有对称性（symmetry）时不能不检查就除固定阶乘。

#### 圆排列与函数计数（Circular Arrangements and Function Counts）

- **圆排列（circular permutation）** ：n个不同人围圆桌、只把旋转看成同一排法时为$(n-1)!$；若座位编号则为$n!$；镜像（reflection）是否视同须题目说明。

  两方向相同的无向环游在$n\ge3$时常再除2。

- **函数计数（counting functions）** ：m元集到n元集总函数$n^m$；单射在$m\le n$时为$P(n,m)$，$m>n$时0；每个输入依次选输出，单射使候选数递减。

  位串为$2^n$，长度r的n元字母串为$n^r$；首位、禁用字符等限制应单独处理。

#### 树形图与受限计数（Tree Diagrams and Restricted Counts）

- **树形图（tree diagram）** ：根到叶的一条完整分支对应一个合法对象，内部节点不是完成结果。五局三胜（best-of-five series）胜方先拿3场即停止，不可把结束后的比赛也计入；

  长度3、4、5的赛果分别2、6、12，共20种。T恤尺寸与颜色若某尺寸可选颜色不同，也须逐分支计数。

- **【拓展／补充】历史IPv4分类计数（classful IPv4 counting）** ：按原题A、B、C类位段限制计数，A类网络部分排除全0，主机部分排除全0与全1；

  数目分别$(2^7-1)(2^{24}-2)$、$2^{14}(2^{16}-2)$、$2^{21}(2^8-2)$，和为3,737,091,842。这里是教材题设的历史模型，不当作现行网络地址分配规则。

### 4.2 鸽巢、拉姆齐与子序列（Pigeonhole, Ramsey and Subsequences）

#### 鸽巢与保证阈值（Pigeonhole Principle and Thresholds）

- **鸽巢原理／抽屉原理（pigeonhole principle / Dirichlet drawer principle）** ：$k+1$个物体进k盒至少一盒有两个；

  从更大有限集到更小有限集不存在单射。广义鸽巢原理（generalized pigeonhole principle）：N个物体进k盒，至少一盒$\lceil N/k\rceil$个。

- **反问题（inverse problem）** ：要保证至少一盒有r个，最少$k(r-1)+1$个；若各盒容量上限不同则超过其上限和才强制违例。

  证明先写清“物体”“盒子”“分配规则”，给出最坏分配说明阈值不能再小。

#### 构造盒子的三种方法（Three Ways to Construct Boxes）

- **余数类（residue class）** 作盒子：两个数模n同余则差可被n整除。对$1,11,111,\ldots$的余数用鸽巢，或直接遇0余数，或两个相同余数相减，得到每个正整数都有一个仅含0、1的十进制正倍数。

- **连续区间和（consecutive interval sum）** 先变前缀和（prefix sum）的差。

  例30天每天至少1场、总共至多45场：30个严格递增前缀和$a_j$与$a_j+14$共60数落在1至59，必跨组相等，故某连续天数正好14场。原证明对其他目标数是否适用要重验取值范围；

  证明失效不等于结论已被反驳。

- **因子分解（factorization）** 作盒子：$1,\ldots,2n$中的$n+1$个数写成$2^kq$，奇数q只有n种，两个共q者一个整除另一个。奇数核（odd part）而非数本身是盒子。

#### 生日问题与拉姆齐（Birthday Problem and Ramsey Theory）

- **生日问题（birthday problem）** ：保证同生日要考虑366种日期，367人才必然重复；这是必然性（certainty）。

  **【拓展】概率版本（probabilistic version）** 假设365天等可能且独立，n人至少一对同生日概率$1-\prod_{i=0}^{n-1}(365-i)/365$，n=23时约0.5073；“概率超过一半”不是“保证”。

- **拉姆齐数（Ramsey number）** $R(r,s)$是使任意红蓝边染色的完全图必含红$K_r$或蓝$K_s$的最小顶点数。$R(3,3)=6$：从一点的5条边至少3条同色；

  这3个邻点若有同色边，与原点成同色三角形，否则3条边全为另一色。五边形的边涂一种色、对角线另一色给出5点反例，故不能只证明上界6就直接写等号。

![[C6.2-K6二色染色必有同色三角形.png|510]]

#### 子序列定理（Monotone Subsequence Theorem）

- **子序列（subsequence）** 保留原顺序但可不连续；连续子串／连续子段（substring / contiguous segment）不可跳项。

  Erdős–Szekeres单调子序列定理（monotone subsequence theorem）：$n^2+1$个互异实数必有长$n+1$的严格递增或递减子序列。

  给第i项标记以它结尾的最长递增与递减长度$(I_i,D_i)$；若两长度均不超过n，仅$n^2$种标签；不同项标签不相同，鸽巢矛盾。互异条件不能漏，n=3即10项保证长4。

- **【拓展】拉姆齐理论的解释边界（limits of Ramsey-style conclusions）** ：规模足够大时保证某种结构存在，不保证该结构有预测价值。

  原笔记较大拉姆齐数的区间属于写作时的背景，不作为当前最新研究进展或本课程计算公式。

### 4.3 排列、组合与约束（Permutations, Combinations and Constraints）

#### 排列与组合公式（Permutation and Combination Formulas）

- **r排列（r-permutation）** 为从n个不同对象无放回取r个并排序，$P(n,r)=n(n-1)\cdots(n-r+1)=n!/(n-r)!$；r组合（r-combination）只选不排，$C(n,r)=\binom nr=n!/[r!(n-r)!]$。

  $P(n,0)=\binom n0=1$，空排列是唯一一种；$\binom nr=0$约定用于整数$r<0$或$r>n$。

- $P(n,r)=\binom nr r!$源于每个无序子集对应$r!$种顺序；$\binom nr=\binom n{n-r}$源于选入与选出互补。锦标赛名次／不同职务要排列，无职务委员会要组合；先选人再分配职务可能两步都要。

#### 计算与应用（Calculation and Applications）

- 计算组合数可取$r\leftarrow\min(r,n-r)$，约分或用$\binom n{r+1}=\binom nr(n-r)/(r+1)$，避免先算巨大阶乘。阶乘与Stirling近似的区别见2.3。

- 位串恰有r个1为$\binom nr$；至少r个1为$\sum_{k=r}^n\binom nk$；两系分别选a、b人为$\binom{n_1}a\binom{n_2}b$；

  彩票匹配恰k个中奖号可用$\binom rk\binom{n-r}{r-k}$，全体结果为$\binom nr$（按题设抽取r号）。

#### 分组与相邻约束（Grouping and Adjacency Constraints）

- 不同标签小组大小$n_1,\ldots,n_k$，总n人分组为$n!/(\prod_i n_i!)$；若等大小的组也不可区分，再除这些等类组的排列次数，不是所有分组一律除$k!$。

- **捆绑法（block method）** ：指定k人必须相邻，把他们当一块，与其他人一起排，再乘块内$k!$；指定内部顺序固定时不乘。

  插空法（gap method）：先排其余m人有$m+1$空，k个指定人两两不相邻时选k空再排人，$m!\binom{m+1}k k!$；可行条件$k\le m+1$。

- 相邻关系有重叠时用容斥，两个被禁止相邻对可能形成三人块；“至少一对相邻”的补集不总是“某指定一对相邻”。

  圆桌空隙为m而非$m+1$，固定旋转后为$(m-1)!\binom mk k!$（m个背景对象不同且$m\ge1$）。

![[C6-相邻约束的捆绑与插空.png|600]]

### 4.4 二项式系数与组合证明（Binomial Coefficients and Combinatorial Proofs）

#### 二项式定理与恒等式（Binomial Theorem and Identities）

- **二项式定理（binomial theorem）** ：$(x+y)^n=\sum_{k=0}^n\binom nk x^{n-k}y^k$，n为非负整数；二项式系数（binomial coefficient）数出从n个因子中选哪k个提供y。

  求$(ax+by)^n$中目标项先匹配指数，再乘相应$a^{n-k}b^k$，没有对应整数k则系数0。

| 恒等式（identity） | 条件与计数解释 |
|---|---|
| $\sum_{k=0}^n\binom nk=2^n$ | 所有子集按大小分类 |
| $\sum_{k=0}^n(-1)^k\binom nk=0$ | $n\ge1$；奇偶大小子集各$2^{n-1}$个，可用切换固定元素的双射 |
| $\sum_{k=0}^n2^k\binom nk=3^n$ | 先选k个入选对象，再各涂两种颜色；或每对象三种状态 |
| $\binom nr=\binom{n-1}{r-1}+\binom{n-1}r$ | 帕斯卡恒等式（Pascal's identity）；按固定对象是否入选 |
| $\binom{m+n}r=\sum_{k=0}^r\binom mk\binom n{r-k}$ | 范德蒙德恒等式（Vandermonde's identity）；按来自第一组的人数 |
| $\sum_{k=0}^n\binom nk^2=\binom{2n}n$ | 前式取两组各n、总选n |
| $\sum_{k=r}^n\binom kr=\binom{n+1}{r+1}$ | 曲棍球棒恒等式（hockey-stick identity）；按最大入选元素分类 |

#### 帕斯卡三角与证明方法（Pascal’s Triangle and Proof Methods）

- **帕斯卡三角（Pascal's triangle）** 两边为1、内部为上方两数和；也是以递推计算二项式系数的方法。

  曲棍球棒亦可按长度$n+1$、含$r+1$个1的位串中最后一个1的位置分类，原文末尾“长度n”是笔误。

- **组合证明（combinatorial proof）** 包括双重计数证明（double-counting proof）和双射证明（bijective proof）：先明确所数对象，分别解释等式两边的每个因子／求和项，再证不重不漏；

  不能只写“由组合意义显然”。代数证明（algebraic proof）可通分阶乘或代入二项式展开，但题目若要求组合证明，应给对象解释。

- **【拓展】证明细节（proof details）** ：上述恒等式的按最大元素分类、奇偶子集双射等详细论证即使课堂略过，也作为正文中的证明方法保留；递推定义还要给边界值，不能只给内部关系。

### 4.5 重复选择、物体分配与整数分拆（Repetition, Distribution and Integer Partitions）

| 选择方式 | r次从n种中选择的结果数 |
|---|---|
| 有序、不可重复（ordered without repetition） | $P(n,r)$ |
| 无序、不可重复（unordered without repetition） | $\binom nr$ |
| 有序、可重复（ordered with repetition） | $n^r$ |
| 无序、可重复（unordered with repetition） | $\binom{n+r-1}r$，$n\ge1$ |

#### 星条法与整数解（Stars and Bars and Integer Solutions）

- **星条法（stars and bars）** ：r颗相同星代表物体，$n-1$条隔板代表n类，允许相邻隔板与端点隔板，分别表示空类；共$r+n-1$个位置选r个为星。

  它计无序重复选择，不计每个具体物体的身份。

- **弱组合（weak composition）** $x_1+\cdots+x_n=r,x_i\ge0$有$\binom{r+n-1}{n-1}$解；

  正整数解（positive integer solution）$x_i\ge1$有$\binom{r-1}{n-1}$解（$r\ge n$）。一般下界$x_i\ge l_i$先作$y_i=x_i-l_i$，剩余和为$r-\sum l_i$；

  剩余负则0解。

- **有上界（upper bounds）** 时星条法不能直接用；

  对违反$x_i\le u_i$的情况作容斥，集合S中变量统一减$u_i+1$：$\sum_{S\subseteq\{1,\ldots,n\}}(-1)^{|S|}\binom{r-\sum_{i\in S}(u_i+1)+n-1}{n-1}$，上方不足$n-1$的项按0处理。

#### 重复物体与循环计数（Repeated Objects and Loop Counts）

- **相同物体的排列（permutations with indistinguishable objects）** ：n个位置中各类型重复$n_i$次，$\sum n_i=n$，数为多项式系数（multinomial coefficient）$n!/(n_1!\cdots n_k!)$。

  每类内部交换不生成新串；从多重字母组成单词、固定各值数量的位串都用它。

- **嵌套循环（nested loops）** 如$1\le i_m\le\cdots\le i_1\le n$的执行次数为$\binom{n+m-1}m$，对应有重复m组合；严格不等时为$\binom nm$。不能只看m层循环就把精确次数写成$n^m$。

![[C6.5-星条法示意图.png|600]]

| n个物体分入k个盒子（distributing objects into boxes） | 允许空盒 | 各盒非空 |
|---|---|---|
| 物体、盒子均可区分（distinguishable） | $k^n$ | $\sum_{i=0}^k(-1)^i\binom ki(k-i)^n=k!S(n,k)$ |
| 物体不可区分、盒子可区分 | $\binom{n+k-1}{k-1}$ | $\binom{n-1}{k-1}$，$n\ge k$ |
| 物体可区分、盒子不可区分（indistinguishable） | $\sum_{j=0}^{\min(n,k)}S(n,j)$ | $S(n,k)$ |
| 物体、盒子均不可区分 | n的至多k部分分拆数 | n的恰k部分分拆数 |

#### 物体入盒与划分（Distribution and Partitions）

- 若可区分物体入可区分盒，且各盒人数$n_i$已固定，改用$n!/(\prod n_i!)$；每盒至多1则为$P(k,n)$（$n\le k$）。先问身份、盒子标签、是否允许空、每盒容量，再选公式。

- 第二类Stirling数的递推与初值见3.5；

  **【拓展／补充】容斥表达式（inclusion–exclusion expression）** $S(n,k)=\frac1{k!}\sum_{i=0}^k(-1)^i\binom ki(k-i)^n$，$n\ge1,k\ge1$。

  递推是笔记补足的标准结果，容斥闭式是原教材引用的结论；不能再声称该数“没有任何公式”。

#### 分拆、容量与边界（Integer Partitions, Capacities and Boundaries）

- **整数分拆（integer partition）** 只看各非空盒装多少，通常写非增序$n_1\ge\cdots\ge n_j>0$，不把顺序不同重算。

  若物体分成多个相同类型（如3苹果、2橘子、1香蕉）而非全部同一种，还要记录每盒的类型组合，不能仅用总数6的整数分拆替代；三盒每盒2个的例题按唯一香蕉所在盒分类，共3种。

> [!warning] 【易错】
> 不可区分盒允许空时，不能把$k^n$一律除$k!$；不同装法的空盒数与对称重数不同。0个物体的边界用唯一空分配处理，$S(0,0)=1$，不误把从j=1开始的求和用于$n=0$。

### 4.6 生成排列与组合的算法（Algorithms for Generating Permutations and Combinations）

> [!important] 【老师明确会考：第19节，00:38:36–00:39:40】
> 老师在演示下一个排列时说“我一定会考这个算法”，并强调大学内容是怎样用算法找出排列与组合，不只是计算数量。以下三个后继算法（successor algorithms）均应能手算，尤其要解释最小性。

词典序（lexicographic order）按第一个不同位置比较。后继（successor）是所有更大对象中最小者，不是任意更大者。

以下伪代码均用1起始下标（one-based indexing）。

#### 下一个排列：操作、例子与证明（Next Permutation: Steps, Example and Proof）

**下一个排列（next permutation）** ，输入互异元素的当前排列：

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

#### 下一个位串：二进制加一（Next Bit String: Binary Increment）

**下一个位串（next bit string）** ：从右向左将末尾连续1改成0，遇第一个0改成1，等价于二进制加1（binary increment）。全1已是最后一个；

从全0开始会遍历$2^n$个子集的特征串，但普通加1不保持1的个数，不能直接当固定r组合后继。

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

- **【拓展】小规模演算（small example）** ：$n=4,r=2$时$12\to13\to14\to23\to24\to34$；$n=5,r=3$时$123,124,125,134,135,145,234,235,245,345$。换成a至e字母，逐位替换即可，顺序不变。

#### 全部枚举与不重不漏（Complete Enumeration without Repetition）

- **生成全部r排列（generate all r-permutations）** ：先遍历$\binom nr$个组合，每组内部再列r!个排列，总$P(n,r)$个，不重不漏，因为每个排列所属底集唯一。

  **这种分组输出不保证全部r排列整体按词典序** ，只保证组合组序及各组内部序。

- **不重不漏证明（completeness and uniqueness）** ：从最小对象开始，后继严格增加且是最小更大者，最大对象停；有限全序中因此恰遍历全部对象。不能只凭“数量对了”断言没重复没遗漏。

  组合特征位串的二进制顺序与递增元组词典序也须区别，不能混接两种后继。

---

## 五、递推关系的应用（Applications of Recurrence Relations）

### 5.1 建模与初始条件（Modeling and Initial Conditions）

本章范围是已有的§8.1；没有把尚未整理的§8.2–8.6扩写成新章节。第19节课堂讲了递推定义、代入验证、复利、兔子、汉诺塔及受限位串；

码字、卡特兰数、讲座调度在原笔记中已补足，以下同样完整保留并标为拓展。

#### 建模检查（Modeling Checks）

- **模型（model）** 先定义$a_n$数什么、单位是什么、n从哪里开始；再写初值、递推式与适用下标。每个分支须互斥且完备；删去／追加部分要能双向对应并保证接缝合法。

  求通项（find a closed form）与建立递推（form a recurrence）是不同任务。

- **候选解验证（verification of a candidate solution）** 直接代入并检查全部初值。

  例如$a_n=2a_{n-1}-a_{n-2}$允许$3n$与常数5，但不允许$2^n$，因为后者右侧是$3\cdot2^{n-2}$，不同于$4\cdot2^{n-2}$，任何n都不相等。

  初值$a_0=3,a_1=5$时，减法递推$a_n=a_{n-1}-a_{n-2}$给$a_2=2,a_3=-3$，不要看成加法。

- **细菌翻倍（bacterial doubling）** $a_n=2a_{n-1},a_0=5$得$5\cdot2^n$；复利$S_n=(1+r)S_{n-1},S_0=P$得$P(1+r)^n$。时间单位、计息时刻改变时须重验下标。

### 5.2 兔子与汉诺塔（Rabbits and the Tower of Hanoi）

#### 兔子模型（Rabbit Model）

- **兔子繁殖（rabbit population）** ：按原模型幼兔满两个月才繁殖、无死亡，$f_1=f_2=1$，$f_n=f_{n-1}+f_{n-2}$（$n\ge3$）。分为上月已有与本月新生，不能假定所有幼兔立即翻倍；

  不同月龄计数约定会改变初值。

#### 三柱汉诺塔（Three-peg Tower of Hanoi）

- **三柱汉诺塔（three-peg Tower of Hanoi）** ：n个大小不同圆盘，单次搬一个且大盘不能压小盘。把前$n-1$盘搬开、移动最大盘、再搬回小盘，得可行上界$H_n\le2H_{n-1}+1$；

  任何解移动最大盘前后都需搬开／恢复小盘，得同样下界，故$H_n=2H_{n-1}+1,H_0=0$，解为$2^n-1$。仅给构造不能证明最少（minimum）。

  64盘需$2^{64}-1$次，展示指数增长（exponential growth）。

#### 【拓展】四柱变式（Four-peg Variant）

- **【拓展】四柱汉诺塔（four-peg Tower of Hanoi）** ：Frame–Stewart策略（Frame–Stewart strategy）$R_0=0,R_n=\min_{0\le m<n}\{2R_m+2^{n-m}-1\}$；

  先用四柱暂存m个小盘，中间用三柱搬其余盘。原笔记据Bousch 2014论文已修正四柱最优性历史，不沿用旧教材“尚未解决”的说法；此结论不外推到任意柱数。

### 5.3 受限位串与状态（Restricted Bit Strings and States）

#### 禁止00与禁止000（Forbidding 00 and 000）

- **不含00（no consecutive zeros）** ：合格n串按末尾1或10分类，$a_n=a_{n-1}+a_{n-2}$，$a_0=1,a_1=2$，得$1,2,3,5,8,13,\ldots$，$a_n=f_{n+2}$。

  只在合法短串后任添0会产生非法接缝，不能两类均算$a_{n-1}$。不含11的计数可通过0、1互换得到同型递推。

- **不含000（no three consecutive zeros）** ：末尾为1、10、100三类；$b_n=b_{n-1}+b_{n-2}+b_{n-3}$，$b_0=1,b_1=2,b_2=4$，从$n=3$适用得$b_3=7,b_4=13,b_5=24,b_6=44$。

  若采用原笔记$b_1,b_2,b_3$作初值，则递推从$n=4$开始。

#### 状态与转移（States and Transitions）

- **状态（state）** 可记末尾连续0个数0、1、2：添1回0，添0使状态递增，状态2不能添0。状态需要保存决定下一步是否合法的足够信息，不能把不同历史错误合并。

![[C8-三连零的状态转移.png|580]]

### 5.4 【拓展】码字与卡特兰数（Codewords and Catalan Numbers）

#### 偶数零码字（Codewords with Even Numbers of Zeros）

- **有效十进制码字（valid decimal codeword）** 为含偶数个0的长度n字符串，允许前导0，0个0也算偶数。

  记偶状态$E_n$、奇状态$O_n$，有$E_n=9E_{n-1}+O_{n-1}$、$O_n=9O_{n-1}+E_{n-1}$，$E_0=1,O_0=0$。非零数字保持奇偶，0翻转。

- 由$E_n+O_n=10^n$、$E_n-O_n=8^n$得$E_n=(10^n+8^n)/2$、$O_n=(10^n-8^n)/2$；也可用$E_n=8E_{n-1}+10^{n-1}$。$E_1=9,E_2=82,E_3=756$。把字符串误当n位整数会改变首位选择及全部初值。

#### 卡特兰递推与闭式（Catalan Recurrence and Closed Form）

- **卡特兰数（Catalan numbers）** $C_n$数$n+1$个保持原序的因子的完整加括号（full parenthesization）。

  按最后一次乘法分成左k次运算与右$n-1-k$次：$C_n=\sum_{k=0}^{n-1}C_kC_{n-1-k}$，$C_0=1$。分类按唯一最后切口，左右独立故相乘、各切口相加。

- $C_0,\ldots,C_5=1,1,2,5,14,42$，闭式$C_n=\binom{2n}n/(n+1)$，渐近$C_n\sim4^n/(n^{3/2}\sqrt\pi)$。

  相同数还计合法括号串（balanced parentheses）、不越过对角线的格路径（Dyck paths）、相应二叉树结构（binary tree shapes）。

  本小节证明递推，不把依赖后续生成函数（generating functions）的系统闭式证明冒充课堂已完成。

![[C8-卡特兰数的合法与非法路径.png|560]]

### 5.5 【拓展】动态规划与加权区间调度（Dynamic Programming and Weighted Interval Scheduling）

#### 动态规划的两个条件（Conditions for Dynamic Programming）

- **动态规划（dynamic programming, DP）** 利用最优子结构（optimal substructure）与重叠子问题（overlapping subproblems），保存中间答案；

  可用自顶向下记忆化（memoization）或自底向上填表（tabulation）。

  递归（recursion）必须有可达的终止条件（termination condition），重复展开子问题和没有终止条件是两种不同错误。

- **分治（divide and conquer）与动态规划的区别** ：分治将原问题拆成较小问题并合并结果；动态规划特别利用子问题的重叠，避免同一状态重复求值。仅仅写成递归，并不足以判断使用了DP。

  例如计算汉诺塔最少步数的递归表达式会反复用到同一$H_{n-1}$，可保存数值；实际输出移动序列仍要输出$2^n-1$次移动，不能用“保存步数”消除这些必要输出。比较两种方法时须先说明在计算数值还是生成操作序列。

#### 调度建模与递推（Scheduling Model and Recurrence）

- **加权区间调度（weighted interval scheduling）** 每场有开始$s_j$、结束$e_j$、权重$w_j\ge0$，$s_j<e_j$，按结束时间非降排序。

  相容（compatible）允许前场结束等于后场开始。前驱（predecessor）$p(j)=\max\{i<j:e_i\le s_j\}$，不存在取0；它是编号，不是场次数或时间。

- **前j场最优总权重（optimal total weight）** $T(j)=\max\{w_j+T(p(j)),T(j-1)\},T(0)=0$。选j则只能配前$p(j)$场最优安排；不选j则是前$j-1$场最优。

  用替换论证（exchange / replacement argument）说明子方案非最优会导致整体非最优。

#### 贪心反例（A Counterexample to the Greedy Choice）

- **最早结束贪心（earliest-finish-time greedy choice）** 可解最大场次数，但不保证最大总权重；两场各10人与一场覆盖二者时间的100人讲座形成反例。

  总人次（total attendances）不等于去重听众数（number of distinct attendees）。

![[C8.1-讲座时间轴与相容前驱.png|650]]

| j | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 原题前驱p(j) | 0 | 0 | 1 | 0 | 0 | 2 | 4 |
| 习题54(a)权重 | 20 | 10 | 50 | 30 | 15 | 25 | 40 |
| T(j) | 20 | 20 | 70 | 70 | 70 | 70 | 110 |

#### 方案恢复、平局与效率（Reconstruction, Ties and Efficiency）

- **恢复方案（reconstruction）** ：从n往前，若$w_j+T(p(j))\ge T(j-1)$，可选j并跳$p(j)$，否则退到$j-1$。例中得到$\{1,3,7\}$，总110。

  平局（tie）表示两条分支均能给某个最优解，不表示j在每一个最优解中；要输出全部最优解须保留两分支。

- 其余原题权重组(b)$100,5,10,20,25,40,30$得最优140，$\{1,6\}$与$\{1,3,7\}$均可；(c)$2,3,8,5,4,7,10$得20，$\{1,3,7\}$；(d)$10,8,7,25,20,30,5$得40，$\{1,6\}$。

  只给时间、不提供权重时不能算出唯一最大人次。

- 已知全部p时填表$O(n)$、恢复$O(n)$、空间$O(n)$；加排序与二分查找（binary search）求前驱，总$O(n\log n)$；逐个向前扫描求p则预处理最坏$O(n^2)$。

  不能把填表复杂度当整个算法复杂度。

---

## 六、图论（Graph Theory）

> [!tip] 【老师强调：第19、21节】
> 第十章是期末重点；第21节还要求未在课堂逐个展开的例题自行练习。以下不凭“课堂跳过”删去某一节，也不把充分条件当充要条件。

### 6.1 图的类型与建模（Graph Types and Modeling）

#### 图的组成与类型（Components and Types of Graphs）

- **图（graph）** $G=(V,E)$由顶点集（vertex set）与边集（edge set）组成；顶点（vertex / node）表示对象，边（edge）表示联系。

  先定义两者的含义，再决定方向、重数、自环；不要只看图形外观。

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

- “允许”不表示图里必须出现；一条有向边含有序起点（initial vertex）与终点（terminal vertex），相反方向的两弧不是同向重弧。

  带权图（weighted graph）给边附权重（weight），记录距离、时间、费用、容量等；同一拓扑不同权重会得到不同优化问题。

| 模型（model） | 顶点与边的含义 |
|---|---|
| 相识图（acquaintanceship graph） | 人；相互认识，通常无向简单 |
| 影响图（influence graph） | 人；谁影响谁，有向 |
| 合作图（collaboration graph） | 作者／演员；合作过，无向 |
| 呼叫图（call graph） | 号码；一次通话，有向且可有重弧 |
| 网页图（web graph） | 网页；超链接，有向 |
| 引用图（citation graph） | 文献；引用关系，有向 |
| 模块依赖图（module dependency graph） | 模块；按题设方向记录依赖，不能擅自反向 |
| 先序图（precedence graph） | 语句／任务；必须先于另一任务，合法顺序用拓扑排序 |
| 航空图（airline graph） | 机场；航班，有向且可多重 |
| 道路网络（road network） | 路口；路段，可能混合方向、带权与多重 |
| 生态位重叠图（niche overlap graph） | 物种；资源竞争／生态位重叠，无向 |
| 蛋白质相互作用图（protein interaction graph） | 蛋白质；相互作用，按题设常作无向 |
| 循环赛图（round-robin tournament graph） | 队伍；胜者指向败者，每对恰一条弧，称竞赛图（tournament） |
| 单淘汰赛树（single-elimination tournament tree） | 比赛；胜者进入下一场的依赖，有根树（rooted tree） |

#### 模型计数与交集图（Counting in Models and Intersection Graphs）

- n队单淘汰需$n-1$场比赛；n队每对赛一次需$\binom n2$场；节点代表比赛还是球队会改变图的顶点数。模型中的实际统计规模仅是原教材历史例子，不作为当代人口／网络规模；

  其数学作用是说明稀疏（sparse）与稠密（dense）存储差别。

- **【拓展】交集图（intersection graph）** 以集合为顶点，两个不同集合交非空才连边；

  同代图（contemporaneous graph）以人为顶点、生命时间区间相交表示同代，是区间交集图（interval intersection graph）的例子。

  无向简单图的邻接关系为对称且反自反；集合关系不能记录同一有序对的多次出现，重图需另存重数。

### 6.2 度、图族、二分图与匹配（Degrees, Graph Families, Bipartite Graphs and Matchings）

#### 邻接、度与握手定理（Adjacency, Degree and Handshaking）

- **邻接（adjacency）** 说两顶点有边相连；关联（incidence）说边以某顶点为端点。邻域（neighborhood）$N(v)$是邻接顶点集合，$N(S)=\bigcup_{v\in S}N(v)$；

  度（degree）$\deg v$数关联边的端点次数，自环计2，平行边逐条计。邻域大小不总等于度。

- **孤立点（isolated vertex）** 度0，悬挂点／叶（pendant vertex / leaf）度1；

  最大度（maximum degree）$\Delta(G)$、最小度（minimum degree）$\delta(G)$。

  握手定理（handshaking theorem）$\sum_v\deg v=2|E|$，故奇度顶点（odd-degree vertex）个数为偶数。

  r正则图（r-regular graph）满足每点度r，$rv=2e$。

#### 有向度与标准图族（Directed Degrees and Standard Families）

- **有向图入度（in-degree）** $\deg^-(v)$与出度（out-degree）$\deg^+(v)$分别数进入与离开的弧，自环各贡献1；$\sum_v\deg^-v=\sum_v\deg^+v=|E|$。

  底层无向图（underlying undirected graph）去掉方向，但是否合并反向弧须按题目约定。

| 图族（graph family） | 点数v | 边数e | 度与补充 |
|---|---|---|---|
| 完全图（complete graph）$K_n$ | n | $n(n-1)/2$ | 每点$n-1$ |
| 圈图（cycle graph）$C_n$，$n\ge3$ | n | n | 每点2 |
| 轮图（wheel graph）$W_n$，本书由$C_n$加中心 | $n+1$ | $2n$ | 中心n，轮缘各3 |
| n维超立方体（n-cube / hypercube）$Q_n$ | $2^n$ | $n2^{n-1}$（$n\ge1$） | n正则，位串差一位相邻 |
| 完全二分图（complete bipartite graph）$K_{m,n}$ | $m+n$ | mn | 两侧度分别n、m |
| 路径图（path graph）$P_n$ | n | $n-1$ | $n\ge2$时两端度1，其余度2 |

- 本书轮图的下标不包含中心；别的书可能用$W_{n+1}$表示同一对象。圈图标准定义从$n=3$开始，不能把单点空图硬叫作$C_1$再套圈的公式；$Q_0$可另定义为一个孤立点，边数0。

#### 二分图的判定（Bipartite Tests）

- **二分图（bipartite graph）** 的顶点可划为$V_1,V_2$，边全部跨两侧；等价于可用至多两色正确着色，等价于不含奇圈（odd cycle）。按距离奇偶分组或用BFS染色可检验；

  必须检查每个分量，不仅起点所在分量。

- $C_n$当且仅当n偶时二分（$n\ge3$），$K_n$当且仅当$n\le2$，所有$Q_n$按位串中1的奇偶分组，$W_n$含三角形故不二分。

  简单二分图$e\le|V_1||V_2|\le\lfloor v^2/4\rfloor$；只有两侧之间每对都连才在第一式取等，原笔记把一般二分图直接写e=mn需修正。r正则二分图在$r>0$时两侧等大，r=0不能据此推出。

#### 【拓展】匹配、Hall与代表系（Matching, Hall and SDR）

- **【拓展：课堂未展开】匹配（matching）** 为互不共享端点的边集；极大匹配（maximal matching）再加边就冲突，最大匹配（maximum matching）边数最多，二者不同。

  饱和（saturate）某侧表示该侧每点都被匹配；完美匹配（perfect matching）饱和全部顶点。

  本教材有时称“从$V_1$到$V_2$的完全匹配（complete matching）”，仅要求配满$V_1$，不要求两侧等大。

- **【拓展】Hall婚姻定理（Hall's marriage theorem）** ：有限二分图存在饱和$V_1$的匹配，当且仅当每个$A\subseteq V_1$都有$|N(A)|\ge|A|$；

  只查整个$V_1$或每个单点不够。必要性是不同人须占不同邻点；充分性可强归纳：若每个非空真子集都有富余，先选任一匹配边后删两端；若有子集卡等号，先匹配该子集与其邻域，再匹配余部。

  该证明不是简单的“随便贪心选边”。

- **【拓展】相异代表系（system of distinct representatives, SDR）** 从每个集合选不同元素，存在当且仅当任意k个集合的并至少k元；转换成集合—元素二分图即Hall。

  缺额（deficiency）$d(A)=|A|-|N(A)|$，最大匹配大小$|V_1|-\max_{A\subseteq V_1}d(A)$（包含空集使最大缺额非负）。

#### 网络拓扑（Network Topologies）

- **【拓展／应用】网络拓扑（network topology）** ：局域网（local area network, LAN）的星形（star）、环形（ring）、总线（bus）；

  并行互连（parallel interconnection）用完全图、线性阵列（linear array）、网格（mesh）与超立方体，取舍在链路成本、最大度与通信跳数（hop count）。

### 6.3 图的运算、补图与度序列（Graph Operations, Complements and Degree Sequences）

#### 子图与图运算（Subgraphs and Graph Operations）

- **子图（subgraph）** $H=(W,F)$满足$W\subseteq V,F\subseteq E$且边端点都在W中；生成子图（spanning subgraph）保留全部顶点；

  诱导子图（induced subgraph）$G[W]$保留W内原有全部边。删点（vertex deletion）同时删关联边；删边（edge deletion）保留点。

  真子图（proper subgraph）是与原图不同的子图，即至少删了一个顶点或一条边；生成子图也可能是真子图，诱导子图也可以等于原图。

  边收缩（edge contraction）把一条边两端粘合，并按题设处理新自环、平行边。

- **并图（union of graphs）** 取点边集合并，交图（intersection）取交；不交并（disjoint union）先保证点集互不相交。

  联图（join of graphs）$G+H$在不交并基础上加上全部跨图边：点$v_G+v_H$、边$e_G+e_H+v_Gv_H$，G侧顶点度加$v_H$，H侧加$v_G$。

- **笛卡尔积图（Cartesian product of graphs）** $G\square H$顶点为$(g,h)$；只有“一坐标相同、另一坐标相邻”才连边，不能两坐标同时变。

  点数$v_Gv_H$，边数$e_Gv_H+e_Hv_G$；$\deg(g,h)=\deg_Gg+\deg_Hh$。$P_m\square P_n$是网格，$Q_{r+s}\cong Q_r\square Q_s$。

> [!tip] 【老师强调：第20节转写约L501–521】
> 老师说很可能在图的运算这里出期末题，尤其join与Cartesian product，但随后明确未承诺一定作为题目。手算应同时会画图、算点边数、算新度数。

![[C10-join与笛卡尔积.png|650]]

#### 【拓展】子图计数与补图（Counting Subgraphs and Complements）

- **【拓展】子图计数（counting subgraphs）** ：非空顶点子图数为$\sum_{\varnothing\ne W\subseteq V}2^{e(G[W])}$；

  不能用只依赖$|W|$的$s(r)$代替各W，除非像完全图一样诱导边数由大小决定。$K_2$有4个、$K_3$有17个。

  诱导子图若允许空顶点集则恰$2^v$种，和任意子图计数不同。

- **【拓展】超立方体的面计数（counting faces of a hypercube）** ：$Q_3$有6个正方形面，每个面诱导一个$Q_2$，不是按画在纸上的“内外两个方框”只数出2个。

  一般$Q_n$的$k$维坐标面（coordinate face）有$\binom nk2^{n-k}$个：选$k$个自由变化坐标，其余坐标固定为0或1。

- **【拓展】补图（complement）** $\overline G$同点集，两个不同点原来不邻接时才连；$e(\overline G)=\binom v2-e(G)$，$\deg_{\overline G}(x)=v-1-\deg_G(x)$；$G\cup\overline G=K_v$。

  $\overline{K_{m,n}}=K_m\cup K_n$，$\overline{C_4}=2K_2$，$\overline{C_5}\cong C_5$。

- **【拓展】自补图（self-complementary graph）** $G\cong\overline G$必须$e=v(v-1)/4$，所以$v\equiv0,1\pmod4$。这是对一个指定图的必要条件，不足以断言它自补；

  $P_4,C_5$为例，$C_4$不是。

#### 【拓展】度序列与实现（Degree Sequences and Realization）

- **【拓展】度序列（degree sequence）** 在本节按非增序列出各点度；图形序列（graphic sequence）可由某简单图实现。必要条件是非负整数、每项至多$v-1$、总和偶；

  这些不充分。简单图至少两个点时必有两点同度，因为0与$v-1$不能同时出现，实际至多v−1种度。

- **【拓展】Erdős–Gallai判据（Erdős–Gallai criterion）** ：非增非负整数$d_1,\ldots,d_n$可图，当且仅当和为偶且每个$1\le k\le n$满足$\sum_{i=1}^kd_i\le k(k-1)+\sum_{i=k+1}^n\min(d_i,k)$。

  Havel–Hakimi算法（Havel–Hakimi algorithm）：移去最大项d，将余下最大的d项各减1，重排；全0成功，负数或d超过余项数失败，不能先把d减1再拿它决定减几项。

  允许自环与重边的伪图中，非负整数度列只需和为偶；不能把简单图判据与之混用。

### 6.4 图的表示与同构（Graph Representations and Isomorphism）

#### 表示法与自环约定（Representations and Loop Conventions）

- **【拓展：课堂未展开表示法细节】邻接表（adjacency list）** 逐点列邻居，存储$O(v+e)$；

  邻接矩阵（adjacency matrix）A以$a_{ij}$记录$i\to j$的弧数／无向重边数，存储$O(v^2)$；

  关联矩阵（incidence matrix）以点为行、边为列，存储$O(ve)$。稀疏图常用邻接表，稠密图矩阵便于常数时间查边；多重边须保留其身份或重数。

- 本教材无向伪图的邻接矩阵自环在对角只计1；图论度数自环计2，所以有自环时度为行和再加自环数，不等于行和。简单无向图A对称、主对角线0、行和为度；有向图行和为出度、列和为入度。

  无向普通关联矩阵的普通边列有两个1，0／1约定的自环列只有一个1，须先声明自环约定。

#### 同构的定义、排除与证明（Defining, Refuting and Proving Isomorphism）

- **图同构（graph isomorphism）** 为顶点双射$f:V_G\to V_H$，同时保留邻接与非邻接，简单图写$uv\in E_G\iff f(u)f(v)\in E_H$；有向图还须保持方向，多重图保持重数和自环。

  图相等（equality of graphs）要求标签相同，同构允许改名。同构本身是等价关系。

- **同构不变量（isomorphism invariant）** ：点边数、度序列、入出度、分量、圈长度与数量、三角形数、邻点度分布、割点、二分性、距离等。不变量不同可否定，同则不够肯定；

  $C_6$与$C_3\cup C_3$同为6点6边2正则却不同构，是骗过度序列检验的“魔鬼对（devil's pair）”。

- **证明同构须给完整双射并核对边与非边，或给置换矩阵（permutation matrix）** P使$A_H=PA_GP^T$；重排行、列须使用同一顶点置换，不能独立乱换。补图与反向图保持同构。

  验证给定双射只需多项式比较，暴力找映射可达$v!$个候选；

  原笔记介绍图同构的准多项式算法（quasipolynomial-time algorithm），不把“没有简单充分判据”误说成绝无充要定义。

![[C10.3-同构即重排行列.png|620]]

#### 【拓展】反向图、带宽与计数（Converse, Bandwidth and Counting）

- **【拓展】反向图（converse / reverse digraph）** 所有弧反向，对应$A^T$；反两次回原图，等于自身反向图当且仅当邻接关系对称。

  二分图按两侧重排后$A=\begin{bmatrix}0&B\\B^T&0\end{bmatrix}$；无向图按连通分量重排得分块对角矩阵（block diagonal matrix）。

- **【拓展】带宽（bandwidth）** 在所有顶点编号中最小化$\max\{|i-j|:v_iv_j\in E\}$；量化非零元距主对角线最远偏移。原例$B(K_5)=4,B(K_{1,3})=2,B(K_{2,3})=3,B(K_{3,3})=4,B(Q_3)=4,B(C_5)=2$；

  $C_5$不能按自然环序排后直接说最大偏移2，可按环顶点编号顺序$1,2,5,3,4$实现。Cuthill–McKee重排序（Cuthill–McKee ordering）与缩小矩阵带宽有关。

- **【拓展】非同构简单图计数（counting nonisomorphic simple graphs）** ：2点2类、3点4类、4点11类；5点3边4类、6点4边9类。

  不同于有标签图（labeled graph）的$2^{\binom n2}$种计数，不能任意除$n!$，因为各图自同构（automorphism）数量不同。

### 6.5 路径、连通性、树与网络可靠性（Paths, Connectivity, Trees and Reliability）

> [!warning] 【考试注意：术语约定】
> 本教材路径（path）允许重复点和边，相当于通行的走法（walk）；简单路径（simple path）强调不重复边，相当于迹（trail）。
>
> 下文讨论树、距离、哈密顿等需要不重复顶点时会明确写出，不能只凭中文“简单”猜定义。

#### 路径与连通性的语言（Language of Paths and Connectivity）

- **长度（length）** 是边数；回路（circuit）起终点相同且正长度；零长度路径只停在一个点，不算回路。圈（cycle）在本提纲指闭合且除首尾外顶点不重复的走法；

  无向图沿一条边往返虽是闭走（closed walk），不因此视为树中有圈。

- **无向连通（connected）** 为任意两点间有路径；有路径就能删去重复顶点段，得到不重复顶点的路径。连通分量（connected component）是极大连通子图，“极大”按包含而非点数最多。

  有向强连通（strongly connected）要求每对双向可达，弱连通（weakly connected）只要求底层无向图连通；

  强连通分量（strongly connected component, SCC）按互达划分。

  【拓展】Kosaraju算法（Kosaraju's algorithm）先在原图做DFS记录完成次序，再按完成次序逆序在反向图做DFS；每次搜出的未访问集合为一个SCC。Tarjan算法（Tarjan's algorithm）利用DFS栈与低链接值（low-link value）一遍求SCC。两者的时间复杂度均为$O(v+e)$；这里只保留原笔记列出的思路与复杂度。

- **无环（acyclic）** 在有向图中指无有向圈，DAG可拓扑排序；去方向后可能仍有无向圈，反之不可混说。SCC缩点（condensation）得到DAG。

#### 极小性、树与生成树（Minimality, Trees and Spanning Trees）

- **极小／极大（minimal / maximal）** 总是相对于具体性质：极小连通图（minimally connected graph）删任一边就不连通，是树；

  极大无圈图（maximal acyclic graph）若仍可加边连不同分量则不极大，固定非空点集时极大无圈即树。极大不等于最大（maximum），定义性质不能省略。

- **树（tree）** 为连通、无圈的简单无向图；森林（forest）为无圈图，可有多个分量。n点树有$n-1$边，任意两点间唯一不重复顶点路径；每边是桥；n≥2时至少两个叶。

  n点k分量森林有$n-k$边。对有限无向简单图，“连通且n−1边”“无圈且n−1边”“两点间唯一路径”均刻画树。

- **生成树（spanning tree）** 保留原图全部顶点、选边形成树；连通当且仅当有生成树，通常不唯一；非连通图只能取生成森林（spanning forest）。

  任意生成树不等于最小生成树（minimum spanning tree, MST），后者还优化边权和。

![[C10-树与两个反例.png|600]]

#### 【拓展】故障与连通度（Failures and Connectivity）

- **【拓展】割点（cut vertex / articulation point）** 删去该点及关联边使分量数增加；割边／桥（cut edge / bridge）删边使分量数增加。

  无向图边是桥当且仅当不在任何圈上；连通图有叶边则是桥，叶本身通常不是割点。判割点要看删后的分量数，不把“剩下少一个点”当不连通。

- **【拓展】不可分图（nonseparable graph）** 按原笔记定义为没有割点的连通图；至少3个顶点时，它等价于双连通图／2连通图（biconnected / 2-connected graph）。$K_2$没有割点，但不满足“至少3个顶点”的2连通约定。

  块（block）是极大不可分子图；常用分块约定也把单条桥及孤立点分别视为块。不同块至多共享一个顶点，共享点是割点。使用“块”的定义时须说明桥与孤立点的约定。

- **【拓展】点割（vertex cut）与边割（edge cut）** 分别是一组删除后使图不连通的点／边；

  点连通度（vertex connectivity）$\kappa(G)$、边连通度（edge connectivity）$\lambda(G)$为最少删除数。简单完全图约定$\kappa(K_n)=n-1$；

  不连通图取0，单点边界单列。对简单图有$\kappa\le\lambda\le\delta$；最大可能连通度不超过$n-1$，这类n上界不可套到有重边图。

- **【拓展】k连通（k-connected）** 通常要求顶点数大于k且$\kappa\ge k$，删少于k点仍连通；能容忍k−1个任意点故障，不是k个。

  最优连通（optimally connected）在原笔记采用$\kappa=\lambda=\delta$。

| 网络（network） | $\kappa,\lambda$ | 直径 |
|---|---|---|
| $P_n$，$n\ge2$ | $1,1$ | $n-1$ |
| $K_n$，$n\ge2$ | $n-1,n-1$ | 1 |
| $K_{m,n}$，$m,n\ge1$ | $\min(m,n),\min(m,n)$ | 两侧都非空时至多2；$K_{1,1}$为1 |
| $P_m\square P_n$，$m,n\ge2$ | $2,2$ | $m+n-2$ |
| $Q_n$，$n\ge1$ | $n,n$ | n |

#### 【拓展】距离与路径冗余（Distances and Path Redundancy）

- **【拓展】距离（distance）** $d(u,v)$为最短路径边数；离心率（eccentricity）$e(v)=\max_ud(u,v)$；

  直径（diameter）$\max_ve(v)$，半径（radius）$\min_ve(v)$，中心（center）为达到半径的顶点。有限连通图满足$\operatorname{rad}\le\operatorname{diam}\le2\operatorname{rad}$；

  不连通时要约定无穷距离或逐分量讨论。

- **【拓展】Menger定理（Menger's theorem）** ：不相邻u、v之间内部点不交路径（internally vertex-disjoint paths）最大数等于分离u、v的最小点割；

  不同u、v之间边不交路径（edge-disjoint paths）最大数等于最小边割。路径冗余对应故障容忍；完整图的全局点连通度用既定约定处理，不能对空的非邻点对集合直接取最小。

- **【拓展】Robbins定理（Robbins' theorem）** ：连通无向图可作强连通定向（strong orientation）当且仅当无桥。

  顶点基（vertex basis）是最小可达种子集：每个非种子顶点可由某种子到达；SCC缩点DAG的每个入度0分量各选一个点即可，孤立分量也要覆盖。

#### 边数、矩阵幂与走法（Edge Bounds, Matrix Powers and Walks）

- **【拓展／补充】边数与分量（edge bounds and components）** ：n点连通图至少n−1边；有k分量的简单图，$e\le\sum_i\binom{n_i}2\le\binom{n-k+1}2$；若$e>\binom{n-1}2$则必连通。

  反向“e≥n−1就连通”错误；点数集中在一个大分量加孤立点可使不连通图仍有很多边。

- **普通邻接矩阵幂（ordinary adjacency matrix powers）** $(A^r)_{ij}$数从i到j恰长r的走法，允许重复，不是简单路径条数；归纳把最后一条边按中间点分解即证。

  简单图$(A^2)_{ii}=\deg v_i$，$(A^2)_{ij}$（i≠j）数共同邻点；多重图的对角平方条目不能直接当度。二分图偶步只到同侧、奇步只到异侧。

- 核对原练习：$K_4$不同两点间长2、3、4、5走法为2、7、20、61；$K_{3,3}$异侧为0、9、0、81，同侧不同点为3、0、27、0。若只问是否可达，换布尔运算；

  不能用普通A幂中的数值直接当关系矩阵。

#### 【拓展】状态图与应用（State Graphs and Applications）

- **【拓展】Alcuin过河问题（Alcuin river-crossing puzzle）** 以两岸人员与物品分布为状态顶点，一次合法摆渡为边；狼羊菜题16种分布中10种安全，最短7次。

  广度优先搜索（breadth-first search, BFS）找最少边路径，深度优先搜索（depth-first search, DFS）可做可达性遍历。

  六度分隔（six degrees of separation）是原笔记用来说明社交网络短联系链的背景；演员共同出演图也称好莱坞图（Hollywood graph）。它不表示每张图的直径都至多6，也不替代对给定图的路径或闭包计算。

  图神经网络（graph neural network, GNN）的邻接聚合（neighborhood aggregation）与矩阵乘法有关，但带非线性的多层网络不能一般直接等同于$A^LXW$。

### 6.6 欧拉与哈密顿（Euler and Hamilton）

| 概念（concept） | 恰好一次的对象 | 首尾 |
|---|---|---|
| 欧拉路径／欧拉迹（Euler path / Euler trail） | 每条边 | 开放版本起终点不同 |
| 欧拉回路（Euler circuit / Euler tour） | 每条边 | 相同 |
| 哈密顿路径（Hamilton path / Hamiltonian path） | 每个顶点 | 一般不同 |
| 哈密顿回路（Hamilton circuit / Hamiltonian cycle） | 每个顶点，终点复写起点仅表示闭合 | 相同 |

#### 欧拉与哈密顿的区别（Euler versus Hamilton）

- 欧拉可重复经过顶点，不能重复边；哈密顿关注顶点，不能把覆盖全部边当作要求。柯尼斯堡七桥问题（Königsberg bridge problem）建成4点7边多重图，四个奇度点，因此不能一笔走完全部桥。

  欧拉图（Eulerian graph）是具有欧拉回路的图；通常在连通图语境下使用，含孤立点时先说明是否忽略这些点。哈密顿图（Hamiltonian graph）是具有哈密顿回路的图，有哈密顿路径还不足以称为哈密顿图。

  【拓展／背景】哈密顿的Icosian游戏（Icosian puzzle）要求沿十二面体（dodecahedron）图访问全部20个顶点后回到起点。原笔记称“二十面体游戏”，应避免误记为20个面；正十二面体有20个顶点，正二十面体（icosahedron）只有12个顶点。

#### 欧拉判据及证明（Euler Criteria and Proof）

- 无向图有边时，先检查非孤立部分连通；有欧拉回路当且仅当所有度偶，有开放欧拉路径当且仅当恰两个奇度点，起终点必须是这两点。若题目把欧拉回路也算路径，则“有欧拉路径”的条件应写奇度点数0或2。

  空边图的零长度情形另按题目约定。

- **必要性（necessity）** 靠每个中途顶点的进出配对；充分性（sufficiency）先走一个闭回路，若还有未用边，找已有回路上仍接未用边的点另走子回路并拼接，直到用完所有边。

#### 【拓展】求欧拉路线的算法（Algorithms for Euler Routes）

- **【拓展／算法】Hierholzer算法（Hierholzer's algorithm）** ：从合法起点出发沿未用边走；无路时退栈并记输出；仍有未用边时继续压栈，最终逆序得欧拉路线。

  实现中每边访问常数次为$O(e)$。开放路径从奇度点起，或临时连两奇点求回路再拆新边。

- **【拓展／算法】Fleury算法（Fleury's algorithm）** ：在剩余图中优先走非桥，只有别无可选时才走桥；走一边就删去，桥的身份会变化。

  每步重新判桥的直接实现通常$O(e^2)$量级，不与Hierholzer的线性实现混淆。

![[C10-Fleury为什么不能先走桥.png|620]]

#### 【拓展】有向欧拉与分笔覆盖（Directed Euler Routes and Trail Covers）

- **【拓展】有向欧拉条件（directed Euler conditions）** ：非零度顶点的底层无向图连通；回路要求每点入度等于出度；

  开放路径要求唯一s满足出度比入度多1、唯一t满足入度比出度多1，其余平衡，从s到t。不能仅看度而忽略所有边是否属于同一可遍历部分。

- **【拓展】最少分几笔（minimum number of trails）** ：一个有边的连通图若有$2k$个奇度点，最少$\max(1,k)$条不重边的迹覆盖全部边，抬笔次数为迹数减1；

  不连通图对各有边分量求和。七桥可分成两迹且不必重画桥；原笔记“必然有桥重画”不成立。加边是否修好欧拉性质要重新数奇度点，而非只看总边数。

- 应用：道路巡检、邮递员问题（Chinese postman problem）目标覆盖边，需重复时与单纯欧拉问题有别；

  DNA片段组装（DNA fragment assembly）可把片段邻接编码为欧拉路线。测试设备覆盖点则对应哈密顿，任务对象必须先辨清。

#### 哈密顿的排除与充分条件（Hamiltonian Tests and Sufficient Conditions）

- **哈密顿回路的排除条件（necessary-condition tests）** ：n≥3时每点度至少2、无割点；二分图两侧必须等大；

  度2点的两条边被强制纳入，若迫使某点用三条边或提前封成不含全部点的小圈，则不可能。哈密顿路径在二分图两侧大小差至多1，不能照搬回路的等大条件。

> [!info] 【历年考过：第21节转写L681附近】
> 老师明确说两年前期末用过哈密顿路径题。画出一条合法路线即可证存在；未找到路线不算证明不存在，要给排除理由或穷举论证。

- **Dirac定理（Dirac's theorem）** ：n≥3的简单图若$\delta\ge n/2$，则有哈密顿回路；Ore定理（Ore's theorem）：每对不相邻u、v都有$\deg u+\deg v\ge n$，则有哈密顿回路。

  Dirac条件蕴涵Ore条件；二者均充分非必要，$C_5$两者都不满足却本身有哈密顿回路。n奇时度的整数门槛是$\lceil n/2\rceil$。

#### 【拓展】闭包证明与结构条件（Closure Proof and Structural Conditions）

- **【拓展】Bondy–Chvátal闭包引理（Bondy–Chvátal closure lemma）** ：不邻接u、v的度和至少n时，加边uv不改变哈密顿回路是否存在。

  反向证明：若新回路用uv，删它得原图哈密顿路径$x_1=u,\ldots,x_n=v$；在位置$i\in\{1,\ldots,n-1\}$中，令$A=\{i:ux_{i+1}\in E\},B=\{i:x_iv\in E\}$。

  $|A|+|B|\ge n>n-1$，必有公共i，可拼成$x_1\cdots x_i x_n x_{n-1}\cdots x_{i+1}x_1$。反复加满足条件的边到完全图即可证Ore；原笔记该证明的位置集合下标漏算，已在此纠正。

- **【拓展】必要结构条件（necessary structural condition）** ：有哈密顿回路则任意非空S删去后分量数不超过$|S|$；有哈密顿路径则不超过$|S|+1$。

  这些条件一般不充分。哈密顿判定为NP完全问题，不是没有定义上的充要条件，而是没有本课欧拉式简单度数充要判据。

![[C10.5-欧拉与哈密顿的区别.png|620]]

| 标准图族 | 欧拉回路 | 开放欧拉路径 | 哈密顿回路 |
|---|---|---|---|
| $K_n$，$n\ge2$ | n奇 | 仅n=2 | n≥3 |
| $C_n$，n≥3 | 有 | 无 | 有 |
| $W_n$，n≥3 | 无 | 无 | 有，须把中心插入轮缘相邻两点之间 |
| $Q_n$，n≥1 | n偶 | 仅n=1 | n≥2 |
| $K_{m,n}$，m,n≥1 | m、n均偶 | $K_{1,1}$，或一侧为2另一侧奇 | m=n≥2 |

#### 【拓展】Gray码、骑士与Petersen（Gray Codes, Knight’s Tours and Petersen Graph）

- **【拓展】Gray码／格雷码（Gray code）** 为相邻二进制码只差一位的序列，循环Gray码对应$Q_n$的哈密顿回路（n≥2）。

  反射构造（reflected binary code）先在旧码前加0，再把旧码倒序前加1拼接；例如$00,01,11,10$。

  旋转编码（rotating encoding）使传感器相邻位置变化一位，减少读数歧义。

- **【拓展】骑士周游（knight's tour）** 将棋盘格作点、马步$(\pm1,\pm2),(\pm2,\pm1)$作边，遍历各格为哈密顿路径，可复返周游（reentrant / closed tour）为回路。

  马步总换黑白色，奇数格棋盘无闭周游；$3\times3$中心孤立，$4\times4$也无周游。

  Warnsdorff启发式（Warnsdorff's heuristic）每步优先后续可走位置少者，是构造策略，不是任意棋盘必成功的证明。

- **【拓展】Petersen图（Petersen graph）** 10点15边3正则，无哈密顿回路，但删任一顶点后有；这是次哈密顿图（hypohamiltonian graph）的例子。

  旅行商问题（traveling salesperson problem, TSP）是在带权哈密顿回路中再求最小总权，详见下一节。

### 6.7 【拓展：§10.6整节课堂未讲】最短路径与旅行商（Shortest Paths and the Traveling Salesperson Problem）

#### 代价与松弛（Costs and Relaxation）

- **带权路径长度（weighted path length）** 为沿途边权和，不是边数；最短路径（shortest path）优化两端点之间的长度。

  最少边数（fewest edges）可把所有边权设1，用BFS；最短时间、最短里程、最低费用使用不同权重，答案可能不同。

  原教材航线例里程最优2109英里，而费用最优197美元，对应路线不同，不能混用指标。

- **松弛（relaxation）** ：若$d(u)+w(u,v)<d(v)$，改$d(v)\leftarrow d(u)+w(u,v)$并记录前驱（predecessor）$\operatorname{prev}(v)=u$。

  标签（label）从上界向下改，不能把更大候选覆盖当前较小值。

  三条性质分别是单调性（monotonicity）：标签只减不增；上界性（upper-bound property）：有限标签对应实际走法，故不小于真实最短距离；局部性（locality）：更新只需$d(u)$与边权，不需先知道完整路径。

  初值$+\infty$表示尚未发现路径，并不是某条有限路线的长度。仅凭“严格变小”不能推出更新次数必有限：可达负权回路（reachable negative-weight cycle）会使标签不断下降，算法的终止与正确性还依赖各自的前提。

#### Dijkstra：条件、过程与例子（Conditions, Procedure and Examples）

- **Dijkstra算法（Dijkstra's algorithm）** 解非负权（nonnegative weights）单源最短路（single-source shortest paths）：初始化$d(s)=0$、其余$\infty$；

  反复从未确定点取最小标签者u，确定其最短距离，松弛全部出边。需要源点到所有顶点的结果时，跑完所有可达点；若只问目标t，t被取出确定时可停。尚未确定的点不能标成“已确定”。

  【拓展／应用】开放式最短路径优先协议（Open Shortest Path First, OSPF）中的最短路径优先（shortest path first, SPF）是原笔记提到的路由应用背景；对应计算的是网络中从本路由器出发的路径代价。

- **正确性（correctness）** 靠贪心不变量（greedy invariant）：已确定点距离真实最短，任何通往未确定点的路径第一次跨出已定集合时，其候选已被松弛；

  非负边保证后续路段不能再把更小的隐藏答案带回来。单条负权边（negative edge）已能使“确定后不再改”失败，例如$s\to u=2,s\to v=5,v\to u=-4$。

| 原教材例2：确定点 | a | c | b | d | e | z |
|---|---|---|---|---|---|---|
| 对应最终距离 | 0 | 2 | 3 | 8 | 10 | 13 |
| 关键变化 | b先4，c为2 | b改3，d先10，e先12 | d改8 | e改10，z先14 | z改13 | 完成 |

- **路线恢复（path reconstruction）** 从z沿prev反向回溯：$a\to c\to b\to d\to e\to z$，$2+1+5+2+3=13$。原例1则为$a\to d\to e\to z$，距离$2+3+1=6$；

  其中$a\to d\to e$应为5，不能抄原印的7。

- Dijkstra朴素数组／矩阵实现$O(v^2)$，邻接表＋二叉堆（binary heap）实现$O((v+e)\log v)$；算法与实现复杂度要一起说。

  负权可考虑Bellman–Ford算法（Bellman–Ford algorithm），时间$O(ve)$；若存在可达负回路（negative cycle），相关目标的最短走法长度可能无有限下界。

![[C10.6-原图-Dijkstra逐步标签.png|650]]

#### Floyd：分层递推与路径恢复（Layered Recurrence and Reconstruction）

- **Floyd／Floyd–Warshall算法（Floyd / Floyd–Warshall algorithm）** 解全对最短路（all-pairs shortest paths）。

  初值$D^{(0)}_{ii}=0$，有边取最小边权，无边$\infty$；第k轮

$$
D_{ij}^{(k)}=\min\bigl(D_{ij}^{(k-1)},D_{ik}^{(k-1)}+D_{kj}^{(k-1)}\bigr).
$$

- 含义为仅允许前k个顶点作中转；k必须最外层。可有负边，但要解释负回路：结束后若某$D_{ii}<0$则检测出负回路，其可到达与可返回关联的点对没有有限最短走法。时间$O(v^3)$，空间$O(v^2)$；

  next表（next-hop table）或中间点表能恢复路线，不能说Floyd本身“无法构造路径”。松弛成功时可更新$\operatorname{next}[i,j]=\operatorname{next}[i,k]$。

- 原例2的a行最终按$a,b,c,d,e,z$为$(0,3,2,8,10,13)$，与Dijkstra一致。Warshall与Floyd的同一分层结构分别使用OR／AND与min／加法，前者求是否可达、后者求最小代价。

#### DAG与A星（DAG and A-star）

- **DAG上按拓扑序松弛所有边，最短路、最长路（longest path）** 均可$O(v+e)$，最长路取max、不可达初值$-\infty$。

  一般图最长简单路径（longest simple path）困难，不能允许重复正圈后仍声称有有限最长长度。

- **A星搜索（A* search）** 按$f(v)=g(v)+h(v)$选点，h为启发函数（heuristic function），$h\equiv0$退化Dijkstra。

  可采纳性（admissibility）要求不高估剩余最短距离；若确定后不重开顶点，通常还需一致性（consistency）$h(u)\le w(u,v)+h(v)$。

  仅可采纳但不一致时，要允许更好g值重开（reopening），不能无条件照Dijkstra永久定点。

#### 旅行商、启发式与近似（TSP, Heuristics and Approximation）

- TSP要求每城市恰一次并回起点，找最小权哈密顿回路；不是最短路，也不是最小生成树。无向完全图固定起点、正反视同、n≥3时有$(n-1)!/2$条候选；有向图一般不能再除2。

  五城原例共12条候选，最优Detroit–Toledo–Kalamazoo–Grand Rapids–Saginaw–Detroit，$58+133+56+113+98=458$。

- **精确优化（exact optimization）** 、启发式（heuristic）与有保证近似（approximation algorithm）要区分。

  最近邻法（nearest-neighbor heuristic）每次去最近未访问城市，直接实现$O(v^2)$，但不保证全局最优或常数近似比。

  2-opt／3-opt局部搜索（local search）换局部边可改进，但局部最优不等于全局最优。

- **近似比（approximation ratio）** c对最小化问题表示$\mathrm{OPT}\le W_{alg}\le c\,\mathrm{OPT}$。

  对非负、无向、满足三角不等式的度量TSP（metric TSP），Christofides算法（Christofides' algorithm）保证3/2：最小生成树＋奇度点最小权完美匹配＋欧拉化＋捷径（shortcutting）；

  前两者分别不超过OPT和OPT/2，三角不等式保证跳过重复点不增长度。此保证不能直接用于任意权重TSP。

- **度量闭包（metric closure）** 把每对顶点边权换成最短路距离，可将“每城至少一次”的闭走优化与闭包上的TSP联系，仍需做全局访问顺序优化；不能由Floyd距离矩阵直接宣称TSP已解。

  一般TSP的优化为NP难（NP-hard），相应有界长度判定为NP完全；工程启发式的某批实例表现不构成普遍误差保证。

### 6.8 平面图、欧拉公式与不可平面障碍（Planarity, Euler's Formula and Obstructions）

#### 可平面与平面嵌入（Planarity and Plane Embeddings）

- **可平面图／平面图（planar graph）** 指 **存在** 一种无边交叉的平面画法；平面嵌入图／平图（plane graph）指已经给定的无交叉画法。现在画得有交叉不能否定可平面，重画或同构重排可能消除交叉；

  边在共同端点相会不算交叉。$K_4,Q_3$可平面，$K_5,K_{3,3}$不可平面。

  在原本交叉的两条边之间加一个新顶点，会改变顶点与邻接关系，得到的是另一张图；不能这样把交叉“改成端点”来证明原图可平面。合法重画须保留原图的点边关联。

> [!info] 【历年考过：第22节转写L398附近】
> 老师在平面图与不交叉论证附近提到过去期末出过题，不能据此把本次具体题型写死。应会从定义分辨planar与plane、统计面并使用定理。

#### 面、欧拉公式与边数界（Faces, Euler’s Formula and Edge Bounds）

- **面／区域（face / region）** 由嵌入划开，外部无界面（unbounded / exterior face）也算一个；

  边界（boundary）围住面，面度（degree of a face）按边界边出现次数计，不按不同边集合大小。桥在同一面边界走两次，自环可围成面。

- **欧拉公式（Euler's formula）** ：连通平面图$v-e+f=2$；c个连通分量推广为$v-e+f=1+c$。树只围一个面，代入$e=v-1$一致；从树逐条加闭圈边，每次e和f各加1；

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
| $K_n$可平面 | 当且仅当$n\le4$ |
| $K_{m,n}$可平面 | m,n非负时当且仅当$\min(m,n)\le2$；一侧空也自然可平面 |
| $Q_n$可平面 | 当且仅当$n\le3$，包含n=0的单点约定 |

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

#### 着色定义与最优性（Coloring and Optimality）

- **合法顶点着色（proper vertex coloring）** 为每点赋色且邻点异色；k着色（k-coloring）表示至多用k种颜色。

  色数／顶点色数（chromatic number）$\chi(G)$是最少用色数。非空无边图色数1；空顶点图常约定0。有自环时不能合法顶点着色，通常讨论简单图；重边不增加新的不同色约束。

- 求精确色数必须双向证明：给一个k着色证$\chi\le k$，再证明k−1色不够以证$\chi\ge k$。加边不会降低色数，删边不会提高；不同连通分量可复用颜色，整体色数取最大，不是相加。

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

- **四色定理（four-color theorem）** ：每个可平面图可用至多4色，$\chi\le4$，不是恰4。$K_4$说明上界可达到；图能4着色不意味着可平面，如$K_{3,3}$甚至可2着色。

  含奇圈排除2色；不含$K_4$并不能排除色数4。

![[C10.8-地图到冲突图到着色.png|620]]

#### 资源分配模型（Resource Allocation Models）

- **排考（exam scheduling）** ：点=课程，边=有共同学生，色=时段。原7门课例中的$\{1,2,3,4\}$形成$K_4$给下界4，时段$\{1,6\},\{2\},\{3,5\},\{4,7\}$给上界4，故最少4。

  原12门课例有$K_5$，可排$\{1,6,12\},\{2,7,10\},\{3,8,11\},\{4,9\},\{5\}$五时段，故最少5。课号对应原笔记；不能把一个可行的六时段表当作最小值6。

- 同模型应用：登机口分配（gate assignment）点=航班、边=占用时段交叠、色=登机口，原6航班例需3口；

  委员会排程（committee scheduling）边=共同成员，原$K_6$少一边的例子需5时段；

  频率／频道分配（frequency / channel assignment）点=发射台、边=干扰；

  寄存器分配（register allocation）点=变量、边=生存期同时活跃（overlapping live ranges），色=寄存器。同一颜色代表可共享资源，不是边的数量。

![[C10.8-原图-考试排程的着色与时段表.png|620]]

#### 【拓展】团、独立集与色数界（Cliques, Independent Sets and Bounds）

- **【拓展】团（clique）** 为两两相邻顶点集，团数（clique number）$\omega(G)$为最大团大小；

  独立集（independent set）为两两不相邻顶点集，独立数（independence number）$\alpha(G)$为最大独立集大小。

  各颜色类（color class）是独立集，但用到的非空颜色类才构成严格意义的划分，不能在“划分”中允许空块。

$$
\max\left\{\omega(G),\left\lceil\frac{v}{\alpha(G)}\right\rceil\right\}
\le\chi(G)\le\min\{\Delta(G)+1,\ v-\alpha(G)+1\}
\quad(v>0).
$$

- **【拓展】界的证明（proofs of bounds）** ：团每点不同色；每色类最多$\alpha$点得$v\le\alpha\chi$；最大独立集共用一色、其余点各一色得$v-\alpha+1$上界。

  团下界不总紧，$C_5$有$\omega=2$、$\chi=3$；原7点图H有$\alpha=2$故需至少4色，即便其最大团只有3。

#### 【拓展】贪心与Brooks（Greedy Coloring and Brooks）

- **【拓展】贪心着色（greedy coloring）** 按指定顺序为每点选已染邻点未用的最小编号色，最多$\Delta+1$色；依赖顺序，不保证最优。

  按度非增也可能多用色：$P_6$顺序$p_2,p_3,p_5,p_4,p_1,p_6$会用3色，而$\chi=2$。

- **【拓展】Brooks定理（Brooks' theorem）** ：连通简单图若不是完全图且不是奇圈，则$\chi\le\Delta$（单点等退化情形单列）；完全图与奇圈达到$\Delta+1$。

  不能省连通条件后把“某个分量是例外”忽略。3着色判定（3-colorability decision）为NP完全，暴力构造仍可判定，不把“难算”误写成没有任何判据。

#### 【拓展】边着色与多重名额（Edge and k-tuple Coloring）

- **【拓展】边着色（edge coloring）** 使共端点的边异色，边色数（edge chromatic number）$\chi'(G)$与顶点色数不同。

  Vizing定理（Vizing's theorem）对简单图给$\Delta\le\chi'\le\Delta+1$；不能直接套有自环或任意多重图。偶圈边色数2、奇圈3；

  $K_n$在n偶时n−1、n奇时n（n≥2），对应循环赛最少轮数。原例G、H最大度都4，边色数分别4、5。

- **【拓展】k重着色（k-tuple coloring）** 每点分配k个不同颜色，相邻点的颜色集合不交，最小总色数为$\chi_k(G)$。$\chi_k(K_n)=kn$；有边二分图$\chi_k=2k$，无边非空图仅k；

  $\chi_2(C_4)=4,\chi_2(W_4)=6,\chi_2(C_5)=5,\chi_3(C_5)=8$，说明一般$\chi_k\ne k\chi$。

#### 【拓展】支配与画廊（Domination and Art Galleries）

- **【拓展】支配集（dominating set）** D要求每个D外顶点至少有一个D内邻点，最小大小为支配数（domination number）$\gamma(G)$；不同于独立集。

  极大独立集（maximal independent set）必支配，但未必是最大独立集（maximum independent set）或最小支配集。

- **【拓展】画廊问题（art gallery problem）** ：无洞简单n边形（simple polygon without holes）可用至多$\lfloor n/3\rfloor$个顶点守卫（vertex guards），最坏情况下需要这么多；

  不是每个具体展厅都恰需该数。

  证明先三角剖分（triangulation）为n−2三角形，再把外平面剖分图（outerplanar triangulation）3着色，取人数最少的颜色类，每个三角形都有该色一个顶点。

  不能把有内部新增点的任意平面三角剖分都当成可3着色。

---

## 七、来源、考试证据与勘误（Sources, Examination Evidence and Corrections）

### 7.1 小节覆盖对照（Section Coverage Map）

下表逐篇列出来源及正文落点，用于定位，不能单独证明每个知识点都已覆盖。原笔记中的例题、自测和习题若只重复同一知识，合并为方法条目；本轮回查中发现的独立概念、反例、边界与新结论已补入正文，并在7.4逐项列出。表中编号是本提纲编号。

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

这里的勘误只写入新提纲，未改动原笔记。历史统计与未解问题背景按原笔记的历史语境保留，不把旧的计算验证界或规模数字冒充当前纪录；计算验证有限实例也不替代一般证明。

### 7.4 本轮缺口复核与补入记录（Gap Audit and Additions）

本轮回查对象为7.1列出的35篇小节讲义、6篇章节汇总及作业笔记，重点逐项比对定义、具名结论、算法、公式条件，以及例题、自测、习题与旁注带出的独立知识。下表记录查出的38组缺口及处理位置；其中“补入”指此前缺少这一知识，“补全”指此前已有部分内容，但名称、条件、推理或应用不全。

这份修订记录便于回查，不能把未列在修订表中的内容理解为不重要，也不能把修订记录冒充逐字逐题的教材替代品。合并的只是重复实例，不能据此自行缩小考试范围。

#### 逻辑与证明（Logic and Proofs）

| 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
|---|---|---|
| 实质蕴涵（material implication） | [[C1.1 命题逻辑 Propositional Logic\|C1.1]]条件语句 | 补全名称与非因果含义，1.1 |
| XOR消去、一次一密、CRC与RAID（XOR cancellation, one-time pad, CRC and RAID） | [[C1.1 命题逻辑 Propositional Logic\|C1.1]]异或与计算机联系 | 补入可逆公式、密钥条件及校验应用，1.1 |
| 布隆过滤器、BNN、XOR非线性可分（Bloom filter, BNN and XOR nonseparability） | [[C1.1 命题逻辑 Propositional Logic\|C1.1]]位并行与AI联系 | 补入应用与概念区别，1.1；模糊控制名称同步补全 |
| 第三类人谜题（puzzles with spies / normals） | [[C1.2 命题逻辑的应用 Applications of Propositional Logic\|C1.2]]骑士与无赖习题说明 | 补入三类人的不同约束，1.2 |
| 知识逻辑与共同知识（epistemic logic and common knowledge） | [[C1.2 命题逻辑的应用 Applications of Propositional Logic\|C1.2]]泥孩子旁注 | 补全名称、知道的层次及应用联系，1.2 |
| 否定范式（negation normal form, NNF） | [[C1.3 命题等价 Propositional Equivalences\|C1.3]]七步等价推导后的方法说明 | 补入定义、转化次序、例子及与DNF／CNF的区别，1.3 |
| 符号与神经符号AI（symbolic and neuro-symbolic AI） | [[C1.4 谓词与量词 Predicates and Quantifiers\|C1.4]]Prolog旁注 | 补入原笔记列举的应用联系，1.4 |
| 邻域独立与聚类系数（independent neighborhood and clustering coefficient） | [[C1.5 嵌套量词 Nested Quantifiers\|C1.5]]朋友关系例题旁注 | 补入量词公式、图论解释及度数边界，1.5 |
| 平均值论证与概率方法（averaging argument and probabilistic method） | [[C1.7 证明导论 Introduction to Proofs\|C1.7]]习题平均值结论后的联系 | 补全方法名称与存在性解释，1.7 |
| 构造主义及证明程序联系（constructivism and proofs as programs） | [[C1.8 证明方法与策略 Proof Methods and Strategy\|C1.8]]无理数幂例题旁注 | 补入Gelfond–Schneider、直觉主义、Curry–Howard与证明助手背景，1.8 |
| 卡塔兰猜想（Catalan's conjecture） | [[C1.8 证明方法与策略 Proof Methods and Strategy\|C1.8]]100以内连续完全幂例题 | 补入一般定理与有限穷举的区别，1.8 |
| 证明与数论背景术语（background terminology of proofs and number theory） | [[C1.8 证明方法与策略 Proof Methods and Strategy\|C1.8]]人物、费马与Collatz旁注 | 补全原笔记背景名称与不可判定性边界，1.8 |

#### 集合、序列与矩阵（Sets, Sequences and Matrices）

| 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
|---|---|---|
| 笛卡尔积相等与空积条件（equality and emptiness of Cartesian products） | [[C2.1 集合 Sets\|C2.1]]笛卡尔积习题 | 补全两个充要条件与非空情形证明方法，2.1 |
| 运算与包含、对称差消去（operations, inclusion and symmetric-difference cancellation） | [[C2.2 集合运算 Set Operations\|C2.2]]相关习题与自测7 | 补入结论、证明与并集不能消去的反例，2.2 |
| 集合后继（set successor） | [[C2.2 集合运算 Set Operations\|C2.2]]自测8、习题59–60 | 补入定义、三个例子、基数及自然数构造，2.2 |
| 比例增长加固定增量（affine recurrence） | [[C2.4 序列与求和 Sequences and Summations\|C2.4]]工资增长模型 | 补入递推、迭代闭式及$r=1$边界，2.4 |
| 正奇数求和（sum of positive odd integers） | [[C2.4 序列与求和 Sequences and Summations\|C2.4]]求和与几何解释 | 补入公式及逐层添方格证明，2.4 |
| $A+A^T$的对称性（symmetry of a matrix plus its transpose） | [[C2.6 矩阵 Matrices\|C2.6]]自测6、习题14 | 补入一般证明，2.6 |
| 数量矩阵与中心（scalar matrices and center） | [[C2.6 矩阵 Matrices\|C2.6]]自测7、补充习题38–39 | 补入正向证明及$2\times2$逆向构造，2.6 |
| 布尔幂最终周期性（eventual periodicity of Boolean powers） | [[C2.6 矩阵 Matrices\|C2.6]]自测8 | 补入有限性证明、交替反例与全1稳定条件，2.6 |

#### 关系（Relations）

| 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
|---|---|---|
| 一对多等对应情况（one-to-many and related correspondences） | [[C9.1 关系及其性质 Relations and Their Properties\|C9.1]]关系与函数的区别 | 补全名称，3.1 |
| 数据库外延与内涵（extension and intension） | [[C9.2 n 元关系与数据库 n-ary Relations and Their Applications\|C9.2]]键的时间条件 | 补入两者定义与选键依据，3.2 |
| 关系代数（relational algebra） | [[C9.2 n 元关系与数据库 n-ary Relations and Their Applications\|C9.2]]三个运算及SQL联系 | 原有运算，补全统称与输入输出含义，3.2 |
| 正负同余合并（congruence up to sign） | [[C9 关系 Relations MOC\|C9汇总]]自测11(b)、12(c) | 补入三性质证明及模7四个类，3.5 |
| 格的有限子集与有限格（finite subsets of lattices and finite lattices） | [[C9 关系 Relations MOC\|C9汇总]]自测19 | 补入归纳方法、有界结论及空子集条件，3.6 |

#### 计数与递推（Counting and Recurrences）

| 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
|---|---|---|
| 组合数学（combinatorics） | [[C6.1 计数基础 The Basics of Counting\|C6.1]]导言 | 补全统称与计数／构造联系，第四部分开头 |
| 分治与动态规划（divide and conquer and dynamic programming） | [[C8.1 递推关系的应用 Applications of Recurrence Relations\|C8.1]]动态规划比较 | 补全区别，并区分汉诺塔求步数与输出移动，5.5 |

#### 图论（Graph Theory）

| 核对项（audit item） | 原笔记位置（source） | 本轮处理与正文位置 |
|---|---|---|
| 有限图与无限图（finite and infinite graphs） | [[C10.1 图与图模型 Graphs and Graph Models\|C10.1]]Remark | 补入点集、边集两方面的条件，6.1 |
| 真子图（proper subgraph） | [[C10.2 图的术语与特殊类型 Graph Terminology and Special Types of Graphs\|C10.2]]定义7 | 补入与生成／诱导子图的区别，6.3 |
| 立方体的六个面（six square faces of a cube） | [[C10.2 图的术语与特殊类型 Graph Terminology and Special Types of Graphs\|C10.2]]$Q_3$子图例 | 补入六个$Q_2$及坐标面计数说明，6.3 |
| 强分量算法（SCC algorithms） | [[C10.4 连通性 Connectivity\|C10.4]]§5末尾 | 补入Kosaraju／Tarjan思路与复杂度，6.5 |
| 不可分图、双连通与块（nonseparable, biconnected graphs and blocks） | [[C10.4 连通性 Connectivity\|C10.4]]§3、§4 | 补入定义与小图约定，6.5 |
| 六度分隔与好莱坞图（six degrees of separation and Hollywood graph） | [[C9.4 关系的闭包 Closures of Relations\|C9.4]]应用；[[C10.4 连通性 Connectivity\|C10.4]]连通例 | 补全名称与不能泛化到任意图的边界，6.5 |
| 欧拉图与哈密顿图（Eulerian and Hamiltonian graphs） | [[C10.5 欧拉路径与哈密顿路径 Euler and Hamilton Paths\|C10.5]]术语定义 | 原有路线判据，补全图的名称与区别，6.6 |
| Icosian游戏（Icosian puzzle） | [[C10.5 欧拉路径与哈密顿路径 Euler and Hamilton Paths\|C10.5]]哈密顿背景 | 补入模型及原笔记已说明的20顶点／12面区别，6.6 |
| 松弛的三条性质（three properties of relaxation） | [[C10.6 最短路径问题 Shortest-Path Problems\|C10.6]]§3 | 补全上界性、局部性及终止性限制，6.7 |
| 交叉处加点改变原图（adding vertices at crossings changes the graph） | [[C10.7 平面图 Planar Graphs\|C10.7]]平面画法说明 | 补入操作限制，6.8 |
| OSPF与SPF（Open Shortest Path First and shortest path first） | [[C10.6 最短路径问题 Shortest-Path Problems\|C10.6]]开场及路由应用 | 补全应用名称，6.7 |
