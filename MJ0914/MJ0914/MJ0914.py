#배포패키지만들기
import os
print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
print(os.getcwd())
#os.system("python setup.py sdist")
os.system("python setup.py install")
#함수 예제
'''
def sum_and_mul(a,b):
   return a+b,a*b
#answer = sum_and_mul(10,30)
sum,mul = sum_and_mul(10,30)
print(sum,mul)
'''
#모듈만들기
'''
import printData

movie=['홍길동',['베테랑',['류승완','황정민','유아인']],
       '고길동',['앤트맨','베테랑'],
       '김길동',['협녀','암살']]
printData.printData(movie)
'''
