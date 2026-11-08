// ============================================================
//  ll.h —— 单链表 LL（脚手架：你要写的部分在这里）
// ============================================================
//
//  对应讲义：[[C2.5 单链表实现]]，接口定义见 [[C2.3 线性表 ADT]]
//
//  【本课的三个重要约定，先记住再动手】
//  1. 【不带头结点】。head 直接指向首元结点，所以空表就是 head == NULL。
//     "在表头插入/删除"必须特判，因为要改的是 head 这个变量本身。
//     （有头结点的话代码能统一，但本课老师明确选了不带头结点这条路。）
//  2. 【有尾指针 tail】。有了它，尾插从 O(n) 变成 O(1)。
//     代价是：每个会改动表尾的操作，都必须记得同步 tail。
//  3. 【先连后断】。插入时先让新结点抓住后面的链，再让前驱改口指向新结点。
//     顺序反了，后半段链表就永久丢失。
//
//  【贯穿全文的一个不变式 invariant】
//      链表为空  ⟺  head == NULL 且 tail == NULL 且 length == 0
//      链表非空  ⟺  tail->next == NULL（tail 真的指向最后一个结点）
//    真链表会出现 tail 悬垂、length 对不上这类问题，
//    这个脚手架用带下标的链表（位置就是下标）回避了它们，
//    但每一关的测试都会检查 tail 和 length 是否正确——
//    这正是本模块最容易失分的地方。
// ------------------------------------------------------------

#ifndef LL_H
#define LL_H
#include <iostream>
#include <utility>
#include <cstdlib>

template <typename T>
struct Node
{
    T data;     // 数据域
    Node *next; // 指针域：下一结点的地址
};

template <typename T>
class LL
{
public:
    LL();  // 初始化：head = tail = NULL, length = 0
    ~LL(); // 销毁：逐个 delete，注意"留住后路"

    bool empty();    // 判空
    int getLength(); // 求长度

    T get(int index);   // Retrieve：取第 index 个元素的数据
    Node<T> *find(T x); // Find：返回第一个值为 x 的【结点指针】，找不到返回 NULL

    bool insert(T x, int index); // 在下标 index 之前插入
    void erase(int index);       // 删除下标 index 处的结点

    void clear(); // 清空（必须真的释放每个结点！）

    // ---- 进阶关（L5）----
    void reverse(); // 就地反转整条链表

    // ---- 只读访问器（已给你实现，不用改）----
    // 真实项目不暴露 head/tail，否则外面能随意改动内部指针；
    // 但测试要核对"尾巴有没有接对"，所以给两个"看得见、改不动"的入口。
    Node<T> *headNode() const { return head; }
    Node<T> *tailNode() const { return tail; }

private:
    int length;
    Node<T> *head;
    Node<T> *tail;
};

// ============================================================
//  以下是实现。把每个 TODO 换成真正的代码。
// ============================================================

// ---------- L1：骨架、遍历、查找 ----------

template <typename T>
LL<T>::LL()
{
    length = 0;
    head = nullptr;
    tail = nullptr;
    // TODO 1: 空表的三个成员怎么初始化？
    // 想一想：head 和 tail 都要初始化吗？
    //
    // 下面三行是【临时占位】，只是为了让你在写完之前程序也能安全地跑起来、
    // 看到一条条红灯，而不是一上来就段错误。
    // 写完 TODO 1 之后，请把这三行删掉，改成你自己写的代码。
}

template <typename T>
LL<T>::~LL()
{
    Node<T> *p = head;
    Node<T> *temp = nullptr;
    while (p != nullptr)
    {
        temp = p->next;
        delete p;
        p = temp;
    }
    length = 0;
    p = nullptr;
    tail = nullptr;
    head = nullptr;
    // TODO 2: 逐个释放所有结点。
    // ★ 关键：不能直接 delete head; head = head->next;
    //   因为 delete 之后 head 指向的内存已经没了，再读 head->next 就是悬垂指针。
    //   正确做法：先用一个临时指针【留住后路】，再删。
    // 释放完把 head、tail、length 都归位。
    //
    // 注意：在你写完 insert 之前，链表里不会有结点，这里先留空是安全的；
    //       但一旦 insert 能造出结点，这个析构不写就是内存泄漏。
}

template <typename T>
bool LL<T>::empty()
{

    return length == 0;
}

template <typename T>
int LL<T>::getLength()
{
    return length;
    // TODO 4: 返回长度（O(1)，因为 length 一直被维护着）。
    // return 0;
}

