import sys

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()
m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().split()))


def solve(listx, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        if listx[mid] == x:
            return 1
        elif listx[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in mlist:
    print(solve(nlist, i, 0, n - 1), end=" ")
