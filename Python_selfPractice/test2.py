import random

lst = []

for i in range(10):
    a = random.randrange(1,300)
    lst.append(a)

max = lst[0]
sml = lst[1]

for i in lst:
    if i > max:
        max = i
    if i < sml:
        sml = i

print(lst)
print(max)
print(sml)