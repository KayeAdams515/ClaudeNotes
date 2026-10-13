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

fig,ax=plt.subplots(figsize=(13,6.8))
box(ax,3.90,6.30,1.20,0.70,'D')
box(ax,6.10,6.30,1.20,0.70,'D')
A1=(2.20,3.40); A2=(8.90,3.40); AM=(6.10,1.00)
node(ax,*A1); node(ax,*A2); node(ax,*AM)
ax.text(0.20,3.40,r'$x[n]$',fontsize=16,va='center')
ax.text(10.15,3.40,r'$y[n]$',fontsize=16,va='center')
# x -> A1
ar(ax,0.72,3.40,1.88,3.40)
# A1 -> A2
ar(ax,2.52,3.40,8.58,3.40)
lab(ax,2.90,3.72,r'$b_0=2$',ha='left')
# w[n] tap at 3.90 up into D1
dot(ax,3.90,3.40)
seg(ax,3.90,3.40,3.90,5.93)
ax.annotate('',xy=(3.90,5.96),xytext=(3.90,3.40),
            arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
# D1 -> D2
seg(ax,4.50,6.30,5.48,6.30)
ax.annotate('',xy=(5.49,6.30),xytext=(4.50,6.30),
            arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
# b1 tap : w[n-1] (between D1 and D2) -> A1 from the left
dot(ax,5.00,6.30)
seg(ax,5.00,6.30,5.00,5.10); seg(ax,5.00,5.10,1.10,5.10)
seg(ax,1.10,5.10,1.10,3.40); ar(ax,1.10,3.40,1.88,3.40)
lab(ax,3.35,4.83,r'$b_1=-3$')
# w[n-2] : output of D2 -> AM  (down the right, then to AM top)
dot(ax,6.70,6.30)
seg(ax,6.70,6.30,6.70,2.60); seg(ax,6.70,2.60,5.60,2.60); ar(ax,5.60,2.60,5.60,1.32)
# a1 feedback : tap y wire -> AM right
dot(ax,8.00,3.40)
seg(ax,8.00,3.40,8.00,0.60); seg(ax,8.00,0.60,6.45,0.60); ar(ax,6.45,0.60,6.42,1.00)
lab(ax,8.22,2.05,r'$a_1=5$',ha='left')
# a2 feedback : tap y wire -> A2 top
dot(ax,9.30,3.40)
seg(ax,9.30,3.40,9.30,7.30); seg(ax,9.30,7.30,8.90,7.30); ar(ax,8.90,7.30,8.90,3.72)
lab(ax,7.62,7.32,r'$a_2=-6$')
# AM -> A2
seg(ax,6.10,1.30,6.10,2.30); ar(ax,6.10,2.30,8.62,3.22)
ax.set_xlim(0.0,10.6); ax.set_ylim(0.10,7.75); ax.axis('off')
ax.set_title('Standard Direct Form II      $w[n]=x[n]+5w[n-1]-6w[n-2]$ ,     $y[n]=2w[n]-3w[n-1]$',fontsize=15)
plt.tight_layout(); plt.savefig('df2_standard.png',dpi=170,bbox_inches='tight'); plt.close()
print('ok')