template <typename T>
Node<T> *LL<T>::find(T x)
{
    Node<T> *p = head;
    while (p)
    {
        if (p->data == x)
        {
            return p;
        }
        p = p->next;
    }
    // TODO 5: 从头遍历，找到值等于 x 的结点就返回它的指针；走完还没找到返回 NULL。
    // ★ 循环条件必须是 ptr != NULL —— 忘了判 NULL 就是段错误。
    // ★ 这是遍历链表的【标准写法】，后面每一关都要用到。
    return NULL;
}

// ---------- L2：定位 ----------

template <typename T>
T LL<T>::get(int index)
{
    if (index < 0 || index >= length)
    {
        exit(EXIT_FAILURE);
    }
    Node<T> *p = head;
    for (int i = 0; i < index; i++)
    {
        p = p->next;
    }
    return p->data;

    // TODO 6: 取下标 index 处结点里的数据。
    // (a) 合法性：index < 0 或 index >= length 时 exit(EXIT_FAILURE) 结束程序
    // (b) 从 head 出发，走 index 步（不是 index+1 步，head 自己就是下标 0）
    // ★ 差一错误高发区：循环写成 i < index 还是 i <= index，差一步就到 NULL 了
    //
    // 下面这行是【临时占位】，防止你在写完之前程序段错误。
    // 写完 TODO 6 之后请删掉它。
    // if (this->head == NULL) return T();
    // return T();
}

// ---------- L3：插入 ----------

template <typename T>
bool LL<T>::insert(T x, int index)
{
    if (index < 0 || index > length) // 注意这里要支持尾插，即认为index等于length也合法
    {
        return false;
    }
    Node<T> *nd = new Node<T>();
    nd->data = x;
    nd->next = nullptr;
    Node<T> *p = head;
    if (index == 0)
    {
        nd->next = head;
        head = nd;
        if (length == 0)
        {
            tail = nd;
        }
    }

    else
    {
        for (int i = 0; i < index - 1; i++)
        {
            p = p->next;
        }
        if (p->next == nullptr)
        {
            p->next = nd;
            tail = nd;
        }
        else
        {
            nd->next = p->next;
            p->next = nd;
        }
    }
    length++;

    return true;

    // TODO 7: 在下标 index 之前插入值为 x 的新结点。
    // 步骤：
    //   (a) 合法性：index < 0 或 index > length 时返回 false
    //       （index == length 表示追加到末尾，合法；这里和 SqList.insert 口径一致）
    //   (b) 先 new 出新结点 s，填好 s->data
    //   (c) 分三种情况，这就是"不带头结点"的代价：
    //       · 头插（index == 0）：s->next = head; head = s;
    //         ★ 别忘空表时 tail 也要指向 s（否则后面尾插必崩）
    //       · 尾插（index == length）：用 tail 可以 O(1) 完成，不用遍历
    //         ★ 空表时 tail 是 NULL，直接写 tail->next 会崩 —— 要和头插合并处理
    //       · 中间插：从 head 走 index-1 步找到【前驱】p，然后
    //             s->next = p->next;   // 先连
    //             p->next = s;         // 后断
    //         ★ 这两句不能交换，交换就丢失后半段链表
    //   (d) length++
    return false;
}

// ---------- L4：删除 ----------

template <typename T>
void LL<T>::erase(int index)
{

    if (index < 0 || index >= length)
    {
        return;
    }
    Node<T> *p = head;
    Node<T> *temp = nullptr;

    if (index == 0)
    {
        temp = head;
        head = head->next;
        delete temp;
        temp = nullptr;
        if (head == nullptr)
        {
            tail = nullptr;
        }
    }
    else
    {
        for (int i = 0; i < index - 1; i++)
        {
            p = p->next;
        }
        temp = p->next;
        p->next = temp->next;
        delete temp;
        temp = nullptr;
        if (p->next == nullptr)
        {
            tail = p;
        }
    }
    length--;
    // TODO 8: 删除下标 index 处的结点。
    // (a) 合法性：index < 0 或 index >= length 时直接 return
    // (b) 删【头结点】：要改 head 本身。
    //     ★ 如果删完表空了，tail 也必须置 NULL（否则 tail 悬垂）
    // (c) 删【其它结点】：走到前驱 p（走 index-1 步），
    //         Node<T>* ptr = p->next;   // 先记住要删的那个
    //         p->next = ptr->next;      // 跨过它
    //         delete ptr;               // 最后才删
    //     ★ 顺序错了就是访问已释放内存
    //     ★ 如果删的是【尾结点】（p->next == NULL），别忘了把 tail 更新成 p
    // (d) length--
}

// ---------- 收尾：清空 ----------

