import os
import sys
#sys예제
'''
print(sys.path)
os.system("Python test.py a b c")
'''
#pickle예제
'''
class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name," : ",self.age)

stu = Student("홍길동","25")
stu.show()

import pickle
f = open("test.txt",'wb')
stu2 = 0
pickle.dump(stu,f)
f.close()

f = open("test.txt",'rb')
stu2 = pickle.load(f)
f.close()
stu2.show()
'''
#os예제
print(os.environ)
print(os.getcwd())
f = os.popen("dir")
print(f.read())

os.chdir("../")

print(os.getcwd())
#파일 복사 예제
for (path,dir,files) in os.walk('.'):
    for filename in files:
        temp = filename.split(".")
        filetype = temp[len(temp)-1]
        if filetype == "txt" and path != ".\sample":
            if not os.path.exists(".\sample"):
                os.mkdir("sample")
            import shutil
            shutil.copy(path+"\\"+filename ,".\sample")
