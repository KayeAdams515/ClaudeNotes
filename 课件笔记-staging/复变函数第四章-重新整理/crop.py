from pathlib import Path
from PIL import Image, ImageDraw
import subprocess,json
r=Path(__file__).resolve().parent
# 坐标单位为 PDF 点，包含图号、坐标标签与箭头。
items=[
('C4.2-原图-无穷振荡光滑弧',11,(35,58,305,177)),
('C4.3-原图-上下半圆同端点',14,(25,199,225,308)),
('C4.3-原图-折线与直线',15,(25,500,245,610)),
('C4.4-原图-线段离原点最近距离',24,(25,497,205,607)),
('C4.5-原图-平方根上下路径',29,(25,492,302,606)),
('C4.5-原图-短线段构造原函数',32,(35,484,272,609)),
('C4.6-原图-方格细分与嵌套',36,(25,304,352,475)),
('C4.6-原图-内部边界抵消',39,(35,422,376,597)),
('C4.7-原图-复连通边界与割线',43,(25,132,312,255)),
('C4.7-原图-闭路变形成小圆',44,(35,425,302,575)),
('C4.7-原图-高斯积分矩形',46,(35,219,250,303)),
('C4.7-原图-无穷自交路径替换',47,(35,58,305,178)),
('C4.8-原图-柯西公式小圆',48,(25,493,265,606)),
('C4.8-原图-内点与边界距离',53,(35,58,350,207)),
('C4.10-原图-邻域链传播',61,(35,503,396,598)),
('C4.10-原图-三角形模的极值',63,(25,206,291,299)),
('C4.10-原图-正弦矩形极值',63,(25,516,302,603)),
]
for name,page,box in items:
 full=r/'read'/f'hi-{page:02d}'
 if not full.with_suffix('.png').exists():
  subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','200','-png','-singlefile',str(r/'source'/'Chapter4.pdf'),str(full)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 im=Image.open(full.with_suffix('.png'));scale=200/72
 im.crop(tuple(round(v*scale) for v in box)).save(r/'vault'/'复变函数'/'attachments'/(name+'.png'))
json.dump(items,open(r/'图片来源.json','w'),ensure_ascii=False,indent=2)
for start in range(0,len(items),6):
 sheet=Image.new('RGB',(1500,1050),'#eeeeee');d=ImageDraw.Draw(sheet)
 for k,(name,page,box) in enumerate(items[start:start+6]):
  im=Image.open(r/'vault'/'复变函数'/'attachments'/(name+'.png'));im.thumbnail((490,460));x=k%3*500;y=k//3*525
  sheet.paste(im,(x,y+35));d.text((x+5,y+8),f'{start+k+1}: PDF {page}',fill='black')
 sheet.save(r/'read'/f'crops-{start:02d}.jpg')
print('17 original figure crops saved')
