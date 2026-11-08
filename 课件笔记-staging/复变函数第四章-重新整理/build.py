from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent
vault=root/'vault'/'复变函数'
meta=[
('C4.1 实参数复值函数的微积分', '41–42',1,6, ['实参数','复积分']),
('C4.2 围道与复积分的定义','43–44',6,13,['围道','复积分']),
('C4.3 参数积分、路径依赖与分支','45–46',13,21,['路径依赖','分支']),
('C4.4 积分估计与 ML 不等式','47',21,26,['积分估计','ML不等式']),
('C4.5 原函数与路径无关','48–49',26,33,['原函数','路径无关']),
('C4.6 柯西-古尔萨定理及其证明','50–51',34,40,['柯西古尔萨定理','证明']),
('C4.7 单连通、复连通与路径变形','52–53',40,48,['单连通','路径变形']),
('C4.8 柯西积分公式与高阶导数','54–56',48,54,['柯西积分公式','高阶导数']),
('C4.9 解析性的推论、柯西估计与刘维尔定理','57–58',54,59,['柯西估计','刘维尔定理']),
('C4.10 最大模原理与调和函数的极值','59',59,64,['最大模原理','调和函数'])]
json.dump(meta,open(root/'meta.json','w'),ensure_ascii=False,indent=2)
for i,(name,sec,a,b,tags) in enumerate(meta):
    old=(root/'backup'/(name+'.md.bak')).read_text()
    fm=old.split('---',2)[1].strip()
    # 既有键和值类型原样保留，只重写正文。
    body=(root/f'body-{i+1:02d}.txt').read_text()
    prev=meta[i-1][0] if i else 'C3.7 反三角与反双曲函数'
    nxt=meta[i+1][0] if i<9 else None
    nav=f'[[{prev}|上一讲]] ｜ '+(f'[[{nxt}|下一讲]]' if nxt else '第四章终点（第五章笔记尚未建立）')+' ｜ [[复变函数 MOC|返回课程索引]]'
    (vault/(name+'.md')).write_text('---\n'+fm+'\n---\n\n# '+name+'\n\n'+body.strip()+'\n\n---\n\n'+nav+'\n')
print('10 notes built')
