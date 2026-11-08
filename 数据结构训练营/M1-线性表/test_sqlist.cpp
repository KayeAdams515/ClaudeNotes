// ============================================================
//  test_sqlist.cpp —— 顺序表测试题
// ============================================================
//  这个文件不用改。它就是"题目要求"本身，读 CHECK 后面的说明就是读题。
//
//  make test       跑全部关卡（用你写的 sqlist.h）
//  make test-ref   跑全部关卡（用参考答案，用来确认环境正常）
//  make test-1     只跑第 1 关（S1）
//  make test-2     只跑第 2 关（S2）
//  make test-3     只跑第 3 关（S3）
//
//  注意：get() 越界会直接 exit 结束程序，所以测试里【不】故意传非法下标给 get()，
//        那部分边界要靠 insert/erase 来体会。
// ------------------------------------------------------------

#include <iostream>
#include <string>

#include "testkit.h"

#ifdef USE_REF
#include "sqlist_ref.h"
#define SQCLASS SqListRef
#else
#include "sqlist.h"
#define SQCLASS SqList
#endif

// ------------------------------------------------------------
// S1：构造、析构、empty、getLength、getCapacity、clear
// ------------------------------------------------------------
int test_s1() {
    std::cout << "\n---- S1 构造与简单函数 ----\n";

    SQCLASS<int> list(5);

    CHECK(list.getCapacity() == 5, "容量应该是构造时传入的 5");
    CHECK(list.getLength() == 0, "刚构造出来的表是空表，length 应该是 0 而不是容量");
    CHECK(list.empty() == true, "空表 empty() 应该返回 true");

    // 装一个元素，再看 length 和 empty 有没有跟着变
    CHECK(list.insert(10, 0) == true, "往空表里插入一个元素应该成功");
    CHECK(list.getLength() == 1, "插入一个元素后 length 应该是 1");
    CHECK(list.empty() == false, "有元素之后 empty() 应该返回 false");

    // clear 之后：长度归零，但容量不变
    list.clear();
    CHECK(list.getLength() == 0, "clear() 之后 length 应该归零");
    CHECK(list.empty() == true, "clear() 之后应该是空表");
    CHECK(list.getCapacity() == 5, "clear() 只清长度，容量必须保持不变");

    // clear 之后还能继续用（这正是它不释放内存的意义）
    CHECK(list.insert(20, 0) == true, "clear() 之后应该还能正常插入");
    CHECK(list.get(0) == 20, "clear() 之后插入的元素应该能正确取回");

    return 0;
}

// ------------------------------------------------------------
// S2：get 按下标取值、find 按值查找
// ------------------------------------------------------------
int test_s2() {
    std::cout << "\n---- S2 取值与查找 ----\n";

    SQCLASS<int> list(8);

    // 依次追加 25 34 57 16 48（讲义里顺序查找用的那组数据）
    CHECK(list.insert(25, 0) == true, "插入 25 到下标 0");
    CHECK(list.insert(34, 1) == true, "插入 34 到下标 1");
    CHECK(list.insert(57, 2) == true, "插入 57 到下标 2");
    CHECK(list.insert(16, 3) == true, "插入 16 到下标 3");
    CHECK(list.insert(48, 4) == true, "插入 48 到下标 4");

    CHECK(list.getLength() == 5, "插入 5 个元素后 length 应该是 5");

    // get：对号入座
    CHECK(list.get(0) == 25, "get(0) 应该是第一个元素 25");
    CHECK(list.get(2) == 57, "get(2) 应该是 57");
    CHECK(list.get(4) == 48, "get(4) 应该是末尾元素 48（合法上界 length-1）");

    // find：按值找下标
    CHECK(list.find(25) == 0, "find(25) 应该是 0（第一个就命中）");
    CHECK(list.find(16) == 3, "find(16) 应该是 3");
    CHECK(list.find(48) == 4, "find(48) 应该是 4（要走完全程倒数第一个才命中）");
    CHECK(list.find(50) == -1, "find(50) 元素不存在，应该返回 -1 这个哨兵值");

    // find 找到的是【第一个】匹配的位置
    CHECK(list.insert(57, 0) == true, "表头再插一个重复值 57");
    CHECK(list.find(57) == 0, "有重复值时应返回第一个匹配的下标");
    CHECK(list.getLength() == 6, "现在应该有 6 个元素");

    return 0;
}

