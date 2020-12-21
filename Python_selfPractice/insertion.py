
#삽입정렬 : while
#class화 시키기 -> 버블, 선택

import random

class InsertionSorting():
    def __init__(self,copy,space):
        self.x = int(input(">>"))
        self.list = []
        self.copy = copy
        self.space = space
    def m_list(self,x,list):
        for i in range(x):
            a = random.randrange(1,101)
            list.append(a)
        self.list = list

    def insertion(self,x,space,lst):
        while x < (len(lst)):
            for i in range(0,x):
                if lst[x] < lst[i]:
                    space = lst[x]
                    lst[x] = lst[i]
                    lst[i] = space
            x += 1
        self.copy = x
        self.space = space
        return self.list

result = InsertionSorting(copy = 1, space = 0)
result.m_list(x = result.x, list = result.list)
print(result.insertion(x = result.copy, space = result.space, lst = result.list))