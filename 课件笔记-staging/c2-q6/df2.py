import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
LW=1.8
def seg(ax,x0,y0,x1,y1,c='k'):
    ax.plot([x0,x1],[y0,y1],c=c,lw=LW,solid_capstyle='round',zorder=2)
def ar(ax,x0,y0,x1,y1,c='k'):
    ax.annotate('',xy=(x1,y1),xytext=(x0,y0),
        arrowprops=dict(arrowstyle='-|>',color=c,lw=LW,shrinkA=0,shrinkB=0),zorder=2)
def box(ax,cx,cy,w,h,txt,fc='#e8f0fb',fs=15):
    ax.add_patch(Rectangle((cx-w/2,cy-h/2),w,h,fill=True,fc=fc,ec='k',lw=1.7,zorder=4))
    ax.text(cx,cy,txt,ha='center',va='center',zorder=5,fontsize=fs)
def node(ax,cx,cy,r=0.30,fc='#fdeee0'):
    ax.add_patch(Circle((cx,cy),r,fill=True,fc=fc,ec='k',lw=1.7,zorder=4))
    ax.text(cx,cy,'+',ha='center',va='center',zorder=5,fontsize=18)
def lab(ax,x,y,t,fs=13):
    ax.text(x,y,t,ha='center',va='center',fontsize=fs,zorder=6,
            bbox=dict(fc='white',ec='none',alpha=0.95,pad=1.5))

# ---------- (A) STANDARD Direct Form II ----------
fig,ax=plt.subplots(figsize=(12,5.2))
box(ax,3.35,3.35,1.15,0.62,'D'); box(ax,5.45,3.35,1.15,0.62,'D')
node(ax,2.50,2.25); node(ax,7.30,2.25); node(ax,5.00,0.85)
ax.text(0.28,2.25,r'$x[n]$',fontsize=15,va='center')
ax.text(8.55,2.25,r'$y[n]$',fontsize=15,va='center')
ar(ax,0.75,2.25,2.20,2.25)
seg(ax,2.80,2.25,7.00,2.25); ar(ax,7.60,2.25,8.35,2.25)
lab(ax,3.06,2.57,r'$b_0=2$')
seg(ax,2.50,2.55,2.50,3.35); ar(ax,2.50,3.35,2.22,3.35)
seg(ax,3.925,3.35,3.45,3.35); ar(ax,3.45,3.35,4.875,3.35)
lab(ax,2.05,1.62,r'$b_1=-3$')
seg(ax,2.78,3.35,2.78,1.82); seg(ax,2.78,1.82,2.50,1.82); ar(ax,2.50,1.82,2.28,2.05)
seg(ax,5.75,2.55,5.75,1.22)
lab(ax,6.28,0.42,r'$a_1=5$')
seg(ax,7.30,1.95,7.30,0.52); ar(ax,7.30,0.52,5.34,0.80)
lab(ax,6.42,3.36,r'$a_2=-6$')
seg(ax,7.30,2.55,7.30,3.35); seg(ax,7.30,3.35,6.62,3.35)
seg(ax,6.62,3.35,6.62,2.22); ar(ax,6.62,2.22,7.00,2.22)
seg(ax,5.00,1.15,5.00,1.92); ar(ax,5.00,1.92,7.00,2.16)
ax.set_xlim(0,9.2); ax.set_ylim(0.15,4.0); ax.axis('off')
ax.set_title('(A)  Direct Form II  —  standard drawing, one delay chain in the middle',fontsize=14)
plt.tight_layout(); plt.savefig('df2_standard.png',dpi=170,bbox_inches='tight'); plt.close()

# ---------- (B) TRANSPOSED (what the student drew) ----------
fig,ax=plt.subplots(figsize=(12,5.6))
box(ax,5.00,1.62,1.15,0.62,'D'); box(ax,5.00,0.48,1.15,0.62,'D')
node(ax,6.20,3.45); node(ax,3.00,2.80); node(ax,7.40,2.80)
ax.text(1.90,3.45,r'$x[n]$',fontsize=15,va='center')
ax.text(2.05,2.80,r'$y[n]$',fontsize=15,va='center')
ax.text(0.55,2.80,r'$y[n]$',fontsize=15,va='center')
ar(ax,2.45,3.45,5.90,3.45)
lab(ax,4.55,3.78,r'$b_0=2$')
seg(ax,4.15,3.45,4.15,3.02); ar(ax,4.15,3.02,3.32,2.92)
lab(ax,3.72,3.14,r'$b_1=-3$')
lab(ax,6.62,2.36,r'$a_1=5$')
seg(ax,6.20,3.15,6.20,2.28); ar(ax,6.20,2.28,3.32,2.70)
lab(ax,6.95,1.52,r'$a_2=-6$')
seg(ax,5.575,0.48,5.575,0.16); seg(ax,5.575,0.16,7.10,0.16); ar(ax,7.10,0.16,7.10,0.98)
seg(ax,4.425,1.62,4.425,0.95); ar(ax,4.425,0.95,4.35,0.82)
seg(ax,6.50,2.80,4.45,2.80); ar(ax,4.45,2.80,2.72,2.80)
seg(ax,4.425,1.31,4.425,1.20)
seg(ax,5.575,1.62,5.70,1.62)
seg(ax,7.70,2.80,8.20,2.80)
ax.set_xlim(0.1,8.5); ax.set_ylim(-0.15,4.05); ax.axis('off')
ax.set_title('(B)  Transposed structure  —  same equation, NOT the standard Direct Form II',fontsize=14)
plt.tight_layout(); plt.savefig('df2_transposed.png',dpi=170,bbox_inches='tight'); plt.close()
print('done')
