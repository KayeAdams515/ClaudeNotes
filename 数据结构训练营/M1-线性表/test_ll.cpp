// ============================================================
//  test_ll.cpp —— 单链表测试题
// ============================================================
//  这个文件不用改。它就是"题目要求"本身。
//
//  make test       跑全部关卡（用你写的 ll.h）
//  make test-ref   跑全部关卡（用参考答案）
//  make test-1 .. test-5   只跑某一关
//
//  【每一关都会额外核对不变式】
//  空链表 ⟺ headNode() == NULL 且 tailNode() == NULL 且 length == 0
//  非空   ⟺ 从 head 走 length-1 步正好到达 tail，且 tail->next == NULL
//  tail 忘了更新、length 忘了增减，都会在这里被抓住。
//
//  关于 get(非法下标)：它会 exit()，所以用 CHECK_ADV 丢到子进程里测，
//  只要求"不崩溃"（段错误就会被抓出来）。
// ------------------------------------------------------------

#include <iostream>
#include <string>

#include "testkit.h"

#ifdef USE_REF
#include "ll_ref.h"
#define NODECLASS NodeRef
#define LLCLASS LLRef
#define JOSEPHUS josephusRef
#else
#include "ll.h"
#define NODECLASS Node
#define LLCLASS LL
#define JOSEPHUS josephus
#endif

// ------------------------------------------------------------
// 工具：构建一条链表 + 核对不变式
// ------------------------------------------------------------
template <typename L>
void build(L& list, const int* arr, int n) {
    for (int i = 0; i < n; i++) list.insert(arr[i], i);
}

// 把链表内容拼成字符串，方便一眼看出错在哪
template <typename L>
std::string dump(L& list) {
    std::string s;
    for (int i = 0; i < list.getLength(); i++) {
        s += std::to_string((int)list.get(i));
        if (i + 1 < list.getLength()) s += " ";
    }
    return s;
}

// 说明：测试里如果直接写 headOf(list).data，而学生还没实现构造/插入，
// headNode() 会是 NULL，测试程序自己先段错误——那就什么都测不出来了。
// 所以统一用下面两个安全取值器：指针为空时返回一个静态的假结点，
// 绝不会崩，比较结果自然是"红"，这正是我们想要的。
template <typename L>
NODECLASS<int>& headOf(L& list) {
    static NODECLASS<int> dummy;
    NODECLASS<int>* p = list.headNode();
    return (p != NULL) ? *p : dummy;
}

template <typename L>
NODECLASS<int>& tailOf(L& list) {
    static NODECLASS<int> dummy;
    NODECLASS<int>* p = list.tailNode();
    return (p != NULL) ? *p : dummy;
}

// 不变式总检查：长度、头尾指针、tail->next、能否走到 tail
template <typename L>
bool invariants(L& list) {
    int n = list.getLength();
    NODECLASS<int>* h = list.headNode();
    NODECLASS<int>* t = list.tailNode();

    if (n == 0) {
        return h == NULL && t == NULL;
    }
    if (h == NULL || t == NULL) return false;
    if (t->next != NULL) return false;  // tail 必须停在最后一个结点上

    NODECLASS<int>* p = h;
    for (int i = 0; i < n - 1; i++) {
        if (p == NULL) return false;
        p = p->next;
    }
    return p == t;  // 走 n-1 步必须正好到 tail
}

