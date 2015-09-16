#fileName = "greenjoa.txt"
#파일 입출력
#파일 입력
'''
with open(fileName,"w+") as myfile:
    myfile.write("201011245 김민주\n")
    myfile.write("201011246 박민주\n")
    myfile.write("201011247 홍민주\n")
    myfile.write("201011248 이민주\n")
'''
#파일 출력
'''
with open(fileName,"r") as myfile:
    content = myfile.read()
    print(content)
'''
#파일 한줄 씩 출력
'''
with open(fileName,"r") as myfile:
    while True :
        content = myfile.readline()
        if not content :
            break
        print(content,end='')
'''
#내가 해던거
'''
fileName = "파일입출력예제1.txt"
with open(fileName,"r") as myfile:
    monicafileName = "Monica.txt"
    monicafie = open(monicafileName,"w")
    for content in myfile:
        (role,etc) = content.split(":")
        if role == "Monica":
            monicafie.write(role+": "+etc+"\n")
'''
#교수님이 하신거
'''
fileName = "파일입출력예제1.txt"
monicafileName = "Monica.txt"
with open(fileName,"r") as myfile,open(monicafileName,"w") as monicafile:
    for content in myfile:
        (role,etc) = content.split(":")
        if role == "Monica":
            monicafile.write(role+": "+etc+"\n")
'''
#리스트에 저장
'''
fileName = "파일입출력예제2.txt"
role_list=[]
with open(fileName,"r") as myfile:
    for content in myfile:
        (role,etc) = content.split(":",1)
        role_list.append(role)
print(role_list)
'''
import pickle
fileName = "파일입출력예제2.txt"
fileName2 = "pickle.txt"
role_list=[]
with open(fileName,"r") as myfile,open(fileName2,"wb") as pic:
    for content in myfile:
        (role,etc) = content.split(":",1)
        role_list.append(role)
    pickle.dump(role_list,pic)
with open(fileName2,"rb") as pic:
    result = pickle.load(pic)
    print(result)