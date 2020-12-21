lst = []

def push(x):
    if len(lst) < 5 :
        lst.append(x)
    else:
        print("over flow")

def pop():
    if len(lst) > 0 :
        del lst[(len(lst))-1]
        return True

while True :
    print(lst)
    d = input(">>")
    if d == "push" :
        x = int(input(">>"))
        push(x)
    elif d == "pop" :
        pop()
    elif d == "quick":
        break