// ------------------------------------------------------------
// L1：构造、析构、empty、getLength、find、遍历
// ------------------------------------------------------------
int test_l1() {
    std::cout << "\n---- L1 骨架与查找 ----\n";

    LLCLASS<int> list;

    CHECK(list.getLength() == 0, "刚构造的链表长度应该是 0");
    CHECK(list.empty() == true, "刚构造的链表应该是空的");
    CHECK(list.headNode() == NULL, "空链表的 head 应该是 NULL");
    CHECK(list.tailNode() == NULL, "空链表的 tail 应该是 NULL");
    CHECK(invariants(list), "空链表应当满足不变式");

    CHECK(list.find(7) == NULL, "空链表里查找任何东西都应该返回 NULL");

    // 铺一组数据：25 34 57 16 48
    int raw[5] = {25, 34, 57, 16, 48};
    build(list, raw, 5);

    CHECK(list.getLength() == 5, "插入 5 个之后 length 应该是 5");
    CHECK(list.empty() == false, "有元素之后不应该是空表");
    CHECK(invariants(list), "插入 5 个之后 head/tail/length 应当自洽");

    // find 返回的是【结点指针】，不是下标
    NODECLASS<int>* p = list.find(57);
    CHECK(p != NULL, "find(57) 应该找到结点，不能返回 NULL");
    if (p != NULL) CHECK(p->data == 57, "找到的结点里数据应该是 57");

    NODECLASS<int>* q = list.find(48);
    CHECK(q != NULL, "find(48) 应该找到末尾那个结点");
    if (q != NULL) CHECK(q == list.tailNode(), "值 48 在末尾，找到的应该就是 tail");
    if (q != NULL) CHECK(q->next == NULL, "找到的末尾结点 next 应该是 NULL");

    CHECK(list.find(99) == NULL, "查找不存在的值应该返回 NULL");

    // 找到的结点必须真的在链表上（从 head 走得到），不能是个野指针
    NODECLASS<int>* walk = list.headNode();
    bool reached = false;
    while (walk != NULL) {
        if (walk == p) { reached = true; break; }
        walk = walk->next;
    }
    CHECK(reached, "find 返回的结点必须真的挂在链表上");

    // 重复值时返回第一个
    list.insert(57, 0);
    NODECLASS<int>* first = list.find(57);
    CHECK(first == list.headNode(), "有重复值时应返回第一个匹配的结点");
    CHECK(list.getLength() == 6, "再插一个之后 length 应该是 6");

    // ---- clear：和顺序表的 clear 语义完全不同，必须真的释放 ----
    LLCLASS<int> another;
    int raw2[4] = {3, 1, 4, 1};
    build(another, raw2, 4);
    CHECK(another.getLength() == 4, "clear 测试前先铺 4 个元素");
    another.clear();
    CHECK(another.getLength() == 0, "clear 之后 length 应该归零");
    CHECK(another.empty() == true, "clear 之后应该是空表");
    CHECK(another.headNode() == NULL, "clear 之后 head 必须归 NULL");
    CHECK(another.tailNode() == NULL, "clear 之后 tail 必须归 NULL");
    CHECK(invariants(another), "clear 之后不变式应当成立");
    CHECK(another.insert(8, 0) == true, "clear 之后还必须能继续正常使用");
    CHECK(another.get(0) == 8, "clear 之后插入的元素应该能取回");
    CHECK(another.getLength() == 1, "clear 之后重新插入，length 应该从 0 开始数");

    return 0;
}

// ------------------------------------------------------------
// L2：get 按下标取值
// ------------------------------------------------------------
int test_l2() {
    std::cout << "\n---- L2 按下标取值 ----\n";

    LLCLASS<int> list;
    int raw[5] = {25, 34, 57, 16, 48};
    build(list, raw, 5);

    CHECK(list.get(0) == 25, "get(0) 应该是第一个元素 25（走 0 步）");
    CHECK(list.get(1) == 34, "get(1) 应该是 34（走 1 步）");
    CHECK(list.get(2) == 57, "get(2) 应该是 57");
    CHECK(list.get(4) == 48, "get(4) 应该是末尾元素 48（走 4 步，正好到 tail）");

    // 只有一个元素时：走 0 步就是它
    LLCLASS<int> one;
    one.insert(9, 0);
    CHECK(one.get(0) == 9, "只有一个元素时 get(0) 应该是它本身");

    // 非法下标：应该 exit 而不是返回垃圾值，更不该崩
    CHECK_ADV(list.get(5), "get(length) 应该报错退出（不能读越界内存）");
    CHECK_ADV(list.get(-1), "get(-1) 应该报错退出");

    return 0;
}

