class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def disc(self):
        print(self.name)
        print(self.age)

p1 = Person('홍길동',22)
p2 = Person('이연주',20)
p1.disc()
p2.disc()

class PersonIn:
    def __init__(self):
        self.name = input("이름:")
        self.age = input("나이:")
    def disco(self):
        print(self.name)
        print(self.age)

p1 = PersonIn()
p2 = PersonIn()
p1.disco()
p2.disco()

class PersonLst:
    def __init__(self):
        self.name = input("이름:")
        self.age = input("나이:")
    def discOo(self):
        print(self.name)
        print(self.age)

lst = []
x = int(input("몇 명을 출력하시겠습니까?"))

for i in range(x):
    lst.append(PersonLst())

for i in range(len(lst)):
    lst[i].discOo()