template <typename T>
void LL<T>::clear()
{
    Node<T> *p = head;
    Node<T> *temp = nullptr;
    while (p)
    {
        temp = p;
        p = p->next;
        delete temp;
    }
    length = 0;
    head = nullptr;
    tail = nullptr;
    // TODO 9: 释放所有结点，把表恢复到刚构造完的状态。
    // ★ 和 SqList::clear() 完全不同：顺序表只是 length = 0（数据还在内存里），
    //   链表必须真的 delete 每个结点，否则内存泄漏。
    // 提示：析构函数里那段代码可以抽出来复用，但这里是手写练习，就再写一遍。
}

// ---------- L5：进阶 ----------

template <typename T>
void LL<T>::reverse()
{
    Node<T> *pre = nullptr;
    Node<T> *cur = head;
    while (cur)
    {
        Node<T> *temp = cur->next;
        cur->next = pre;
        pre = cur;
        cur = temp;
    }
    std::swap(head, tail);
    // TODO 10: 就地反转整条链表，不能新建结点。
    // 标准三指针写法：
    //   Node<T>* prev = NULL;
    //   Node<T>* cur  = head;
    //   while (cur != NULL) {
    //       Node<T>* nxt = cur->next;  // 先留住后路
    //       cur->next = prev;          // 掉头
    //       prev = cur;                // 两根指针一起前进
    //       cur = nxt;
    //   }
    // 循环结束后：新的 head 是谁？新的 tail 又是谁？
    //   ★ 别忘了 tail——这正是"维护两个指针"的代价，反转也要照顾 tail。
    // 试着先自己画一遍三个指针的移动过程，再动手写。
}

// 独立算法：只依赖 n、m，不依赖任何已有 LL 对象。
// 定义放在头文件中，因此用 inline 避免多个源文件包含时重复定义。
inline int josephus(int n, int m)
{
    if (n <= 0 || m <= 0)
    {
        return -1;
    }
    if (n == 1)
    {
        return 1;
    }
    // n>=2
    Node<int> *head = nullptr;
    Node<int> *tail = nullptr;
    Node<int> *p = new Node<int>();
    int length = n;
    p->data = 1;
    head = p;
    for (int i = 1; i < n; i++)
    {
        Node<int> *temp = p;
        p = new Node<int>;
        temp->next = p;
        p->data = i + 1;
    }
    tail = p;
    tail->next = head;

    p = head; // p is the cursor;
    while (length > 1)
    {
        Node<int> *toBeExcuted = nullptr;
        if (m == 1)
        {
            toBeExcuted = head;
        }
        else
        {
            for (int i = 0; i < m - 2; i++)
            {
                p = p->next;
            }
            Node<int> *temp = p->next;
            p->next = p->next->next;
            toBeExcuted = temp;
        }

        std::cout << toBeExcuted->data << "is executed.";

        if (toBeExcuted == head)
        {
            head = toBeExcuted->next;
            tail->next = head;
        }
        else if (toBeExcuted == tail)
        {
            tail = p;
        }
        delete toBeExcuted;
        toBeExcuted = nullptr;
        if (m == 1)
        {
            p = head; // head 已更新为下一位
        }
        else
        {
            p = p->next; // p 是仍然存在的前驱
        }
        length--;
    }
    int ans = head->data;
    delete head;
    head = nullptr;
    return ans;

    // TODO 11: 约瑟夫环，返回幸存者的编号（从 1 开始）；n 或 m 非正时返回 -1。
    // n = 8, m = 3 时答案应该是 7（也就是第 7 个人）。
    //
    // 思路（讲义 [[C2.5 单链表实现]] 十三节）：
    //   1. 造一条【循环】链表：n 个结点，编号 1..n，
    //      最后让 tail->next = head，首尾接上
    //   2. 让 tail 指向"当前起点"的前一个结点
    //   3. 循环直到只剩一个结点：
    //        先数 m-1 步跳过安全的人（tail 往后挪 m-1 次）
    //        然后删掉 tail->next（数到第 m 个的人）
    //   4. 剩下那个结点的 data 就是答案，释放它之后返回
    //
    // ★ 若用 circle 管理结点，接环后须在返回前恢复普通链表结构及正确的
    //   head/tail/length；不要手动释放结点后又让 circle 析构重复释放。
    //   也可自行用局部 Node<int>* first/last 建环并负责释放，不使用 LL 对象。
    // ★ 循环链表的终止条件不能用 ptr == NULL（永远不成立，会死循环），
    //   要用"剩几个结点"来数。
    // ★ 数 m-1 步时别数错：从当前起点开始数 1，数到 m 出列，
    //   所以起点本身算第 1 个，要挪 m-1 次才对。
    return -1;
}

#endif // LL_H
