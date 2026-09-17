---
title: "C1 基础：逻辑与证明 MOC"
course: 离散数学 Discrete Mathematics
chapter: "1 基础：逻辑与证明 The Foundations: Logic and Proofs"
tags:
  - 离散数学
  - MOC
  - 索引
  - 术语表
aliases:
  - C1 MOC
  - 第一章索引
  - The Foundations Logic and Proofs
source:
  - "Rosen, Discrete Mathematics and Its Applications, Chapter 1, pp.1–114"
  - "课件 Dr 欧士琪 SCUT 2026Fall: Ch1.1 Part1–3, Ch1.2"
lecturer: "Dr Shiqi (Shawn) Ou 欧士琪, South China University of Technology"
---

# C1 基础：逻辑与证明 MOC

> [!abstract] 本章总纲（课本章首语）
> **逻辑规则赋予数学陈述精确的含义。** 例如，这些规则帮助我们理解并推理诸如"存在一个不是两个平方数之和的整数"和"对每个正整数 $n$，不超过 $n$ 的正整数之和是 $n(n+1)/2$"这样的陈述。
> **逻辑是一切数学推理的基础，也是一切自动推理的基础。** 它在计算机器的设计、系统规约、人工智能、计算机编程、程序设计语言，以及计算机科学与许多其他研究领域中都有实际应用。
>
> **要理解数学，必须理解什么构成一个正确的数学论证，即证明。** 一旦证明了一个数学陈述为真，就称它为**定理**。关于某一主题的一组定理组织起我们关于该主题的知识。**要学好一个数学主题，必须主动构造关于该主题的数学论证，而不只是阅读讲解。** 而且，知道一个定理的证明往往使我们能够修改结果以适应新的情形。
>
> **人人都知道证明在数学中很重要，但许多人惊讶于证明在计算机科学中同样重要。** 事实上，证明被用来：验证计算机程序对所有可能的输入值都产生正确的输出、说明算法总是产生正确的结果、确立系统的安全性、以及创造人工智能。此外，人们已经创造出**自动推理系统**，让计算机能够构造自己的证明。
>
> **本章将解释什么构成一个正确的数学论证，并介绍构造这些论证的工具。** 我们会发展一套不同的证明方法的武器库，使我们能够证明许多不同类型的结果；在介绍完各种证明方法后，还会介绍若干构造证明的策略。我们将引入**猜想**的概念，并解释通过研究猜想来发展数学的过程。

---

## 章节导航

| 节 | 笔记 | 核心内容 | 必背要点 |
|---|---|---|---|
| 1.1 | [[C1.1 命题逻辑 Propositional Logic]] | 命题、五个联结词、真值表、条件语句的各种表述、逆/否/逆否、优先级、位运算 | $p\to q$ 只在"前真后假"时为假；"$p$ only if $q$" = $p \to q$；只有逆否等价 |
| 1.2 | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] | 英语翻译、系统规约与一致性、布尔检索、逻辑谜题、逻辑电路 | 一致 = 存在使全部为真的赋值；三种基本门；表达式 ↔ 电路 |
| 1.3 | [[C1.3 命题等价 Propositional Equivalences]] | 永真式/矛盾式/可能式、逻辑等价、Table 6/7/8、德摩根律、可满足性、数独编码 | $p\to q \equiv \neg p \vee q$；$\neg(p\to q) \equiv p \wedge \neg q$；德摩根律 |
| 1.4 | [[C1.4 谓词与量词 Predicates and Quantifiers]] | 谓词、命题函数、$\forall$/$\exists$/$\exists!$、论域、受限量词、约束变元、量词德摩根律、翻译、Prolog | **$\forall$ 配 $\to$，$\exists$ 配 $\wedge$**；$\neg\forall \equiv \exists\neg$，$\neg\exists \equiv \forall\neg$ |
| 1.5 | [[C1.5 嵌套量词 Nested Quantifiers]] | 嵌套量词、**量词顺序**、Table 1、数学陈述翻译、极限定义、嵌套量词的否定 | **$\forall x\exists y \ne \exists y\forall x$**；$\exists\forall \Rightarrow \forall\exists$（单向） |
| 1.6 | [[C1.6 推理规则 Rules of Inference]] | 有效论证、Table 1（8 条）、归结、谬误、Table 2（UI/UG/EI/EG）、全称肯定前件式 | 有效 ≠ 可靠；肯定后件/否定前件是谬误；EI 先于 UI |
| 1.7 | [[C1.7 证明导论 Introduction to Proofs]] | 术语、直接证明、逆否证明、空/平凡证明、反证法、$\sqrt2$ 无理、等价性证明、反例、证明中的错误 | 逆否 $\equiv$ 原命题；反证法证 $p\to q$ 是假设 $p \wedge \neg q$；循环论证 |
| 1.8 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] | 穷举/分情况证明、WLOG、存在性证明（构造性/非构造性）、唯一性证明、正向/逆向推理、棋盘铺砌与染色论证、开放问题 | 情形必须完备；染色的颜色数 = 拼块覆盖格数；逆向推理找 $p \to q$ |

---

---

## 🎓 课程信息与考试情报（来自课堂录音转写稿 `transcript/1-8节课.txt`）

> [!info] 这一节的内容全部来自课堂口头announcement，课件和教材上都没有。**备考前先看这一节。**

### 📌 基本信息

| 项 | 内容 |
|---|---|
| **任课教师** | **Dr Shiqi (Shawn) Ou 欧士琪**，华南理工大学 未来技术学院 |
| **办公室** | **B1-C513**（**需先发邮件预约**，老师明确表示不接受随机敲门） |
| **助教 TA** | **余子龙**（老师的博士生）。Office hour 每周四，通过**腾讯会议**线上进行，链接与时间在 QQ 群公布 |
| **沟通渠道** | **QQ 群**——课件 PPT、作业、syllabus、成绩提醒、考场安排全部在群里发布 |
| **学分/学时** | **3 学分，48 学时**（其中 2 学时用于期中考试） |
| **上课安排** | 每周 **3 次**：周二、周三（下午）、周四，共约 8 周（9 月—10 月底） |
| **教室** | **F3-B409** |
| **教材** | Rosen《Discrete Mathematics and Its Applications》。**纸质版 $100+，但 QQ 群里有电子版，不必购买** |

> [!warning] ⚠️ 调课（第 3 周通知）
> 因国庆假期，**9 月 20 日（周日）补课**，**按周二的课表**，上午 **8:50** 开始。
> 那一周共四次课：**周二、周三、周四、周日**。

### 📊 成绩构成

| 项目 | 占比 | 说明 |
|---|:-:|---|
| **出勤与参与 Attendance & Participation** | **2%** | 老师会随机点名提问，**回答一次即可拿满**，**答对答错都算分**。不回答就拿不到。老师说"学院要求必须有考勤分" |
| **作业 Homework** | **4 次 × 2% = 8%** | 见下方作业规范 |
| **期中考试 Midterm** | 大头 | **只考第一章**，闭卷 |
| **期末考试 Final** | 大头 | 闭卷 |

> [!note] 历年给分情况（老师自述）
> 平均分接近 90，**中位数超过 90**；第一学期有 1 人挂科，去年**无人挂科**。
> 老师的原则：**"你如果是 59 分差那 1 分到 60，我不会刁难你；但你 89 分想要 90，那就不会帮。"**

### 📝 期中考试（⭐ 最重要）

> [!important] 已确认的全部信息
> - **时间**：**2026 年 9 月 24 日（第 4 周 周四）**
> - **范围**：**只考第一章**（The Foundations: Logic and Proofs）。
>   老师明确说："9 月 24 日之前我们会开始讲第二章和其他章节，**但第二章不需要为期中复习**"——因为两天挨得太近。
> - **形式**：**闭卷 Closed book**（期末同样闭卷）
> - **考场**（AI 一班 / AI 二班分开）：
> - 
>   | 班级 | 考场 |
>   |---|---|
>   | **AI 一班** | **408** |
>   | **AI 二班** | **409**（平时上课的教室） |
>   最终安排以 QQ 群通知为准。

### 🎯 ⭐⭐ 考题来源（第 1 节课老师亲口说明）

> [!warning] 这是全课最重要的一条备考情报
> **"我的期末考试和期中考试题，大部分来自教材的课后练习题（practice questions）。
> 当然会有一些修改，但改动十分有限。"**
>
> 而且他补充了筛选范围：
> **"我不是每个 chapter 都会讲——你要看 syllabus，看我会教哪些部分，然后去做那些部分的练习题。
> 如果你把那些题都做对了，我完全确信你能在这门课拿到非常好的成绩。"**
>
> **备考动作**：对照 syllabus 圈出讲过的小节 → **刷 Rosen 对应小节的课后习题** → **用教材最后几页的答案自查**（老师专门提到"textbook 最后几页会列出最终答案"）。

