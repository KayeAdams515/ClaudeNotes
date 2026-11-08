from itertools import product,combinations
from math import comb
from collections import deque
from fractions import Fraction
import json
out={}
f=[0,1,1]
for n in range(3,14):f.append(f[-1]+f[-2])
out['rabbits']=f[1:7]
a=[sum('00' not in ''.join(s) for s in product('01',repeat=n)) for n in range(11)]
assert all(a[n]==a[n-1]+a[n-2] for n in range(2,11))
assert all(a[n]==f[n+2] for n in range(11))
out['bitstrings_n0_to10']=a
out['valid_length5']=[''.join(s) for s in product('01',repeat=5) if '00' not in ''.join(s)]
even=[sum(s.count('0')%2==0 for s in product('0123456789',repeat=n)) for n in range(5)]
assert all(even[n]==(10**n+8**n)//2 for n in range(5))
assert all(even[n]==8*even[n-1]+10**(n-1) for n in range(1,5))
out['even_zero_codewords_n0_to4']=even
assert '1230407869'.count('0')==2 and '120987045608'.count('0')==3
C=[1]
for n in range(1,11):C.append(sum(C[k]*C[n-k-1] for k in range(n)))
assert C==[comb(2*n,n)//(n+1) for n in range(11)]
out['catalan_n0_to10']=C
# BFS over all legal positions of up to 5 disks; each disk position is its peg.
def hanoi_bfs(n):
 start=(0,)*n;goal=(1,)*n;q=deque([(start,0)]);seen={start}
 while q:
  state,d=q.popleft()
  if state==goal:return d
  tops={}
  for disk,peg in enumerate(state):tops.setdefault(peg,disk)
  for peg,disk in tops.items():
   for dest in range(3):
    if dest!=peg and (dest not in tops or disk<tops[dest]):
     nxt=list(state);nxt[disk]=dest;nxt=tuple(nxt)
     if nxt not in seen:seen.add(nxt);q.append((nxt,d+1))
h=[hanoi_bfs(n) for n in range(1,6)]
assert h==[2**n-1 for n in range(1,6)]
out['hanoi_shortest_bfs_n1_to5']=h
out['hanoi64_seconds']=2**64-1
out['hanoi64_years_365_25_days']=float(Fraction(2**64-1,31557600))
# Times measured as minutes since midnight, independent of p values copied from text.
s=[480,540,630,570,510,660,780];e=[600,660,720,780,840,840,840]
p=[max([i+1 for i in range(j) if e[i]<=s[j]],default=0) for j in range(7)]
assert p==[0,0,1,0,0,2,4]
out['p']=p
weights=[[20,10,50,30,15,25,40],[100,5,10,20,25,40,30],[2,3,8,5,4,7,10],[10,8,7,25,20,30,5]]
for letter,w in zip('abcd',weights):
 T=[0]
 for j in range(7):T.append(max(w[j]+T[p[j]],T[-1]))
 feasible=[]
 for flags in product([0,1],repeat=7):
  ids=[i for i in range(7) if flags[i]]
  if all(e[i]<=s[j] or e[j]<=s[i] for i,j in combinations(ids,2)):
   feasible.append((sum(w[i] for i in ids),[i+1 for i in ids]))
 best=max(v for v,ids in feasible)
 assert T[-1]==best
 j=7;chosen=[]
 while j:
  if w[j-1]+T[p[j-1]]>=T[j-1]:chosen.append(j);j=p[j-1]
  else:j-=1
 out['schedule_'+letter]={'weights':w,'T':T,'best':best,'all_optimal':[ids for v,ids in feasible if v==best],'backtrack':chosen[::-1]}
print(json.dumps(out,ensure_ascii=False,indent=2))
