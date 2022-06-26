import sys

while True:
    xlist = sorted(list(map(int, sys.stdin.readline().split())))
    if xlist[0] == 0 and xlist[1] == 0 and xlist[2] == 0:
        break
    if xlist[0] ** 2 + xlist[1] ** 2 == xlist[2] ** 2:
        print('right')
    else:
        print('wrong')
