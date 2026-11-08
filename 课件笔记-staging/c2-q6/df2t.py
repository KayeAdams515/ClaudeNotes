import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.lines import Line2D
BLUE='#1450c8'; RED='#cc1f1f'; LW=2.1
def seg(ax,x0,y0,x1,y1,c=BLUE):
    ax.plot([x0,x1],[y0,y1],c=c,lw=LW,solid_capstyle='round',zorder=2)
def ar(ax,x0,y0,x1,y1,c=BLUE):
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),
        arrowprops=dict(arrowstyle='-|>',color=c,lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
def box(ax,cx,cy,w,h,txt,fs=16):
    ax.add_patch(Rectangle((cx-w/2,cy-h/2),w,h,fill=True,fc='#e8f0fb',ec='k',lw=1.8,zorder=4))
    ax.text(cx,cy,txt,ha='center',va='center',zorder=5,fontsize=fs)
def node(ax,cx,cy,r=0.30):
    ax.add_patch(Circle((cx,cy),r,fill=True,fc='#fdeee0',ec='k',lw=1.8,zorder=4))
    ax.text(cx,cy,'+',ha='center',va='center',zorder=5,fontsize=18)
def lab(ax,x,y,t,fs=13,c=BLUE,ha='center'):
    ax.text(x,y,t,ha=ha,va='center',fontsize=fs,zorder=7,color=c,
            bbox=dict(fc='white',ec='none',alpha=0.95,pad=1.8))
def dot(ax,x,y):
    ax.add_patch(Circle((x,y),0.055,fc='k',ec='k',zorder=6))

fig,ax=plt.subplots(figsize=(13.5,7.4))
# ---- input-side delay chain: x[n] -> D -> x[n-1]
box(ax,3.60,6.10,1.20,0.70,'D')
# adders:  A1 = x-side summer (black/hand-drawn),  A2 = output-side summer
A1=(5.80,3.20); A2=(8.90,3.20); A3=(6.60,0.80)
node(ax,*A1); node(ax,*A2); node(ax,*A3)
ax.text(0.15,3.20,r'$x[n]$',fontsize=16,va='center')
ax.text(10.15,3.20,r'$y[n]$',fontsize=16,va='center')
# ===== feedforward (blue) =====
dot(ax,2.00,3.20)
seg(ax,0.70,3.20,5.48,3.20,BLUE)
lab(ax,2.35,3.52,r'$b_0=2$',ha='left')
# x[n] -> D -> x[n-1] -> b1 path
ar(ax,2.00,3.20,2.00,5.75,BLUE)
ar(ax,4.20,6.10,4.90,6.10,BLUE)
dot(ax,4.55,6.10)
seg(ax,4.55,6.10,4.55,4.60,BLUE); ar(ax,4.55,4.60,5.50,3.36,BLUE)
lab(ax,3.15,5.90,'x[n]',fs=12)
lab(ax,5.05,5.95,'x[n-1]',fs=12)
lab(ax,4.85,4.90,r'$b_1=-3$',ha='left')
# ===== feedback (red) =====
# a1 = 5 : output y -> A1
dot(ax,9.70,3.20)
seg(ax,9.70,3.20,9.70,7.30,RED); seg(ax,9.70,7.30,6.10,7.30,RED); ar(ax,6.10,7.30,6.10,3.52,RED)
lab(ax,8.00,7.34,r'$a_1=5$',c=RED)
# a2 = -6 : y delayed twice -> A3
dot(ax,8.20,3.20)
seg(ax,8.20,3.20,8.20,0.20,RED); seg(ax,8.20,0.20,6.95,0.20,RED); ar(ax,6.95,0.20,6.90,0.62,RED)
lab(ax,7.55,0.24,r'$a_2=-6$',c=RED)
# A1 -> A2
ar(ax,6.12,3.20,8.58,3.20,BLUE)
# A3 -> A2
ar(ax,6.90,0.95,9.05,3.06,RED)
ax.set_xlim(-0.05,10.6); ax.set_ylim(-0.25,7.65); ax.axis('off')
h=[Line2D([0],[0],color=BLUE,lw=3,label='feedforward  $b_0,b_1$'),
   Line2D([0],[0],color=RED,lw=3,label='feedback  $a_1,a_2$')]
ax.legend(handles=h,loc='lower left',fontsize=13,framealpha=0.95)
ax.set_title('Transposed structure — mathematically equivalent, but NOT the requested Direct Form II',fontsize=15)
plt.tight_layout(); plt.savefig('df2_transposed.png',dpi=170,bbox_inches='tight'); plt.close()
print('ok')
