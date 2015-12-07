import numpy as np
from matplotlib import pyplot as plt
#기본 그래프
'''
plt.plot([1,2,3,4])
plt.show()
'''
#그래프 속성 주기
'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16],"bo-")
plt.show()
'''
#속성 각각 주기
'''
t = np.arange(0., 5., 0.2) 
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') 
'''
#그래프에 범례주기 (삼각함수)
'''
X = np.arange(0.,1.1,0.1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
plt.plot(X, np.cos(X), color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, np.sin(X), color="red", linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left')
plt.show()
'''
#x, y 축 바꾸기
'''
# Set x limits 
plt.xlim(-4.0, 4.0) 
# Set x ticks 
plt.xticks(np.linspace(-4, 4, 9, endpoint=True)) 
# Set y limits 
plt.ylim(-1.0, 1.0) 
# Set y ticks 
plt.yticks(np.linspace(-1, 1, 5, endpoint=True)) 
plt.show()
'''
#subplot
'''
def f(t): 
    return np.exp(-t) * np.cos(2*np.pi*t) 
t1 = np.arange(0.0, 5.0, 0.1) 
t2 = np.arange(0.0, 5.0, 0.02) 
plt.figure(1) 
plt.subplot(211) 
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') 
plt.subplot(212) 
plt.plot(t2, np.cos(2*np.pi*t2), 'r--') 
plt.show()
'''
#축을 tick marks를 기준으로 이동
'''
def f(t): 
    return np.exp(-t) * np.cos(2*np.pi*t) 
t2 = np.arange(-5.0, 5.0, 0.02) 
plt.plot(t2, np.cos(2*np.pi*t2), 'r--') 
ax = plt.gca() # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
'''
#분포도 그리기
'''
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)#포인터의 s=크기정보 c=색상정보
plt.xlim(-1.5, 1.5)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())
plt.show()
'''
#contour plots(분포도, 등고선)
'''
* contourf : draw filled contours
* contour : draw contour lines
-. X, Y : 좌표
-. f(X,Y) : contour plot
-. 8 : 주어진 레벨까지 선택
'''
'''
def f(x,y): 
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2) 
n = 256 
x = np.linspace(-3, 3, n) 
y = np.linspace(-3, 3, n) 
X,Y = np.meshgrid(x, y) 
plt.axes([0.025, 0.025, 0.95, 0.95]) 
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot) 
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5) 
plt.clabel(C, inline=1, fontsize=10) 
plt.xticks(()) 
plt.yticks(()) 
plt.show()
'''
#imshow
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)
n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(Z, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.92)
plt.xticks(())
plt.yticks(())
plt.show()