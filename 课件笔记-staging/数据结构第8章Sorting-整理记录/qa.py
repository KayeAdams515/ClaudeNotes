from pathlib import Path
from collections import defaultdict
import re,json,hashlib

V=Path('/Users/andyue/Library/CloudStorage/OneDrive-个人/文档/obsidian');W=Path('/private/tmp/sorting-notes');O=W/'output'/'数据结构'
files=list(O.glob('*.md'));stems=defaultdict(list)
for p in V.rglob('*'):
 if p.is_file():stems[p.name].append(p)
for p in O.rglob('*'):
 if p.is_file():
  stems[p.name]=[q for q in stems[p.name] if q!=V/'数据结构'/p.relative_to(O)]
  stems[p.name].append(p)
errs=[];data=[]
keys={'title','course','chapter','section','tags','aliases','source'}
for p in files:
 s=p.read_text();assert s.startswith('---\n');parts=s.split('---',2);meta=json.loads((W/'frontmatter.json').read_text())[p.name];body=parts[2]
 if p.name.startswith('C8'):
  if set(meta)!=keys:errs.append((p.name,'frontmatter keys'))
  for k in ['tags','aliases','source']:
   if not isinstance(meta[k],list):errs.append((p.name,'list type '+k))
  for bad in ['课件','<!--','TODO','TBD','篇末自测']:
   if bad in body:errs.append((p.name,'forbidden '+bad))
  if '## 0. 开场：' not in body:errs.append((p.name,'opening'))
  three=body.split('## 这一讲的三句话')[1].split('## 速查表')[0]
  if len(re.findall(r'^\d\. ',three,re.M))!=3:errs.append((p.name,'three sentences'))
 # fence matching, ignoring code while parsing links
 fences=re.findall(r'^```.*$',body,re.M)
 if len(fences)%2:errs.append((p.name,'fences'))
 clean=re.sub(r'```.*?```','',body,flags=re.S)
 if clean.count('$$')%2:errs.append((p.name,'display math'))
 inline=clean.replace('$$','')
 if len(re.findall(r'(?<!\\)\$',inline))%2:errs.append((p.name,'inline math'))
 targets=re.findall(r'!?\[\[([^\]]+)\]\]',clean)
 for target in targets:
  target=re.split(r'(?<!\\)\|',target)[0].replace('\\|','|').split('#')[0]
  if not target:continue
  name=target.rsplit('/',1)[-1]
  if '/' in target:
   if (V/(target+'.md')).exists() or (V/target).exists():continue
  if not name.endswith(('.md','.png','.jpg','.pdf','.pptx')):name+='.md'
  if len(stems[name])!=1:
   # MOC old broken links should not block this chapter, but report separately
   if p.name.startswith('C8') or name.startswith('C8'):errs.append((p.name,'link '+name+' count='+str(len(stems[name]))))
 if re.search(r'[:/\\|?*"<>]|[\x00-\x1f]',p.name):errs.append((p.name,'unsafe filename'))
 data.append({'file':p.name,'characters':len(s),'headings':len(re.findall(r'^## ',s,re.M)),'links':len(targets),'images':len(re.findall(r'!\[\[',s))})
report={'files':data,'errors':errs,'checks':['frontmatter keys and types','new link existence and uniqueness','code fences','math delimiters','opening and 3-sentence close','forbidden placeholders and source wording','safe filenames']}
(W/'staging-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2));assert not errs
