#List예제
'''
data=['a','b','c',['abcd','efg']]
print(data[0])
print(data[-1])
print(data[-1][1])
b=[1,2,3]
c=['life','is','too','short']
'''
#List에 삽입 삭제
'''
guest=['a','b','c','d']
guest[0]='greenjoa'
print(guest)
guest[1]=['greenjoa1','greenjoa2']#1번 인덱스에 List를 삽입
print(guest)
guest[1:2]=['greenjoa1','greenjoa2']#1번 인덱스에 그린조아1 2번 인덱스에 그린조아2
print(guest)

guest.insert(2,'e')
guest.append('greenjoa2')
print(guest)

guest.remove('c')
guest[1:2]=[]
del guest[0]
print(guest.index('c'))
'''
#List예제
'''
data=['greenjoa1','greenjoa2','greenjoa3']
data.insert(data.index('greenjoa1')+1,'pw1')
data.insert(data.index('greenjoa2')+1,'pw2')
data.insert(data.index('greenjoa3')+1,'pw3')
print(data)
'''
#for문
'''
guests=['a','b','c',['d','e']]
for steps in guests:
    for guest in steps:
        print(guest)
for steps in guests:
    if isinstance(steps,list):
        for guest in steps:
            print(guest)
    else :
        print(steps)
data2 = range(4)
print(data2)
'''
'''
data=['1','3','5','2','4','6']
data.sort()
print(data)
data.reverse()
print(data)
top3 = data[0:3]
print(top3)
'''
score=[87,62,63,45,90]
num = score.pop()
print(num)
num = score.pop(2)
print(num)
num=score.count(63)
print(num)
score.extend([50,60])
print(score)