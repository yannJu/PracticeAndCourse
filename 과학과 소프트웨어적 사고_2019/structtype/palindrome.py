word = input("문자열을 입력하시오: ")
check = False

for c in range(len(word)):
    for cm in range(len(word) - 1, -1, -1):
        if word[c] != word[cm]:
            check = True
            break
    if check:
        break

if check == False:
    print("회문입니다.")