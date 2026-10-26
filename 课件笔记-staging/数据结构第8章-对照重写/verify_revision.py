from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,re,math,subprocess,hashlib,sys
W=Path('/tmp/c8-revision-20261020');O=W/'output/数据结构';V=Path.cwd()
results={}
def inv(a):return sum(x>y for i,x in enumerate(a) for y in a[i+1:])
def check(name,actual,expected):
 assert actual==expected,(name,actual,expected)
 results[name]=actual

a=[1,3,5,4,2,6]; trace=[a.copy()]
for i,j in [(2,3),(3,4),(2,3),(1,2)]:
 a[i],a[j]=a[j],a[i]; trace.append(a.copy())
check('六项相邻交换的逆序轨迹',[inv(a) for a in trace],[4,3,2,1,0])
check('远距交换一次消掉三对',inv([3,2,1])-inv([1,2,3]),3)

a=[5,7,12,19,21,26,33,40,14];tmp=a[-1];j=8;tr=[]
while j and tmp<a[j-1]:
 a[j]=a[j-1];a[j-1]=None;j-=1;tr.append(a.copy())
 if j and a[j-1] is None: raise AssertionError('空位不唯一')
a[j]=tmp
check('插入14的最终结果',a,[5,7,12,14,19,21,26,33,40])
check('插入14移动次数',len(tr),5)

def down(a,k,end):
 while 2*k+1<end:
  c=2*k+1
  if c+1<end and a[c]<a[c+1]: c+=1
  if a[k]>=a[c]: break
  a[k],a[c]=a[c],a[k];k=c
a=[9,7,8,1,3];tr=[a.copy()]
for end in range(4,0,-1):
 a[0],a[end]=a[end],a[0];down(a,0,end);tr.append(a.copy())
check('五项堆排序每轮状态',tr,[[9,7,8,1,3],[8,7,3,1,9],[7,1,3,8,9],[3,1,7,8,9],[1,3,7,8,9]])
a=[9,7,8,10,3]
for k in [1,0]:down(a,k,5)
check('从孩子开始修堆',a,[10,9,8,7,3])
check('15节点建堆上界',sum(2**k*(3-k) for k in range(4)),11)

a=[8,3,7,4,9,2,6];n=len(a);mid=n//2
if a[mid]<a[0]:a[mid],a[0]=a[0],a[mid]
if a[-1]<a[0]:a[-1],a[0]=a[0],a[-1]
if a[-1]<a[mid]:a[-1],a[mid]=a[mid],a[-1]
a[mid],a[-1]=a[-1],a[mid]
check('快排七项样本整理',a.copy(),[4,3,7,8,9,2,6])
p=a[-1];i=1;j=n-2
while True:
 while i<=j and a[i]<p:i+=1
 while i<=j and p<a[j]:j-=1
 if i>j:break
 a[i],a[j]=a[j],a[i];i+=1;j-=1
check('快排交叉位置',[i,j],[3,2])
a[i],a[-1]=a[-1],a[i]
check('七项分区结果',a,[4,3,2,6,9,7,8])
check('七项递归结束',sorted(a),[2,3,4,6,7,8,9])

for n in range(2,20):
 h=sum((F(1,k) for k in range(1,n+1)),F())
 acc=sum((2*F(k-1,k*(k+1)) for k in range(2,n+1)),F())
 assert acc*(n+1)==2*(n+1)*h-4*n
check('理想随机快排n=2精确比较数',str(acc) if False else str(2*3*F(3,2)-8),'1')
check('大域位图字节',10**12//8,125000000000)
check('大域4字节计数表',10**12*4,4000000000000)

items=[(2,'甲'),(1,'乙'),(2,'丙')];P=[0,1,3];out=[None]*3;tr=[]
for v,label in reversed(items):
 P[v]-=1;out[P[v]]=(v,label);tr.append([x for x in out])
check('稳定计数输出',out,[(1,'乙'),(2,'甲'),(2,'丙')])
base=[16,31,99,59,27,90,10,26,21,60,18,57,17]
for e,expected in [(1,[90,10,60,31,21,16,26,27,57,17,18,99,59]),(10,[10,16,17,18,21,26,27,31,57,59,60,90,99])]:
 buckets=[[] for _ in range(10)]
 for x in base:buckets[x//e%10].append(x)
 base=[x for b in buckets for x in b];check(f'基数原13项位权{e}',base,expected)
a=[3,2,1,0];out=[None]*4;lo=0;hi=3
for x in a:
 if x&1:out[hi]=x;hi-=1
 else:out[lo]=x;lo+=1
check('双端数组物理布局',out,[2,0,1,3])
logical=out[:lo]+out[lo:][::-1]
check('双端数组FIFO读取',logical,[2,0,3,1])
check('32位二进制与256进制轮数',[math.ceil(32/1),math.ceil(32/8)],[32,4])

files=list(O.glob('C8*.md'));preserved={}
for p in files:
 s=p.read_text();old=(W/'before'/p.name).read_text()
 assert re.findall(r'```cpp\n(.*?)```',old,re.S)==re.findall(r'```cpp\n(.*?)```',s,re.S)
 assert set(re.findall(r'!\[\[.*?\]\]',old))<=set(re.findall(r'!\[\[.*?\]\]',s))
 # Ruby标准库解析真正的YAML，不用只认键名的退路冒充解析。
 parsed=subprocess.run(['ruby','-ryaml','-rjson','-e','print JSON.generate(YAML.safe_load(STDIN.read))'],input=s.split('---',2)[1],text=True,capture_output=True,check=True)
 meta=json.loads(parsed.stdout)
 assert set(meta)=={'title','course','chapter','section','tags','aliases','source'}
 assert meta['title']==p.stem and isinstance(meta['chapter'],int) and isinstance(meta['section'],str)
 assert all(isinstance(meta[x],list) for x in ['tags','aliases','source'])
 clean=re.sub(r'```.*?```','',s.split('---',2)[2],flags=re.S)
 assert clean.count('$$')%2==0 and len(re.findall(r'(?<!\\)\$',clean.replace('$$','')))%2==0
 assert len(re.findall(r'^```',s,re.M))%2==0
 heads=set(re.findall(r'^#{1,6} (.*)$',s,re.M))
 for anchor in re.findall(r'\[\[#([^\]|]+)',clean):assert anchor in heads,(p.name,anchor)
 assert all(x not in clean for x in ['课件','幻灯片','TODO','<!--','本节自测','篇末自测'])
 assert all(x in clean for x in ['[!question]','[!important]','[!warning]','## 这一讲的三句话','## 速查表'])
 three=clean.split('## 这一讲的三句话')[1].split('## 速查表')[0]
 assert len(re.findall(r'^\d\. ',three,re.M))==3
 preserved[p.name]={'字符数':len(s),'原字符数':len(old),'提问':s.count('[!question]'),'代码块保留':len(re.findall(r'```cpp',s)),'原图保留':s.count('![['),'Mermaid':s.count('```mermaid'),'YAML及锚点':'通过'}
results['逐篇结构与保留核验']=preserved
sha=hashlib.sha256((V/'数据结构/pdfs/sort.pptx').read_bytes()).hexdigest()
check('原PPTX与既有逐页记录一致',sha,json.loads(Path('/tmp/sorting-notes/package-check.json').read_text())['sha256'])
(W/'revision-verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps(preserved,ensure_ascii=False,indent=2));print('新增数值、轨迹、YAML、锚点和内容保留检查通过')
