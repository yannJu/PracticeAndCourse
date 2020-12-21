lst = []

def inqueue (x):
    if len(lst) < 5 :
        lst.append(x)
        return True
    else :
        print("over flow")

def outqueue ():
    if len(lst) > 0 :
        del lst[0]
        return True
    else:
        print("under flow")


while True:
    print(lst)
    c = input(">>")
    if c == "inqueue" :
        n = int(input(">>"))
        inqueue(n)
    elif c == "outqueue" :
        outqueue()
    elif c == "quick" :
        break