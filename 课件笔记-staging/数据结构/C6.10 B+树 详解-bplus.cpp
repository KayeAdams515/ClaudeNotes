// =====================================================================
//  C6.10 B+树 详解 · 完整参考实现（先裂后插版，M 与 L 是模板参数）
//
//  编译与运行（自测部分见文件末尾）：
//      g++ -O2 -std=c++17 -Wall -o bplus bplus.cpp && ./bplus
//
//  约定（与讲义一致）：
//    - 内部块最多 M 个孩子（M-1 个路标键），叶子块最多 L 条记录；
//    - 除根以外，叶子至少 ceil(L/2) 条、内部块至少 ceil(M/2) 个孩子；
//    - 键 k_i 是第 i+1 棵子树的最小键（第 0 棵子树没有键）；
//    - 叶子分裂：右半最小键“复制”到父亲；内部分裂：中间键“移”到父亲；
//    - 满的结点先分裂、再把新条目放进该去的那一半。
//
//  reads / writes 两个计数器把“读块 / 写块”显式记下来，用来核对讲义第一节
//  的代价模型：一次查找的读块数应当恰好等于树高（根常驻内存，不计）。
// =====================================================================
// C6.10 B+树 详解 · 参考实现
// 约定：内部结点 M 路（最多 M-1 个键），键 k_i 是第 i+1 棵子树的最小键；
//       叶子块最多 L 条记录，除根以外至少 ceil(L/2) 条；
//       叶子分裂时右半最小键“复制”到父亲，内部分裂时中间键“移”到父亲。
// 本文件把“读块/写块”显式计数，用来核对讲义里的代价模型。
#include <cstddef>
#include <iostream>
#include <random>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

// ============================ 结点 ============================
template <typename Key, int M, int L>
struct Node {
    bool leaf;
    int n;                              // 当前键数
    Key keys[M];                        // 内部：最多 M-1 个路标；叶子：记录
    Node* child[M + 1];                 // 内部结点的孩子
    Key data[L];                        // 叶子的记录数据（这里就存键本身）
    Node* next;                         // 叶子链表指针

    explicit Node(bool is_leaf) : leaf(is_leaf), n(0), next(nullptr) {
        for (int i = 0; i <= M; ++i) child[i] = nullptr;
    }
    bool full() const { return n >= (leaf ? L : M - 1); }
};

// ============================ B+ 树 ============================
template <typename Key, int M, int L>
class BPlusTree {
public:
    static constexpr int kMaxKeys = M - 1;
    static constexpr int kMinLeaf = (L + 1) / 2;      // ceil(L/2)：L=3 时为 2
    static constexpr int kMinChild = (M + 1) / 2;     // ceil(M/2)
    static constexpr int kLeafSplit = (L + 1) / 2;    // 叶分裂后左半留 ⌈L/2⌉ 条

    BPlusTree() : root_(new Node<Key, M, L>(true)) {}
    ~BPlusTree() { destroy(root_); }

    // 磁盘 I/O 计数：读一个结点 = 读一个磁盘块
    mutable long long reads = 0;
    mutable long long writes = 0;

    // ---------------- 查找 ----------------
    // 返回 leaf 与下标；根常驻内存，所以读盘次数 = 树高（不含根）
    Node<Key, M, L>* find_leaf(const Key& k, int& idx) const {
        Node<Key, M, L>* p = root_;
        while (!p->leaf) {
            int i = 0;
            while (i < p->n && !(k < p->keys[i])) ++i;   // 第一个 > k 的位置
            p = p->child[i];
            ++reads;                                     // 读下一层的块
        }
        idx = lower_bound_in(p, k);
        return p;
    }

    bool contains(const Key& k) const {
        reads = 0;
        int idx;
        Node<Key, M, L>* leaf = find_leaf(k, idx);
        return idx < leaf->n && !(k < leaf->keys[idx]) && !(leaf->keys[idx] < k);
    }

    // 区间查询：找到起点后沿叶子链表走
    void range(const Key& lo, const Key& hi, std::vector<Key>& out) const {
        reads = 0;
        int idx;
        Node<Key, M, L>* leaf = find_leaf(lo, idx);
        while (leaf) {
            for (int i = idx; i < leaf->n; ++i) {
                if (hi < leaf->keys[i]) return;
                out.push_back(leaf->keys[i]);
            }
            idx = 0;
            leaf = leaf->next;
            if (leaf) ++reads;
        }
    }

