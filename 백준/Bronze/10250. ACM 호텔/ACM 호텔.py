import sys

a = int(sys.stdin.readline().rstrip())

for _ in range(a):
    h, w, n = map(int, sys.stdin.readline().split())
    fnum = 1
    bnum = 1
    for i in range(1, n):
        fnum += 1
        if i % h == 0:
            bnum += 1
            fnum = 1
    if fnum / 10 >= 1 and bnum / 10 >= 1:
        print(str(fnum)+str(bnum))
    elif fnum / 10 < 1 and bnum / 10 >= 1:
        print(str(fnum) + str(bnum))
    else:
        print(str(fnum)+str(0)+str(bnum))