#ifndef DOJO_DLLIST_H
#define DOJO_DLLIST_H

template <typename T>
struct DNode
{
    T data;
    DNode *prior;
    DNode *next;
};

// 不带头结点、非循环。空表 head == tail == nullptr。
// 下标从 0 开始；非法插入返回 false，非法删除直接返回。
template <typename T>
class DLList
{
public:
    DLList();
    ~DLList();
    bool empty() const;
    int getLength() const;
    void clear();
    bool insert(T x, int index);
    void erase(int index);

    // 已提供：只允许外部观察结点，不修改链接。
    const DNode<T> *headNode() const { return head; }
    const DNode<T> *tailNode() const { return tail; }
    DLList(const DLList &) = delete;
    DLList &operator=(const DLList &) = delete;

private:
    DNode<T> *head;
    DNode<T> *tail;
    int length;
};

// D1：骨架。先跑 make test-1；非空 clear/析构在 D2、D3 中继续验收。
template <typename T>
DLList<T>::DLList() : head(nullptr), tail(nullptr), length(0)
{
    // TODO 1：上面是安全占位初始化；理解后自己写一遍初始化。
}

template <typename T>
DLList<T>::~DLList()
{
    clear();
    // TODO 2：逐个释放结点。可以复用 clear()。
}

template <typename T>
bool DLList<T>::empty() const
{
    // TODO 3：空表返回 true。
    return length == 0;
}

template <typename T>
int DLList<T>::getLength() const
{
    // TODO 4：返回当前长度。
    return length;
}

template <typename T>
void DLList<T>::clear()
{
    DNode<T> *p = head;
    DNode<T> *temp = nullptr;
    while (head)
    {
        temp = head;
        head = head->next;
        delete temp; // 不必维护各节点的prior
    }
    head = nullptr;
    tail = nullptr;
    length = 0;

    // TODO 5：先保留 next，再 delete；最后 head、tail 置空，长度归零。
}

// D2：插入。index 合法范围 [0, length]，失败不能改变表。
template <typename T>
bool DLList<T>::insert(T x, int index)
{
    (void)x;
    (void)index;
    if (index < 0 || index > length) {
    return false;
}
    DNode<T> *p = new DNode<T>;
    p->data = x;
    p->prior = nullptr;
    p->next = nullptr;
    if (empty())//单独处理插入前表为空的情况
    {
        head = p;
        tail = p;
        length++;
    }
    else
    {
        if (index <= 0)
        {
            p->next = head;
            head->prior = p;
            head = p;
        }
        else if (index >= length)
        {   
            p->prior = tail;
            tail->next = p;
            tail = p;
        }
        else
        {
            DNode<T> *cur = head;
            for (int i = 0; i < index - 1; i++)
            {
                cur = cur->next;
            }
            p->prior = cur;
            p->next = cur->next;
            cur->next->prior = p;
            cur->next = p;
        }
        length++;
    }
    return true;
    // TODO 6：先判下标，再 new 结点。
    // 空表/头插/尾插/中间插；新结点的 prior、next 都要初始化。
    // 中间插：先保存左右邻居并让新结点连上它们，再让两边指向新结点。
    // 头插、尾插要求 O(1)，中间插允许 O(n)。成功后 length++，返回 true。
    return false;
}

// D3：删除。index 合法范围 [0, length-1]，非法直接 return。
template <typename T>
void DLList<T>::erase(int index)
{
    (void)index;
    if (index < 0 || index > length - 1)
    {
        return;
    }

    DNode<T> *p = head;


    for (int i = 0; i < index; i++) // p就是等待删除的那个
    {
        p = p->next;
    }
    if(length == 1){
        head = nullptr;
        tail = nullptr;
    }
    else if (p->next == nullptr) // 特殊处理删除尾结点的情况
    {
        tail = p->prior;
        p->prior->next = nullptr;
    }
    else if (p->prior == nullptr)//头结点
    {
        head = p->next;
        p->next->prior = nullptr;
    }
    else
    {
        p->prior->next = p->next;
        p->next->prior = p->prior;
    }
    delete p;
    length--;
    if (empty())
    {
        head = nullptr;
        tail = nullptr;
    }
    // }
    // TODO 7：找到待删结点，让左右邻居相接，维护 head/tail，再 delete。
    // 邻居可能为空；删掉唯一结点后，head、tail 都要置空。最后 length--。
    // 按下标定位允许 O(n)；拿到结点后解除链接应为 O(1)。
}

#endif
