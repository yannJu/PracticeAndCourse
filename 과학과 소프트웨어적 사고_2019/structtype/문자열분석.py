word = input("문자열을 입력하시오: ")

dic = {'digits' : 0, 'spaces' : 0, 'alphas' : 0}

for w in word:
    if w.isdigit():
        dic['digits'] += 1

    elif w == " ":
        dic['spaces'] += 1

    elif w.isalpha():
        dic['alphas'] += 1

print(dic)