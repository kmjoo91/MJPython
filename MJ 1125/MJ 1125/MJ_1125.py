import numpy as np
from matplotlib import pyplot as plt

#기본
print(np.eye((3)))#단위행렬
print(np.diag(np.array([1,2,3,4])))#대각행렬
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print(data.T)#전치행렬
print(data)#T를 해도 본래값은 안변함
data = np.array([1,2,3,4])
print(data.T)
data = np.array([[1,2,3,4]])
print(data.T)
data = np.arange(10)
print(data)
data = np.arange(10,1,-1)
print(data)
data = np.arange(10,1,-1)[:, np.newaxis]
print(data)
data = np.arange(2,8,dtype = np.float)
print(data)
data = np.arange(35).reshape(5,7)
print(data)
data = np.linspace(1., 4., 6) #start, end, num-points
print(data)
data = np.linspace(1., 4., 6, endpoint=False)
print(data)

#random
data = np.random.rand(4)
print(data)
data = np.random.randn(16).reshape(4,4)
print(data)

#파일 읽어오기
data = np.loadtxt('data.txt')
year, hares, lynxes, carrots = data.T
print(data)
#plt.plot(year, hares, year, lynxes, year, carrots)
#plt.show()
#인덱스 & 슬라이싱
data = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(data[0])
print(data[-1])
print(data[0:2])
print(data[1:4:2])
print(data[::-1])
print(data[2,0])
x = np.arange(10,1,-1)
print(x[np.array([3,3,1,8])])
print(x[np.array([[1,1],[2,3]])])
y=np.arange(35).reshape(5,7)
print(y[np.array([0,2,4])])
b = y>20
print(y[b])
data = np.arange(36).reshape(6,6)
print(data)
#mask
mask=np.array(np.array([1,0,1,0,0,1],dtype=bool))
print(data[mask, 2])#data[행,열]
mask1=np.array([0,1,2,3,4])
mask2=np.array([1,2,3,4,5])
print(data[mask1,mask2])
print(data[3:,np.array([0,2,5])])