// ------------------------------------------------------------
// L3：insert 头 / 中 / 尾
// ------------------------------------------------------------
int test_l3() {
    std::cout << "\n---- L3 插入（头、中、尾）----\n";

    LLCLASS<int> list;

    // --- 空表插入：这是头插和尾插的交叉点，最容易漏 tail ---
    CHECK(list.insert(10, 0) == true, "往空表插入应该成功");
    CHECK(list.getLength() == 1, "插入后 length 应该是 1");
    CHECK(list.headNode() != NULL, "插完之后 head 不该还是 NULL");
    CHECK(list.tailNode() != NULL, "空表插入后 tail 也必须指向这个结点（漏了这里后面必崩）");
    CHECK(list.headNode() == list.tailNode(), "只有一个结点时 head 和 tail 应该是同一个");
    CHECK(tailOf(list).next == NULL, "唯一的结点 next 应该是 NULL");
    CHECK(list.get(0) == 10, "取出来的值应该是 10");

    // --- 在只有一个结点时再尾插，检验 tail 是否正确 ---
    CHECK(list.insert(20, 1) == true, "尾插应该成功");
    CHECK(list.getLength() == 2, "尾插后 length 应该是 2");
    CHECK(headOf(list).data == 10, "表头应该还是 10");
    CHECK(tailOf(list).data == 20, "tail 应该更新成新插入的 20");
    CHECK(tailOf(list).next == NULL, "新的尾结点 next 必须还是 NULL");
    CHECK(list.get(1) == 20, "下标 1 应该是 20");
    CHECK(invariants(list), "两次插入后不变式应当成立");

    // --- 中间插入 ---
    // 当前：10 20，在下标 1 前插入 15 → 10 15 20
    CHECK(list.insert(15, 1) == true, "中间插入应该成功");
    CHECK(dump(list) == "10 15 20", "中间插入后顺序应该是 10 15 20");
    CHECK(tailOf(list).data == 20, "中间插入不该动到 tail");
    CHECK(invariants(list), "中间插入后不变式应当成立");

    // --- 头插 ---
    CHECK(list.insert(5, 0) == true, "头插应该成功");
    CHECK(dump(list) == "5 10 15 20", "头插后顺序应该是 5 10 15 20");
    CHECK(headOf(list).data == 5, "head 应该更新成新结点");
    CHECK(tailOf(list).data == 20, "头插不该动到 tail");
    CHECK(invariants(list), "头插后不变式应当成立");

    // --- 尾插（多条数据） ---
    CHECK(list.insert(25, 4) == true, "在 length 处插入等于追加到末尾");
    CHECK(dump(list) == "5 10 15 20 25", "尾插后顺序应该正确");
    CHECK(tailOf(list).data == 25, "tail 应该跟着走");

    // --- 边界：非法下标必须被拒绝，且不动链表 ---
    int before = list.getLength();
    CHECK(list.insert(99, -1) == false, "index 为负应该返回 false");
    CHECK(list.insert(99, 6) == false, "index 大于 length 应该返回 false");
    CHECK(list.getLength() == before, "被拒绝的插入不该改变 length");
    CHECK(dump(list) == "5 10 15 20 25", "被拒绝的插入不该改变链表内容");
    CHECK(invariants(list), "多次操作后不变式应当仍然成立");

    return 0;
}

// ------------------------------------------------------------
// L4：erase 删头 / 中 / 尾
// ------------------------------------------------------------
int test_l4() {
    std::cout << "\n---- L4 删除（头、中、尾）----\n";

    LLCLASS<int> list;
    int raw[5] = {15, 25, 35, 45, 55};
    build(list, raw, 5);

    // --- 删表头：要改 head 本身 ---
    list.erase(0);
    CHECK(list.getLength() == 4, "删表头后 length 应该是 4");
    CHECK(dump(list) == "25 35 45 55", "删表头后应该是 25 35 45 55");
    CHECK(headOf(list).data == 25, "head 应该指向原来的第二个结点");
    CHECK(tailOf(list).data == 55, "删表头不该影响 tail");
    CHECK(invariants(list), "删表头后不变式应当成立");

    // --- 删中间 ---
    list.erase(1);  // 删掉 35
    CHECK(list.getLength() == 3, "删中间后 length 应该是 3");
    CHECK(dump(list) == "25 45 55", "删中间后应该是 25 45 55");
    CHECK(invariants(list), "删中间后不变式应当成立");

    // --- 删尾结点：必须更新 tail ---
    list.erase(2);
    CHECK(list.getLength() == 2, "删尾后 length 应该是 2");
    CHECK(dump(list) == "25 45", "删尾后应该是 25 45");
    CHECK(tailOf(list).data == 45, "删掉尾结点后 tail 必须前移，不能悬垂");
    CHECK(tailOf(list).next == NULL, "新的 tail 仍然必须停在最后一个结点上");
    CHECK(invariants(list), "删尾后不变式应当成立");

    // --- 删到只剩一个，再删光：head 和 tail 都要归 NULL ---
    list.erase(0);
    CHECK(list.getLength() == 1, "还剩一个元素");
    CHECK(list.headNode() == list.tailNode(), "只剩一个时 head 和 tail 应该是同一个");
    list.erase(0);
    CHECK(list.getLength() == 0, "删光后 length 应该是 0");
    CHECK(list.empty() == true, "删光后应该判定为空表");
    CHECK(list.headNode() == NULL, "删光后 head 必须归 NULL");
    CHECK(list.tailNode() == NULL, "删光后 tail 必须归 NULL（否则 tail 悬垂）");
    CHECK(invariants(list), "删光后不变式应当成立");

    // --- 边界：非法下标什么都不做，也不能崩 ---
    int raw2[3] = {7, 8, 9};
    LLCLASS<int> list2;
    build(list2, raw2, 3);
    list2.erase(-1);
    CHECK(dump(list2) == "7 8 9", "erase 负数下标应该什么都不做");
    CHECK(list2.getLength() == 3, "erase 负数下标不该改变 length");
    list2.erase(3);
    CHECK(dump(list2) == "7 8 9", "erase(length) 应该什么都不做");
    list2.erase(100);
    CHECK(list2.getLength() == 3, "erase 越界不该改变 length");
    CHECK(invariants(list2), "非法删除后不变式应当仍然成立");

    return 0;
}