> [!important] 📍 已被老师点名的往年真题（滚动更新）
> | 题目 | 出处 | 老师的原话 |
> |---|---|---|
> | **"什么是 tautology（永真式）？"** | 去年**期末** | "非常简单的一个概念，但有一小部分人没答上来" |
> | **把 $\forall x\exists y\,P(x,y)$ 在 $\{1,2,3\}$ 上展开** | 某年**期末** | "这道题有一年被我拿来做期末考试的题了，今年拿来做例题" |
> | **用直接证明证"$n$ 奇 ⇒ $n^2$ 奇"** | **上学期期末** | "这就是期末的考试题，就是要你用 direct proof 做这么一个证明题" |
> | **自然语言 ↔ 量词表达式的翻译** | **本次期中预告** | "这种自然语言的翻译工作，肯定会是你们期中考试的题目" |
> | **等价律推导题** | **本次期中预告** | "一定有推导题，这个毋庸置疑——这太好出试卷了" |

### ✍️ ⭐⭐ 答题规范（老师**三次**强调，直接关系得分）

> [!warning] 推导题：每一步都必须注明依据
> 第 1 节课、第 4 节课、第 8 节课**各强调了一次**，第 8 节课的原话是：
> **"我强调一遍，请大家务必记住——这会影响你是否能拿到完整的分数。"**
>
> **格式**：`每一步的表达式　|　右侧写规则名 或 该规则的公式`
> - 记得住名字就写名字（Identity Law、De Morgan's Laws、Modus Ponens…）；
> - **记不住名字，把该定律的等式写在旁边同样给分**——老师原话："摩根肯定是人名，我都记不住。你可以写公式，我就知道你是什么意思。"

> [!warning] ⭐ 结论是复合表达式时，必须推出**整个表达式**
> 第 8 节课有同学问："我推出 $\neg q$ 真、$s$ 真，再组合成 $\neg q\to s$ 可以吗？"
> **老师：不行。**
> **"我要的是整个 expression 为真，而不是 $\neg q$ 真、$s$ 真。"**
> （之所以容易混，是因为上一题的结论恰好是单个 $t$，一个命题就是一个完整表达式。）
> 详见 [[C1.6 推理规则 Rules of Inference]] 课堂补充 T1。

> [!warning] $\mathbf T$ / $\mathbf F$ 禁止当变量用
> 在离散数学里 $\mathbf T$、$\mathbf F$ 有特殊含义（恒真/恒假），**不能拿来代表命题变元**。
> 老师在 §1.3 和 §1.6 各强调过一次，而且**当场承认自己课件上误用了 $T$ 做代换变量**，说"考试这么写可能要扣分"。
> **做代换时请用 $S,R$ 或 $A,B$。**

> [!note] 其他两条小规范
> - **题目用什么字母，你就可以用什么字母**：往年考题有用 $x,y,z$ 的，"你写 $p,q$ 也行，$x,y,z$ 也行，**但总得写出公式**"。
> - **$\equiv$ 与 $\Leftrightarrow$ 等效，但一份答卷里要统一**，不要一行三条杠、下一行双箭头。

### 📄 作业规范

> [!important] 四条硬性要求
> 1. **必须手写**——不接受打字稿。**用 iPad 等电子设备手写是允许的**（有同学私下问过，老师公开确认）。
> 2. **不必抄题**，直接写答案。
> 3. 提交**扫描件或照片**（PDF / JPG），通过 **QQ 群里助教公布的链接**提交。
> 4. **提交后务必确认成功**——助教会公布提交名单，**自己核对**。
>
> ⚠️ 老师专门讲了一个案例：上学期有同学称已提交但系统未收到，**直到期末合分时才反映**，老师认为这不合理。
> **"如果几个月都没看到分数，应该第一时间反馈。"**
>
> **迟交政策**：晚 3 天交会扣迟交分但仍给分；拖到学期末才交一般不予接受。

### ⚖️ 学术诚信

> [!warning] 老师讲了两个真实案例
> - 上学期本院有学生**找人替考**（且不同性别），已被**劝退**；
> - 老师的强化学习课上抓到有学生**用大模型拍照答题**，该课直接挂科。
>
> 老师对大模型的态度：**可以用来启发思路，但不要依赖**——
> **"因为考试是闭卷的，你如果一直靠大模型解题，考试时会很困难。"**

### 📈 教学节奏预告

> [!note] 第一章之后会明显加速
> **"第一章我们花了近 3 周，其他章节会讲得非常快，有时候一次课就讲完一整章。"**
> **"这不意味着其他章节不重要——而且后面的题目难度会比前几周更大。"**
> **9 月 20 日（周日）开始进入第二章及后续章节。**

---

## 📚 课堂进度与课件对照（Dr. 欧士琪 SCUT 2026 Fall）

> [!info] 已收到的课件
> | 课件文件 | 日期 | 覆盖内容 | 已并入笔记 |
> |---|---|---|---|
> | `Ch1.1_Part1.pdf`（23 slides） | 2026-09-02 | Warm Up 四题、Wason 随堂测四题、命题定义、$\neg\ \wedge\ \vee\ \oplus$、两道 Small Exercise | [[C1.1 命题逻辑 Propositional Logic]] 课件补充 L0–L3 |
> | `Ch1.1_Part2.pdf`（20 slides） | 2026-09-02 | 真值表、条件语句、必要/充分条件、双条件、运算符总表 | [[C1.1 命题逻辑 Propositional Logic]] 课件补充 L4 |
> | `Ch1.1_Part3.pdf`（18 slides） | 2026-09-03 | 复合命题、**运算优先级**、加括号五步、逐列建表、翻译四步算法 | [[C1.1 命题逻辑 Propositional Logic]] 课件补充 L5–L6 |
> | `Ch1.2.pdf`（12 slides） | 2026-09-03 | 系统规约（真值表解法）、位运算、Batman/Joker 谜题、**命题类型** | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] 课件补充 L1–L4 |
> | `Ch1.3.pdf`（29 slides） | 2026-09-08 | 逻辑等价定义、真值表法及其代价、Table 6 逐条真值表验证、德摩根律推广、**Table 7/8 全部推导** | [[C1.3 命题等价 Propositional Equivalences]] 课件补充 L1–L4 |
> | `Ch1.4_Part1.pdf`（29 slides） | 2026-09-09 | 命题逻辑的两个局限、谓词、量化四要素、三类量化、判真判假四格表、量词优先级、作用域与自由/约束变元 | [[C1.4 谓词与量词 Predicates and Quantifiers]] 课件补充 L1–L4 |
> | `Ch1.4_Part2.pdf`（29 slides） | 2026-09-10 | **自由/约束变元七行对照表**、**量词分配律的四人反例表**、**含常量 $A$ 的八条等价式**、量词德摩根律、受限论域三种写法、翻译与系统规约 | [[C1.4 谓词与量词 Predicates and Quantifiers]] 课件补充 L5–L9 |
> | `Ch1.5_Part1.pdf`（13 slides） | 2026-09-10 | 嵌套量词判读口诀、量词顺序、$xy=0$ 随堂测、翻译例题 | [[C1.5 嵌套量词 Nested Quantifiers]] 课件补充 L1 |
> | `Ch1.5_Part2.pdf`（22 slides） | 2026-09-15 | ⭐ **「恰好一个」四种情形（15 张）**、$\forall x(P(x)\to A)\equiv\exists xP(x)\to A$、有限论域展开、嵌套量词的否定 | [[C1.5 嵌套量词 Nested Quantifiers]] 课件补充 L2–L4 |
> | `Ch1.6_Part1.pdf`（8 slides） | 2026-09-15 | 两个错误论证引入、论证/前提/结论、有效性判据（"只盯前真后假"） | [[C1.6 推理规则 Rules of Inference]] 课件补充 L1–L2 |
> | `Ch1.6_Part2.pdf`（33 slides） | 2026-09-16 | Table 1 八条规则、**推理 vs 等价对照表**、**⇒ 链式书写法**、两个谬误、四条量化规则、全称肯定前件式 | [[C1.6 推理规则 Rules of Inference]] 课件补充 L3–L7 |
> | `Ch1.6_Part3.pdf`（20 slides） | 2026-09-16 | ⚠️ **文件名写 1.6，内容是教材 §1.7**：非形式证明、定理与证明的分类表、直接证明（含"死胡同"例）、逆否证明 | [[C1.7 证明导论 Introduction to Proofs]] 课件补充 L1–L5 |

> [!info] 🎤 课堂录音转写稿（已合并）
> `transcript/1-8节课-已合并.txt`——**第 1–8 节课**的完整录音转写，覆盖 2026-09-02 至 2026-09-16。
> 该文件内每节课含**两遍识别结果**，已按惯例只取质量更高的**第一遍**。
> 转写稿独有的内容（课程信息、考试情报、答题规范、课件勘误、师生问答）已分别并入：
> [[C1.1 命题逻辑 Propositional Logic]]、[[C1.3 命题等价 Propositional Equivalences]]、[[C1.4 谓词与量词 Predicates and Quantifiers]]、[[C1.5 嵌套量词 Nested Quantifiers]]、[[C1.6 推理规则 Rules of Inference]]、[[C1.7 证明导论 Introduction to Proofs]] 各篇的「🎤 课堂补充」小节，以及本页的「🎓 课程信息与考试情报」。

> [!warning] ⚠️ `Ch1.6_Part3.pdf` 的文件名与内容不符
> 这份课件标题写的是 "1.6 Rules of Inference (Part 3)"，但**整份讲的都是教材 §1.7 的证明方法**。
> 复习 §1.7 时**一定要打开这份文件**，不要被文件名误导。