// ------------------------------------------------------------
// S3：insert 插入、erase 删除
// ------------------------------------------------------------
int test_s3() {
    std::cout << "\n---- S3 插入与删除 ----\n";

    SQCLASS<int> list(9);

    // 讲义原例：数组 25 12 47 89 36 14（length=6）
    int raw[6] = {25, 12, 47, 89, 36, 14};
    for (int i = 0; i < 6; i++) list.insert(raw[i], i);
    CHECK(list.getLength() == 6, "先铺好 6 个元素");

    // --- 边界：insert 允许 index == length（追加到末尾）---
    CHECK(list.insert(99, 6) == true, "index == length 是合法的，表示追加到末尾");
    CHECK(list.get(6) == 99, "追加的元素应该在下标 6");
    CHECK(list.getLength() == 7, "追加之后 length 应该是 7");
    list.erase(6);  // 还原

    // --- 边界：越界必须被拒绝 ---
    CHECK(list.insert(99, -1) == false, "index 为负应该返回 false");
    CHECK(list.insert(99, 7) == false, "index 大于 length 应该返回 false（比 length 大就不行）");
    CHECK(list.getLength() == 6, "两次非法插入都不应该改变 length");

    // --- 中间插入：检验搬移方向 ---
    // 在下标 3（值 89）之前插入 99，结果应为 25 12 47 99 89 36 14
    CHECK(list.insert(99, 3) == true, "在下标 3 前插入 99 应该成功");
    CHECK(list.getLength() == 7, "插入后 length 应该是 7");
    CHECK(list.get(2) == 47, "下标 2 应该还是 47");
    CHECK(list.get(3) == 99, "新元素应该落在下标 3");
    CHECK(list.get(4) == 89, "原来的 89 应该被挤到下标 4");
    CHECK(list.get(5) == 36, "原来的 36 应该被挤到下标 5（从后往前搬才不会被覆盖）");
    CHECK(list.get(6) == 14, "末尾元素 14 应该保持不变");
    list.erase(3);  // 还原

    // --- 表头插入 ---
    CHECK(list.insert(1, 0) == true, "在下标 0 前插入应该成功");
    CHECK(list.get(0) == 1, "表头插入后新元素应该在下标 0");
    CHECK(list.get(1) == 25, "原来的首元素 25 应该被挤到下标 1");
    CHECK(list.getLength() == 7, "表头插入后 length 应该是 7");
    list.erase(0);  // 还原

    // --- 判满：容量 9，现在 6 个，塞到满为止 ---
    CHECK(list.insert(1, 6) == true, "塞第 7 个应该成功");
    CHECK(list.insert(2, 7) == true, "塞第 8 个应该成功");
    CHECK(list.insert(3, 8) == true, "塞第 9 个应该成功（刚好满）");
    CHECK(list.getLength() == 9, "此时 length 应该等于 capacity");
    CHECK(list.insert(4, 9) == false, "已满时插入应该返回 false（先不做扩容）");
    CHECK(list.getLength() == 9, "失败的插入不应该改变 length");

    // --- erase：越界必须被忽略，且不能崩 ---
    list.erase(-1);
    CHECK(list.getLength() == 9, "erase 负数下标应该什么都不做");
    list.erase(9);
    list.erase(100);
    CHECK(list.getLength() == 9, "erase 越界下标应该什么都不做");

    // --- erase：表头、中间、末尾 ---
    // 当前内容：25 12 47 89 36 14 1 2 3（9 个）
    list.erase(0);  // 删表头
    CHECK(list.getLength() == 8, "删一个元素后 length 应该是 8");
    CHECK(list.get(0) == 12, "删掉表头后，下标 0 应该是原来的第二个元素");

    list.erase(0);  // 当前表头 12，删掉 → 47 开头
    CHECK(list.get(0) == 47, "继续删表头");

    int before2 = list.get(2);  // 应该是 36
    list.erase(1);              // 删中间：删掉 89
    CHECK(list.get(1) == before2, "删中间后，后面的元素应该整体左移一格");
    CHECK(list.getLength() == 6, "删到这里应该剩 6 个元素");

    list.erase(5);  // 删末尾
    CHECK(list.getLength() == 5, "删末尾后 length 应该是 5");

    // --- 与讲义核对：删完顺序必须仍然正确 ---
    CHECK(list.get(0) == 47, "剩余元素顺序应为 47");
    CHECK(list.get(1) == 36, "剩余元素顺序应为 36");
    CHECK(list.get(2) == 14, "剩余元素顺序应为 14");
    CHECK(list.get(3) == 1, "剩余元素顺序应为 1");
    CHECK(list.get(4) == 2, "剩余元素顺序应为 2");

    return 0;
}

