from HW7_studentClass import *
friends = []

f = open("friendsfile.txt", "r")
s = f.readlines()
for friend_str in s:
    s = friend_str.split()
    friends.append((s[0], int(s[1])))

while True:
    print("============")
    print("1.친구 리스트 출력")
    print("2.친구 추가")
    print("3.친구 삭제")
    print("4.이름 변경")
    print("5.번호 변경")
    print("9.종료")

    menu = int(input("메뉴를 선택하시오:"))
    if menu == 1:
        print(friends)

    elif menu == 2:
        name = input("이름을 입력하시오:")
        age = input("나이를 입력하시오:")
        phone = input("번호를 빈칸과 - 없이 입력하시오:")
        id = input("학번을 입력하시오:")
        group = input("동아리명을 입력하시오.(없으면 X입력하시오):")
        major = input("전공을 입력하시오:")
        st = Student(name, age, phone, id, group, major)
        friends.append((name,phone))

    elif menu == 3:
        cnt = len(friends)
        del_name = input("삭제하고 싶은 이름을 입력하시오:")
        for nameidx in friends:
            if del_name == nameidx[0]:
                friends.remove(nameidx)
                break
        #이름이 발견되지 않은 경우 -> 처음 lst의 길이와 변화가 없는 경우
        if len(friends) == cnt:
            print("이름이 발견되지 않았음")

    elif menu == 4:
        old_name = input("변경하고 싶은 기존 이름을 입력하시오:")
        for friend_name in friends:
            if old_name == friend_name[0]:
                index = friends.index(friend_name)
                new_name = input("새로운 이름을 입력하시오:")
                friends[index] = (new_name, friend_name[1])
                break
        else:
            print("이름이 발견되지 않았음")

    elif menu == 5:
        old_phone = input("변경하고 싶은 번호를 가진 이름을 입력하시오:")
        for friend_phone in friends:
            if old_phone == friend_phone[0]:
                index = friends.index(friend_phone)
                new_phone = input("새로운 번호를 입력하시오:")
                friends[index] = (friend_phone[0], new_phone)
                break

    elif menu == 9:
        f = open("friendsfile.txt", "w")
        for each in friends:
            tupStr = each[0] + " " + str(each[1])
            f.write(tupStr + "\n")
        break

    else:
        print("번호를 제대로 입력하세요!!")

        #연주야 gui로 만들자~!!! -연썬

    #아아아아아아아ㅏ아악 치키이이이닌   아아아아아악 치킨이이이익
    #연주안뇽 안뇽 안용 하이
    #빨리 와아아아앙ㅇㅇ아아아아아아앙ㅇ
    #연쥬쓰 연쥬스 쥬스쥬스 자쥬스
    #교수님 사랑해요

