import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
LW=2.0
def seg(ax,x0,y0,x1,y1,c='k'):
    ax.plot([x0,x1],[y0,y1],c=c,lw=LW,solid_capstyle='round',zorder=2)
def ar(ax,x0,y0,x1,y1,c='k'):
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),
        arrowprops=dict(arrowstyle='-|>',color=c,lw=LW,shrinkA=0,shrinkB=0,
                        mutation_scale=22),zorder=2)
def box(ax,cx,cy,w,h,txt,fs=15):
    ax.add_patch(Rectangle((cx-w/2,cy-h/2),w,h,fill=True,fc='#e8f0fb',ec='k',lw=1.7,zorder=4))
    ax.text(cx,cy,txt,ha='center',va='center',zorder=5,fontsize=fs)
def node(ax,cx,cy,r=0.30,fc='#fdeee0'):
    ax.add_patch(Circle((cx,cy),r,fill=True,fc=fc,ec='k',lw=1.7,zorder=4))
    ax.text(cx,cy,'+',ha='center',va='center',zorder=5,fontsize=18)
def lab(ax,x,y,t,fs=13,ha='center'):
    ax.text(x,y,t,ha=ha,va='center',fontsize=fs,zorder=6,
            bbox=dict(fc='white',ec='none',alpha=0.95,pad=1.8))
def dot(ax,x,y):
    ax.add_patch(Circle((x,y),0.055,fc='k',ec='k',zorder=6))

# ================= STANDARD DIRECT FORM II =================
fig,ax=plt.subplots(figsize=(12.5,5.4))
A1=(2.30,2.20); A2=(8.40,2.20)
box(ax,3.90,3.45,1.15,0.62,'D'); box(ax,6.10,3.45,1.15,0.62,'D')
node(ax,*A1); node(ax,*A2); node(ax,6.10,0.55)
ax.text(0.15,2.20,r'$x[n]$',fontsize=15,va='center')
ax.text(9.45,2.20,r'$y[n]$',fontsize=15,va='center')
# x -> A1
ar(ax,0.62,2.20,1.98,2.20)
# A1 -> A2 main line  (tap for w[n] at x=3.30)
ar(ax,2.62,2.20,8.08,2.20)
lab(ax,2.98,2.52,r'$b_0=2$',ha='left')
# w[n] -> D1
dot(ax,3.30,2.20)
seg(ax,3.30,2.20,3.30,3.45); ar(ax,3.30,3.45,3.30,3.45)
seg(ax,3.30,3.45,3.30,3.45)
ar(ax,3.30,3.45,3.30,3.45)
seg(ax,3.30,2.20,3.30,3.45)
ar(ax,3.30,3.45,3.30,3.45)
seg(ax,3.30,3.45,3.30,3.45)
ax.annotate('',xy=(3.325,3.45),xytext=(3.30,2.20),
            arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
seg(ax,4.475,3.45,5.52,3.45); ar(ax,5.52,3.45,5.52,3.45)
ax.annotate('',xy=(5.525,3.45),xytext=(4.475,3.45),
            arrowprops=dict(arrowstyle='-|>',color='k',lw=LW,shrinkA=0,shrinkB=0,mutation_scale=22),zorder=3)
# b1 tap from w[n-1]
dot(ax,4.80,3.45)
seg(ax,4.80,3.45,4.80,1.35); seg(ax,4.80,1.35,2.30,1.35); ar(ax,2.30,1.35,2.30,1.88)
lab(ax,4.05,1.10,r'$b_1=-3$')
# a1 feedback from y line down to middle adder
dot(ax,7.60,2.20)
seg(ax,7.60,2.20,7.60,0.55); ar(ax,7.60,0.55,6.42,0.55)
lab(ax,7.85,1.28,r'$a_1=5$',ha='left')
# middle adder -> A2
seg(ax,6.10,0.87,6.10,1.75); ar(ax,6.10,1.75,8.16,2.06)
# a2 feedback from y line up and over to A2 top
dot(ax,8.85,2.20)
seg(ax,8.85,2.20,8.85,3.90); seg(ax,8.85,3.90,8.40,3.90); ar(ax,8.40,3.90,8.40,2.52)
lab(ax,7.10,3.92,r'$a_2=-6$')
# w[n-2] -> middle adder (feedforward)
dot(ax,6.10,3.45)
seg(ax,6.10,3.45,6.10,0.55); ar(ax,6.10,0.55,6.10,0.55)
ax.set_xlim(0,9.9); ax.set_ylim(0.05,4.35); ax.axis('off')
ax.set_title('(A)  Direct Form II — standard drawing (one delay chain, taps fed back to the left adder)',fontsize=14)
plt.tight_layout(); plt.savefig('df2_standard.png',dpi=170,bbox_inches='tight'); plt.close()
print('A ok')
