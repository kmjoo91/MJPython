import glob
import os
'''
glob.glob("*")
path = input()
for i in glob.iglob(path):
    print(i)
'''
#파일 트리
'''
ndir = nfile =0
def traverse(dir,depth):
    global ndir,nfile
    for obj in glob.glob(dir+'/*'):
        if depth==0:
            prefix = '|--'
        else:
            prefix = '|'+' '*depth+'|--'
        if os.path.isdir(obj):
            ndir += 1
            print(prefix + os.path.basename(obj))
            traverse(obj,depth+1)
        elif os.path.isfile(obj):
            nfile+=1
            print(prefix+os.path.basename(obj))
        else:
            print(prefix + 'unknwon object',obj)
if __name__ == '__main__':
    traverse('..',0)
    print('Wn',ndir,'directories',nfile,'nfiles')
'''
'''
import tempfile
with tempfile.TemporaryFile('w+') as fp:
    fp.delete = False
    fp.write("Hello world!")
    fp.seek(0)
    data = fp.read()
    print(data)
    print(fp.name)
    print(os.path.exists(fp.name))
print(os.path.exists(fp.name))
'''
#time 예제
'''
import time
time1 = time.time()
time.sleep(3)
time2 = time.time()
spendtime = time2-time1
print(spendtime)
print(time.strftime("%B %dth %A %I:%M",time.localtime()))
print(time.strftime("%Y-%m-%d %I:%M",time.localtime()))
time1 = time.ctime(12345678910)
print(time1)
t = time.strptime(time1)
print(t)
'''
#calendar 예제
'''
import calendar
print(calendar.calendar(2000))
print(calendar.prcal(2000))

print(calendar.monthrange(1991,6))
'''
import random
rand_arr = random.sample(range(100),10)
print(rand_arr)
random.shuffle(rand_arr)
print(rand_arr)
print(random.choice(rand_arr))
data = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
datalist=[]
for val, cnt in data:
    for i in range(cnt):
        datalist.append(val)
print(datalist)

population = [val for val,cnt in data for i in range(cnt)]
print(population)

import webbrowser 
url = "http://google.com"
webbrowser.open_new_tab(url) 
webbrowser.open_new(url)