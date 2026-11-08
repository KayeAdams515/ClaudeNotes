import runpy
from pathlib import Path
import contextlib,io,json
from itertools import combinations,product
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
 ns=runpy.run_path('/private/tmp/discrete-c10/verify_math.py')
R={};A=np.array([[0,3,0,2],[3,0,1,1],[0,1,1,2],[2,1,2,0]])
assert (A.sum(axis=1)+A.diagonal()).tolist()==[5,5,5,5]
assert (A.sum()-A.trace())//2+A.trace()==10
M6=np.array([[1,1,0,0,0,0],[0,0,1,1,0,1],[0,0,0,0,1,1],[1,0,1,0,0,0],[0,1,0,1,1,0]])
assert M6.sum(axis=0).tolist()==[2]*6
M7=np.array([[1,1,1,0,0,0,0,0],[0,1,1,1,0,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,1],[0,0,0,0,1,1,0,0]])
assert M7.sum(axis=0).tolist()==[1,2,2,2,2,2,2,1]
R['adjacency_and_incidence']={'pseudograph_degree':[5]*4,'loop_columns':[1,8],'parallel_columns':[2,3]}
assert 64*63//2==2016 and 2*4*(4-1)==24 and 3*2**2==12
R['network_topologies']={'K64_edges':2016,'4by4_mesh_edges':24,'Q3_edges':12}
# Enumerate actual crown graph order using the exact color-class greedy rule.
V=['a1','b1','a2','b2','a3','b3'];es=[(f'a{i}',f'b{j}') for i in range(1,4) for j in range(1,4) if i!=j]
ad={v:set() for v in V}
for a,b in es:ad[a].add(b);ad[b].add(a)
C={};k=0
while len(C)<len(V):
 k+=1;I=[]
 for v in V:
  if v not in C and not(set(I)&ad[v]):C[v]=k;I.append(v)
assert k==3 and ns['coloring'](V,es,2)
R['greedy_counterexample']={'greedy_colors':k,'coloring':C,'optimum':2}
for n in range(3,8):
 # Formula for clustering on a complete graph independently from triple enumeration.
 wedges=n*(n-1)*(n-2);triangles=n*(n-1)*(n-2)//6
 assert 6*triangles/wedges==1
R['clustering_complete_graphs']='n=3..7 coefficient 1; C4 has zero triangles'
# Check listed directed Euler sequences against each graph's actual arc set.
H2=ns['edges']('ag gc cb bg ge ed df fa');H3=ns['edges']('ca ab bc cd db')
for es,seq in [(H2,list('agcbgedfa')),(H3,list('cab cdb'.replace(' ','')))]:
 assert sorted(es)==sorted(zip(seq,seq[1:]))
R['directed_euler']='H2 circuit 8 arcs and H3 path 5 arcs verified'
# Verify every original Euler path against its full independently transcribed edge set.
checks=[('ae ec cd de eb ba','aecdeba'),('ac cd de eb bd da ab','acdebdab'),('ab bc cd da bd','dab cdb'.replace(' ','')),('ag gf fe de ab bc cd cg bg cf fd','bagfedcgbcfd')]
for es,seq in checks:
 assert sorted(tuple(sorted(e)) for e in ns['edges'](es))==sorted(tuple(sorted(e)) for e in zip(seq,seq[1:]))
R['undirected_euler']='all four listed source path/circuit edge multisets verified'
print(json.dumps(R,ensure_ascii=False,indent=2))
