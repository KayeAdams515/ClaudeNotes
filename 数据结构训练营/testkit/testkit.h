// testkit.h —— 极简测试框架
// 用法：在测试文件里写 CHECK(条件, "出错时的说明");
// 全部通过 → 打印「全部通过」并返回 0；有失败 → 打印哪一条红了并返回 1。
//
// 这里没有任何魔法，看不懂可以完全忽略，它不影响你写数据结构。

#ifndef TESTKIT_H
#define TESTKIT_H

#include <iostream>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <functional>
#include <sys/wait.h>
#include <unistd.h>

namespace tk {

inline int& fail_count() {
    static int n = 0;
    return n;
}

inline int& check_count() {
    static int n = 0;
    return n;
}

inline void check(bool ok, const std::string& what, const char* file, int line) {
    check_count()++;
    if (!ok) {
        fail_count()++;
        std::cout << "  [红] " << what << "\n"
                  << "       位置：" << file << ":" << line << "\n";
    } else {
        std::cout << "  [绿] " << what << "\n";
    }
}

inline int summary(const std::string& title) {
    std::cout << "\n==============================\n";
    std::cout << title << "：共 " << check_count() << " 项检查，";
    if (fail_count() == 0) {
        std::cout << "全部通过 ✓\n";
        std::cout << "==============================\n";
        return 0;
    }
    std::cout << fail_count() << " 项失败 ✗\n";
    std::cout << "提示：先逐字读测试文件里那一条 CHECK 的要求，再回去看你的实现。\n";
    std::cout << "==============================\n";
    return 1;
}

// 把一段【会故意崩溃或退出】的代码放到子进程里跑，父进程检查它有没有被信号打死。
// 用途：测试"传入非法下标会 exit"这类边界，而不让整个测试程序挂掉。
// 判据：只要子进程不是被信号终止（也就是没有段错误），就算通过。
// 参数用 std::function，这样可以用 lambda 捕获测试里的局部变量。
inline void expect_no_crash(const std::function<void()>& fn, const std::string& what,
                            const char* file, int line) {
    check_count()++;
    std::cout.flush();
    pid_t pid = fork();
    if (pid == 0) {
        // 子进程：把输出丢掉，跑那段代码
        if (!freopen("/dev/null", "w", stdout)) { _exit(0); }
        if (!freopen("/dev/null", "w", stderr)) { _exit(0); }
        fn();
        _exit(0);
    } else if (pid < 0) {
        fail_count()++;
        std::cout << "  [红] " << what << "（fork 失败，无法测试）\n";
    } else {
        int status = 0;
        waitpid(pid, &status, 0);
        if (WIFSIGNALED(status)) {
            fail_count()++;
            std::cout << "  [红] " << what << "\n"
                      << "       程序被信号 " << WTERMSIG(status)
                      << " 终止了（通常是段错误：访问了 NULL 或野指针）\n"
                      << "       位置：" << file << ":" << line << "\n";
        } else {
            std::cout << "  [绿] " << what << "\n";
        }
    }
    std::cout.flush();
}

}  // namespace tk

#define CHECK(cond, what) ::tk::check((cond), (what), __FILE__, __LINE__)

// 用于测试 exit / 崩溃边界：CHECK_ADV(表达式, "说明")
#define CHECK_ADV(call, what)                                            \
    do {                                                                 \
        ::tk::expect_no_crash([&]() { call; }, (what), __FILE__, __LINE__); \
    } while (0)

#define TEST_END(title) return ::tk::summary(title)

#endif  // TESTKIT_H
