import sys

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))

print(nlist.count(n))