// ------------------------------------------------------------
// L5：进阶 —— 反转链表、约瑟夫环
// ------------------------------------------------------------
int test_l5() {
    std::cout << "\n---- L5 进阶：反转与约瑟夫环 ----\n";

    // ---------- 反转 ----------
    LLCLASS<int> list;
    int raw[5] = {1, 2, 3, 4, 5};
    build(list, raw, 5);

    list.reverse();
    CHECK(dump(list) == "5 4 3 2 1", "反转之后顺序应该是 5 4 3 2 1");
    CHECK(list.getLength() == 5, "反转不该改变 length");
    CHECK(headOf(list).data == 5, "反转后 head 应该是原来的尾 5");
    CHECK(tailOf(list).data == 1, "反转后 tail 应该是原来的头 1");
    CHECK(tailOf(list).next == NULL, "反转后新的 tail 的 next 必须是 NULL");
    CHECK(invariants(list), "反转后不变式应当成立（tail 很容易忘）");

    // 反转两次应该回到原样
    list.reverse();
    CHECK(dump(list) == "1 2 3 4 5", "反转两次应该回到原样");
    CHECK(tailOf(list).data == 5, "反转两次后 tail 应该回到 5");
    CHECK(invariants(list), "反转两次后不变式应当成立");

    // 单元素反转：head 和 tail 都不变
    LLCLASS<int> one;
    one.insert(42, 0);
    one.reverse();
    CHECK(one.getLength() == 1, "单元素链表反转后长度还是 1");
    CHECK(headOf(one).data == 42, "单元素反转后内容不变");
    CHECK(one.headNode() == one.tailNode(), "单元素反转后 head 和 tail 仍然重合");
    CHECK(invariants(one), "单元素反转后不变式应当成立");

    // 空表反转：不能崩
    LLCLASS<int> emptyOne;
    emptyOne.reverse();
    CHECK(emptyOne.getLength() == 0, "空表反转后仍然是空表");
    CHECK(emptyOne.headNode() == NULL, "空表反转后 head 仍然是 NULL");
    CHECK(emptyOne.tailNode() == NULL, "空表反转后 tail 仍然是 NULL（别忘设成 NULL）");

    // ---------- 约瑟夫环：独立函数，无须创建 LL 对象 ----------
    // 讲义给的核对值：n = 8, m = 3 → 幸存者编号 7（从 1 编号）
    CHECK(JOSEPHUS(8, 3) == 7, "n=8, m=3 的幸存者应该是 7 号");
    CHECK(JOSEPHUS(1, 1) == 1, "只有 1 个人时幸存者就是 1 号");
    CHECK(JOSEPHUS(2, 1) == 2, "n=2, m=1 时第一个出列，剩 2 号");
    CHECK(JOSEPHUS(3, 3) == 2, "n=3, m=3 时幸存者应该是 2 号");
    CHECK(JOSEPHUS(5, 2) == 3, "n=5, m=2 时幸存者应该是 3 号");
    CHECK(JOSEPHUS(41, 3) == 31, "n=41, m=3（历史原题）幸存者应该是 31 号");

    // 独立函数只核对输入、结果和重复调用，不再检查某个 LL 对象的长度。
    CHECK(JOSEPHUS(0, 3) == -1, "人数为 0 时应该返回 -1");
    CHECK(JOSEPHUS(-2, 3) == -1, "人数为负时应该返回 -1");
    CHECK(JOSEPHUS(5, 0) == -1, "报数间隔为 0 时应该返回 -1");
    CHECK(JOSEPHUS(5, -2) == -1, "报数间隔为负时应该返回 -1");
    CHECK(JOSEPHUS(1, 7) == 1, "只有 1 个人时，即使 m 大于 n 也应该返回 1");
    CHECK(JOSEPHUS(5, 7) == 4, "m 大于 n 时需要循环报数，幸存者应该是 4 号");
    CHECK(JOSEPHUS(8, 3) == 7, "多次调用后再次求同一问题，结果应保持一致");

    return 0;
}

int main(int argc, char** argv) {
    // 让输出立刻可见：万一程序中途段错误，也能看到崩溃前跑到哪一条
    std::cout << std::unitbuf;
    std::string level = (argc > 1) ? argv[1] : "all";

    if (level == "all" || level == "1") test_l1();
    if (level == "all" || level == "2") test_l2();
    if (level == "all" || level == "3") test_l3();
    if (level == "all" || level == "4") test_l4();
    if (level == "all" || level == "5") test_l5();

    TEST_END("LL 测试");
}