> [!info] 🏷️ 全库「拓展」标注约定
> 从 §1.3 起，各篇笔记中标有 **（拓展）** 或 **【拓展】** 的内容，表示**课堂课件中没有出现、仅存在于教材**的部分。
> - 复习时**先掌握未标注的主干内容**，行有余力再看拓展；
> - 拿到新课件后需要**回头退役**已被讲到的标记（把"（拓展）"摘掉，内容一个字不删）。
>
> **当前各篇的标注状态**
> | 笔记 | 课件覆盖情况 | 标注情况 |
> |---|---|---|
> | [[C1.1 命题逻辑 Propositional Logic]] | 完整覆盖（Part1–3） | 无需标注 |
> | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] | 部分覆盖 | 见该篇「课件 vs 教材」表 |
> | [[C1.3 命题等价 Propositional Equivalences]] | §2–§5 全覆盖 | §6 可满足性、§7 数独、§8 SAT + 9 处习题 已标 |
> | [[C1.4 谓词与量词 Predicates and Quantifiers]] | §0–§9 基本全覆盖 | 前置/后置条件、空论域、嵌套循环、Lewis Carroll、Prolog 已标 |
> | [[C1.5 嵌套量词 Nested Quantifiers]] | 主干全覆盖 | 嵌套循环、极限定义、极限不存在、航空公司例、Carroll 习题 已标 |
> | [[C1.6 推理规则 Rules of Inference]] | **几乎全覆盖** | 仅「子句与 CNF」已标 |
> | [[C1.7 证明导论 Introduction to Proofs]] | **只讲了一半** | 术语、空/平凡证明、反证法展开、等价性证明、反例、证明错误 已标 |
> | [[C1.8 证明方法与策略 Proof Methods and Strategy]] | **整节尚未讲授** | 按约定**不逐条标注**，见该篇篇首进度说明 |
>
> **✅ 已用第 1–8 节课的录音转写稿复核**：上表中所有标为（拓展）的内容，课堂上确实**都没有讲到**，标记全部保留有效，**本次无需退役任何标记**。
> 唯一需要说明的是 [[C1.7 证明导论 Introduction to Proofs]] §8 反证法——老师在**第 1 节课**的"证明方法概览"里口头介绍过它的做法（"假设结论不成立，倒推出矛盾"），在**第 8 节课**的分类表里也点了名，但**始终没有展开、没有给例子**，故维持「课堂仅点到方法名，展开为拓展」的写法。
> | 第 2 章各篇 | **整章尚未讲授** | 同上，见 [[C2 基本结构：集合、函数、序列、求和与矩阵 MOC]] |

### 讲课顺序 ≠ 教材顺序（**复习时按课件顺序走**）

```mermaid
graph LR
    subgraph 老师的 Ch1.1
    A1["Proposition<br/>命题定义"] --> A2["Propositional Operator<br/>¬ ∧ ∨ ⊕ → ↔"]
    A2 --> A3["Compound Proposition<br/>优先级 / 加括号 / 建表"]
    A3 --> A4["Applications<br/>翻译英语句子"]
    end
    subgraph 老师的 Ch1.2
    B1["System Specifications<br/>系统规约"] --> B2["Logic and Bit Operations<br/>位运算 ← 教材在 1.1"]
    B2 --> B3["Logic Puzzles<br/>Batman / Joker"]
    B3 --> B4["Types of Proposition<br/>永真/矛盾/可能 ← 教材在 1.3"]
    end
    A4 --> B1
    B4 -.->|"下次课大概率接"| C["1.3 逻辑等价<br/>Table 6/7/8"]
```

| 教材位置 | 老师放在 | 备注 |
|---|---|---|
| §1.1 位运算 | **§1.2** | 推迟 |
| §1.2 翻译英语句子 | **§1.1 Part 3** | 提前 |
| §1.2 布尔检索 | **暂未讲** | |
| §1.2 泥孩子问题 | **暂未讲** | |
| §1.2 逻辑电路 | **暂未讲** | 可能并入第 12 章 |
| §1.3 可满足性 / 数独 / SAT | **暂未讲** | 本笔记 §6–§8 已标（拓展） |
| §1.4 前置/后置条件、Lewis Carroll、Prolog | **暂未讲** | 已标（拓展） |
| §1.5 极限的 $\varepsilon$-$\delta$ 定义 | **暂未讲** | 已标（拓展） |
| §1.7 反证法、$\sqrt2$ 无理、等价性证明、反例、证明错误 | **暂未讲** | 已标（拓展） |
| §1.7 "恰好一个"的表达 | **提前到 §1.5** | ⭐ 老师在 Ch1.5 Part2 用 15 张幻灯片专讲 |
| **§1.8 全节** | **暂未讲** | 整节未开讲 |
| §1.3 命题类型（永真/矛盾/可能） | **§1.2** | 提前 |

### ⚠️ 课件与教材的**实质性差异**（考试以课件为准）

> [!warning] 只有一处，但很关键
> **运算符优先级**：教材 Table 8 只列 5 个运算符（不含 $\oplus$）；**老师的表把 $\vee$ 和 $\oplus$ 并列为第 3 级**：
>
> | 优先级 | 运算符 |
> |:-:|:-:|
> | 1 | $\neg$ |
> | 2 | $\wedge$ |
> | 3 | **$\vee$、$\oplus$** |
> | 4 | $\to$ |
> | 5 | $\leftrightarrow$ |
>
> 详见 [[C1.1 命题逻辑 Propositional Logic]] 课件补充 L5.1。

### 老师独有、教材没有的知识点（**这些最容易被漏掉**）

> [!important] §1.3–§1.7 新增的六条（2026-09-08 起的课件）
> | 内容 | 位置 | 为什么重要 |
> |---|---|---|
> | **Table 7/8 全部现场推导，只背 $P\to Q\equiv\neg P\vee Q$** | [[C1.3 命题等价 Propositional Equivalences]] 课件补充 L2 | ⭐⭐ 老师不要求背表，**要求会推**——考法完全不同 |
> | **自由 / 约束变元七行对照表** | [[C1.4 谓词与量词 Predicates and Quantifiers]] 课件补充 L5 | ⭐ 概念辨析题的标准答案来源 |
> | **量词分配律的四人反例表** | [[C1.4 谓词与量词 Predicates and Quantifiers]] 课件补充 L6 | ⭐⭐ 两条不成立的分配律，必须会举反例 |
> | **含常量 $A$ 的八条量词等价式** | [[C1.4 谓词与量词 Predicates and Quantifiers]] 课件补充 L7 | ⭐ 教材未列，化简量词式必用 |
> | **「恰好一个」四种情形 + 两个陷阱** | [[C1.5 嵌套量词 Nested Quantifiers]] 课件补充 L2 | ⭐⭐ 课堂占时最多，翻译大题的头号考点 |
> | **推理 vs 等价对照表、⇒ 链式书写法** | [[C1.6 推理规则 Rules of Inference]] 课件补充 L3–L4 | ⭐ 澄清 $\to$ 与 $\leftrightarrow$ 的分工；第二种答题格式 |


| 内容 | 位置 | 为什么重要 |
|---|---|---|
| **Warm Up 四个错误推理** | [[C1.1 命题逻辑 Propositional Logic]] L0 | 全章四大陷阱的预告 |
| **Wason 选择任务四题** | [[C1.1 命题逻辑 Propositional Logic]] L1 | ⭐ 检验 $p \to q$ 只需查"$p$ 真"和"$q$ 假"两项 |
| **$\wedge$ 像 A、$\vee$ 像 v 的助记** | [[C1.1 命题逻辑 Propositional Logic]] L2.2 | 专治符号记反 |
| **否定不能提供额外信息** | [[C1.1 命题逻辑 Propositional Logic]] L3 | ⭐ "Today is Monday" 不是 "Today is Friday" 的否定 |
| **必要/充分条件的真值表定义** | [[C1.1 命题逻辑 Propositional Logic]] L4.4 | ⭐ 一秒定箭头方向 |
| **必要/充分四种组合总表** | [[C1.1 命题逻辑 Propositional Logic]] L4.9 | 概念辨析题 |
| **加括号五步 + 逐列建表六步** | [[C1.1 命题逻辑 Propositional Logic]] L5.2–L5.3 | ⭐ 答题的标准格式 |
| **翻译英语句子四步算法** | [[C1.1 命题逻辑 Propositional Logic]] L6 | ⭐ 翻译大题的步骤分 |
| **系统规约的真值表解法** | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] L1.3 | 与教材推理法互补 |
| **Batman/Joker 的穷举表解法** | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] L3 | 谜题题的通法 |

---

## 全章知识地图

