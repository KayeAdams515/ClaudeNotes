from pathlib import Path
import re,json,subprocess,sys,hashlib,collections
r=Path(__file__).resolve().parent;live=r.parents[1];v=r/'vault'/'复变函数'
if '--final' in sys.argv:v=live/'复变函数'
# 将表格数学绝对值改为显式定界符，避免 Markdown 切列。只处理本次 C4 文本。
if '--fix' in sys.argv:
 for p in v.glob('C4*.md'):
  lines=[]
  for line in p.read_text().splitlines():
   if line.startswith('|'):
    def cv(m):
     t=m.group();parts=t.split('|')
     if len(parts)>1:
      assert (len(parts)-1)%2==0,(p,t)
      t=''.join(part+(('\\lvert ' if i%2==0 else '\\rvert ') if i<len(parts)-1 else '') for i,part in enumerate(parts))
     return t
    line=re.sub(r'\$[^$\n]+\$',cv,line)
   lines.append(line)
  p.write_text('\n'.join(lines)+'\n')
files=sorted(v.glob('C4*.md'))+[v/'复变函数 MOC.md']
errors=[];checks=[]
allfiles=collections.defaultdict(list)
# 将暂存成果作为覆盖层，排除备份与所有其他暂存目录，避免把重复名误判为有效目标。
for p in live.rglob('*'):
 if p.is_file() and not any(x.startswith('.') for x in p.relative_to(live).parts) and '课件笔记-staging' not in p.parts:
  allfiles[p.name].append(p)
for p in v.rglob('*'):
 if p.is_file():
  target=live/'复变函数'/p.relative_to(v)
  allfiles[p.name]=[x for x in allfiles[p.name] if x!=target]+[p]
for p in files:
 s=p.read_text();assert s.startswith('---\n')
 fm=s.split('---',2)[1]
 keys=re.findall(r'^([A-Za-z_]+):',fm,re.M)
 if len(keys)!=len(set(keys)):errors.append((p.name,'duplicate keys'))
 bp=r/'backup'/p.name
 if not bp.exists():bp=bp.with_name(bp.name+'.bak')
 old=bp.read_text().split('---',2)[1]
 if fm.strip()!=old.strip():errors.append((p.name,'frontmatter modified'))
 # 使用系统 Ruby 的 YAML 解析器验证完整属性及类型。
 result=subprocess.run(['/usr/bin/ruby','-ryaml','-rjson','-e','x=YAML.safe_load(STDIN.read); puts JSON.generate(x.transform_values{|v| v.class.name})'],input=fm,text=True,capture_output=True)
 if result.returncode:errors.append((p.name,'YAML parse',result.stderr))
 else:checks.append((p.name,'YAML types',json.loads(result.stdout)))
 body=s.split('---',2)[2]
 codefree=re.sub(r'```.*?```','',body,flags=re.S)
 if body.count('```')%2:errors.append((p.name,'fence imbalance'))
 if codefree.count('$$')%2:errors.append((p.name,'display math imbalance'))
 remainder=codefree.replace('$$','')
 if len(re.findall(r'(?<!\\)\$',remainder))%2:errors.append((p.name,'inline math imbalance'))
 for match in re.finditer(r'(!?)\[\[([^\]]+)\]\]',codefree):
  embedded=match[1]=='!';t=match[2].split('|')[0].split('#')[0].replace('\\','').strip();key=Path(t).name
  if not embedded and not key.endswith('.md'):key+='.md'
  if key not in allfiles:errors.append((p.name,'missing link',t))
  elif embedded and len(allfiles[key])!=1:errors.append((p.name,'nonunique image',t))
 if p.name.startswith('C4.'):
  for banned in ['课件','TODO','TBD','待补充','篇末自测','解析与说明','题目与思路']:
   if banned in body:errors.append((p.name,'banned phrase',banned))
  if len(re.findall(r'^## 这一讲的三句话$',body,re.M))!=1:errors.append((p.name,'missing recap'))
  if not re.search(r'^## 0\. 开场',body,re.M):errors.append((p.name,'missing opening'))
  # Mermaid以外普通段落应占正文主体。
  n=sum(len(x) for x in body.splitlines() if x and not x.startswith(('>','#','|','```')))
  checks.append((p.name,'characters',len(body),'ordinary_prose',n))
 # 每个表格的列数必须一致（双链别名管道先屏蔽）。
 table=[]
 for i,line in enumerate(body.splitlines()+[''],1):
  if line.startswith('|'):
   line=re.sub(r'\[\[.*?\]\]','LINK',line)
   n=len(re.findall(r'(?<!\\)\|',line))
   if table and n!=table[0][1]:errors.append((p.name,'table column mismatch',i,n,table[0]))
   table.append((i,n))
  else:table=[]
# 图片有效解码，尺寸检查。
from PIL import Image
for p in v.joinpath('attachments').glob('C4.*-原图-*.png'):
 im=Image.open(p);im.load();assert min(im.size)>150
checks.append(('image_count',len(list(v.joinpath('attachments').glob('C4.*-原图-*.png')))))
report={'phase':'final' if '--final' in sys.argv else 'staging','errors':errors,'checks':checks}
name='复制后校验.json' if '--final' in sys.argv else '暂存校验.json'
(r/name).write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'phase':report['phase'],'files':len(files),'errors':errors},ensure_ascii=False,indent=2))
assert not errors
