import sys

n, m = map(int, sys.stdin.readline().split())
nlist = [sys.stdin.readline().rstrip() for _ in range(n)]
mlist = [sys.stdin.readline().rstrip() for _ in range(m)]
count = 0

for mcount in mlist:
    if mcount in nlist:
        count += 1
print(count)