```mermaid
graph TD
    START["第 1 章<br/>基础：逻辑与证明"] --> A["【语言层】<br/>命题逻辑 1.1–1.3"]
    START --> B["【语言层】<br/>谓词逻辑 1.4–1.5"]
    START --> C["【推理层】<br/>推理规则 1.6"]
    START --> D["【实践层】<br/>证明方法 1.7–1.8"]

    A --> A1["1.1 命题 + 5 个联结词<br/>¬ ∧ ∨ ⊕ → ↔"]
    A1 --> A2["1.2 应用：翻译 / 规约 / 检索<br/>谜题 / 逻辑电路"]
    A1 --> A3["1.3 逻辑等价 ≡<br/>Table 6/7/8 + 可满足性 SAT"]

    A3 -->|"命题逻辑表达力不够<br/>看不见句子内部结构"| B1["1.4 谓词 P(x) + 量词 ∀ ∃"]
    B1 --> B2["1.5 嵌套量词<br/>⭐ 量词顺序"]

    A3 --> C1["1.6 命题逻辑推理规则<br/>8 条 Table 1"]
    B2 --> C2["1.6 量化推理规则<br/>UI / UG / EI / EG"]
    C1 & C2 --> C3["组合：全称肯定前件式<br/>全称否定后件式"]

    C3 --> D1["1.7 四种基本证明方法<br/>直接 / 逆否 / 空+平凡 / 反证"]
    D1 --> D2["1.8 扩展方法<br/>穷举 / 分情况 / WLOG<br/>存在性 / 唯一性"]
    D2 --> D3["证明策略<br/>正向 / 逆向 / 改编 / 找反例"]

    D3 --> E["后续章节"]
    E --> E1["第 2 章 集合<br/>（Table 6 → 集合恒等式）"]
    E --> E2["第 4 章 数论<br/>（√n 无理、素性判定）"]
    E --> E3["第 5 章 数学归纳法<br/>（∀n P(n)）"]
    E --> E4["第 6 章 组合<br/>（鸽巢原理、组合证明）"]
    E --> E5["第 12 章 布尔代数<br/>（逻辑电路化简）"]
```

---

## 三张必背的表

### TABLE A｜命题逻辑真值表汇总（§1.1）

| $p$ | $q$ | $\neg p$ | $p \wedge q$ | $p \vee q$ | $p \oplus q$ | $p \to q$ | $p \leftrightarrow q$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| T | T | F | **T** | T | F | T | **T** |
| T | F | F | F | T | T | **F** | F |
| F | T | T | F | T | T | T | F |
| F | F | T | F | **F** | F | T | **T** |

**优先级**：$\neg$ (1) > $\wedge$ (2) > $\vee$、$\oplus$ (3) > $\to$ (4) > $\leftrightarrow$ (5)；**量词 $\forall,\exists$ 高于一切联结词**。
（⚠️ $\oplus$ 与 $\vee$ 同级是**老师课件的规定**，教材 Table 8 未列 $\oplus$——考试按课件。）

### TABLE B｜最常用的逻辑等价（§1.3）

| 等价式 | 名称 |
|---|---|
| $p \to q \equiv \neg p \vee q$ | ⭐ 条件的析取形式（**消箭头**） |
| $\neg(p \to q) \equiv p \wedge \neg q$ | ⭐ **条件的否定 = 反例** |
| $p \to q \equiv \neg q \to \neg p$ | ⭐ 逆否等价 |
| $\neg(p \wedge q) \equiv \neg p \vee \neg q$ | ⭐ 德摩根律 |
| $\neg(p \vee q) \equiv \neg p \wedge \neg q$ | ⭐ 德摩根律 |
| $p \leftrightarrow q \equiv (p\to q)\wedge(q\to p)$ | 双条件的定义式 |
| $(p \to r)\wedge(q\to r) \equiv (p\vee q)\to r$ | 分情况证明的依据 |
| $p \to (q \to r) \equiv (p \wedge q) \to r$ | 输出律 exportation |
| $\neg\forall x P(x) \equiv \exists x \neg P(x)$ | ⭐ 量词德摩根律 |
| $\neg\exists x P(x) \equiv \forall x \neg P(x)$ | ⭐ 量词德摩根律 |
| $\neg\forall x(P(x)\to Q(x)) \equiv \exists x(P(x)\wedge\neg Q(x))$ | ⭐ **反例的形式化** |

### TABLE C｜推理规则（§1.6）

| 规则 | 形式 | 名称 |
|---|---|---|
| 1 | $p,\ p\to q \therefore q$ | Modus ponens 肯定前件式 |
| 2 | $\neg q,\ p\to q \therefore \neg p$ | Modus tollens 否定后件式 |
| 3 | $p\to q,\ q\to r \therefore p\to r$ | Hypothetical syllogism 假言三段论 |
| 4 | $p\vee q,\ \neg p \therefore q$ | Disjunctive syllogism 析取三段论 |
| 5 | $p \therefore p\vee q$ | Addition 附加律 |
| 6 | $p\wedge q \therefore p$ | Simplification 化简律 |
| 7 | $p,\ q \therefore p\wedge q$ | Conjunction 合取律 |
| 8 | $p\vee q,\ \neg p\vee r \therefore q\vee r$ | Resolution 归结 |
| 9 | $\forall xP(x) \therefore P(c)$ | Universal instantiation 全称实例化 |
| 10 | $P(c)$（任意 $c$）$\therefore \forall xP(x)$ | Universal generalization 全称推广 |
| 11 | $\exists xP(x) \therefore P(c)$（某个 $c$） | Existential instantiation 存在实例化 |
| 12 | $P(c)$（某个 $c$）$\therefore \exists xP(x)$ | Existential generalization 存在推广 |

**❌ 两个谬误（形似规则但无效）**：
- **肯定后件谬误**：$p\to q,\ q \therefore p$
- **否定前件谬误**：$p\to q,\ \neg p \therefore \neg q$

---

## 关键术语表 Key Terms（**课本原文术语，附中文对照**）

> [!note] 使用说明
> 这是课本章末 "Key Terms and Results" 的完整翻译对照，**一个都没省略**。名词解释题直接从这里出。

### §1.1–1.2 命题逻辑

| 英文术语 | 中文 | 定义 |
|---|---|---|
| **proposition** | 命题 | 一个非真即假的陈述 |
| **propositional variable** | 命题变元 | 表示一个命题的变量 |
| **truth value** | 真值 | 真或假 |
| **$\neg p$ (negation of $p$)** | $p$ 的否定 | 真值与 $p$ 相反的命题 |
| **logical operators** | 逻辑运算符 | 用来组合命题的运算符 |
| **compound proposition** | 复合命题 | 用逻辑运算符组合若干命题构造出的命题 |
| **truth table** | 真值表 | 显示命题所有可能真值的表 |
| **$p \vee q$ (disjunction)** | $p$ 与 $q$ 的析取 | 命题"$p$ 或 $q$"，当且仅当 $p,q$ 中至少一个为真时为真 |
| **$p \wedge q$ (conjunction)** | $p$ 与 $q$ 的合取 | 命题"$p$ 且 $q$"，当且仅当 $p,q$ 都为真时为真 |
| **$p \oplus q$ (exclusive or)** | $p$ 与 $q$ 的异或 | 命题"$p$ XOR $q$"，当 $p,q$ 中恰好一个为真时为真 |
| **$p \to q$ ($p$ implies $q$)** | $p$ 蕴涵 $q$ | 命题"若 $p$ 则 $q$"，当且仅当 $p$ 真且 $q$ 假时为假 |
| **converse of $p \to q$** | $p\to q$ 的逆命题 | 条件语句 $q \to p$ |
| **contrapositive of $p \to q$** | $p\to q$ 的逆否命题 | 条件语句 $\neg q \to \neg p$ |
| **inverse of $p \to q$** | $p\to q$ 的否命题 | 条件语句 $\neg p \to \neg q$ |
| **$p \leftrightarrow q$ (biconditional)** | 双条件 | 命题"$p$ 当且仅当 $q$"，当且仅当 $p,q$ 真值相同时为真 |
| **bit** | 位 | 0 或 1 |
| **Boolean variable** | 布尔变量 | 取值为 0 或 1 的变量 |
| **bit operation** | 位运算 | 对一个或多个位的运算 |
| **bit string** | 位串 | 位的序列 |
| **bitwise operations** | 按位运算 | 对位串的运算，对一个串中每一位与另一串中对应位进行操作 |
| **logic gate** | 逻辑门 | 对一个或多个位执行逻辑运算并产生一个输出位的逻辑元件 |
| **logic circuit** | 逻辑电路 | 由逻辑门构成、产生一个或多个输出位的开关电路 |

### §1.3 命题等价

| 英文术语 | 中文 | 定义 |
|---|---|---|
| **tautology** | 永真式 / 重言式 | 永远为真的复合命题 |
| **contradiction** | 矛盾式 | 永远为假的复合命题 |
| **contingency** | 可能式 | 有时为真有时为假的复合命题 |
| **consistent compound propositions** | 一致的复合命题 | 存在一组变量真值赋值使这些命题全部为真 |
| **satisfiable compound proposition** | 可满足的复合命题 | 存在一组变量真值赋值使其为真 |
| **logically equivalent compound propositions** | 逻辑等价的复合命题 | 真值永远相同的复合命题 |

### §1.4–1.5 谓词逻辑

