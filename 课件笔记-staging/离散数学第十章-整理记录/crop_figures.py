from pathlib import Path
from PIL import Image,ImageDraw
import subprocess,json
w=Path('/private/tmp/discrete-c10');out=w/'vault'/'离散数学'/'attachments'
specs=[
('C10.3-原图-同构不变量两例',33,(.03,.17,.95,.30)),
('C10.4-原图-连通与分量',42,(.17,.17,.90,.32)),
('C10.4-原图-圈与同构两例',47,(.30,.58,.84,.715)),
('C10.5-原图-欧拉有向无向六例',54,(.03,.59,.92,.72)),
('C10.5-原图-欧拉路径三例',58,(.18,.17,.93,.272)),
('C10.5-原图-十二面体环游',59,(.30,.17,.90,.295)),
('C10.5-原图-哈密顿路径三例',59,(.30,.445,.89,.565)),
('C10.1-原图-模块依赖与程序先序',7,(.17,.565,.88,.72)),
('C10.2-原图-邻域与度两例',12,(.18,.43,.84,.55)),
('C10.2-原图-员工与任务匹配',19,(.19,.17,.84,.275)),
('C10.4-原图-连通度五例',43,(.315,.405,.79,.71)),
('C10.5-原图-七桥与多重图',53,(.14,.57,.86,.73)),
('C10.5-原图-弯刀欧拉回路',57,(.30,.17,.68,.265)),
('C10.5-原图-旋转编码与Gray码',63,(.17,.155,.90,.48)),
('C10.6-原图-航线三种权重',68,(.15,.17,.89,.555)),
('C10.6-原图-网络三种权重',69,(.03,.17,.80,.48)),
('C10.6-原图-Dijkstra逐步标签',73,(.03,.17,.96,.44)),
('C10.7-原图-K4与Q3的平面表示',79,(.03,.17,.92,.29)),
('C10.7-原图-同胚细分三例',83,(.24,.17,.94,.26)),
('C10.7-原图-K5细分障碍',84,(.17,.17,.88,.295)),
('C10.7-原图-Petersen细分障碍',85,(.14,.17,.91,.30)),
('C10.8-原图-地图与对偶图',87,(.31,.17,.70,.26)),
('C10.8-原图-地图对应的对偶图',87,(.31,.56,.71,.66)),
('C10.8-原图-加边改变色数',89,(.23,.17,.89,.30))]
for n,p,box in specs:
 rendered=w/'read'/f'hi-{p:03}.png'
 if not rendered.exists():
  subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','180','-singlefile','-png',str(w/'source'/'第十章.pdf'),str(rendered.with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 im=Image.open(rendered);width,height=im.size
 im.crop(tuple(int(f*x) for f,x in zip(box,[width,height,width,height]))).save(out/(n+'.png'))
# overview only; individual final assets will also be opened for figure evidence.
for j in range(0,len(specs),6):
 canvas=Image.new('RGB',(1500,1250),'#e3e3e3');d=ImageDraw.Draw(canvas)
 for k,(n,p,b) in enumerate(specs[j:j+6]):
  im=Image.open(out/(n+'.png'));im.thumbnail((730,365));x=k%2*750;y=k//2*415
  canvas.paste(im,(x,y+25));d.text((x+5,y+5),n.split('-原图-')[0]+' / PDF '+str(p),fill='black')
 canvas.save(w/'read'/f'crops-{j//6+1}.jpg',quality=90)
(w/'figure-manifest.json').write_text(json.dumps([{'file':n+'.png','source_physical':p,'printed':p+640,'normalized_box':b,'type':'原图裁切'} for n,p,b in specs],ensure_ascii=False,indent=2))
print('cropped',len(specs))
