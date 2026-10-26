from pathlib import Path
import re, json, hashlib, collections, shutil

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / '信号与系统'
WORK = Path(__file__).resolve().parent
TITLE = 'C3–5 四种傅里叶表示并行讲义'
TARGET = COURSE / (TITLE + '.md')
sources = json.loads((WORK / 'source_inventory.json').read_text())

topics = [
 ('共同起点：复指数、特征函数与频率响应', 'eigen'),
 ('四套公式：正交、有限维与周期趋于无穷', 'formulas'),
 ('四种矩形并排：占空比、半角技巧与时宽带宽', 'rectangle'),
 ('基本信号与周期谱：指数、冲激、常数和正弦', 'pairs'),
 ('收敛与有限近似：四种情形到底各需要什么条件', 'convergence'),
 ('线性：同一组基底上的权重怎样组合', 'linearity'),
 ('时移与相位：幅度不变为什么仍会改变图像', 'shift'),
 ('频移与调制：移频谱为什么要在时域乘复指数', 'modulation'),
 ('共轭、实信号与奇偶分解', 'symmetry'),
 ('反转与尺度：连续伸缩、离散插零和抽取', 'scaling'),
 ('微分、差分、积分与累加', 'calculus'),
 ('帕塞瓦尔：周期看功率，非周期看能量', 'parseval'),
 ('卷积与相乘：普通卷积、周期卷积及归一化', 'convolution'),
 ('LTI 系统、滤波与微分差分方程求解', 'systems'),
 ('对偶、采样与四类信号之间的动作', 'duality'),
 ('性质表、变换表和原有综合题', 'tables'),
 ('原篇导读、完整复盘与阅读线索', 'archive'),
]

# 顺序是原笔记的顶层编号；x 表示完整收尾，p 表示原篇导读。
maps = {
 'C3.1': ['eigen','eigen','eigen','eigen','eigen','eigen','eigen','eigen','eigen','formulas','eigen'],
 'C3.2': ['formulas','formulas','formulas','formulas','rectangle','symmetry'],
 'C3.3': ['convergence','convergence','convergence','convergence','convergence'],
 'C3.4': ['tables','linearity','shift','scaling','scaling','convolution','symmetry','parseval','modulation','calculus','pairs','convolution','tables','tables'],
 'C3.5': ['formulas','formulas','formulas','pairs','rectangle','pairs','tables'],
 'C3.6': ['systems','systems','systems','systems','systems'],
 'C4.1': ['formulas','formulas','convergence','pairs','duality','tables'],
 'C4.2': ['pairs','pairs','pairs','pairs'],
 'C4.3': ['shift','linearity','shift','modulation','symmetry','calculus','scaling','calculus','calculus','duality','parseval','tables','tables'],
 'C4.4': ['systems','convolution','systems','convolution','systems','systems','systems','systems','pairs','systems'],
 'C4.5': ['modulation','convolution','convolution','modulation','modulation','modulation','modulation','modulation','convergence'],
 'C5.1': ['formulas','formulas','formulas','rectangle','pairs','convergence','tables'],
 'C5.2': ['pairs','pairs','pairs','pairs','pairs'],
 'C5.3': ['tables','formulas','linearity','shift','scaling','symmetry','calculus','scaling','calculus','parseval','tables'],
 'C5.4': ['systems','convolution','calculus','systems','systems','systems'],
 'C5.5': ['modulation','convolution','tables','duality','duality','duality'],
}
categories = {'C3.1':'共同基础','C3.2':'CTFS','C3.3':'CTFS','C3.4':'CTFS','C3.5':'DTFS','C3.6':'系统与两类级数','C4.1':'CTFT','C4.2':'CTFT','C4.3':'CTFT','C4.4':'CTFT','C4.5':'CTFT','C5.1':'DTFT','C5.2':'DTFT','C5.3':'DTFT','C5.4':'DTFT','C5.5':'DTFT'}

# 混合性质拆到同一主题下，避免 DTFS 的性质仍缩在单独一章。
split_rules = {
 ('C3.5',6): {'6.1':'convolution','6.2':'calculus','6.3':'scaling','6.4':'parseval','6.5':'tables'},
 ('C4.1',3): {'3.1':'pairs','3.2':'pairs','3.3':'pairs','3.4':'rectangle','3.5':'rectangle','3.6':'pairs'},
 ('C4.2',3): {'3.1':'pairs','3.2':'pairs','3.3':'rectangle'},
 ('C5.3',3): {'3.1':'shift','3.2':'modulation'},
 ('C5.5',1): {'1.1':'convolution','1.2':'convolution','1.3':'modulation'},
}

