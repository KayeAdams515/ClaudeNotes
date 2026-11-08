#ifndef DOJO_RING_H
#define DOJO_RING_H

struct RingNode {
    int data;
    RingNode* next;
};

// 不带头结点的单向循环链表。非空时 tail->next == head。
// 这是循环结构练习，不重复写约瑟夫算法。数据是什么编号由调用者决定。
class Ring {
public:
    // 基础状态与观察接口已提供，C1 只写下面四个 TODO。
    Ring() : head(nullptr), tail(nullptr), length(0) {}
    ~Ring() { clear(); }
    bool empty() const { return length == 0; }
    int getLength() const { return length; }
    const RingNode* headNode() const { return head; }
    const RingNode* tailNode() const { return tail; }

    void pushBack(int x);
    bool popFront();
    void rotate(int steps);
    void clear();
    Ring(const Ring&) = delete;
    Ring& operator=(const Ring&) = delete;

private:
    RingNode* head;
    RingNode* tail;
    int length;
};

inline void Ring::pushBack(int x) {
    (void)x;
    // TODO 1：O(1) 尾插。空表时新结点的 next 指向自己。
    // 非空时保持原 head，追加后重新满足 tail->next == head。
}

inline bool Ring::popFront() {
    // TODO 2：空表返回 false；否则删头并返回 true，要求 O(1)。
    // 唯一结点需单独处理；其余情况更新 head 和 tail->next。
    return false;
}

inline void Ring::rotate(int steps) {
    (void)steps;
    // TODO 3：steps <= 0 或空表时不动；否则把 head 和 tail 一起前进 steps 格。
    // 比如 1->2->3，rotate(1) 后从 head 看是 2->3->1。
    // 不创建、不释放、不修改结点数据，也不重接 next；可用 steps % length。
}

inline void Ring::clear() {
    // TODO 4：释放所有结点并恢复空表，可以反复调用 popFront()。
    // 或先断环再逐个释放；不要用 while(p != nullptr) 直接遍历未断开的环。
}

#endif
