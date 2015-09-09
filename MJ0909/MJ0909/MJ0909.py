#dictionary
'''
a = {'name':'pey','phone':'01099993323','birth':'1118'}
b=list(a.keys())
print(b)
print(a)
a.clear()
print(a)

movie = {'홍길동':{'베테랑':'5.0','암살':'4.5'},'고길동':{'베테랑':'4.5','암살':'5.0'}}
print(movie)
print(movie['홍길동']['암살'])#= movie.get('홍길동').get('암살')
'''
#if문
'''
answer = input("Would you like express shipping??").lower()
if answer == "yes" :
    print("That will be an extra $ 10")
'''
#for문
'''
a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
'''
#for문 예제 및 리스트안에 for문
'''
for i in range(1,10):
    for j in range(1,10):
        print("{0:d}*{1:d}={2:d} ".format(i,j,i*j),end="")
    print()

result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)
'''
#turtle
import turtle
'''
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(90)
'''
'''
nSides =5
for steps in range(nSides):
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides):
        turtle.forward(50)
        turtle.right(360/nSides)
'''
prompt="""
1.Add
2.Del
3.List
4.Quit

enter:"""
number = 0
while number !=4:
    print(prompt,end="")
    number = int(input())