    // ---------------- 插入 ----------------
    bool insert(const Key& k) {
        writes = 0;
        std::vector<Node<Key, M, L>*> path;      // 从根到叶
        std::vector<int> slot;                   // 每层走的是第几个孩子
        Node<Key, M, L>* p = root_;
        while (!p->leaf) {
            int i = 0;
            while (i < p->n && !(k < p->keys[i])) ++i;
            path.push_back(p);
            slot.push_back(i);
            p = p->child[i];
        }
        reads = static_cast<long long>(path.size());

        int i = lower_bound_in(p, k);
        if (i < p->n && !(p->keys[i] < k) && !(k < p->keys[i])) return false;  // 已存在

        // 统一规则：一个结点“已经满了”就先分裂，再把新条目放进该去的那一半。
        // 叶子：满 = 已有 L 条 -> 裂成 floor(L/2) | ceil(L/2)；
        // 内部：满 = 已有 M 个孩子 -> 裂成 floor(M/2) | ceil(M/2)，中间那个键移上去。
        // 这样每一半天然都 >= 下限，L=3 时 (58,59,61)+60 -> (58,59)(60,61)。
        Node<Key, M, L>* child = nullptr;   // 上一步裂出来的右半，要挂到父亲里
        int child_slot = -1;
        Key sep;                            // 提升到父亲的键

        if (p->full()) {
            // ---- 叶子分裂 ----
            Key tmp[L + 1];
            for (int j = 0; j < p->n; ++j) tmp[j] = p->keys[j];
            tmp[p->n] = k;                               // 把新记录并进来再对半分
            for (int j = p->n; j > 0 && tmp[j] < tmp[j - 1]; --j) {
                Key t = tmp[j]; tmp[j] = tmp[j - 1]; tmp[j - 1] = t;   // 插入排序，保持有序
            }
            const int m = p->n + 1;                      // 此刻 m == L+1
            Node<Key, M, L>* right = new Node<Key, M, L>(true);
            const int left_n = kLeafSplit;               // ⌈L/2⌉
            const int right_n = m - left_n;
            for (int j = 0; j < left_n; ++j) { p->keys[j] = tmp[j]; p->data[j] = tmp[j]; }
            for (int j = 0; j < right_n; ++j) { right->keys[j] = tmp[left_n + j]; right->data[j] = tmp[left_n + j]; }
            p->n = left_n;
            right->n = right_n;
            right->next = p->next;
            p->next = right;
            ++writes;
            sep = right->keys[0];                        // 复制，不是移走
            child = right;
            child_slot = i;                              // 新叶子插在原来的位置上
        } else {
            insert_into_leaf(p, i, k);
            ++writes;
            return true;
        }

        // ---- 把 (sep, child) 挂进父亲，父亲满了就继续往上裂 ----
        Node<Key, M, L>* left = p;
        Node<Key, M, L>* right = child;
        while (!path.empty()) {
            Node<Key, M, L>* parent = path.back();
            int s = path.empty() ? 0 : slot.back();
            path.pop_back();
            slot.pop_back();

            if (!parent->full()) {
                insert_into_internal(parent, s, sep, right, child_slot);
                ++writes;
                return true;
            }

            // 父亲已经满了（M 个孩子）：把新条目并进来凑成 M+1 个，再切成两半。
            // 切完左边留 floor(M/2) 个孩子、右边留 ceil(M/2) 个，中间那个键升高一层。
            {
                // 先按 (sep, right) 该在的位置，把父结点现有的键/孩子各腾出一格
                int ks = 0;
                while (ks < parent->n && !(sep < parent->keys[ks])) ++ks;   // sep 的键位
                for (int j = parent->n; j > ks; --j) parent->keys[j] = parent->keys[j - 1];
                for (int j = parent->n + 1; j > ks + 1; --j) parent->child[j] = parent->child[j - 1];
                parent->keys[ks] = sep;
                parent->child[ks + 1] = right;
                ++parent->n;                             // 现在有 M 个键、M+1 个孩子
            }

            Node<Key, M, L>* up = new Node<Key, M, L>(false);
            const int kc = M / 2;                        // 左边留 kc 个孩子（M=5 -> 2）
            Key up_key = parent->keys[kc];               // 中间那个键升高
            up->n = parent->n - kc - 1;
            for (int j = 0; j < up->n; ++j) up->keys[j] = parent->keys[kc + 1 + j];
            for (int j = 0; j <= up->n; ++j) up->child[j] = parent->child[kc + 1 + j];
            parent->n = kc;
            ++writes;

            sep = up_key;
            right = up;
            left = parent;
        }
        // 顶层也裂了：新建根
        Node<Key, M, L>* new_root = new Node<Key, M, L>(false);
        new_root->n = 1;
        new_root->keys[0] = sep;
        new_root->child[0] = left;
        new_root->child[1] = right;
        root_ = new_root;
        ++writes;
        return true;
    }

