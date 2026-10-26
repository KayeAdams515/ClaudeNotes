from pathlib import Path
import numpy as np, json

W=Path(__file__).resolve().parent
checks=[]
def check(name,error,tolerance,detail=''):
    error=float(error)
    checks.append(dict(name=name,error=error,tolerance=tolerance,detail=detail,passed=error<=tolerance))
    assert error<=tolerance,(name,error,tolerance)

# 用定义与解析式交叉计算四种矩形，不把公式再代回同一公式。
N,M=17,3
k=np.arange(N); ns=np.arange(-M,M+1)
a_direct=np.exp(-2j*np.pi*k[:,None]*ns/N).sum(axis=1)/N
theta=2*np.pi*k/N
a_formula=np.empty(N);a_formula[0]=(2*M+1)/N
a_formula[1:]=np.sin((2*M+1)*theta[1:]/2)/np.sin(theta[1:]/2)/N
check('DTFS 矩形：有限和与正弦比',np.max(abs(a_direct-a_formula)),2e-14)
omega=np.array([-2*np.pi,-1.2,0,.7,2*np.pi]);X_direct=np.exp(-1j*omega[:,None]*ns).sum(axis=1)
X_formula=np.array([(2*M+1) if abs(np.sin(v/2))<1e-12 else np.sin((2*M+1)*v/2)/np.sin(v/2) for v in omega])
check('DTFT 矩形：含可去零点',np.max(abs(X_direct-X_formula)),2e-14)
T,T1=5.,.7;t=np.linspace(-T1,T1,100001);O=np.array([-4.,-1.,0.,2.3]);
X_quad=np.trapezoid(np.exp(-1j*O[:,None]*t),t,axis=1)
X_exact=2*T1*np.sinc(O*T1/np.pi)
check('CTFT 矩形：数值积分与 Sa',np.max(abs(X_quad-X_exact)),3e-10,'梯形积分步长 1.4e-5，按二阶误差设限')
kk=np.arange(-8,9);Of=2*np.pi*kk/T
ctfs_quad=np.trapezoid(np.exp(-1j*Of[:,None]*t),t,axis=1)/T
ctfs_exact=2*T1/T*np.sinc(Of*T1/np.pi)
check('CTFS 矩形：一个周期投影',np.max(abs(ctfs_quad-ctfs_exact)),4e-10)

# 辛普森法复核过冲常数，避开缺失的 SciPy 依赖。
v=np.linspace(0,np.pi,200001);f=np.sinc(v/np.pi);h=v[1]-v[0]
Si=h/3*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-2:2].sum())
G=Si/np.pi-.5
check('吉布斯渐近常数',abs(G-.0894898722360836),2e-13,repr(float(G)))

rng=np.random.default_rng(6);x=rng.normal(size=17)+1j*rng.normal(size=17)
A=np.fft.fft(x)/len(x)
check('DTFS 精确综合',np.max(abs(np.fft.ifft(A*len(x))-x)),3e-15)
check('DTFS 帕塞瓦尔',abs(np.mean(abs(x)**2)-np.sum(abs(A)**2)),3e-15)
shift=4;phase=np.exp(-2j*np.pi*k*shift/17)
check('DTFS 时移',np.max(abs(np.fft.fft(np.roll(x,shift))/17-A*phase)),3e-14)
mod=3
check('DTFS 频移',np.max(abs(np.fft.fft(x*np.exp(2j*np.pi*mod*k/17))/17-np.roll(A,mod))),3e-14)
y=rng.normal(size=17);B=np.fft.fft(y)/17
conv=np.array([sum(x[r]*y[(n-r)%17] for r in range(17)) for n in range(17)])
check('DTFS 未归一化周期卷积的 N 因子',np.max(abs(np.fft.fft(conv)/17-17*A*B)),2e-14)
prod_coeff=np.array([sum(A[r]*B[(q-r)%17] for r in range(17)) for q in range(17)])
check('DTFS 相乘的系数周期卷积',np.max(abs(np.fft.fft(x*y)/17-prod_coeff)),3e-15)
check('DTFS 对偶的 1/N 与反转',np.max(abs(np.fft.fft(A)/17-x[(-k)%17]/17)),3e-16)
expanded=np.zeros(34,dtype=complex);expanded[::2]=x
check('DTFS 插零的 1/m 因子',np.max(abs(np.fft.fft(expanded)/34-np.tile(A,2)/2)),3e-15)

image=rng.normal(size=(20,24));F=np.fft.fft2(image);p,q=3,7
U,V=np.meshgrid(np.arange(20),np.arange(24),indexing='ij')
G2=np.fft.fft2(np.roll(image,(p,q),axis=(0,1)))
check('二维循环平移相位',np.max(abs(G2-F*np.exp(-2j*np.pi*(U*p/20+V*q/24)))),5e-12)

# 直接构造离散周期方波的低通截断，验证不能概括为“离散无过冲”。
square=np.zeros(64);square[16:48]=1
freq=np.fft.fftfreq(64)*64;mask=abs(freq)<=9
reconstruction=np.fft.ifft(np.fft.fft(square)*mask).real
overshoot=float(reconstruction.max()-1)
assert overshoot>.06
checks.append(dict(name='离散截断方波的反例',overshoot=overshoot,passed=True,detail='64 点周期序列，仅保留 -9 至 9 次谐波'))

L=64;n=np.arange(L);win=.5-.5*np.cos(2*np.pi*n/L)
check('50% 重叠的周期 Hann 窗叠加',np.max(abs(win+np.roll(win,L//2)-1)),5e-16)
(W/'math_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(json.dumps({'passed':len(checks),'Gibbs_constant':float(G),'discrete_overshoot_counterexample':overshoot},ensure_ascii=False))
