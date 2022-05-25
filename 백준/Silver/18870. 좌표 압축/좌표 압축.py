import sys

n = int(sys.stdin.readline().rstrip())

xlist = list(map(int, sys.stdin.readline().split()))
y = list(set(xlist))
y.sort()
dic = {y[i]: i for i in range(len(y))}
for x in xlist:
    print(dic[x], end=" ")
