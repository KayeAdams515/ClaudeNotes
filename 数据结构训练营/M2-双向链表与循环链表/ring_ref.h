// 循环链表参考实现：重点学习空表与单结点如何维持同一套结构约定。
// 先尝试，再对照变量含义与分支；一轮可理解后改写，独立复写留到二轮。
#ifndef DOJO_RING_REF_H
#define DOJO_RING_REF_H

struct RingNode {
    int data;
    RingNode* next;
};

// 不带头结点。空表两端为空；非空时 tail->next==head。
// 单结点 head==tail，且它的 next 指向自己，不能置为空。
// head 表示当前逻辑起点，tail 表示它的前驱；轮转会改变两者的身份。
// 容器独占结点，禁止复制，避免多个对象重复释放同一条环。
class Ring {
public:
    Ring() : head(nullptr), tail(nullptr), length(0) {}
    ~Ring() { clear(); }
    bool empty() const { return length == 0; }
    int getLength() const { return length; }
    const RingNode* headNode() const { return head; }
    const RingNode* tailNode() const { return tail; }
    Ring(const Ring&) = delete;
    Ring& operator=(const Ring&) = delete;

    // O(1)。先让新结点指向原 head，再让旧 tail 指向它，最后更新 tail。
    // 空表不能访问旧 tail，需另建自环；非空表插入不改变当前 head。
    void pushBack(int x) {
        // 花括号按 data、next 顺序初始化；空表 head 为空，下面会改成自环。
        RingNode* node = new RingNode{x, head};
        if (length == 0) {
            head = tail = node;
            node->next = node;
        } else {
            tail->next = node;
            tail = node;
        }
        ++length;
    }

    // O(1)。保存 old 用于释放；先把仍存活的结构接好，再 delete old。
    // 只有一个结点时，old->next 仍是 old，不能照普通情况推进 head。
    bool popFront() {
        if (length == 0) return false;
        RingNode* old = head;
        // 删唯一结点：两端归空；否则新 head 需要被 tail 重新接住。
        if (length == 1) head = tail = nullptr;
        else {
            head = head->next;
            tail->next = head;
        }
        delete old;
        --length;
        return true;
    }

    // 环的链接不变，只移动“从哪里开始看”的入口。
    // head 前进一步时 tail 也前进一步，才能仍是 head 的前驱。
    // 数据编号与起点无关，不用交换 data，也不创建或释放结点。
    void rotate(int steps) {
        if (steps <= 0 || length == 0) return;
        // 完整走一圈回到原处，取模去掉重复圈数；先判空以避免对 0 取模。
        // 时间 O(steps % length)，额外空间 O(1)。
        steps %= length;
        for (int i = 0; i < steps; ++i) {
            head = head->next;
            tail = tail->next;
        }
    }

    // O(n)：每次成功 popFront 删除一个结点；空表返回 false 使循环结束。
    // 不用 while(p!=nullptr) 遍历未断开的环，那样永远不会遇到空指针。
    // 空表反复 clear 也安全，析构复用同一逻辑。
    void clear() {
        while (popFront()) {}
    }

private:
    RingNode* head;
    RingNode* tail;
    int length;
};
#endif
