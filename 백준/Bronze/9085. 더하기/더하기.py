import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    nlist = list(map(int, sys.stdin.readline().split()))
    print(sum(nlist))