| 英文术语 | 中文 | 定义 |
|---|---|---|
| **predicate** | 谓词 | 句子中给主语赋予某种性质的那一部分 |
| **propositional function** | 命题函数 | 含一个或多个变量的陈述，当每个变量被赋值或被量词约束时成为命题 |
| **domain (universe) of discourse** | 论域（讨论域） | 命题函数中变量可以取的值 |
| **$\exists x P(x)$** | $P(x)$ 的存在量化 | 当且仅当论域中存在 $x$ 使 $P(x)$ 为真时该命题为真 |
| **$\forall x P(x)$** | $P(x)$ 的全称量化 | 当且仅当论域中每个 $x$ 都使 $P(x)$ 为真时该命题为真 |
| **logically equivalent expressions** | 逻辑等价的表达式 | 无论代入什么命题函数、使用什么论域，真值都相同的表达式 |
| **free variable** | 自由变元 | 命题函数中未被约束的变量 |
| **bound variable** | 约束变元 | 被量化的变量 |
| **scope of a quantifier** | 量词的作用域 | 陈述中量词约束其变量的那一部分 |

### §1.6 推理规则

| 英文术语 | 中文 | 定义 |
|---|---|---|
| **argument** | 论证 | 一个陈述序列 |
| **argument form** | 论证形式 | 一个由命题变元构成的复合命题序列 |
| **premise** | 前提 | 论证或论证形式中除最后一个之外的陈述 |
| **conclusion** | 结论 | 论证或论证形式中的最后一个陈述 |
| **valid argument form** | 有效的论证形式 | 所有前提的真蕴涵结论为真的复合命题序列 |
| **valid argument** | 有效论证 | 具有有效论证形式的论证 |
| **rule of inference** | 推理规则 | 可用于证明论证有效的有效论证形式 |
| **fallacy** | 谬误 | 常被错误地当作推理规则使用的无效论证形式（更一般地，指不正确的论证） |
| **circular reasoning / begging the question** | 循环论证 / 窃取论题 | 一个或多个步骤基于待证陈述本身为真的推理 |

### §1.7–1.8 证明

| 英文术语 | 中文 | 定义 |
|---|---|---|
| **theorem** | 定理 | 可以被证明为真的数学断言 |
| **conjecture** | 猜想 | 被提出为真但尚未被证明的数学断言 |
| **proof** | 证明 | 定理为真的论证 |
| **axiom** | 公理 | 被假定为真、可作为证明定理基础的陈述 |
| **lemma** | 引理 | 用来证明其他定理的定理 |
| **corollary** | 推论 | 可作为刚证明的定理的推论而被证明的命题 |
| **vacuous proof** | 空证明 | 基于 $p$ 为假来证明 $p\to q$ 为真的证明 |
| **trivial proof** | 平凡证明 | 基于 $q$ 为真来证明 $p\to q$ 为真的证明 |
| **direct proof** | 直接证明 | 通过说明 $p$ 真时 $q$ 必真来证明 $p\to q$ 为真 |
| **proof by contraposition** | 逆否证明 | 通过说明 $q$ 假时 $p$ 必假来证明 $p\to q$ 为真 |
| **proof by contradiction** | 反证法 | 基于条件语句 $\neg p \to q$ 为真（其中 $q$ 是矛盾式）来证明 $p$ 为真 |
| **exhaustive proof** | 穷举证明 | 通过检查所有可能情形的清单来确立结果的证明 |
| **proof by cases** | 分情况证明 | 分成若干情形的证明，这些情形覆盖所有可能性 |
| **without loss of generality (WLOG)** | 不失一般性 | 证明中的一种假设，使得可以通过减少需考虑的情形数来证明定理 |
| **counterexample** | 反例 | 使 $P(x)$ 为假的元素 $x$ |
| **constructive existence proof** | 构造性存在性证明 | 明确找出具有指定性质的元素的存在性证明 |
| **nonconstructive existence proof** | 非构造性存在性证明 | 不明确找出该元素的存在性证明 |
| **rational number** | 有理数 | 可以表示为两个整数 $p, q$ 之比（$q \ne 0$）的数 |
| **uniqueness proof** | 唯一性证明 | 证明恰好有一个元素满足指定性质 |

### 关键结果 RESULTS（课本原文）

1. **§1.3 Table 6、7、8 中给出的逻辑等价。**
2. **量词的德摩根律 (De Morgan's laws for quantifiers)。**
3. **命题演算的推理规则 (Rules of inference for propositional calculus)。**
4. **量化语句的推理规则 (Rules of inference for quantified statements)。**

---

## 章末复习题速答 Review Questions

> [!question] 1. 定义命题的否定。"This is a boring course" 的否定是什么？
> **答**：$\neg p$ 是真值与 $p$ 相反的命题，读作"并非 $p$"。
> 否定："**This is not a boring course.**"

> [!question] 2. 用真值表定义析取、合取、异或、条件、双条件。
> **答**：见上文 TABLE A。
> 以 $p$ = "I'll go to the movies tonight"，$q$ = "I'll finish my discrete mathematics homework" 为例：
> - 析取：I'll go to the movies tonight **or** I'll finish my homework.
> - 合取：I'll go to the movies tonight **and** I'll finish my homework.
> - 异或：I'll go to the movies tonight **or** I'll finish my homework, **but not both**.
> - 条件：**If** I go to the movies tonight, **then** I'll finish my homework.
> - 双条件：I'll go to the movies tonight **if and only if** I finish my homework.

> [!question] 3. 至少五种用英语写 $p \to q$ 的方式；定义逆命题和逆否命题。
> **答**：if $p$ then $q$；$p$ implies $q$；$p$ only if $q$；$q$ whenever $p$；$q$ if $p$；$p$ is sufficient for $q$；$q$ is necessary for $p$；$q$ unless $\neg p$；$q$ follows from $p$。
> 逆命题 $q \to p$；逆否命题 $\neg q \to \neg p$。
> 对 "If it is sunny tomorrow, then I will go for a walk in the woods."：
> - **逆命题**：If I go for a walk in the woods tomorrow, then it will be sunny.
> - **逆否命题**：If I do not go for a walk in the woods tomorrow, then it will not be sunny.

> [!question] 4. 什么叫两个命题逻辑等价？有哪些方法证明？
> **答**：$p \leftrightarrow q$ 是永真式。方法：① 真值表逐行比对；② 用已知等价律做链式变形。
> 证 $\neg p \vee (r \to \neg q) \equiv \neg p \vee \neg q \vee \neg r$：
> **方法一（等价变形）**：$r \to \neg q \equiv \neg r \vee \neg q$，故左边 $\equiv \neg p \vee \neg r \vee \neg q \equiv \neg p \vee \neg q \vee \neg r$（交换律）。✓
> **方法二（真值表）**：列 8 行逐一比对（略）。

> [!question] 5. 如何用析取范式由真值表构造命题？为什么这说明 $\{\wedge,\vee,\neg\}$ 功能完备？有单个运算符就完备的吗？
> **答**：对每一个使命题为真的赋值写一个合取项（变元为真写变元、为假写其否定），再把所有合取项析取起来。因为任何真值表都能这样实现，所以 $\{\wedge,\vee,\neg\}$ 功能完备。
> **有**：NAND（$\mid$，Sheffer 竖线）和 NOR（$\downarrow$，Peirce 箭头）各自单独就是功能完备的。

> [!question] 6. 谓词 $P(x)$ 的全称量化和存在量化是什么？它们的否定是什么？
> **答**：$\forall xP(x)$（对论域中每个 $x$，$P(x)$ 为真）；$\exists xP(x)$（论域中存在 $x$ 使 $P(x)$ 为真）。
> 否定：$\neg\forall xP(x) \equiv \exists x\neg P(x)$；$\neg\exists xP(x) \equiv \forall x\neg P(x)$。

> [!question] 7. $\exists x\forall y P(x,y)$ 与 $\forall y \exists x P(x,y)$ 有何区别？举一个真值不同的例子。
> **答**：前者要求存在一个**固定的** $x$ 对所有 $y$ 都成立；后者允许 $x$ 依赖于 $y$。前者更强：$\exists x\forall y P \Rightarrow \forall y\exists x P$，反之不成立。
> **例**：论域为实数，$P(x,y)$ 为 "$x + y = 0$"。
> $\forall y\exists x P(x,y)$ **真**（取 $x = -y$）；$\exists x\forall y P(x,y)$ **假**（没有一个 $x$ 对所有 $y$ 都行）。

> [!question] 8. 什么叫命题逻辑中的有效论证？证明"地球是平的"那个论证有效。
> **答**：有效 = 所有前提的真蕴涵结论为真，等价于 $(p_1\wedge\cdots\wedge p_n)\to q$ 是永真式。
> 设 $p$ = "The earth is flat"，$q$ = "You can sail off the edge of the earth"。
> 前提：$p \to q$ 和 $\neg q$；结论：$\neg p$。
> 这正是 **modus tollens**，是有效的论证形式。✓
> （**注意**：论证有效，但要断定"地球不是平的"为真，还需要前提为真——这里两个前提确实都为真，故论证**可靠**。）

> [!question] 9. 用推理规则证明：由"所有斑马都有条纹"和"Mark 是斑马"推出"Mark 有条纹"。
> **答**：设 $Z(x)$ = "$x$ 是斑马"，$S(x)$ = "$x$ 有条纹"。
> | Step | Reason |
> |---|---|
> | 1. $\forall x(Z(x) \to S(x))$ | Premise |
> | 2. $Z(\text{Mark}) \to S(\text{Mark})$ | Universal instantiation from (1) |
> | 3. $Z(\text{Mark})$ | Premise |
> | 4. $S(\text{Mark})$ | Modus ponens from (2) and (3) |
>
> （即**全称肯定前件式 universal modus ponens**。）

> [!question] 10. 描述直接证明、逆否证明、反证法；对"若 $n$ 是偶数，则 $n+4$ 是偶数"各给一个证明。
> **答**：
> **直接证明**：设 $n$ 偶，$n = 2k$。则 $n + 4 = 2k + 4 = 2(k+2)$ 是偶数。∎
> **逆否证明**：设 $n+4$ 不是偶数，即 $n + 4 = 2k+1$。则 $n = 2k - 3 = 2(k-2) + 1$ 是奇数，即 $n$ 不是偶数。∎
> **反证法**：假设 $n$ 是偶数**且** $n+4$ 不是偶数。由 $n = 2k$ 得 $n+4 = 2(k+2)$ 是偶数，与假设矛盾。∎

> [!question] 11. 如何证明双条件 $p \leftrightarrow q$？证明"$3n+2$ 是奇数当且仅当 $9n+5$ 是偶数"。
> **答**：分别证 $p \to q$ 与 $q \to p$。
> **（⇒）** 设 $3n+2$ 是奇数，则 $3n+2 = 2k+1$，故 $3n = 2k - 1$。于是
> $$9n + 5 = 3(3n) + 5 = 3(2k-1) + 5 = 6k + 2 = 2(3k+1)$$
> 是偶数。✓
> **（⇐）** 用逆否：设 $3n+2$ 是偶数，则 $3n+2 = 2k$，故 $3n = 2k-2$。于是
> $$9n+5 = 3(2k-2)+5 = 6k - 1 = 2(3k-1)+1$$
> 是奇数，即 $9n+5$ 不是偶数。✓ ∎

> [!question] 12. 要证 $p_1,p_2,p_3,p_4$ 等价，证明 $p_4\to p_2$、$p_3\to p_1$、$p_1\to p_2$ 够吗？
> **答**：**不够。** 这三条形成的有向图是 $p_4 \to p_2$，$p_3 \to p_1 \to p_2$——**无法从 $p_2$ 走回任何其他命题**（$p_2$ 没有出边），所以不能建立完整的等价环。
> **一组够用的条件语句**：$p_1 \to p_2$，$p_2 \to p_3$，$p_3 \to p_4$，$p_4 \to p_1$（**循环蕴涵**，任意两点之间都能沿环到达）。

> [!question] 13. 若 $\forall xP(x)$ 为假，如何证明？说明"对每个正整数 $n$，$n^2 \ge 2^n$"为假。
> **答**：**找反例**。
> 取 $n = 3$：$3^2 = 9$，$2^3 = 8$——这个不构成反例（$9 \ge 8$ 成立）。
> 取 $n = 5$：$5^2 = 25$，$2^5 = 32$，$25 < 32$ ⇒ **$n = 5$ 是反例**，该陈述为假。∎
> （$n = 1$：$1 \ge 2$? 否 ⇒ **$n = 1$ 也是反例**，而且更简单。）

> [!question] 14. 构造性与非构造性存在性证明的区别？各举一例。
> **答**：构造性明确给出具有该性质的元素；非构造性证明存在但不给出具体元素。
> **构造性例**：存在一个能以两种方式写成立方和的正整数——$1729 = 10^3+9^3 = 12^3+1^3$。
> **非构造性例**：存在无理数 $x,y$ 使 $x^y$ 有理——由 $\sqrt2^{\sqrt2}$ 有理或无理分两种情形，但不知道是哪种。

> [!question] 15. "存在唯一的 $x$ 使 $P(x)$"的证明包含哪些要素？
> **答**：**存在性**（找到一个 $x$ 使 $P(x)$ 为真）+ **唯一性**（说明若 $y \ne x$ 则 $\neg P(y)$，或等价地：$P(x) \wedge P(y) \Rightarrow x = y$）。

> [!question] 16. 如何用分情况证明关于绝对值的结果，如 $|xy| = |x||y|$？
> **答**：按 $x$ 与 $y$ 的符号分四种情形（都非负 / $x$ 非负 $y$ 负 / $x$ 负 $y$ 非负 / 都负），每种情形中用 $|a| = a$（$a \ge 0$）或 $|a| = -a$（$a < 0$）去掉绝对值号后直接验证。四种情形穷尽所有可能。（详见 [[C1.8 证明方法与策略 Proof Methods and Strategy]] 例 4。）

---

## 补充习题精选 Supplementary Exercises

> [!example] 补充习题 1｜命题符号化（综合复习 §1.1）
> $p$ = "I will do every exercise in this book"，$q$ = "I will get an 'A' in this course"。
> a) **I will get an "A" in this course only if I do every exercise in this book.**
> ⇒ "$q$ only if $p$" = $\boxed{q \to p}$
> b) **I will get an "A" in this course and I will do every exercise in this book.**
> ⇒ $\boxed{q \wedge p}$
> c) **Either I will not get an "A" in this course or I will not do every exercise in this book.**
> ⇒ $\boxed{\neg q \vee \neg p}$（等价于 $\neg(p \wedge q)$，德摩根律）
> d) **For me to get an "A" in this course it is necessary and sufficient that I do every exercise in this book.**
> ⇒ "充要条件" ⇒ $\boxed{q \leftrightarrow p}$
>
> **要点**：a) 的 "only if" 方向和 d) 的"充要条件"是本章翻译题的两大高频考点。

