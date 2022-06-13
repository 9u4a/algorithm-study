import sys

n, m = map(int, sys.stdin.readline().split())
alist = []
blist = []

for a in range(n):
    alist.append(list(map(int, sys.stdin.readline().split())))

for b in range(n):
    blist.append(list(map(int, sys.stdin.readline().split())))


for a in range(n):
    for b in range(m):
        print(alist[a][b] + blist[a][b], end=" ")
    print()

