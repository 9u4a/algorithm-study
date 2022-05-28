from bisect import bisect_left, bisect_right
import sys

n = int(sys.stdin.readline().rstrip())
nlist = sorted(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().split()))


def solve(listx, x):
    return bisect_right(listx, x) - bisect_left(listx, x)


for i in mlist:
    print(solve(nlist, i), end=" ")
