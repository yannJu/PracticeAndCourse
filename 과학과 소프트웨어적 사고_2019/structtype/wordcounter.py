dic = {"B4" : "Before", "TX": "Thanks", "BBL" : "Be Back Later", "BCNU": "Be Seeing You", "HAND": "Have A Nice Day"}

word = input("번역할 문장을 입력하시오: ")
lst = word.split()
result = ""

for i in lst:
    if i in dic:
        result += dic[i] + " "
    else:
        result += i

print(result)