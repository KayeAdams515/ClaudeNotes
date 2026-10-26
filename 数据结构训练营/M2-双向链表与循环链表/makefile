CXX := clang++
CXXFLAGS := -std=c++17 -Wall -Wextra -g -O0 -I../testkit -I.

.PHONY: test test-ref test-1 test-2 test-3 test-4 test-ring clean

m2: test_m2.cpp dllist.h ring.h ../testkit/testkit.h
	$(CXX) $(CXXFLAGS) test_m2.cpp -o m2

m2_ref: test_m2.cpp dllist_ref.h ring_ref.h ../testkit/testkit.h
	$(CXX) $(CXXFLAGS) -DUSE_REF test_m2.cpp -o m2_ref

test: m2
	./m2 all

test-ref: m2_ref
	./m2_ref all

# 默认 test / test-ref 只跑双向链表 D1–D3。第 4 关保留为选做。
test-ring: test-4

test-1 test-2 test-3 test-4: m2
	./m2 $(patsubst test-%,%,$@)

clean:
	rm -f m2 m2_ref