    // ---------------- 删除 ----------------
    bool erase(const Key& k) {
        writes = 0;
        std::vector<Node<Key, M, L>*> path;
        Node<Key, M, L>* p = root_;
        while (!p->leaf) {
            int i = 0;
            while (i < p->n && !(k < p->keys[i])) ++i;
            path.push_back(p);
            p = p->child[i];
        }
        reads = static_cast<long long>(path.size());

        int i = lower_bound_in(p, k);
        if (i >= p->n || p->keys[i] < k || k < p->keys[i]) return false;
        remove_from_leaf(p, i);
        ++writes;

        if (p == root_ || p->n >= kMinLeaf) {
            refresh_all(root_);            // 删掉的可能正是某棵子树的最小键
            return true;
        }

        Node<Key, M, L>* node = p;
        int idx = -1;
        while (!path.empty()) {
            Node<Key, M, L>* parent = path.back();
            path.pop_back();
            idx = slot_of(parent, node);
            bool is_leaf = node->leaf;
            int lo = is_leaf ? kMinLeaf : kMinChild;

            Node<Key, M, L>* left = idx > 0 ? parent->child[idx - 1] : nullptr;
            Node<Key, M, L>* right = idx + 1 <= parent->n ? parent->child[idx + 1] : nullptr;

            // ① 兄弟有余量：借一个过来（重分配）
            if (left && (is_leaf ? left->n : child_count(left)) > lo) {
                if (is_leaf) {
                    for (int j = node->n; j > 0; --j) {
                        node->keys[j] = node->keys[j - 1];
                        node->data[j] = node->data[j - 1];
                    }
                    node->keys[0] = left->keys[left->n - 1];
                    node->data[0] = left->data[left->n - 1];
                    --left->n; ++node->n;
                } else {
                    for (int j = node->n; j > 0; --j) node->keys[j] = node->keys[j - 1];
                    for (int j = node->n + 1; j > 0; --j) node->child[j] = node->child[j - 1];
                    node->child[0] = left->child[left->n];
                    node->keys[0] = min_of(left->child[left->n]);
                    --left->n; ++node->n;
                }
                writes += 2;                            // 写被借的兄弟 + 被补的结点
                parent->keys[idx - 1] = node->keys[0];
                ++writes;                               // 写父亲
                refresh_all(root_);
                return true;
            }
            if (right && (is_leaf ? right->n : child_count(right)) > lo) {
                if (is_leaf) {
                    node->keys[node->n] = right->keys[0];
                    node->data[node->n] = right->data[0];
                    ++node->n;
                    remove_from_leaf(right, 0);
                } else {
                    node->child[node->n + 1] = right->child[0];
                    node->keys[node->n] = min_of(right->child[0]);
                    ++node->n;
                    for (int j = 0; j + 1 < right->n; ++j) right->keys[j] = right->keys[j + 1];
                    for (int j = 0; j <= right->n; ++j) right->child[j] = right->child[j + 1];
                    --right->n;
                }
                writes += 2;
                parent->keys[idx] = right->keys[0];
                ++writes;
                refresh_all(root_);
                return true;
            }

            // ② 兄弟也只有半满：合并（优先与右兄弟）
            if (right) {
                merge_nodes(node, right, parent->keys[idx]);
                delete right;
                remove_key(parent, idx, idx + 1);
            } else {
                merge_nodes(left, node, parent->keys[idx - 1]);
                delete node;
                remove_key(parent, idx - 1, idx);
                node = left;
            }
            writes += 2;                                // 写合并结果 + 写父亲
            refresh_keys(parent);
            ++writes;

            node = parent;
            if (node == root_) break;
            if ((node->leaf ? node->n : child_count(node)) >= (node->leaf ? kMinLeaf : kMinChild)) {
                refresh_all(root_);
                return true;
            }
        }

        // 根只剩一个孩子：删根，树矮一层
        if (!root_->leaf && child_count(root_) == 1) {
            Node<Key, M, L>* old = root_;
            root_ = root_->child[0];
            delete old;
            ++writes;
        }
        refresh_all(root_);
        return true;
    }

    // ---------------- 调试输出 ----------------
    void dump(std::ostream& os) const { dump_node(os, root_, 0); }

    int height() const {
        int h = 0;
        Node<Key, M, L>* p = root_;
        while (!p->leaf) { p = p->child[0]; ++h; }
        return h;
    }

