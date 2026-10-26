from pathlib import Path
import re,sys,json
import subprocess
root=Path('/Users/andyue/Library/CloudStorage/OneDrive-个人/文档/obsidian')
stage=Path('/private/tmp/discrete-c8-1/vault')
base=root if '--final' in sys.argv else stage
names=['C8.1 递推关系的应用 Applications of Recurrence Relations.md','C8 高级计数技巧 Advanced Counting Techniques MOC.md','C6 计数 Counting MOC.md','C6.6 生成排列与组合 Generating Permutations and Combinations.md']
files=[p for p in root.rglob('*') if p.is_file() and not any(x in p.parts for x in ['课件笔记-staging','.git','.obsidian','作业归档-staging'])]
files += list(stage.rglob('*')) if base==stage else []
known={p.name for p in files};known|={p.stem for p in files if p.suffix=='.md'}
results=[]
expected={'title','course','chapter','section','tags','aliases','source'}
for name in names:
 p=base/'离散数学'/name;t=p.read_text()
 assert t.startswith('---\n')
 fm,body=t[4:].split('\n---',1);props=json.loads(subprocess.check_output(['ruby','-rpsych','-rjson','-e','puts JSON.generate(Psych.safe_load(STDIN.read))'],input=fm.encode()))
 assert set(props)==expected,(name,set(props))
 assert all(isinstance(props[k],str) for k in expected-{'tags','aliases'})
 assert all(isinstance(props[k],list) for k in ['tags','aliases'])
 keys=re.findall(r'^([a-zA-Z]+):',fm,re.M);assert len(keys)==len(set(keys))
 assert not re.search(r'[:/\\|?*"<>\x00-\x1f]',name)
 assert body.count('```')%2==0
 clean=re.sub(r'```.*?```','',body,flags=re.S)
 if name.startswith('C8'):
  assert '课件' not in re.sub(r'`[^`]*`','',clean) and '自测' not in clean
  assert not re.search(r'TODO|TBD|PLACEHOLDER|待填|待补充',clean)
  assert len(re.findall(r'(?m)^\$\$\s*$',clean))%2==0
  nomath=re.sub(r'\$\$.*?\$\$','',clean,flags=re.S)
  assert len(re.findall(r'(?<!\\)\$',nomath))%2==0
  for i,line in enumerate(clean.splitlines(),1):
   assert len(re.findall(r'(?<!\\)\$',line))%2==0 or line.strip()=='$$',(name,i,line)
  missing=[]
  for target in re.findall(r'!?\[\[([^\]]+)\]\]',clean):
   target=target.replace('\\|','|').split('|')[0].split('#')[0]
   if target and target not in known: missing.append(target)
  assert not missing,(name,missing)
  for line in body.splitlines():
   if line.startswith('|'):assert not re.search(r'\[\[[^\]]*(?<!\\)\|',line),(name,line)
 results.append({'file':name,'frontmatter':'pass','fences':'pass','new_links_and_math':'pass' if name.startswith('C8') else 'existing body preserved; new navigation checked separately'})
# Only one final-course image with this name. Staging is intentionally excluded.
img='C8.1-讲座时间轴与相容前驱.png'
if base==root:assert len([p for p in files if p.name==img])==1
else:assert (stage/'离散数学'/'attachments'/img).exists() and not [p for p in files if p.name==img and stage not in p.parents]
for name in names[2:]:
 t=(base/'离散数学'/name).read_text()
 assert '[[C8.1 递推关系的应用 Applications of Recurrence Relations]]' in t
 assert '[[C8 高级计数技巧 Advanced Counting Techniques MOC]]' in t
print(json.dumps({'location':str(base),'checks':results,'image_unique':'pass','new_navigation':'pass'},ensure_ascii=False,indent=2))