> [!example] 补充习题 33｜改编例 4 到三个因子
> 改编 §1.7 例 4 的证明，证明：若 $n = abc$，其中 $a,b,c$ 是正整数，则 $a \le \sqrt[3]{n}$ 或 $b \le \sqrt[3]{n}$ 或 $c \le \sqrt[3]{n}$。
>
> **解（逆否证明）**：假设结论为假。由**德摩根律**，$a > \sqrt[3]{n}$ **且** $b > \sqrt[3]{n}$ **且** $c > \sqrt[3]{n}$（三个都成立）。
> 三式相乘（都是正数，可以相乘）：
> $$abc > \sqrt[3]{n} \cdot \sqrt[3]{n} \cdot \sqrt[3]{n} = n$$
> 即 $abc \ne n$，与 $n = abc$ 矛盾。
> 由逆否命题，原命题成立。∎
>
> **要点**：与 §1.7 例 4 完全同构（两个因子 → $\sqrt n$，三个因子 → $\sqrt[3]{n}$），是"**改编已有证明**"策略（§1.8）的最佳练习。
> **一般化**：$n = a_1a_2\cdots a_k$ ⇒ 至少有一个 $a_i \le \sqrt[k]{n}$。

> [!example] 补充习题 34｜$\sqrt[3]{2}$ 是无理数
> **证明（反证）**：假设 $\sqrt[3]{2} = a/b$，$a, b$ 是整数，$b \ne 0$，且 $a/b$ 是**最简分数**。
> 两边立方：$2 = a^3/b^3$，即
> $$2b^3 = a^3$$
> 故 $a^3$ 是偶数 ⇒ **$a$ 是偶数**（若 $a$ 奇则 $a^3$ 奇）。设 $a = 2c$：
> $$2b^3 = 8c^3 \implies b^3 = 4c^3 = 2(2c^3)$$
> 故 $b^3$ 是偶数 ⇒ **$b$ 是偶数**。
> 于是 $a, b$ 都有因子 2，与"最简分数"矛盾。∎
>
> **要点**：与 §1.7 例 10（$\sqrt2$ 无理）几乎逐字对应，只是把平方换成立方——**"改编已有证明"的又一个例子**。

> [!example] 补充习题 35｜两个有理数之间必有无理数
> 证明：任何两个有理数之间都存在一个无理数。
>
> **证明（构造性）**：设 $r < s$ 是两个有理数。考虑
> $$x = r + \frac{s - r}{\sqrt2}$$
> **① $x$ 落在 $r$ 与 $s$ 之间**：因为 $1 < \sqrt2 < 2$，有 $0 < \dfrac{s-r}{\sqrt2} < s - r$，故 $r < x < s$。✓
> **② $x$ 是无理数**：假设 $x$ 有理。则
> $$\sqrt2 = \frac{s-r}{x - r}$$
> 是两个有理数之商（$x \ne r$），因而是有理数——与 $\sqrt2$ 无理矛盾。故 $x$ 无理。✓ ∎
>
> **要点**：**"把已知的无理数缩放平移到指定区间"是构造无理数的通用手法。**
> 这个结论说明**无理数在实数中稠密 (dense)**；同理有理数也稠密。这是第 2 章讨论实数集势时的预备知识。

> [!example] 补充习题 39 & 40｜验证 $3x+1$ 猜想
> **39a) $x = 6$**：$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to \boxed{1}$（8 步）
> **39b) $x = 7$**：$7 \to 22 \to 11 \to 34 \to 17 \to 52 \to 26 \to 13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to \boxed{1}$（16 步）
> **39c) $x = 17$**：$17 \to 52 \to 26 \to 13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to \boxed{1}$（12 步）
> **39d) $x = 21$**：$21 \to 64 \to 32 \to 16 \to 8 \to 4 \to 2 \to \boxed{1}$（7 步）
> **40a) $x = 16$**：$16 \to 8 \to 4 \to 2 \to \boxed{1}$（4 步，因为 $16 = 2^4$）
> **40b) $x = 11$**：$11 \to 34 \to 17 \to \cdots \to \boxed{1}$（接 39c 的轨迹，共 14 步）
>
> **要点**：注意 **$2^k$ 形式的数最快**（一路除 2）；一旦轨迹碰到某个已验证过的数，就可以直接接上——**这是记忆化 (memoization) 的思想**，实际验证程序都这么做。

