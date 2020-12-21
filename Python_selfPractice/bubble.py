import random

class BubbleSorting:
    def __init__(self,n,list):
        self.n = n
        self.lst = list
    def m_list(self,n,lst):
        for i in range(n):
            a = random.randrange(1,101)
            lst.append(a)
        self.lst = lst

    def bubble(self,lst):
        for j in range(len(lst)):
            for i in range(len(lst)-1):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
        return lst

n = int(input(">>"))

result = BubbleSorting(n = n, list = [])
result.m_list(n = result.n,lst = result.lst)

print(result.bubble(lst = result.lst))