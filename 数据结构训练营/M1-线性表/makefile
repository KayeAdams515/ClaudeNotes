# ============================================================
#  M1-线性表 · makefile
# ============================================================
#  make test       跑全部关卡（用【你写的】sqlist.h / ll.h）
#  make test-ref   跑全部关卡（用【参考答案】，确认环境正常）
#  make test-1     只跑第 1 关
#  make test-2 / test-3 / test-4 / test-5
#  make test-sq    只跑顺序表
#  make test-ll    只跑单链表
#  make clean      删掉编译产物
#
#  如果要用 GDB 单步调试：
#     make debug-1   然后按提示跑 gdb
# ------------------------------------------------------------

CXX      := g++
CXXFLAGS := -std=c++17 -Wall -Wextra -g -O0 -I../testkit -I.
RM       := rm -f

# ---------- 顺序表 ----------
sqlist: test_sqlist.cpp sqlist.h ../testkit/testkit.h
	$(CXX) $(CXXFLAGS) test_sqlist.cpp -o sqlist

sqlist_ref: test_sqlist.cpp sqlist_ref.h ../testkit/testkit.h
	$(CXX) $(CXXFLAGS) -DUSE_REF test_sqlist.cpp -o sqlist_ref

# ---------- 单链表 ----------
ll: test_ll.cpp ll.h ../testkit/testkit.h
	$(CXX) $(CXXFLAGS) test_ll.cpp -o ll

ll_ref: test_ll.cpp ll_ref.h ../testkit/testkit.h
	$(CXX) $(CXXFLAGS) -DUSE_REF test_ll.cpp -o ll_ref

# ---------- 目标 ----------
.PHONY: test test-ref test-sq test-ll test-s4 test-1 test-2 test-3 test-4 test-5 clean debug-1

test: sqlist ll
	@echo ""
	@echo "############ 顺序表 SqList ############"
	@./sqlist all || true
	@echo ""
	@echo "############ 单链表 LL ############"
	@./ll all || true

test-ref: sqlist_ref ll_ref
	@echo ""
	@echo "############ 参考答案 · 顺序表 ############"
	@./sqlist_ref all
	@echo ""
	@echo "############ 参考答案 · 单链表 ############"
	@./ll_ref all

test-sq: sqlist
	@./sqlist all

test-ll: ll
	@./ll all

test-1: sqlist ll
	@echo "=== 第 1 关：SqList S1 / LL L1 ==="
	@./sqlist 1 || true
	@./ll 1 || true

test-2: sqlist ll
	@echo "=== 第 2 关：SqList S2 / LL L2 ==="
	@./sqlist 2 || true
	@./ll 2 || true

test-3: sqlist ll
	@echo "=== 第 3 关：SqList S3 / LL L3 ==="
	@./sqlist 3 || true
	@./ll 3 || true

test-4: sqlist ll
	@echo "=== 第 4 关：SqList S4（扩容） / LL L4（删除）==="
	@./sqlist 4 || true
	@./ll 4 || true

test-5: ll
	@echo "=== 第 5 关：LL L5 ==="
	@./ll 5 || true

test-s4: sqlist
	@./sqlist 4

debug-1: sqlist
	@echo "运行：gdb ./sqlist   然后输入  run 1"
	@echo "或直接：lldb ./sqlist  ;  run 1"

clean:
	$(RM) sqlist sqlist_ref ll ll_ref
