from cmath import exp,sin,cos,sinh,cosh,tan,log
from math import pi,sqrt,factorial
from pathlib import Path
import json
checks=[]
def quad(f,a,b,n=8192):
 h=(b-a)/n
 return h/3*(f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))+2*sum(f(a+2*k*h) for k in range(1,n//2)))
def chk(label,actual,expected):
 err=abs(actual-expected);tol=2e-7*(1+abs(expected))
 checks.append(dict(label=label,actual=str(actual),expected=str(expected),error=err,tolerance=tol,passed=err<tol))
 assert err<tol,(label,actual,expected,err,tol)
def circle(f,center=0,R=1,a=0,b=2*pi):
 return quad(lambda t:f(center+R*exp(1j*t))*1j*R*exp(1j*t),a,b)
def line(f,a,b):return quad(lambda t:f(a+(b-a)*t)*(b-a),0,1)
chk('42例：指数',quad(lambda t:exp(1j*t),0,pi/4),1/sqrt(2)+1j*(1-1/sqrt(2)))
chk('42-2a',quad(lambda t:(1+1j*t)**2,0,1),2/3+1j)
chk('42-2b',quad(lambda t:(1/t-1j)**2,1,2),-.5-1j*log(4))
chk('42-2c',quad(lambda t:exp(2j*t),0,pi/6),sqrt(3)/4+.25j)
chk('42-2d Re(z)>0',quad(lambda t:exp(-(2+1j)*t),0,24),1/(2+1j))
for m,n in [(0,0),(3,2),(-2,5),(4,4)]:chk(f'42-3 m={m},n={n}',quad(lambda t:exp(1j*m*t)*exp(-1j*n*t),0,2*pi),2*pi if m==n else 0)
chk('42-4 实部',quad(lambda t:exp(t)*cos(t),0,pi),-(1+exp(pi))/2)
chk('42-4 虚部',quad(lambda t:exp(t)*sin(t),0,pi),(1+exp(pi))/2)
f=lambda z:z.imag-z.real-3j*z.real**2
chk('45折线',line(f,0,1j)+line(f,1j,1+1j),(1-1j)/2)
chk('45直线',line(f,0,1+1j),1-1j)
for a,b,want in [(0,pi,-4+2j*pi),(pi,2*pi,4+2j*pi),(0,2*pi,4j*pi)]:chk('46-1 '+str(a),circle(lambda z:(z+2)/z,R=2,a=a,b=b),want)
chk('46-2a',circle(lambda z:z-1,center=1,a=pi,b=2*pi),0)
chk('46-2b',line(lambda z:z-1,0,2),0)
f=lambda z:pi*exp(pi*z.conjugate())
chk('46-3 共轭正方形',sum(line(f,a,b) for a,b in [(0,1),(1,1+1j),(1+1j,1j),(1j,0)]),4*(exp(pi)-1))
chk('46-4 分段三次曲线',quad(lambda x:1+3j*x*x,-1,0)+quad(lambda x:4*x**3*(1+3j*x*x),0,1),2+3j)
chk('46例平方根',quad(lambda t:sqrt(3)*exp(.5j*t)*3j*exp(1j*t),0,pi),-2*sqrt(3)*(1+1j))
chk('46例复幂',quad(lambda t:exp((-1+1j)*1j*t)*1j*exp(1j*t),-pi,pi),2j*sinh(pi))
chk('46-6',quad(lambda t:exp(-t)*1j*exp(1j*t),0,pi),-(1+exp(-pi))/2*(1-1j))
chk('46-7',quad(lambda t:exp((-1-2j)*1j*t)*1j*exp(1j*t),0,pi/2),.5j*(exp(pi)-1))
for a in [1/4,-1.5,3]:
 R=2
 chk(f'46-8 a={a}',quad(lambda t:exp((a-1)*(log(R)+1j*t))*1j*R*exp(1j*t),-pi,pi),2j*R**a*sin(a*pi)/a)
chk('46-9b 分支改变',quad(lambda t:exp(-.75j*t)*1j*exp(1j*t),0,2*pi),-4+4j)
for m,n in [(-1,0),(2,3),(2,2),(-3,2)]:chk(f'46-10 {m},{n}',circle(lambda z:z**m*z.conjugate()**n),2j*pi if n==m+1 else 0)
chk('46-11角参',circle(lambda z:z.conjugate(),R=2,a=-pi/2,b=pi/2),4j*pi)
for n in [-3,-1,0,1,4]:chk(f'46-13 n={n}',circle(lambda z:(z-(1+1j))**(n-1),center=1+1j,R=2),2j*pi if n==0 else 0)
chk('48例指数',line(lambda z:exp(pi*z),1j,.5j),(1+1j)/pi)
chk('48例平方根上',quad(lambda t:sqrt(3)*exp(.5j*t)*3j*exp(1j*t),pi,0),2*sqrt(3)*(1+1j))
chk('49-4平方根下',quad(lambda t:sqrt(3)*exp(.5j*t)*3j*exp(1j*t),pi,2*pi),2*sqrt(3)*(-1+1j))
chk('49-2a',line(lambda z:z*z,0,1+1j),2/3*(-1+1j))
chk('49-2b',line(lambda z:cos(z/2),0,pi+2j),exp(1)+exp(-1))
chk('49-2c',line(lambda z:(z-2)**3,1,3),0)
for b in [.3,1,2]:chk(f'53-4 Gaussian b={b}',quad(lambda x:exp(-x*x)*cos(2*b*x),0,10),sqrt(pi)/2*exp(-b*b))
chk('53-6三段平方根',2/3+quad(lambda t:exp(.5j*t)*1j*exp(1j*t),0,pi)+2j/3,0)
chk('53-7面积单位圆',circle(lambda z:z.conjugate())/(2j),pi)
chk('54例',circle(lambda z:cos(z)/(z*(z*z+9))),2j*pi/9)
chk('55例高阶',circle(lambda z:exp(2*z)/z**4),8j*pi/3)
# 四边直接积分，不以柯西公式再次执行同一推导。
def square(f):return sum(line(f,a,b) for a,b in [(-2-2j,2-2j),(2-2j,2+2j),(2+2j,-2+2j),(-2+2j,-2-2j)])
for label,f,ans in [
 ('57-1a',lambda z:exp(-z)/(z-pi*1j/2),2*pi),
 ('57-1b',lambda z:cos(z)/(z*(z*z+8)),1j*pi/4),
 ('57-1c',lambda z:z/(2*z+1),-1j*pi/2),
 ('57-1d',lambda z:cosh(z)/z**4,0),
 ('57-1e x0=.3',lambda z:tan(z/2)/(z-.3)**2,1j*pi/cos(.15)**2)]:chk(label,square(f),ans)
chk('57-2a',circle(lambda z:1/(z*z+4),center=1j,R=2),pi/2)
chk('57-2b',circle(lambda z:1/(z*z+4)**2,center=1j,R=2),pi/16)
chk('57-3内',circle(lambda s:(2*s*s-s-2)/(s-2),R=3),8j*pi)
chk('57-3外',circle(lambda s:(2*s*s-s-2)/(s-4),R=3),0)
chk('57-4内',circle(lambda s:(s**3+2*s)/(s-.2)**3,R=2),6j*pi*.2)
for a in [-2,0,.3,2]:chk(f'57-7 a={a}',quad(lambda t:exp(a*cos(t))*cos(a*sin(t)),0,pi),pi)
for w,h in [(1+2j,.01j),(2-.3j,.02)]:chk('57-9余项恒等式',((w-h)**-2-w**-2)/h-2/w**3,(3*w*h-2*h*h)/((w-h)**2*w**3))
for z,z0 in [(1+2j,.3j),(-2+1j,1.2)]:
 for k in [1,2,5]:chk(f'59-8差幂 k={k}',z**k-z0**k,(z-z0)*sum(z**(k-1-j)*z0**j for j in range(k)))
chk('59-4正弦最大模',abs(sin(pi/2+1j)),cosh(1))
# 原始路径上的密集取样复核估计：取样只用于发现反例，不替代理论证明。
for t in range(1001):
 z=2*exp(1j*pi/2*t/1000)
 assert abs((z-2)/(z**4+1))<=4/15+1e-12
 assert abs((z+4)/(z**3-1))<=6/7+1e-12
 assert abs(1/(z*z-1))<=1/3+1e-12
out=Path(__file__).resolve().parent/'复算结果.json';out.write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(f'{len(checks)} numerical/algebra checks passed; Simpson n=8192, tolerance 2e-7*(1+|expected|).')
