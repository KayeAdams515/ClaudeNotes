// ============================================================
//  sqlist_ref.h —— 顺序表 SqList 参考实现（结合注释主动对照学习）
// ============================================================
//  先尝试，再逐函数比较：边界、变量含义、搬移方向、复杂度。
//  一轮理解后可模仿改写；独立复写留到二轮。
// ------------------------------------------------------------

#ifndef SQLIST_REF_H
#define SQLIST_REF_H

#include <cstdlib>

// 思路：用“数组 + 有效长度”表示线性表。只有 [0,length) 是逻辑元素。
// 始终保持 0 <= length <= capacity；已分配空间不等于已有数据。
// 教学约定：capacity 非负；T 支持默认构造、赋值和相等比较。
// 本例拥有动态数组，但未实现深拷贝；不要复制此容器，否则可能重复释放。
// 这是一份课程实现，不是可直接替代 vector 的完整通用容器。
template <typename T>
class SqListRef {
public:
    explicit SqListRef(int capacity);
    ~SqListRef();

    bool empty();
    int getLength();
    int getCapacity();

    T get(int index);
    int find(T x);

    bool insert(T x, int index);
    void erase(int index);

    void clear();

private:
    T* elem;
    int capacity;
    int length;
};

template <typename T>
// 构造 O(capacity)（一般 T 的数组构造）：申请存储与设定长度是两件事。
// 参数 capacity 与成员同名，用 this-> 指定成员，避免声明局部 elem 将成员屏蔽。
SqListRef<T>::SqListRef(int capacity) {
    this->capacity = capacity;
    this->elem = new T[capacity];
    // 保留课件判空形式：普通 new 分配失败默认抛异常，通常不会返回空指针。
    // 只有使用 nothrow new 时，分配失败判空才是主要处理方式。
    if (!this->elem) exit(EXIT_FAILURE);
    this->length = 0;
}

template <typename T>
// new[] 与 delete[] 成对；这里销毁整个数组，不能只用 delete。
// delete[] 空指针本来就安全，外层 if 不是必需条件。
SqListRef<T>::~SqListRef() {
    if (this->elem) delete[] this->elem;
    this->elem = NULL;
}

template <typename T>
// empty、getLength、getCapacity 都只读成员，均为 O(1)。
bool SqListRef<T>::empty() { return this->length == 0; }

template <typename T>
int SqListRef<T>::getLength() { return this->length; }

template <typename T>
int SqListRef<T>::getCapacity() { return this->capacity; }

template <typename T>
// O(1) 逻辑清空：保留容量和整个数组，后续 insert 可以覆盖旧位置。
// 它不会立即销毁数组中 T 的对象；与逐结点释放的链表 clear 不同。
void SqListRef<T>::clear() { this->length = 0; }

template <typename T>
// 按长度检查而非容量：容量 10、长度 3 时，get(3) 仍应拒绝。
// 合法下标 [0,length-1]，计算数组地址直接取值，O(1)（不计 T 的复制成本）。
T SqListRef<T>::get(int index) {
    if (index < 0 || index >= this->length) exit(EXIT_FAILURE);
    return this->elem[index];
}

template <typename T>
// 从左到右查找，第一个相等就返回，因此重复值返回首个位置。
// 全部检查后返回 -1；最坏 O(n)，没有命中时也必须走完整个有效区间。
int SqListRef<T>::find(T x) {
    for (int i = 0; i < this->length; i++) {
        if (this->elem[i] == x) return i;
    }
    return -1;
}

template <typename T>
// 插入是“选一个空隙”，有 length+1 个位置，允许 index==length。
// 先检查再修改，失败时表完全不变；当前版本满表返回 false，不自动扩容。
// 最坏 O(n)，尾插 O(1)；以下按元素赋值为 O(1) 分析。
bool SqListRef<T>::insert(T x, int index) {
    if (index < 0 || index > this->length) return false;
    if (this->length == this->capacity) return false;
    // i 是本轮写入位置，从空闲的 elem[length] 开始。
    // 右移必须从后往前，否则会覆盖尚未搬走的源数据。
    // 最后一轮把旧 elem[index] 搬到 index+1，再把 x 放进 index。
    for (int i = this->length; i > index; i--) {
        this->elem[i] = this->elem[i - 1];
    }
    this->elem[index] = x;
    this->length++;
    return true;
}

template <typename T>
// 删除是“选已有元素”，不允许 index==length。非法下标忽略。
// 左移从前往后：第一个后继覆盖被删位置，后面的源数据还没被破坏。
// 最坏 O(n)，删尾 O(1)。不用清理旧末位，长度减一后该位置不可被 get 访问。
void SqListRef<T>::erase(int index) {
    if (index < 0 || index >= this->length) return;
    for (int i = index + 1; i < this->length; i++) {
        this->elem[i - 1] = this->elem[i];
    }
    this->length--;
}

#endif  // SQLIST_REF_H
