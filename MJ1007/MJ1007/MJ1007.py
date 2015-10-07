#내장함수
'''
#dir enumerate
list1 = [1,2,3,4,5]
print(dir(list1))

data = list(enumerate(list1))
print(data)


#filter
def evenNum(a):
    return a%2 ==0
print(list(filter(evenNum,list1)))

#id
b= 3
print(id(b))
print(id(3))

#lambda
print(list(filter(lambda a : a%2==0,list1)))

#list
a = [1,2,3]
b = list(a)
c = a
d = [1,2,3]

print(id(a))
print(id(b))
print(id(c))
print(id(d))

#map
print(list(map(lambda a:a*2,[0,1,2,3,4])))


#repr
HI=str("hi")

print(eval(repr("hi".upper())))
print(eval(str("hi".upper())))


#sort
list2=[2,3,1,5,2,6,7,2,9,10]

print(sorted(list2))

print(repr("hi".upper()))
print(str("hi".upper()))
'''
quiz = {'홍길동':[80,70,60,92],
             '김길동':[24,35,18,10],
             '고길동':[10,20,8,5]}
print(quiz)
for items in quiz:
    quiz.get(items).sort()
    print(items+":",quiz.get(items))
temp = quiz.copy();
quiz_key = sorted(quiz)
print(quiz_key)
quiz.clear();
for item in quiz_key:
    print(item)
    quiz[item] = temp.get(item)

print(quiz)