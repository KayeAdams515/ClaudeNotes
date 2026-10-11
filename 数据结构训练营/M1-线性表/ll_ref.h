// ============================================================
//  ll_ref.h —— 单链表 LL 参考答案（卡住了才看）
// ============================================================
//  看完记得关掉，回到 ll.h 自己默写一遍。
//  特别留意三处：头插时 tail 的处理、删尾时 tail 的更新、reverse 时 tail 的更新。
// ------------------------------------------------------------

#ifndef LL_REF_H
#define LL_REF_H

#include <cstdlib>

template <typename T>
struct NodeRef {
    T data;
    NodeRef* next;
};

template <typename T>
class LLRef {
public:
    LLRef();
    ~LLRef();

    bool empty();
    int getLength();

    T get(int index);
    NodeRef<T>* find(T x);

    bool insert(T x, int index);
    void erase(int index);
    void clear();

    void reverse();
    int josephus(int n, int m);

    NodeRef<T>* headNode() const { return head; }
    NodeRef<T>* tailNode() const { return tail; }

private:
    int length;
    NodeRef<T>* head;
    NodeRef<T>* tail;
};

template <typename T>
LLRef<T>::LLRef() {
    this->head = NULL;
    this->tail = NULL;
    this->length = 0;
}

template <typename T>
LLRef<T>::~LLRef() {
    NodeRef<T>* cur = this->head;
    while (cur != NULL) {
        NodeRef<T>* temp = cur;   // 先留住后路
        cur = cur->next;
        delete temp;
    }
    this->head = NULL;
    this->tail = NULL;
    this->length = 0;
}

template <typename T>
bool LLRef<T>::empty() { return this->length == 0; }

template <typename T>
int LLRef<T>::getLength() { return this->length; }

template <typename T>
NodeRef<T>* LLRef<T>::find(T x) {
    NodeRef<T>* ptr = this->head;
    while (ptr != NULL) {
        if (ptr->data == x) return ptr;
        ptr = ptr->next;
    }
    return NULL;
}

template <typename T>
T LLRef<T>::get(int index) {
    if (index < 0 || index >= this->length) exit(EXIT_FAILURE);
    NodeRef<T>* ptr = this->head;
    for (int i = 0; i < index; i++) {
        ptr = ptr->next;
    }
    return ptr->data;
}

template <typename T>
bool LLRef<T>::insert(T x, int index) {
    if (index < 0 || index > this->length) return false;

    NodeRef<T>* s = new NodeRef<T>;
    if (!s) return false;
    s->data = x;
    s->next = NULL;

    if (index == 0) {                  // 头插（含空表的情况）
        s->next = this->head;
        this->head = s;
        if (this->tail == NULL) this->tail = s;   // 空表时 tail 也要指过来
    } else if (index == this->length) {           // 尾插：有 tail 所以 O(1)
        this->tail->next = s;
        this->tail = s;
    } else {                                      // 中间插
        NodeRef<T>* p = this->head;
        for (int i = 0; i < index - 1; i++) {     // 停在前驱
            p = p->next;
        }
        s->next = p->next;   // 先连
        p->next = s;         // 后断
    }
    this->length++;
    return true;
}

template <typename T>
void LLRef<T>::erase(int index) {
    if (index < 0 || index >= this->length) return;

    if (index == 0) {                 // 删头结点：要改 head 本身
        NodeRef<T>* ptr = this->head;
        this->head = this->head->next;
        delete ptr;
        if (this->head == NULL) this->tail = NULL;   // 删完空了，tail 也必须归位
    } else {                          // 删其它结点
        NodeRef<T>* p = this->head;
        for (int i = 0; i < index - 1; i++) {
            p = p->next;
        }
        NodeRef<T>* ptr = p->next;    // 先记住要删的
        p->next = ptr->next;          // 跨过它
        delete ptr;                   // 最后才删
        if (p->next == NULL) this->tail = p;   // 删的正好是尾结点，更新 tail
    }
    this->length--;
}

template <typename T>
void LLRef<T>::clear() {
    NodeRef<T>* cur = this->head;
    while (cur != NULL) {
        NodeRef<T>* temp = cur;
        cur = cur->next;
        delete temp;
    }
    this->head = NULL;
    this->tail = NULL;
    this->length = 0;
}

template <typename T>
void LLRef<T>::reverse() {
    NodeRef<T>* prev = NULL;
    NodeRef<T>* cur = this->head;
    NodeRef<T>* old_head = this->head;

    while (cur != NULL) {
        NodeRef<T>* nxt = cur->next;  // 留住后路
        cur->next = prev;             // 掉头
        prev = cur;                   // 前进
        cur = nxt;
    }

    this->head = prev;     // 原来的尾成了新的头
    this->tail = old_head; // 原来的头成了新的尾（空表时 old_head 是 NULL，正好）
}

template <typename T>
int LLRef<T>::josephus(int n, int m) {
    if (n <= 0 || m <= 0) return -1;

    // 造一条循环链表，编号 0 .. n-1
    NodeRef<T>* first = NULL;
    NodeRef<T>* last = NULL;
    for (int i = 0; i < n; i++) {
        NodeRef<T>* node = new NodeRef<T>;
        node->data = (T)i;
        node->next = NULL;
        if (first == NULL) {
            first = node;
            last = node;
        } else {
            last->next = node;
            last = node;
        }
    }
    last->next = first;   // 首尾相接

    NodeRef<T>* tail = last;   // tail 指向当前起点的前一个
    int size = n;
    while (size > 1) {
        for (int i = 0; i < m - 1; i++) {   // 跳过 m-1 个安全的人
            tail = tail->next;
        }
        NodeRef<T>* out = tail->next;       // 数到第 m 个，出列
        tail->next = out->next;
        delete out;
        size--;
    }

    int survivor = (int)tail->data;
    delete tail;
    return survivor;
}

#endif  // LL_REF_H