    std::vector<Key> all() const {
        std::vector<Key> v;
        Node<Key, M, L>* p = root_;
        while (!p->leaf) p = p->child[0];
        while (p) {
            for (int i = 0; i < p->n; ++i) v.push_back(p->keys[i]);
            p = p->next;
        }
        return v;
    }

    // 结构自检
    bool check(std::string& err) const {
        std::set<int> depths;
        std::vector<Key> keys = all();
        for (size_t i = 1; i < keys.size(); ++i)
            if (!(keys[i - 1] < keys[i])) { err = "叶子非升序或重复"; return false; }
        return check_node(root_, 0, depths, err) && depths.size() <= 1;
    }

private:
    Node<Key, M, L>* root_;

    static int lower_bound_in(Node<Key, M, L>* p, const Key& k) {
        int lo = 0, hi = p->n;
        while (lo < hi) { int m = (lo + hi) / 2; if (p->keys[m] < k) lo = m + 1; else hi = m; }
        return lo;
    }
    static void insert_into_leaf(Node<Key, M, L>* p, int i, const Key& k) {
        for (int j = p->n; j > i; --j) { p->keys[j] = p->keys[j - 1]; p->data[j] = p->data[j - 1]; }
        p->keys[i] = k; p->data[i] = k; ++p->n;
    }
    static void remove_from_leaf(Node<Key, M, L>* p, int i) {
        for (int j = i; j + 1 < p->n; ++j) { p->keys[j] = p->keys[j + 1]; p->data[j] = p->data[j + 1]; }
        --p->n;
    }
    // 在 p 的第 i 个键位插入 k，并把新孩子 right 挂到第 i+1 个孩子位
    static void insert_into_internal(Node<Key, M, L>* p, int i, const Key& k,
                                     Node<Key, M, L>* right, int /*child_slot*/) {
        for (int j = p->n; j > i; --j) { p->keys[j] = p->keys[j - 1]; p->child[j + 1] = p->child[j]; }
        p->keys[i] = k;
        p->child[i + 1] = right;
        ++p->n;
    }

    // 把 right 的内容并进 left 里，sep 是父亲里那个分隔键
    static void merge_nodes(Node<Key, M, L>* left, Node<Key, M, L>* right, const Key& sep) {
        if (left->leaf) {
            for (int j = 0; j < right->n; ++j) {
                left->keys[left->n + j] = right->keys[j];
                left->data[left->n + j] = right->data[j];
            }
            left->n += right->n;
            left->next = right->next;
        } else {
            left->keys[left->n] = sep;                       // 把分隔键拉下来
            ++left->n;
            for (int j = 0; j < right->n; ++j) left->keys[left->n + j] = right->keys[j];
            for (int j = 0; j <= right->n; ++j) left->child[left->n + j] = right->child[j];
            left->n += right->n;
        }
    }

    // 自底向上把整棵树的路标重算成“对应子树的最小键”。
    // 合并 / 借记录会改变某棵子树的最小键，进而让祖先的路标连锁失效；
    // 演示用的树很小，直接一次重算，保证输出始终是严格规范形。
    void refresh_all(Node<Key, M, L>* p) {
        if (p->leaf) return;
        for (int i = 0; i <= p->n; ++i) refresh_all(p->child[i]);
        refresh_keys(p);
    }


    static int child_count(Node<Key, M, L>* p) { return p->n + 1; }
    static int slot_of(Node<Key, M, L>* parent, Node<Key, M, L>* c) {
        for (int i = 0; i <= parent->n; ++i) if (parent->child[i] == c) return i;
        return -1;
    }
    static void remove_key(Node<Key, M, L>* p, int ki, int ci) {
        for (int j = ki; j + 1 < p->n; ++j) p->keys[j] = p->keys[j + 1];
        for (int j = ci; j + 1 <= p->n; ++j) p->child[j] = p->child[j + 1];
        --p->n;
    }
    void refresh_keys(Node<Key, M, L>* p) {
        if (p->leaf) return;
        for (int i = 1; i <= p->n; ++i) p->keys[i - 1] = min_of(p->child[i]);
    }
    static Key min_of(Node<Key, M, L>* p) {
        while (!p->leaf) p = p->child[0];
        return p->keys[0];
    }

    void dump_node(std::ostream& os, Node<Key, M, L>* p, int depth) const {
        os << std::string(depth * 2, ' ');
        os << (p->leaf ? "(" : "[");
        for (int i = 0; i < p->n; ++i) { if (i) os << ' '; os << p->keys[i]; }
        os << (p->leaf ? ")" : "]") << "\n";
        if (!p->leaf) for (int i = 0; i <= p->n; ++i) dump_node(os, p->child[i], depth + 1);
    }

