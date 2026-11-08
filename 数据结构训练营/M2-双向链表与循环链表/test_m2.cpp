#include <iostream>
#include <string>
#include <vector>
#include <random>
#include "testkit.h"
#ifdef USE_REF
#include "dllist_ref.h"
#include "ring_ref.h"
#else
#include "dllist.h"
#include "ring.h"
#endif

// 有界遍历：链接成环或长度错误时返回 false，避免检查器自己无限循环。
bool matches(const DLList<int>& list, const std::vector<int>& expected) {
    const int n = static_cast<int>(expected.size());
    if (list.getLength() != n || list.empty() != (n == 0)) return false;
    if (n == 0) return !list.headNode() && !list.tailNode();
    if (!list.headNode() || !list.tailNode()) return false;
    if (list.headNode()->prior || list.tailNode()->next) return false;
    const DNode<int>* p = list.headNode();
    const DNode<int>* previous = nullptr;
    for (int i = 0; i < n; ++i) {
        if (!p || p->data != expected[i] || p->prior != previous) return false;
        previous = p;
        p = p->next;
    }
    if (p || previous != list.tailNode()) return false;
    p = list.tailNode();
    const DNode<int>* next = nullptr;
    for (int i = n - 1; i >= 0; --i) {
        if (!p || p->data != expected[i] || p->next != next) return false;
        next = p;
        p = p->prior;
    }
    return !p && next == list.headNode();
}

bool matches(const Ring& ring, const std::vector<int>& expected) {
    const int n = static_cast<int>(expected.size());
    if (ring.getLength() != n || ring.empty() != (n == 0)) return false;
    if (n == 0) return !ring.headNode() && !ring.tailNode();
    if (!ring.headNode() || !ring.tailNode()) return false;
    if (ring.tailNode()->next != ring.headNode()) return false;
    const RingNode* p = ring.headNode();
    for (int i = 0; i < n; ++i) {
        if (!p || (i > 0 && p == ring.headNode()) || p->data != expected[i]) return false;
        if (i == n - 1 && p != ring.tailNode()) return false;
        p = p->next;
    }
    return p == ring.headNode();
}

// 计数对象：观察 clear、erase 和析构是否真正销毁了结点中的元素。
struct Tracked {
    inline static int live = 0;
    int value;
    Tracked(int x = 0) : value(x) { ++live; }
    Tracked(const Tracked& x) : value(x.value) { ++live; }
    Tracked& operator=(const Tracked&) = default;
    ~Tracked() { --live; }
};

void d1() {
    std::cout << "\n---- D1 双向链表骨架 ----\n";
    DLList<int> list;
    CHECK(list.empty(), "新表应该为空");
    CHECK(list.getLength() == 0, "新表长度为 0");
    CHECK(!list.headNode() && !list.tailNode(), "空表头尾指针都为空");
    list.clear();
    list.clear();
    CHECK(matches(list, {}), "空表反复 clear 后仍保持完整空表状态");
}

void d2() {
    std::cout << "\n---- D2 插入：正向、反向和两端 ----\n";
    DLList<int> list;
    CHECK(!list.insert(99, -1), "负下标插入返回 false，不结束程序");
    CHECK(!list.insert(99, 1), "空表不能在下标 1 插入");
    CHECK(matches(list, {}), "失败的插入不改变空表");
    CHECK(list.insert(20, 0), "空表插入 20 成功");
    CHECK(matches(list, {20}), "单结点的头尾相同，prior/next 都为空");
    CHECK(list.insert(10, 0), "头插 10 成功");
    CHECK(matches(list, {10,20}), "头插后原表头的 prior 也要更新");
    CHECK(list.insert(40, 2), "index==length 时尾插成功");
    CHECK(matches(list, {10,20,40}), "尾插后新 tail 的 prior 正确");
    CHECK(list.insert(30, 2), "中间插入 30 成功");
    CHECK(matches(list, {10,20,30,40}), "中间插入的四条链接全部接好");
    CHECK(list.insert(20, 2), "允许重复值");
    CHECK(matches(list, {10,20,20,30,40}), "重复值按位置插入，不能按值决定位置");
    CHECK(!list.insert(99, 6), "超过 length 的插入被拒绝");
    CHECK(matches(list, {10,20,20,30,40}), "失败插入不改变正反向顺序");
    list.clear();
    CHECK(matches(list, {}), "非空 clear 后头尾和长度都归位");
    CHECK(list.insert(7, 0), "clear 之后仍能插入");
    CHECK(matches(list, {7}), "clear 之后复用正常");
    CHECK(Tracked::live == 0, "计数元素初始没有存活对象");
    {
        DLList<Tracked> objects;
        objects.insert(Tracked(1), 0);
        objects.insert(Tracked(2), 1);
        CHECK(Tracked::live == 2, "两个结点各持有一个元素");
        objects.clear();
        CHECK(Tracked::live == 0, "clear 真正释放全部结点");
        objects.insert(Tracked(3), 0);
    }
    CHECK(Tracked::live == 0, "析构自动释放仍留在表中的结点");
}

