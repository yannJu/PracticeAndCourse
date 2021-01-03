#1년 1/1 == mon, mon % 7 == 1, ..., sun % 7 == 0, 입력된 년도 - 1 까지의 날을 더하고 월 - 1 까지 더한다음 해당월의 1일의 요일을 구하기

def check(year): #윤년판별
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else: return False

def sumY(year): #해당년도 - 1 까지의 날짜를 더함
    sum = 0
    for i in range(1, year):#(q.반복하여 함수를 호출하는 것이 불필요하지 않은가?/ 조건문 내에서 해결하는 것이 더 효율적????)
        if check(i):
            sum += 366
            #print("윤년")
        else: sum += 365
        #print(i, " : ", sum)
    #print(sum)

    return sum

def sumM(year, month): #해달월 - 1 까지의 날짜를 더함
    Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0

    for i in range(1, month):
        sum += Month[i - 1]
        if (i == 2) and check(year) == 1 : sum += 1
        #print(i, " : ", sum)
    #print(sum)

    return sum

def printSc(year, month): #달력출력
    cnt = 1
    crrt = (sumY(year) + sumM(year, month) + 1) % 7
    print("   ", end='')
    if month == 2:
        if (check(year) == 1): max = 29
        else: max = 28
    elif month in [4, 6, 9, 11]:
        max = 30
    else: max = 31

    for i in range(0, crrt):
        print("    ", end='')
        cnt += 1

    for j in range(1, max + 1):
        if (j > 9): print(j, end='  ')
        else: print(j, end='   ')
        if (cnt == 7):
            cnt = 0
            print('\n',end='   ')
            pass
        cnt += 1


#-----------------------Main

print("원하는 년도의 달력을 출력합니다.\n년도를 입력하세요 (e.g 2001) : ")
year = int(input())
print("월을 입력하세요 (1-12) : ")
month = int(input())

print("\n        {}년도 {}월        ".format(year, month))
print("===============================")
print("  SUN MON TUE WED THU FRI SAT")

printSc(year, month)