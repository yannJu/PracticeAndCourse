import random

lottoLst = []
while len(lottoLst) < 6:
    lottonum = random.randrange(1, 46)
    if (lottonum not in lottoLst):
        lottoLst.append(lottonum)

print(lottoLst)