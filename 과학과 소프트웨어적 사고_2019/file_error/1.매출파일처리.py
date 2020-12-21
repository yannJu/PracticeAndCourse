infilename = input("입력 파일 이름: ")
outfilename = input("출력 파일 이름: ")

sum = 0
cnt = 0
aver = 0

infile = open(infilename, "r")
for f in infile:
    f = f.rstrip()
    sum += int(f)
    cnt += 1

aver = sum / cnt
result = "총매출 = {}, \n평균 일매출 = {}".format(sum, aver)

outfile = open(outfilename, "w")
outfile.write(result)
