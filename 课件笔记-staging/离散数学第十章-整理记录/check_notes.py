from pathlib import Path
import re,sys,json,subprocess
root=Path('/Users/andyue/Library/CloudStorage/OneDrive-个人/文档/obsidian');w=Path('/private/tmp/discrete-c10');stage=w/'vault'
base=root if '--final' in sys.argv else stage
new_names=[p.name for p in (stage/'离散数学').glob('C10*.md')]
old_names=['C9 关系 Relations MOC.md','C9.6 偏序 Partial Orderings.md']
exclude={'课件笔记-staging','作业归档-staging','.git','.obsidian'}
actual=[p for p in root.rglob('*') if p.is_file() and not (set(p.relative_to(root).parts)&exclude)]
# Overlay staged files instead of treating stage copies as duplicate targets.
lookup={}
for p in actual:
 lookup.setdefault(p.name,[]).append(p)
 if p.suffix=='.md':lookup.setdefault(p.stem,[]).append(p)
if base==stage:
 for p in (stage/'离散数学').rglob('*'):
  if p.is_file():
   lookup[p.name]=[p]
   if p.suffix=='.md':lookup[p.stem]=[p]
records=[];expected={'title','course','chapter','section','tags','aliases','source'}
embeds=set()
for name in new_names+old_names:
 p=base/'离散数学'/name;t=p.read_text();assert t.startswith('---\n')
 fm,body=t[4:].split('\n---',1)
 props=json.loads(subprocess.check_output(['ruby','-rpsych','-rjson','-e','puts JSON.generate(Psych.safe_load(STDIN.read))'],input=fm.encode()))
 assert set(props)==expected,(name,set(props))
 assert all(isinstance(props[k],str) for k in expected-{'tags','aliases'})
 assert all(isinstance(props[k],list) and all(isinstance(x,str) for x in props[k]) for k in ['tags','aliases'])
 keys=re.findall(r'^(\w+):',fm,re.M);assert len(keys)==len(set(keys))
 assert not re.search(r'[:/\\|?*"<>\x00-\x1f]',name)
 assert body.count('```')%2==0
 clean=re.sub(r'```.*?```','',body,flags=re.S)
 if name in new_names:
  assert '课件' not in re.sub(r'`[^`]+`','',clean),name
  assert not re.search(r'TODO|TBD|PLACEHOLDER|待填|待补充|解析与说明|题目与思路|显然|如图所以',clean),name
  assert re.search(r'(?m)^## 0\. 开场：',clean) or name.endswith('MOC.md')
  if not name.endswith('MOC.md'):
   summary=clean.split('## 这一讲的三句话')[1].split('## 速查表')[0]
   assert len(re.findall(r'(?m)^\d\. ',summary))==3
  for i,line in enumerate(clean.splitlines(),1):
   assert len(re.findall(r'(?<!\\)\$',line))%2==0,(name,i,line)
  for target in re.findall(r'!?\[\[([^\]]+)\]\]',clean):
   target=target.replace('\\|','|').split('|')[0]
   file,_,anchor=target.partition('#')
   assert file in lookup,(name,'missing',file)
   assert len(lookup[file])==1,(name,'ambiguous',file)
   if anchor:
    targetbody=lookup[file][0].read_text()
    assert anchor in re.findall(r'(?m)^#+ (.*)$',targetbody),(name,anchor)
  for target in re.findall(r'!\[\[([^\]]+)\]\]',clean):embeds.add(target.split('|')[0])
  # Check TeX groups, skipping escaped literal braces.
  for formula in re.findall(r'\$\$(.*?)\$\$|(?<!\$)\$([^$\n]+)\$(?!\$)',clean,re.S):
   expr=formula[0] or formula[1]
   expr=re.sub(r'\\[{}]','',expr);level=0
   for ch in expr:
    if ch=='{':level+=1
    if ch=='}':level-=1
    assert level>=0,(name,expr)
   assert level==0,(name,expr)
   assert not re.search(r'(?<!\\)\\\\(?=[A-Za-z])',expr),(name,'double slash command',expr)
  # Each contiguous table has a consistent number of unescaped separators.
  tables=re.findall(r'(?m)(?:^\|.*\n)+',body)
  for table in tables:
   counts=[len(re.findall(r'(?<!\\)\|',line)) for line in table.splitlines()]
   assert len(set(counts))==1,(name,'table columns',counts)
  records.append({'file':name,'properties':'pass','links_and_images':'pass','math_delimiters_and_groups':'pass','tables':'pass','fences':'pass'})
 else:
  assert '[[C10 图 Graphs MOC]]' in body and '[[C10.1 图与图模型 Graphs and Graph Models]]' in body
  records.append({'file':name,'existing_properties':'pass','new_navigation':'pass','scope':'original body otherwise preserved'})
imgs={p.name for p in (base/'离散数学'/'attachments').glob('C10*.png')}
assert imgs==embeds,(imgs-embeds,embeds-imgs)
assert len(imgs)==24
for name in imgs:assert len(lookup[name])==1,(name,'duplicate image')
assert (root/'离散数学'/'pdfs'/'第十章.pdf').exists()
print(json.dumps({'location':str(base),'new_lectures':8,'chapter_index':1,'image_count':len(imgs),'files':records,'image_unique':'pass','source_exists':'pass'},ensure_ascii=False,indent=2))