void d3() {
    std::cout << "\n---- D3 删除与混合操作 ----\n";
    DLList<int> list;
    list.erase(0);
    CHECK(matches(list, {}), "空表删除不退出、不改变状态");
    for (int i = 1; i <= 4; ++i) list.insert(i, i-1);
    CHECK(matches(list, {1,2,3,4}), "先插入四个结点");
    list.erase(-1);
    list.erase(4);
    CHECK(matches(list, {1,2,3,4}), "非法删除不改变链表");
    list.erase(1);
    CHECK(matches(list, {1,3,4}), "删中间同时修复两侧链接");
    list.erase(0);
    CHECK(matches(list, {3,4}), "删头后新 head 的 prior 为空");
    list.erase(1);
    CHECK(matches(list, {3}), "删尾后新 tail 的 next 为空");
    list.erase(0);
    CHECK(matches(list, {}), "删除唯一结点，头尾都归空");
    list.insert(8, 0);
    CHECK(matches(list, {8}), "删光后可以重新插入");
    list.clear();

    std::mt19937 random(20261025);
    std::vector<int> expected;
    bool all_ok = true;
    for (int step = 0; step < 200; ++step) {
        if (expected.empty() || random() % 2 == 0) {
            const int index = random() % (expected.size() + 1);
            const int value = static_cast<int>(random() % 11);
            const bool inserted = list.insert(value, index);
            expected.insert(expected.begin() + index, value);
            if (!inserted) { all_ok = false; break; }
        } else {
            const int index = random() % expected.size();
            list.erase(index);
            expected.erase(expected.begin() + index);
        }
        if (!matches(list, expected)) { all_ok = false; break; }
    }
    CHECK(all_ok, "200 次固定种子的增删，逐步核对正反向顺序、长度和链接");
    {
        DLList<Tracked> objects;
        objects.insert(Tracked(1), 0);
        objects.insert(Tracked(2), 1);
        objects.erase(0);
        CHECK(Tracked::live == 1, "erase 释放被删除结点中的元素");
    }
    CHECK(Tracked::live == 0, "剩余结点由析构释放");
}

void c1() {
    std::cout << "\n---- C1 循环链表：尾插、轮转、删头、清空 ----\n";
    Ring ring;
    CHECK(matches(ring, {}), "循环链表空表的头尾都为空");
    CHECK(!ring.popFront(), "空表删头返回 false");
    ring.rotate(3);
    ring.clear();
    CHECK(matches(ring, {}), "空表旋转、清空安全");
    ring.pushBack(1);
    CHECK(matches(ring, {1}), "单结点首尾重合，next 指向自己");
    ring.rotate(7);
    CHECK(matches(ring, {1}), "单结点轮转保持自环");
    ring.pushBack(2);
    ring.pushBack(3);
    CHECK(matches(ring, {1,2,3}), "尾插后从 head 走一圈恰好回到 head");
    const RingNode* first = ring.headNode();
    const RingNode* second = first ? first->next : nullptr;
    const RingNode* third = second ? second->next : nullptr;
    ring.rotate(1);
    CHECK(matches(ring, {2,3,1}), "轮转一格后 head 与 tail 一起前进");
    CHECK(ring.headNode() == second && ring.tailNode() == first,
          "轮转保留原结点，不能复制数据冒充指针移动");
    CHECK(first && second && third && first->next == second && second->next == third && third->next == first,
          "轮转不改动 next 链接");
    ring.rotate(6);
    CHECK(matches(ring, {2,3,1}), "整圈轮转不改变逻辑顺序");
    ring.rotate(5);
    CHECK(matches(ring, {1,2,3}), "超过一圈的轮转也正确");
    ring.rotate(0);
    ring.rotate(-1);
    CHECK(matches(ring, {1,2,3}), "按约定，零和负步数不动");
    CHECK(ring.popFront(), "删头成功");
    CHECK(matches(ring, {2,3}), "删头后 tail->next 指向新的 head");
    ring.popFront();
    CHECK(matches(ring, {3}), "删到单结点时仍是自环");
    ring.popFront();
    CHECK(matches(ring, {}), "删掉唯一结点后头尾归空");
    CHECK(!ring.popFront(), "删光后再次删除返回 false");
    ring.pushBack(8);
    ring.pushBack(9);
    ring.rotate(1);
    ring.pushBack(10);
    CHECK(matches(ring, {9,8,10}), "轮转后尾插仍从当前 head 维护正确环");
    ring.clear();
    ring.clear();
    CHECK(matches(ring, {}), "非空环能清空，且允许重复清空");
    ring.pushBack(42);
    CHECK(matches(ring, {42}), "清空后可重新建立自环");
    // 留下非空环，由析构调用 clear。
}

int main(int argc, char** argv) {
    std::cout << std::unitbuf;
    const std::string level = argc > 1 ? argv[1] : "all";
    if (level != "all" && level != "1" && level != "2" && level != "3" && level != "4") {
        std::cerr << "关卡只能是 all、1、2、3、4\n";
        return 2;
    }
    if (level == "all" || level == "1") d1();
    if (level == "all" || level == "2") d2();
    if (level == "all" || level == "3") d3();
    // 循环链表为选做，不计入默认 all；只有明确选择第 4 关才运行。
    if (level == "4") c1();
    TEST_END("M2 双向链表与循环链表");
}
