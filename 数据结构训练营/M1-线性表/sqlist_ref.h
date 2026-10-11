// ============================================================
//  sqlist_ref.h —— 顺序表 SqList 参考答案（卡住了才看）
// ============================================================
//  看完记得关掉，回到 sqlist.h 自己默写一遍。
//  抄一遍等于没写。
// ------------------------------------------------------------

#ifndef SQLIST_REF_H
#define SQLIST_REF_H

#include <cstdlib>

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
SqListRef<T>::SqListRef(int capacity) {
    this->capacity = capacity;
    this->elem = new T[capacity];
    if (!this->elem) exit(EXIT_FAILURE);
    this->length = 0;
}

template <typename T>
SqListRef<T>::~SqListRef() {
    if (this->elem) delete[] this->elem;
    this->elem = NULL;
}

template <typename T>
bool SqListRef<T>::empty() { return this->length == 0; }

template <typename T>
int SqListRef<T>::getLength() { return this->length; }

template <typename T>
int SqListRef<T>::getCapacity() { return this->capacity; }

template <typename T>
void SqListRef<T>::clear() { this->length = 0; }

template <typename T>
T SqListRef<T>::get(int index) {
    if (index < 0 || index >= this->length) exit(EXIT_FAILURE);
    return this->elem[index];
}

template <typename T>
int SqListRef<T>::find(T x) {
    for (int i = 0; i < this->length; i++) {
        if (this->elem[i] == x) return i;
    }
    return -1;
}

template <typename T>
bool SqListRef<T>::insert(T x, int index) {
    if (index < 0 || index > this->length) return false;
    if (this->length == this->capacity) return false;
    for (int i = this->length; i > index; i--) {
        this->elem[i] = this->elem[i - 1];
    }
    this->elem[index] = x;
    this->length++;
    return true;
}

template <typename T>
void SqListRef<T>::erase(int index) {
    if (index < 0 || index >= this->length) return;
    for (int i = index + 1; i < this->length; i++) {
        this->elem[i - 1] = this->elem[i];
    }
    this->length--;
}

#endif  // SQLIST_REF_H
