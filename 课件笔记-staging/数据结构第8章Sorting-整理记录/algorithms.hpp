#include <algorithm>
#include <vector>
#include <utility>
#include <cstddef>
template<class T>
void selection_sort(T* a, int n) {
    for (int i=0; i<n-1; ++i) {
        int low=i;
        for (int j=n-1; j>i; --j)
            if (a[j]<a[low]) low=j;
        std::swap(a[i],a[low]);
    }
}
template<class T>
void insertion_swap(T* a, int n) {
    for (int k=1; k<n; ++k)
        for (int j=k; j>0; --j) {
            if (a[j]<a[j-1]) std::swap(a[j],a[j-1]);
            else break;
        }
}
template<class T>
void insertion_range(T* a, int first, int last) {
    for (int k=first+1; k<last; ++k) {
        T tmp=a[k];
        int j=k;
        while (j>first && tmp<a[j-1]) {
            a[j]=a[j-1];
            --j;
        }
        a[j]=tmp;
    }
}
template<class T>
void bubble_sort(T* a, int n) {
    int end=n-1;
    while (end>0) {
        int last=0;
        for (int j=0; j<end; ++j)
            if (a[j+1]<a[j]) {
                std::swap(a[j],a[j+1]);
                last=j;
            }
        end=last;
    }
}
template<class T>
void sift_down(T* a, int root, int end) {
    while (root<end/2) { // 有左孩子，避免先计算可能溢出的2*root+1
        int child=2*root+1;
        if (child+1<end && a[child]<a[child+1]) ++child;
        if (!(a[root]<a[child])) break;
        std::swap(a[root],a[child]);
        root=child;
    }
}
template<class T>
void heap_sort(T* a, int n) {
    for (int k=n/2; k>0; ) sift_down(a,--k,n);
    for (int end=n; end>1; ) {
        std::swap(a[0],a[--end]);
        sift_down(a,0,end);
    }
}
template<class T>
void merge_part(T* a, T* tmp, int first, int mid, int last) {
    int i=first, j=mid, k=first;
    while (i<mid && j<last) {
        if (a[j]<a[i]) tmp[k++]=a[j++];
        else tmp[k++]=a[i++]; // 相等取左，保持稳定
    }
    while (i<mid) tmp[k++]=a[i++];
    while (j<last) tmp[k++]=a[j++];
    for (k=first; k<last; ++k) a[k]=tmp[k];
}
template<class T>
void merge_rec(T* a, T* tmp, int first, int last) {
    if (last-first<=6) {
        insertion_range(a,first,last);
        return;
    }
    int mid=first+(last-first)/2;
    merge_rec(a,tmp,first,mid);
    merge_rec(a,tmp,mid,last);
    merge_part(a,tmp,first,mid,last);
}
template<class T>
void merge_sort(T* a, int n) {
    if (n<2) return;
    std::vector<T> tmp(a,a+n);
    merge_rec(a,tmp.data(),0,n);
}
template<class T>
void quick_range(T* a, int first, int last, int cutoff=6) {
    if (last-first<=cutoff) {
        insertion_range(a,first,last);
        return;
    }
    int mid=first+(last-first)/2;
    if (a[mid]<a[first]) std::swap(a[mid],a[first]);
    if (a[last-1]<a[first]) std::swap(a[last-1],a[first]);
    if (a[last-1]<a[mid]) std::swap(a[last-1],a[mid]);
    std::swap(a[mid],a[last-1]);
    T pivot=a[last-1];
    int i=first+1, j=last-2;
    while (true) {
        while (i<=j && a[i]<pivot) ++i;
        while (i<=j && pivot<a[j]) --j;
        if (i>j) break;
        std::swap(a[i],a[j]);
        ++i; --j;
    }
    std::swap(a[i],a[last-1]);
    quick_range(a,first,i,cutoff);
    quick_range(a,i+1,last,cutoff);
}
void radix_sort(std::vector<unsigned>& a) {
    if (a.empty()) return;
    std::vector<unsigned> out(a.size());
    unsigned maxv=*std::max_element(a.begin(),a.end());
    for (unsigned bit=1; bit && bit<=maxv; bit<<=1) {
        std::size_t zeros=0;
        for (unsigned x:a) if (!(x&bit)) ++zeros;
        std::size_t p0=0, p1=zeros;
        for (unsigned x:a) {
            if (x&bit) out[p1++]=x;
            else out[p0++]=x;
        }
        a.swap(out);
    }
}
void merge88(std::vector<int>& a, int m, const std::vector<int>& b, int n) {
    int i=m-1, j=n-1, k=m+n-1;
    while (j>=0) {
        if (i>=0 && a[i]>b[j]) a[k--]=a[i--];
        else a[k--]=b[j--];
    }
}
void parity905(std::vector<int>& a) {
    int i=0, j=static_cast<int>(a.size())-1;
    while (i<j) {
        while (i<j && a[i]%2==0) ++i;
        while (i<j && a[j]%2!=0) --j;
        if (i<j) std::swap(a[i++],a[j--]);
    }
}