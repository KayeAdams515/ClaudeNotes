// ============================================================
//  sqlist.h —— 顺序表 SqList（脚手架：你要写的部分在这里）
// ============================================================
//
//  对应讲义：[[C2.4 顺序表实现]]，接口定义见 [[C2.3 线性表 ADT]]
//
//  【怎么用这个文件】
//  下面每个函数的函数体里都有一句 TODO，把它替换成真正的代码。
//  文件末尾有全部函数实现，从上往下写就行。
//  写完一个就 `make test-1` 跑一下，红了就改。
//
//  【三个坑，写之前先记住】
//  1. get 的合法下标是 [0, length-1]，但 insert 允许 index == length（追加到末尾）。
//     这两个边界不一样，是整个模块最容易错的地方。
//  2. insert 搬元素必须【从后往前】，否则会把一个值复制满整个数组。
//  3. capacity 是"最多能装几个"，length 是"现在装了几个"。
//     永远保持 length <= capacity。
//
//  模板的成员函数实现要写在头文件里（这是模板的规矩，不是风格问题）。
// ------------------------------------------------------------

#ifndef SQLIST_H
#define SQLIST_H

#include <cstdlib>
#include <iostream>

template <typename T>
class SqList {
public:
    explicit SqList(int capacity);  // 初始化：开数组、记容量、长度置 0
    ~SqList();                      // 销毁：释放数组

    bool empty();                   // 判空
    int getLength();                // 求长度
    int getCapacity();              // 求容量

    T get(int index);               // Retrieve：按下标取元素
    int find(T x);                  // Find：按值找下标，找不到返回 -1

    bool insert(T x, int index);    // 在第 index 个位置【之前】插入
    void erase(int index);          // 删除下标为 index 的元素

    void clear();                   // 清空：只把 length 置 0，不释放内存

private:
    T* elem;       // 动态数组首地址（就是讲义里的 L0）
    int capacity;  // 最多能装几个
    int length;    // 当前装了几个
};

// ============================================================
//  以下是实现。把每个 TODO 换成真正的代码。
// ============================================================

// ---------- S1：构造与简单函数 ----------

template <typename T>
SqList<T>::SqList(int capacity) {
    // TODO 1: 用 new T[capacity] 开数组存进 elem；
    //         把参数存进 this->capacity；
    //         length 置 0（不是 capacity！新表是空的）。
    // 讲义：[[C2.4 顺序表实现]] 三、初始化与简单函数
}

template <typename T>
SqList<T>::~SqList() {
    // TODO 2: 释放 elem。
    // 陷阱：数组必须用 delete[] 而不是 delete。先判空指针更保险。
}

template <typename T>
bool SqList<T>::empty() {
    // TODO 3: 表里没元素时返回 true。
    return true;
}

template <typename T>
int SqList<T>::getLength() {
    // TODO 4: 返回当前元素个数。
    return 0;
}

template <typename T>
int SqList<T>::getCapacity() {
    // TODO 5: 返回容量。
    return 0;
}

template <typename T>
void SqList<T>::clear() {
    // TODO 6: 清空表。
    // 注意：这里【不】释放内存，容量保持不变——这是讲义里特意强调的语义。
}

// ---------- S2：取值与查找 ----------

template <typename T>
T SqList<T>::get(int index) {
    // TODO 7: 返回下标 index 处的元素。
    // 合法范围是 [0, length-1]；越界时调用 exit(EXIT_FAILURE) 结束程序。
    // 想一想：为什么不是 [0, capacity-1]？（可分配但没装数据的格子是垃圾值）
    return T();
}

template <typename T>
int SqList<T>::find(T x) {
    // TODO 8: 从头顺序查找值为 x 的元素，返回它的下标；找不到返回 -1。
    // 这道题是感受 O(n) 的最好例子：可能第一个就命中，也可能要走完全程。
    return -1;
}

// ---------- S3：插入与删除 ----------

template <typename T>
bool SqList<T>::insert(T x, int index) {
    // TODO 9: 在下标 index 之前插入 x。
    // 步骤：
    //   (a) 合法性检查：index < 0 或 index > length 时返回 false
    //       ★ 注意是 > 不是 >=，因为 index == length 表示追加到末尾，是合法的
    //   (b) 判满：length == capacity 时返回 false（先不做扩容，那是 S4 的进阶题）
    //   (c) 腾位置：把下标 [index, length-1] 的元素整体右移一格
    //       ★ 必须从后往前搬！写成 elem[i+1] = elem[i] 且 i 递增，会一路复制同一个值
    //   (d) 放入 x，然后 length++
    return false;
}

template <typename T>
void SqList<T>::erase(int index) {
    // TODO 10: 删除下标 index 处的元素。
    // 步骤：
    //   (a) 合法性检查：index < 0 或 index >= length 时 return
    //       ★ 这里是 >=，和 insert 的边界【不一样】，想清楚为什么
    //   (b) 把下标 [index+1, length-1] 的元素整体左移一格（这次是从前往后搬）
    //   (c) length--
    // 另外想一想：被删掉的那个位置上的旧值，需要手动清掉吗？
}

#endif  // SQLIST_H
