import sys

n, m = map(int, sys.stdin.readline().split())
nlist = set([sys.stdin.readline().rstrip() for _ in range(n)])
mlist = set([sys.stdin.readline().rstrip() for _ in range(m)])


clist = sorted(list(nlist & mlist))

print(len(clist))
for c in clist:
    print(c)
