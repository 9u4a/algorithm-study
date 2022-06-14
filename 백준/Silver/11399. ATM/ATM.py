import sys

n = int(sys.stdin.readline().rstrip())

nlist = sorted(list(map(int, sys.stdin.readline().split())))
clist = []
count = 0
for i in range(n):
    count += nlist[i]
    clist.append(count)

print(sum(clist))

