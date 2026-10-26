from itertools import combinations,permutations,product
from collections import Counter
from math import factorial,comb
import json
import numpy as np
R={}
def edges(s):return [tuple(e) for e in s.split()]
def deg(es,V=None):
 d=Counter(dict.fromkeys(V or [],0))
 for a,b in es:d[a]+=1;d[b]+=1
 return dict(d)
def comps(V,es):
 unseen=set(V);out=[]
 while unseen:
  todo=[unseen.pop()];seen=set(todo)
  while todo:
   a=todo.pop()
   for u,v in es:
    b=v if u==a else u if v==a else None
    if b in unseen:unseen.remove(b);seen.add(b);todo.append(b)
  out.append(seen)
 return out
def conn(V,es):return len(comps(V,es))<=1
def cuts(es):
 V=sorted(set(sum((list(e) for e in es),[])))
 ks=next(k for k in range(len(V)) if any(not conn(set(V)-set(S),[(a,b) for a,b in es if a not in S and b not in S]) for S in combinations(V,k)))
 ls=next(k for k in range(len(es)+1) if any(not conn(V,[e for i,e in enumerate(es) if i not in S]) for S in combinations(range(len(es)),k)))
 return ks,ls
E1=edges('ab af bc be bf cd ce cf ef')
assert list(deg(E1,'abcdefg').values())==[2,4,4,1,3,4,0]
H=edges('ab ad ae ae bb bc bd be de de de')
assert [deg(H)[x] for x in 'abcde']==[4,6,1,5,6]
D=edges('aa ab ac ae bd cc cb dc de ea ed ee')
assert [sum(b==v for a,b in D) for v in 'abcdef']==[2,2,3,2,3,0]
assert [sum(a==v for a,b in D) for v in 'abcdef']==[4,1,2,2,3,0]
R['degrees']={'G':deg(E1,'abcdefg'),'H':deg(H),'directed_edge_count':len(D),'10_vertices_degree6_edges':10*6//2}
# Hall conditions by distinct neighbors; every subset is checked from original capabilities.
caps1={'A':{'r','t'},'B':{'a','i','t'},'C':{'r','a','i'},'D':{'r'}}
caps2={'W':{'a'},'X':{'r','i','t'},'Y':{'a'},'Z':{'r','a','t'}}
for label,caps in [('Project1',caps1),('Project2',caps2)]:
 violations=[]
 for k in range(5):
  for A in combinations('rait',k):
   N={person for person,skills in caps.items() if skills & set(A)}
   if len(N)<len(A):violations.append({'jobs':A,'neighbors':sorted(N)})
 R[label]={'Hall_holds':not violations,'violations':violations}
assert R['Project1']['Hall_holds'] and not R['Project2']['Hall_holds']
# Adjacency matrix is rebuilt from graph edges, not copied from expected matrix power.
V=list('abcd');es=edges('ab ac bd cd');A=np.array([[int((u,v) in es or (v,u) in es) for v in V] for u in V])
A4=np.linalg.matrix_power(A,4);assert A4[0,3]==8
R['A4']=A4.tolist()
Giso={(0,1),(0,3),(1,2),(1,5),(2,3),(3,4),(4,5)}
f=[5,2,3,4,0,1]
Hiso={tuple(sorted((f[a],f[b]))) for a,b in Giso}
assert len(Hiso)==7
R['isomorphism_10_3_example11']={'mapping_1based':[i+1 for i in f],'G_edges_1based':[[a+1,b+1] for a,b in sorted(Giso)],'H_edges_1based':[[a+1,b+1] for a,b in sorted(Hiso)]}
G14=edges('13 14 15 23 25 34');m={'1':'3','4':'2','3':'1','2':'5','5':'4'}
assert {''.join(sorted(m[a]+m[b])) for a,b in G14}==set('12 13 15 23 34 45'.split())
R['isomorphism_10_4_example14']='all six edges and all nonedges preserved'
connexamples=['ab bc bd cd ce ef fg gh eh eg','ab ac bc cd de ef cf','ab ag bg bc gf cf cd fe de','ab ag bg bc gf cf cd ce de df ef af','ab bc cd hg gf fe ah bg cf de ag bh cg ce df bd hf']
R['connectivity']={f'G{i+1}':cuts(edges(s)) for i,s in enumerate(connexamples)}
assert list(R['connectivity'].values())==[(1,1),(1,2),(2,2),(2,3),(3,3)]
R['Konigsberg_degrees']=deg(edges('ab ab ac ac ad bd cd'))
assert sorted(R['Konigsberg_degrees'].values())==[3,3,3,5]
seq='a b d g h j i h k g f d c b e i f e a'.split();uedges=[tuple(sorted((a,b))) for a,b in zip(seq,seq[1:])]
assert len(uedges)==18 and len(set(uedges))==18 and all(v%2==0 for v in deg(uedges).values())
R['scimitar']={'edge_count':18,'degrees':deg(uedges)}
gray=['000','001','011','010','110','111','101','100']
assert len(set(gray))==8
changes=[int(a,2)^int(b,2) for a,b in zip(gray,gray[1:]+gray[:1])];assert all(x and x&(x-1)==0 for x in changes)
R['gray_xor']=changes

def shortest(V,E,start):
 d={v:float('inf') for v in V};d[start]=0;prev={};done=set();rows=[]
 while len(done)<len(V):
  u=min((v for v in V if v not in done),key=d.get)
  done.add(u)
  for a,b,w in E:
   v=b if a==u else a if b==u else None
   if v is not None and v not in done and d[u]+w<d[v]:d[v]=d[u]+w;prev[v]=u
  rows.append([u,{v:d[v] if d[v]!=float('inf') else 'infinity' for v in V}])
 return d,prev,rows
E=[('a','b',4),('a','d',2),('b','c',3),('b','e',3),('d','e',3),('c','z',2),('e','z',1)]
assert shortest(list('abcdez'),E,'a')[0]['z']==6
E2=[('a','b',4),('a','c',2),('b','c',1),('b','d',5),('c','d',8),('c','e',10),('d','e',2),('d','z',6),('e','z',3)]
d,p,rows=shortest(list('abcdez'),E2,'a');assert d['z']==13
# Cross-check with all-pairs dynamic programming, independently of greedy vertex selection.
V=list('abcdez');F=[[0 if i==j else float('inf') for j in V] for i in V]
for a,b,c in E2:i=V.index(a);j=V.index(b);F[i][j]=F[j][i]=c
for k in range(len(V)):
 for i in range(len(V)):
  for j in range(len(V)):F[i][j]=min(F[i][j],F[i][k]+F[k][j])
assert F[0][-1]==13
R['Dijkstra_example2']=rows
# Five-city TSP, all original ten edge weights, enumerate 24 tours.
V='DTSGK';ws={'DT':58,'DS':98,'DG':147,'DK':135,'TS':142,'TG':167,'TK':133,'SG':113,'SK':137,'GK':56}
def weight(a,b):return ws.get(a+b,ws.get(b+a))
tours=[]
for perm in permutations(V[1:]):
 route=('D',)+perm+('D',);tours.append((''.join(route),sum(weight(a,b) for a,b in zip(route,route[1:]))))
expect={'DTGSKD':610,'DTGKSD':516,'DTKSGD':588,'DTKGSD':458,'DTSKGD':540,'DTSGKD':504,'DSTGKD':598,'DSTKGD':576,'DSKTGD':682,'DSGTKD':646,'DGSTKD':670,'DGTSKD':728}
assert all(dict(tours)[k]==v for k,v in expect.items()) and min(v for k,v in tours)==458
R['TSP']={'table':expect,'all_optimal':[k for k,v in tours if v==458],'25_city_candidates':factorial(24)//2,'years_at_1ns_each':(factorial(24)//2)*1e-9/31557600}

def coloring(V,es,k):
 ad={v:set() for v in V}
 for a,b in es:ad[a].add(b);ad[b].add(a)
 order=sorted(V,key=lambda v:-len(ad[v]));C={}
 def go(i):
  if i==len(V):return C.copy()
  u=order[i]
  for c in range(k):
   if all(C.get(v)!=c for v in ad[u]):
    C[u]=c;r=go(i+1)
    if r is not None:return r
    C.pop(u)
  return None
 return go(0)
CG=edges('ab ac bc bd cd be cf de df ef eg fg');CH=CG+[('a','g')]
assert coloring('abcdefg',CG,2) is None and coloring('abcdefg',CG,3)
assert coloring('abcdefg',CH,3) is None and coloring('abcdefg',CH,4)
exam=edges('12 13 14 17 23 24 25 27 34 36 37 45 46 56 57 67')
C={'1':1,'6':1,'2':2,'3':3,'5':3,'4':4,'7':4}
assert all(C[a]!=C[b] for a,b in exam) and coloring('1234567',exam,3) is None
R['chromatic']={'G':3,'H':4,'exam':4,'exam_witness':C}
# Original map dual graphs and the specific color sets printed in the note.
left=edges('AB AC AD BC BD CD AE DE DF DG EF EG FG');right=edges('AB AC AD BC BE CD CE DE')
cl={'A':1,'G':1,'B':2,'E':2,'C':3,'F':3,'D':4};cr={'A':1,'E':1,'B':3,'D':3,'C':2}
assert all(cl[a]!=cl[b] for a,b in left) and coloring('ABCDEFG',left,3) is None
assert all(cr[a]!=cr[b] for a,b in right) and coloring('ABCDE',right,2) is None
R['map_chromatic']=[4,3]
R['planar']={'20_degree3':{'edges':20*3//2,'regions':20*3//2-20+2},'K5':[5,10,3*5-6],'K33':[6,9,2*6-4],'subdivided_K5':[15,20]}
# Weight tuples transcribed from the three original versions of each network.
air=[('SF','NY',2534,245,129),('SF','C',1855,175,99),('SF','D',957,140,89),('SF','LA',349,75,39),('LA','D',834,120,89),('D','C',908,130,69),('LA','NY',2451,230,129),('C','B',860,130,79),('C','NY',722,110,59),('C','A',606,100,99),('NY','B',191,50,39),('NY','A',760,115,79),('NY','M',1090,165,99),('A','M',595,90,69)]
network=[('SF','LA',349,3,400),('SF','D',957,4,1000),('SF','C',1855,5,1500),('LA','D',1736,7,1400),('LA','DA',1235,5,1100),('D','C',908,6,500),('D','DA',645,4,600),('C','DA',798,5,800),('C','B',860,3,900),('C','NY',722,4,700),('DA','NY',1372,6,1200),('B','NY',191,2,300)]
for label,data,start,end in [('airline',air,'B','LA'),('network',network,'SF','NY')]:
 values=[];verts=sorted({v for row in data for v in row[:2]})
 for index in [2,3,4]:
  ds,pr,rr=shortest(verts,[(row[0],row[1],row[index]) for row in data],start)
  route=[end]
  while route[-1]!=start:route.append(pr[route[-1]])
  values.append({'value':ds[end],'route':route[::-1]})
 R[label]=values
print(json.dumps(R,ensure_ascii=False,indent=2))
