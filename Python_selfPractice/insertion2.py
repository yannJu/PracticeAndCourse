lst = []
import random
n = int(input(">>"))

for i in range(n):
    a = random.randrange(1,101)
    lst.append(a)

for i in range(1,n):

    space = lst[i]
    j = i-1
    while (space< lst[j]) and (j >= 0):
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = space

print(lst)