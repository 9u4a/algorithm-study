import sys

n, m = map(int, sys.stdin.readline().split())
nlist = {}

for a in range(n):
    ncount = sys.stdin.readline().rstrip()
    nlist[ncount] = a + 1
    nlist[a + 1] = ncount
for _ in range(m):
    mcount = sys.stdin.readline().rstrip()
    if mcount.isdigit():
        print(nlist[int(mcount)])
    else:
        print(nlist[mcount])
