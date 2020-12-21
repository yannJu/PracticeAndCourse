word = input("문자열을 입력하시오: ")

lst = word.split()
result = ""

for x in lst:
    result += x[0]

print(result)