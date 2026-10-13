import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
LW=2.0
def seg(ax,x0,y0,x1,y1,c='k',ls='-'):
    ax.plot([x0,x1],[y0,y1],c=c,lw=LW,solid_capstyle='round',ls=ls,zorder=2)
def ar(ax,x0,y0,x1,y1):
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),
        arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
def box(ax,cx,cy,w,h,txt,fs=16):
    ax.add_patch(Rectangle((cx-w/2,cy-h/2),w,h,fill=True,fc='#e8f0fb',ec='k',lw=1.8,zorder=4))
    ax.text(cx,cy,txt,ha='center',va='center',zorder=5,fontsize=fs)
def node(ax,cx,cy,r=0.30):
    ax.add_patch(Circle((cx,cy),r,fill=True,fc='#fdeee0',ec='k',lw=1.8,zorder=4))
    ax.text(cx,cy,'+',ha='center',va='center',zorder=5,fontsize=18)
def lab(ax,x,y,t,fs=13,ha='center'):
    ax.text(x,y,t,ha=ha,va='center',fontsize=fs,zorder=7,
            bbox=dict(fc='white',ec='none',alpha=0.95,pad=1.8))
def dot(ax,x,y):
    ax.add_patch(Circle((x,y),0.055,fc='k',ec='k',zorder=6))

fig,ax=plt.subplots(figsize=(13,6.6))
# delays
box(ax,3.60,6.20,1.20,0.70,'D')
box(ax,5.80,6.20,1.20,0.70,'D')
# adders
A1=(2.00,3.40); A2=(8.60,3.40); AM=(5.80,1.00)
node(ax,*A1); node(ax,*A2); node(ax,*AM)
ax.text(0.05,3.40,r'$x[n]$',fontsize=16,va='center')
ax.text(9.90,3.40,r'$y[n]$',fontsize=16,va='center')
# forward: x -> A1 -> A2
ar(ax,0.62,3.40,1.68,3.40)
ar(ax,2.32,3.40,8.28,3.40)
lab(ax,2.75,3.74,r'$b_0=2$',ha='left')
# tap w[n] -> D1
dot(ax,3.60,3.40)
seg(ax,3.60,3.40,3.60,5.83); ar(ax,3.60,5.83,3.60,5.84)
ax.annotate('',xy=(3.60,5.86),xytext=(3.60,3.40),
            arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
# D1 -> D2
seg(ax,4.20,6.20,5.18,6.20)
ax.annotate('',xy=(5.19,6.20),xytext=(4.20,6.20),
            arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
# b1 tap (w[n-1]) -> A1
dot(ax,4.70,6.20)
seg(ax,4.70,6.20,4.70,4.90); seg(ax,4.70,4.90,2.00,4.90); ar(ax,2.00,4.90,2.00,3.72)
lab(ax,3.35,4.62,r'$b_1=-3$')
# w[n-2] tap -> AM  (tap on the w[n-1]->w[n-2] path, not through the box)
dot(ax,5.80,6.20)
seg(ax,5.80,6.20,5.80,5.60); seg(ax,5.80,5.60,6.40,5.60); ar(ax,6.40,5.60,6.40,2.50)
seg(ax,6.40,2.50,5.80,2.50); ar(ax,5.80,2.50,5.80,1.32)
# a1 feedback: tap y wire -> AM
dot(ax,7.70,3.40)
seg(ax,7.70,3.40,7.70,1.00); ar(ax,7.70,1.00,6.13,1.00)
lab(ax,7.95,2.10,r'$a_1=5$',ha='left')
# a2 feedback: tap y wire -> A2 top
dot(ax,9.00,3.40)
seg(ax,9.00,3.40,9.00,7.10); seg(ax,9.00,7.10,8.60,7.10); ar(ax,8.60,7.10,8.60,3.72)
lab(ax,7.30,7.12,r'$a_2=-6$')
# AM -> A2
seg(ax,5.80,1.30,5.80,2.45); ar(ax,5.80,2.45,8.32,3.22)
ax.set_xlim(-0.25,10.4); ax.set_ylim(0.45,7.6); ax.axis('off')
ax.set_title('Standard Direct Form II   $w[n]=x[n]+5w[n-1]-6w[n-2]$ ,   $y[n]=2w[n]-3w[n-1]$',fontsize=15)
plt.tight_layout(); plt.savefig('df2_standard.png',dpi=170,bbox_inches='tight'); plt.close()
print('ok')