> [!example] 补充习题 41 & 42 & 43 & 44｜铺砌问题综合（染色论证练习）
> **41. 去掉两个"相邻"角（不是对角）的标准棋盘能否铺砌？**
> **解**：**能。** 相邻的两个角**颜色不同**（一黑一白），去掉后剩 31 黑 31 白，共 62 格，颜色平衡，**不违反染色论证**。
> 构造：去掉左上和右上两角后，第一行剩 6 格，可用 3 块横放的骨牌覆盖；其余 7 行各 8 格，每行用 4 块横放的骨牌。总计 $3 + 28 = 31$ 块。✓ ∎
>
> **42. 去掉全部四个角的标准棋盘能否铺砌？**
> **解**：**能。** 四个角中两黑两白，去掉后剩 30 黑 30 白，共 60 格，平衡。
> 构造：第一行和第八行各剩 6 格（各用 3 块横骨牌），中间 6 行各 8 格（各用 4 块）。总计 $3+3+24 = 30$ 块。✓ ∎
>
> **43. 证明：方格数为偶数的矩形棋盘总可以用骨牌铺砌。**
> **证明**：设棋盘为 $m \times n$，$mn$ 为偶数 ⇒ **$m$ 或 $n$ 至少有一个是偶数**。
> 不失一般性设 $n$ 是偶数（否则把棋盘旋转 90°）。则每一行有偶数个格子，**每行用 $n/2$ 块横放的骨牌**即可铺满。总共 $mn/2$ 块。∎
>
> **44. 去掉三个角的 $5\times5$ 棋盘能否铺砌？**
> **解**：**不能。** $5 \times 5 = 25$ 格，去掉 3 格剩 **22** 格，是偶数，奇偶性不排除。用染色：$5\times5$ 棋盘四角同色（设为黑），黑格 13 个、白格 12 个。去掉 3 个角（都是黑格）后剩 **10 黑 12 白**。
> 铺砌需 $22/2 = 11$ 块骨牌，覆盖 11 黑 11 白，与 10 黑 12 白矛盾。**不能铺砌。** ∎
>
> **要点（本组题的总结）**：
> | 去掉的格子 | 颜色 | 是否平衡 | 能否铺砌 |
> |---|---|---|---|
> | 1 个角（例 19） | — | 格数为奇 | ❌ |
> | 对角 2 个角（例 20） | 同色 | 32:30 ❌ | ❌ |
> | 相邻 2 个角（41） | 异色 | 31:31 ✓ | ✅ |
> | 4 个角（42） | 两黑两白 | 30:30 ✓ | ✅ |
> | $5\times5$ 去 3 角（44） | 同色 | 10:12 ❌ | ❌ |
>
> **判据：格数为偶 且 黑白格数相等 是必要条件**（对标准棋盘的这些情形也充分，但一般不一定——见习题 47）。

> [!example] 补充习题 46 & 47｜必要条件不是充分条件
> **46. 从 $8\times8$ 棋盘去掉一个白格和一个黑格，剩下的总能用骨牌铺砌。**（∗ 难题）
> **思路（课本提示）**：说明在插入适当的"隔板"后，剩余格子被划分成的每一部分都能被骨牌覆盖。
> **标准做法（Gomory 定理）**：在棋盘上画一条**蛇形闭回路 (Hamiltonian cycle)**，依次穿过全部 64 格（每格恰好一次，首尾相接）。因为回路上黑白格交替，去掉一黑一白两格后，回路被断成**两段（或一段）路径**，每段路径上的格子数都是**偶数**（因为两端颜色相反），于是每段都可以从一端开始两两配对，用骨牌铺满。∎
>
> **47. 从 $8\times8$ 棋盘去掉两个白格和两个黑格，可以使剩余部分无法铺砌。**
> **解（构造反例）**：去掉与**某个角相邻**的三个格子加上那个角自己，把某一格**孤立**出来。
> 具体地：设左上角为 $(1,1)$。去掉 $(1,2)$、$(2,1)$、以及另外两格使黑白各去两个——例如去掉 $(1,2)$、$(2,1)$（这两格与 $(1,1)$ 异色）、$(1,1)$ 本身、以及任意一个与 $(1,1)$ 同色的格。
> 更简洁的构造：**去掉 $(1,2)$、$(2,1)$、$(2,2)$ 与另一个适当颜色的格**，则 $(1,1)$ 成为**孤立格**——它的两个邻居 $(1,2)$ 和 $(2,1)$ 都被去掉了，没有骨牌能覆盖它。
> 只要调整第四个去掉的格子的颜色使黑白各去两个即可。**因此黑白平衡不是充分条件。** ∎
>
> **要点**：**46 与 47 合起来说明：黑白平衡是必要条件；对"随机去掉一黑一白"是充分的，但对"去掉两黑两白"就不充分了。**
> **一般理论**：骨牌铺砌 ⟺ 棋盘图存在**完美匹配**；由 **Hall 定理 / König 定理**（第 10 章）刻画，比"数颜色"精细得多。

> [!example] 补充习题 49｜五种四格骨牌 Tetrominoes
> a) 画出五种不同的**四格骨牌 (tetromino)**（由四个方格组成的多联骨牌）。
> b) 对每一种，判断能否用它铺砌标准棋盘。
>
> **解 a)（用文本示意，即俄罗斯方块的五种基本块）**：
> ```
> I 形:  ████         O 形:  ██        T 形:  ███
>                            ██               ·█·
>
> L 形:  █··         S/Z 形: ·██
>        ███                 ██·
> ```
> 五种：**I（直线）、O（正方形）、T、L（含其镜像 J）、S（含其镜像 Z）**。
> （注：多联骨牌允许旋转和翻转视为相同，故 L 与 J 算同一种，S 与 Z 算同一种，共 **5** 种。）
>
> **解 b)**：$8\times8 = 64$ 格，每块覆盖 4 格，需 16 块。
> - **I 形**：✅ 能。每行放 2 块横向的 I（$4+4 = 8$），8 行共 16 块。
> - **O 形**：✅ 能。把棋盘划分成 $16$ 个 $2\times2$ 区块，每块放一个 O。
> - **L 形**：✅ 能。两个 L 可以拼成一个 $2\times4$ 矩形，用 8 个这样的矩形铺满。
> - **S/Z 形**：❌ **不能**。（考虑最左上角的格子：任何 S/Z 块覆盖它时都会伸出棋盘或留下无法填补的缺口；严格证明可用**列染色**——把第 1、3、5、7 列染色，每块 S/Z 覆盖这些列中**奇数个**格子……详细论证较长。）
> - **T 形**：✅ **能**。（四个 T 可以拼成一个 $4\times4$ 正方形，用 4 个这样的正方形铺满 $8\times8$。）
>
> **要点**：这题综合了**构造性存在性证明**（能铺的给出构造）与**染色论证**（不能铺的找不变量），是 §1.8 全部技巧的期末大练习。

---

## 全章自测 Chapter Self-Test（30 题快速过关）

> [!question] 命题逻辑（1.1–1.3）
> 1. $p \to q$ 何时为假？ → **仅"前真后假"**
> 2. "$p$ only if $q$" 是什么？ → $p \to q$
> 3. "A unless B" 是什么？ → $\neg B \to A$
> 4. 哪个与 $p\to q$ 等价？ → **逆否命题** $\neg q \to \neg p$
> 5. 充分条件在箭头哪端？ → **箭尾**（必要条件在箭头）
> 6. $n$ 个变元的真值表几行？ → $2^n$
> 7. 运算符优先级？ → $\neg > \wedge > \vee > \to > \leftrightarrow$
> 8. 写出两条德摩根律。 → $\neg(p\wedge q)\equiv\neg p\vee\neg q$；$\neg(p\vee q)\equiv\neg p\wedge\neg q$
> 9. $p \to q$ 的析取形式？ → $\neg p \vee q$
> 10. $\neg(p \to q)$ 等于？ → $p \wedge \neg q$
> 11. 永真式 / 矛盾式 / 可能式的定义？ → 恒真 / 恒假 / 都不是
> 12. "可满足"与"永真"的关系？ → $A$ 不可满足 ⟺ $\neg A$ 永真

> [!question] 谓词逻辑（1.4–1.5）
> 13. 受限论域下 $\forall$ 配什么？$\exists$ 配什么？ → **$\forall$ 配 $\to$，$\exists$ 配 $\wedge$**
> 14. $\neg\forall xP(x)$ 等于？ → $\exists x\neg P(x)$
> 15. $\neg\forall x(P(x)\to Q(x))$ 等于？ → $\exists x(P(x)\wedge\neg Q(x))$（**反例**）
> 16. 哪些量词分配律成立？ → **$\forall$ 对 $\wedge$、$\exists$ 对 $\vee$**（另两个不成立）
> 17. 空论域下 $\forall$ 和 $\exists$ 的真值？ → $\forall$ 恒真，$\exists$ 恒假
> 18. $\forall x\exists y$ 与 $\exists y\forall x$ 谁强？ → **$\exists y\forall x$ 强**，单向蕴涵 $\exists\forall \Rightarrow \forall\exists$
> 19. 写出极限的量词定义。 → $\forall\varepsilon>0\ \exists\delta>0\ \forall x(0<|x-a|<\delta \to |f(x)-L|<\varepsilon)$
> 20. $\exists!xP(x)$ 展开？ → $\exists x(P(x) \wedge \forall y(P(y) \to y = x))$

