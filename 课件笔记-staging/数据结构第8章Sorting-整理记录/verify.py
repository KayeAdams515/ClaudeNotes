from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import math,json,itertools,re
W=Path('/private/tmp/sorting-notes');O=W/'output'/'数据结构'
report={}
def inv(a):return sum(x>y for i,x in enumerate(a) for y in a[i+1:])
examples=[[1,16,12,26,25,35,33,58,45,42,56,67,83,75,74,86,81,88,99,95],[1,17,21,42,24,27,32,35,45,47,57,23,66,69,70,76,87,85,95,99],[22,20,81,38,95,84,99,12,79,44,26,87,96,10,48,80,1,31,16,92]]
assert [inv(x) for x in examples]==[13,13,100]
a=list(map(int,'''61 548 3 923 195 973 289 237 57 299 594 928 515 55 507 351 262 797 788 442 97 798 227 127 474 825 7 182 929 852 504 485 45 98 538 476 175 374 523 800 19 901 349 947 613 265 844 811 636 859 81 270 697 563 976 539'''.split()));assert len(a)==56 and inv(a)==646
report['inversions']=[13,13,100,inv(a)];report['fixed_positions']=[sum(x==y for x,y in zip(a,sorted(a))) for a in examples]
a=list(map(int,'0 3 2 8 5 3 7 5 3 2 8 2 3 5 1 3 2 8 5 3 4 9 2 3 5 1 0 9 3 5 2 3 5 4 2 1 3'.split()))
report['counts']=[a.count(x) for x in range(10)];assert report['counts']==[2,3,7,10,2,7,0,1,3,2]
assert [a[:10].count(x) for x in range(10)]==[1,0,2,3,0,2,0,1,1,0]
def heap(a,record=False):
 a=a.copy();rows=[]
 def down(k,end):
  while 2*k+1<end:
   c=2*k+1
   if c+1<end and a[c]<a[c+1]:c+=1
   if a[k]>=a[c]:break
   a[k],a[c]=a[c],a[k];k=c
 for k in range(len(a)//2-1,-1,-1):down(k,len(a))
 built=a.copy();rows.append(('建堆',' '.join(map(str,a))))
 for end in range(len(a)-1,0,-1):
  a[0],a[end]=a[end],a[0];down(0,end);rows.append((f'固定 {a[end]}',' '.join(map(str,a[:end]))+' ｜ '+' '.join(map(str,a[end:]))))
 assert a==sorted(a);return built,rows
h21=[81,13,77,24,35,61,48,3,23,87,92,95,74,57,99,86,28,15,55,7,51]
report['heap21']=heap(h21)[0]
assert report['heap21']==[99,92,95,86,87,81,77,28,55,51,35,61,74,57,48,3,24,15,23,7,13]
def table(rows,head):return '| '+head[0]+' | '+head[1]+' |\n| --- | --- |\n'+'\n'.join('| '+x+' | `'+y+'` |' for x,y in rows)+'\n'
p=O/'C8.3 堆排序.md';s=p.read_text();s=s.replace('<!-- HEAP_EXERCISE -->',table(heap([34,15,65,59,79,42,40,80,50,61,23,46])[1],['操作','堆前缀与有序后缀']));p.write_text(s)
def quick(a,cutoff):
 a=a.copy();rows=[]
 def rec(l,r):
  if r-l<=cutoff:
   a[l:r]=sorted(a[l:r]);rows.append((f'插入 [{l},{r})',' '.join(map(str,a[l:r]))));return
  m=l+(r-l)//2
  if a[m]<a[l]:a[m],a[l]=a[l],a[m]
  if a[r-1]<a[l]:a[r-1],a[l]=a[l],a[r-1]
  if a[r-1]<a[m]:a[r-1],a[m]=a[m],a[r-1]
  a[m],a[r-1]=a[r-1],a[m];pivot=a[r-1];i=l+1;j=r-2
  while True:
   while i<=j and a[i]<pivot:i+=1
   while i<=j and a[j]>pivot:j-=1
   if i>j:break
   a[i],a[j]=a[j],a[i];i+=1;j-=1
  a[i],a[r-1]=a[r-1],a[i];rows.append((f'[{l},{r}) 枢轴{pivot}→{i}',' '.join(map(str,a[l:r]))));rec(l,i);rec(i+1,r)
 rec(0,len(a));return a,rows
inp=[34,15,65,59,68,42,40,80,50,65,23];out,rows=quick(inp,4);assert out==sorted(inp)
report['quick_exercise']=rows
p=O/'C8.5 快速排序.md';s=p.read_text();s=s.replace('<!-- QUICK_EXERCISE -->',table(rows,['任务','该区间完成当前操作后']))
s=s.replace('| `[5,14)` | 样本48、3、35，取35？先核对当前数组：样本48、3、35已在前轮改变，不能沿用初始值 | 以随后说明的实际状态为准 |','| `[5,14)` | 样本48、51、35，取48；固定在10 | `[5,10)`、`[11,14)` |')
s=s.replace('上表最后一行刻意暴露手算时的常见误法：**不能用前一轮交换之前的三样本选下一轮枢轴**。','手算时**必须从当前数组选样本，不能沿用前一轮交换之前的数值**。')
p.write_text(s)
def radix_rows(a,d,b=2,fmt=lambda x:str(x)):
 rows=[]
 for k in range(d):
  a=sorted(a,key=lambda x:x//b**k%b);rows.append((f'第{k+1}轮，位权 {b**k}',' '.join(fmt(x) for x in a)))
 return rows
p=O/'C8.7 基数排序.md';s=p.read_text();s=s.replace('<!-- BINARY_FIVE -->',table(radix_rows([15,27,25,16,26,5,28,7,11,21],5,fmt=lambda x:format(x,'05b')),['轮次','逻辑收集顺序']))
s=s.replace('<!-- BINARY_THREE -->',table(radix_rows([6,7,1,3,5,2,0,4,2,1,7,2,1,3,5,2,7,5,0,4],3),['轮次','逻辑收集顺序（十进制）']));p.write_text(s)
# 所有涉及小数的结论由原输入重算
H=lambda p:-p*math.log(p)-(1-p)*math.log(1-p)
report['numeric']={'MiB':10**7/8/1024**2,'GiB':10**10/1024**3,'depth3':math.log(.5)/math.log(11/16),'depth1':math.log(.5)/math.log(.75),'entropy1':math.log(2)/H(.25),'entropy3':math.log(2)/H(5/16),'entropy_ninther':math.log(2)/H(469/1280),'ninther_ratio':811/469,'ninther_depth':math.log(.5)/math.log(811/1280)}
F3=lambda x:3*x*x-2*x*x*x
G=lambda x:F3(F3(x))
for key,fn in [('three',F3),('ninther',G)]:
 l=0.;r=.5
 for _ in range(100):
  m=(l+r)/2
  if fn(m)<.05:l=m
  else:r=m
 report['numeric'][key+'_tail']=r;report['numeric'][key+'_90ratio']=(1-r)/r
# 分数多项式验证ninther期望，不依赖浮点
mul=lambda a,b:[sum((a[i]*b[k-i] for i in range(len(a)) if 0<=k-i<len(b)),F(0)) for k in range(len(a)+len(b)-1)]
f=[F(0),F(0),F(3),F(-2)]; one_minus=[F(1),F(0),F(-3),F(2)];der=[F(0),F(6),F(-6)]
g=[6*x for x in mul(mul(f,one_minus),der)]
expect=sum((2*c*F(1,2)**(k+2)/F(k+2) for k,c in enumerate(g)),F(0));assert expect==F(469,1280)
report['ninther_exact']=str(expect)
# 归并例每个最终段直接从原始相应区间重算
base=[13,77,49,35,61,48,73,23,95,3,89,37,57,99,17,32,94,28,15,55,7,51,88,97,62]
report['merge_ranges']={f'{l}:{r}':sorted(base[l:r]) for l,r in [(0,6),(6,12),(0,12),(12,18),(18,21),(21,25),(18,25),(12,25),(0,25)]}
report['quick25']=quick(base,6)[1]
(W/'numeric-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report['numeric'],indent=2));print('numeric and trace checks passed')