def clean(s):
    # 只作称谓与排版规范化，知识性正文不删减。
    s = s.replace('课件', '教学材料')
    s = re.sub(r'(?m)^> (\| 帕塞瓦尔[^\n]*)$', r'\1', s)
    for old,new in json.loads((WORK/'attachment_map.json').read_text()).items():
        s=s.replace('![['+old,'![['+new)
    lines=[]
    for line in s.splitlines(keepends=True):
        if re.match(r'^\s*(?:>\s*)?\|',line):
            line=re.sub(r'\$[^$\n]+\$',lambda m: re.sub(r'(?<!\\)\|',r'\\vert ',m.group()),line)
            line=re.sub(r'\[\[([^\]\n]+)\]\]',lambda m:'[['+re.sub(r'(?<!\\)\|',r'\\|',m.group(1))+']]',line)
        lines.append(line)
    s=''.join(lines)
    return s

def render_unit(s, prefix):
    def heading(m):
        hs, txt = m.group(1), m.group(2)
        depth = 4 if m.start()==0 else min(6, len(hs)+2)
        return '#' * depth + ' ' + (prefix + ' · ' if len(hs) <= 3 else '') + txt
    return re.sub(r'(?m)^(#{1,6}) (.+)$', heading, clean(s)).strip()

units=[]
for src in sources:
    prefix=src['file'].split(' ')[0]
    for ui,raw in enumerate(src['units']):
        if not raw.strip(): continue
        first=raw.splitlines()[0]
        match=re.match(r'## (\d+)\.',first)
        n=int(match.group(1)) if match else None
        topic=maps[prefix][n] if n is not None else 'archive'
        rule=split_rules.get((prefix,n))
        parts=re.split(r'(?m)(?=^### )',raw) if rule else [raw]
        for pi,piece in enumerate(parts):
            if not piece.strip():continue
            sub=re.match(r'### (\d+\.\d+)',piece)
            dest=rule.get(sub.group(1),topic) if rule and sub else topic
            units.append({'id':f'{prefix}-u{ui:02d}-p{pi:02d}','file':src['file'],'prefix':prefix,'category':categories[prefix] if dest!='archive' else prefix,'topic':dest,'raw':piece,'rendered':render_unit(piece,prefix)})

intro = (WORK / 'intro.md').read_text()
additions = json.loads((WORK / 'additions.json').read_text())
corrections = json.loads((WORK / 'corrections.json').read_text())
out=[intro.rstrip()]
coverage=[]
for number,(title,key) in enumerate(topics,1):
    out.append(f'\n## {number}. {title}\n')
    out.append(additions.get(key,'').strip())
    members=[u for u in units if u['topic']==key]
    cats=list(dict.fromkeys(u['category'] for u in members))
    desired=['共同基础','CTFS','DTFS','CTFT','DTFT','系统与两类级数']
    cats.sort(key=lambda c: desired.index(c) if c in desired else 20+list(categories).index(c))
    for cat in cats:
        out.append(f'\n### {number} · {cat} · '+('原篇导读与复盘（历史快照）' if key=='archive' else '完整推导、例题与原有讲解')+'\n')
        if key=='archive':
            out.append('以下完整保留原篇的任务导读、历史进度、三句话、速查、预告与相关链接。其“尚未讲授”等说法记录的是原篇当时状态；本讲义的课堂进度以篇首与第 18 节为准。来源材料名集中保留在本讲义来源清单与工作记录中。\n')
        for u in [v for v in members if v['category']==cat]:
            title_line=u['raw'].splitlines()[0]
            warning_key=u['prefix']+'|'+re.sub(r'^#+\s*','',title_line)
            if warning_key in corrections:out.append(corrections[warning_key].strip())
            if key=='archive' and u['raw'].startswith('# '):
                out.append('#### '+u['prefix']+' · 原篇导读\n')
            start=sum(len(x)+2 for x in out)
            out.append(u['rendered'])
            coverage.append({k:u[k] for k in ['id','file','topic','category'] } | {'original_heading':title_line,'sha256_raw':hashlib.sha256(u['raw'].encode()).hexdigest(),'rendered_chars':len(u['rendered'])})

out.append((WORK/'ending.md').read_text().strip())
result='\n\n'.join(out).rstrip()+'\n'
staged=WORK/(TITLE+'.md');staged.write_text(result)
(WORK/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
# 每块的全部正文都在实际成品中，且每个原始字节均属于一个分块。
assert len(coverage)==len(units)
for src in sources:
    retained=''.join(u['raw'] for u in units if u['file']==src['file'])
    original=''.join(src['units'])
    assert retained==original,(src['file'],'原文分割遗漏')
for u in units:
    assert u['rendered'] in result,(u['id'],'成品遗漏')
print(json.dumps({'source_notes':len(sources),'retained_blocks':len(units),'source_body_chars':sum(len(''.join(s['units'])) for s in sources),'output_chars':len(result),'output_bytes':len(result.encode()),'stage':str(staged)},ensure_ascii=False,indent=2))
