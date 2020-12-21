infile = input("파일명을 입력하시오: ")
dic = dict()

f = open(infile, "r")
line = f.readlines()

for s in line:
    for x in s.rstrip():
        if x not in dic:
            dic[x] = 1

        else:
            dic[x] += 1

print(dic)
f.close()