#작은것을 골라 자리를 계속 바꾼다.
import random

class SelectSorting:
    def __init__(self,list):
        self.n = int(input(">>"))
        self.list = list
    def m_list(self,n,list):
        for i in range(n):
            a = random.randrange(1,101)
            list.append(a)
        self.list = list

    def select(self,x):
        for j in range(len(x)-1):
            min = j
            for i in range(j, len(x)):
                if((x)[min] > (x)[i]):
                    min = i
            x[min], x[j] = x[j], x[min]
        return self.list

result = SelectSorting(list = [])
result.m_list(n = result.n, list = result.list)
print(result.select(x = result.list))