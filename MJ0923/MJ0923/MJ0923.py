#coding:cp949
#클래스 및 abstarctmethod 예제
'''
from abc import ABCMeta, abstractmethod
class Terran(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
    def attack(self):
        pass

class Tank(Terran):
    def __init__(self, name,damage):
        super().__init__(name)
        self.damage = damage
    def attack(self):
        print("탱크를 쏩니다.")

class Marine(Terran):
    def __init__(self, name,hp):
        super().__init__(name)
        self.hp=hp
    def attack(self):
        print("총을 쏩니다.")

def Attack(terran):
    terran.attack()

t1 = Tank("Tank",0)
t2 = Marine("Tank",100)
tlist=[Tank("tank1",0),Tank("tank2",0),Marine("Marine1",0)]

for item in tlist:
    Attack(item)
'''
class MyList(list):
    name=""
    def __init__(self, name):
        super().__init__([])
        self.name = name
    def __str__(self):
        return self.name+":"+super().__str__()
list1 = MyList("greenjoa")
list1.append(10)
list1.append(50)
list1.append(60)
list1.append(80)
list1.append(100)
print(list1)
print(dir(list1))
