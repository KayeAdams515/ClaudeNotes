// ============================================================
//  ll_ref.h —— 单链表 LL 参考实现（结合注释主动对照学习）
// ============================================================
//  主动对照每个函数的指针含义、分支设计和边界；独立复写留到二轮。
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

// 不带头结点：head 就是第一个数据结点，所以头部增删必须更新 head。
// 非空时 tail 是最后一个结点，tail->next==NULL；空表两端均为空、长度为 0。
// 保存 tail 换来 O(1) 尾插；每次删尾、删光、反转都要维护它。
// 本例拥有结点而未实现深拷贝，不要复制整个 LLRef 容器。
// 以下复杂度以结点分配和元素操作为 O(1) 讨论。
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

    NodeRef<T>* headNode() const { return head; }
    NodeRef<T>* tailNode() const { return tail; }

private:
    int length;
    NodeRef<T>* head;
    NodeRef<T>* tail;
};

template <typename T>
// 构造 O(1)：头尾都必须初始化，不能只初始化 head。
LLRef<T>::LLRef() {
    this->head = NULL;
    this->tail = NULL;
    this->length = 0;
}

template <typename T>
// 析构 O(n)：cur 指向尚未处理的第一个结点。
// 先从活结点读取 next，再释放；释放后不能再从 temp 读取任何字段。
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
// 判空与长度读取都是 O(1)，不需要遍历计算。
bool LLRef<T>::empty() { return this->length == 0; }

template <typename T>
int LLRef<T>::getLength() { return this->length; }

template <typename T>
// ptr 是当前检查的结点，循环条件先排除空指针，才能读取 data。
// 返回结点指针，不是下标；返回首个匹配，找不到返回 NULL。最坏 O(n)。
NodeRef<T>* LLRef<T>::find(T x) {
    NodeRef<T>* ptr = this->head;
    while (ptr != NULL) {
        if (ptr->data == x) return ptr;
        ptr = ptr->next;
    }
    return NULL;
}

template <typename T>
// head 已经是下标 0，所以走 index 步；不是 index+1 步。
// 先验证 [0,length-1]，避免遍历越过尾端；最坏 O(n)。
T LLRef<T>::get(int index) {
    if (index < 0 || index >= this->length) exit(EXIT_FAILURE);
    NodeRef<T>* ptr = this->head;
    for (int i = 0; i < index; i++) {
        ptr = ptr->next;
    }
    return ptr->data;
}

template <typename T>
// 分支按“要更新哪个外部入口”组织：头插更新 head，尾插更新 tail，
// 中间插只修改前驱链接。先处理头插，覆盖空表 index==0==length 的重叠情况。
// 头插/尾插 O(1)，中间定位 O(n)，已有前驱后的接链 O(1)。
bool LLRef<T>::insert(T x, int index) {
    if (index < 0 || index > this->length) return false;

    NodeRef<T>* s = new NodeRef<T>;
    // 普通 new 失败通常抛异常；此判空保留课件形式，不是完整异常处理。
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
// 单链表不能从待删结点找到前驱，所以非头部删除要先找 index-1。
// 删头不需要找前驱；删除唯一结点后还要归空 tail。
// 删尾虽有 tail，仍需找它的前驱，所以最坏 O(n)，不能声称删尾 O(1)。
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
// O(n)：真正释放结点，而不是只把 length 设为 0。
// 每轮先推进 cur 再释放 temp；结束后统一恢复头、尾、长度，支持重复清空和复用。
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
// O(n) 时间、O(1) 额外空间。把链表分成“已反转前缀”和“未处理后缀”。
// 每轮开始：prev 是已反转部分的首结点，cur 是未处理部分的首结点。
// nxt 必须保存 cur->next；只保存 cur 本身不能保留即将被覆盖的后继地址。
// old_head 保存未来的尾结点；循环结束 cur==NULL，prev 正好是新头。
// 空表不会进循环；单结点也适用，不需要额外分支。
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

// 独立算法参考实现：不依赖 LLRef 对象。
// 独立函数，自行拥有并释放局部结点，不读取或修改已有 LLRef 对象。
// 编号从 1 开始。最坏 O(n*m) 时间、O(n) 空间；这是链表模拟而非递推优化。
// 此写法与“从报 1 者出发移动 m-2 次”的写法约定不同，不要混用步数。
// 这里 tail 是报数游标，表示报 1 者的前驱；它不再是固定编号的末结点。
inline int josephusRef(int n, int m) {
    if (n <= 0 || m <= 0) return -1;

    // 造一条循环链表，编号 1 .. n
    NodeRef<int>* first = NULL;
    NodeRef<int>* last = NULL;
    for (int i = 0; i < n; i++) {
        NodeRef<int>* node = new NodeRef<int>;
        node->data = i + 1;
        node->next = NULL;
        if (first == NULL) {
            first = node;
            last = node;
        } else {
            last->next = node;
            last = node;
        }
    }
    // 建环前先完成普通链；first 是起点，last 是最后追加的结点。
    last->next = first;   // 首尾相接

    NodeRef<int>* tail = last;   // tail 指向当前起点的前一个
    int size = n;
    // 不变式：tail->next 是本轮报 1 的人。
    // 向前走 m-1 步后，tail->next 是报 m 的人。m==1 时零步，直接删除。
    while (size > 1) {
        for (int i = 0; i < m - 1; i++) {   // 跳过 m-1 个安全的人
            tail = tail->next;
        }
        NodeRef<int>* out = tail->next;       // 数到第 m 个，出列
        tail->next = out->next;
        delete out;
        // 删除后 tail 仍活着，其 next 是下一轮报 1 者，无需额外前进。
        size--;
    }

    // 只剩自环结点；先保存答案再释放。不能 delete 后再读 data。
    int survivor = (int)tail->data;
    delete tail;
    return survivor;
}

#endif  // LL_REF_H
