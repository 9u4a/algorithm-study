import sys

n, k = map(int, sys.stdin.readline().split())
nlist = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
count = 0

for a in range(n-1, -1, -1):
    if k >= nlist[a]:
        count += k // nlist[a]
        k %= nlist[a]

print(count)
