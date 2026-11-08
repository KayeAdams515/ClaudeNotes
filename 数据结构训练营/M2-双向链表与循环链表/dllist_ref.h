// 双向链表参考实现：主动比较它如何组织边界，不必把所有写法强行改成同一种。
// 阅读顺序：结构不变式 -> 左右邻居含义 -> 接链/断链 -> 生命周期和复杂度。
// 一轮允许理解后模仿改写，二轮再独立复写。
#ifndef DOJO_DLLIST_REF_H
#define DOJO_DLLIST_REF_H

template <typename T>
struct DNode {
    T data;
    DNode* prior;
    DNode* next;
};

// 不带头结点、非循环。空表两端为空；非空表 head->prior、tail->next 为空。
// 相邻结点需要双向吻合：左结点的 next 和右结点的 prior 互相指向对方。
// 本例不提供容器复制：浅拷贝会让两个对象析构同一批结点，因此显式禁用。
// 下标从 0 开始；元素构造和赋值成本按 O(1) 分析。
template <typename T>
class DLList {
public:
    // 初始化列表在进入构造函数体前初始化成员；空表不需要申请结点。
    DLList() : head(nullptr), tail(nullptr), length(0) {}
    // 复用 clear，使手动清空和析构使用同一套释放逻辑。
    ~DLList() { clear(); }
    bool empty() const { return length == 0; }
    int getLength() const { return length; }
    // const 结点指针用于观察。测试能看链接，但不能通过该结点指针直接赋值字段。
    const DNode<T>* headNode() const { return head; }
    const DNode<T>* tailNode() const { return tail; }
    DLList(const DLList&) = delete;
    DLList& operator=(const DLList&) = delete;

    // O(n)。head 每轮代表未释放部分的起点，next 是临时保存的后路。
    // 整条链都要释放，不必逐轮维护 prior；结束后一次性恢复空表状态。
    void clear() {
        while (head) {
            DNode<T>* next = head->next;
            delete head;
            head = next;
        }
        tail = nullptr;
        length = 0;
    }

    // 将插入拆成两步：先找到左右邻居，再统一接链。
    // left==nullptr 表示插在最前；right==nullptr 表示插在最后。
    // 空表时左右都为空，同一套接链代码自然同时更新 head 和 tail。
    // 头插/尾插 O(1)；中间插入的定位 O(n)，之后的接链 O(1)。
    bool insert(T x, int index) {
        // 先检查再分配；失败不产生结点、不改原链。index==length 是合法尾插。
        if (index < 0 || index > length) return false;
        DNode<T>* right = nullptr;
        DNode<T>* left = nullptr;
        if (index == length) {
            // 同时覆盖空表；空表时 tail 本来就为空，所以 left/right 均为空。
            left = tail; // 尾插不遍历
        } else if (index == 0) {
            right = head;
        } else {
            right = head;
            for (int i = 0; i < index; ++i) right = right->next;
            left = right->prior;
        }
        // 花括号按 DNode 成员声明顺序初始化：data=x、prior=left、next=right。
        // 新结点先保存两边地址，再修改旧结点；避免覆盖仍需使用的链接。
        DNode<T>* node = new DNode<T>{x, left, right};
        // 有左邻居就更新它的 next；没有左邻居，说明新结点就是 head。
        if (left) left->next = node;
        else head = node;
        // 有右邻居就更新它的 prior；没有右邻居，说明新结点就是 tail。
        // 两个判断独立执行，不写成 else if，才能覆盖空表的“两端都更新”。
        if (right) right->prior = node;
        else tail = node;
        ++length;
        return true;
    }

    // 删除同样分别处理左右两侧，无需列举“头/尾/中间/唯一结点”四大分支。
    // 按下标定位最坏 O(n)，已有结点后的断链 O(1)；删尾用 tail 可直接定位。
    void erase(int index) {
        if (index < 0 || index >= length) return;
        DNode<T>* node = head;
        if (index == length - 1) node = tail;
        else for (int i = 0; i < index; ++i) node = node->next;
        // 修复左侧：有前驱就跨过 node；否则新的 head 是 node 的后继。
        if (node->prior) node->prior->next = node->next;
        else head = node->next;
        // 修复右侧：有后继就让它认新前驱；否则新的 tail 是 node 的前驱。
        // 唯一结点两边都为空，因此两个 else 分别将 head/tail 置空，自然覆盖边界。
        if (node->next) node->next->prior = node->prior;
        else tail = node->prior;
        // 必须接好两侧之后再释放；delete 后不能再读取 node 的 prior/next。
        delete node;
        --length;
    }

private:
    DNode<T>* head;
    DNode<T>* tail;
    int length;
};
#endif
