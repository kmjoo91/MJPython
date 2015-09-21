class Movie:
    '''영화 클래스입니다'''
    title="greenjoa"
    director="greenjoa"
    scenario="greenjoa"
    count=0
    def __init__(self, title,director):
        self.title=title
        self.director=director
        print(self.title+"이 생성됩니다.")
        Movie.count+=1

    def showinfo(self):
        print(self.title+" "+self.director+" "+self.scenario)

    def __del__(self):
        print(self.title+"이 소멸됩니다.")
        Movie.count-=1

    @staticmethod
    def showcount():
        print(Movie.count)
    @classmethod
    def c_showcount(cls):
        print(cls.count)
#class 기본
'''
movie1=Movie("암살","류승완")
movie2=Movie("임살","류승범")
movie3=Movie("엄살","류종빈")
movie4=Movie("염살","류철헌")

print(type(movie4))
movie4=movie3
movie4.showinfo()
movie4.director="류원진"
movie3.showinfo()
movie1.actor = "전지현"

movie1.showinfo()
movie2.showinfo()
print(movie1.actor)
movie3.showinfo()
movie3.scenario="bluejoa"
movie3.showinfo()
movie3.__class__.scenario="joa"

movie1.showinfo()

print(movie1.__doc__)

print(id(movie3))
print(id(movie4))
'''

#static method, class method
m1=Movie("m1","m1")
print(m1.count)
m2=Movie("m2","m2")
print(m2.count)
m1.count=3
print(id(m1.count))
print(id(m2.count))
Movie.showcount()
Movie.c_showcount()
m1.c_showcount()