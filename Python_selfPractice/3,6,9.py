# 1-100까지의 숫자를 출력하는데, 3,6,9가 있으면 *을 출력

def change(x):
    print(x.replace("3","*").replace("6","*").replace("9","*"))

for i in range(1,101):
    if "3" in str(i) or "6" in str(i) or "9"  in str(i):
        change(str(i))
    else:
        print(i)