> [!question] 推理与证明（1.6–1.8）
> 21. 有效 (valid) 与可靠 (sound) 的区别？ → 有效只保证形式；可靠 = 有效 + 前提全真
> 22. 两个谬误是什么？ → **肯定后件**（$p\to q, q \therefore p$）、**否定前件**（$p\to q,\neg p\therefore\neg q$）
> 23. UG 对 $c$ 有什么要求？ → 必须是**任意**元素，不能用它的特殊性质
> 24. 一个证明中 EI 和 UI 谁先用？ → **EI 先**
> 25. 空证明与平凡证明的依据？ → 前提为假 / 结论为真
> 26. 反证法证 $p\to q$ 假设什么？ → **$p$ 且 $\neg q$**
> 27. 证 $n$ 个命题等价最省力的方法？ → **循环蕴涵**，$n$ 个条件语句而非 $n^2-n$ 个
> 28. 逆向推理的正确方向？ → 找可证的 $p$ 使 $p \to q$（**反了就是窃取论题**）
> 29. 染色论证用几种颜色？ → **等于每块拼图覆盖的格子数**
> 30. 课本最后一句话说了什么？ → **不存在能证明所有数学定理的程序**（哥德尔 / 丘奇—图灵）

---

## 与后续章节的连接

```mermaid
graph LR
    C1["第 1 章<br/>逻辑与证明"] --> C2["第 2 章 集合<br/>Table 6 → 集合恒等式<br/>∧↔∩ ∨↔∪ ¬↔补<br/>§2.5 康托尔对角线法"]
    C1 --> C3["第 3 章 算法<br/>SAT 与 NP-完全性<br/>算法正确性证明"]
    C1 --> C4["第 4 章 数论<br/>√n 无理的一般证明<br/>素性判定用 a ≤ √n"]
    C1 --> C5["第 5 章 归纳与递归<br/>§5.1 数学归纳法（∀nP(n)）<br/>§5.3 结构归纳法<br/>§5.5 程序正确性"]
    C1 --> C6["第 6 章 计数<br/>§6.2 鸽巢原理<br/>组合证明"]
    C1 --> C9["第 9 章 关系<br/>n 元谓词 = n 元关系"]
    C1 --> C10["第 10 章 图<br/>骨牌铺砌 = 二分图完美匹配"]
    C1 --> C12["第 12 章 布尔代数<br/>逻辑电路化简<br/>卡诺图 / Quine–McCluskey"]
```

| 本章内容 | 在哪里继续 |
|---|---|
| Table 6 逻辑等价 | 第 2 章**集合恒等式**、第 12 章**布尔代数恒等式**（一一对应） |
| 可满足性 SAT | 第 3 章**算法复杂度**（NP-完全性） |
| 推广的德摩根律 $\neg\bigvee p_j \equiv \bigwedge \neg p_j$ | §5.1 **数学归纳法**证明 |
| 逻辑电路 | 第 12 章**布尔代数与电路设计** |
| 前置/后置条件 | §5.5 **程序正确性** |
| $n$ 元谓词 | 第 9 章**关系**、数据库理论 |
| $\sqrt2$、$\sqrt3$ 无理 | 第 4 章**数论**（一般的 $\sqrt n$） |
| $a \le \sqrt n$（§1.7 例 4） | 第 4 章**素性判定**（只需试除到 $\sqrt n$） |
| 鸽巢原理（§1.7 例 9） | §6.2 **鸽巢原理** |
| 棋盘铺砌与染色 | 第 6 章**组合**、第 10 章**图论匹配**、§5.1 **直角三格骨牌的归纳证明** |
| Chomp 必胜策略 | §5.2 **强归纳法**（正方形网格与两行网格的显式策略） |
| 停机问题 | 后续章节（§3 章及以后） |

---

## 复习路线建议

> [!important] 按考试权重排序的复习顺序
> **第一梯队（必须滚瓜烂熟，占分最多）**
> 1. **§1.1 条件语句的各种英文表述 + 逆/否/逆否** —— 翻译题的全部基础
> 2. **§1.3 Table 6/7/8** —— 化简题、否定题的工具箱
> 3. **§1.4 "$\forall$ 配 $\to$，$\exists$ 配 $\wedge$" + 量词德摩根律** —— 谓词翻译与求否定
> 4. **§1.5 量词顺序** —— 概念辨析题的常客
> 5. **§1.6 Table 1 与 Table 2 + 两个谬误** —— 推理题
>
> **第二梯队（要会做，但套路固定）**
> 6. **§1.7 四种证明方法 + $\sqrt2$ 无理** —— 证明大题
> 7. **§1.8 分情况证明 + 染色论证** —— 证明大题
>
> **第三梯队（理解即可，偶尔考概念）**
> 8. §1.2 逻辑电路、布尔检索、逻辑谜题
> 9. §1.3 数独编码、§1.8 开放问题

> [!question] 一句话概括整章
> **第 1 章教会你两件事：① 如何把含糊的自然语言变成精确的符号（1.1–1.5）；② 如何用这些符号进行不会出错的推理并写出别人认可的证明（1.6–1.8）。**
> 这两件事是后面所有章节、以及你今后所有数学与理论计算机课程的**共同底座**。

---

## 附：本章所有插图索引

| 图 | 出处 | 内容 | 笔记位置 |
|---|---|---|---|
| ![[C1-图1-基本逻辑门-Inverter-OR-AND.png\|60]] | §1.2 FIGURE 1 | 三种基本逻辑门 | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] |
| ![[C1-图2-组合电路示例.png\|60]] | §1.2 FIGURE 2 | 组合电路 $(p\wedge\neg q)\vee\neg r$ | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] |
| ![[C1-图3-电路实现-p或非r-与-非p或-q或非r.png\|60]] | §1.2 FIGURE 3 | 由表达式构造的电路 | [[C1.2 命题逻辑的应用 Applications of Propositional Logic]] |
| ![[C1-图4-9x9数独谜题.png\|60]] | §1.3 FIGURE 1 | $9\times9$ 数独谜题 | [[C1.3 命题等价 Propositional Equivalences]] |
| ![[C1-图5-Chomp游戏与三种走法.png\|60]] | §1.8 FIGURE 1 | Chomp 游戏与三种走法 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] |
| ![[C1-图6-标准棋盘.png\|60]] | §1.8 FIGURE 2 | 标准棋盘 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] |
| ![[C1-图7-两块多米诺骨牌.png\|60]] | §1.8 FIGURE 3 | 两块多米诺骨牌 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] |
| ![[C1-图8-用多米诺骨牌覆盖标准棋盘.png\|60]] | §1.8 FIGURE 4 | 骨牌铺砌标准棋盘 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] |
| ![[C1-图9-去掉左上和右下角的棋盘.png\|60]] | §1.8 FIGURE 5 | 去掉对角两角的棋盘 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] |
| ![[C1-图10-直角三格骨牌与直线三格骨牌.png\|60]] | §1.8 FIGURE 6 | 两种三格骨牌 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] |
| ![[C1-图11-用三种颜色染色的标准棋盘.png\|60]] | §1.8 FIGURE 7 | 三色染色的棋盘 | [[C1.8 证明方法与策略 Proof Methods and Strategy]] |
| ![[C1-课件-Wason选择任务Q1-饮酒年龄.png\|60]] | 课件 Ch1.1 Part1 s8 | Wason 随堂测 Q1：饮酒年龄 | [[C1.1 命题逻辑 Propositional Logic]] |
| ![[C1-课件-Wason选择任务Q2-上网时长.png\|60]] | 课件 Ch1.1 Part1 s9 | Wason 随堂测 Q2：上网时长 | [[C1.1 命题逻辑 Propositional Logic]] |
| ![[C1-课件-Wason选择任务Q3-字母数字卡.png\|60]] | 课件 Ch1.1 Part1 s10 | Wason 随堂测 Q3：字母—数字卡 | [[C1.1 命题逻辑 Propositional Logic]] |
| ![[C1-课件-Wason选择任务Q4-形状颜色卡.png\|60]] | 课件 Ch1.1 Part1 s11 | Wason 随堂测 Q4：形状—颜色卡 | [[C1.1 命题逻辑 Propositional Logic]] |
| ![[C1-课件-Wason选择任务-答案.png\|60]] | 课件 Ch1.1 Part1 s12 | Wason 随堂测答案 | [[C1.1 命题逻辑 Propositional Logic]] |
| ![[C1-课件-数轴示意-x大于50与x小于100.png\|60]] | 课件 Ch1.1 Part1 s22 | 数轴：$x>50$ 与 $x<100$ 的四种运算 | [[C1.1 命题逻辑 Propositional Logic]] |

---

**下一章** → [[C2 基本结构：集合、函数、序列、求和与矩阵 MOC]]
