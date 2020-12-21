def append_Num(infile, outfile):
    infile = open(infile, "r")
    outfile = open(outfile, "w")
    cnt = 1
    for s in infile:
        result = "{}: {}".format(cnt, s)
        outfile.write(result)
        cnt += 1

    infile.close()
    outfile.close()

infile = input("파일명을 입력하시오: ")
outfile = input("저장할 파일명을 입력하시오: ")

append_Num(infile, outfile)