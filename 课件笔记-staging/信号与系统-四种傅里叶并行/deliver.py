from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).resolve().parent;ROOT=W.parents[1];C=ROOT/'信号与系统'
title='C3–5 四种傅里叶表示并行讲义'
source=W/(title+'.md');target=C/(title+'.md')
assert source.exists() and not target.exists()
index=C/'信号与系统 MOC.md';backup=W/'信号与系统 MOC.md.before.bak'
assert index.read_bytes()==backup.read_bytes(),'用户修改了索引，请先合并差异'
old=C/'transcript/第十三节课.txt';new=C/'transcript/第十三节课-已合并.txt'
assert old.exists() and not new.exists()
mapping=json.loads((W/'attachment_map.json').read_text())
for name in mapping.values():assert not (C/'attachments'/name).exists()
report={'new_note':str(target),'note_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'transcript_old':str(old),'transcript_new':str(new),'transcript_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'original_notes_unchanged':16,'reused_figures':48,'disambiguated_figures':11}
for name in mapping.values():shutil.move(str(W/'attachments'/name),C/'attachments'/name)
shutil.move(str(source),target)
shutil.copy2(W/'信号与系统 MOC.md.staged',index)
old.rename(new)
assert hashlib.sha256(target.read_bytes()).hexdigest()==report['note_sha256']
assert hashlib.sha256(new.read_bytes()).hexdigest()==report['transcript_sha256']
(W/'delivery.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