// ------------------------------------------------------------
// S4：进阶 —— 扩容的套路（"忘了搬 length" 专项）
// ------------------------------------------------------------
//  this 版本没有 grow()，扩容需要你手动模拟：
//  找一个更大的新数组，把旧数组里【前 length 个】元素搬过去。
//  这一步最容易犯的错是：搬了 capacity 个而不是 length 个，
//  于是把没装数据的垃圾值也搬了过去。这个测试就是专门抓这个错的。
//
//  想真正写进类里的话，可以自己给 SqList 加一个 void grow(); 然后
//  在 insert 判满时调用它——那属于选做，讲义 [[C2.4 顺序表实现]] 六节有原话。
int test_s4() {
    std::cout << "\n---- S4 进阶：扩容套路 ----\n";

    SQCLASS<int> small(3);
    small.insert(1, 0);
    small.insert(2, 1);
    small.insert(3, 2);
    CHECK(small.getLength() == 3, "先把容量 3 装到满");
    CHECK(small.insert(4, 3) == false, "满表的插入应该被拒绝（还没有扩容能力）");

    // 手动扩容：容量翻倍到 6，只搬前 length 个元素
    SQCLASS<int> big(6);
    for (int i = 0; i < small.getLength(); i++) {
        big.insert(small.get(i), i);
    }
    CHECK(big.getCapacity() == 6, "新数组容量应该是 6");
    CHECK(big.getLength() == 3, "搬迁之后【长度】必须还是 3，不是 6");

    int expect[3] = {1, 2, 3};
    for (int i = 0; i < 3; i++) {
        CHECK(big.get(i) == expect[i], "搬迁后第 " + std::to_string(i) + " 个元素应该原样保留");
    }

    // 扩容没出问题的话，现在应该还能再塞进去
    CHECK(big.insert(4, 3) == true, "扩容之后应该还能继续插入");
    CHECK(big.insert(5, 4) == true, "继续插入");
    CHECK(big.getLength() == 5, "此时长度应该是 5");
    CHECK(big.get(3) == 4, "新插入的元素位置应该正确");
    CHECK(big.get(4) == 5, "新插入的元素位置应该正确");

    // 装满到新的容量为止
    CHECK(big.insert(6, 5) == true, "塞第 6 个应该成功");
    CHECK(big.getLength() == 6, "装满后长度等于容量");
    CHECK(big.insert(7, 6) == false, "再次满表，仍然应该被拒绝");

    return 0;
}

int main(int argc, char** argv) {
    // 让输出立刻可见：万一程序中途崩溃，也能看到崩溃前跑到哪一条
    std::cout << std::unitbuf;
    std::string level = (argc > 1) ? argv[1] : "all";

    if (level == "all" || level == "1") test_s1();
    if (level == "all" || level == "2") test_s2();
    if (level == "all" || level == "3") test_s3();
    if (level == "all" || level == "4") test_s4();

    TEST_END("SqList 测试");
}
