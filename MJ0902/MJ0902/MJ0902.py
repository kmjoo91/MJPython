#print("Hellow orld")
#정수출력
'''
print('TestNumber %d'%8)
print("Test Number {1:d}{0:d}{0:d}".format(8,9))
# string
salary = input("Please enter your salary : ")
bonus = input("Please enter your bonus : ")
paycheck1 = salary + bonus
#형변환 1
paycheck2 = int(salary) + int(bonus)
#형변환 2
salary1 = int(input("Please enter your salary1 : "))
bonus1 = int(input("Please enter your bonus1 : "))
paycheck3 = int(salary1) + int(bonus1)
print(paycheck1)
print(paycheck2)
print(+paycheck3)
# type check
print(type(paycheck3))
'''
#문자열
'''
name="greenjoa"
print(name[0])
print(name[-1])
print(name[0:3])
'''
#문자열 수정
'''
a="pithon"
#a[1]='y' 잘못된방법
#[인덱스부터:인덱스전까지]
a=a[:1]+'y'+a[2:]
print(a)
'''
#문자열정렬
'''
Teststr = 'five'
print('test %10s'%Teststr)
print('test %-10s'%Teststr)
'''
#문자열 함수
upper = input("대문자").upper()
lower = input("소문자").lower()
print("대문자 : "+upper)
print("소문자 : "+lower)
