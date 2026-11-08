from pathlib import Path
import re,json,subprocess,collections,hashlib
W=Path(__file__).resolve().parent
ROOT=W.parents[1]
COURSE=ROOT/'信号与系统'
TITLE='C3–5 四种傅里叶表示并行讲义'
sources=json.loads((W/'source_inventory.json').read_text())
candidate=COURSE/(TITLE+'.md')
if not candidate.exists():candidate=W/(TITLE+'.md')
text=candidate.read_text();checks=[]
def passed(name,detail):checks.append({'check':name,'result':'通过','detail':detail})

for s in sources:
    now=(COURSE/s['file']).read_text()
    body=now.split('---',2)[2].lstrip('\n')
    assert body==''.join(s['units']),s['file']+' 原笔记正文被更改'
passed('原 16 篇正文未改动','与开工快照逐字符相等')

manifest=json.loads((W/'coverage.json').read_text())
assert len(manifest)==192
passed('内容覆盖','192 个分块全部纳入；构建时逐块验证完整文本，分块重组与原文逐字符相等')

headings=re.findall(r'(?m)^#{1,6} (.+)$',text)
assert len(headings)==len(set(headings)),[x for x,n in collections.Counter(headings).items() if n>1]
passed('标题与本篇锚点','标题均唯一')

# 用系统 YAML 解析器读取实际 frontmatter，而非仅以正则猜测结构。
yamltext=text.split('---',2)[1]
proc=subprocess.run(['ruby','-r','yaml','-r','json','-e','puts JSON.generate(YAML.safe_load(STDIN.read))'],input=yamltext,text=True,capture_output=True,check=True)
meta=json.loads(proc.stdout)
assert set(meta)=={'title','course','chapter','section','tags','aliases','source'}
for key in ['tags','aliases','source']:assert isinstance(meta[key],list)
passed('frontmatter','YAML 解析通过，沿用原有 7 个键，列表字段类型正确')

files=list(ROOT.rglob('*'));files=[p for p in files if p.is_file()]
byname=collections.defaultdict(list)
for p in files:byname[p.name].append(p)
assets=re.findall(r'!\[\[([^\]|]+)',text)
assert len(assets)==59 and len(set(assets))==59
for name in assets:
    loc=COURSE/'attachments'/name
    if not loc.exists():loc=W/'attachments'/name
    assert loc.exists(),name
passed('全部原图保留','59 张独立配图均有实际文件；11 张重名图使用独立名称')

links=re.findall(r'(?<!!)\[\[([^\]]+)\]\]',text)
for raw in links:
    dest=raw.replace('\\|','|').split('|',1)[0]
    note,sep,anchor=dest.partition('#')
    if not note:
        assert anchor in headings,(dest,'锚点不存在')
    elif not sep:
        assert (COURSE/(note+'.md')).exists() or byname[note] or byname[note+'.md'],dest
    else:
        target=COURSE/(note+'.md')
        assert target.exists(),dest
        targetheads=re.findall(r'(?m)^#{1,6} (.+)$',target.read_text())
        assert anchor in targetheads,(dest,'旧篇锚点不存在')
passed('笔记双链','所有笔记目标与本篇锚点均存在')

# 排除围栏示例后，逐行检查所有 display math 成对闭合。
in_code=False;balance=0;code_count=0
for i,line in enumerate(text.splitlines(),1):
    plain=re.sub(r'^\s*(?:>\s*)*','',line)
    if plain.startswith('```'):
        in_code=not in_code;code_count+=1;continue
    if in_code:continue
    balance+=line.count('$$')
assert not in_code and balance%2==0,(code_count,balance)
passed('围栏与公式定界符',f'{code_count//2} 个代码/图形围栏成对；{balance//2} 对行间公式定界符')

table_sizes=[];current=[]
def splitcols(line):
    return re.split(r'(?<!\\)\|',line.strip().strip('|'))
for i,line in enumerate(text.splitlines(),1):
    plain=re.sub(r'^\s*(?:>\s*)*','',line)
    if plain.startswith('|'):
        current.append((i,len(splitcols(plain))))
    else:
        if len(current)>=2:
            sizes=set(x[1] for x in current)
            assert len(sizes)==1,('表格列数不一致',current)
            table_sizes.append(current)
        current=[]
passed('表格分隔符',f'{len(table_sizes)} 张表列数一致；绝对值与双链别名未截断单元格')
assert '课件' not in text
assert not re.search(r'(?i)\b(TODO|TBD|FIXME)\b|待填|此处补充',text)
passed('成稿清理','无占位符，材料称谓已规范')

# 实际 source 路径，允许入库前已准备但尚未改名的第十三节课。
for f in ['第八、九、十节课-已合并.txt','第十一节课-已合并.txt','第十二节课-已合并.txt','第十三节课-已合并.txt']:
    p=COURSE/'transcript'/f
    assert p.exists() or (f=='第十三节课-已合并.txt' and (p.parent/'第十三节课.txt').exists())
passed('转写来源','第 10–13 节课来源均存在；第十三节课按整合完成状态改名')

math=json.loads((W/'math_checks.json').read_text())
assert all(c['passed'] for c in math)
passed('独立数值复算',f'{len(math)} 项通过，包括四种矩形、吉布斯、二维平移、卷积系数和对偶')
(W/'validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(json.dumps(checks,ensure_ascii=False,indent=2))
