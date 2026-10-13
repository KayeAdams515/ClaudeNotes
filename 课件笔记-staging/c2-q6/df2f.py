import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
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
# ---- delays on the top:  w[n] -> D1 -> w[n-1] -> D2 -> w[n-2]
box(ax,4.20,6.30,1.20,0.70,'D')
box(ax,6.60,6.30,1.20,0.70,'D')
A1=(2.10,3.20); A2=(9.30,3.20); A3=(5.70,0.80)
node(ax,*A1); node(ax,*A2); node(ax,*A3)
ax.text(0.15,3.20,r'$x[n]$',fontsize=16,va='center')
ax.text(10.55,3.20,r'$y[n]$',fontsize=16,va='center')
# ===== feedforward (blue) =====
ar(ax,0.70,3.20,1.78,3.20,BLUE)
# w[n] : branch up to D1, and forward with b0
dot(ax,3.20,3.20)
ar(ax,3.20,3.20,3.20,5.95,BLUE)
ar(ax,4.80,6.30,6.00,6.30,BLUE)
lab(ax,5.70,6.02,'w[n-1]',fs=12)
lab(ax,3.45,5.10,'w[n]',fs=12)
# b0 w[n] -> A2
ar(ax,3.20,3.20,8.98,3.20,BLUE)
lab(ax,2.55,3.52,r'$b_0=2$',ha='left')
# b1 w[n-1] -> A2   (tap between the two delays)
dot(ax,5.40,6.30)
seg(ax,5.40,6.30,5.40,4.30,BLUE); ar(ax,5.40,4.30,8.98,3.34,BLUE)
lab(ax,6.05,4.52,r'$b_1=-3$',ha='left')
# ===== feedback (red): w[n-1], w[n-2] -> A3 ; A3 -> A2 ; y -> A3 =====
dot(ax,7.20,6.30)
lab(ax,7.72,6.06,'w[n-2]',fs=12)
seg(ax,7.20,6.30,7.20,1.90,RED); seg(ax,7.20,1.90,5.95,1.90,RED); ar(ax,5.95,1.90,5.85,1.10,RED)
seg(ax,5.40,6.30,5.40,6.72,RED); seg(ax,5.40,6.72,5.70,6.72,RED); ar(ax,5.70,6.72,5.70,2.60,RED)
seg(ax,5.70,2.60,5.70,1.10,RED)
lab(ax,4.35,7.00,r'$a_1=5$',c=RED)
# A3 -> A2
ar(ax,5.95,0.95,9.02,3.06,RED)
# y -> A3  (a2 branch, with 1-sample delay implied)
dot(ax,8.45,3.20)
seg(ax,8.45,3.20,8.45,0.20,RED); seg(ax,8.45,0.20,6.05,0.20,RED); ar(ax,6.05,0.20,5.86,0.62,RED)
lab(ax,7.25,0.24,r'$a_2=-6$',c=RED)
ax.set_xlim(-0.05,11.0); ax.set_ylim(-0.25,7.55); ax.axis('off')
# legend
from matplotlib.lines import Line2D
h=[Line2D([0],[0],color=BLUE,lw=3,label='feedforward  $b_0,b_1$  (from $x$ side)'),
   Line2D([0],[0],color=RED,lw=3,label='feedback  $a_1,a_2$  (from $y$ side)')]
ax.legend(handles=h,loc='lower left',fontsize=13,framealpha=0.95)
ax.set_title('Standard Direct Form II      $w[n]=x[n]+5w[n-1]-6w[n-2]$ ,     $y[n]=2w[n]-3w[n-1]$',fontsize=15)
plt.tight_layout(); plt.savefig('df2_standard.png',dpi=170,bbox_inches='tight'); plt.close()
print('ok')
