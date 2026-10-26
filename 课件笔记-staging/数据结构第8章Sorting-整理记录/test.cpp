#include "algorithms.hpp"
#include <cassert>
#include <random>
#include <limits>
#include <iostream>
struct Record {
 int key,id;
 bool operator<(const Record& o) const {return key<o.key;}
};
int main(){
 std::mt19937 rng(20261019); long tested=0;
 for(int n=0;n<130;++n) for(int t=0;t<100;++t){
  std::vector<int> src(n);for(int& x:src)x=int(rng()%41)-20;
  if(t==0)std::sort(src.begin(),src.end());
  if(t==1)std::sort(src.rbegin(),src.rend());
  if(t==2)std::fill(src.begin(),src.end(),7);
  auto expected=src;std::sort(expected.begin(),expected.end());
  for(int which=0;which<7;++which){
   auto a=src;
   switch(which){
    case 0:selection_sort(a.data(),n);break;
    case 1:insertion_swap(a.data(),n);break;
    case 2:insertion_range(a.data(),0,n);break;
    case 3:bubble_sort(a.data(),n);break;
    case 4:heap_sort(a.data(),n);break;
    case 5:merge_sort(a.data(),n);break;
    case 6:quick_range(a.data(),0,n,(t%2)?4:6);break;
   }
   assert(a==expected);++tested;
  }
  std::vector<unsigned> u;for(int x:src)u.push_back(unsigned(x));
  if(n>0&&t==3)u[0]=std::numeric_limits<unsigned>::max();
  auto e=u;std::sort(e.begin(),e.end());radix_sort(u);assert(u==e);++tested;
  auto p=src;parity905(p);auto ps=p;std::sort(ps.begin(),ps.end());assert(ps==expected);
  bool odd=false;for(int x:p){if(x%2)odd=true;else assert(!odd);}++tested;
  int m=n/2;std::vector<int> a(src.begin(),src.begin()+m),b(src.begin()+m,src.end());
  std::sort(a.begin(),a.end());std::sort(b.begin(),b.end());a.resize(n);
  merge88(a,m,b,n-m);assert(a==expected);++tested;
  std::vector<Record> records;for(int i=0;i<n;++i)records.push_back({src[i],i});
  for(int which=0;which<3;++which){auto a=records;
   if(which==0)insertion_range(a.data(),0,n);
   if(which==1)bubble_sort(a.data(),n);
   if(which==2)merge_sort(a.data(),n);
   for(int i=1;i<n;++i){assert(a[i-1].key<=a[i].key);if(a[i-1].key==a[i].key)assert(a[i-1].id<a[i].id);}
  }
 }
 std::cout<<tested<<" algorithm input checks; stability checks passed\n";
}
