import sys

n = int(sys.stdin.readline().rstrip())
listn = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
listm = list(map(int, sys.stdin.readline().split()))


def solve(listx, t, start, end):
    while start <= end:
        mid = (start + end) // 2
        if listx[mid] == t:
            return 1
        elif listx[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in listm:
    print(solve(listn, i, 0, n - 1))