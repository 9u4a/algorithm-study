import sys

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))
print(max(nlist) * min(nlist))
