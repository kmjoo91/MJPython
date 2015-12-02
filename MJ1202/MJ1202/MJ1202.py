import numpy as np
from matplotlib import pyplot as plt
#도시사이 거리구하기
'''
mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
print(distance_array)
'''
#두점 사이 거리구하기
'''
x,y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x**2 + y**2)
print(distance)
plt.pcolor(distance)
plt.colorbar()
plt.show()
'''
#Grid 만들기
'''
x, y = np.ogrid[0:5, 0:5] # grid에 대한 계산을 다루기 유용
#x : (5,1), y : (1,5) #shape을 가짐
print(x)
print(y)
print(x+y)
x, y = np.mgrid[0:5, 0:5]
#x,y : (5,5) #shape을 가짐
print(x)
print(y)
print(x+y)
'''
#ravel함수
'''
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.ravel()) #[1,2,3,4,5,6]
print(a.T)
print(a.T.ravel())
a.shape 
print(a.shape)
b = a.ravel()
print(b) 
b = b.reshape((2, 3))
print(b)
'''
#newaxis
'''
z = np.array([1, 2, 3])
print(z[:, np.newaxis])
print(z[np.newaxis, :])
'''
#사이즈조절
'''
a = np.arange(4) 
print(a)
a.resize((8,))
print(a)
'''
#sorting
'''
a = np.array([[4, 3, 5], [1, 2, 1]])
print(a)
b = np.sort(a, axis=1) #Sorts each row separately!
print(b)
a.sort(axis=1)
print(a)
a = np.array([4, 3, 1, 2])
print(a)
j = np.argsort(a) # sorting with index 
j_max = np.argmax(a) # finding maxima 
j_min = np.argmin(a) # finding minima
print(j)
print(j_max)
print(j_min)
'''
#다항식
'''
p = np.poly1d([3, 2, -1])
print(p(0))
print(p.roots)
print(p.order)
p = np.polynomial.Polynomial([-1, 2, 3])
print(p)
x = np.linspace(0, 1, 20)
print(x)
y = np.cos(x) + 0.3*np.random.rand(20) 
print(y)
p = np.poly1d(np.polyfit(x, y, 3)) 
t = np.linspace(0, 1, 200) 
print(t)
print(p)
plt.plot(x, y, 'o', t, p(t), '-') 
plt.show()
x = np.linspace(-1, 1, 2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x, y, 90)
t = np.linspace(-1, 1, 200)
plt.plot(x, y, 'r.')
plt.plot(t, p(t), 'k-', lw=3)
plt.show()
'''
img = plt.imread('korea.png')
print(img.shape)
print(img.dtype)
subimg = img[96:330,205:435]
plt.imshow(subimg)
plt.show()