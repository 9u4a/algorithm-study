import sys

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline().rstrip())
count = 0
for a in nlist:
    if a == v:
        count += 1

print(count)