    bool check_node(Node<Key, M, L>* p, int d, std::set<int>& depths, std::string& err) const {
        if (p->leaf) {
            depths.insert(d);
            if (p != root_ && p->n < kMinLeaf) { err = "叶子不足半满"; return false; }
            if (p->n > L) { err = "叶子超容量"; return false; }
            return true;
        }
        if (p->n != child_count(p) - 1) { err = "键数与孩子数不匹配"; return false; }
        if (p->n + 1 > M) { err = "内部超容量"; return false; }
        if (p == root_) { if (p->n + 1 < 2) { err = "根孩子数<2"; return false; } }
        else if (p->n + 1 < kMinChild) { err = "内部不足半满"; return false; }
        for (int i = 1; i <= p->n; ++i) {
            if (!(p->keys[i - 1] == min_of(p->child[i]))) { err = "路标不等于子树最小键"; return false; }
        }
        for (int i = 0; i <= p->n; ++i) if (!check_node(p->child[i], d + 1, depths, err)) return false;
        return true;
    }

    void destroy(Node<Key, M, L>* p) {
        if (!p) return;
        if (!p->leaf) for (int i = 0; i <= p->n; ++i) destroy(p->child[i]);
        delete p;
    }
};

// ============================ 测试 ============================
int main() {
    using Tree = BPlusTree<int, 5, 3>;
    std::mt19937 rng(12345);
    int failures = 0;

    // 1) 随机对照测试（M=5/L=3）
    for (int trial = 0; trial < 200; ++trial) {
        Tree t;
        std::set<int> ref;
        std::string err;
        std::vector<int> ops;
        for (int step = 0; step < 3000; ++step) {
            int k = static_cast<int>(rng() % 400);
            if (ref.count(k) == 0 && (rng() % 3)) {
                t.insert(k); ref.insert(k);
            } else if (ref.count(k)) {
                t.erase(k); ref.erase(k);
            } else {
                t.insert(k); ref.insert(k);
            }
            if (!t.check(err)) { std::cout << "结构错: " << err << " step=" << step << "\n"; ++failures; break; }
            std::vector<int> got = t.all();
            std::vector<int> want(ref.begin(), ref.end());
            if (got != want) { std::cout << "内容不一致 step=" << step << "\n"; ++failures; break; }
        }
    }
    std::cout << (failures ? "随机测试失败\n" : "随机测试 200 轮 × 3000 步：全部通过\n");

    // 2) 课本那棵树：插入 55/87/60/11/35/86
    {
        Tree t;
        std::vector<int> init = {2,3,4,7,8,9,12,14,15,18,20,21,24,26,27,28,30,32,33,36,
                                 39,40,42,43,45,48,49,51,52,54,56,58,59,61,63,64,66,67,
                                 69,71,74,75,78,79,81,82,85,88,91,92,98};
        for (int k : init) t.insert(k);
        std::cout << "\n--- 升序建树 51 条，高度 " << t.height() << " ---\n";
        t.dump(std::cout);
        for (int k : {55, 87, 60, 11, 35, 86}) {
            t.insert(k);
            std::cout << "插入 " << k << " 后：读 " << t.reads << " 块，写 " << t.writes
                      << " 块，高度 " << t.height() << "，记录 " << t.all().size() << "\n";
        }
        std::cout << "\n--- 插入 6 条后 ---\n";
        t.dump(std::cout);
        std::string err;
        std::cout << "自检：" << (t.check(err) ? "OK" : err) << "\n";
        for (int k : {98, 75, 39, 59, 35, 88}) {
            t.erase(k);
            std::cout << "删除 " << k << " 后：读 " << t.reads << " 块，写 " << t.writes
                      << " 块，高度 " << t.height() << "，记录 " << t.all().size() << "\n";
        }
        std::cout << "\n--- 删除 6 条后 ---\n";
        t.dump(std::cout);
        std::cout << "自检：" << (t.check(err) ? "OK" : err) << "\n";
    }

    // 3) 顺序插入 vs 随机插入：分裂次数
    {
        Tree t1, t2;
        std::vector<int> asc;
        for (int i = 0; i < 200; ++i) asc.push_back(i);
        for (int k : asc) t1.insert(k);
        std::vector<int> sh = asc;
        std::shuffle(sh.begin(), sh.end(), rng);
        for (int k : sh) t2.insert(k);
        std::cout << "\n200 个键：升序插入高度 " << t1.height()
                  << "，随机插入高度 " << t2.height() << "\n";
    }
    return 0;
}
