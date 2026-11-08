import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
LW=2.0
def seg(ax,x0,y0,x1,y1):
    ax.plot([x0,x1],[y0,y1],c='k',lw=LW,solid_capstyle='round',zorder=2)
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

fig,ax=plt.subplots(figsize=(13,7.0))
box(ax,4.20,6.40,1.20,0.70,'D')
box(ax,6.60,6.40,1.20,0.70,'D')
A1=(2.10,3.40); A2=(9.20,3.40); AM=(5.60,1.00)
node(ax,*A1); node(ax,*A2); node(ax,*AM)
ax.text(0.15,3.40,r'$x[n]$',fontsize=16,va='center')
ax.text(10.45,3.40,r'$y[n]$',fontsize=16,va='center')
# main forward path
ar(ax,0.70,3.40,1.78,3.40)
ar(ax,2.42,3.40,8.88,3.40)
lab(ax,2.80,3.72,r'$b_0=2$',ha='left')
# w[n] -> D1
dot(ax,4.20,3.40)
ax.annotate('',xy=(4.20,6.05),xytext=(4.20,3.40),
            arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
# D1 -> D2
ar(ax,4.80,6.40,6.00,6.40)
# b1 : w[n-1] -> A1  (approach from lower-left)
dot(ax,5.40,6.40)
seg(ax,5.40,6.40,5.40,5.15); seg(ax,5.40,5.15,1.05,5.15)
seg(ax,1.05,5.15,1.05,3.05); ar(ax,1.05,3.05,1.85,3.25)
lab(ax,3.60,4.90,r'$b_1=-3$')
# w[n-2] -> AM (top input)
dot(ax,7.20,6.40)
seg(ax,7.20,6.40,7.20,2.70); seg(ax,7.20,2.70,5.60,2.70); ar(ax,5.60,2.70,5.60,1.32)
# b0*w[n] -> AM (bottom input)
seg(ax,5.60,0.70,5.60,0.72); ar(ax,5.60,0.70,5.60,0.72)
dot(ax,5.60,3.40)
seg(ax,5.60,3.40,5.60,0.70)
# a1 : y -> AM right input
dot(ax,8.30,3.40)
seg(ax,8.30,3.40,8.30,0.60); seg(ax,8.30,0.60,5.94,0.60); ar(ax,5.94,0.60,5.92,1.00)
lab(ax,8.50,2.00,r'$a_1=5$',ha='left')
# a2 : y -> A2 top input
dot(ax,9.65,3.40)
seg(ax,9.65,3.40,9.65,7.40); seg(ax,9.65,7.40,9.20,7.40); ar(ax,9.20,7.40,9.20,3.72)
lab(ax,7.95,7.42,r'$a_2=-6$')
# AM -> A2
seg(ax,5.60,1.30,5.60,2.40); ar(ax,5.60,2.40,8.92,3.22)
ax.set_xlim(-0.05,10.9); ax.set_ylim(0.10,7.85); ax.axis('off')
ax.set_title('Standard Direct Form II      $w[n]=x[n]+5w[n-1]-6w[n-2]$ ,     $y[n]=2w[n]-3w[n-1]$',fontsize=15)
plt.tight_layout(); plt.savefig('df2_standard.png',dpi=170,bbox_inches='tight'); plt.close()
print('ok')
